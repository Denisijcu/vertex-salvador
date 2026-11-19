"""
ejemplos_lote_a.py — Ejemplos de entrenamiento, lote A: de 1881 a 2018 (P01–P05, E01–E05, T02, T04).
Uso (desde E:\\vertex-salvador):  python ejemplos_lote_a.py  ->  datos\\ejemplos_lote_a.jsonl
"""
from ejemplos_base import B, C, D, E, L, guardar

E("sv-a001", "P02", "hecho", "¿Qué fue La Matanza de 1932?",
  [[B("La Matanza 1932 levantamiento campesino", ["FR-P02-003", "FR-P02-004", "FR-P02-005", "FR-P02-001"], epoca="P02")]],
  """
La Matanza es el nombre que en El Salvador se le da a la represión que siguió al levantamiento campesino de enero de 1932, uno de los episodios que más ha marcado la historia del país.

Entre el 22 y el 25 de enero de 1932 hubo una rebelión en el occidente del país. La encabezaban comunistas, con Farabundo Martí, e indígenas, con Feliciano Ama. El gobierno del general Maximiliano Hernández Martínez la aplastó, y a esa represión es a lo que se llama La Matanza.

El contexto ayuda a entenderlo. Con la crisis de 1929 se desplomaron los precios del café, que era el corazón de la economía; los salarios cayeron por debajo de lo necesario para vivir y hubo desempleo masivo. Según la Encyclopedia of Latin American History, la revuelta nació del enojo de los trabajadores del café y de los campesinos por esas condiciones y de la agitación de los dirigentes comunistas.

Lo que no está fijado es el número de muertos. El Salvador Perspectives habla de decenas de miles de campesinos muertos en la represión, y un trabajo de la Universidad del Sur de California da más de 30.000. Durante el levantamiento, según Wikipedia, los rebeldes mataron a unas 2.000 personas. Por eso conviene hablar de un rango y no de una cifra exacta.
""")

E("sv-a002", "P01", "contexto", "¿Por qué los campesinos se levantaron en 1932? ¿Tenía que ver con la tierra?",
  [[B("causas levantamiento 1932 tierra café reforma agraria", ["FR-P01-001", "FR-P02-001", "FR-P02-004"])]],
  """
Sí, la tierra está en el fondo de la historia, aunque no fue la única causa.

Según un texto académico de la colección de la UCA, la Reforma Agraria Liberal de 1881-1882 suprimió la propiedad comunal de la tierra. Eso permitió concentrarla en pocas manos y dedicarla al café, y muchos campesinos perdieron las tierras que trabajaban. Medio siglo después, buena parte del campo vivía de trabajar en fincas ajenas.

Luego vino el golpe económico. Con la crisis de 1929 se hundieron los precios internacionales del café. El país quedó con excedentes que no podía vender, sin liquidez, con salarios por debajo de lo necesario para subsistir y con desempleo masivo.

A eso se sumó la organización política. La Encyclopedia of Latin American History atribuye la revuelta de 1932 a dos factores juntos: el enojo de los trabajadores del café y de los campesinos por sus condiciones de vida, y la agitación de los dirigentes del Partido Comunista, en especial de Farabundo Martí.

O sea, que la pérdida de la tierra comunal preparó el terreno, la crisis del café lo volvió insoportable y la organización comunista le dio forma de levantamiento.
""")

E("sv-a003", "P02", "hecho", "¿Quién fue Farabundo Martí?",
  [[B("Farabundo Martí biografía Partido Comunista", ["FR-P02-002", "FR-P02-006", "FR-P02-003"])]],
  """
Farabundo Martí fue el dirigente comunista más conocido de El Salvador en la primera mitad del siglo veinte, y su nombre sigue presente en la política del país.

Fue uno de los dirigentes rurales de la Federación Regional de Trabajadores y, en 1930, fundó el Partido Comunista de El Salvador junto con Miguel Mármol. Antes había estado en Nicaragua luchando junto a Augusto César Sandino contra la ocupación estadounidense, una experiencia que lo convirtió en una figura con peso regional.

Su momento decisivo fue el levantamiento de enero de 1932 en el occidente del país, que encabezó del lado comunista mientras Feliciano Ama lo hacía del lado indígena. La rebelión fue aplastada por el gobierno del general Maximiliano Hernández Martínez, en la represión que se conoce como La Matanza.

Martí fue fusilado el 1 de febrero de 1932 en San Salvador, a los 38 años. Casi medio siglo más tarde, en 1980, la coalición guerrillera que se formó contra los gobiernos militares tomó su nombre: Frente Farabundo Martí para la Liberación Nacional, el FMLN.
""")

