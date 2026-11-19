"""
ejemplos_lote_e.py — Ejemplos de entrenamiento, lote E: historia (P01–P05, E01–E05, T02, T04, X01).
Preguntas con otras palabras, preguntas cortas o vagas que igual se contestan buscando primero, varios turnos,
líneas de tiempo, tabla de cifras y lectura de documentos.
Uso (desde E:\\vertex-salvador):  python ejemplos_lote_e.py  ->  datos\\ejemplos_lote_e.jsonl
"""
from ejemplos_base import B, C, D, E, L, guardar

# ---------------------------------------------------------------- P01–P03
E("sv-e001", "P01", "contexto", "¿De dónde viene el problema de la tierra en El Salvador?",
  [[B("reforma agraria liberal tierras comunales café", ["FR-P01-001", "FR-P02-001", "FR-P02-003"], epoca="P01")]],
  """
Hay que irse al siglo diecinueve, al café.

Según un texto académico de la colección de la UCA, la Reforma Agraria Liberal de 1881-1882 suprimió la propiedad comunal de la tierra. Muchas comunidades campesinas e indígenas trabajaban tierras que eran de todos; al desaparecer esa figura, la tierra se fue concentrando en pocas manos y se dedicó al café, y muchos campesinos perdieron las parcelas que trabajaban.

Eso armó una economía muy dependiente de un solo producto. Por eso, cuando llegó la crisis de 1929, el golpe fue tremendo: según el mismo texto, se hundieron los precios internacionales del café, el país quedó con excedentes que nadie compraba y sin liquidez, los salarios cayeron por debajo de lo necesario para vivir y hubo desempleo masivo.

Esa mezcla de campesinos sin tierra y crisis económica es el fondo de lo que vino después: el levantamiento de 1932 y su represión, que marcaron la política salvadoreña durante décadas.

Si quieres seguir el hilo, el siguiente paso natural es La Matanza de 1932.
""")

E("sv-e002", "P02", "hecho", "háblame de 1932",
  [[B("levantamiento 1932 La Matanza", ["FR-P02-003", "FR-P02-005", "FR-P02-006"], epoca="P02")]],
  """
1932 es el año de La Matanza, uno de los episodios más duros de la historia salvadoreña.

Entre el 22 y el 25 de enero de 1932 hubo un levantamiento en el occidente del país. Lo encabezaron comunistas, con Farabundo Martí, e indígenas, con Feliciano Ama. El gobierno del general Maximiliano Hernández Martínez lo aplastó, y esa represión es lo que se conoce como La Matanza.

Cuántos murieron no está fijado. El Salvador Perspectives habla de decenas de miles de campesinos muertos en la represión del ejército, y un trabajo de la Universidad del Sur de California da más de 30.000 hombres, mujeres y niños. Durante el levantamiento, según Wikipedia, los rebeldes mataron a unas 2.000 personas.

Farabundo Martí fue fusilado el 1 de febrero de 1932 en San Salvador, a los 38 años. Casi medio siglo después, la coalición guerrillera de 1980 tomó su nombre: Frente Farabundo Martí para la Liberación Nacional.

Por eso 1932 pesa tanto: dejó una herida en el campo y le dio a la izquierda armada su símbolo.
""")

E("sv-e003", "P02", "hecho", "¿Quién era Feliciano Ama?",
  [[B("Feliciano Ama levantamiento 1932", ["FR-P02-003", "FR-P02-004"], epoca="P02")]],
  """
Feliciano Ama fue uno de los líderes indígenas del levantamiento de 1932 en el occidente de El Salvador.

Lo que tengo documentado es su papel en ese momento: entre el 22 y el 25 de enero de 1932 hubo una rebelión encabezada por comunistas, con Farabundo Martí, y por indígenas, con Feliciano Ama. El gobierno del general Maximiliano Hernández Martínez la aplastó, y esa represión se conoce como La Matanza.

Sobre las causas, la Encyclopedia of Latin American History dice que la revuelta nació del enojo de los trabajadores del café y de los campesinos por sus condiciones de vida, y de la agitación de los dirigentes del Partido Comunista, sobre todo de Farabundo Martí.

Esa doble cara importa: hubo una dirección comunista, pero también un componente indígena y campesino con sus propios agravios, ligados a la pérdida de tierras.

De la vida de Ama antes y fuera de la rebelión no tengo más datos en mis documentos, así que no te voy a inventar una biografía. Si quieres, te cuento quién era Farabundo Martí, del que sí hay más información.
""")

E("sv-e004", "P02", "conflicto", "¿Cuántos murieron en La Matanza? Me han dicho cifras muy distintas.",
  [[B("número de muertos La Matanza 1932", ["FR-P02-005"], epoca="P02")]],
  """
Es normal que te hayan dado cifras distintas, porque no hay un número fijado.

Te doy cada estimación con su fuente. El Salvador Perspectives habla de decenas de miles de campesinos muertos en la represión del ejército. Un trabajo de la Universidad del Sur de California da más de 30.000 hombres, mujeres y niños. Y del otro lado, durante el propio levantamiento, según Wikipedia, los rebeldes mataron a unas 2.000 personas.

¿Por qué la diferencia? Hay varias razones habituales en estos casos: la represión fue en zonas rurales, las autoridades de la época no dejaron un registro fiable de las víctimas, y los cálculos posteriores salen de testimonios, censos y estudios con métodos distintos.

Lo que sí comparten las fuentes es la escala: la represión del ejército mató a muchísima más gente que la rebelión. En el debate político, la derecha y la izquierda salvadoreñas han usado esas cifras de forma distinta, pero ninguna fuente seria pone en duda que fue una matanza.

Si alguien te da un número exacto sin decir de dónde sale, desconfía.
""")

