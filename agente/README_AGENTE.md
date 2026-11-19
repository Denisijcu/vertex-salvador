# Servidor de herramientas de vertex-salvador

`servidor_mcp.py` le da al modelo las 4 herramientas con las que se entrenó, con el mismo formato de respuesta. La
instalación completa, paso a paso, está en `..\GUIA_INSTALACION.md`. Aquí solo lo esencial.

## Instalar (Windows)
Doble clic en `instalar.bat`. Crea un entorno `.venv` dentro de esta carpeta (no toca el Python del sistema), instala
`mcp`, prueba el servidor (debe decir `TODO OK`) y muestra el bloque exacto para el `mcp.json` de LM Studio
(**Program → Install → Edit mcp.json**).

## Archivos
| Archivo | Qué es |
|---|---|
| `servidor_mcp.py` | El servidor MCP (funciona con `mcp` 1.x y 2.x) |
| `instalar.bat` | Instalador para Windows |
| `mostrar_config.py` | Imprime el bloque para `mcp.json` con las rutas de esta carpeta |
| `probar_servidor.py` | Pruebas sin LM Studio; termina en `TODO OK` |
| `SISTEMA.txt` | La instrucción de sistema con la que se entrenó el modelo: se pega tal cual en LM Studio |
| `cifras.json` | Tabla de cifras, cada fila con su atribución y el fragmento que la sostiene |
| `docs_privados\` | Documentos propios que el buscador puede consultar; no entran al entrenamiento ni al repositorio |

Esta carpeta tiene que quedarse dentro del proyecto: el servidor lee `..\fuentes\`.

## Ajustes en LM Studio
Context Length **8192** al cargar · Temperature 0.3 · Repeat Penalty 1.05 · Enable Thinking **desactivado** ·
System Prompt: el contenido de `SISTEMA.txt`.

## Herramientas
| Herramienta | Qué hace |
|---|---|
| `buscar_documentos` | BM25 sobre los fragmentos aprobados y los documentos privados. La época es una preferencia, no un filtro: si el modelo elige mal la época, el documento correcto sale igual. Descarta resultados que solo coinciden en una palabra suelta |
| `leer_documento` | Abre un fragmento completo o un documento privado entero (o un rango de trozos, `"2-4"`) |
| `consultar_cifras` | Filas de `cifras.json` con su atribución |
| `linea_tiempo` | Fragmentos de una época o de un rango de años, en orden (hasta 25; avisa si hay más) |

## Documentos privados en PDF o Word
Desde esta carpeta:
```
.venv\Scripts\python.exe -m pip install pypdf python-docx
```
