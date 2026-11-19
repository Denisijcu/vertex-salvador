"""
ejemplos_lote_j.py — Ejemplos de entrenamiento, lote J: reintentar la búsqueda con otras palabras cuando la
primera no trae nada, combinar herramientas (buscar, leer, cifras, línea de tiempo) y temas poco cubiertos.
Uso (desde E:\\vertex-salvador):  python ejemplos_lote_j.py  ->  datos\\ejemplos_lote_j.jsonl
"""
from ejemplos_base import B, C, D, E, L, guardar

# ---------------------------------------------------------------- reintentar con otras palabras
E("sv-j001", "E04", "hecho", "¿Qué pasó con el pacto de Funes con los mareros?",
  [[B("pacto Funes mareros", [])],
   [B("tregua entre pandillas 2012 Funes", ["FR-E04-001", "FR-E04-006"], epoca="E04")]],
  """
Lo que se suele llamar "el pacto de Funes" en los documentos aparece como la tregua entre pandillas de 2012. La primera búsqueda no trajo nada con esas palabras, así que busqué por la tregua, y aquí está.

La tregua duró del 9 de marzo de 2012 al 26 de mayo de 2014. Sus principales negociadores fueron el ministro de Seguridad, David Munguía Payés, el exdiputado y exguerrillero Raúl Mijango y el obispo Fabio Colindres, bajo la supervisión del presidente Mauricio Funes.

El final fue en los tribunales. En 2023 un tribunal de San Salvador condenó a Munguía Payés a 18 años de cárcel y a Funes, juzgado en ausencia, a 14 años, por la tregua de 2012, por agrupaciones ilícitas e incumplimiento de deberes. Raúl Mijango fue absuelto en 2017 y en 2019.

Así que, en lo judicial, la justicia salvadoreña consideró que Funes sí fue responsable de ese acuerdo con las pandillas.

Si quieres, te cuento cuánto bajaron los homicidios durante la tregua y qué pasó cuando se rompió.
""")

E("sv-j002", "E11", "hecho", "¿Qué es la mega cárcel de Tecoluca?",
  [[B("mega cárcel Tecoluca", ["FR-E11-001", "FR-E13-001"])]],
  """
Es el CECOT, el Centro de Confinamiento del Terrorismo, la cárcel que el gobierno de Bukele construyó para los pandilleros.

Está en Tecoluca, en el departamento de San Vicente. Se construyó entre julio de 2022 y enero de 2023 y abrió a finales de enero de 2023. Tiene capacidad para 40.000 presos y es la cárcel más grande de América Latina. Recibió a sus primeros 2.000 reclusos el 24 de febrero de 2023.

Por eso la llaman "megacárcel": por su tamaño. Es una de las piezas centrales del régimen de excepción, junto con las detenciones masivas.

Fuera de El Salvador se hizo conocida por las imágenes de sus traslados y porque en 2025 recibió a deportados de Estados Unidos.

También está en el centro de las críticas de organizaciones de derechos humanos, que cuestionan la falta de información pública sobre quiénes están dentro y en qué condiciones.

¿Quieres saber cuántos presos tiene, o lo de los deportados?
""")

E("sv-j003", "E09", "hecho", "¿Qué dijo la OEA cuando sacaron a los jueces en El Salvador?",
  [[B("OEA jueces El Salvador", [])],
   [B("reacción internacional destitución Sala de lo Constitucional 2021", ["FR-E09-003", "FR-E09-001"], epoca="E09")]],
  """
La primera búsqueda, con "jueces", no trajo nada; los documentos hablan de los magistrados de la Sala de lo Constitucional. Con esas palabras sí encontré la reacción.

Lo que pasó: el 1 de mayo de 2021, en su primera sesión, la nueva Asamblea Legislativa, con mayoría de Nuevas Ideas, destituyó a los cinco magistrados de la Sala de lo Constitucional y al fiscal general, Raúl Melara, y los sustituyó esa misma noche. La destitución se aprobó con 64 votos a favor y 19 en contra.

La reacción: la OEA rechazó las destituciones. También el secretario de Estado de Estados Unidos, Antony Blinken, expresó a Bukele una profunda preocupación. Y media hora después de la destitución, la propia Sala saliente la declaró inconstitucional.

No tengo el texto exacto del comunicado de la OEA, solo que rechazó la medida, así que no te voy a citar frases que no están en mis documentos.

Del otro lado, Nuevas Ideas sostuvo que los magistrados habían actuado contra la Constitución durante la pandemia. Si quieres, te doy ese argumento con su fuente.
""")

