"""
mostrar_config.py — Imprime el bloque exacto para el archivo mcp.json de LM Studio, con las rutas de ESTA carpeta.
Lo llama instalar.bat al final. Se puede correr solo (desde la carpeta agente):
    .venv\\Scripts\\python.exe mostrar_config.py
"""
import json
import sys
from pathlib import Path

aqui = Path(__file__).resolve().parent
python_venv = aqui / ".venv" / ("Scripts" if sys.platform == "win32" else "bin") / (
    "python.exe" if sys.platform == "win32" else "python")
if not python_venv.exists():
    sys.exit("No encuentro el entorno .venv en esta carpeta. Ejecuta primero instalar.bat.")

bloque = {"mcpServers": {"vertex-salvador": {"command": str(python_venv), "args": [str(aqui / "servidor_mcp.py")]}}}
print()
print("=" * 78)
print("Copia este bloque en LM Studio: pestaña Program > Install > Edit mcp.json")
print("Si el archivo ya tiene otros servidores, agrega solo la entrada \"vertex-salvador\" dentro de \"mcpServers\".")
print("=" * 78)
print(json.dumps(bloque, indent=2, ensure_ascii=False))
print("=" * 78)