E("sv-e005", "P03", "hecho", "¿Por qué Duarte terminó en Venezuela?",
  [[B("Duarte elecciones 1972 exilio Venezuela", ["FR-P03-001", "FR-P03-002", "FR-P03-003", "FR-P03-004"], epoca="P03")]],
  """
Por las elecciones de 1972 y lo que vino después.

En las presidenciales del 20 de febrero de 1972, Arturo Armando Molina, del Partido de Conciliación Nacional (PCN), el partido de los militares, fue declarado ganador con el 43 % de los votos. Pero la junta electoral de San Salvador había anunciado que ganaba José Napoleón Duarte, candidato de la oposición unida, por unos 6.000 votos.

Tras esas elecciones hubo un intento de golpe que fracasó, y lo único que consiguió fue que Duarte fuera arrestado y desterrado a Venezuela, donde vivió hasta 1979.

Ese episodio es clave para entender los setenta. A mucha gente le dejó la idea de que por las urnas no se podía cambiar nada, porque cuando la oposición ganaba, el resultado no se respetaba. Las elecciones de 1977 estuvieron marcadas otra vez por denuncias de fraude.

Duarte volvió después del golpe de octubre de 1979 y llegó a ser una figura central de los años ochenta. Si quieres, te cuento el golpe de octubre de 1979.
""")

E("sv-e006", "P03", "hecho", "¿Hubo fraude en las elecciones de los setenta?",
  [[B("fraude elecciones 1972 1977", ["FR-P03-003", "FR-P03-001", "FR-P03-004"], epoca="P03")],
   [C("elecciones_presidenciales", [("1972", "Molina declarado ganador con 43 %", "Wikipedia", "FR-P03-001")], desde="1972", hasta="1977")]],
  """
Las dos presidenciales de esa década, la de 1972 y la de 1977, estuvieron marcadas por denuncias de fraude.

En 1972 el caso es bastante claro en las fuentes: Arturo Armando Molina, del PCN, fue declarado ganador con el 43 % de los votos, cuando la junta electoral de San Salvador había anunciado que ganaba José Napoleón Duarte, de la oposición unida, por unos 6.000 votos.

Para 1977 tengo el juicio de los estudios de país de la Biblioteca del Congreso de Estados Unidos, que dicen que esa votación se manipuló de forma aún más descarada que la de 1972. La tabla de cifras no trae un resultado numérico de 1977, así que no te doy porcentajes de ese año.

El efecto político fue profundo. Según la misma fuente, en los años setenta crecieron la represión y la frustración de la oposición. Mucha gente que había apostado por las urnas pasó a ver la lucha armada como el único camino, y hacia 1979 ya operaban varias organizaciones guerrilleras separadas.

Así que, sí: es uno de los ingredientes de la guerra de los años ochenta.
""")

E("sv-e007", "P03", "hecho", "¿Quiénes formaron la junta de 1979?",
  [[B("Junta Revolucionaria de Gobierno 1979 miembros", ["FR-P03-004", "FR-P03-005", "FR-P03-006"], epoca="P03")]],
  """
En octubre de 1979 un golpe militar sacó del poder al general Carlos Humberto Romero. Según la biografía del CIDOB, tomó el poder entonces una Junta Revolucionaria de Gobierno de cinco miembros: dos coroneles, Adolfo Majano y Jaime Abdul Gutiérrez, y tres civiles, entre ellos Guillermo Manuel Ungo.

¿Qué intentó esa junta? Según el California Migration Project, hizo algunas reformas agrarias y nacionalizó el comercio del café. Al mismo tiempo, Estados Unidos, con Cuba y Nicaragua ya gobernadas por revoluciones, buscaba impedir que la revolución se extendiera por el continente, y vio en la junta una forma de frenarla con reformas.

El contexto pesa: para 1979 ya operaban en El Salvador varias organizaciones guerrilleras separadas, y en Nicaragua los sandinistas acababan de tomar el poder en julio.

De los otros dos civiles no tengo los nombres en mis documentos, así que no te los voy a dar de memoria. Si quieres, te cuento cómo esas guerrillas separadas terminaron unificándose en el FMLN.
""")

# ---------------------------------------------------------------- P04–P05 y X01
E("sv-e008", "P04", "contexto", "¿Qué tenía que ver Cuba con las guerrillas de Centroamérica?",
  [[B("Cuba apoyo guerrillas América Latina Tricontinental OLAS", ["FR-P04-001", "FR-P04-002", "FR-P04-004"], epoca="P04")]],
  """
Mucho, y desde los años sesenta. Te lo cuento por pasos.

Del 3 al 15 de enero de 1966 La Habana acogió la Conferencia Tricontinental, con 512 delegados de 82 países de Asia, África y América Latina. De ahí nació la OSPAAAL, y la conferencia declaró su apoyo a la lucha armada.

Según el sociólogo Emir Sader, en 1967 Cuba convocó además la Organización Latinoamericana de Solidaridad (OLAS), que optó abiertamente por las guerrillas. Pero cuando la lucha armada se reanudó en la década siguiente, con el centro en Centroamérica, la OLAS ya era solo un órgano de difusión sin capacidad real de coordinar a nadie.

El aparato que sí funcionó fue otro. Según un estudio publicado en la revista EIAL, el Departamento América del Partido Comunista de Cuba fue el enlace de La Habana con las guerrillas de América Latina y el Caribe.

Así que hubo dos niveles: la idea, que Cuba proclamó en voz alta, de que la revolución se hacía con las armas, y una estructura práctica para relacionarse con los movimientos. Cómo se aplicó eso en El Salvador es la siguiente parte de la historia; te la busco si quieres.
""")