E("sv-a004", "P03", "hecho", "¿Qué pasó en las elecciones de 1972 en El Salvador?",
  [[B("elecciones presidenciales 1972 Duarte Molina fraude", ["FR-P03-001", "FR-P03-002", "FR-P03-003"], epoca="P03")]],
  """
Las elecciones de 1972 son una de las claves para entender por qué El Salvador terminó en guerra.

Se celebraron el 20 de febrero de 1972. El candidato oficial, Arturo Armando Molina, del Partido de Conciliación Nacional, fue declarado ganador con el 43 % de los votos. Pero la junta electoral de San Salvador había anunciado antes que el ganador era José Napoleón Duarte, el candidato de la oposición unida, por unos 6.000 votos. Esa contradicción alimentó las denuncias de fraude.

Después hubo un intento de golpe que no prosperó y que terminó con Duarte arrestado y desterrado a Venezuela, donde vivió hasta 1979.

Lo de 1972 no fue un caso aislado. Las elecciones de 1977 también estuvieron marcadas por denuncias de fraude y, según los estudios de país de la Biblioteca del Congreso de Estados Unidos, esa votación se manipuló de forma aún más descarada. A lo largo de los setenta crecieron la represión y la frustración de una oposición que veía cerrada la vía electoral.
""")

E("sv-a005", "P03", "contexto", "Hazme el cuento de cómo se llegó al golpe de 1979.",
  [[L("P03", ["FR-P03-003", "FR-P03-004", "FR-P03-005", "FR-P03-006"])]],
  """
Te lo cuento en orden.

Durante los años setenta la vía electoral se fue cerrando. Las elecciones de 1972 y de 1977 quedaron marcadas por denuncias de fraude, y en ese clima crecieron tanto la represión como la frustración de la oposición.

Hacia 1979 ya operaban en El Salvador varias organizaciones guerrilleras, cada una por su lado. En octubre de 1979 un golpe militar sacó del poder al general Carlos Humberto Romero.

Según la biografía de Napoleón Duarte que publica el CIDOB, el poder pasó a una Junta Revolucionaria de Gobierno de cinco miembros: dos coroneles, Adolfo Majano y Jaime Abdul Gutiérrez, y tres civiles, entre ellos Guillermo Manuel Ungo. Era un intento de cambiar desde dentro un sistema que parecía a punto de estallar.

De acuerdo con el California Migration Project, esa junta intentó algunas reformas agrarias y nacionalizó el comercio del café. Al mismo tiempo, Estados Unidos, que veía a Cuba y a Nicaragua gobernadas por revoluciones, quería impedir que la revolución llegara a El Salvador.

Ese es el punto de partida de la guerra civil: un gobierno que prometía reformas, unas guerrillas que se estaban organizando y dos potencias de la Guerra Fría que miraban el país con mucho interés.
""")

E("sv-a006", "P04", "hecho", "¿Qué fue la Conferencia Tricontinental?",
  [[B("Conferencia Tricontinental La Habana OLAS", ["FR-P04-001", "FR-P04-002"], epoca="P04")]],
  """
La Tricontinental fue una gran conferencia que La Habana organizó a mediados de los años sesenta para reunir a los movimientos revolucionarios y anticoloniales del llamado Tercer Mundo.

Se celebró del 3 al 15 de enero de 1966 y reunió a 512 delegados de 82 países de Asia, África y América Latina. De ella salió la Organización de Solidaridad de los Pueblos de Asia, África y América Latina, conocida como OSPAAAL, y la conferencia declaró su apoyo a la lucha armada.

Al año siguiente, en 1967, Cuba convocó otra reunión centrada en el continente: la Organización Latinoamericana de Solidaridad, la OLAS. Según el sociólogo Emir Sader, la OLAS optó abiertamente por la lucha armada y las guerrillas como camino.

Sader añade un matiz importante para El Salvador. Cuando la lucha armada se reanudó en la década siguiente, ya con el centro en Centroamérica, la OLAS se había convertido en un órgano de difusión sin capacidad real de coordinar a los movimientos. La coordinación pasó a otros canales, como el Departamento América del Partido Comunista de Cuba.
""")

E("sv-a007", "P04", "hecho", "¿Qué era el Departamento América de Cuba y quién lo dirigía?",
  [[B("Departamento América Manuel Piñeiro Barbarroja", ["FR-P04-003", "FR-P04-004", "FR-P05-005"])]],
  """
El Departamento América era una oficina del Comité Central del Partido Comunista de Cuba dedicada a la relación con los movimientos revolucionarios del continente.

Según un estudio publicado en la revista EIAL, funcionó como el aparato de enlace de Cuba con las guerrillas de América Latina y el Caribe y, con el tiempo, también representó al Partido en la diplomacia cubana. Es decir, era a la vez un canal político y una herramienta de política exterior.

Lo dirigía Manuel Piñeiro, conocido como Barbarroja, que se encargaba de centralizar el control y la ayuda a los grupos insurgentes de la región. Sobre la fecha en que tomó el mando hay una pequeña diferencia entre fuentes: el diario colombiano El Tiempo la sitúa en 1974, y una entrevista recogida por Archivo Chile habla de 1975.

Para El Salvador, esta oficina importa porque fue una de las vías por las que los dirigentes guerrilleros llegaban a Fidel Castro. Así lo contaron excomandantes como Joaquín Villalobos, Eduardo Sancho y Claudio Armijo en entrevistas para la revista Cold War History.
""")

