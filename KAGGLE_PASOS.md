# Cómo entrenar vertex-salvador en Kaggle (siempre igual)

Es el mismo procedimiento de vertex-exilio. Lo único nuevo es que **primero va la prueba corta** y, solo si dice
BAJÓ, la corrida larga.

## Regla
Cada vez que Claude cambie un script de entrenamiento, lo dice con estas palabras: **"HAY QUE SUBIRLO AL DATASET"**.
Si no lo dice, no hay nada que subir.

## 1. Preparar los 3 archivos (en tu PC)
Desde `E:\vertex-salvador`:
```
python exportar.py
python preparar_kaggle.py
```
`exportar.py` usa el oasst2 que ya tienes en `E:\vertex-exilio\fuentes\generales\` (no hay que bajar nada).
Solo usa la biblioteca estándar de Python: no instala ni cambia ningún paquete.

Eso deja en **`E:\vertex-salvador\kaggle_subir\`** los únicos 3 archivos que se suben:
`entrenar_kaggle.py` · `gemma_train.jsonl` · `gemma_val.jsonl`

## 2. El dataset y el notebook (una sola vez)
1. Kaggle → **Datasets → New Dataset** → nombre `vertex-salvador` → subir los 3 archivos de `kaggle_subir`.
2. **New Notebook** → Settings: Accelerator **GPU T4 x2** · Internet **On** · panel **Input** → Add Input → el dataset
   `vertex-salvador`.
3. Tokens o contraseñas: nunca en una celda; si hacen falta, **Add-ons → Secrets** (`HF_TOKEN`).

## 3. La prueba corta (obligatoria, ~15-20 minutos)
El notebook tiene SOLO estas dos celdas:
```
!pip install -q unsloth
```
```
!python "$(find /kaggle/input -name entrenar_kaggle.py | head -1)" --prueba
```
**Save Version → Save & Run All (Commit)**. Al terminar, en **Logs**, mira tres cosas:
1. El ejemplo impreso al principio: lo que el modelo aprende va entre ⟦ ⟧. Las respuestas de las herramientas
   (`response:buscar_documentos{…}`) tienen que quedar **fuera** de los ⟦ ⟧.
2. La línea `eval_loss ANTES … | DESPUÉS … | BAJÓ` o `SUBIÓ`.
3. Las 4 salidas en crudo del final: en las preguntas propias debería aparecer `<|tool_call>call:buscar_documentos{…}`.

Si dice **SUBIÓ** o **FRENO**, no se lanza la corrida larga: copia el log y se revisa.

## 4. La corrida larga (entrena, exporta y sube todo)
Cambia la segunda celda quitando `--prueba`:
```
!python "$(find /kaggle/input -name entrenar_kaggle.py | head -1)"
```
**Save & Run All (Commit)**. Se puede cerrar el navegador. Si la pérdida bajó, al final hace solo:
1. Guarda el LoRA y lo sube (privado) a `Denisijcu/vertex-salvador`.
2. Exporta el GGUF q4_k_m y lo sube (privado) a `Denisijcu/vertex-salvador-GGUF`.

El log termina en `TERMINADO`. El `.gguf` para LM Studio se baja de Hugging Face. No hace falta añadir ningún
Input ni abrir otra sesión. Necesita `HF_TOKEN` en **Add-ons → Secrets**. Si dice SUBIÓ o FRENO, no guarda ni sube
nada y ese modelo no se usa.

## 5. Volver a sacar solo el GGUF (si algún día falla esa parte)
`!python "$(find /kaggle/input -name entrenar_kaggle.py | head -1)" --solo-gguf`
Baja el LoRA de `Denisijcu/vertex-salvador` y vuelve a exportar y subir el GGUF. Tampoco necesita otro Input.

## Cuando cambian los datos
Si se añaden fragmentos o ejemplos: `python validar.py ...` (0 errores) → `python exportar.py` →
`python preparar_kaggle.py` → Kaggle: tu dataset → **New Version** → subir los 3 archivos → en el notebook, Input →
tres puntos → **Check for updates** → prueba corta otra vez.