E("sv-e009", "P04", "hecho", "¿Quién era Barbarroja?",
  [[B("Manuel Piñeiro Barbarroja Departamento América", ["FR-P04-003", "FR-P04-004"], epoca="P04")]],
  """
Barbarroja era el apodo de Manuel Piñeiro, el cubano que dirigió durante años el Departamento América del Comité Central del Partido Comunista de Cuba.

Ese departamento se encargaba de centralizar el control y la ayuda a los grupos insurgentes de América Latina. Según un estudio publicado en la revista EIAL, fue el aparato de enlace de Cuba con las guerrillas del continente y del Caribe, y más tarde también representó al Partido en la diplomacia cubana.

Sobre desde cuándo lo dirigió hay una pequeña discrepancia entre fuentes: el diario El Tiempo fecha en 1974 el inicio de su mando, y una entrevista recogida por Archivo Chile lo sitúa desde 1975.

Para El Salvador es un nombre importante. Según un artículo de Cold War History basado en entrevistas con excomandantes del FMLN, varios de ellos, como Joaquín Villalobos, Eduardo Sancho y Claudio Armijo, contaron que el Departamento América era la vía para llegar a Fidel Castro.

Si quieres, te busco cómo describen esos excomandantes la relación con Cuba.
""")

E("sv-e010", "X01", "perspectivas", "¿Cuba entrenó y dirigió a la guerrilla salvadoreña?",
  [[B("Cuba papel FMLN unificación guerrilla", ["FR-P05-001", "FR-P05-003", "FR-P05-005", "FR-P05-006"], epoca="P05")]],
  """
Que Cuba apoyó a la guerrilla salvadoreña está documentado. Lo que se discute es cuánto la dirigió. Te doy cada versión con nombre.

Lo que dice una agencia de prensa: según un despacho de AFP publicado por T13, Fidel Castro, animado por el triunfo sandinista de julio de 1979, apoyó con decisión a la guerrilla salvadoreña, que estaba dispersa; las cinco organizaciones fundaron el FMLN en La Habana el 10 de octubre de 1980.

Lo que decía Estados Unidos: según el informe que su delegación presentó en 1981 ante la Comisión de Derechos Humanos de la ONU, Castro y el gobierno cubano tuvieron un papel tutelar directo para agrupar a las facciones en un frente unificado y asesoraron la planificación de sus operaciones. Es la postura de un gobierno enfrentado a Cuba.

Lo que dicen los excomandantes: según un artículo de Cold War History basado en entrevistas, dirigentes como Ana Guadalupe Martínez y Salvador Sánchez Cerén coincidieron en que Cuba encarnaba la posibilidad del cambio, y Fidel Castro y el Che Guevara eran sus modelos.

Y lo que decía la propia guerrilla: según su manifiesto del 10 de enero de 1980, la lucha tenía raíces históricas propias, como la encabezada por Farabundo Martí.

En pocas palabras: apoyo e influencia sí; que fuera una creación cubana es la tesis de Washington, y la guerrilla la rechazaba.
""")

E("sv-e011", "X01", "multiple", "Tengo un modelo sobre el exilio cubano. ¿Dónde se cruza esa historia con la de El Salvador?",
  [[B("Cuba revolución expansión Centroamérica El Salvador", ["FR-P04-001", "FR-P04-005", "FR-P05-001", "FR-P03-006"])]],
  """
El cruce está en los años sesenta a ochenta, cuando la Revolución Cubana quiso extenderse y Centroamérica se volvió su frente principal.

Del lado cubano, la Conferencia Tricontinental, del 3 al 15 de enero de 1966 en La Habana, declaró su apoyo a la lucha armada. Según un informe especial del Departamento de Estado de EE. UU. de 1981, el gobierno de Castro quiso desde el principio reproducir en otros países la guerra de guerrillas del Movimiento 26 de Julio, y Castro declaró el 26 de julio de 1980 que Guatemala, El Salvador, Chile y Bolivia enseñaban que no había otra fórmula que la lucha armada. Ese informe es la postura de Washington, no un hecho neutro.

Del lado salvadoreño, según AFP, Castro apoyó con decisión a la guerrilla dispersa y las cinco organizaciones fundaron el FMLN en La Habana el 10 de octubre de 1980.

Y Estados Unidos reaccionó: según el California Migration Project, tras el golpe de 1979 Washington buscaba impedir que la revolución se extendiera, con Cuba y Nicaragua ya gobernadas por revoluciones.

Para tu proyecto, el punto de unión es claro: el mismo gobierno del que salió el exilio cubano fue el que apoyó a la guerrilla salvadoreña, y la respuesta de Washington a ese apoyo moldeó la guerra en El Salvador.
""")

E("sv-e012", "P05", "hecho", "¿Cuándo nació el FMLN?",
  [[B("fundación FMLN 1980 organizaciones", ["FR-P05-002", "FR-P02-006", "FR-E01-007"], epoca="P05")]],
  """
El FMLN se formó el 10 de octubre de 1980 como coalición de cinco organizaciones de izquierda.

Eran estas: las Fuerzas Populares de Liberación (FPL), el Ejército Revolucionario del Pueblo (ERP), la Resistencia Nacional (RN), el Partido Comunista Salvadoreño (PCS) y el Partido Revolucionario de los Trabajadores Centroamericanos (PRTC). Esta última se sumó un poco después, el 5 de diciembre de 1980.

El nombre no es casual. Frente Farabundo Martí para la Liberación Nacional recoge el nombre de Farabundo Martí, el dirigente comunista fusilado el 1 de febrero de 1932 en San Salvador, a los 38 años, tras el levantamiento de ese año. Casi medio siglo después la guerrilla lo adoptó como símbolo.

La unificación fue importante porque hasta entonces esas organizaciones actuaban por separado y con rivalidades entre ellas. Juntas pudieron coordinar la guerra que empezaba.

El FMLN combatió hasta los acuerdos de paz de 1992 y después se convirtió en partido político, el mismo en el que, años más tarde, empezó su carrera Nayib Bukele. Si quieres, sigo por ahí.
""")

