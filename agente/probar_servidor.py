"""
probar_servidor.py — Prueba las 4 herramientas sin LM Studio ni MCP (no necesita nada instalado).

Uso (desde E:\\vertex-salvador\\agente):
    python probar_servidor.py
Sale 'TODO OK' si todas las comprobaciones pasan (y devuelve código 1 si alguna falla, para instalar.bat).
"""
import json
import sys

import servidor_mcp as s

fallos = 0


def ver(nombre, salida, condicion):
    global fallos
    d = json.loads(salida)
    ok = condicion(d)
    fallos += 0 if ok else 1
    print(f"[{'OK' if ok else 'FALLA'}] {nombre}")
    primero = (d.get("resultados") or d.get("eventos") or d.get("filas") or [d.get("documento")])[:1]
    if primero and primero[0]:
        print("       ", json.dumps(primero[0], ensure_ascii=False)[:220], "…")


ver("buscar: régimen de excepción", s.h_buscar_documentos("¿por qué se aprobó el régimen de excepción?"),
    lambda d: any(r["doc_id"].startswith("FR-E10") for r in d["resultados"]))
ver("buscar: Cuba y el FMLN, prefiere la época P05", s.h_buscar_documentos("Cuba FMLN La Habana", epoca="P05"),
    lambda d: d["total"] > 0 and d["resultados"][0]["epoca"] == "P05")
ver("buscar: CECOT con la época equivocada igual lo encuentra", s.h_buscar_documentos("CECOT El Salvador", epoca="E10"),
    lambda d: any(r["doc_id"] == "FR-E11-001" for r in d["resultados"]))
ver("buscar: Haití, la emboscada", s.h_buscar_documentos("soldados salvadoreños emboscada Haití"),
    lambda d: any(r["doc_id"] == "FR-E15-007" for r in d["resultados"]))
ver("buscar: algo que no existe da lista vacía con nota", s.h_buscar_documentos("receta de pupusas revueltas"),
    lambda d: d["total"] == 0 and "nota" in d)
ver("buscar: colección privada", s.h_buscar_documentos("bitácora", coleccion_="privada"),
    lambda d: all(r["coleccion"] == "privada" for r in d["resultados"]))
ver("leer documento FR-E01-004", s.h_leer_documento("FR-E01-004"),
    lambda d: d["documento"] and "Comisión de la Verdad" in d["documento"]["texto"])
ver("cifras: homicidios 2021-2025", s.h_consultar_cifras("homicidios", "2021", "2025"),
    lambda d: [f["periodo"] for f in d["filas"]] == ["2021", "2022", "2023", "2024", "2025"])
ver("cifras: métrica que no existe", s.h_consultar_cifras("pib_per_capita"),
    lambda d: d["total"] == 0 and "metricas_disponibles" in d)
ver("cifras: elecciones con el 84,65 % y el 43,48 %", s.h_consultar_cifras("elecciones_presidenciales"),
    lambda d: {"FR-E12-001", "FR-E12-003"} <= {f["doc_id"] for f in d["filas"]})
ver("cifras: despliegue en Haití", s.h_consultar_cifras("despliegue_haiti"), lambda d: d["total"] == 3)
ver("línea de tiempo E09", s.h_linea_tiempo("E09"), lambda d: d["total"] > 0)
ver("línea de tiempo E15 (Haití)", s.h_linea_tiempo("E15"), lambda d: d["total"] > 0)
print("\nTODO OK" if not fallos else f"\n{fallos} comprobaciones fallaron")
sys.exit(1 if fallos else 0)