E("sv-a008", "P05", "perspectivas", "¿Fue Cuba la que creó y armó al FMLN?",
  [[B("papel de Cuba en la creación del FMLN", ["FR-P05-001", "FR-P05-003", "FR-P05-004", "FR-P05-005", "FR-P05-006"], epoca="P05")]],
  """
Cuba tuvo un papel importante en la unificación del FMLN, y eso está bastante documentado. Decir que lo creó sola ya es una interpretación, y aquí las fuentes no coinciden del todo.

Según un despacho de AFP publicado por T13, Fidel Castro, animado por el triunfo sandinista de julio de 1979, apoyó con decisión a una guerrilla salvadoreña que entonces estaba dispersa. Las cinco organizaciones fundaron el FMLN en La Habana el 10 de octubre de 1980, y en noviembre de 1989 Castro respaldó la gran ofensiva guerrillera sobre San Salvador.

El gobierno de Estados Unidos fue más lejos. En el informe que su delegación presentó ante la Comisión de Derechos Humanos de la ONU, afirmó que Castro tuvo un papel tutelar directo para agrupar a las facciones y que Cuba asesoró la planificación militar. Un memorando de la CIA ya desclasificado decía lo mismo sobre su papel personal.

Los propios excomandantes, en entrevistas para la revista Cold War History, cuentan que veían a Cuba como la prueba de que el cambio era posible y que el Departamento América era la vía para llegar a Castro.

Pero las organizaciones guerrilleras, en su manifiesto de 1980, sostenían que su lucha tenía raíces propias, desde la oposición a los gobiernos de la familia Meléndez-Quiñónez hasta Farabundo Martí. Lo más preciso es decir que Cuba impulsó y facilitó la unión de movimientos que ya existían.
""")

E("sv-a009", "P05", "hecho", "¿Qué organizaciones formaron el FMLN?",
  [[B("organizaciones fundadoras FMLN", ["FR-P05-002", "FR-P02-006"], epoca="P05")]],
  """
El FMLN nació como una coalición de cinco organizaciones de izquierda que hasta entonces actuaban por separado.

Se formó el 10 de octubre de 1980 y lo integraron las Fuerzas Populares de Liberación (FPL), el Ejército Revolucionario del Pueblo (ERP), la Resistencia Nacional (RN), el Partido Comunista Salvadoreño (PCS) y el Partido Revolucionario de los Trabajadores Centroamericanos (PRTC). Este último fue el que se sumó más tarde, el 5 de diciembre de 1980.

Cada grupo tenía su historia, su línea y sus dirigentes, y no siempre se llevaban bien. Por eso la unificación fue un paso importante: les permitió coordinar las operaciones militares y presentarse como un solo frente ante el gobierno y ante la comunidad internacional.

El nombre se tomó de Farabundo Martí, el dirigente comunista fusilado tras el levantamiento de 1932, para conectar la nueva coalición con esa tradición. Si quieres, te busco cómo influyó Cuba en esa unificación, que es un tema con versiones distintas.
""")

E("sv-a010", "T04", "multiple", "¿La Revolución Cubana tiene algo que ver con las pandillas de El Salvador? Yo creo que hay una relación.",
  [[B("expansión de la Revolución Cubana y guerrillas centroamericanas", ["FR-P04-002", "FR-P05-001"]),
    B("origen de la MS-13 en Los Ángeles", ["FR-E02-001", "FR-E02-003"])],
   [B("diáspora salvadoreña y guerras civiles", ["FR-T04-001"], epoca="T04")]],
  """
Hay una relación, pero es indirecta: pasa por la guerra civil y por la emigración. Te la explico como una cadena, con lo que dicen las fuentes en cada eslabón.

Primer eslabón: Cuba y la guerrilla. Según el sociólogo Emir Sader, Cuba apostó en los sesenta por la lucha armada como camino para América Latina. Según un despacho de AFP, tras el triunfo sandinista de 1979 Fidel Castro apoyó con decisión a la guerrilla salvadoreña, que fundó el FMLN en La Habana en 1980, y en 1989 respaldó su gran ofensiva.

Segundo eslabón: la guerra produjo un éxodo. Según el Migration Policy Institute, la evolución de la MS-13 y del Barrio 18 hacia organizaciones transnacionales está ligada a la diáspora salvadoreña, que a su vez es producto de las guerras civiles centroamericanas.

Tercer eslabón: las pandillas nacen fuera. La MS-13 surgió en Los Ángeles en los años ochenta, formada por jóvenes que habían huido de la guerra o eran hijos de refugiados, para protegerse de otras pandillas.

Cuarto eslabón: vuelven deportadas. Las deportaciones desde Estados Unidos se triplicaron a finales de los noventa y llevaron la MS-13 a Centroamérica.

Así que el impulso cubano a la guerrilla es un factor real dentro de la cadena. Lo que no sostienen las fuentes es que Cuba creara las pandillas: estas nacen en las calles de Los Ángeles y se expanden con la política de deportaciones de Estados Unidos.
""")

