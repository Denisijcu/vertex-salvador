"""
preparar_kaggle.py — Deja en E:\\vertex-salvador\\kaggle_subir\\ EXACTAMENTE los 3 archivos que se suben al dataset
de Kaggle, y nada más:
    entrenar_kaggle.py    gemma_train.jsonl    gemma_val.jsonl

Uso (desde E:\\vertex-salvador):
    python exportar.py
    python preparar_kaggle.py
"""
import hashlib
import json
import shutil
import sys
from collections import Counter
from pathlib import Path

ORIGEN, DESTINO, SCRIPT = Path("exportacion"), Path("kaggle_subir"), Path("entrenar_kaggle.py")
for p in (ORIGEN / "gemma_train.jsonl", ORIGEN / "gemma_val.jsonl", SCRIPT):
    if not p.exists():
        sys.exit(f"No encuentro {p}. ¿Estás en E:\\vertex-salvador y corriste antes exportar.py? No hago nada.")

DESTINO.mkdir(exist_ok=True)
for nombre in ("gemma_train.jsonl", "gemma_val.jsonl"):
    filas = [json.loads(l) for l in open(ORIGEN / nombre, encoding="utf-8") if l.strip()]
    if not filas:
        sys.exit(f"{nombre} está vacío. No hago nada.")
    shutil.copy2(ORIGEN / nombre, DESTINO / nombre)
    c = Counter(f["origen"] for f in filas)
    total = sum(c.values())
    con_llamadas = sum(1 for f in filas if any(m.get("tool_calls") for m in f["messages"]))
    print(f"{nombre}: {total} ejemplos {dict(c)} -> "
          f"{ {k: round(100 * v / total, 1) for k, v in c.items()} } | con llamadas a herramientas: {con_llamadas}")
shutil.copy2(SCRIPT, DESTINO / SCRIPT.name)
print("=== kaggle_subir listo ===")
for f in sorted(DESTINO.iterdir()):
    print(f"  {f.name:22} {f.stat().st_size:>10} bytes  sha256 {hashlib.sha256(f.read_bytes()).hexdigest()[:8]}")
print("Sube al dataset de Kaggle SOLO estos 3 archivos.")
