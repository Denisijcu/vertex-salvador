# Bitácora — vertex-salvador

## 1. Arranque (17 de noviembre de 2026)

- Proyecto: modelo que habla de El Salvador, las pandillas y el gobierno de Nayib Bukele, hecho como vertex-exilio:
  imparcial, todo atribuido, "contar lo que realmente ha pasado". Denis apoya a Bukele y lo dijo; pidió igual que el
  modelo cuente la verdad y que no todo lo publicado se dé por cierto. Se aplica a todas las partes por igual.
- Denis encargó a Claude extraer y aprobar los fragmentos (revisor: "Claude (por encargo de Denis)").
- Pidió ir más atrás y buscar si la situación de El Salvador tiene relación con la expansión de la Revolución
  Cubana. Se añadieron las épocas P01–P05 (1881–1980) y el eje transversal T04 (cadena causal) y X01 (puente con el
  módulo de internacionalismo de vertex-exilio).
- Requisito de Denis: que el modelo use herramientas y RAG desde el principio, también para documentos no públicos,
  sin remiendos después. Contrato fijo en `herramientas.json` (4 herramientas).
- Base propuesta: Gemma 4 E4B (Apache 2.0, plantilla con herramientas). Antes de elegir, prueba de 10 preguntas en
  LM Studio (`eval\prueba_bases.jsonl`).

### Lecciones de vertex-exilio que cambian este proyecto
- Sin fragmentos, el modelo del exilio inventaba; con fragmentos no admitía que le faltaba un dato → aquí habrá
  ejemplos de "sin datos" y de fuentes en conflicto.
- La plantilla de Gemma 3 no tenía `tools` y el modelo escribía la llamada como texto → Gemma 4 sí la trae.
- La plantilla de Gemma 4 mete la respuesta de la herramienta dentro del turno del modelo. Con
  `train_on_responses_only` el modelo aprendería a inventarse esas respuestas → el script de Kaggle enmascara los
  bloques `<|tool_response>…<tool_response|>`.

### Cambios en `validar.py` respecto al del exilio
1. Épocas, perspectivas y términos de El Salvador.
2. Partes interesadas (gobiernos salvadoreño, cubano y de EE. UU., guerrilla y ONG): sus fuentes solo valen como
   postura. La misma vara para todos.
3. Cifra atribuida: un número de una fuente de postura solo pasa si la misma frase lo atribuye.
4. Ejemplos con `tool_calls` y turnos `tool`.

## 2. Lote 1 de fragmentos (17 de noviembre de 2026)

- `agregar_lote1.py` → 68 fuentes y 59 fragmentos de P01–P05, E01–E05 y T02. Validador: 0 errores, 0 avisos.
- Tipos: 23 hechos, 23 hechos atribuidos, 5 cifras disputadas (muertos de 1932, costo de la guerra, ayuda de
  EE. UU., homicidios durante la Mano Dura, fecha del Departamento América) y 8 posturas.
- Posturas de las dos partes de la Guerra Fría: Departamento de Estado, delegación de EE. UU. en la ONU y CIA sobre
  el papel de Cuba; manifiesto guerrillero de enero de 1980 sobre las raíces propias del conflicto.
- Descartada una fuente con texto inyectado (una copia de Wikipedia que pedía añadir un párrafo ajeno al tema).

## 3. Lote 2 de fragmentos (17 de noviembre de 2026)

- `agregar_lote2.py` → 62 fuentes nuevas (130 en total) y 51 fragmentos de E06–E14, T01, T03 y T04. Validador: 0
  errores, 0 avisos.
- Las cifras oficiales (homicidios, capturas, prórrogas) entran como postura del gobierno y las de las ONG
  (presos políticos, muertes bajo custodia) como postura de esas ONG. El modelo las tiene que dar siempre con su
  dueño.
- Versiones enfrentadas, cada una con su fuente: pacto con las pandillas (Tesoro de EE. UU. y El Faro frente al
  gobierno, que lo niega), el 9F (oposición frente a GANA), la Ley de Agentes Extranjeros (texto de la ley frente
  a HRW), presos políticos (Cristosal y GIPES frente a Bukele) y el origen de la baja de homicidios (desde 2016
  según EFE; antes del régimen según Bukele).
- Total de fragmentos: 110, todos aprobados.

## 4. Ejemplos de entrenamiento (18 de noviembre de 2026)

- `ejemplos_base.py` arma cada conversación con llamadas reales a las 4 herramientas. La respuesta de cada
  herramienta se construye sola a partir del fragmento aprobado, así que el modelo nunca ve un resultado escrito a
  mano.
