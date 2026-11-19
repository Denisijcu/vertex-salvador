---
license: apache-2.0
base_model: unsloth/gemma-4-E4B-it-unsloth-bnb-4bit
language:
- es
- en
library_name: peft
pipeline_tag: text-generation
tags:
- lora
- qlora
- unsloth
- gemma4
- tool-use
- mcp
- el-salvador
---

# vertex-salvador (adaptador LoRA)

Adaptador LoRA de **vertex-salvador**: Gemma 4 E4B afinado para explicar la historia de El Salvador buscando en una
biblioteca de documentos verificados y atribuyendo cada versión y cada cifra a quien la sostiene.

**Para usar el modelo en LM Studio no hace falta este repositorio:** descargue el GGUF de
[Denisijcu/vertex-salvador-GGUF](https://huggingface.co/Denisijcu/vertex-salvador-GGUF). Este adaptador sirve para
reentrenar, combinar con el modelo base o exportar a otros formatos.

## Contenido

| Archivo | Qué es |
|---|---|
| `adapter_model.safetensors` | Pesos del adaptador (140 MB) |
| `adapter_config.json` | Configuración LoRA y modelo base |
| `chat_template.jinja`, `tokenizer.json`, `tokenizer_config.json`, `processor_config.json` | Plantilla de chat de Gemma 4 (con herramientas) y tokenizador |

## Cargarlo con Unsloth

```python
from unsloth import FastModel

model, tokenizer = FastModel.from_pretrained(
    model_name="Denisijcu/vertex-salvador",
    max_seq_length=3072,
    load_in_4bit=True,
)
```

## Entrenamiento

| Elemento | Valor |
|---|---|
| Modelo base | `unsloth/gemma-4-E4B-it-unsloth-bnb-4bit` (Gemma 4 E4B de Google) |
| Método | QLoRA, r = 16, alpha = 16, solo capas de lenguaje |
| Datos | 261 conversaciones propias en español e inglés (256 con llamadas a herramientas) + conversaciones generales de oasst2 (60/25/15) |
| Máscara | Solo aprenden los turnos del modelo; el contenido devuelto por las herramientas queda fuera de la pérdida |
| Hiperparámetros | Tasa 5e-5 constante, lote efectivo 8, 1 época, longitud máxima 3072 |
| Resultado | Pérdida de validación de 2,0652 a 1,1118 (44 ejemplos) |

## Licencia

Apache 2.0, la misma licencia del modelo base Gemma 4.

## Autor

Denis Sánchez Leyva — Vertex Coders LLC, Miami, Florida.