E("sv-e013", "P05", "hecho", "¿El FMLN se fundó en Cuba?",
  [[B("FMLN fundado en La Habana", ["FR-P05-001", "FR-P05-002"], epoca="P05")]],
  """
Según la fuente que tengo, sí. Un despacho de AFP publicado por T13 dice que las cinco organizaciones guerrilleras fundaron el FMLN en La Habana el 10 de octubre de 1980, con el apoyo decidido de Fidel Castro, que estaba animado por el triunfo sandinista de julio de 1979.

La fecha coincide con la que dan otras fuentes para la formación de la coalición: el 10 de octubre de 1980, con las FPL, el ERP, la Resistencia Nacional, el Partido Comunista Salvadoreño y el PRTC, que se sumó el 5 de diciembre de ese año.

Lo del lugar, La Habana, solo lo tengo de esa fuente, así que te lo doy atribuido y no como un hecho confirmado por varias.

Lo que conviene no mezclar: que se fundara en Cuba y con apoyo cubano no quiere decir que Cuba lo inventara de la nada. Las organizaciones ya existían y peleaban por separado antes de 1980; lo que Castro impulsó, según varias fuentes, fue su unificación.

Según AFP, Castro también apoyó en noviembre de 1989 la gran ofensiva guerrillera sobre San Salvador. ¿Quieres que te cuente esa parte?
""")

# ---------------------------------------------------------------- E01 guerra
E("sv-e014", "E01", "hecho", "¿Por qué es tan importante monseñor Romero?",
  [[B("monseñor Romero asesinato carta a Carter", ["FR-E01-001", "FR-E01-002"], epoca="E01")]],
  """
Monseñor Óscar Arnulfo Romero era el arzobispo de San Salvador, y su asesinato marcó el arranque de la guerra.

Lo mataron de un disparo el 24 de marzo de 1980 mientras celebraba misa en la capilla de un hospital de San Salvador. Que asesinaran al arzobispo en pleno altar le mostró al país y al mundo hasta dónde había llegado la violencia política.

Romero se había vuelto una voz muy incómoda. Según el Zinn Education Project, en febrero de 1980, un mes antes de morir, escribió al presidente Jimmy Carter para pedirle que detuviera la ayuda militar de Estados Unidos al gobierno salvadoreño. Para los sectores más pobres era quien hablaba por ellos; para otros, un obispo que se había metido en política.

Su figura sigue pesando en El Salvador. Es una referencia moral para mucha gente, más allá de la Iglesia, y su muerte es uno de los casos que investigó después la Comisión de la Verdad.

Si quieres, te busco qué concluyó la Comisión de la Verdad sobre la violencia de esos años.
""")

E("sv-e015", "E01", "hecho", "¿Quién hizo la masacre de El Mozote?",
  [[B("El Mozote masacre Batallón Atlacatl", ["FR-E01-003", "FR-E01-005"], epoca="E01")]],
  """
La hizo el ejército salvadoreño, con unidades del Batallón Atlacatl.

Según Wikipedia, el 11 de diciembre de 1981, en El Mozote y caseríos vecinos del departamento de Morazán, el ejército mató a más de 800 civiles. La operación la hicieron unidades del Batallón Atlacatl, una unidad de reacción rápida creada en 1980.

Es la peor masacre de la guerra y una de las peores de América Latina en el siglo veinte. Las víctimas eran campesinos de una zona donde la guerrilla tenía presencia.

Encaja con el panorama general que dibujó después la Comisión de la Verdad. Según un análisis académico de la Universidad Federal de Pelotas, el informe de la Comisión atribuyó al ejército y a grupos paramilitares el 85 % de las violaciones que documentó, y responsabilizó al FMLN de una parte menor.

Que la responsabilidad principal sea del Estado no borra los crímenes de la guerrilla, que también los hubo. Pero en El Mozote la autoría está clara.

Si te interesa, te cuento qué pasó con esos crímenes después de la guerra, con la ley de amnistía que se aprobó al terminar la guerra.
""")

E("sv-e016", "E01", "hecho", "¿Qué fue la amnistía de 1993?",
  [[B("amnistía general 1993 Cristiani", ["FR-E01-006", "FR-E01-004"], epoca="E01")]],
  """
Fue la ley que dejó sin castigo los crímenes de la guerra, aprobada casi de inmediato después del informe de la Comisión de la Verdad.

El orden de los hechos lo dice todo. La Comisión de la Verdad, creada por los Acuerdos de Paz, hizo público su informe, «De la locura a la esperanza», el 15 de marzo de 1993. Según la Comisión Interamericana de Derechos Humanos, el 18 de marzo de 1993, apenas tres días después, el presidente Alfredo Cristiani anunció una amnistía general que dejó sin castigo los crímenes cometidos por agentes del Estado entre 1980 y 1992.

Para el gobierno de entonces, era una forma de cerrar la guerra y evitar que la reconciliación se rompiera con juicios. Para las víctimas y las organizaciones de derechos humanos, fue una forma de garantizar la impunidad justo cuando se sabía quién había hecho qué.

La Comisión Interamericana fue muy crítica con esa ley, y por eso la cito como fuente de la fecha y del alcance.

Si quieres, te busco qué concluyó el informe de la Comisión de la Verdad, que es lo que la amnistía dejó sin consecuencias.
""")