E("sv-j004", "E15", "hecho", "¿Qué pasó en el Sylvio?",
  [[B("Sylvio", [])],
   [B("estadio Sylvio Cator Haití operación", ["FR-E15-015"], epoca="E15")]],
  """
Supongo que te refieres al estadio Sylvio Cator de Puerto Príncipe, en Haití. Con solo "Sylvio" no salió nada, pero buscando el nombre completo sí.

Según EFE, el 12 de noviembre de 2026 Bukele anunció que, tras una operación conjunta con la Policía Nacional de Haití y fuerzas haitianas, se tomó el control del estadio, que estaba en manos de las bandas desde febrero de 2024. Dijo que allí se instalará una base operativa para seguir avanzando hacia otras zonas.

Bukele también informó de que dentro del estadio se encontraron varios cráneos humanos, y amenazó a las pandillas con una ofensiva.

El Sylvio Cator era el estadio donde jugaba como local la selección haitiana de fútbol, por eso la operación tuvo mucha carga simbólica.

Casi todo lo que se sabe del operativo viene del anuncio de Bukele y de las fuerzas que participaron; no tengo una evaluación independiente de cómo fue.

Si te referías a otra cosa con "Sylvio", dímelo y lo busco.
""")

# ---------------------------------------------------------------- combinar herramientas
E("sv-j005", "E13", "hecho", "Busca la Ley de Agentes Extranjeros, abre el primer documento y dime cuánto cobra.",
  [[B("Ley de Agentes Extranjeros", ["FR-E13-003", "FR-E13-005"], epoca="E13")],
   [D("FR-E13-003")]],
  """
Abrí el documento principal. La Ley de Agentes Extranjeros cobra un impuesto del 30 % sobre las donaciones que reciben del exterior las personas y organizaciones obligadas a registrarse.

El documento dice que la aprobó la Asamblea el 20 de mayo de 2025, con 57 votos, y que obliga a quienes reciben fondos del exterior a inscribirse en un Registro de Agentes Extranjeros (RAEX).

Para que te hagas una idea de lo que significa: casi un tercio de cada donación extranjera se va en ese impuesto. Para organizaciones que viven casi solo de la cooperación internacional, es un golpe muy fuerte.

En la misma búsqueda salió otro documento con la crítica. Según Human Rights Watch, la ley da al gobierno amplias facultades para vigilar, sancionar y cerrar a las organizaciones que estigmatiza como agentes extranjeros, y se aprobó prácticamente sin debate ni consulta pública.

El gobierno, por su parte, la presenta como una ley de transparencia sobre la influencia extranjera.

¿Quieres que abra también el documento de Human Rights Watch?
""")

