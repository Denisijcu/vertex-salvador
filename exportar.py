"""
exportar.py — Exporta el dataset de vertex-salvador para el entrenamiento (SFT con herramientas).

Es el exportar_gemma.py de vertex-exilio con tres cambios:
  1. Cada línea lleva "messages" en formato de chat con herramientas (tool_calls y turnos "tool") y "tools" (el
     contrato de herramientas.json, o null). El texto NO se escribe aquí: lo pinta en Kaggle la plantilla real del
     modelo base, para no atarnos a una plantilla escrita a mano.
  2. Solo entran los ejemplos que pasan validar.py sin errores.
  3. La mitad de las conversaciones generales también llevan las herramientas declaradas, para que el modelo
     aprenda a NO llamarlas cuando no hacen falta.

Mezcla acordada (igual que en el exilio):
  60 %  ejemplos propios aprobados (datos/ejemplos_*.jsonl)
  25 %  conversación general en español  (OpenAssistant oasst2, Apache-2.0)
  15 %  conversación general en inglés   (OpenAssistant oasst2, Apache-2.0)

Uso (desde E:\\vertex-salvador). El oasst2 ya lo tienes bajado en la carpeta del exilio; no hace falta bajarlo:
    python exportar.py
    python exportar.py --oasst ..\\vertex-exilio\\fuentes\\generales\\2023-11-05_oasst2_ready.messages.jsonl.gz

Escribe:
  exportacion/gemma_train.jsonl   exportacion/gemma_val.jsonl   reportes/reporte_exportacion.json
No toca datos/ ni fuentes/: solo lee.
"""
import argparse
import glob
import gzip
import hashlib
import json
import random
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import validar

PROPIO, ES, EN = 60, 25, 15
SIN_SISTEMA = 0.10          # uno de cada diez ejemplos propios va sin instrucción de sistema
GENERAL_CON_HERRAMIENTAS = 0.5
VAL = 0.10
CALIDAD_MIN = 0.75
OASST_DEFECTO = Path("../vertex-exilio/fuentes/generales/2023-11-05_oasst2_ready.messages.jsonl.gz")
EXCLUIDOS = [Path("fuentes/generales/excluidos.txt"), Path("../vertex-exilio/fuentes/generales/excluidos.txt")]

# Lo de oasst2 que toque política, El Salvador, Cuba, violencia o temas sensibles se queda fuera: de eso el modelo
# aprende SOLO con nuestros ejemplos verificados.
BLOQUEO = re.compile(
    r"\b(salvador\w*|bukele|cuscatl\w*|maras?|pandill\w*|gangs?|ms-?13|cecot|cuba\w*|castro|fidel|habana|havana|"
    r"guerrill\w*|fmln|arena|exili\w*|exile\w*|comunis\w*|communis\w*|socialis\w*|marxis\w*|capitalis\w*|"
    r"dictad\w*|dictator\w*|r[eé]gimen|regime|revoluci\w*|revolution\w*|embargo|bloqueo|pol[ií]tic\w*|"
    r"politic\w*|elecci\w*|election\w*|vot\w*|partido|party|trump|biden|obama|putin|ch[aá]vez|maduro|venezuel\w*|"
    r"israel\w*|palestin\w*|ucrani\w*|ukrain\w*|rusia|russia|guerra|war|terroris\w*|aborto|abortion|inmigra\w*|"
    r"immigra\w*|refugia\w*|refugee\w*|deport\w*|prisi[oó]n|prison\w*|c[aá]rcel\w*|jail\w*|police|polic[ií]a|"
    r"homicid\w*|asesin\w*|murder\w*|crimen|crime\w*|religi\w*|dios|god|iglesia|church|ideolog\w*|gobierno|"
    r"government|presidente|president|derechos humanos|human rights|g[eé]neros?|genders?|transg\w*|sexual\w*|"
    r"sexo|sex|porn\w*|er[oó]tic\w*|drogas?|drugs?|marihuana|marijuana|cannabis|razas?|races?|racis\w*|"
    r"anorex\w*|bulimi\w*|depresi\w*|depression|suicid\w*|diagn[oó]stic\w*|diagnos\w*|cripto\w*|crypto\w*|"
    r"bitcoin|conspira\w*|nsfw|trading|fiscal\w*|impuestos?|taxes?|sentient|chatbots?|are you|eres t[uú])\b",
    re.IGNORECASE)
