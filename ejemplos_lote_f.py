"""
ejemplos_lote_f.py — Ejemplos de entrenamiento, lote F: la era Bukele (E06–E14, T01, T03) con otras preguntas.
Uso (desde E:\\vertex-salvador):  python ejemplos_lote_f.py  ->  datos\\ejemplos_lote_f.jsonl
"""
from ejemplos_base import B, C, D, E, L, guardar

E("sv-f001", "T01", "hecho", "¿Cuántos años tiene Bukele y de dónde es?",
  [[B("Nayib Bukele nacimiento familia", ["FR-T01-001", "FR-E06-001", "FR-E07-001", "FR-E12-001"], epoca="T01")]],
  """
Según su biografía en Wikipedia, Nayib Armando Bukele Ortez nació el 24 de julio de 1981 en San Salvador, la capital. Tu pregunta por la edad la puedes calcular desde esa fecha; yo te doy el dato tal como está en la fuente.

Viene de una familia de empresarios. Es hijo de Armando Bukele Kattán, un empresario que murió en 2015, y de Olga Marina Ortez. Estudió en la Universidad Centroamericana (UCA), una de las universidades más conocidas del país, pero no terminó la carrera.

Antes de la política se dedicó a los negocios familiares, y su salto a la vida pública fue joven: en 2012, a los 31 años, ganó la alcaldía de Nuevo Cuscatlán, un municipio pequeño junto a San Salvador, como miembro del FMLN.

Ganó la presidencia el 3 de febrero de 2019, todavía muy joven, y fue reelegido el 4 de febrero de 2024.

Si quieres, te sigo con su carrera política, desde la alcaldía hasta la ruptura con el FMLN.
""")

E("sv-f002", "T01", "perspectivas", "¿Bukele es de izquierda o de derecha?",
  [[B("Bukele ideología FMLN GANA difícil de encasillar", ["FR-T01-002", "FR-E06-001", "FR-E06-002"], epoca="T01")]],
  """
Es difícil de encasillar, y así lo describen incluso quienes lo conocen.

Según BBC Mundo, se le ve como un político difícil de ubicar en el mapa clásico: fue alcalde por el FMLN, el partido de izquierda que nació de la guerrilla, y ganó la presidencia con GANA, un partido de derecha nacido de una escisión de ARENA.

Su recorrido lo muestra. En 2012 ganó la alcaldía de Nuevo Cuscatlán con el FMLN, y en 2015 la de San Salvador, también con ese partido. En 2017 lo expulsaron del FMLN por sus diferencias con la dirección, y ese año fundó Nuevas Ideas. Como su partido no pudo inscribirse a tiempo, en 2019 se presentó con GANA.

Sus defensores dicen que eso demuestra que no responde a ideologías sino a resultados. Sus críticos, desde la izquierda y desde la derecha, lo ven como alguien que usa cualquier etiqueta que le sirva para llegar al poder.

En la práctica, su política de seguridad, el régimen de excepción y la mano firme suelen asociarse con la derecha, y él mismo ha rechazado que lo definan por esas categorías. Lo justo es decir que su trayectoria no encaja en una sola.
""")

E("sv-f003", "E06", "hecho", "¿Qué hizo Bukele como alcalde?",
  [[B("Bukele alcalde Nuevo Cuscatlán San Salvador", ["FR-E06-001", "FR-E06-002"], epoca="E06")]],
  """
Fue alcalde dos veces antes de llegar a la presidencia.

En 2012, a los 31 años, ganó la alcaldía de Nuevo Cuscatlán, un municipio pequeño junto a San Salvador, como miembro del FMLN. En 2015 dio el salto a la alcaldía de la capital, San Salvador, también con el FMLN, y la ejerció de 2015 a 2018.

Sobre su gestión concreta, obras o programas de esos años, no tengo datos verificados en mis documentos, así que no te voy a listar logros ni fracasos de memoria.

Lo que sí está documentado es cómo terminó esa etapa. Sus diferencias con la dirección del FMLN acabaron con su expulsión del partido en 2017. Ese mismo año fundó Nuevas Ideas, que al principio no pudo inscribirse como partido porque no cumplía los requisitos de la ley electoral. Por eso, para 2019, se presentó a la presidencia con GANA.

Esa ruptura es clave en su historia política: pasó de ser una figura joven de la izquierda a construir su propio movimiento, que después dominaría la Asamblea. Si quieres, te cuento cómo ganó en 2019.
""")