E("sv-a011", "E01", "hecho", "¿Cómo mataron a monseñor Romero?",
  [[B("asesinato monseñor Óscar Romero", ["FR-E01-001", "FR-E01-002"], epoca="E01")]],
  """
Monseñor Óscar Arnulfo Romero, arzobispo de San Salvador, fue asesinado de un disparo el 24 de marzo de 1980 mientras celebraba misa en la capilla de un hospital de la capital. Fue uno de los hechos que marcaron el paso de la crisis política a la guerra abierta.

Romero se había convertido en una de las voces más fuertes contra la violencia que vivía el país. Según el Zinn Education Project, en febrero de 1980, apenas unas semanas antes de su muerte, escribió al presidente de Estados Unidos, Jimmy Carter, para pedirle que detuviera la ayuda militar al gobierno salvadoreño. Para muchos salvadoreños esa carta resume el papel que había asumido: hablar en nombre de las víctimas cuando pocas instituciones lo hacían.

Si te interesa saber quién estuvo detrás del crimen o qué dijo después la Comisión de la Verdad sobre la violencia de esos años, puedo buscarlo; prefiero no darte nombres sin tener el documento delante.
""")

E("sv-a012", "E01", "hecho", "¿Qué pasó en El Mozote?",
  [[B("masacre de El Mozote 1981", ["FR-E01-003", "FR-E01-005"], epoca="E01")]],
  """
El Mozote es el nombre de la peor masacre de civiles de la guerra salvadoreña, y por eso aparece en casi cualquier historia de ese periodo.

Según Wikipedia, el 11 de diciembre de 1981, en El Mozote y en los caseríos vecinos del departamento de Morazán, el ejército salvadoreño mató a más de 800 civiles. La operación la hicieron unidades del Batallón Atlacatl, una unidad de reacción rápida creada en 1980 para combatir a la guerrilla en el oriente del país.

El caso es un ejemplo de lo que encontró después la Comisión de la Verdad de la ONU. Según un análisis académico de la Universidad Federal de Pelotas, ese informe atribuyó al ejército y a grupos paramilitares el 85 % de las violaciones que documentó, y responsabilizó al FMLN de una parte menor.

Si necesitas el detalle de las investigaciones judiciales posteriores, puedo buscarlo, pero no lo tengo en estos fragmentos.
""")

E("sv-a013", "E01", "hecho", "¿Qué fue la Comisión de la Verdad y qué concluyó?",
  [[B("Comisión de la Verdad El Salvador informe", ["FR-E01-004", "FR-E01-005", "FR-E01-006"], epoca="E01")]],
  """
La Comisión de la Verdad fue el organismo que los Acuerdos de Paz crearon para investigar los crímenes más graves de la guerra.

Se constituyó el 15 de julio de 1992 con tres miembros nombrados por el secretario general de la ONU: el expresidente colombiano Belisario Betancur, el venezolano Reinaldo Figueredo y el jurista estadounidense Thomas Buergenthal. Su informe, titulado «De la locura a la esperanza», se hizo público el 15 de marzo de 1993.

Su conclusión más citada es la del reparto de responsabilidades. Según un análisis académico de la Universidad Federal de Pelotas, el informe atribuyó al ejército y a grupos paramilitares el 85 % de las violaciones que documentó, y responsabilizó al FMLN de una parte menor.

Lo que vino después también es parte de la historia. Según la Comisión Interamericana de Derechos Humanos, el 18 de marzo de 1993, tres días después de publicarse el informe, el presidente Alfredo Cristiani anunció una amnistía general que dejó sin castigo los crímenes cometidos por agentes del Estado entre 1980 y 1992.

Así que la Comisión dijo qué había pasado, pero la amnistía impidió durante años que esos casos llegaran a los tribunales.
""")

E("sv-a014", "E01", "hecho", "¿Cuándo y dónde se firmó la paz en El Salvador?",
  [[B("firma acuerdos de paz Chapultepec", ["FR-E01-007", "FR-E01-008"], epoca="E01")]],
  """
La paz se firmó el 16 de enero de 1992 en el castillo de Chapultepec, en Ciudad de México. Allí el gobierno del presidente Alfredo Cristiani y la comandancia del FMLN firmaron, con mediación de la ONU, los acuerdos que pusieron fin a doce años de guerra.

No fue algo de un día. Según El Diario de Hoy, el camino empezó con un primer acercamiento entre las partes en la iglesia de La Palma, en Chalatenango, el 15 de octubre de 1984, en plena guerra. Pasaron años de contactos y de rupturas hasta que el 4 de abril de 1990 se firmó en Ginebra el primer acuerdo, que sirvió de base para todo lo que se pactó en 1992.

De esos acuerdos salió también la Comisión de la Verdad, que investigó los peores crímenes del conflicto.

Para muchos salvadoreños es la fecha que separa la guerra de la posguerra. Si quieres, te busco qué pasó con la Comisión de la Verdad y la amnistía que vino después.
""")