E("sv-j006", "E11", "contexto", "Dame la línea de tiempo del régimen de excepción con las cifras de cada año.",
  [[L("E11", ["FR-E10-001", "FR-E10-002", "FR-E11-001", "FR-E11-003", "FR-E14-002", "FR-E14-001"])],
   [C("homicidios", [("2021", "1.211", "cifras oficiales", "FR-E11-004"),
                     ("2022", "615", "cifras oficiales", "FR-E11-004"),
                     ("2023", "194", "cifras oficiales", "FR-E11-004"),
                     ("2024", "114", "cifras oficiales", "FR-E11-004"),
                     ("2025", "82", "cifras oficiales", "FR-E11-004")], desde="2021")]],
  """
Aquí la tienes, con los hitos y, al lado, los homicidios oficiales de cada año.

- Marzo de 2022: entre el 25 y el 27 hay 87 homicidios, 62 de ellos el sábado 26. El 27, la Asamblea aprueba el régimen de excepción con 67 votos de 84.
- 2022: según las cifras oficiales citadas por Diario El Mundo, 615 homicidios, frente a 1.211 en 2021.
- Enero de 2023: abre el CECOT, con capacidad para 40.000 presos. Según Wikipedia, para entonces había más de 62.000 supuestos pandilleros arrestados.
- 2023: 194 homicidios.
- 2024: 114 homicidios.
- 2025: 82 homicidios.
- Febrero de 2026: según el decreto de prórroga, el régimen ha dejado más de 91.300 capturas.
- 24 de junio de 2026: la Asamblea aprueba la prórroga número 52; la medida lleva más de cuatro años sin interrupción.

Todas las cifras de homicidios y la de capturas son oficiales, del propio Estado. Las organizaciones de derechos humanos no discuten tanto la baja de homicidios como el costo: detenciones de inocentes y muertes bajo custodia.

¿Quieres que te agregue las cifras de esas organizaciones a la línea de tiempo?
""")

E("sv-j007", "E01", "hecho", "Busca El Mozote y luego dime qué dijo la Comisión de la Verdad del ejército.",
  [[B("El Mozote", ["FR-E01-003"], epoca="E01")],
   [B("Comisión de la Verdad responsabilidad ejército", ["FR-E01-005", "FR-E01-004"], epoca="E01")]],
  """
Primero El Mozote. Según Wikipedia, el 11 de diciembre de 1981, en El Mozote y caseríos vecinos del departamento de Morazán, el ejército salvadoreño mató a más de 800 civiles. La operación la hicieron unidades del Batallón Atlacatl, una unidad de reacción rápida creada en 1980.

Ahora, la Comisión de la Verdad. Se constituyó el 15 de julio de 1992, en cumplimiento de los Acuerdos de Paz, con tres miembros nombrados por el secretario general de la ONU: Belisario Betancur, Reinaldo Figueredo y Thomas Buergenthal. Su informe, «De la locura a la esperanza», se hizo público el 15 de marzo de 1993.

Sobre el ejército, según un análisis académico de la Universidad Federal de Pelotas, el informe atribuyó al ejército y a grupos paramilitares el 85 % de las violaciones que documentó, y responsabilizó al FMLN de una parte menor.

Es decir, El Mozote no fue un caso aislado: encaja con la conclusión general de la Comisión de que la gran mayoría de las violaciones de la guerra fue obra de las fuerzas del Estado.

¿Quieres saber qué pasó con esos crímenes después del informe?
""")

E("sv-j008", "E15", "hecho", "Consulta las cifras del despliegue en Haití y compáralas con lo que pedía la ONU.",
  [[C("despliegue_haiti", [("primer contingente (misión liderada por Kenia)", "70 soldados para evacuaciones médicas", "Voz de América", "FR-E15-003"),
                           ("28 de octubre de 2026", "más de 2.000 militares", "Cancillería salvadoreña, según El Diario de Hoy", "FR-E15-008"),
                           ("octubre de 2026 (toda la GSF)", "más de 2.000 tropas de seis países, alrededor del 37 % de lo previsto", "Latin Times", "FR-E15-021")])],
   [B("mandato Fuerza de Supresión de Pandillas efectivos", ["FR-E15-005", "FR-E15-017"], epoca="E15")]],
  """
Aquí van las cifras de la tabla y lo que preveía la ONU, cada una con su fuente.

Lo que preveía la ONU: según Diario El Mundo, la Fuerza de Supresión de Pandillas se aprobó con un mandato de 12 meses, 5.550 efectivos de seguridad y más de 50 empleados civiles.

Lo que tenía la fuerza: según Latin Times, en octubre de 2026 había desplegadas más de 2.000 tropas de seis países, alrededor del 37 % de lo previsto.

Lo que puso El Salvador:
- Al principio, según la Voz de América, 70 soldados para evacuaciones médicas.
- A finales de octubre de 2026, más de 2.000 militares, según la Cancillería citada por El Diario de Hoy.

La trampa de la comparación: parecería que El Salvador puso casi tantos militares como toda la fuerza internacional. Pero la ONU aclaró el 2 de noviembre que la gran mayoría de ese refuerzo salvadoreño no forma parte de la Fuerza de Supresión de Pandillas. Son dos cosas distintas: la misión de la ONU, que está por debajo de lo previsto, y un despliegue mayoritariamente bilateral entre El Salvador y Haití.

Si quieres, te cuento qué implica que estén fuera de la misión de la ONU.
""")