E("sv-f004", "E07", "hecho", "¿Por cuánto ganó Bukele en 2019 y contra quién?",
  [[C("elecciones_presidenciales", [("2019", "Bukele 53 %", "Primicias / EFE", "FR-E07-001")], desde="2019", hasta="2019")],
   [B("elección presidencial 2019 Calleja ARENA", ["FR-E07-001", "FR-E06-002", "FR-E07-002"], epoca="E07")]],
  """
El 3 de febrero de 2019 Bukele ganó la elección presidencial en primera vuelta con el 53 % de los votos válidos, como candidato de GANA.

El segundo fue Carlos Calleja, de ARENA, que quedó en torno al 32 %. Es decir, le sacó una ventaja de unos veinte puntos y no hizo falta segunda vuelta.

Lo histórico no fue solo el margen. Con esa victoria Bukele rompió treinta años de alternancia entre ARENA y el FMLN, los dos partidos que habían dominado la política salvadoreña desde el final de la guerra. Uno venía de la derecha que gobernó en los años noventa y dos mil, y el otro de la antigua guerrilla.

Mucho de su atractivo venía de ahí: se presentó como alguien de fuera de esos dos partidos, aunque había sido alcalde por el FMLN hasta que lo expulsaron en 2017.

Asumió el 1 de junio de 2019 y, pocas semanas después, lanzó su primera estrategia de seguridad, el Plan Control Territorial. Si quieres, te cuento en qué consistía.
""")

E("sv-f005", "E07", "conflicto", "¿Los homicidios bajaron por Bukele o ya venían bajando?",
  [[C("homicidios", [("2015", "6.657 homicidios; 103 por cada 100.000", "estadísticas oficiales", "FR-E05-001"),
                     ("2018", "51 por cada 100.000; 3.340 asesinatos", "fuentes oficiales citadas por AFP", "FR-E05-003"),
                     ("2021", "1.211", "cifras oficiales", "FR-E11-004"),
                     ("2025", "82", "cifras oficiales", "FR-E11-004")])],
   [B("baja de homicidios antes de Bukele y atribución del gobierno", ["FR-E07-002", "FR-E07-003", "FR-E11-005"])]],
  """
Las dos cosas son ciertas, y por eso se discute tanto.

Ya venían bajando: según las cifras oficiales, después del récord de 2015, con 6.657 homicidios y una tasa de unos 103 por cada 100.000 habitantes, la tasa fue cayendo hasta 51 por cada 100.000 en 2018, con 3.340 asesinatos. Bukele no había llegado todavía.

Bajaron mucho más con él: según las cifras oficiales citadas por Diario El Mundo, hubo 1.211 homicidios en 2021 y 82 en 2025.

Lo que dice cada parte:
- El gobierno atribuye la baja desde junio de 2019 a su Plan Control Territorial. Bukele explicó en X que la disminución empezó antes del régimen de excepción y se acentuó desde 2022.
- Según un balance de EFE publicado por Primicias, Bukele logró acentuar una disminución que había empezado en 2016.
- Sus críticos insisten en que la tendencia ya existía y que parte del mérito se le atribuye de más.

La forma más justa de decirlo: la caída empezó antes de Bukele, y con él se aceleró hasta niveles que el país no había conocido. El porqué exacto, si fue el plan, el régimen o, según investigaciones periodísticas, algún pacto con las pandillas que el gobierno niega, es lo que sigue en debate.
""")

E("sv-f006", "E08", "hecho", "¿Por qué Bukele metió soldados en la Asamblea?",
  [[B("9F préstamo Plan Control Territorial Asamblea militares", ["FR-E08-001", "FR-E08-002"], epoca="E08")]],
  """
Para presionar a los diputados a que le aprobaran un préstamo.

El 9 de febrero de 2020 Bukele entró en la Asamblea Legislativa acompañado de militares y policías armados. Los diputados, que entonces eran de mayoría opositora, no habían aprobado un préstamo de 109 millones de dólares para la fase III del Plan Control Territorial, su estrategia de seguridad. Bukele se sentó en la silla del presidente de la Asamblea y rezó en el Salón Azul.

Había convocado una sesión extraordinaria para ese día, pero según EFE no pudo celebrarse por falta de quórum, porque solo se presentaron 20 diputados. Ante sus seguidores, que lo esperaban afuera, Bukele dio una semana a los legisladores para aprobar el préstamo.

Desde entonces el episodio se conoce como el 9F, y es uno de los más polémicos de su gobierno. La oposición y muchos observadores lo vieron como una presión militar sobre otro poder del Estado; sus aliados lo niegan.

Si quieres, te doy cómo lo describió cada parte, porque las versiones son opuestas.
""")

E("sv-f007", "E09", "hecho", "¿Qué pasó con el fiscal general en 2021?",
  [[B("destitución fiscal general Raúl Melara 2021", ["FR-E09-001", "FR-E09-003"], epoca="E09")]],
  """
Lo destituyeron el mismo día que a los magistrados de la Sala de lo Constitucional.

El 1 de mayo de 2021, en su primera sesión, la nueva Asamblea Legislativa, con mayoría de Nuevas Ideas tras las elecciones del 28 de febrero, destituyó a los cinco magistrados de la Sala de lo Constitucional y al fiscal general, Raúl Melara. Los sustituyó esa misma noche. La destitución de los magistrados se aprobó con 64 votos a favor y 19 en contra.

La reacción fue inmediata. Media hora después de la destitución, la Sala saliente la declaró inconstitucional, aunque ya no tenía forma de hacer valer esa decisión. La OEA rechazó las destituciones y el secretario de Estado de Estados Unidos, Antony Blinken, le expresó a Bukele una profunda preocupación.

El significado político es grande: en una sola noche, el partido del presidente cambió a quienes debían controlar la constitucionalidad de sus actos y a quien dirigía la persecución de los delitos.

Las razones que dio Nuevas Ideas para sacar a los magistrados las tengo aparte; si te interesan, te las doy junto con las críticas.
""")