IDENTIDAD = re.compile(r"open ?assistant|laion|chatgpt|openai|gpt-?\d|soy un modelo de lenguaje|as an ai|"
                       r"language model|modelo de lenguaje", re.IGNORECASE)
NUMERO = re.compile(r"\d+(?:[.,]\d+)*")


def palabras(t):
    return len(t.split())


def etiqueta(labels, nombre):
    if labels is None:
        return None
    if isinstance(labels, dict) and nombre in labels and isinstance(labels[nombre], dict):
        return float(labels[nombre].get("value"))
    nombres = labels.get("name") if isinstance(labels, dict) else None
    if nombres is None or len(nombres) == 0:
        return None
    nombres = list(nombres)
    return float(labels["value"][nombres.index(nombre)]) if nombre in nombres else None


def leer_oasst(ruta):
    with gzip.open(ruta, "rt", encoding="utf-8") as f:
        for l in f:
            if l.strip():
                yield json.loads(l)


def cargar_propios(fuentes):
    ejemplos, problemas, vistos = [], [], set()
    for ruta in sorted(glob.glob("datos/ejemplos_*.jsonl")):
        for n, l in enumerate(open(ruta, encoding="utf-8-sig"), 1):
            if not l.strip():
                continue
            d = json.loads(l)
            if d.get("estado_revision") != "aprobado":
                continue
            errores, _ = validar.validar_ejemplo(d, fuentes)
            if errores:
                problemas.append(f"{ruta}:{n} {d.get('id')}: {errores[0]}")
                continue
            if d["id"] in vistos:
                problemas.append(f"{ruta}:{n} id repetido {d['id']}")
                continue
            vistos.add(d["id"])
            ejemplos.append({"id": d["id"], "origen": "propio", "etapa": d["etapa"], "tipo": d["tipo"],
                             "messages": d["messages"]})
    return ejemplos, problemas


def cargar_generales(ruta):
    excluidos = set()
    for e in EXCLUIDOS:
        if e.exists():
            excluidos |= {l.split("#")[0].strip() for l in e.read_text(encoding="utf-8").splitlines()} - {""}
    raices, por_padre = [], {}
    for m in leer_oasst(ruta):
        if m.get("review_result") is not True or m.get("deleted") is True or m.get("synthetic") is True:
            continue
        if m.get("role") == "prompter" and m.get("parent_id") in (None, "") and m.get("lang") in ("es", "en"):
            raices.append(m)
        elif m.get("role") == "assistant" and m.get("rank") == 0:
            por_padre[m["parent_id"]] = m
    candidatos, motivos, vistos = {"es": [], "en": []}, Counter(), set()
    for p in raices:
        r = por_padre.get(p["message_id"])
        if r is None:
            motivos["sin respuesta rank 0"] += 1
            continue
        if r.get("lang") != p["lang"]:
            motivos["idioma distinto"] += 1
            continue
        pregunta, respuesta = p["text"].strip(), r["text"].strip()
        calidad = etiqueta(r.get("labels"), "quality")
        tox = r["detoxify"].get("toxicity") if isinstance(r.get("detoxify"), dict) else None
        if f"oasst2-{r['message_id']}" in excluidos:
            motivos["excluido a mano"] += 1
        elif calidad is None or calidad < CALIDAD_MIN:
            motivos["calidad baja"] += 1
        elif tox is None or tox >= 0.1:
            motivos["toxicidad"] += 1
        elif BLOQUEO.search(pregunta) or BLOQUEO.search(respuesta):
            motivos["tema bloqueado"] += 1
        elif IDENTIDAD.search(respuesta) or IDENTIDAD.search(pregunta):
            motivos["habla de su identidad"] += 1
        elif len(NUMERO.findall(respuesta)) > 3:
            motivos["más de 3 números"] += 1
        elif not (40 <= palabras(respuesta) <= 450) or palabras(pregunta) < 3:
            motivos["longitud"] += 1
        elif pregunta.lower() in vistos:
            motivos["pregunta repetida"] += 1
        else:
            vistos.add(pregunta.lower())
            candidatos[p["lang"]].append({"id": f"oasst2-{r['message_id']}", "origen": f"general_{p['lang']}",
                                          "etapa": "general", "tipo": "general",
                                          "messages": [{"role": "user", "content": pregunta},
                                                       {"role": "assistant", "content": respuesta}]})
    return candidatos, motivos