E("sv-a015", "E01", "hecho", "¿Cuántos muertos dejó la guerra civil salvadoreña?",
  [[B("número de víctimas guerra civil El Salvador", ["FR-E01-009", "FR-E01-005"])]],
  """
La cifra que más se repite es la de unos 75.000 muertos, pero no hay un número único y las fuentes dan detalles distintos sobre desaparecidos y presos.

Un despacho de la agencia EFE habla de más de 75.000 muertos y 7.000 desaparecidos. La Voz de América da 75.000 muertos, 8.000 desaparecidos y 12.000 presos. Las diferencias no son enormes, pero muestran que se trata de estimaciones y no de un recuento cerrado.

Más allá del número, la pregunta de quién causó esas muertes también tiene una respuesta documentada. Según un análisis académico de la Universidad Federal de Pelotas, el informe de la Comisión de la Verdad de la ONU atribuyó al ejército y a grupos paramilitares el 85 % de las violaciones que documentó, y al FMLN una parte menor.

Así que lo más honesto es decir que la guerra dejó en torno a 75.000 muertos y varios miles de desaparecidos, con cifras que cambian según quién las cuente. Si necesitas una fuente concreta para citar, dime para qué la quieres y te digo cuál encaja mejor.
""")

E("sv-a016", "E01", "hecho", "¿Cuánta plata le dio Estados Unidos al gobierno salvadoreño durante la guerra?",
  [[B("ayuda de Estados Unidos a El Salvador en la guerra", ["FR-E01-010", "FR-E01-002", "FR-P03-006"])]],
  """
Fue mucho dinero, pero el total depende de quién haga la cuenta y de qué años cuente.

El California Migration Project habla de más de 6.000 millones de dólares entre 1979 y 1991. Un estudio de la Universidad de El Salvador, más acotado, cuenta 3.348,5 millones de dólares de ayuda económica y militar entre 1980 y 1988, canalizados a través de la agencia de cooperación estadounidense AID. Y una nota de la revista ECA, de la UCA, señala que la cifra que más se repite en la prensa es la de 5.000 millones.

Las diferencias se explican en buena parte por los periodos que mide cada uno y por si se suma solo la ayuda militar o también la económica.

Lo que sí está claro es que la ayuda fue política desde el principio. Según el Zinn Education Project, en febrero de 1980 monseñor Romero escribió al presidente Carter para pedirle que la detuviera, porque consideraba que alimentaba la represión. Washington, en cambio, según el California Migration Project, buscaba impedir que la revolución que ya gobernaba Cuba y Nicaragua se extendiera por el continente.
""")

E("sv-a017", "E02", "hecho", "¿Dónde nació la MS-13?",
  [[B("origen de la Mara Salvatrucha MS-13", ["FR-E02-001", "FR-E02-004"], epoca="E02")]],
  """
Aunque mucha gente piensa que nació en El Salvador, la MS-13 nació en Estados Unidos.

La Mara Salvatrucha surgió en los años ochenta en el barrio de Pico-Union, en Los Ángeles. Al principio era un grupo para proteger a los inmigrantes salvadoreños de otras pandillas de la zona. La formaron jóvenes salvadoreños que habían huido de la guerra civil o que eran hijos de refugiados, y que se encontraron en barrios pobres donde las pandillas ya dominaban la calle.

Su gran rival, el Barrio 18, también tiene raíces en Los Ángeles. El ir y venir constante de gente entre esa ciudad y Centroamérica hizo que las dos se asentaran en El Salvador entre finales de los ochenta y principios de los noventa.

Así que la historia de la MS-13 es, en el fondo, una historia de migración: nace de los refugiados de una guerra, crece en las calles de una ciudad estadounidense y vuelve a El Salvador con los años. Si quieres, te busco cómo influyeron las deportaciones de los noventa en esa expansión, que fue el factor decisivo.
""")

E("sv-a018", "E02", "contexto", "Si las maras nacieron en Estados Unidos, ¿cómo llegaron a El Salvador?",
  [[B("deportaciones y expansión de las pandillas a Centroamérica", ["FR-E02-003", "FR-E02-002", "FR-E02-004"])]],
  """
Llegaron sobre todo por las deportaciones, aunque el movimiento de gente entre los dos países ya venía de antes.

Primero hay que entender quiénes estaban en Los Ángeles. Según el Migration Policy Institute, la diáspora salvadoreña en Estados Unidos es en gran parte producto de las guerras civiles centroamericanas, en las que Washington apoyó a los gobiernos que combatían a las guerrillas. En 2019 sumaba 1,4 millones de personas, y el grupo más grande vivía en Los Ángeles.

Desde finales de los ochenta, el ir y venir constante entre Los Ángeles y Centroamérica ya permitió que la MS-13 y el Barrio 18 empezaran a asentarse en El Salvador.

El salto grande vino en los noventa. Las deportaciones desde Estados Unidos se triplicaron a finales de esa década, con leyes de la época del presidente Clinton que facilitaron expulsar a inmigrantes con antecedentes penales. Muchos pandilleros deportados llegaron a un país que acababa de salir de la guerra, y allí abrieron nuevos grupos.

En esos años las pandillas pasaron de ser grupos juveniles a organizaciones carcelarias y transnacionales.
""")

