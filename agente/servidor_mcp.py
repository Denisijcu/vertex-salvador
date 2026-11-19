"""
servidor_mcp.py — Servidor MCP de vertex-salvador con las 4 herramientas del contrato (herramientas.json):
    buscar_documentos · leer_documento · consultar_cifras · linea_tiempo

Responde EXACTAMENTE con el formato con el que se entrenó el modelo (mismos campos), así que lo que el modelo ve en
LM Studio es lo mismo que vio en el entrenamiento.

Busca en dos colecciones:
  - publica:  los fragmentos aprobados de ..\\fuentes\\fragmentos_*.jsonl
  - privada:  los documentos que pongas en agente\\docs_privados\\ (.txt, .md; .pdf si tienes pypdf; .docx si tienes
              python-docx). NUNCA entran al entrenamiento: solo al buscador. Se recargan solos si cambian.

Buscador: BM25 en Python puro, sin descargar modelos ni nada de internet.

Probar sin LM Studio (desde E:\\vertex-salvador\\agente):
    python probar_servidor.py
Arrancar como servidor MCP (lo arranca LM Studio con la configuración de README_AGENTE.md):
    python servidor_mcp.py
Necesita el paquete 'mcp' (sirve la versión 1.x o la 2.x; pip show mcp para ver si ya lo tienes).
"""
from __future__ import annotations

import csv
import json
import sys
import math
import re
import unicodedata
from collections import Counter
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
AGENTE = Path(__file__).resolve().parent
PRIVADOS = AGENTE / "docs_privados"
CIFRAS = AGENTE / "cifras.json"

STOP = set("""el la los las de del que y en un una unos unas por con para se su sus al lo le les es son fue fueron
era como mas más pero o u a e ni ya muy sin sobre entre hasta desde cuando donde qué que cual cuál quien quién este
esta estos estas ese esa esos esas eso esto hay ha han había me te nos the of and to in is that for with was on as by
an be are it this from at or""".split())
EPOCAS = {f"P0{i}" for i in range(1, 6)} | {f"E{i:02d}" for i in range(1, 15)} | {"T01", "T02", "T03", "T04", "X01",
                                                                                   "general"}


def normalizar(t: str) -> str:
    t = unicodedata.normalize("NFD", t.lower())
    return "".join(c for c in t if unicodedata.category(c) != "Mn")


def terminos(t: str) -> list[str]:
    salida = []
    for w in re.findall(r"[a-z0-9ñ]+(?:-[a-z0-9]+)?", normalizar(t)):
        if w in STOP or len(w) < 2:
            continue
        salida.append(w[:7] if not w.isdigit() else w)   # raíz corta: "pandillas" y "pandillero" se juntan
    return salida


# ------------------------------------------------------------------ carga de documentos

def _fuentes():
    ruta = BASE / "fuentes" / "registro_fuentes.csv"
    if not ruta.exists():
        sys.exit(f"No encuentro {ruta}. La carpeta 'agente' tiene que quedarse dentro de la carpeta del proyecto, "
                 "junto a la carpeta 'fuentes'. No la muevas por separado.")
    with ruta.open(encoding="utf-8-sig", newline="") as f:
        return {r["id_fuente"]: r for r in csv.DictReader(f)}


def _publicos():
    fuentes = _fuentes()
    docs = {}
    for ruta in sorted((BASE / "fuentes").glob("fragmentos_*.jsonl")):
        for l in ruta.open(encoding="utf-8"):
            if not l.strip():
                continue
            d = json.loads(l)
            if d.get("estado") != "aprobado":
                continue
            src = fuentes.get(d["id_fuente"], {})
            docs[d["id"]] = {"doc_id": d["id"],
                             "fuente": f"{src.get('titulo', '')} — {src.get('autor_institucion', '')}".strip(" —"),
                             "coleccion": "publica", "epoca": d["etapa"], "tipo": d["tipo"], "texto": d["texto"],
                             "url": src.get("url", "")}
    return docs


def _leer_archivo(p: Path) -> str:
    suf = p.suffix.lower()
    if suf in (".txt", ".md"):
        return p.read_text(encoding="utf-8", errors="replace")
    if suf == ".pdf":
        try:
            from pypdf import PdfReader
        except ImportError:
            return ""
        return "\n\n".join((pg.extract_text() or "") for pg in PdfReader(str(p)).pages)
    if suf == ".docx":
        try:
            import docx
        except ImportError:
            return ""
        return "\n\n".join(par.text for par in docx.Document(str(p)).paragraphs)
    return ""


def _trozos(texto: str, palabras_por_trozo: int = 150) -> list[str]:
    parrafos = [x.strip() for x in re.split(r"\n\s*\n", texto) if x.strip()]
    trozos, actual = [], []
    for par in parrafos:
        actual.append(par)
        if sum(len(x.split()) for x in actual) >= palabras_por_trozo:
            trozos.append("\n".join(actual))
            actual = []
    if actual:
        trozos.append("\n".join(actual))
    return trozos