E("sv-e017", "E01", "hecho", "¿Cómo empezaron las conversaciones de paz?",
  [[B("camino a la paz La Palma Ginebra Chapultepec", ["FR-E01-008", "FR-E01-007"], epoca="E01")]],
  """
Fue un proceso largo, de casi ocho años, con tres momentos clave.

El primero fue un acercamiento. Según El Diario de Hoy, el camino a la paz empezó con un encuentro en la iglesia de La Palma, Chalatenango, el 15 de octubre de 1984, entre el gobierno y la guerrilla.

El segundo fue el primer acuerdo formal. Según la misma fuente, el de Ginebra se firmó el 4 de abril de 1990 y sirvió de base para los acuerdos finales.

El tercero fue la firma. El 16 de enero de 1992, en el castillo de Chapultepec, en Ciudad de México, el gobierno de Alfredo Cristiani y la comandancia del FMLN firmaron, con mediación de la ONU, los acuerdos que pusieron fin a doce años de guerra.

Entre La Palma y Ginebra hubo años de guerra abierta, y fue la propia guerra la que empujó a las partes: ninguna podía ganarla del todo.

Los acuerdos crearon, entre otras cosas, la Comisión de la Verdad, que se constituyó ese mismo 1992. Si quieres, te cuento qué concluyó.
""")

E("sv-e018", "E01", "hecho", "Dame las cifras de la guerra civil: muertos, desaparecidos y ayuda de Estados Unidos.",
  [[C("victimas_guerra_civil", [("1980-1992", "más de 75.000 muertos y 7.000 desaparecidos", "EFE", "FR-E01-009"),
                                ("1980-1992", "75.000 muertos, 8.000 desaparecidos y 12.000 presos", "Voz de América", "FR-E01-009")]),
    C("ayuda_eeuu_guerra", [("1979-1991", "más de 6.000 millones de dólares", "California Migration Project", "FR-E01-010"),
                            ("1980-1988", "3.348,5 millones de dólares", "Universidad de El Salvador", "FR-E01-010")])],
   [D("FR-E01-010")]],
  """
Aquí van, cada una con su fuente, porque ninguna de las dos cosas tiene una cifra única.

Víctimas:
- Según un despacho de EFE, más de 75.000 muertos y 7.000 desaparecidos.
- Según la Voz de América, 75.000 muertos, 8.000 desaparecidos y 12.000 presos.

Las dos coinciden en el orden de los muertos y difieren en desaparecidos. Es lo habitual en guerras sin registros completos.

Ayuda de Estados Unidos:
- Según el California Migration Project, más de 6.000 millones de dólares entre 1979 y 1991.
- Según un estudio de la Universidad de El Salvador, 3.348,5 millones de dólares de ayuda económica y militar entre 1980 y 1988, a través de la AID.
- Y según una nota de la revista ECA, la cifra que más se repite es de 5.000 millones.

Fíjate en que los periodos no son los mismos: una cuenta doce años y otra nueve, y no todas incluyen los mismos tipos de ayuda. Por eso no se pueden comparar como si midieran lo mismo.

Si me dices para qué las necesitas, te recomiendo cuál citar y cómo.
""")

E("sv-e019", "E01", "contexto", "¿Por qué Estados Unidos apoyó al gobierno salvadoreño en la guerra?",
  [[B("Estados Unidos apoyo gobierno salvadoreño impedir revolución", ["FR-P03-006", "FR-E01-010", "FR-E01-002"])]],
  """
Por la Guerra Fría. Washington veía El Salvador como el siguiente país que podía caer tras Cuba y Nicaragua.

Según el California Migration Project, tras el golpe de 1979, con Cuba y Nicaragua ya gobernadas por revoluciones, Estados Unidos buscaba impedir que la revolución se extendiera por el continente. El Salvador, con una guerrilla en crecimiento y apoyo cubano, era el lugar donde querían frenarla.

Ese apoyo fue enorme, aunque las cifras varían: el mismo California Migration Project da más de 6.000 millones de dólares entre 1979 y 1991; un estudio de la Universidad de El Salvador cuenta 3.348,5 millones entre 1980 y 1988; y la revista ECA dice que la cifra que más se repite es de 5.000 millones.

No todo el mundo estaba de acuerdo, ni siquiera en Estados Unidos. Según el Zinn Education Project, en febrero de 1980 monseñor Romero le escribió a Jimmy Carter pidiéndole que detuviera la ayuda militar. Un mes después lo asesinaron.

El debate de fondo, que sigue hasta hoy, es si esa ayuda evitó un gobierno como el cubano o si alargó una guerra en la que el ejército cometió la mayoría de las atrocidades.
""")

# ---------------------------------------------------------------- E02 maras
E("sv-e020", "E02", "hecho", "¿Es verdad que la MS-13 se inventó en Estados Unidos?",
  [[B("origen MS-13 Los Ángeles Pico-Union", ["FR-E02-001", "FR-E02-002"], epoca="E02")]],
  """
Sí. La Mara Salvatrucha (MS-13) nació en los años ochenta en el barrio de Pico-Union, en Los Ángeles.

La formaron jóvenes salvadoreños que habían huido de la guerra civil o eran hijos de refugiados, y al principio su función era protegerse de las otras pandillas de la zona, que eran más antiguas y más grandes.

Para entender por qué había tantos salvadoreños en Los Ángeles hay que volver a la guerra. Según el Migration Policy Institute, la diáspora salvadoreña en Estados Unidos es en gran parte producto de las guerras civiles centroamericanas, en las que Washington apoyó a los gobiernos que combatían a las guerrillas. En 2019 esa diáspora sumaba 1,4 millones de personas, y el grupo más grande vivía en Los Ángeles.

Así que el origen es una cadena: la guerra expulsó a mucha gente, muchos llegaron a barrios pobres de Los Ángeles, y allí algunos jóvenes formaron la MS-13.

Cómo pasó después de Los Ángeles a El Salvador es otra parte de la historia: las deportaciones de los noventa. ¿Te la cuento?
""")