E("sv-a019", "T02", "hecho", "¿Cómo se organizan las maras? ¿Qué es una clica?",
  [[B("estructura de las pandillas clicas programas ranfla", ["FR-T02-001", "FR-T02-002"], epoca="T02")]],
  """
Las maras no son un ejército con un jefe único: funcionan más bien como una red de células con cierta jerarquía.

La unidad básica es la clica. La MS-13 y el Barrio 18 se dividen en estas células, que tienen bastante autonomía para manejar sus propios negocios en su territorio. Varias clicas se agrupan en lo que llaman programas, y los programas responden a una dirección superior que se conoce como la ranfla. La extorsión es una de sus fuentes de dinero más importantes, y en general se considera que la MS-13 es la más sofisticada de las dos.

El Barrio 18, además, no es una sola organización. Según InSight Crime, hacia 2005 las peleas internas lo partieron en El Salvador en dos facciones rivales, los Revolucionarios y los Sureños, que desde entonces también se enfrentan entre sí, además de pelear con la MS-13.

El Estado salvadoreño declaró al Barrio 18 organización terrorista el 24 de agosto de 2015.
""")

E("sv-a020", "E03", "hecho", "¿Qué fue el plan Mano Dura?",
  [[B("plan Mano Dura Francisco Flores 2003", ["FR-E03-001", "FR-E03-002", "FR-E03-003", "FR-E03-006"], epoca="E03")]],
  """
El plan Mano Dura fue la primera gran ofensiva del Estado salvadoreño contra las pandillas, y abrió una forma de hacer política que se repitió durante años.

Lo lanzó a mediados de 2003 el presidente Francisco Flores, de ARENA, y lo presentó en cadena nacional el 23 de julio de 2003. Consistía en capturas sistemáticas de pandilleros y en sacar a la Fuerza Armada a apoyar a la Policía en las calles.

Según InSight Crime, la Ley Antimaras que lo respaldaba entró en vigor el 10 de octubre de 2003. Los resultados judiciales fueron pobres: según la Policía, el plan dejó 19.275 arrestos entre julio de 2003 y agosto de 2004, y 17.540 de esos detenidos quedaron libres por falta de pruebas.

Políticamente, en cambio, funcionó. InSight Crime sostiene que a quienes sufrían a las pandillas no les importó que la ley fuera inconstitucional, y que el plan reanimó al presidente y a su partido.

A largo plazo tuvo un efecto que nadie buscaba. Según el Migration Policy Institute, la Mano Dura arrestó a más de 30.000 supuestos pandilleros entre 2003 y 2005 y convirtió las cárceles en centros de reclutamiento de las pandillas.
""")

E("sv-a021", "E03", "conflicto", "¿Funcionó la Mano Dura o no?",
  [[B("resultados del plan Mano Dura homicidios", ["FR-E03-005", "FR-E03-006", "FR-E03-007", "FR-E03-002"], epoca="E03")]],
  """
Depende de qué se mida, y las fuentes no coinciden ni siquiera en las cifras de homicidios.

Los que la defendían la daban por buena. Según Infobae, el presidente Antonio Saca afirmó en 2004 que, si lanzaba el Súper Mano Dura, era porque el Mano Dura había sido efectivo.

Las cifras cuentan otra cosa, aunque tampoco una sola. Con datos de la Policía citados por EFE, hubo 2.340 muertes violentas en 1999, 2.388 en 2003 y 2.933 en 2004, es decir, más homicidios después del plan. Wikipedia, en cambio, recoge un descenso del 14 % de los asesinatos en 2004, seguido de una subida hasta 64,7 por cada 100.000 habitantes en 2006. Con esas dos versiones, lo único seguro es que no hubo una baja duradera.

En la parte judicial el balance es pobre. Según la Policía, de 19.275 arrestos hechos entre 2003 y 2004, 17.540 detenidos quedaron libres por falta de pruebas.

Y hay un efecto de fondo que señala un estudio del Migration Policy Institute: al llenar las cárceles de pandilleros sin separarlos, la Mano Dura las convirtió en centros de reclutamiento.
""")