class Coleccion:
    def __init__(self):
        self.publicos = _publicos()
        self.privados, self.huella = {}, None
        self.cifras = json.loads(CIFRAS.read_text(encoding="utf-8"))["metricas"] if CIFRAS.exists() else {}
        self._indexar()

    def _huella_privados(self):
        if not PRIVADOS.exists():
            return ()
        return tuple(sorted((str(p), p.stat().st_mtime) for p in PRIVADOS.rglob("*") if p.is_file()))

    def _cargar_privados(self):
        self.privados = {}
        if not PRIVADOS.exists():
            return
        for p in sorted(PRIVADOS.rglob("*")):
            if not p.is_file():
                continue
            for n, t in enumerate(_trozos(_leer_archivo(p)), 1):
                did = f"PRIV:{p.relative_to(PRIVADOS).as_posix()}#{n}"
                self.privados[did] = {"doc_id": did, "fuente": p.name, "coleccion": "privada", "epoca": "general",
                                      "tipo": "documento_privado", "texto": t}

    def _indexar(self):
        self.huella = self._huella_privados()
        self._cargar_privados()
        self.docs = {**self.publicos, **self.privados}
        self.tf = {d: Counter(terminos(v["texto"] + " " + v["fuente"])) for d, v in self.docs.items()}
        self.largo = {d: sum(c.values()) for d, c in self.tf.items()}
        self.medio = sum(self.largo.values()) / max(len(self.largo), 1)
        df = Counter()
        for c in self.tf.values():
            df.update(c.keys())
        n = len(self.docs)
        self.idf = {t: math.log(1 + (n - f + 0.5) / (f + 0.5)) for t, f in df.items()}

    def al_dia(self):
        if self._huella_privados() != self.huella:
            self._indexar()

    def buscar(self, consulta, epoca=None, coleccion="todas", k=5, k1=1.4, b=0.75):
        self.al_dia()
        q = terminos(consulta)
        puntos = []
        for d, tf in self.tf.items():
            v = self.docs[d]
            if coleccion in ("publica", "privada") and v["coleccion"] != coleccion:
                continue
            s, cubiertos = 0.0, 0
            for t in q:
                if t in tf:
                    f = tf[t]
                    cubiertos += 1
                    s += self.idf[t] * f * (k1 + 1) / (f + k1 * (1 - b + b * self.largo[d] / self.medio))
            # Cobertura mínima: con 3 o más términos, al menos 2 de cada 5 deben aparecer. Así una sola palabra
            # suelta ("receta") no trae un documento de otro tema (lección del buscador de vertex-exilio).
            if s > 0 and (len(set(q)) < 3 or cubiertos / len(q) >= 0.4):
                # La época es una preferencia, no un filtro: el modelo a veces elige mal la época (buscó el CECOT
                # en E10 y es E11). Los de la época pedida suben un 50 %, pero un documento mejor de otra época
                # sigue saliendo.
                if epoca and v["epoca"] == epoca:
                    s *= 1.5
                puntos.append((s, d))
        puntos.sort(reverse=True)
        mejores = [s for s, _ in puntos[:1]]
        # Filtro de relevancia: fuera lo que puntúa menos del 35 % del mejor, para no traer temas ajenos.
        return [self.docs[d] for s, d in puntos[:k] if mejores and s >= 0.35 * mejores[0]]


COL = None


def coleccion():
    global COL
    if COL is None:
        COL = Coleccion()
    return COL


def _limpio(doc):
    return {k: doc[k] for k in ("doc_id", "fuente", "coleccion", "epoca", "tipo", "texto")}


def _anio(texto: str):
    m = re.search(r"(1[89]\d\d|20\d\d)", texto)
    return int(m.group(1)) if m else None


# ------------------------------------------------------------------ las 4 herramientas (lógica pura)

def h_buscar_documentos(consulta: str, epoca: str | None = None, coleccion_: str = "todas",
                        max_resultados: int = 5) -> str:
    if epoca and epoca not in EPOCAS:
        epoca = None
    k = max(1, min(int(max_resultados or 5), 15))
    res = [_limpio(d) for d in coleccion().buscar(consulta, epoca, coleccion_ or "todas", k)]
    nota = None
    if not res and epoca:
        # El modelo a veces elige mal la época. Antes de decir "no hay nada", se busca en todas.
        res = [_limpio(d) for d in coleccion().buscar(consulta, None, coleccion_ or "todas", k)]
        if res:
            nota = f"Sin coincidencias en la época {epoca}; resultados de todas las épocas."
    salida = {"resultados": res, "total": len(res)}
    if nota:
        salida["nota"] = nota
    if not res:
        salida["nota"] = "Sin coincidencias en la colección consultada."
    return json.dumps(salida, ensure_ascii=False)