E("sv-e021", "E02", "contexto", "¿Las deportaciones de Estados Unidos tienen la culpa de las maras en El Salvador?",
  [[B("deportaciones años noventa MS-13 Centroamérica", ["FR-E02-003", "FR-E02-004", "FR-E02-005"], epoca="E02")]],
  """
Son una parte grande de la explicación, aunque no la única.

Las deportaciones desde Estados Unidos se triplicaron a finales de los años noventa y llevaron la MS-13 a Centroamérica, donde los miembros deportados abrieron nuevos grupos. Esas deportaciones las permitieron las leyes de la época del presidente Clinton, que facilitaron expulsar a inmigrantes con antecedentes penales. En esa década la MS-13 pasó de pandilla juvenil a pandilla carcelaria y a organización transnacional.

Además, el ir y venir constante entre Los Ángeles y Centroamérica permitió que el Barrio 18 y la MS-13 se asentaran en El Salvador entre finales de los ochenta y principios de los noventa.

El efecto fue brutal. Según Wikipedia, tras la llegada de las pandillas desde Los Ángeles la tasa de homicidios llegó a 139 por cada 100.000 habitantes en 1995.

Ahora, decir que la culpa es solo de Estados Unidos deja fuera lo que pasaba en El Salvador: un país que salía de la guerra, con muchas armas en la calle, jóvenes sin oportunidades y un Estado débil. Las deportaciones trajeron la estructura; el terreno estaba preparado para que creciera.
""")

E("sv-e022", "T02", "hecho", "¿Qué diferencia hay entre la MS-13 y el Barrio 18?",
  [[B("MS-13 Barrio 18 diferencias estructura facciones", ["FR-T02-001", "FR-T02-002", "FR-E02-001"], epoca="T02")]],
  """
Las dos nacieron en Los Ángeles y se organizan de forma parecida, pero son enemigas a muerte y tienen diferencias.

Estructura común: las dos se dividen en células llamadas clicas, que funcionan con bastante autonomía. Las clicas se agrupan en programas, que responden a una dirección llamada ranfla. La extorsión es una de sus fuentes de dinero más importantes.

Diferencias:
- En general se considera que la MS-13 es la más sofisticada de las dos.
- La MS-13 nació en los años ochenta en Pico-Union, Los Ángeles, entre jóvenes salvadoreños que huían de la guerra o eran hijos de refugiados.
- El Barrio 18 se partió. Según InSight Crime, hacia 2005 peleas internas lo dividieron en El Salvador en dos facciones rivales, los Revolucionarios y los Sureños, que desde entonces también se enfrentan entre sí.

O sea que en El Salvador no había dos bandos, sino tres: la MS-13 y las dos facciones del 18, todos contra todos.

El Salvador declaró al Barrio 18 organización terrorista el 24 de agosto de 2015. Si quieres, te cuento qué pasó ese año, que fue el más violento de su historia.
""")

E("sv-e023", "T02", "hecho", "¿Qué es la ranfla?",
  [[B("ranfla dirección pandillas clicas programas", ["FR-T02-001"], epoca="T02")]],
  """
La ranfla es la dirección de las pandillas, la cúpula que está arriba de todo.

Para entenderla hay que ver la estructura completa. La MS-13 y el Barrio 18 se dividen en células llamadas clicas, que son los grupos de base en cada barrio o zona y funcionan con bastante autonomía. Las clicas se agrupan en programas, que reúnen a varias de ellas en un territorio más grande. Y los programas responden a la ranfla, que es la dirección.

Esa autonomía de las clicas es importante: no es un ejército con una cadena de mando rígida, sino una red. Por eso, cuando un gobierno negociaba con los líderes o los encerraba, no siempre se controlaba lo que hacían las clicas en la calle.

En cuanto al dinero, la extorsión es una de sus fuentes más importantes: cobrar a comerciantes, transportistas y vecinos a cambio de no atacarlos.

En general se considera que la MS-13 es la más sofisticada de las dos pandillas. Si quieres, te cuento cómo se dividió el Barrio 18 en dos facciones.
""")

E("sv-e024", "T04", "multiple", "Explícame la cadena: de la guerra a las maras y al régimen de excepción.",
  [[B("diáspora guerra civil pandillas transnacionales", ["FR-T04-001", "FR-E02-003"]),
    B("régimen de excepción marzo 2022", ["FR-E10-001", "FR-E10-002"])]],
  """
Va en eslabones, y cada uno explica el siguiente.

Primero, la guerra. Según el Migration Policy Institute, la diáspora salvadoreña es producto de las guerras civiles centroamericanas, y la evolución de la MS-13 y del Barrio 18 de pandillas juveniles a organizaciones transnacionales está ligada a esa diáspora.

Segundo, Los Ángeles. Muchos salvadoreños que huían de la guerra llegaron a barrios pobres de esa ciudad, y allí nacieron o crecieron las pandillas.

Tercero, las deportaciones. Se triplicaron a finales de los noventa con las leyes de la época de Clinton, y llevaron la MS-13 a Centroamérica, donde los deportados abrieron nuevos grupos.

Cuarto, la violencia en El Salvador. Las pandillas se apoderaron de barrios enteros y los homicidios llegaron a niveles de guerra.

Quinto, el régimen de excepción. Entre el 25 y el 27 de marzo de 2022 hubo 87 homicidios, 62 de ellos el sábado 26, y el 27 la Asamblea aprobó, a petición de Bukele, un régimen de excepción de 30 días, que se ha prorrogado desde entonces.

Ojo: es una cadena de causas, no de culpables únicos. En cada eslabón hubo decisiones de distintos actores, salvadoreños y extranjeros. ¿Quieres que profundice en alguno?
""")