E("sv-a022", "E03", "hecho", "¿Qué diferencia había entre la Mano Dura y la Súper Mano Dura?",
  [[B("Súper Mano Dura Antonio Saca 2004", ["FR-E03-004", "FR-E03-005", "FR-E03-001"], epoca="E03")]],
  """
La Súper Mano Dura fue la continuación del plan de Francisco Flores bajo su sucesor, Antonio Saca, también de ARENA, con más capturas y con una parte nueva de prevención.

La Mano Dura original la lanzó Flores a mediados de 2003: capturas sistemáticas de pandilleros y la Fuerza Armada apoyando a la Policía en las calles. Saca asumió en 2004 y el 30 de agosto de ese año, a los 60 días de llegar al poder, presentó la Súper Mano Dura para aumentar todavía más las capturas.

La diferencia principal es que Saca la acompañó de dos programas que su antecesor no tenía: Mano Amiga y Mano Extendida, pensados para la prevención y la reinserción de jóvenes en riesgo.

En el discurso, Saca presentó su plan como prueba de que el anterior había funcionado. Según Infobae, afirmó que, si lanzaba el Súper Mano Dura, era porque el Mano Dura había sido efectivo. Los resultados de los dos planes, sin embargo, siguen discutiéndose, sobre todo por las cifras de homicidios de esos años y por el efecto que tuvieron en las cárceles.
""")

E("sv-a023", "E04", "hecho", "¿Qué fue la tregua entre pandillas de 2012?",
  [[B("tregua entre pandillas 2012", ["FR-E04-001", "FR-E04-002", "FR-E04-004", "FR-E04-005"], epoca="E04")]],
  """
La tregua fue un acuerdo para bajar los homicidios en el que participaron las pandillas, mediadores y funcionarios del gobierno de Mauricio Funes, y todavía hoy es uno de los temas más polémicos del país.

Duró del 9 de marzo de 2012 al 26 de mayo de 2014. Sus principales negociadores fueron el ministro de Seguridad, David Munguía Payés, el exdiputado y exguerrillero Raúl Mijango y el obispo Fabio Colindres, bajo la supervisión del presidente Funes.

Se hizo pública casi por accidente. El 14 de marzo de 2012 el periódico El Faro informó del traslado de 30 líderes pandilleros de la cárcel de máxima seguridad a otros penales y dijo que respondía a una negociación con las pandillas. Las autoridades dieron explicaciones contradictorias, pero los homicidios cayeron un 53 % a partir de ese traslado.

Según Nueva Sociedad, el 14 de abril de 2012 Funes anunció en la Cumbre de las Américas el primer día sin homicidios en casi tres años. Y según El Diario NY, entre marzo y diciembre de 2011 hubo 3.697 homicidios, frente a 1.761 en el mismo periodo de 2012.

La tregua bajó las muertes, pero a costa de negociar con las pandillas, y cuando se rompió la violencia volvió con más fuerza.
""")

E("sv-a024", "E04", "hecho", "¿Condenaron a alguien por la tregua?",
  [[B("juicio condena tregua Funes Munguía Payés", ["FR-E04-006", "FR-E04-007"], epoca="E04")]],
  """
Sí. Años después, la tregua terminó en los tribunales.

En 2023 un tribunal de San Salvador condenó al exministro de Seguridad David Munguía Payés a 18 años de cárcel y al expresidente Mauricio Funes, que fue juzgado en ausencia, a 14 años, por la tregua de 2012. Los delitos fueron agrupaciones ilícitas e incumplimiento de deberes. El mediador Raúl Mijango, en cambio, fue absuelto dos veces, en 2017 y en 2019.

La acusación de la Fiscalía fue dura. Según la Voz de América, sostuvo que Munguía Payés fue el autor intelectual de una tregua cuya ruptura convirtió a El Salvador en 2015 en el país más violento del mundo, y que Funes aprobó el acuerdo y dispuso dinero público para el proceso.

Lo que la sentencia establece es la responsabilidad penal según ese tribunal; el debate político sobre si la tregua fue una política de seguridad o un pacto con criminales sigue abierto.
""")

E("sv-a025", "E04", "perspectivas", "¿La tregua fue idea del gobierno de Funes o de las pandillas?",
  [[B("quién impulsó la tregua de 2012", ["FR-E04-001", "FR-E04-002", "FR-E04-003", "FR-E04-007"], epoca="E04")]],
  """
Las versiones han cambiado con los años, y eso es parte de lo que la hace tan polémica.

Al principio, el gobierno no reconocía ninguna negociación. Cuando El Faro informó en marzo de 2012 del traslado de 30 líderes pandilleros y lo atribuyó a un acuerdo con el gobierno, las autoridades dieron explicaciones contradictorias.

Con el tiempo, los propios protagonistas contaron más. Los principales negociadores fueron el ministro David Munguía Payés, el exdiputado Raúl Mijango y el obispo Fabio Colindres, con la supervisión del presidente Mauricio Funes. Según un estudio publicado en Nueva Sociedad, el ministro venía afirmando que la guerra entre pandillas causaba el 90 % de los homicidios, y según la misma publicación dijo después que quien controlara esa guerra iba a controlar el 75 % de las muertes del país. Es decir, la veía como una estrategia de seguridad pensada desde el gobierno.

La Fiscalía salvadoreña lo planteó de forma más grave. Según la Voz de América, sostuvo que Munguía Payés fue el autor intelectual de la tregua y que Funes la aprobó y puso dinero público.

Lo que las fuentes muestran, por tanto, es que el gobierno de Funes tuvo un papel activo y que las pandillas aceptaron negociar. Quién la propuso primero no está del todo claro en estos documentos.
""")