E("sv-f008", "E09", "conflicto", "¿Fue legal que destituyeran a los magistrados?",
  [[B("destitución magistrados Sala Constitucional argumentos", ["FR-E09-001", "FR-E09-002", "FR-E09-003"], epoca="E09")]],
  """
Eso es justo lo que cada lado responde distinto. Te pongo los argumentos con su dueño.

Lo que pasó: el 1 de mayo de 2021 la nueva Asamblea, con mayoría de Nuevas Ideas, destituyó a los cinco magistrados de la Sala de lo Constitucional y al fiscal general, y los sustituyó esa misma noche, con 64 votos a favor y 19 en contra.

Lo que dijo la Asamblea: según El Financiero, la iniciativa de Nuevas Ideas sostenía que los magistrados habían actuado contra la Constitución al anteponer intereses particulares a la salud de la población durante la pandemia. Era una referencia a las sentencias en las que la Sala había frenado medidas del gobierno.

Lo que dijeron los otros: media hora después la Sala saliente declaró inconstitucional su destitución. La OEA rechazó las destituciones y el secretario de Estado de Estados Unidos, Antony Blinken, expresó a Bukele una profunda preocupación.

El fondo del debate es quién decide qué es constitucional cuando el que controla la Asamblea saca al tribunal que lo controla a él. No te voy a dar un veredicto propio; lo que te puedo decir es que la Sala destituida y la comunidad internacional lo consideraron ilegal, y el oficialismo lo considera un acto dentro de sus facultades.
""")

E("sv-f009", "E09", "hecho", "¿Por qué sancionó Estados Unidos a Osiris Luna?",
  [[B("sanción Tesoro Osiris Luna Carlos Marroquín tregua", ["FR-E09-005", "FR-E09-006", "FR-E10-001"], epoca="E09")]],
  """
Por presuntas negociaciones con las pandillas. Te lo doy como lo dice Washington y como responde el gobierno salvadoreño.

Según el Departamento del Tesoro de Estados Unidos, que el 8 de diciembre de 2021 sancionó a Osiris Luna, director de Centros Penales, y a Carlos Marroquín, director de Reconstrucción del Tejido Social, ambos dirigieron en 2020 reuniones promovidas por el gobierno de Bukele para pactar una tregua secreta con líderes pandilleros. Esa es la acusación del gobierno estadounidense, no una sentencia judicial.

Según La Prensa de Panamá, el gobierno de Bukele niega haber pactado con las pandillas. Esa misma fuente recuerda que en 2021 el gobierno se había negado a extraditar a Estados Unidos a líderes de la MS-13 reclamados por la justicia de Nueva York, algo que los críticos relacionan con la acusación.

El tema sigue vivo porque toca el centro del relato del gobierno: si la baja de homicidios fue mérito de la fuerza del Estado o, en parte, de un acuerdo con las pandillas.

Hay más elementos en esta historia, como una investigación periodística sobre la ola de violencia de marzo de 2022. ¿Te la busco?
""")

E("sv-f010", "E10", "hecho", "¿Qué pasó el 26 de marzo de 2022?",
  [[B("26 de marzo 2022 homicidios día más violento", ["FR-E10-001", "FR-E10-002"], epoca="E10")]],
  """
Fue el día más violento de El Salvador desde el fin de la guerra civil.

Entre el 25 y el 27 de marzo de 2022 hubo 87 homicidios en todo el país. Solo el sábado 26 se registraron 62. La Policía y el gobierno atribuyeron la ola de asesinatos a la MS-13.

La respuesta llegó al día siguiente. El 27 de marzo de 2022 la Asamblea Legislativa aprobó, a petición de Bukele, un régimen de excepción de 30 días por las graves perturbaciones del orden público causadas por grupos delincuenciales. Votaron a favor 67 de los 84 diputados.

Ese fin de semana es el punto de partida de todo lo que vino después: las detenciones masivas, el CECOT y la caída de los homicidios a niveles muy bajos. El régimen de excepción, que iba a durar 30 días, se ha prorrogado desde entonces.

Por qué estalló esa violencia justo ese fin de semana es otra pregunta, y ahí hay versiones distintas, entre ellas una investigación periodística que el gobierno rechaza. Si quieres, te las doy.
""")

