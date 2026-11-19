---
license: apache-2.0
base_model: google/gemma-4-E4B-it
language:
- es
- en
pipeline_tag: text-generation
library_name: gguf
tags:
- gguf
- gemma4
- tool-use
- mcp
- rag
- el-salvador
- history
- lm-studio
---

# vertex-salvador (GGUF)

**Asistente local que explica la historia de El Salvador con fuentes y con neutralidad.**

Este repositorio contiene el modelo en formato GGUF, listo para [LM Studio](https://lmstudio.ai): Gemma 4 E4B de Google
afinado con QLoRA para **buscar antes de responder, atribuir cada versión y cada cifra a quien la sostiene, y decir
cuándo no tiene un dato**.

El modelo está pensado para usarse **junto con su servidor de herramientas (MCP)**, que le da acceso a una biblioteca
de 133 fragmentos verificados de 153 fuentes públicas. Sin el servidor, el modelo conversa pero no tiene de dónde
sacar los datos.

> **Instalación paso a paso:** ver `GUIA_INSTALACION.md` en el repositorio de GitHub del proyecto.

## Archivos

| Archivo | Tamaño | Uso |
|---|---|---|
| `gemma-4-E4B-it.Q4_K_M.gguf` | 5,3 GB | **El modelo.** Es el único archivo necesario para texto y herramientas |
| `gemma-4-E4B-it.F16-mmproj.gguf` | 990 MB | Proyector de visión de Gemma 4. No hace falta para este uso |

## Uso en LM Studio

1. Descargue `gemma-4-E4B-it.Q4_K_M.gguf` y colóquelo en
   `C:\Users\<usuario>\.lmstudio\models\Denisijcu\vertex-salvador-GGUF\`.
2. Instale el servidor de herramientas ejecutando `agente\instalar.bat` del repositorio de GitHub, y copie en el
   `mcp.json` de LM Studio el bloque que muestra (pestaña **Program → Install → Edit mcp.json**).
3. Configuración **necesaria**:

| Ajuste | Valor |
|---|---|
| Context Length (al cargar) | **8192** |
| System Prompt | El contenido de `agente/SISTEMA.txt` |
| Temperature | 0.3 |
| Repeat Penalty | 1.05 |
| Enable Thinking | Desactivado |

Con un contexto de 2048 tokens, LM Studio recorta la conversación cuando entran los resultados de las herramientas y
el modelo pierde el hilo. Con 8192 ese problema no aparece.

## Herramientas que espera el modelo

El modelo se entrenó con este contrato exacto (lo implementa el servidor del proyecto):

| Herramienta | Argumentos |
|---|---|
| `buscar_documentos` | `consulta`, `epoca` (opcional), `coleccion` (`publica`, `privada` o `todas`), `max_resultados` |
| `leer_documento` | `doc_id`, `seccion` (opcional) |
| `consultar_cifras` | `metrica`, `desde`, `hasta` |
| `linea_tiempo` | `epoca`, `desde`, `hasta` |

## Cómo responde

- **Hechos documentados** (una ley, una fecha, una votación): como hechos, con su fuente.
- **Cifras o afirmaciones de una parte**: siempre atribuidas ("según la Policía Nacional Civil…", "según Cristosal…").
- **Hechos disputados**: cada versión con su autor, sin veredicto propio.

La regla se aplica por igual al gobierno, la oposición, las organizaciones civiles, los organismos internacionales y la
prensa. El modelo no da opiniones personales sobre personas ni decisiones políticas.

## Entrenamiento

| Elemento | Valor |
|---|---|
| Modelo base | `google/gemma-4-E4B-it` (vía `unsloth/gemma-4-E4B-it-unsloth-bnb-4bit`) |
| Método | QLoRA, r = 16, alpha = 16, solo capas de lenguaje |
| Datos | 261 conversaciones propias (español e inglés; 256 con llamadas a herramientas) mezcladas con conversaciones generales de oasst2 en proporción 60/25/15 (propias / español / inglés) |
| Ejemplos | 391 de entrenamiento y 44 de validación |
| Máscara | La pérdida solo cuenta las llamadas y respuestas del modelo; el contenido devuelto por las herramientas queda fuera, para que el modelo no aprenda a inventarlo |
| Hiperparámetros | Tasa 5e-5 constante, lote efectivo 8, 1 época, longitud máxima 3072 |
| Resultado | Pérdida de validación de 2,0652 a 1,1118 |
| Hardware | Kaggle, 2 × NVIDIA T4 |
| Cuantización | Q4_K_M con llama.cpp |

## Límites

- **Fecha de corte de los datos: 18 de noviembre de 2026.**
- Solo conoce lo que está en su biblioteca; no busca en internet.
- La búsqueda es por palabras: si la pregunta usa términos muy distintos a los del documento, puede no encontrarlo.
- En ocasiones atribuye un dato correcto a otra fuente de la misma búsqueda. Para un uso oficial, compruebe la fuente
  que muestra LM Studio en el detalle de cada herramienta.
- Es un modelo pequeño para uso local: rápido y privado, pero no sustituye a la consulta de las fuentes originales.

## Licencia

Apache 2.0, la misma licencia del modelo base Gemma 4.

## Autor

Denis Sánchez Leyva — Vertex Coders LLC, Miami, Florida.