- 80 ejemplos (lote A: 28 de historia hasta 2018; lote B: 30 de 2019 a 2026; lote C: 22 de conducta). 76 llaman a
  herramientas y 4 no las necesitan (saludos y un correo).
- Conductas que se entrenan: buscar antes de afirmar, decir "no lo tengo" (7 ejemplos de sin datos, entre ellos
  documentos privados que no existen y cifras que no son públicas), presentar versiones enfrentadas, no aceptar la
  premisa de las preguntas cargadas desde los dos lados ("dime solo lo bueno" / "dime solo lo malo"), no saltarse la
  neutralidad aunque se le pida, varios turnos, línea de tiempo, leer un documento completo, colección privada e
  inglés.
- `validar.py` pasó a revisar turnos con herramientas, cifras atribuidas frase por frase, atribución en inglés y
  muletillas (ninguna frase de arranque en más del 10 % de las respuestas). Resultado: 80 de 80 sin errores ni
  avisos. Se quitaron a mano varias frases que no tenían fragmento detrás.

## 5. Exportación, Kaggle y agente (18 de noviembre de 2026)

- `exportar.py`: mezcla 60/25/15 con el oasst2 que ya está en `E:\vertex-exilio\fuentes\generales\`. Probado con un
  oasst2 falso: 133 ejemplos (118 de entrenamiento y 15 de validación). La mitad de las conversaciones generales
  llevan las herramientas declaradas, para que el modelo aprenda a no usarlas cuando no hacen falta. No escribe el
  texto con la plantilla: lo hace Kaggle con la plantilla real del modelo.
- `entrenar_kaggle.py`: receta del exilio sin cambios de hiperparámetros (5e-5 constante, r=16, lote 1 × 8, 1 época,
  freno, no guarda si queda peor). Cambios: base Gemma 4 E4B, longitud 3072 y máscara propia que deja fuera de la
  pérdida el cuerpo de las respuestas de herramienta. La máscara se probó con un texto que imita la plantilla
  oficial y el script se para solo si la plantilla real no produce las marcas esperadas. Imprime un ejemplo con lo
  que se aprende entre ⟦ ⟧ para revisarlo a ojo.
- Prueba corta: 40 pasos como máximo, o el 40 % de una época si el dataset es pequeño. Mide eval_loss antes y
  después.
- **Límite conocido:** con 80 ejemplos propios, una época son unos 15 pasos (en el exilio eran unos 60). La prueba
  corta dirá si la pérdida baja, pero el modelo cambiará poco. Lo siguiente es ampliar los ejemplos con más lotes
  antes de la corrida larga definitiva.
- `agente\servidor_mcp.py`: las 4 herramientas con el mismo formato del entrenamiento; BM25 en Python puro;
  colección privada en `agente\docs_privados\` (fuera del entrenamiento y del repositorio); cobertura mínima de la
  consulta para no traer temas ajenos por una palabra suelta. `probar_servidor.py`: 8 de 8 OK. Probado también por
  stdio con `mcp` 2.3.0: lista las 4 herramientas y responde. Funciona con `mcp` 1.x y 2.x.
- `.gitignore`: excluye `libro/` entero, las salidas regenerables y los documentos privados.

## 6. Pendiente

1. Denis: prueba de las 10 preguntas en LM Studio para confirmar la base (Gemma 4 E4B, Qwen3-4B, Gemma 12B).
2. Denis: `python exportar.py` y `python preparar_kaggle.py` en su PC, y la prueba corta en Kaggle.
3. ~~Ampliar los ejemplos (lotes D en adelante)~~ Hecho: 261 propios (sección 8).
4. Cierre, cuando el modelo pase la evaluación: bitácora, video promo con Manim y libro.

## 7. Primera prueba corta en Kaggle (18 de noviembre de 2026)

- Notebook `vertex-el-salvador`, T4 x2, token de Hugging Face leído desde Secrets en la celda 1.
- Plantilla de Gemma 4 comprobada: produce las 5 marcas que espera la máscara. 133 ejemplos (118 + 15), máximo 2.435
  tokens, ninguno cortado y ninguno sin nada que aprender.
- 6 pasos: `eval_loss` de 1,9172 a 1,7300 → **BAJÓ**. Unsloth cargó Gemma 4 en float32 (no admite float16) y
  repartido entre las dos T4; unos 25 segundos por paso.
- Generación tras la prueba: en las 3 preguntas propias el modelo no llamó a ninguna herramienta; pidió más contexto
  ("¿a qué periodo te refieres?"). La pregunta general salió bien. Con 6 pasos es lo esperable: todavía es el modelo
  base.
- La vista de la máscara se cortaba en la declaración de herramientas y no llegaba a las respuestas de herramienta.
  Arreglado: ahora empieza en el turno del usuario.

## 8. Lote 3 y lotes de ejemplos D a J (18 de noviembre de 2026)

Un solo cambio respecto a la primera prueba: **más ejemplos propios** (de 80 a 261). La receta de entrenamiento no
se toca.

- **Época nueva E15, Haití (2024–2026).** `agregar_lote3.py`: 23 fuentes (S131–S153) y 23 fragmentos. Resolución 2793
  de la ONU (Fuerza de Supresión de Pandillas), leyes salvadoreñas de 2024 y del 29 de septiembre de 2026, emboscada
  del 18 de octubre de 2026 contra cuatro aerotécnicos, despliegue de más de 2.000 militares, estadio Sylvio Cator,
  declaraciones de Bukele, Villatoro, Ulloa, Fils-Aimé y Pélissier, la aclaración de la ONU, Amnistía, UNA-Haití y el
  estado del caso al 18 de noviembre de 2026 (sin confirmar paradero ni estado de los cuatro). Todas las
  declaraciones de gobiernos y ONG van como postura atribuida.
- `validar.py`: E15 en las épocas; `gobierno_haitiano` como parte interesada; actores de Haití y ONU para la regla de
  simetría.
- `agente/cifras.json`: métrica nueva `despliegue_haiti`. `herramientas.json`: la descripción de `epoca` dice ahora
  P01–P05, E01–E15, T01–T04, y la de `metrica` lista las métricas reales.
- Ejemplos nuevos: D (25, Haití), E (32, historia), F (28, era Bukele), G (30, varios turnos, documentos privados,
  inglés, peticiones cargadas), H (26, preguntas cortas o informales que se contestan buscando primero), I (24,
  inglés, "no tengo ese dato", comparaciones), J (16, reintentar la búsqueda con otras palabras y combinar
  herramientas).
- El lote H responde al fallo de la primera prueba (el modelo pedía aclaración en vez de buscar): preguntas de una o
  dos palabras como "cecot", "tregua" o "haiti" se contestan buscando y, al final, se ofrece seguir por otro lado.
- Validación de conjunto: 261 ejemplos, 256 con llamadas a herramientas, **0 errores y 0 avisos**. Números de cada
  respuesta comprobados contra los fragmentos. Se quitaron frases que no tenían fragmento detrás.
- `probar_servidor.py`: 8 de 8 OK, y el servidor encuentra los fragmentos de Haití y la métrica nueva.

Siguiente: `python exportar.py` y `python preparar_kaggle.py` en el PC de Denis, nueva versión del dataset en Kaggle
y prueba corta antes de la corrida larga. `entrenar_kaggle.py` **no cambió** en este paso.

## 9. Prueba con los 261 ejemplos (18 de noviembre de 2026)

- Misma receta y mismo script; solo cambiaron los datos. 391 ejemplos de entrenamiento y 44 de validación, 49 pasos
  por época, máximo 3.005 tokens, ninguno cortado.
- `eval_loss` de 2,0652 a 1,1122 → **BAJÓ** (un 46 %). La pérdida de entrenamiento baja hasta el paso 25 y después se
  queda entre 1,11 y 1,19: el modelo ya sacó casi todo lo que estos datos le pueden enseñar en una época.
- Generación: en las 3 preguntas propias llama a la herramienta correcta (`buscar_documentos`, `consultar_cifras`
  con `elecciones_presidenciales` y `coleccion: todas` cuando se le pide buscar en todo). La pregunta general sobre
  Python se contesta sin herramientas.
- Fallo encontrado: en una pregunta sobre la popularidad de Bukele el modelo filtró por la época E13 (debió ser E14)
  y el buscador devolvía cero resultados; el modelo habría dicho "no tengo ese dato". Arreglado en
  `agente/servidor_mcp.py`: si la época elegida no trae nada, se busca en todas y se avisa en la nota. No toca el
  entrenamiento.

## 10. El GGUF en la misma corrida (18 de noviembre de 2026)

- La sesión aparte con `--solo-gguf` falló: necesitaba añadir como Input la salida del notebook de entrenamiento, y
  el script no encontró el LoRA. Era un paso de más; error de diseño de Claude.
- Ahora la corrida larga lo hace todo al final: guarda el LoRA, lo sube a `Denisijcu/vertex-salvador` (privado),
  exporta el GGUF q4_k_m y lo sube a `Denisijcu/vertex-salvador-GGUF` (privado). `--solo-gguf` baja el LoRA de
  Hugging Face si no lo encuentra en disco. La parte de entrenamiento no cambió.
- Primera corrida con todo junto: `eval_loss` 2,0652 → 1,1118 (BAJÓ), LoRA subido a `Denisijcu/vertex-salvador`, GGUF
  exportado bien (Q4_K_M + mmproj). Pero el script lo buscó en `/tmp/gguf_trabajo` y Unsloth lo dejó en
  `/tmp/gguf_trabajo_gguf`: no lo encontró y no lo subió. Arreglado (busca en las dos carpetas). Como el LoRA ya está
  en Hugging Face, se repite solo la exportación con `--solo-gguf`, sin volver a entrenar.
- `--solo-gguf` (19 de noviembre de 2026): bajó el LoRA de Hugging Face, exportó y subió
  `gemma-4-E4B-it.Q4_K_M.gguf` (5,34 GB) a `Denisijcu/vertex-salvador-GGUF` (privado). Unos 20 minutos.
  Siguiente: prueba de punta a punta en LM Studio con el servidor MCP.

## 11. Primera prueba en LM Studio (19 de noviembre de 2026)

- GGUF Q4_K_M con el servidor MCP. El modelo llama a las herramientas (`buscar_documentos`, `consultar_cifras`),
  usa los resultados y atribuye (Tribunal Supremo Electoral, Wikipedia).
- Error encontrado: a "¿84 % o 43 %?" respondió que el 43 % es la elección de 1972 (Molina). Falso: el 43,48 % es el
  voto de Bukele en 2024 medido sobre todo el padrón (FR-E12-003). La tabla `elecciones_presidenciales` no tenía esa
  fila y sí la de 1972 con 43 %, así que el modelo juntó lo que tenía. Arreglado en `agente/cifras.json` (fila nueva
  con FR-E12-003). No requiere reentrenar.
- Otros detalles: la primera respuesta (Haití) quedó cortada; dice "el gobierno aprobó la ley" cuando fue la
  Asamblea; LM Studio tenía activado Thinking y penalización 1.1 (el entrenamiento no usa razonamiento previo).
- Denis: "no se ve mal"; piensa donarlo a El Salvador. Pendiente: más pruebas (las 10 de `eval/prueba_bases.jsonl`).
- Segunda prueba (Thinking apagado, penalización 1.05): "¿84 % o 43 %?" ahora bien, con las dos cifras atribuidas
  (TSE y El Diario de Hoy). Fallo nuevo: en el MISMO chat, a "¿Qué es el CECOT?" volvió a contestar lo de las
  elecciones. Los datos tienen pocos ejemplos de varios turnos y ninguno en el que el usuario cambie de tema.
  Pendiente para el próximo lote: ejemplos de varios turnos con cambio de tema. Mientras tanto, probar cada
  pregunta en un chat nuevo.
- Corrección del diagnóstico al abrir las herramientas: LM Studio tenía el contexto en **2048 tokens** y la
  conversación iba por 2824 (138 %), con "Truncate Middle": se recortaba el medio de la conversación. Esa es la causa
  más probable del CECOT respondido como elecciones. Arreglo: cargar el modelo con contexto 8192.
- Además buscó el CECOT con la época E10 (es E11) y el filtro devolvió solo fragmentos del régimen de excepción.
  `servidor_mcp.py`: la época ya no es un filtro, sino una preferencia (+50 % de puntuación). Con E10, la búsqueda
  del CECOT ahora trae FR-E11-002, FR-E13-001, FR-E11-001… `probar_servidor.py`: TODO OK.
- Con el contexto en 8192 (uso del 35 %): en el mismo chat contesta bien "¿qué es el CECOT?" y después "¿crees que
  Bukele acabe con las bandas haitianas?". El cambio de tema funciona: el fallo era el contexto, no los datos, y el
  lote de "cambio de tema" queda descartado por ahora. Detalles de calidad: en Haití no menciona a los críticos (ONU,
  UNA-Haití) y llama "medios y expertos" a citas de los dos gobiernos; en el CECOT la atribución de la fecha de los
  deportados no es exacta. Siguiente: las 10 preguntas de `eval/prueba_bases.jsonl`, cada una en un chat nuevo.