E("sv-f011", "E10", "conflicto", "¿Por qué hubo tantos asesinatos en marzo de 2022? ¿Se rompió un pacto?",
  [[B("ola de asesinatos marzo 2022 causas pacto MS-13", ["FR-E10-001", "FR-E10-003", "FR-E09-006"])]],
  """
Hay dos versiones, y ninguna está probada en un tribunal. Te las doy con nombre.

Lo que no se discute: entre el 25 y el 27 de marzo de 2022 hubo 87 homicidios, 62 de ellos el sábado 26, el día más violento desde el fin de la guerra. La Policía y el gobierno atribuyeron la ola a la MS-13.

La versión periodística: según una investigación de El Faro recogida por Telemundo, la ola se desató por la supuesta ruptura de un pacto entre el gobierno de Bukele y la MS-13. Es decir, que las pandillas mataron para presionar al gobierno cuando el acuerdo se cayó.

La versión del gobierno: el gobierno niega haber pactado con las pandillas. Según La Prensa de Panamá, mantiene esa negativa desde las primeras acusaciones.

Para ubicar el debate: Estados Unidos ya había sancionado en 2021 a dos funcionarios salvadoreños acusándolos de negociar con pandilleros, algo que el gobierno también rechazó.

Lo que yo puedo decirte es lo que sostiene cada uno. Si hubo o no un pacto no está resuelto con pruebas públicas que lo confirmen o lo descarten.
""")

E("sv-f012", "E10", "hecho", "¿Cuánto dura la detención sin juez con el régimen de excepción?",
  [[B("régimen de excepción detención administrativa garantías", ["FR-E10-004"], epoca="E10")]],
  """
Con el régimen de excepción la detención administrativa se amplía a 15 días. Es decir, una persona puede estar detenida hasta ese tiempo antes de ser presentada ante un juez, cuando lo normal es un plazo mucho más corto.

No es lo único que cambia. El régimen de excepción suspende garantías como la inviolabilidad de las comunicaciones, lo que permite intervenirlas, y el derecho a la defensa de los detenidos, que pueden pasar ese tiempo sin un abogado.

Y no es temporal en la práctica: la Asamblea lo ha prorrogado cada 30 días desde marzo de 2022.

Para el gobierno, esas facultades son las que permitieron desarticular a las pandillas, cuyos miembros antes salían por falta de pruebas o por amenazas a testigos. Para las organizaciones de derechos humanos, son justo lo que explica las detenciones de inocentes que denuncian.

Si quieres, te busco cuántas personas han sido detenidas bajo el régimen y qué dicen las dos partes sobre esas cifras.
""")

E("sv-f013", "E11", "hecho", "¿Cuánta gente cabe en el CECOT?",
  [[B("CECOT capacidad presos", ["FR-E11-001", "FR-E11-002", "FR-E13-001"], epoca="E11")]],
  """
El CECOT tiene capacidad para 40.000 presos. Es la cárcel más grande de América Latina.

Está en Tecoluca, en el departamento de San Vicente. Se construyó entre julio de 2022 y enero de 2023, abrió a finales de enero de 2023 y recibió a sus primeros 2.000 reclusos el 24 de febrero de 2023.

Otra cosa es cuántos hay dentro. Según Centroamérica 360, las autoridades no han dado cifras oficiales actualizadas de la población del CECOT. En octubre de 2023 se dijo que operaba al 30 % de su capacidad, pero eso tiene años y no lo puedo dar como dato actual.

Su nombre completo es Centro de Confinamiento del Terrorismo, y fue pensado para los pandilleros considerados más peligrosos. En 2025 también recibió a deportados de Estados Unidos, lo que lo volvió conocido fuera de El Salvador.

Si quieres, te cuento lo de los deportados o qué dicen las organizaciones de derechos humanos sobre las condiciones en las cárceles.
""")

E("sv-f014", "E11", "hecho", "¿Cuántos detenidos van con el régimen de excepción?",
  [[C("detenciones_regimen", [("enero de 2023", "más de 62.000", "Wikipedia", "FR-E11-003"),
                              ("febrero de 2026", "más de 91.300", "decreto de prórroga de la Asamblea Legislativa", "FR-E14-002")])]],
  """
Tengo dos cortes, uno de 2023 y otro de 2026.

Según Wikipedia, cuando abrió el CECOT, en enero de 2023, el gobierno ya había arrestado a más de 62.000 supuestos pandilleros bajo el régimen de excepción.

La cifra más reciente viene del propio Estado: según el decreto de prórroga aprobado por la Asamblea en febrero de 2026, el régimen había dejado más de 91.300 capturas de personas vinculadas a estructuras criminales. Es la cifra oficial, y como tal te la doy atribuida.

Lo que esas cifras no dicen es cuántos de los detenidos eran de verdad pandilleros. Ahí está el gran desacuerdo. El gobierno sostiene que son personas ligadas a las maras. Organizaciones como Cristosal sostienen que miles de inocentes cayeron en las detenciones masivas.

Tampoco tengo una cifra oficial de cuántos han sido liberados o condenados.

Si quieres, te busco qué dicen las organizaciones de derechos humanos sobre los detenidos que murieron bajo custodia, que es otra cifra muy discutida.
""")

