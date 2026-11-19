# vertex-salvador

**Un asistente de IA local que explica la historia de El Salvador con fuentes y con neutralidad.**

vertex-salvador combina un modelo de lenguaje afinado (Gemma 4 E4B) con un servidor de herramientas
([MCP](https://modelcontextprotocol.io)) que le da acceso a una biblioteca de documentos verificados. Antes de dar una
fecha, una cifra o un nombre, el modelo los busca; después responde atribuyendo cada versión y cada cifra a quien la
sostiene. Funciona completo en una computadora con Windows, con [LM Studio](https://lmstudio.ai), sin enviar datos a
ningún servicio externo.

Cubre de 1881 a noviembre de 2026: la tierra y el café, el levantamiento de 1932, la influencia de la Revolución
Cubana, la guerra civil y los Acuerdos de Paz, el origen de las pandillas en Los Ángeles, la Mano Dura, la tregua de
2012, el gobierno de Nayib Bukele, el régimen de excepción, el CECOT y la participación salvadoreña en Haití.

> **Para instalarlo y usarlo:** [GUIA_INSTALACION.md](GUIA_INSTALACION.md)

---

## Cómo responde

| Tipo de afirmación | Ejemplo | Cómo la presenta el modelo |
|---|---|---|
| Hecho documentado | La fecha de un decreto, una votación | Como hecho, con su fuente |
| Cifra o afirmación de una parte | Homicidios según la Policía; muertes bajo custodia según una ONG | Atribuida: "según…" |
| Hecho disputado | Si hubo un pacto con las pandillas; si hay presos políticos | Cada versión con su autor, sin veredicto propio |

La misma regla se aplica a todas las partes: gobierno, oposición, organizaciones civiles, organismos internacionales y
prensa. Las reglas completas están en [POLITICA_FUENTES.md](POLITICA_FUENTES.md).

## Componentes

| Componente | Descripción | Dónde |
|---|---|---|
| Modelo (GGUF Q4_K_M, 5,3 GB) | Gemma 4 E4B afinado con QLoRA, listo para LM Studio | [Denisijcu/vertex-salvador-GGUF](https://huggingface.co/Denisijcu/vertex-salvador-GGUF) |
| Adaptador LoRA | El resultado del afinado, para reentrenar o exportar | [Denisijcu/vertex-salvador](https://huggingface.co/Denisijcu/vertex-salvador) |
| Servidor de herramientas | `buscar_documentos`, `leer_documento`, `consultar_cifras`, `linea_tiempo` | [`agente/`](agente/) |
| Biblioteca | 133 fragmentos verificados de 153 fuentes públicas, en 25 épocas y ejes | [`fuentes/`](fuentes/), [EPOCAS.md](EPOCAS.md) |
| Tabla de cifras | Cada cifra con su atribución y el fragmento que la sostiene | [`agente/cifras.json`](agente/cifras.json) |
| Datos de entrenamiento | 261 conversaciones propias en español e inglés, 256 con uso de herramientas | [`datos/`](datos/) |

## Inicio rápido

1. Instale [LM Studio](https://lmstudio.ai) y [Python 3.10+](https://www.python.org/downloads/) (marcando
   *Add python.exe to PATH*).
2. Descargue este repositorio y el archivo `gemma-4-E4B-it.Q4_K_M.gguf` de
   [Hugging Face](https://huggingface.co/Denisijcu/vertex-salvador-GGUF).
3. Ejecute `agente\instalar.bat` y copie en el `mcp.json` de LM Studio el bloque que muestra al final.
4. Cargue el modelo con **Context Length 8192**, pegue `agente\SISTEMA.txt` como instrucción de sistema y ponga
   temperatura 0,3, *Repeat Penalty* 1.05 y *Enable Thinking* desactivado.

Cada paso, con la solución de los problemas más comunes, está en [GUIA_INSTALACION.md](GUIA_INSTALACION.md).

## Las herramientas

| Herramienta | Qué hace |
|---|---|
| `buscar_documentos` | Búsqueda BM25 en la biblioteca y en los documentos privados; puede dar preferencia a una época |
| `leer_documento` | Abre un fragmento completo o un documento privado |
| `consultar_cifras` | Devuelve las filas de una métrica (homicidios, detenciones, elecciones…) con su atribución |
| `linea_tiempo` | Ordena los hechos de una época o de un rango de años |

El contrato exacto está en [herramientas.json](herramientas.json). Los documentos que se copien en
`agente/docs_privados/` se pueden consultar, pero nunca entran al entrenamiento ni a este repositorio.

## Estado y límites

- **Versión 1** (19 de noviembre de 2026). Datos hasta el **18 de noviembre de 2026**.
- Probado en LM Studio 0.4 con el servidor MCP: busca antes de responder, usa los resultados y atribuye.
- Límites conocidos: solo sabe lo que está en la biblioteca; la búsqueda es por palabras; en ocasiones atribuye un dato
  correcto a otra fuente de la misma búsqueda. Detalle en la sección 8 de la guía.

## Estructura del repositorio

```
vertex-salvador/
├── GUIA_INSTALACION.md     Instalación y uso, paso a paso
├── DESARROLLO.md           Cómo se construyó y cómo se reentrena
├── BITACORA.md             Registro de decisiones y pruebas
├── POLITICA_FUENTES.md     Reglas de verificación
├── EPOCAS.md               Épocas y ejes del dataset
├── herramientas.json       Contrato de las 4 herramientas
├── agente/                 Servidor MCP, instalador, instrucción de sistema, tabla de cifras
├── fuentes/                Registro de fuentes y fragmentos aprobados
├── datos/                  Conversaciones de entrenamiento
├── eval/                   Preguntas de evaluación
└── *.py                    Generación, validación, exportación y entrenamiento
```

## Licencia

Distribuido bajo la licencia Apache 2.0, la misma del modelo base
[Gemma 4 E4B](https://huggingface.co/google/gemma-4-E4B-it). Cada fragmento conserva el enlace a su fuente original en
`fuentes/registro_fuentes.csv`.

## Autor

**Denis Sánchez Leyva** — [Vertex Coders LLC](https://vertex-services.org), Miami, Florida.
