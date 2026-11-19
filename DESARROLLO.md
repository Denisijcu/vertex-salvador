# vertex-salvador — guía de desarrollo

Cómo se construyó el modelo y cómo se vuelve a entrenar. Para instalarlo y usarlo, ver `GUIA_INSTALACION.md`.

Modelo y agente que hablan de la historia de El Salvador, de las pandillas y del gobierno de Nayib Bukele con la
regla de vertex-exilio: **contar lo que pasó, con su fuente, y atribuir cada versión y cada cifra a quien la da.**

## Estructura
| Ruta | Qué es |
|---|---|
| `POLITICA_FUENTES.md` | Reglas de verificación: tipos de afirmación, niveles de fuente, qué se rechaza |
| `EPOCAS.md` | Las 25 épocas y ejes del dataset, de 1881 a 2026 |
| `herramientas.json` | Contrato fijo de las 4 herramientas (no se cambia después de entrenar) |
| `fuentes\registro_fuentes.csv` | 153 fuentes públicas (S001–S153) y una de prueba privada (S900), con perspectiva y uso |
| `fuentes\fragmentos_lote1.jsonl`, `lote2`, `lote3` | 133 fragmentos aprobados (lote 3: Haití, E15) |
| `agregar_lote1.py`, `agregar_lote2.py`, `agregar_lote3.py` | Generan el registro y los fragmentos |
| `ejemplos_base.py`, `ejemplos_lote_a.py` … `ejemplos_lote_j.py` | Generan los ejemplos; las respuestas de herramienta se construyen solas desde los fragmentos |
| `datos\ejemplos_lote_*.jsonl` | 261 ejemplos de entrenamiento, 256 con llamadas a herramientas |
| `validar.py` | Validador (0 errores en todo) |
| `exportar.py`, `preparar_kaggle.py` | Mezcla 60/25/15 y los 3 archivos para Kaggle |
| `entrenar_kaggle.py` | QLoRA sobre Gemma 4 E4B, máscara para las respuestas de herramienta; entrena, exporta el GGUF y sube todo a Hugging Face en una sola corrida |
| `KAGGLE_PASOS.md` | El procedimiento de Kaggle, siempre igual |
| `agente\servidor_mcp.py` | Servidor MCP con las 4 herramientas, para LM Studio |
| `agente\instalar.bat`, `agente\mostrar_config.py`, `agente\SISTEMA.txt` | Instalador del servidor, bloque para `mcp.json` e instrucción de sistema |
| `agente\cifras.json` | Tabla de cifras con atribución |
| `eval\prueba_bases.jsonl` | Las 10 preguntas para escoger el modelo base en LM Studio |
| `BITACORA.md` | Lo que se hizo y se decidió |

## Orden de trabajo
1. `python validar.py fuentes\fragmentos_lote1.jsonl --fragmentos` (y lote2, lote3) → 0 errores.
2. `python validar.py datos\ejemplos_lote_a.jsonl` (y de la b a la j) → 0 errores.
3. `python exportar.py` y `python preparar_kaggle.py` → `kaggle_subir\`.
4. Kaggle según `KAGGLE_PASOS.md`: primero la prueba corta y, si dice BAJÓ, la corrida larga, que deja el LoRA y el GGUF en Hugging Face.
5. Agente en LM Studio según `GUIA_INSTALACION.md`.