E("sv-a026", "E05", "contexto", "¿Por qué el 2015 fue tan violento en El Salvador?",
  [[B("violencia récord 2015 causas", ["FR-E05-001", "FR-E05-002", "FR-E04-007", "FR-E04-001"], epoca="E05")]],
  """
2015 fue el año más violento de la historia reciente de El Salvador, y no tuvo una sola causa.

Las cifras impresionan. Según las estadísticas oficiales, hubo al menos 6.657 homicidios, con una tasa de unos 103 por cada 100.000 habitantes, la más alta de la historia del país. Ese año El Salvador fue el país más violento del hemisferio occidental.

Sobre las causas, InSight Crime habla de una combinación de factores: la fragmentación de las pandillas, los choques internos dentro de ellas y la aparición de grupos de justicia por mano propia. Cuando una estructura se parte, sus pedazos pelean por el territorio y por el dinero de la extorsión, y eso multiplica las muertes.

Hay otra explicación que mira a la política. Según la Voz de América, la Fiscalía salvadoreña sostuvo que la ruptura de la tregua entre pandillas de 2012, de la que acusó al exministro David Munguía Payés, fue lo que convirtió a El Salvador en 2015 en el país más violento del mundo.

Las dos lecturas pueden ser compatibles: el fin de la tregua dejó a pandillas divididas y en guerra.
""")

E("sv-a027", "E05", "hecho", "¿Los homicidios ya venían bajando antes de que llegara Bukele?",
  [[C("homicidios", [("2015", "6.657 homicidios; 103 por cada 100.000", "estadísticas oficiales", "FR-E05-001"),
                     ("2016", "81 por cada 100.000", "fuentes oficiales citadas por AFP", "FR-E05-003"),
                     ("2017", "60 por cada 100.000", "fuentes oficiales citadas por AFP", "FR-E05-003"),
                     ("2018", "51 por cada 100.000; 3.340 asesinatos", "fuentes oficiales citadas por AFP", "FR-E05-003")],
      desde="2015", hasta="2018"),
    B("tendencia de homicidios antes de 2019", ["FR-E07-003"])]],
  """
Sí. Las cifras oficiales muestran que la caída empezó antes de su gobierno, aunque con Bukele se hizo mucho más pronunciada.

El punto más alto fue 2015, con al menos 6.657 homicidios y una tasa de unos 103 por cada 100.000 habitantes, según las estadísticas oficiales. A partir de ahí la tasa fue bajando año tras año: 81 por cada 100.000 habitantes en 2016, 60 en 2017 y 51 en 2018, año en que se registraron 3.340 asesinatos, siempre según fuentes oficiales citadas por AFP.

Un balance de EFE publicado por Primicias lo resume así: Bukele logró acentuar la disminución de los homicidios que había empezado en 2016. Esa misma fuente recoge que, según las autoridades, su gobierno quitó a las pandillas el control de los barrios populares.

Así que las dos cosas son ciertas a la vez. La tendencia a la baja ya existía cuando llegó Bukele, y durante su gobierno la caída fue mucho más fuerte. Cuánto se debe a cada política es justo lo que se discute: sus defensores lo atribuyen a su estrategia de seguridad y sus críticos recuerdan que la baja venía de antes. Si quieres, te busco las cifras de los años de su gobierno.
""")

E("sv-a028", "E05", "hecho", "¿Cuántos pandilleros había en El Salvador?",
  [[B("número de miembros de pandillas El Salvador", ["FR-E05-004"], epoca="E05")]],
  """
No hay un censo de pandilleros, así que cualquier número es una estimación, y la que tengo es la del propio gobierno de hace unos años.

Según El Heraldo, en 2018 las autoridades salvadoreñas calculaban que las pandillas tenían algo más de 70.000 miembros, de los cuales unos 17.000 estaban presos. En ese momento el gobierno les atribuía la mayor parte de los homicidios del país, y el ministro de Seguridad explicó la baja de las muertes de ese año por el combate contra la delincuencia y por programas de prevención y rehabilitación.

Hay que tomar esa cifra como lo que es: un cálculo oficial de una época concreta. Contar a los miembros de una organización clandestina es muy difícil, porque no todos tienen el mismo grado de pertenencia y muchos colaboradores no se consideran miembros.

Tampoco te puedo dar con este documento una cifra actual. Si quieres, busco las cifras más recientes de capturas, aclarando siempre quién las da y que una captura no equivale a ser miembro de una pandilla.
""")

guardar("ejemplos_lote_a.jsonl")