E("sv-f015", "E11", "perspectivas", "¿Qué dice el gobierno de los resultados del régimen de excepción?",
  [[B("gobierno resultados régimen de excepción homicidios territorios", ["FR-E11-006", "FR-E11-005", "FR-E14-004"])],
   [B("críticas organizaciones régimen de excepción", ["FR-E14-006", "FR-E14-010"])]],
  """
El gobierno lo presenta como la política que salvó al país. Te doy su versión y, al final, la de sus críticos.

Según EFE, Bukele y su gabinete de Seguridad sostienen que el régimen permitió combatir a las maras, liberar territorios que dominaban y reducir mucho los homicidios en un país que durante años estuvo entre los más violentos del mundo. EFE añade un matiz: El Salvador ya venía con bajas sostenidas de asesinatos desde 2016.

Según Diario El Mundo, Bukele explicó en X que la disminución de los homicidios empezó antes del régimen de excepción y se acentuó a partir de 2022, cuando se aprobó.

Y según EFE, el vicepresidente Félix Ulloa aseguró que las condiciones que llevaron a decretar el régimen en marzo de 2022 no se han superado, que es el argumento para seguir prorrogándolo.

Del otro lado, Cristosal sostiene que el gobierno tiene al menos 86 presos políticos y que miles de inocentes cayeron en las detenciones masivas, y el Informe Mundial 2026 de Human Rights Watch dice que el gobierno siguió eliminando los controles al Poder Ejecutivo. El gobierno rechaza esas acusaciones.
""")

E("sv-f016", "E12", "hecho", "¿Cuánta gente votó en la reelección de Bukele?",
  [[B("participación elección presidencial 2024 padrón", ["FR-E12-001", "FR-E12-003"], epoca="E12")]],
  """
Según El Diario de Hoy, de los 6.214.399 salvadoreños habilitados para votar, más de 2,9 millones no votaron en la elección presidencial de 2024.

Bukele ganó con 2.701.725 votos, el 84,65 % de los votos válidos, según el Tribunal Supremo Electoral. Si esos votos se miden contra todo el padrón y no solo contra los que fueron a votar, equivalen, según El Diario de Hoy, al 43,48 % de los habilitados.

Las dos lecturas son ciertas y se usan para cosas distintas. El gobierno destaca el 84,65 %, uno de los resultados más altos de América Latina. Sus críticos destacan que casi la mitad del padrón no votó.

La elección fue el 4 de febrero de 2024, y Nuevas Ideas ganó además 54 de los 60 escaños de la Asamblea Legislativa.

Si quieres, te busco el debate sobre si la reelección era constitucional, que es la otra gran discusión de esa elección.
""")

E("sv-f017", "E12", "hecho", "¿Por qué ahora hay menos diputados y municipios?",
  [[B("reducción municipios diputados 2023", ["FR-E12-002", "FR-E12-001"], epoca="E12")]],
  """
Porque en junio de 2023 la Asamblea aprobó, a propuesta de Bukele, una reforma que redujo los municipios de 262 a 44 y los diputados de 84 a 60, para la legislatura que empezó en 2024.

El gobierno la presentó como una forma de ahorrar dinero público y hacer más eficiente la administración. Mis documentos no recogen el detalle de ese argumento ni de las críticas, así que te doy solo los hechos de la reforma.

El efecto político se vio en la elección del 4 de febrero de 2024: con 60 escaños en juego, Nuevas Ideas ganó 54. Con menos curules y circunscripciones distintas, los partidos pequeños tuvieron más difícil entrar, algo que suele pasar cuando se reduce el tamaño de un parlamento.

Para la oposición esto se suma a otras decisiones que, según ella, concentran el poder. Para el oficialismo es una muestra de que el país se modernizó.

Si quieres, te busco cómo quedó la Asamblea y qué dicen las organizaciones críticas sobre la concentración del poder.
""")

E("sv-f018", "E13", "hecho", "¿Cuánto le pagó Estados Unidos a El Salvador por los deportados?",
  [[B("pago Estados Unidos deportados CECOT 6 millones", ["FR-E13-002", "FR-E13-001"], epoca="E13")]],
  """
Según la Casa Blanca, Washington pagó aproximadamente 6 millones de dólares al gobierno de Bukele por recluir durante un año a los deportados que mandó al CECOT.

El acuerdo lo cerraron Bukele y el secretario de Estado, Marco Rubio, y no se ha hecho público. Así que la cifra es la que dio la Casa Blanca; no hay un documento abierto con las condiciones.

El contexto: el 15 de marzo de 2025 el presidente Donald Trump invocó la Ley de Enemigos Extranjeros de 1798 contra la banda venezolana Tren de Aragua. Ese mismo día, pese a que el juez federal James Boasberg había prohibido esos vuelos mientras decidía, llegaron a El Salvador 238 deportados, 23 de ellos salvadoreños señalados como pandilleros de la MS-13. Todos fueron recluidos en el CECOT.

El caso generó una batalla judicial en Estados Unidos y críticas de organizaciones de derechos humanos, porque muchos deportados no habían sido condenados.

Si quieres, te cuento qué pasó con ellos o qué dijeron las partes sobre el acuerdo.
""")