# ---------------------------------------------------------------- E03–E05
E("sv-e025", "E03", "hecho", "¿Cuántos arrestaron con la Mano Dura?",
  [[C("detenciones_mano_dura", [("julio de 2003 a agosto de 2004", "19.275 arrestos; 17.540 liberados por falta de pruebas", "Policía, según InSight Crime", "FR-E03-002"),
                                ("2003-2005", "más de 30.000 arrestos", "Migration Policy Institute", "FR-E03-006")])]],
  """
Tengo dos cifras, de periodos distintos.

Según la Policía, citada por InSight Crime, el plan Mano Dura dejó 19.275 arrestos entre julio de 2003 y agosto de 2004. Lo llamativo es el otro número: 17.540 de esos detenidos quedaron libres por falta de pruebas. Es decir, la gran mayoría de las capturas no se sostuvo ante un juez.

Para un periodo más largo, el Migration Policy Institute dice que la Mano Dura arrestó a más de 30.000 supuestos pandilleros entre 2003 y 2005. Esa misma fuente añade un efecto que nadie buscaba: las cárceles se convirtieron en centros de reclutamiento de las pandillas, porque allí se juntaban, se organizaban y captaban a otros presos.

Esas dos lecciones, muchas capturas que no llegan a condena y cárceles que fortalecen a las pandillas, se repiten mucho en el debate sobre las políticas de mano dura en El Salvador, incluido el régimen de excepción.

Si quieres, te cuento si los homicidios bajaron o no con la Mano Dura, porque ahí las fuentes no coinciden.
""")

E("sv-e026", "E03", "hecho", "¿Qué fue la Ley Antimaras?",
  [[B("Ley Antimaras 2003 inconstitucional", ["FR-E03-002", "FR-E03-003", "FR-E03-001"], epoca="E03")]],
  """
Fue la ley que acompañó al plan Mano Dura del presidente Francisco Flores, de ARENA.

Flores presentó el plan en cadena nacional el 23 de julio de 2003: capturas sistemáticas de pandilleros y apoyo de la Fuerza Armada a la Policía en las calles. Según InSight Crime, la Ley Antimaras entró en vigor el 10 de octubre de 2003 para dar base legal a esas capturas.

El problema es que la ley era inconstitucional. Pero, según InSight Crime, a quienes sufrían a las pandillas no les importó. El plan Mano Dura reanimó al presidente y devolvió a su partido al camino de la victoria electoral: la gente veía que por fin se hacía algo.

Los resultados en los tribunales fueron flojos. Según la Policía, citada por la misma fuente, hubo 19.275 arrestos entre julio de 2003 y agosto de 2004, y 17.540 de esos detenidos quedaron libres por falta de pruebas.

Ese choque entre una política popular y su encaje legal es un patrón que vuelve a aparecer años después con el régimen de excepción. Si quieres, comparo las dos cosas.
""")

E("sv-e027", "E03", "perspectivas", "¿Saca tenía razón al decir que la Mano Dura funcionó?",
  [[B("Saca Súper Mano Dura efectiva", ["FR-E03-005", "FR-E03-004"], epoca="E03"),
    B("resultados Mano Dura homicidios cárceles", ["FR-E03-006", "FR-E03-007"], epoca="E03")]],
  """
Depende de qué midas. Te pongo lo que decía Saca y lo que dicen otras fuentes.

Lo que dijo Saca: según Infobae, al anunciar su plan en 2004, Antonio Saca afirmó que si lanzaba el Súper Mano Dura era porque el Mano Dura había sido efectivo. Lo presentó el 30 de agosto de 2004, a los 60 días de asumir, con programas de prevención y reinserción llamados Mano Amiga y Mano Extendida.

Lo que dicen los números: no coinciden. Con cifras de la Policía citadas por EFE, hubo 2.340 muertes violentas en 1999, 2.388 en 2003 y 2.933 en 2004, es decir, más. Wikipedia, en cambio, recoge un descenso del 14 % de los asesinatos en 2004, seguido de una subida hasta 64,7 por cada 100.000 habitantes en 2006.

Lo que dice un estudio del Migration Policy Institute: la Mano Dura arrestó a más de 30.000 supuestos pandilleros entre 2003 y 2005 y convirtió las cárceles en centros de reclutamiento.

Así que en lo político sí funcionó, porque ARENA siguió ganando. En homicidios, las cifras se contradicen. Y a mediano plazo, varias fuentes creen que fortaleció a las pandillas.
""")

E("sv-e028", "E04", "hecho", "¿Cuánto bajaron los homicidios con la tregua de 2012?",
  [[C("homicidios", [("marzo-diciembre de 2011", "3.697", "El Diario NY", "FR-E04-005"),
                     ("marzo-diciembre de 2012", "1.761", "El Diario NY", "FR-E04-005")], desde="2011", hasta="2012")],
   [B("tregua homicidios cayeron traslado líderes", ["FR-E04-002", "FR-E05-001", "FR-E04-006"], epoca="E04")]],
  """
Bajaron muchísimo, a menos de la mitad, y muy rápido.

Según El Diario NY, entre marzo y diciembre de 2011 hubo 3.697 homicidios, y en el mismo periodo de 2012, ya con la tregua, 1.761.

El cambio se notó desde el principio. El 14 de marzo de 2012 el periódico El Faro informó del traslado de 30 líderes pandilleros de la cárcel de máxima seguridad a otros penales, y dijo que respondía a una negociación del gobierno con las pandillas a cambio de bajar los homicidios. Las autoridades dieron explicaciones contradictorias, pero los homicidios cayeron un 53 % a partir del traslado.

El precio de esa baja es lo que se discute. Las pandillas no se desarmaron: siguieron con la extorsión y ganaron poder de negociación frente al Estado. Y cuando la tregua se rompió, la violencia volvió con más fuerza, hasta el récord de 2015.

Años después, en 2023, la justicia condenó a los responsables políticos de la tregua. Si quieres, te cuento cómo terminó ese juicio.
""")