# ---------------------------------------------------------------- temas poco cubiertos
E("sv-j009", "E06", "contexto", "¿Por qué expulsaron a Bukele del FMLN?",
  [[B("expulsión Bukele FMLN 2017 diferencias dirección", ["FR-E06-002", "FR-T01-002", "FR-E06-001"], epoca="E06")]],
  """
Por sus diferencias con la dirección del partido, que terminaron con su expulsión en 2017.

Bukele había hecho toda su carrera con el FMLN: fue alcalde de Nuevo Cuscatlán desde 2012 y de San Salvador de 2015 a 2018, siempre con ese partido. Pero chocó con la cúpula, y en 2017 lo expulsaron.

Mis documentos no recogen el detalle de los motivos oficiales de la expulsión ni las acusaciones concretas de cada lado, así que no te voy a reconstruir ese pleito de memoria. Lo que sí está claro es lo que vino después.

Ese mismo año fundó Nuevas Ideas. Al principio no pudo inscribirse como partido porque no cumplía los requisitos de la ley electoral, y para 2019 se presentó a la presidencia con GANA.

Según BBC Mundo, eso lo convirtió en un político difícil de encasillar: fue alcalde por el FMLN, de izquierda, y ganó la presidencia con GANA, un partido de derecha nacido de una escisión de ARENA.

Visto con el tiempo, la expulsión fue el punto de partida de su proyecto propio, que terminaría desplazando al FMLN y a ARENA del poder.
""")

E("sv-j010", "E07", "hecho", "Explícame el Plan Control Territorial de Bukele.",
  [[B("Plan Control Territorial 2019", ["FR-E07-002", "FR-E07-003", "FR-E08-001"], epoca="E07")]],
  """
Es la estrategia de seguridad contra las pandillas con la que empezó el gobierno de Bukele, antes del régimen de excepción.

Bukele asumió el 1 de junio de 2019 y el 20 de junio puso en marcha el Plan Control Territorial. El gobierno atribuye a ese plan la baja de los homicidios desde junio de 2019.

Según un balance de EFE publicado por Primicias, Bukele logró acentuar la disminución de los homicidios que había empezado en 2016 y, de acuerdo con las autoridades, quitó a las pandillas el control de los barrios populares.

El plan tenía fases, y una de ellas desató la primera gran crisis política del gobierno. Para financiar la fase III, Bukele pidió a la Asamblea, entonces de mayoría opositora, un préstamo de 109 millones de dólares. Como no se lo aprobaban, el 9 de febrero de 2020 entró en la Asamblea con militares y policías armados, en el episodio que se conoce como el 9F.

Mis documentos no detallan qué contenía cada fase del plan, así que no te las enumero.

¿Quieres que te cuente el 9F o cómo se pasó del plan al régimen de excepción?
""")