E("sv-f019", "E13", "perspectivas", "¿Por qué la Ley de Agentes Extranjeros es tan polémica?",
  [[B("Ley de Agentes Extranjeros impuesto 30 % ONG", ["FR-E13-003", "FR-E13-004", "FR-E13-005"], epoca="E13")]],
  """
Porque toca el dinero de las organizaciones que más critican al gobierno. Te doy los hechos y las dos lecturas.

Lo que hace la ley: la aprobó la Asamblea el 20 de mayo de 2025, con 57 votos. Obliga a las personas y organizaciones que reciben fondos del exterior a inscribirse en un Registro de Agentes Extranjeros (RAEX) y les cobra un impuesto del 30 % sobre esas donaciones.

Lo que dice la ley de sí misma: según LexLatin, declara como finalidad promover la transparencia sobre la influencia extranjera y resguardar la seguridad, la soberanía nacional y la estabilidad social y política del país. El gobierno la presenta como una medida para saber quién financia a quién.

Lo que dicen los críticos: según Human Rights Watch, la ley da al gobierno amplias facultades para vigilar, sancionar y cerrar a las organizaciones que estigmatiza como agentes extranjeros, y se aprobó prácticamente sin debate ni consulta pública.

El choque es este: muchas ONG de derechos humanos y medios independientes viven de donaciones internacionales. Para el gobierno, ese dinero es injerencia extranjera; para ellas, la ley es una forma de asfixiarlas.
""")

E("sv-f020", "E14", "hecho", "¿Cuántas veces han prorrogado el régimen de excepción?",
  [[C("prorrogas", [("24 de junio de 2026", "prórroga número 52", "Asamblea Legislativa", "FR-E14-001")])],
   [B("prórroga régimen de excepción cada 30 días", ["FR-E10-004", "FR-E14-004"])]],
  """
El 24 de junio de 2026 la Asamblea aprobó la prórroga número 52 del régimen de excepción. Para entonces la medida llevaba más de cuatro años en vigor sin interrupción.

El mecanismo es que la Asamblea lo prorroga cada 30 días desde marzo de 2022, porque la Constitución no permite decretarlo por tiempo indefinido de una sola vez. Por eso hay que renovarlo mes a mes, y por eso el número de prórrogas sube tanto.

No tengo la cifra de prórrogas posteriores a junio de 2026. Si siguió el ritmo mensual, habría más, pero no te voy a dar un número que no está en mis documentos.

El gobierno justifica seguir renovándolo. Según EFE, el vicepresidente Félix Ulloa aseguró que las condiciones que llevaron a decretar el régimen en marzo de 2022 no se han superado.

Sus críticos sostienen que una medida de excepción que dura años ya no es excepcional, sino una forma permanente de gobernar sin algunas garantías.

Si quieres, te busco qué dice el último decreto que tengo sobre por qué se mantiene.
""")

E("sv-f021", "E14", "hecho", "¿Cuántos homicidios hubo en 2026?",
  [[C("homicidios", [("enero-octubre de 2026", "48", "Policía Nacional Civil", "FR-E14-003")], desde="2026")],
   [C("homicidios", [("2015", "6.657 homicidios; 103 por cada 100.000", "estadísticas oficiales", "FR-E05-001"),
                     ("2025", "82", "cifras oficiales", "FR-E11-004")], desde="2015", hasta="2025")]],
  """
Según los reportes oficiales de la Policía Nacional Civil citados por El Diario de Hoy, entre enero y octubre de 2026 hubo 48 homicidios en todo el país, y en el mes de octubre fueron cuatro.

No tengo la cifra del año completo, porque mis datos de homicidios llegan hasta octubre.

Para dimensionarlo: según las cifras oficiales, en 2025 hubo 82 homicidios, y en 2015 llegaron a 6.657. Es una de las caídas más grandes del mundo en tan poco tiempo.

Un matiz que conviene tener presente: son cifras de la Policía, es decir, del propio gobierno, y por eso te las doy atribuidas. No tengo en mis documentos una serie independiente con la que compararlas, ni datos sobre cómo se clasifican casos como las muertes bajo custodia, que las organizaciones civiles cuentan aparte.

Así que lo justo es decir que, según la Policía, la violencia homicida está en el nivel más bajo de la historia reciente del país.
""",
  )