def separar_val(ejemplos, azar, clave):
    grupos = defaultdict(list)
    for e in ejemplos:
        grupos[e[clave]].append(e)
    train, val = [], []
    for k in sorted(grupos):
        g = grupos[k][:]
        azar.shuffle(g)
        n = round(len(g) * VAL)
        if n == 0 and len(g) >= 5:
            n = 1
        val += g[:n]
        train += g[n:]
    return train, val


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--oasst", type=Path, default=OASST_DEFECTO)
    ap.add_argument("--semilla", type=int, default=42)
    args = ap.parse_args()
    if not Path("validar.py").exists() or not Path("herramientas.json").exists():
        sys.exit("No encuentro validar.py o herramientas.json. ¿Estás en E:\\vertex-salvador? No hago nada.")
    if not args.oasst.exists():
        sys.exit(f"No encuentro {args.oasst}. Indica la ruta con --oasst. No hago nada.")
    azar = random.Random(args.semilla)
    herramientas = json.loads(Path("herramientas.json").read_text(encoding="utf-8"))["tools"]
    fuentes = validar.cargar_fuentes(Path("fuentes/registro_fuentes.csv"))

    propios, problemas = cargar_propios(fuentes)
    if problemas:
        print("Hay ejemplos con errores; corre validar.py y corrígelos. No exporto nada:")
        for p in problemas[:20]:
            print("  ", p)
        sys.exit(1)
    n_es = round(len(propios) * ES / PROPIO)
    n_en = round(len(propios) * EN / PROPIO)
    candidatos, motivos = cargar_generales(args.oasst)
    for lang, n in (("es", n_es), ("en", n_en)):
        if len(candidatos[lang]) < n:
            sys.exit(f"Solo hay {len(candidatos[lang])} generales en '{lang}' y hacen falta {n}. No exporto nada.")

    def puesto(e):
        return hashlib.sha256(f"{args.semilla}:{e['id']}".encode()).hexdigest()
    generales = sorted(candidatos["es"], key=puesto)[:n_es] + sorted(candidatos["en"], key=puesto)[:n_en]

    sin_sistema = 0
    for e in propios:
        e["tools"] = herramientas
        if azar.random() < SIN_SISTEMA and e["messages"][0]["role"] == "system":
            e["messages"] = e["messages"][1:]
            sin_sistema += 1
    for e in generales:
        e["tools"] = herramientas if azar.random() < GENERAL_CON_HERRAMIENTAS else None

    tr_p, va_p = separar_val(propios, azar, "tipo")
    tr_g, va_g = separar_val(generales, azar, "origen")
    train, val = tr_p + tr_g, va_p + va_g
    azar.shuffle(train)
    azar.shuffle(val)

    Path("exportacion").mkdir(exist_ok=True)
    Path("reportes").mkdir(exist_ok=True)
    for nombre, filas in (("gemma_train.jsonl", train), ("gemma_val.jsonl", val)):
        with (Path("exportacion") / nombre).open("w", encoding="utf-8", newline="\n") as f:
            for e in filas:
                f.write(json.dumps(e, ensure_ascii=False) + "\n")
    total = len(train) + len(val)
    origen = Counter(e["origen"] for e in train + val)
    reporte = {
        "semilla": args.semilla, "total": total, "train": len(train), "val": len(val),
        "por_origen": dict(origen), "porcentajes": {k: round(100 * v / total, 1) for k, v in origen.items()},
        "propios_por_tipo": dict(Counter(e["tipo"] for e in propios)),
        "propios_con_llamadas": sum(1 for e in propios if any(m.get("tool_calls") for m in e["messages"])),
        "propios_sin_sistema": sin_sistema,
        "generales_con_herramientas_declaradas": sum(1 for e in generales if e["tools"]),
        "generales_disponibles": {k: len(v) for k, v in candidatos.items()},
        "generales_descartados": dict(motivos.most_common()),
    }
    (Path("reportes") / "reporte_exportacion.json").write_text(json.dumps(reporte, ensure_ascii=False, indent=2),
                                                              encoding="utf-8")
    print("=== Exportación vertex-salvador ===")
    print(f"Total: {total} | train: {len(train)} | val: {len(val)}")
    print("Por origen:", dict(origen), "->", reporte["porcentajes"])
    print(f"Propios: {len(propios)} | con llamadas a herramientas: {reporte['propios_con_llamadas']} | "
          f"sin sistema: {sin_sistema}")
    print("Generales con herramientas declaradas:", reporte["generales_con_herramientas_declaradas"])
    print("Escrito: exportacion\\gemma_train.jsonl, exportacion\\gemma_val.jsonl, reportes\\reporte_exportacion.json")


if __name__ == "__main__":
    main()