def h_leer_documento(doc_id: str, seccion: str | None = None) -> str:
    col = coleccion()
    col.al_dia()
    if doc_id in col.docs:
        return json.dumps({"documento": _limpio(col.docs[doc_id])}, ensure_ascii=False)
    if doc_id.startswith("PRIV:"):        # documento privado entero o por trozos ("12-15")
        base = doc_id.split("#")[0]
        trozos = sorted((d for d in col.privados if d.startswith(base + "#")), key=lambda x: int(x.split("#")[1]))
        if seccion and re.fullmatch(r"\d+(-\d+)?", seccion):
            a, _, b = seccion.partition("-")
            a, b = int(a), int(b or a)
            trozos = [t for t in trozos if a <= int(t.split("#")[1]) <= b]
        if trozos:
            texto = "\n\n".join(col.privados[t]["texto"] for t in trozos)
            return json.dumps({"documento": {"doc_id": base, "fuente": col.privados[trozos[0]]["fuente"],
                                             "coleccion": "privada", "epoca": "general",
                                             "tipo": "documento_privado", "texto": texto[:12000]}},
                              ensure_ascii=False)
    return json.dumps({"documento": None, "nota": f"No existe el documento {doc_id}."}, ensure_ascii=False)


def h_consultar_cifras(metrica: str, desde: str | None = None, hasta: str | None = None) -> str:
    col = coleccion()
    filas = col.cifras.get(metrica)
    if filas is None:
        clave = normalizar(metrica).replace(" ", "_")
        filas = next((v for k, v in col.cifras.items() if clave in k or k in clave), [])
    d, h = _anio(desde or ""), _anio(hasta or "")
    salida = []
    for f in filas:
        a = _anio(f["periodo"])
        if (d and a and a < d) or (h and a and a > h):
            continue
        doc = col.docs.get(f["doc_id"])
        salida.append({**f, "fuente": doc["fuente"] if doc else ""})
    res = {"filas": salida, "total": len(salida)}
    if not salida:
        res["nota"] = "No hay filas para esa métrica o ese periodo."
        res["metricas_disponibles"] = sorted(col.cifras)
    return json.dumps(res, ensure_ascii=False)


def h_linea_tiempo(epoca: str | None = None, desde: str | None = None, hasta: str | None = None) -> str:
    col = coleccion()
    d, h = _anio(desde or ""), _anio(hasta or "")
    eventos = []
    for did in sorted(col.publicos):
        v = col.publicos[did]
        if epoca and v["epoca"] != epoca:
            continue
        a = _anio(v["texto"])
        if (d and (not a or a < d)) or (h and (not a or a > h)):
            continue
        eventos.append(v)
    eventos.sort(key=lambda v: (_anio(v["texto"]) or 9999, v["doc_id"]))
    tope = 25
    salida = [{**_limpio(v), "orden": n} for n, v in enumerate(eventos[:tope], 1)]
    respuesta = {"eventos": salida, "total": len(salida)}
    if len(eventos) > tope:
        # Antes se cortaba sin avisar y se perdían los hechos más recientes; ahora se dice.
        respuesta["nota"] = (f"Hay {len(eventos)} eventos y se muestran los {tope} primeros. Para ver el resto, "
                             f"pide un rango más corto con 'desde' y 'hasta'.")
    return json.dumps(respuesta, ensure_ascii=False)


# ------------------------------------------------------------------ servidor MCP

def main():
    try:                                    # mcp 1.x
        from mcp.server.fastmcp import FastMCP as Servidor
    except ModuleNotFoundError:             # mcp 2.x renombró FastMCP a MCPServer
        from mcp.server.mcpserver import MCPServer as Servidor

    mcp = Servidor("vertex-salvador")

    @mcp.tool()
    def buscar_documentos(consulta: str, epoca: str | None = None, coleccion: str = "todas",
                          max_resultados: int = 5) -> str:
        """Busca fragmentos en la colección de documentos (públicos y privados). Devuelve texto, fuente, época y
        tipo. Úsala antes de afirmar cualquier hecho, cifra o fecha."""
        return h_buscar_documentos(consulta, epoca, coleccion, max_resultados)

    @mcp.tool()
    def leer_documento(doc_id: str, seccion: str | None = None) -> str:
        """Abre un documento completo, o una sección, cuando el fragmento de buscar_documentos no alcanza."""
        return h_leer_documento(doc_id, seccion)

    @mcp.tool()
    def consultar_cifras(metrica: str, desde: str | None = None, hasta: str | None = None) -> str:
        """Consulta la tabla de cifras (homicidios, detenciones_regimen, prorrogas, muertes_custodia,
        presos_politicos, elecciones_presidenciales...). Cada fila trae valor, atribución y el documento que la
        sostiene."""
        return h_consultar_cifras(metrica, desde, hasta)

    @mcp.tool()
    def linea_tiempo(epoca: str | None = None, desde: str | None = None, hasta: str | None = None) -> str:
        """Devuelve los eventos ordenados de una época (P01–P05, E01–E15, T01–T04) o de un rango de años."""
        return h_linea_tiempo(epoca, desde, hasta)

    mcp.run()


if __name__ == "__main__":
    main()