E("sv-f022", "E14", "perspectivas", "¿Qué es el GIPES y qué dijo de El Salvador?",
  [[B("GIPES expertos CIDH lesa humanidad", ["FR-E14-007", "FR-E14-009"], epoca="E14")]],
  """
GIPES es un grupo internacional de expertos que analizó la situación de derechos humanos en El Salvador. Según el Tico Times, está respaldado por la Comisión Internacional de Juristas y la FIDH.

Lo que concluyó: en marzo de 2026, ante la Comisión Interamericana de Derechos Humanos (CIDH), el grupo dijo que hay bases razonables para creer que se cometen crímenes de lesa humanidad en el país, en el marco del régimen de excepción. "Bases razonables" es una fórmula del derecho penal internacional: no es una condena, sino la conclusión de que hay indicios suficientes para investigar.

Lo que respondió el gobierno: según el Tico Times, Bukele rechazó tanto esa conclusión como la acusación de que hay presos políticos. Ese mismo mes acusó a las organizaciones de derechos humanos de actuar como bufetes de abogados de los criminales y dijo que su gobierno nunca atenderá sus críticas.

Así que tienes dos posiciones opuestas: un grupo de expertos que ve indicios graves y un gobierno que lo considera una defensa de los pandilleros. No hay, hasta donde llegan mis datos, una investigación judicial internacional abierta por ese motivo.
""")

E("sv-f023", "E14", "reformulacion", "La gente en El Salvador está feliz con Bukele, así que todo lo que dicen las ONG es mentira.",
  [[B("popularidad Bukele 2026", ["FR-E14-005"], epoca="E14"),
    B("denuncias ONG presos detenciones", ["FR-E14-006", "FR-E14-008"], epoca="E14")]],
  """
Que Bukele sea popular está bien documentado. Lo que no se sigue de eso es que las denuncias sean falsas: son dos preguntas distintas.

Sobre la popularidad: Bukele llegó a 2026 con índices altos, que se han mantenido sin grandes cambios en sus siete años en el poder. Descansan sobre todo en la reducción de los homicidios y en el régimen de excepción. Para mucha gente, poder salir a la calle sin miedo a las maras pesa más que cualquier otra cosa.

Sobre las denuncias: Cristosal sostiene que hay al menos 86 presos políticos y que miles de inocentes cayeron en las detenciones masivas. Y las muertes bajo custodia las llevan organizaciones civiles: Socorro Jurídico Humanitario registra 530, y otra organización citada por el Tico Times, al menos 500. El gobierno no publica una cifra propia y rechaza esas acusaciones.

Una mayoría puede apoyar una política y, al mismo tiempo, esa política puede afectar injustamente a una minoría. Una cosa no anula la otra. Lo que sí puedes hacer es mirar cada denuncia y ver si viene con nombres, fechas y pruebas, y en qué responde el gobierno.

Si quieres, te busco casos concretos con su fuente.
""")

E("sv-f024", "T03", "hecho", "¿Ecuador copió el modelo de Bukele?",
  [[B("Ecuador Noboa estado de excepción megacárceles", ["FR-T03-002", "FR-T03-003"], epoca="T03")]],
  """
En parte, sí. Tomó dos de sus piezas más visibles.

En Ecuador, el presidente Daniel Noboa impuso un estado de excepción desde el 8 de enero de 2024 y presentó un plan para construir megacárceles al estilo salvadoreño. Es decir, la medida de excepción y la gran cárcel, las dos cosas que identifican al modelo Bukele fuera de El Salvador.

No es el único caso. Según un reportaje de CONNECTAS publicado en agosto de 2026, en tres años los presidentes de Colombia, Ecuador, Perú, Costa Rica, Panamá y Guatemala prometieron una megacárcel como parte de su política contra el crimen.

Lo que no tengo en mis documentos es una evaluación de cómo le ha ido a Ecuador con esas medidas, ni cifras de su violencia, así que no te puedo decir si funcionó.

Los analistas advierten que copiar el modelo no garantiza el resultado. Para Honduras, por ejemplo, un análisis de la Universidad de Navarra dice que la receta no funciona igual porque allí mata más el narcotráfico que las maras. Algo parecido se discute para Ecuador, donde el crimen organizado tiene otra estructura. ¿Quieres que te cuente el caso de Honduras?
""")

E("sv-f025", "T03", "perspectivas", "¿El modelo Bukele se puede aplicar en otros países?",
  [[B("modelo Bukele otros países Honduras análisis", ["FR-T03-001", "FR-T03-004", "FR-T03-003"], epoca="T03")]],
  """
Hay gobiernos que lo están intentando y analistas que dudan de que funcione igual. Te doy las dos cosas.

Los que lo intentan: en Honduras, el gobierno de Xiomara Castro, de izquierda, decretó un estado de excepción en diciembre de 2022 inspirado en el salvadoreño, y en 2024 anunció planes para una cárcel al estilo del CECOT. Según un reportaje de CONNECTAS de agosto de 2026, en tres años los presidentes de Colombia, Ecuador, Perú, Costa Rica, Panamá y Guatemala prometieron una megacárcel.

Los que dudan: según un análisis de la Universidad de Navarra, la receta no funciona igual en Honduras porque allí mata más el narcotráfico que las maras, el gobierno tiene menos poder y los cuerpos policiales son más complejos.

Ese análisis apunta a algo general: el modelo salvadoreño se aplicó contra pandillas territoriales muy visibles, con un gobierno que controla la Asamblea y la justicia. Donde el crimen es otro, o donde el poder está más repartido, el resultado puede ser distinto.

Que un presidente de izquierda, como Castro, también lo copiara muestra que el atractivo no es solo ideológico: es la promesa de seguridad rápida. Si funciona igual en otro lugar es algo que todavía no tengo cómo demostrar.
""")