E("sv-j011", "T03", "hecho", "¿Honduras también tiene régimen de excepción?",
  [[B("Honduras estado de excepción Xiomara Castro", ["FR-T03-001", "FR-T03-004"], epoca="T03")]],
  """
Sí, inspirado en el salvadoreño.

En Honduras, el gobierno de Xiomara Castro, de izquierda, decretó un estado de excepción en diciembre de 2022 inspirado en el de El Salvador, y en 2024 anunció planes para construir una cárcel al estilo del CECOT.

Es un caso interesante porque muestra que el modelo de Bukele atrae más allá de las ideologías: un gobierno de izquierda copió la política de un presidente que se enfrenta con la izquierda salvadoreña.

Pero los analistas advierten que no es lo mismo. Según un análisis de la Universidad de Navarra, la receta de Bukele no funciona igual en Honduras porque allí mata más el narcotráfico que las maras, el gobierno tiene menos poder y los cuerpos policiales son más complejos.

O sea, el problema hondureño es distinto en su origen: las maras están, pero no son la principal fuente de violencia, y el Estado no tiene el mismo control sobre sus instituciones que el gobierno salvadoreño.

No tengo en mis documentos cifras de homicidios de Honduras ni una evaluación de cómo le ha ido con esa medida. ¿Quieres saber qué otros países han copiado el modelo?
""")

E("sv-j012", "X01", "hecho", "¿Qué decía Fidel Castro de la lucha armada en El Salvador?",
  [[B("Fidel Castro discurso lucha armada El Salvador 1980", ["FR-P04-005", "FR-P05-001"])]],
  """
La cita más clara que tengo viene de un documento del gobierno de Estados Unidos, así que te la doy con esa atribución.

Según un informe especial del Departamento de Estado de Estados Unidos de 1981, el gobierno de Castro quiso desde el principio reproducir en otros países la guerra de guerrillas rural del Movimiento 26 de Julio. Ese mismo informe dice que Fidel Castro declaró el 26 de julio de 1980 que Guatemala, El Salvador, Chile y Bolivia enseñaban que no había otra fórmula que la lucha armada revolucionaria.

Ese informe es la postura de Washington en plena Guerra Fría, cuando buscaba justificar su apoyo al gobierno salvadoreño, así que conviene leerlo como tal.

Lo que dice una agencia de prensa coincide en el fondo: según un despacho de AFP publicado por T13, Castro, animado por el triunfo sandinista de julio de 1979, apoyó con decisión a la guerrilla salvadoreña, y en noviembre de 1989 apoyó la ofensiva guerrillera sobre San Salvador.

Es decir, que Castro defendía la vía armada y apoyó a la guerrilla salvadoreña está respaldado por fuentes distintas. El alcance exacto de ese apoyo es lo que cada lado describe a su manera.
""")

E("sv-j013", "P05", "hecho", "¿Qué fue la ofensiva de 1989?",
  [[B("ofensiva guerrillera San Salvador noviembre 1989", ["FR-P05-001", "FR-E01-008", "FR-E01-007"], epoca="P05")]],
  """
En noviembre de 1989 la guerrilla del FMLN lanzó una gran ofensiva sobre San Salvador, la capital. Según un despacho de AFP publicado por T13, Fidel Castro apoyó esa ofensiva.

Eso es todo lo que tengo documentado sobre ella en mi colección: la fecha, que fue sobre la capital y el apoyo de Castro. No tengo en mis documentos cuánto duró, cuántos muertos dejó ni los episodios concretos que ocurrieron durante esos días, así que no te los voy a contar de memoria.

Lo que sí te puedo dar es el contexto. La ofensiva llegó tras casi una década de guerra, en la que ninguno de los dos bandos lograba ganar. Y unos meses después, según El Diario de Hoy, el 4 de abril de 1990 se firmó en Ginebra el primer acuerdo formal entre el gobierno y la guerrilla, que sirvió de base para los acuerdos de paz de 1992.

Por eso se suele ver la ofensiva como uno de los empujones hacia la negociación: mostró que la guerrilla podía golpear la capital, pero también que no podía tomar el poder.

Si quieres, te cuento cómo se llegó a los acuerdos de paz.
""")