E("sv-e029", "E04", "hecho", "¿Quién era Raúl Mijango?",
  [[B("Raúl Mijango tregua negociador absuelto", ["FR-E04-001", "FR-E04-006"], epoca="E04")]],
  """
Raúl Mijango fue uno de los principales negociadores de la tregua entre pandillas de 2012. Era exdiputado y exguerrillero.

La tregua duró del 9 de marzo de 2012 al 26 de mayo de 2014. Los negociadores principales fueron tres: el ministro de Seguridad, David Munguía Payés; Mijango; y el obispo Fabio Colindres, todo bajo la supervisión del presidente Mauricio Funes.

Su papel era el de mediador con los líderes de las pandillas. Que fuera un exguerrillero, con experiencia en las negociaciones de otra época, le daba un perfil particular para ese trabajo.

En lo judicial, su caso terminó distinto al de los políticos. Mijango fue absuelto en 2017 y en 2019. En cambio, en 2023 un tribunal de San Salvador condenó al exministro Munguía Payés a 18 años de cárcel y al expresidente Funes, juzgado en ausencia, a 14 años, por agrupaciones ilícitas e incumplimiento de deberes relacionados con la tregua.

Del resto de su vida, fuera de la tregua, no tengo datos en mis documentos. Si quieres, te cuento qué sostuvo la Fiscalía sobre quién fue el autor de la tregua.
""")

E("sv-e030", "E05", "hecho", "Dame los homicidios de 2015 a 2018.",
  [[C("homicidios", [("2015", "6.657 homicidios; 103 por cada 100.000", "estadísticas oficiales", "FR-E05-001"),
                     ("2016", "81 por cada 100.000", "fuentes oficiales citadas por AFP", "FR-E05-003"),
                     ("2017", "60 por cada 100.000", "fuentes oficiales citadas por AFP", "FR-E05-003"),
                     ("2018", "51 por cada 100.000; 3.340 asesinatos", "fuentes oficiales citadas por AFP", "FR-E05-003")],
      desde="2015", hasta="2018")],
   [B("llegada de Bukele a la presidencia 2019", ["FR-E07-001"], epoca="E07")]],
  """
Aquí van, según las cifras oficiales:

- 2015: al menos 6.657 homicidios, con una tasa de unos 103 por cada 100.000 habitantes. Es la más alta de la historia del país y convirtió a El Salvador en el país más violento del hemisferio occidental.
- 2016: 81 por cada 100.000 habitantes.
- 2017: 60 por cada 100.000.
- 2018: 51 por cada 100.000, con 3.340 asesinatos.

Para los años del medio solo tengo la tasa, no el número total de homicidios, así que no te lo calculo.

La tendencia es clara: después del récord de 2015 la violencia fue bajando año tras año. Eso es importante para un debate de hoy, porque esa baja empezó antes de que Bukele llegara a la presidencia en 2019. Su gobierno sostiene que logró acelerarla mucho, y sus críticos le recuerdan que ya venía de antes.

Si quieres, te busco qué explicación daban las autoridades de 2018 para esa baja, o te sigo la serie con los años de Bukele.
""")

E("sv-e031", "E05", "contexto", "¿Por qué se rompió la tregua y vino tanta violencia?",
  [[B("ruptura tregua violencia 2015 causas", ["FR-E04-007", "FR-E05-002", "FR-T02-002"])]],
  """
Hay dos explicaciones que se complementan, y una de ellas viene de una de las partes, así que te las separo.

La de la Fiscalía: según la Voz de América, la Fiscalía sostuvo en el juicio que el exministro David Munguía Payés fue el autor intelectual de la tregua, cuya ruptura convirtió a El Salvador en 2015 en el país más violento del mundo, y que el presidente Mauricio Funes aprobó el acuerdo y dispuso dinero público para el proceso. Es la acusación en un juicio, no una conclusión neutral.

La de los investigadores: según InSight Crime, lo que llevó a El Salvador al récord de 2015 fue una combinación de fragmentación de las pandillas, choques internos y grupos de justicia por mano propia.

Esa fragmentación tiene un origen concreto. Según la misma fuente, hacia 2005 el Barrio 18 se partió en dos facciones rivales, los Revolucionarios y los Sureños, que también se enfrentan entre sí. Ese mismo año, el 24 de agosto de 2015, El Salvador declaró al Barrio 18 organización terrorista.

O sea: al acabarse la tregua no solo volvió la guerra entre pandillas y Estado, sino una guerra de todos contra todos.
""")

E("sv-e032", "E05", "hecho", "¿Cuántos pandilleros calculaban que había en 2018?",
  [[B("número de pandilleros 2018 autoridades", ["FR-E05-004"], epoca="E05")],
   [C("detenciones_regimen", [("febrero de 2026", "más de 91.300", "decreto de prórroga de la Asamblea Legislativa", "FR-E14-002")])]],
  """
Según El Heraldo, en 2018 las autoridades salvadoreñas calculaban que las pandillas tenían algo más de 70.000 miembros, unos 17.000 de ellos presos.

Te lo doy como cálculo de las autoridades, porque es eso: una estimación del gobierno de entonces, no un censo. Contar a los miembros de una organización clandestina es muy difícil, y además no siempre está claro dónde se pone la línea entre un miembro, un colaborador y alguien de la familia o del barrio.

Esa misma fuente recoge que las autoridades atribuían la mayor parte de los homicidios a las pandillas, y que el ministro de Seguridad de entonces atribuyó la baja de ese año al combate contra la delincuencia y a programas de prevención y rehabilitación.

La cifra sirve para dar una idea del tamaño del problema antes del régimen de excepción. Años después, según el decreto de prórroga de febrero de 2026, el régimen había dejado más de 91.300 capturas de personas vinculadas a estructuras criminales, que es un número más alto que aquel cálculo; eso es parte del debate sobre a quién se ha detenido.
""",
  )

guardar("ejemplos_lote_e.jsonl")
