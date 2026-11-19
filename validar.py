"""
validar.py — Validador y saneador del dataset de vertex-salvador.

Es el validador de vertex-exilio con cuatro cambios:
  1. Épocas, perspectivas y términos de El Salvador.
  2. Partes interesadas (gobiernos salvadoreño, cubano y de EE. UU., guerrilla, ONG): sus fuentes solo valen como
     postura. La misma vara para todos.
  3. Cifra atribuida: un número que solo sostiene una fuente de postura puede aparecer en la respuesta si la
     MISMA frase lo atribuye ("según la PNC...", "Cristosal registra..."). Si no, es ERROR.
  4. Ejemplos con herramientas: turnos 'assistant' con tool_calls y turnos 'tool' con la respuesta.

Solo librería estándar (Python 3.10+).

Uso (desde E:\\vertex-salvador):
    python validar.py fuentes\\fragmentos_lote1.jsonl --fragmentos
    python validar.py datos\\ejemplos_lote1.jsonl
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

# ---------------------------------------------------------------- configuración

ETAPAS = {f"P0{i}" for i in range(1, 6)} | {f"E{i:02d}" for i in range(1, 16)} | \
         {"T01", "T02", "T03", "T04", "X01", "general"}
TIPOS = {"hecho", "contexto", "perspectivas", "humano", "reformulacion",
         "sin_datos", "conflicto", "multiple", "saludo"}
ESTADOS = {"pendiente", "aprobado", "rechazado"}
PERSPECTIVAS_FUENTE = {"gobierno_salvadoreno", "gobierno_eeuu", "gobierno_cubano", "gobierno_haitiano", "fmln_guerrilla", "ong_ddhh",
                       "academica", "prensa", "organismo_internacional", "enciclopedia", "ninguna"}
# Partes interesadas: lo que dicen es su versión, nunca un hecho por sí solo.
PARTES_INTERESADAS = {"gobierno_salvadoreno", "gobierno_eeuu", "gobierno_cubano", "gobierno_haitiano", "fmln_guerrilla",
                      "ong_ddhh"}

USOS_FUENTE = {"hechos", "postura", "ambos", "pendiente"}
USOS_PARA_HECHOS = {"hechos", "ambos"}
TIPOS_FRAGMENTO = {"hecho", "hecho_atribuido", "postura", "cifra_disputada", "testimonio"}

MIN_PALABRAS = {"saludo": 8, "sin_datos": 50}
MIN_DEFECTO, MAX_PALABRAS = 150, 450
UMBRAL_CASI_DUPLICADO = 0.80

TERMINOS_PROHIBIDOS = [
    "lacra", "lacras", "escoria", "sinverguenza", "sinverguenzas", "ratas", "basura humana",
    "genocida", "genocidio", "heroico", "heroica", "glorioso", "gloriosa", "mesias", "tirano", "tirania",
    "narcodictadura",
]
TERMINOS_DISPUTADOS = [
    "dictadura", "dictador", "regimen", "terrorista", "terroristas", "presos politicos", "preso politico",
    "autoritario", "autoritarismo", "golpe de estado", "autogolpe", "milagro", "persecucion politica",
]
# Nombres propios o términos técnicos que contienen palabras disputadas y no deben marcarse.
NOMBRES_PROPIOS = ["regimen de excepcion", "centro de confinamiento del terrorismo", "golpe de estado de 1979",
                   "golpe militar de octubre de 1979", "golpe de octubre de 1979"]

MARCAS_ATRIBUCION = ["segun", "afirma", "afirman", "afirmo", "sostiene", "sostienen", "sostuvo", "califico",
                     "calificaron", "llama", "llaman", "llamo", "denomina", "denominan", "considera", "consideran",
                     "describe", "describen", "describio", "dijo", "declaro", "denuncia", "denuncian", "denuncio",
                     "denunciaron", "senala", "senalan", "senalo", "atribuye", "atribuyo", "atribuyeron", "acuso",
                     "acusaron", "informo", "informa", "relata", "relato", "cuenta", "conto", "registra", "registro",
                     "reporta", "reporto", "estima", "calcula", "calculaba", "escribio", "escribe", "anuncio",
                     "concluyo", "concluye", "asegura", "aseguro", "niega", "nego", "rechaza", "rechazo",
                     "according", "said", "says", "claimed", "declared", "reported", "notes", "framed", "dice", "dicen", "da", "dan", "habla", "hablan", "ven", "presenta", "presentan", "citan", "cita", "fecha", "cifras oficiales", "oficialmente"]

ACTORES = {
    "gobierno salvadoreno": ["gobierno salvadoreno", "gobierno de bukele", "bukele", "nuevas ideas", "autoridades",
                             "policia", "pnc", "ministro", "asamblea", "fiscalia", "gobierno de el salvador", "gana",
                             "oficialismo", "vicepresidente", "villatoro", "ulloa", "fuerza armada", "cancilleria"],
    "criticos y ong": ["cristosal", "socorro juridico", "human rights watch", "hrw", "amnistia", "cidh", "ong",
                       "organizaciones de derechos humanos", "wola", "expertos", "gipes", "oposicion", "cispes",
                       "criticos", "sindicatos", "el faro"],
    "eeuu": ["estados unidos", "washington", "departamento de estado", "tesoro", "cia", "gobierno estadounidense"],
    "cuba": ["cuba", "castro", "la habana", "gobierno cubano", "departamento america"],
    "guerrilla": ["fmln", "guerrilla", "guerrilleros", "comandantes"],
    "haiti y onu": ["fils-aime", "gobierno haitiano", "gobierno de haiti", "policia nacional de haiti", "onu",
                    "naciones unidas", "una-haiti", "consejo de seguridad"],
    "academia": ["historiador", "investigador", "academico", "estudio", "universidad", "insight crime", "analista"],
}

STOP_ES = {"el", "la", "los", "las", "de", "que", "y", "en", "un", "una", "por", "con", "para", "se", "del"}
STOP_EN = {"the", "of", "and", "to", "in", "is", "that", "for", "with", "was", "on", "as", "by"}

RE_EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")
RE_TELEFONO = re.compile(r"(?:\+?\d{1,3}[\s.-]?)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}")
RE_NUMERO = re.compile(r"\d[\d.,]*\d|\d")
RE_CITA = re.compile(r"\"[^\"]*\"|“[^”]*”|«[^»]*»")
RE_FRASE = re.compile(r"(?<=[.!?;])\s+|\n+")


# ---------------------------------------------------------------- utilidades

def normalizar(texto: str) -> str:
    t = unicodedata.normalize("NFD", texto.lower())
    return "".join(c for c in t if unicodedata.category(c) != "Mn")


def numero_canonico(s: str) -> str:
    s = s.strip(".,")
    if re.fullmatch(r"\d{1,3}([.,]\d{3})+", s):
        return re.sub(r"[.,]", "", s)
    return s.replace(",", ".")


def numeros_en(texto: str) -> set[str]:
    return {numero_canonico(n) for n in RE_NUMERO.findall(texto)}


def palabras(texto: str) -> list[str]:
    return re.findall(r"\w+", texto, flags=re.UNICODE)


def fuera_de_citas(texto: str) -> str:
    return RE_CITA.sub(" ", texto)


def contiene_termino(texto_norm: str, termino: str) -> bool:
    return re.search(rf"\b{re.escape(termino)}\b", texto_norm) is not None


def atribuida(frase: str) -> bool:
    fn = normalizar(frase)
    return any(contiene_termino(fn, m) for m in MARCAS_ATRIBUCION)


def shingles(texto: str, n: int = 5) -> set[str]:
    w = palabras(normalizar(texto))
    return {" ".join(w[i:i + n]) for i in range(max(len(w) - n + 1, 1))}


def jaccard(a: set[str], b: set[str]) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


# ---------------------------------------------------------------- carga

def cargar_fuentes(ruta: Path) -> dict[str, dict]:
    if not ruta.exists():
        print(f"[ERROR] No encuentro el registro de fuentes: {ruta}")
        sys.exit(2)
    with ruta.open(encoding="utf-8-sig", newline="") as f:
        return {fila["id_fuente"].strip(): fila for fila in csv.DictReader(f)}


def cargar_jsonl(ruta: Path) -> list[tuple[int, dict | None, str | None]]:
    filas = []
    with ruta.open(encoding="utf-8-sig") as f:
        for n, linea in enumerate(f, 1):
            if not linea.strip():
                continue
            try:
                filas.append((n, json.loads(linea), None))
            except json.JSONDecodeError as e:
                filas.append((n, None, f"JSON inválido: {e}"))
    return filas


def respuestas_finales(msgs: list[dict]) -> list[str]:
    """Textos del asistente que lee la persona (no las llamadas a herramientas)."""
    return [m["content"] for m in msgs
            if m.get("role") == "assistant" and str(m.get("content", "")).strip()]


# ---------------------------------------------------------------- reglas por ejemplo

def validar_turnos(msgs: list[dict]) -> list[str]:
    errores = []
    if not isinstance(msgs, list) or len(msgs) < 2:
        return ["messages debe tener al menos un turno user y uno assistant"]
    i = 1 if msgs[0].get("role") == "system" else 0
    if msgs[i].get("role") != "user":
        errores.append("el primer turno (tras el system) debe ser del user")
    pendientes = 0
    previo = None
    for n, m in enumerate(msgs[i:], i):
        rol = m.get("role")
        if rol == "user":
            if pendientes:
                errores.append(f"turno {n}: faltan respuestas de herramienta antes del user")
            if previo == "user":
                errores.append(f"turno {n}: dos turnos user seguidos")
        elif rol == "assistant":
            llamadas = m.get("tool_calls") or []
            if pendientes:
                errores.append(f"turno {n}: el assistant habla antes de recibir la respuesta de la herramienta")
            for tc in llamadas:
                fn = tc.get("function", {})
                if not fn.get("name"):
                    errores.append(f"turno {n}: tool_call sin nombre")
                if not isinstance(fn.get("arguments"), dict):
                    errores.append(f"turno {n}: los arguments de {fn.get('name')} deben ser un objeto JSON")
            pendientes = len(llamadas)
            if not llamadas and not str(m.get("content", "")).strip():
                errores.append(f"turno {n}: assistant sin contenido ni llamadas")
        elif rol == "tool":
            if pendientes <= 0:
                errores.append(f"turno {n}: respuesta de herramienta sin llamada previa")
            pendientes -= 1
            if not str(m.get("content", "")).strip():
                errores.append(f"turno {n}: respuesta de herramienta vacía")
        else:
            errores.append(f"turno {n}: rol desconocido '{rol}'")
        previo = rol
    if msgs[-1].get("role") != "assistant" or not str(msgs[-1].get("content", "")).strip():
        errores.append("el último turno debe ser una respuesta del assistant con texto")
    return errores


def validar_ejemplo(ej: dict, fuentes: dict[str, dict]) -> tuple[list[str], list[str]]:
    errores, avisos = [], []
    for campo in ("id", "etapa", "tipo", "messages", "fuentes", "estado_revision"):
        if campo not in ej:
            errores.append(f"falta el campo '{campo}'")
    if errores:
        return errores, avisos
    if ej["etapa"] not in ETAPAS:
        errores.append(f"etapa desconocida '{ej['etapa']}'")
    if ej["tipo"] not in TIPOS:
        errores.append(f"tipo desconocido '{ej['tipo']}'")
    if ej["estado_revision"] not in ESTADOS:
        errores.append(f"estado_revision desconocido '{ej['estado_revision']}'")

    msgs = ej["messages"]
    errores += validar_turnos(msgs)
    if errores:
        return errores, avisos

    finales = respuestas_finales(msgs)
    respuestas = "\n".join(finales)
    resp_norm = normalizar(respuestas)
    resp_sin_citas = normalizar(fuera_de_citas(respuestas))

    minimo = MIN_PALABRAS.get(ej["tipo"], MIN_DEFECTO)
    for t in finales:
        n = len(palabras(t))
        if n < minimo:
            errores.append(f"respuesta corta ({n} palabras, mínimo {minimo} para '{ej['tipo']}')")
        elif n > MAX_PALABRAS:
            avisos.append(f"respuesta larga ({n} palabras, máximo {MAX_PALABRAS})")

    # --- fuentes
    if not ej["fuentes"] and ej["tipo"] not in ("saludo", "sin_datos"):
        errores.append("sin fuentes: todo ejemplo con datos necesita al menos un fragmento")
    texto_hechos, texto_postura = "", ""
    for f in ej["fuentes"]:
        fid = f.get("id_fuente", "")
        if fid not in fuentes:
            errores.append(f"fuente '{fid}' no está en registro_fuentes.csv")
        frag = str(f.get("fragmento", "")).strip()
        if len(palabras(frag)) < 10:
            errores.append(f"fragmento de '{fid}' vacío o demasiado corto")
        uso = fuentes.get(fid, {}).get("uso", "").strip()
        if uso == "pendiente":
            errores.append(f"fuente '{fid}' en evaluación (uso=pendiente)")
        elif uso in USOS_PARA_HECHOS:
            texto_hechos += " " + frag
        elif uso == "postura":
            texto_postura += " " + frag

    # Lo que devolvieron las herramientas también cuenta como contexto, pero solo si sale de los fragmentos
    # listados: así un número que el ejemplo pone en la respuesta de una herramienta sin fragmento detrás se detecta.
    nums_hechos = numeros_en(texto_hechos)
    nums_postura = numeros_en(texto_postura)
    for frase in RE_FRASE.split(respuestas):
        for num in sorted(numeros_en(frase) - nums_hechos):
            if num in nums_postura:
                if not atribuida(frase):
                    errores.append(f"la cifra '{num}' solo la sostiene una parte interesada y la frase no la "
                                   f"atribuye: «{frase.strip()[:90]}…»")
            else:
                errores.append(f"el número '{num}' no aparece en ningún fragmento (¿inventado?)")

    # --- lenguaje cargado
    for t in TERMINOS_PROHIBIDOS:
        if contiene_termino(resp_sin_citas, t):
            errores.append(f"término cargado fuera de cita: '{t}'")
        elif contiene_termino(resp_norm, t):
            avisos.append(f"término cargado dentro de cita: '{t}' — confirma que está atribuido")
    for oracion in RE_FRASE.split(fuera_de_citas(respuestas)):
        on = normalizar(oracion)
        for nombre in NOMBRES_PROPIOS:
            on = on.replace(nombre, " ")
        for t in TERMINOS_DISPUTADOS:
            if contiene_termino(on, t) and not atribuida(oracion):
                avisos.append(f"término disputado sin atribución: '{t}' en «{oracion.strip()[:80]}…»")

    # --- simetría
    if ej["tipo"] in ("perspectivas", "conflicto"):
        presentes = [a for a, claves in ACTORES.items() if any(contiene_termino(resp_norm, c) for c in claves)]
        if len(presentes) < 2:
            errores.append(f"tipo '{ej['tipo']}' con menos de 2 actores (encontrados: {presentes or 'ninguno'})")

    if RE_EMAIL.search(respuestas):
        errores.append("posible correo electrónico en la respuesta")
    if RE_TELEFONO.search(respuestas):
        avisos.append("posible número de teléfono en la respuesta")

    w = [x.lower() for x in palabras(respuestas)]
    es, en = sum(x in STOP_ES for x in w), sum(x in STOP_EN for x in w)
    if en > es and not ej.get("idioma") == "en":
        errores.append("la respuesta parece estar en inglés (marca 'idioma': 'en' si es a propósito)")

    if ej["estado_revision"] == "aprobado" and not str(ej.get("revisor", "")).strip():
        avisos.append("aprobado sin nombre de revisor")
    return errores, avisos


# ---------------------------------------------------------------- reglas de conjunto

def revisar_duplicados(ejemplos: list[dict]) -> dict[str, list[str]]:
    hallazgos: dict[str, list[str]] = defaultdict(list)
    for i, c in Counter(e["id"] for e in ejemplos).items():
        if c > 1:
            hallazgos[i].append(f"ERROR id repetido {c} veces")
    hashes, preguntas, sh = {}, {}, []
    for e in ejemplos:
        resp = "\n".join(respuestas_finales(e["messages"]))
        primera = next(m for m in e["messages"] if m.get("role") == "user")
        preg = normalizar(primera["content"]).strip()
        h = hashlib.sha256(normalizar(resp).encode()).hexdigest()
        if h in hashes:
            hallazgos[e["id"]].append(f"ERROR respuesta idéntica a {hashes[h]}")
        else:
            hashes[h] = e["id"]
        if preg in preguntas:
            hallazgos[e["id"]].append(f"AVISO pregunta idéntica a {preguntas[preg]}")
        else:
            preguntas[preg] = e["id"]
        sh.append((e["id"], shingles(resp)))
    for i in range(len(sh)):
        for j in range(i + 1, len(sh)):
            a, b = sh[i][1], sh[j][1]
            if min(len(a), len(b)) / max(len(a), len(b), 1) < UMBRAL_CASI_DUPLICADO:
                continue
            s = jaccard(a, b)
            if s >= UMBRAL_CASI_DUPLICADO:
                hallazgos[sh[j][0]].append(f"AVISO casi duplicado de {sh[i][0]} (similitud {s:.2f})")
    return hallazgos


def revisar_muletillas(ejemplos: list[dict]) -> list[str]:
    """Receta: una frase que aparece en más del 10 % de las respuestas se vuelve muletilla."""
    avisos = []
    if len(ejemplos) < 20:
        return avisos
    inicios = Counter(" ".join(palabras(normalizar(r))[:5]) for e in ejemplos for r in respuestas_finales(e["messages"]))
    total = sum(inicios.values())
    for frase, c in inicios.most_common(5):
        if c / total > 0.10:
            avisos.append(f"AVISO {c} de {total} respuestas empiezan igual: «{frase}…»")
    return avisos


def revisar_registro(fuentes: dict[str, dict]) -> list[str]:
    problemas = []
    for fid, fila in fuentes.items():
        persp, uso = fila.get("perspectiva", "").strip(), fila.get("uso", "").strip()
        if persp not in PERSPECTIVAS_FUENTE:
            problemas.append(f"{fid}: perspectiva '{persp}' no válida")
        if uso not in USOS_FUENTE:
            problemas.append(f"{fid}: uso '{uso}' no válido")
        if persp in PARTES_INTERESADAS and uso != "postura":
            problemas.append(f"{fid}: una fuente de parte interesada ({persp}) solo puede tener uso=postura")
        if not fila.get("licencia", "").strip():
            problemas.append(f"{fid}: falta la licencia")
        url = fila.get("url", "").strip()
        if not (url.startswith("https://") or url.startswith("privado://")):
            problemas.append(f"{fid}: la url debe empezar por https:// (o privado:// para documentos privados)")
    return problemas


# ---------------------------------------------------------------- fragmentos

def validar_fragmentos(ruta: Path, fuentes: dict[str, dict]) -> int:
    filas = cargar_jsonl(ruta)
    print(f"\n=== Validando fragmentos {ruta} ({len(filas)} líneas) ===\n")
    problemas_reg = revisar_registro(fuentes)
    for p in problemas_reg:
        print(f"[REGISTRO] {p}")
    total_err, total_av = len(problemas_reg), 0
    ids, por_tipo, por_persp, por_etapa, estados = Counter(), Counter(), Counter(), Counter(), Counter()
    for n, fr, err in filas:
        errores, avisos = [], []
        if err:
            errores.append(err)
            fr = {}
        fid_frag = fr.get("id", f"linea_{n}")
        ids[fid_frag] += 1
        if fr.get("estado") == "rechazado":
            estados["rechazado"] += 1
            continue
        estados["aprobado" if fr.get("estado") == "aprobado" else "pendiente"] += 1
        for campo in ("id", "etapa", "tipo", "id_fuente", "ubicacion", "texto", "corroborado_por", "revisado"):
            if campo not in fr and not err:
                errores.append(f"falta el campo '{campo}'")
        tipo = fr.get("tipo")
        if tipo and tipo not in TIPOS_FRAGMENTO:
            errores.append(f"tipo '{tipo}' no válido")
        if fr.get("etapa") and fr["etapa"] not in ETAPAS:
            errores.append(f"etapa desconocida '{fr['etapa']}'")
        principal = fr.get("id_fuente", "")
        todas = [principal] + list(fr.get("corroborado_por", []))
        for f in todas:
            if f and f not in fuentes:
                errores.append(f"fuente '{f}' no está en el registro")
        usos = {f: fuentes.get(f, {}).get("uso", "") for f in todas if f in fuentes}
        de_hechos = [f for f, u in usos.items() if u in USOS_PARA_HECHOS]
        texto_n = normalizar(fr.get("texto", ""))
        if any(u == "pendiente" for u in usos.values()):
            errores.append("cita una fuente en evaluación")
        if tipo == "hecho" and not de_hechos:
            errores.append("un 'hecho' necesita al menos una fuente de hechos")
        if tipo == "hecho" and len(de_hechos) < 2:
            avisos.append("hecho con una sola fuente de hechos: buscar corroboración")
        if tipo in ("postura", "hecho_atribuido", "testimonio") and \
                not any(contiene_termino(texto_n, m) for m in MARCAS_ATRIBUCION):
            errores.append(f"un '{tipo}' debe ir atribuido en el texto ('según...', 'afirmó...')")
        if tipo == "postura" and not fr.get("actor"):
            avisos.append("postura sin campo 'actor'")
        if tipo == "hecho_atribuido" and usos.get(principal) not in USOS_PARA_HECHOS:
            errores.append("un 'hecho_atribuido' necesita una fuente de uso hechos/ambos; si no, es 'postura'")
        if tipo == "testimonio" and not fr.get("testigo"):
            errores.append("un testimonio necesita el campo 'testigo'")
        if tipo == "cifra_disputada" and len(todas) < 2:
            errores.append("una cifra disputada debe citar al menos dos fuentes")
        if len(palabras(fr.get("texto", ""))) < 8:
            errores.append("texto vacío o demasiado corto")
        if not fr.get("revisado"):
            avisos.append("sin revisar")
        por_tipo[tipo] += 1
        por_etapa[fr.get("etapa")] += 1
        por_persp[fuentes.get(principal, {}).get("perspectiva", "?")] += 1
        if errores or avisos:
            print(f"--- {fid_frag}")
            for e in errores:
                print(f"   ERROR  {e}")
            for a in avisos:
                print(f"   AVISO  {a}")
        total_err += len(errores)
        total_av += len(avisos)
    for i, c in ids.items():
        if c > 1:
            print(f"--- {i}\n   ERROR  id repetido {c} veces")
            total_err += 1
    print("\n=== Balance de fragmentos ===")
    print("Por época:      ", dict(sorted(por_etapa.items())))
    print("Por tipo:       ", dict(por_tipo))
    print("Por perspectiva:", dict(por_persp))
    print(f"Revisión: {estados['aprobado']} aprobados | {estados['rechazado']} rechazados | "
          f"{estados['pendiente']} pendientes")
    print(f"Errores: {total_err} | Avisos: {total_av}")
    return 1 if total_err else 0


# ---------------------------------------------------------------- main

def main() -> int:
    ap = argparse.ArgumentParser(description="Valida el dataset de vertex-salvador")
    ap.add_argument("archivo", type=Path)
    ap.add_argument("--fuentes", type=Path, default=Path("fuentes/registro_fuentes.csv"))
    ap.add_argument("--reporte", type=Path, default=Path("reportes/reporte_validacion.json"))
    ap.add_argument("--fragmentos", action="store_true")
    args = ap.parse_args()

    fuentes = cargar_fuentes(args.fuentes)
    filas = cargar_jsonl(args.archivo)
    primera = next((d for _, d, e in filas if d), None)
    if args.fragmentos or (primera and "messages" not in primera and "id_fuente" in primera):
        return validar_fragmentos(args.archivo, fuentes)

    print(f"\n=== Validando {args.archivo} ({len(filas)} líneas) ===\n")
    for p in revisar_registro(fuentes):
        print(f"[REGISTRO] {p}")
    resultados: dict[str, dict] = {}
    ejemplos: list[dict] = []
    for n, ej, err in filas:
        if err:
            resultados[f"linea_{n}"] = {"errores": [err], "avisos": []}
            continue
        errores, avisos = validar_ejemplo(ej, fuentes)
        resultados[ej.get("id", f"linea_{n}")] = {"errores": errores, "avisos": avisos}
        if not errores or "messages" in ej:
            ejemplos.append(ej)
    for eid, lista in revisar_duplicados([e for e in ejemplos if "messages" in e]).items():
        for h in lista:
            nivel, msg = h.split(" ", 1)
            resultados.setdefault(eid, {"errores": [], "avisos": []})
            resultados[eid]["errores" if nivel == "ERROR" else "avisos"].append(msg)
    total_err = total_av = 0
    for eid, r in resultados.items():
        if not r["errores"] and not r["avisos"]:
            continue
        print(f"--- {eid}")
        for e in r["errores"]:
            print(f"   ERROR  {e}")
        for a in r["avisos"]:
            print(f"   AVISO  {a}")
        total_err += len(r["errores"])
        total_av += len(r["avisos"])
    for a in revisar_muletillas(ejemplos):
        print(a)
    print("\n=== Balance ===")
    print("Por época:", dict(sorted(Counter(e.get("etapa") for e in ejemplos).items())))
    print("Por tipo: ", dict(Counter(e.get("tipo") for e in ejemplos)))
    con_herr = sum(1 for e in ejemplos if any(m.get("tool_calls") for m in e.get("messages", [])))
    print(f"Con llamadas a herramientas: {con_herr} de {len(ejemplos)}")
    limpios = [e for e in ejemplos if not resultados[e["id"]]["errores"]]
    aprobados = [e for e in limpios if e.get("estado_revision") == "aprobado"]
    print(f"\nEjemplos: {len(ejemplos)} | sin errores: {len(limpios)} | aprobados listos: {len(aprobados)}")
    print(f"Errores: {total_err} | Avisos: {total_av}")
    args.reporte.parent.mkdir(parents=True, exist_ok=True)
    args.reporte.write_text(json.dumps(resultados, ensure_ascii=False, indent=2), encoding="utf-8")
    return 1 if total_err else 0


if __name__ == "__main__":
    sys.exit(main())