E("sv-j014", "E15", "contexto", "¿Por qué Haití tiene tantas pandillas?",
  [[B("crisis Haití pandillas causas gobierno elecciones", ["FR-E15-021", "FR-E15-015"], epoca="E15")]],
  """
Mis documentos están centrados en El Salvador, así que de las causas profundas de la crisis haitiana tengo poco. Te doy lo que sí está documentado y te digo dónde están los límites.

Lo que tengo: según Latin Times, Haití aplazó sin fecha las elecciones previstas para diciembre de 2026, y el país no tiene un gobierno elegido en las urnas desde 2016. Esa debilidad del Estado es parte del terreno en el que las bandas crecieron.

También hay un ejemplo de hasta dónde llegó su control: según EFE, el estadio Sylvio Cator, el principal del país, estuvo en manos de las bandas desde febrero de 2024 hasta que una operación conjunta lo recuperó en noviembre de 2026.

Y la propia fuerza internacional tiene problemas para llenarse: en octubre de 2026 tenía alrededor del 37 % de las tropas previstas.

Lo que no tengo: la historia de cómo se formaron las bandas haitianas, quién las financia o sus vínculos políticos.

Para entender bien las causas te convendría una fuente especializada en Haití; si quieres, te ayudo a pensar qué buscar.
""")

E("sv-j015", "E12", "conflicto", "¿Bukele ganó con el 84 % o con el 43 %? He visto las dos cifras.",
  [[B("resultado elección 2024 porcentaje votos válidos padrón", ["FR-E12-001", "FR-E12-003"], epoca="E12")]],
  """
Las dos cifras son correctas, pero miden cosas distintas. Por eso cada lado usa la que le conviene.

El 84,65 %: según el Tribunal Supremo Electoral, el 4 de febrero de 2024 Bukele fue reelegido con 2.701.725 votos, el 84,65 % de los votos válidos. Es el porcentaje sobre la gente que fue a votar y emitió un voto válido. Es la cifra oficial del resultado, y la que destaca el gobierno.

El 43,48 %: según El Diario de Hoy, de los 6.214.399 salvadoreños habilitados para votar, más de 2,9 millones no votaron. Si se mide el voto de Bukele contra todo el padrón, incluidos los que no votaron, equivale al 43,48 %. Es la cifra que destacan sus críticos para decir que no lo apoya la mayoría absoluta de los ciudadanos.

Las elecciones en todo el mundo se ganan con los votos válidos, no con el padrón, así que el resultado oficial es el 84,65 %. El 43,48 % sirve para otra discusión: cuánta gente participó y cuánta no.

Las dos lecturas son legítimas siempre que se diga qué mide cada una. Lo que no es correcto es presentar el 43,48 % como si fuera el resultado de la elección.
""")

E("sv-j016", "general", "hecho", "Ponme a prueba: hazme tres preguntas sobre la historia de El Salvador.",
  [[B("datos clave historia El Salvador", ["FR-P02-006", "FR-E01-007", "FR-E10-002"])]],
  """
¡Va! Te hago tres preguntas, y debajo pongo las respuestas para que no hagas trampa mirando antes.

Primera: ¿de quién tomó su nombre la guerrilla del FMLN y en qué año murió esa persona?

Segunda: ¿en qué lugar y en qué fecha se firmaron los acuerdos de paz que terminaron la guerra civil?

Tercera: ¿cuántos diputados votaron a favor del régimen de excepción el día que se aprobó, y de cuántos?

.
.
.

Respuestas:

Primera: de Farabundo Martí, fusilado el 1 de febrero de 1932 en San Salvador, a los 38 años. Casi medio siglo después, la coalición guerrillera de 1980 tomó su nombre.

Segunda: en el castillo de Chapultepec, en Ciudad de México, el 16 de enero de 1992. Los firmaron el gobierno de Alfredo Cristiani y la comandancia del FMLN, con mediación de la ONU.

Tercera: 67 de los 84 diputados, el 27 de marzo de 2022, a petición de Bukele.

¿Cuántas acertaste? Si quieres, subo la dificultad o te hago preguntas de una época concreta.
""")

guardar("ejemplos_lote_j.jsonl")
