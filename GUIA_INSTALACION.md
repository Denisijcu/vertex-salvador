# vertex-salvador — Guía de instalación y uso

**Versión 1 · 19 de noviembre de 2026**
Autor: Denis Sánchez Leyva — Vertex Coders LLC (Miami, Florida)

Esta guía explica, paso a paso, cómo instalar y usar **vertex-salvador** en una computadora con Windows. No hace falta
saber programar: basta con seguir los pasos en orden. La instalación completa toma unos 30 minutos, casi todos de
descarga.

---

## 1. Qué es vertex-salvador

vertex-salvador es un asistente de inteligencia artificial que funciona **dentro de la propia computadora, sin
conexión a servicios externos**. Explica la historia de El Salvador desde la reforma agraria de 1881 hasta noviembre
de 2026: el levantamiento de 1932, la guerra civil y los Acuerdos de Paz, el origen de las pandillas, la tregua de 2012,
el gobierno de Nayib Bukele, el régimen de excepción, el CECOT y la participación salvadoreña en Haití.

Tiene dos partes que trabajan juntas:

| Parte | Qué es | Dónde está |
|---|---|---|
| **El modelo** | Un modelo de lenguaje (Gemma 4 E4B de Google, afinado para este fin) en un archivo de unos 5,3 GB | Hugging Face: `Denisijcu/vertex-salvador-GGUF` |
| **El servidor de herramientas** | Un pequeño programa en Python que le da al modelo una biblioteca de documentos verificados | Esta carpeta: `agente\` |

El modelo **no responde de memoria**: antes de dar una fecha, una cifra o un nombre, consulta la biblioteca con sus
herramientas y responde a partir de lo que encuentra. Si el dato no está, lo dice.

### Cómo responde: neutralidad y atribución

El modelo está construido para **contar lo que pasó y decir quién afirma cada cosa**. En la práctica:

- Los **hechos documentados** (una ley, una fecha, una votación) los da como hechos, con su fuente.
- Las **cifras y afirmaciones de una parte** las atribuye siempre: "según la Policía Nacional Civil…", "según el
  Tribunal Supremo Electoral…", "según Cristosal…".
- Cuando hay **versiones enfrentadas** (por ejemplo, entre el gobierno y organizaciones de derechos humanos), presenta
  cada versión con su autor y no da un veredicto propio.

Esta regla vale igual para todas las partes: el gobierno, la oposición, las organizaciones civiles, los organismos
internacionales y la prensa. Es importante saberlo de antemano: si se le pregunta por un tema discutido, el modelo va
a presentar tanto los datos oficiales como las críticas, cada uno con su fuente.

### Qué contiene la biblioteca

- **133 fragmentos verificados**, extraídos de **153 fuentes públicas** (documentos oficiales, agencias de prensa,
  medios salvadoreños e internacionales, estudios académicos e informes de organismos).
- Una **tabla de cifras** con atribución: homicidios, detenciones, prórrogas del régimen de excepción, resultados
  electorales, víctimas de la guerra, ayuda de Estados Unidos y el despliegue en Haití, entre otras.
- Opcionalmente, **documentos propios** de quien lo use (ver la sección 7).

**Fecha de corte:** los datos llegan al **18 de noviembre de 2026**. Lo ocurrido después no está en la biblioteca.

---

## 2. Requisitos

| Elemento | Mínimo | Recomendado |
|---|---|---|
| Sistema operativo | Windows 10 u 11 de 64 bits | Windows 11 |
| Memoria RAM | 16 GB | 32 GB |
| Tarjeta gráfica | No es obligatoria | NVIDIA con 8 GB de memoria o más (responde mucho más rápido) |
| Espacio en disco | 10 GB libres | 20 GB libres |
| Internet | Solo durante la instalación | — |

Programas que hay que instalar (los dos son gratuitos):

1. **LM Studio** — el programa donde se conversa con el modelo: <https://lmstudio.ai>
2. **Python 3.10 o superior** — lo usa el servidor de herramientas: <https://www.python.org/downloads/>

> **Importante al instalar Python:** en la primera pantalla del instalador, marque la casilla
> **"Add python.exe to PATH"** antes de pulsar *Install Now*. Si no se marca, el paso 4 no funcionará.

---

## 3. Descargar los archivos

### 3.1 La carpeta del proyecto

Descargue el repositorio completo de GitHub (botón verde **Code → Download ZIP**) y descomprímalo en una ruta sencilla,
por ejemplo:

```
C:\vertex-salvador
```

En el resto de esta guía se usa esa ruta. Si elige otra, cámbiela donde corresponda.

> **No mueva la carpeta `agente` fuera del proyecto.** El servidor necesita la carpeta `fuentes`, que está a su lado.

### 3.2 El modelo

1. Entre en <https://huggingface.co/Denisijcu/vertex-salvador-GGUF> → pestaña **Files and versions**.
2. Descargue el archivo **`gemma-4-E4B-it.Q4_K_M.gguf`** (unos 5,3 GB). El archivo que termina en `mmproj.gguf` es
   para imágenes y no hace falta.
3. Abra LM Studio → **My Models** (el icono de carpeta de la barra izquierda). Arriba aparece la ruta de la carpeta de
   modelos; normalmente es `C:\Users\<su usuario>\.lmstudio\models`.
4. Dentro de esa carpeta, cree estas dos carpetas, una dentro de otra, y ponga ahí el archivo descargado:

```
C:\Users\<su usuario>\.lmstudio\models\Denisijcu\vertex-salvador-GGUF\gemma-4-E4B-it.Q4_K_M.gguf
```

LM Studio necesita esas dos carpetas (la del autor y la del modelo) para reconocer el archivo. Cierre y vuelva a abrir
LM Studio: el modelo aparecerá en **My Models**.

---

## 4. Instalar el servidor de herramientas

1. Abra la carpeta `C:\vertex-salvador\agente`.
2. Haga doble clic en **`instalar.bat`**.

El instalador hace cuatro cosas y muestra cada paso en pantalla:

| Paso | Qué hace |
|---|---|
| 1/4 | Comprueba que Python 3.10 o superior está instalado |
| 2/4 | Crea un entorno de Python propio (`.venv`) dentro de la carpeta `agente`. **No modifica el Python del sistema.** |
| 3/4 | Instala el paquete `mcp` dentro de ese entorno (necesita internet) |
| 4/4 | Prueba el servidor: todas las comprobaciones deben salir `[OK]` y al final debe decir **`TODO OK`** |

Al terminar, el instalador muestra un bloque de texto como este, ya con las rutas de su computadora:

```json
{
  "mcpServers": {
    "vertex-salvador": {
      "command": "C:\\vertex-salvador\\agente\\.venv\\Scripts\\python.exe",
      "args": [
        "C:\\vertex-salvador\\agente\\servidor_mcp.py"
      ]
    }
  }
}
```

**Deje esa ventana abierta**: el bloque se usa en el paso siguiente. Si la cerró, puede volver a ejecutar
`instalar.bat`; es seguro repetirlo.

---

## 5. Conectar el servidor con LM Studio

1. En LM Studio, abra la pestaña **Program** de la barra lateral derecha y elija **Install → Edit mcp.json**. Se abre
   el archivo dentro de LM Studio.
2. **Si el archivo está vacío** o solo contiene `{"mcpServers": {}}`: reemplace todo su contenido por el bloque que
   mostró el instalador.
3. **Si ya tiene otros servidores**: copie solo la entrada `"vertex-salvador": { … }` y péguela dentro de
   `"mcpServers"`, separada de las demás con una coma.
4. Guarde el archivo (**Ctrl + S**).
5. En la misma pestaña **Program**, compruebe que `vertex-salvador` aparece y está **activado**.

> Las barras invertidas van **dobles** en `mcp.json` (`C:\\vertex-salvador\\…`). Si copia el bloque del instalador,
> ya vienen bien escritas.

---

## 6. Configurar el modelo (una sola vez)

Estos ajustes son **necesarios** para que el modelo funcione como fue entrenado.

### 6.1 Al cargar el modelo

1. En la barra superior de LM Studio, pulse **Select a model to load** y elija `vertex-salvador-GGUF`.
2. Antes de cargarlo, abra las opciones de carga y ponga **Context Length** en **8192**.
3. Pulse **Load Model**.

> **Por qué 8192:** cada consulta a la biblioteca agrega texto a la conversación. Con un contexto menor (por ejemplo,
> 2048), LM Studio recorta la conversación y el modelo pierde el hilo: puede responder a la pregunta anterior en lugar
> de la nueva. Este fallo se comprobó en las pruebas y desaparece con 8192.

### 6.2 Instrucción de sistema y parámetros

En el panel derecho (**Model Parameters**):

| Ajuste | Valor |
|---|---|
| **System Prompt** | Copie y pegue el contenido completo del archivo `agente\SISTEMA.txt` |
| **Temperature** | 0,3 |
| **Repeat Penalty** | 1.05 |
| **Enable Thinking** (sección *Reasoning*) | **Desactivado** |

> Copie la instrucción de sistema **desde `SISTEMA.txt`**, no desde otros archivos del proyecto: es el texto limpio,
> sin comillas ni saltos de línea de código.

Para no repetir estos ajustes, pulse **Save** en la sección *Preset* y guárdelos con el nombre `vertex-salvador`.

---

## 7. Uso diario

1. Abra LM Studio y cargue `vertex-salvador-GGUF` con el preset `vertex-salvador`.
2. En la caja de mensaje, compruebe que aparece la etiqueta **vertex-salvador** (el servidor de herramientas). Si no
   aparece, actívela con el icono de herramientas que está junto a la caja.
3. Escriba la pregunta.

La primera vez que el modelo use una herramienta, LM Studio puede pedir permiso para ejecutarla. Acepte; si lo desea,
puede indicar que lo permita siempre para este servidor.

Debajo del nombre del modelo verá qué herramienta usó (`buscar_documentos`, `consultar_cifras`, `leer_documento` o
`linea_tiempo`). Pulsando la flecha de la derecha se ve exactamente qué consultó y qué encontró: así se puede comprobar
cada respuesta contra su fuente.

### Ejemplos de preguntas

- ¿Qué es el CECOT?
- ¿Por qué se aprobó el régimen de excepción?
- ¿Cuántos homicidios hubo entre 2021 y 2025?
- Hazme una línea de tiempo desde la tregua de 2012 hasta la reelección de 2024.
- ¿Qué está haciendo El Salvador en Haití?
- ¿Qué relación tuvo Cuba con la guerrilla salvadoreña?
- What is the state of exception in El Salvador? *(también responde en inglés)*

### Documentos propios

El servidor también puede consultar documentos internos, sin que salgan de la computadora:

1. Copie los documentos en `C:\vertex-salvador\agente\docs_privados\`.
2. Formatos admitidos: `.txt` y `.md`. Para `.pdf` y `.docx`, instale además dos paquetes en el entorno del servidor,
   desde la carpeta `agente`:
   ```
   .venv\Scripts\python.exe -m pip install pypdf python-docx
   ```
3. Pregunte normalmente, o pida de forma explícita: *"Busca en mis documentos…"*.

El servidor detecta los documentos nuevos o modificados sin reiniciar. Estos documentos **no forman parte del
entrenamiento** del modelo ni se comparten con nadie: solo se leen cuando el modelo los busca.

---

## 8. Límites conocidos

Conviene tenerlos presentes al usar el modelo y al evaluar sus respuestas:

1. **Fecha de corte.** Los datos llegan al 18 de noviembre de 2026. Por ejemplo, el caso de los cuatro aerotécnicos
   desaparecidos en Haití estaba abierto en esa fecha; el modelo lo dice así y no inventa un desenlace.
2. **Solo sabe lo que está en la biblioteca.** No busca en internet. Si una pregunta cae fuera de los temas cubiertos,
   el modelo debe decir que no tiene el dato.
3. **La búsqueda es por palabras.** Si una pregunta usa palabras muy distintas a las de los documentos (por ejemplo,
   "opinión pública" cuando el documento dice "popularidad"), puede no encontrarlo. Reformular la pregunta suele
   resolverlo.
4. **Precisión en las atribuciones.** En las pruebas, el modelo atribuyó alguna vez un dato correcto a una fuente
   equivocada de la misma búsqueda. Para un uso oficial, compruebe la fuente con la flecha de la herramienta (sección 7).
5. **No da opiniones propias** sobre personas o decisiones políticas. Si se le pregunta "¿qué opinas?", presenta los
   hechos y las posturas de cada parte.
6. **Es un modelo pequeño** (unos 8 000 millones de parámetros) pensado para funcionar en una computadora normal. Es
   rápido y privado, pero puede cometer errores de redacción. Sus respuestas no sustituyen a la consulta de las
   fuentes originales.

---

## 9. Solución de problemas

| Síntoma | Causa probable | Solución |
|---|---|---|
| `instalar.bat` dice que no encuentra Python | Python no está instalado o no se marcó "Add python.exe to PATH" | Reinstale Python marcando esa casilla y vuelva a ejecutar `instalar.bat` |
| `instalar.bat` falla en el paso 3/4 | Sin internet o un proxy bloquea la descarga | Compruebe la conexión y vuelva a ejecutarlo |
| El servidor dice que no encuentra `registro_fuentes.csv` | La carpeta `agente` se movió fuera del proyecto | Devuélvala a su sitio, junto a la carpeta `fuentes` |
| El modelo no aparece en **My Models** | El archivo no está en la carpeta `Denisijcu\vertex-salvador-GGUF\` | Revise la sección 3.2 y reinicie LM Studio |
| El modelo responde sin usar herramientas | El servidor no está activado en esa conversación | Active la etiqueta `vertex-salvador` junto a la caja de mensaje (sección 7) |
| `vertex-salvador` aparece con error en la pestaña Program | Ruta incorrecta en `mcp.json` | Vuelva a ejecutar `instalar.bat` y copie el bloque que muestra |
| Responde a la pregunta anterior o pierde el hilo | Contexto demasiado pequeño | Recargue el modelo con **Context Length 8192** (sección 6.1) |
| Tarda mucho en empezar a responder | *Enable Thinking* activado, o sin tarjeta gráfica | Desactive *Enable Thinking*; con tarjeta gráfica NVIDIA es mucho más rápido |
| La respuesta se corta a la mitad | Límite de longitud activado | En *Settings*, desactive **Limit Response Length** |

Para comprobar el servidor en cualquier momento, sin LM Studio, abra una ventana de comandos en la carpeta `agente` y
ejecute:

```
.venv\Scripts\python.exe probar_servidor.py
```

Debe terminar en `TODO OK`.

---

## 10. Cómo se construyó

- **Fuentes:** cada fragmento de la biblioteca se extrajo de una fuente registrada y se revisó con reglas escritas
  (`POLITICA_FUENTES.md`): qué cuenta como hecho, qué se atribuye y qué se rechaza. Las cifras que sostiene una sola
  de las partes se atribuyen siempre a esa parte.
- **Entrenamiento:** 261 conversaciones de ejemplo escritas a partir de esos fragmentos, en español y en inglés, en las
  que el modelo aprende a buscar antes de responder, a atribuir y a reconocer cuándo no tiene un dato. Se mezclaron
  con conversaciones generales para que no pierda su capacidad de conversar. Afinado con QLoRA sobre Gemma 4 E4B.
- **Resultado del entrenamiento:** la pérdida de validación bajó de 2,07 a 1,11.
- **Detalle técnico completo:** `DESARROLLO.md` y `BITACORA.md` en el repositorio.

## 11. Licencia

El modelo base, Gemma 4 E4B de Google, se publica bajo la licencia Apache 2.0, y vertex-salvador se distribuye bajo
esa misma licencia. Los fragmentos de la biblioteca son resúmenes con su fuente original registrada en
`fuentes\registro_fuentes.csv`.
