"""
ejemplos_base.py — Piezas comunes para escribir los ejemplos de entrenamiento de vertex-salvador.

Cada ejemplo se escribe así:
    E(id, etapa, tipo, pregunta, pasos, respuesta)
donde 'pasos' es una lista de rondas de herramientas; cada ronda es una lista de llamadas:
    B("consulta", ["FR-E10-001", ...], epoca="E10")      -> buscar_documentos
    B("consulta", [], coleccion="privada")                -> buscar_documentos sin resultados
    L("E09", ["FR-E09-001", ...])                         -> linea_tiempo
    C("homicidios", [fila, ...])                          -> consultar_cifras (cada fila apunta a su fragmento)
    D("FR-E01-004")                                       -> leer_documento

La respuesta de cada herramienta se construye SOLA a partir de los fragmentos aprobados de fuentes/: así el texto
que el modelo ve como resultado es exactamente el texto verificado, y nunca uno escrito a mano.
"""
import csv
import glob
import json
from pathlib import Path

REVISOR = "Claude (por encargo de Denis)"
HOY = "2026-11-18"

SISTEMA = ("Eres el asistente de vertex-salvador. Hablas de la historia de El Salvador, de las pandillas y del "
           "gobierno de Nayib Bukele con neutralidad: cuentas lo que pasó, distingues los hechos documentados de lo "
           "que afirma cada parte y atribuyes cada versión y cada cifra a quien la sostiene. Antes de dar un dato, "
           "fecha o cifra, búscalo con tus herramientas. Si las herramientas no traen el dato, dilo con claridad y "
           "explica qué sí encontraste, sin inventar. Responde en el idioma de la persona, con un tono natural y "
           "cercano.")

HERRAMIENTAS = json.loads(Path("herramientas.json").read_text(encoding="utf-8"))["tools"]

# Documentos privados de prueba: material real del propio proyecto, para enseñar a buscar en la colección privada.
PRIVADOS = {
    "PRIV-001": {"id_fuente": "S900", "etapa": "general", "tipo": "hecho",
                 "texto": "Bitácora del proyecto, 17 de noviembre de 2026: Denis encargó a Claude extraer y aprobar los "
                          "fragmentos; las cifras oficiales del gobierno y las de las ONG entran siempre como postura "
                          "de quien las da, con la misma vara para todas las partes."},
    "PRIV-002": {"id_fuente": "S900", "etapa": "general", "tipo": "hecho",
                 "texto": "Bitácora del proyecto, 17 de noviembre de 2026: el modelo base propuesto es Gemma 4 E4B y, "
                          "antes de elegirlo, se prueban tres bases con las mismas 10 preguntas en LM Studio; los "
                          "documentos privados nunca entran al entrenamiento, solo al buscador."},
}


def cargar_fragmentos():
    frags = {}
    for ruta in sorted(glob.glob("fuentes/fragmentos_*.jsonl")):
        for l in open(ruta, encoding="utf-8"):
            if l.strip():
                d = json.loads(l)
                if d.get("estado") == "aprobado":
                    frags[d["id"]] = d
    frags.update(PRIVADOS)
    return frags


def cargar_fuentes():
    with open("fuentes/registro_fuentes.csv", encoding="utf-8-sig", newline="") as f:
        return {r["id_fuente"]: r for r in csv.DictReader(f)}


FRAGS = cargar_fragmentos()
FUENTES = cargar_fuentes()
EJEMPLOS = []
_n = [0]


def _resultado(fid):
    fr = FRAGS[fid]
    src = FUENTES.get(fr["id_fuente"], {})
    return {"doc_id": fid, "fuente": f"{src.get('titulo', '')} — {src.get('autor_institucion', '')}".strip(" —"),
            "coleccion": "privada" if fid.startswith("PRIV") else "publica",
            "epoca": fr["etapa"], "tipo": fr["tipo"], "texto": fr["texto"]}


def B(consulta, ids, epoca=None, coleccion=None, max_resultados=None):
    args = {"consulta": consulta}
    if epoca:
        args["epoca"] = epoca
    if coleccion:
        args["coleccion"] = coleccion
    if max_resultados:
        args["max_resultados"] = max_resultados
    res = {"resultados": [_resultado(i) for i in ids], "total": len(ids)}
    if not ids:
        res["nota"] = "Sin coincidencias en la colección consultada."
    return ("buscar_documentos", args, res, list(ids))


def L(epoca, ids):
    eventos = [{**_resultado(i), "orden": n} for n, i in enumerate(ids, 1)]
    return ("linea_tiempo", {"epoca": epoca}, {"eventos": eventos, "total": len(ids)}, list(ids))


def D(fid):
    return ("leer_documento", {"doc_id": fid}, {"documento": _resultado(fid)}, [fid])


def C(metrica, filas, desde=None, hasta=None):
    """filas: lista de (periodo, valor, atribucion, fragmento)."""
    args = {"metrica": metrica}
    if desde:
        args["desde"] = desde
    if hasta:
        args["hasta"] = hasta
    salida = []
    for periodo, valor, atrib, fid in filas:
        assert fid in FRAGS, fid
        salida.append({"periodo": periodo, "valor": valor, "atribucion": atrib, "doc_id": fid,
                       "fuente": _resultado(fid)["fuente"]})
    res = {"filas": salida, "total": len(salida)}
    if not salida:
        res["nota"] = "No hay filas para esa métrica o ese periodo."
    return ("consultar_cifras", args, res, [f[3] for f in filas])


def E(eid, etapa, tipo, pregunta, pasos, respuesta, seguimiento=None, idioma=None, sin_sistema=False):
    """seguimiento: lista opcional de (pregunta2, pasos2, respuesta2) para conversaciones de varios turnos."""
    msgs = [] if sin_sistema else [{"role": "system", "content": SISTEMA}]
    usados = []

    def turno(preg, ps, resp):
        msgs.append({"role": "user", "content": preg})
        for ronda in ps:
            llamadas = []
            for nombre, args, res, ids in ronda:
                _n[0] += 1
                cid = f"call_{_n[0]:04d}"
                llamadas.append((cid, nombre, args, res))
                usados.extend(ids)
            msgs.append({"role": "assistant", "content": "",
                         "tool_calls": [{"id": c, "type": "function", "function": {"name": n, "arguments": a}}
                                        for c, n, a, _ in llamadas]})
            for c, n, a, r in llamadas:
                msgs.append({"role": "tool", "tool_call_id": c, "name": n,
                             "content": json.dumps(r, ensure_ascii=False)})
        msgs.append({"role": "assistant", "content": resp.strip()})

    turno(pregunta, pasos, respuesta)
    for p2, ps2, r2 in seguimiento or []:
        turno(p2, ps2, r2)
    vistos = []
    for i in usados:
        if i not in vistos:
            vistos.append(i)
    ej = {"id": eid, "etapa": etapa, "tipo": tipo, "messages": msgs,
          "fuentes": [{"id_fragmento": i, "id_fuente": FRAGS[i]["id_fuente"], "fragmento": FRAGS[i]["texto"]}
                      for i in vistos],
          "estado_revision": "aprobado", "revisor": REVISOR, "fecha_revision": HOY}
    if idioma:
        ej["idioma"] = idioma
    EJEMPLOS.append(ej)


def guardar(nombre):
    Path("datos").mkdir(exist_ok=True)
    ruta = Path("datos") / nombre
    with ruta.open("w", encoding="utf-8", newline="\n") as f:
        for e in EJEMPLOS:
            f.write(json.dumps(e, ensure_ascii=False) + "\n")
    print(f"{len(EJEMPLOS)} ejemplos en {ruta}")
