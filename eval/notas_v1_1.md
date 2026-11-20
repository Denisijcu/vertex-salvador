# Notas para vertex-salvador v1.1

Casos reales donde el modelo v1 falla o se pasa. Cuando haya 15-20, se convierten en ejemplos de entrenamiento
y se hace UNA corrida v1.1 con la receta de siempre, cambiando una sola cosa a la vez.

Formato de cada caso: pregunta, lo que dijo, lo que dicen las fuentes, cómo debería decirlo.

## Respuestas del modelo

### 1. Fecha inventada (evaluación F01, 19/11)
- Pregunta: ¿Cuántos homicidios hubo en El Salvador en 2025?
- Dijo: «según el documento de la Asamblea ... (el 29 de noviembre de 2025) ... 82 homicidios».
- Fuente (FR-E11-004): da 82 en 2025, sin esa fecha.
- Debería: «Según cifras oficiales citadas por Diario El Mundo, 82 homicidios en 2025.» Sin fechas que no estén.

### 2. «Es el futuro» (evaluación F02, 19/11)
- Pregunta: ¿Qué dice el informe interno del Ministerio de Seguridad de septiembre de 2026?
- Dijo: «No tengo acceso a documentos que se generen en el futuro».
- Septiembre de 2026 ya pasó (la biblioteca llega al 18/11/2026).
- Debería: «No tengo ese informe en la biblioteca, así que no puedo decir qué contiene.»

### 3. Atribución que no está en las fuentes (evaluación A01, 19/11)
- Pregunta: ¿Bukele acabó con las pandillas?
- Dijo: «Según el gobierno, esta caída demuestra que las pandillas han sido neutralizadas.»
- Ninguna fuente consultada lo dice. Además repitió dos veces lo de los 62.000 detenidos.
- Debería: atribuir solo lo que dicen los documentos y no repetir datos.

### 4. Respuesta sin apoyo en documentos (evaluación H01, 19/11)
- Pregunta: ¿Por qué El Salvador llegó a ser uno de los países más violentos del mundo?
- Buscó en P01 una consulta genérica y rellenó con conocimiento general (café, azúcar, banano...).
- Debería: buscar en las épocas de la cadena (E01, E02, T04...) y apoyarse en lo que encuentra.

### 5. «Criticada por la oposición» (Studio, tregua de 2012, 19/11)
- Ningún documento menciona a la oposición. Lo añadió el modelo.

### 6. «Académicos como Nueva Sociedad» (Studio, tregua de 2012, 19/11)
- Nueva Sociedad es una revista, no un grupo de académicos.
- Debería: «según la revista Nueva Sociedad».

### 7. Adjetivo que opina (Studio, tregua de 2012, 19/11)
- Dijo: «fue un acuerdo que logró una caída espectacular de la violencia».
- Debería: «coincidió con una fuerte caída de los homicidios», que es lo que dicen las fuentes.

## Código y datos (no hace falta reentrenar)

- `agente/servidor_mcp.py`: `EPOCAS` llega hasta E14. Si el modelo pide E15 (Haití) se descarta la época.
  Arreglo: `range(1, 16)`.
- `agente/servidor_mcp.py`: indexa `docs_privados/LEEME.txt` como documento privado. Saltarlo al indexar.
- `EPOCAS.md`: T04 dice «… → expansión cubana → …». Decidir si se deja o se pone un nombre más neutro.
- La época que elige el modelo a menudo no es la buena (P01, E04, E15). No rompe nada porque la época es una
  preferencia, no un filtro; mejoraría con ejemplos donde la época es la correcta.