E("sv-f026", "E09", "hecho", "Dame la línea de tiempo de cómo Bukele llegó a controlar la Asamblea.",
  [[L("E09", ["FR-E06-002", "FR-E07-001", "FR-E08-001", "FR-E09-001", "FR-E09-004", "FR-E12-002", "FR-E12-001"])]],
  """
Aquí va, paso a paso:

- 2017: lo expulsan del FMLN y funda Nuevas Ideas, que al principio no puede inscribirse como partido.
- 3 de febrero de 2019: gana la presidencia en primera vuelta, con el 53 %, como candidato de GANA. La Asamblea sigue siendo de mayoría opositora.
- 9 de febrero de 2020: el 9F. Entra en la Asamblea con militares y policías para presionar por un préstamo de 109 millones de dólares.
- 28 de febrero de 2021: elecciones legislativas que dan la mayoría a Nuevas Ideas.
- 1 de mayo de 2021: en su primera sesión, la nueva Asamblea destituye a los cinco magistrados de la Sala de lo Constitucional y al fiscal general, con 64 votos a favor y 19 en contra.
- 2021: una resolución de la Corte Suprema lo habilita para la reelección, que la Constitución prohíbe de forma inmediata.
- Junio de 2023: la Asamblea reduce los diputados de 84 a 60 y los municipios de 262 a 44.
- 4 de febrero de 2024: reelegido con el 84,65 %; Nuevas Ideas gana 54 de los 60 escaños.

En siete años pasó de no tener partido inscrito a controlar casi toda la Asamblea.
""")

E("sv-f027", "E13", "hecho", "¿Detuvieron a una abogada de Cristosal?",
  [[B("Ruth López Cristosal detención", ["FR-E13-006", "FR-E13-003"], epoca="E13")]],
  """
Sí. Se trata de Ruth López, directora de anticorrupción y justicia de la ONG Cristosal y crítica de Bukele.

Según Los Angeles Times, en mayo de 2025 la Policía la detuvo en su casa y la Fiscalía la acusó de enriquecimiento ilícito. Cristosal calificó la detención de represalia política.

Te lo doy con las dos versiones porque son opuestas. Para la Fiscalía, es un caso penal por enriquecimiento ilícito. Para Cristosal y otros críticos, es una forma de castigar a una de las voces que más documentaba los abusos del régimen de excepción y los casos de corrupción.

El caso se dio en un momento de tensión con las organizaciones civiles: ese mismo mes, el 20 de mayo de 2025, la Asamblea aprobó la Ley de Agentes Extranjeros, que cobra un impuesto del 30 % a las donaciones del exterior.

No tengo en mis documentos cómo avanzó el proceso judicial después de la detención, así que no sé si hubo juicio, condena o liberación. Si quieres, te cuento qué dice Cristosal en su último informe sobre presos políticos.
""")

E("sv-f028", "E11", "contexto", "¿Por qué la gente apoya el régimen de excepción si quita derechos?",
  [[B("apoyo popular régimen de excepción seguridad", ["FR-E14-005", "FR-E11-004"]),
    B("violencia antes del régimen pico 2015", ["FR-E05-001", "FR-E10-001"])]],
  """
Porque para la mayoría lo que cambió en su vida diaria pesa más que lo que perdió en garantías.

Hay que recordar de dónde venía el país. En 2015 El Salvador tuvo al menos 6.657 homicidios, con una tasa de unos 103 por cada 100.000 habitantes, la más alta de su historia, y fue el país más violento del hemisferio. En marzo de 2022, justo antes del régimen de excepción, hubo 87 homicidios en un solo fin de semana.

Después, según las cifras oficiales, los homicidios bajaron de 1.211 en 2021 a 615 en 2022, 194 en 2023, 114 en 2024 y 82 en 2025. Para quien vivía pagando extorsión o con miedo a salir, eso es una transformación.

Por eso Bukele llegó a 2026 con índices altos de popularidad, que descansan sobre todo en la baja de los homicidios y en el régimen de excepción.

Las garantías que el régimen de excepción suspende, como el derecho a la defensa, afectan sobre todo a quien es detenido. Mucha gente piensa que eso no le va a pasar a ella. Las organizaciones de derechos humanos insisten en que sí le ha pasado a inocentes, y ese es el costo que el debate pone sobre la mesa.
""")

guardar("ejemplos_lote_f.jsonl")
