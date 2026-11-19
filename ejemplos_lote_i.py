"""
ejemplos_lote_i.py — Ejemplos de entrenamiento, lote I: inglés, varios turnos, "no tengo ese dato",
comparaciones con la tabla de cifras y versiones enfrentadas de la historia.
Uso (desde E:\\vertex-salvador):  python ejemplos_lote_i.py  ->  datos\\ejemplos_lote_i.jsonl
"""
from ejemplos_base import B, C, D, E, L, guardar

# ---------------------------------------------------------------- inglés
E("sv-i001", "T01", "hecho", "Who is Nayib Bukele?",
  [[B("Nayib Bukele biography career", ["FR-T01-001", "FR-E06-001", "FR-E07-001", "FR-E12-001"], epoca="T01")]],
  """
Nayib Bukele is the president of El Salvador.

According to his Wikipedia biography, Nayib Armando Bukele Ortez was born on 24 July 1981 in San Salvador. He is the son of businessman Armando Bukele Kattán, who died in 2015, and Olga Marina Ortez. He studied at the Central American University (UCA) but did not finish his degree.

His political career went like this:
- In 2012, aged 31, he was elected mayor of Nuevo Cuscatlán, a small town next to San Salvador, as a member of the FMLN.
- In 2015 he won the mayoralty of San Salvador, also with the FMLN, and held it until 2018.
- On 3 February 2019 he won the presidency in the first round with 53 % of the valid vote, running for GANA.
- On 4 February 2024 he was re-elected with 2,701,725 votes, 84.65 % of the valid vote, and his party Nuevas Ideas won 54 of the 60 seats in the Assembly.

He is best known for his crackdown on the gangs under a state of exception, which made him very popular at home and drew strong criticism from human rights groups.

Would you like the security side, the re-election debate or the criticism?
""", idioma="en")

E("sv-i002", "E02", "hecho", "Where did MS-13 come from?",
  [[B("MS-13 origin Los Angeles deportations", ["FR-E02-001", "FR-E02-003", "FR-E02-002"], epoca="E02")]],
  """
MS-13 was born in the United States, not in El Salvador.

The Mara Salvatrucha (MS-13) emerged in the eighties in the Pico-Union neighbourhood of Los Angeles. It was formed by young Salvadorans who had fled the civil war or were children of refugees, initially to protect themselves from other gangs in the area.

Why were there so many Salvadorans in Los Angeles? According to the Migration Policy Institute, the Salvadoran diaspora in the US is largely a product of the Central American civil wars, in which Washington backed the governments fighting the guerrillas. In 2019 it numbered 1.4 million people, with the largest group living in Los Angeles.

Then came the deportations. They tripled in the late nineties and took MS-13 to Central America, where deported members started new groups. Those deportations were made possible by laws from the Clinton era that targeted immigrants with criminal records. In that decade the gang went from a youth gang to a prison gang and then a transnational organisation.

So the story is a chain: war, exile, street gangs in Los Angeles, and deportations back home.
""", idioma="en")

E("sv-i003", "E11", "conflicto", "Is the drop in homicides in El Salvador real?",
  [[C("homicidios", [("2015", "6.657 homicidios; 103 por cada 100.000", "estadísticas oficiales", "FR-E05-001"),
                     ("2021", "1.211", "cifras oficiales", "FR-E11-004"),
                     ("2025", "82", "cifras oficiales", "FR-E11-004")])],
   [B("homicide figures criticism official data", ["FR-E11-006", "FR-E14-008"])]],
  """
The drop is huge according to official figures, and nobody seriously disputes that violence fell. What is debated is how it is counted and what caused it.

The official numbers: in 2015 there were at least 6,657 homicides, a rate of about 103 per 100,000 people, the highest in the country's history. According to official figures cited by Diario El Mundo, there were 1,211 homicides in 2021 and 82 in 2025.

The government's view: according to EFE, Bukele and his security cabinet say the state of exception allowed them to fight the gangs, free territory they controlled and sharply reduce homicides. EFE adds that El Salvador had already seen steady declines since 2016.

The caveat from civil society: deaths in custody are not part of those homicide series. Civil organisations count them separately and do not agree with each other: Socorro Jurídico Humanitario records 530 deaths, and another group cited by the Tico Times counts at least 500. The government publishes no figure of its own.

So the fair answer: the fall is real and very large; official figures come from the government itself; and some deaths linked to the crackdown are tracked only by NGOs.
""", idioma="en")

E("sv-i004", "E01", "hecho", "How did the Salvadoran civil war end?",
  [[B("peace accords Chapultepec 1992 Truth Commission", ["FR-E01-007", "FR-E01-008", "FR-E01-004", "FR-E07-001"], epoca="E01")]],
  """
It ended with a negotiated peace, after a long process.

According to El Diario de Hoy, the path to peace began with a first meeting at the church of La Palma, Chalatenango, on 15 October 1984. The first formal agreement, signed in Geneva on 4 April 1990, laid the groundwork for the final accords.

On 16 January 1992, at Chapultepec Castle in Mexico City, the government of Alfredo Cristiani and the FMLN leadership signed, with UN mediation, the peace accords that ended twelve years of war.

The accords also set up a Truth Commission. It was established on 15 July 1992, with three members appointed by the UN Secretary-General: Belisario Betancur, Reinaldo Figueredo and Thomas Buergenthal. Its report, "From Madness to Hope", was made public on 15 March 1993.

After the accords, the FMLN laid down its weapons and became a political party, alternating in power with ARENA for decades, until Bukele broke that pattern in 2019.

Would you like to know what the Truth Commission concluded?
""", idioma="en")

E("sv-i005", "E15", "sin_datos", "Have the four Salvadoran soldiers in Haiti been found?",
  [[B("four Salvadoran soldiers Haiti found", ["FR-E15-022"], epoca="E15")]],
  """
Not as of my latest data. On 18 November 2026, one month after the ambush, authorities had not confirmed either the whereabouts or the condition of the four aviation technicians. On 10 November Vice President Félix Ulloa had said there was no trace of them.

Anything after that date I don't have. For updates, check the Salvadoran armed forces' official channels or current news.
""", idioma="en")

E("sv-i006", "E14", "perspectivas", "What do human rights groups say about Bukele?",
  [[B("human rights groups criticism Bukele 2026", ["FR-E14-010", "FR-E14-006", "FR-E14-009"], epoca="E14")]],
  """
They are highly critical, and the government rejects their criticism. Here are both sides.

According to Human Rights Watch's World Report 2026, Bukele's government kept dismantling checks on executive power and stepped up repression against human rights defenders, journalists, activists and trade unionists.

According to a report Cristosal presented in Guatemala in March 2026, the government holds at least 86 political prisoners, mostly human rights defenders, journalists, judicial officials, trade unionists and environmentalists. Cristosal also says thousands of innocent people were caught up in the mass arrests.

The government's response has been blunt. According to the Tico Times, in March 2026 Bukele accused human rights organisations of acting as law firms for criminals and said his government will never heed their criticism.

It's worth keeping in mind who is speaking. These organisations document cases and publish reports, but they are also parties in a political conflict with the government. And the government, for its part, does not publish its own figures on things like deaths in custody, which makes independent checking harder.

If you'd like, I can look up the official figures the government uses to defend its record.
""", idioma="en")

# ---------------------------------------------------------------- varios turnos
E("sv-i007", "E15", "hecho", "¿Qué pasó el 18 de octubre en Haití?",
  [[B("18 de octubre 2026 emboscada Haití", ["FR-E15-007"], epoca="E15")]],
  """
El domingo 18 de octubre de 2026 hubo una emboscada contra militares salvadoreños en Haití.

Cuatro aerotécnicos de la Fuerza de Tarea Libertad II, que formaban parte de la Fuerza de Supresión de Pandillas respaldada por la ONU, fueron atacados por grupos armados en Santo, una localidad de Croix-des-Bouquets, a unos 12 kilómetros de Puerto Príncipe.

Según la Fuerza Armada salvadoreña, regresaban a su campamento después de comprar alimentos. Salieron del vehículo blindado en el que viajaban, que fue incendiado, y se perdió el contacto con ellos.

Eran técnicos de aviación, no tropas de combate: su función tenía que ver con el apoyo aéreo de la misión.

Esa emboscada cambió el papel de El Salvador en Haití. Hasta entonces su presencia era pequeña y dentro de la fuerza internacional; a partir de ahí, el gobierno de Bukele lanzó un despliegue de una escala muy distinta.

¿Quieres que te cuente qué hizo El Salvador después?
""",
  seguimiento=[("Sí, ¿qué hizo?",
                [[B("respuesta El Salvador despliegue tras emboscada", ["FR-E15-008", "FR-E15-012", "FR-E15-017"], epoca="E15")]],
                """
Mandó un contingente enorme para buscarlos.

A finales de octubre de 2026 El Salvador envió a Haití más de 2.000 militares, con blindados y helicópteros. Los primeros refuerzos llegaron a Puerto Príncipe el 22 de octubre y el 28 de octubre la Cancillería confirmó que el contingente superaba los 2.000 efectivos.

Bukele explicó el objetivo. Según Diario El Mundo, dijo el 29 de octubre: "Esto no es una operación contra el pueblo haitiano, ni una invasión al país de Haití". Afirmó que lo principal es que los cuatro técnicos vuelvan a El Salvador y que su gobierno cubre el 90 % de los gastos.

La ONU puso un matiz importante. El 2 de noviembre aclaró que la gran mayoría de esos militares adicionales no forma parte de la Fuerza de Supresión de Pandillas, así que quedan fuera de sus mecanismos de supervisión. Recordó que toda operación debe respetar el derecho internacional de los derechos humanos y el derecho internacional humanitario.

Es decir, una parte de la presencia salvadoreña está bajo la ONU y la mayor parte del refuerzo responde directamente al gobierno de Bukele, con el acuerdo del gobierno haitiano.
""")])

E("sv-i008", "P03", "hecho", "¿Qué pasó en El Salvador en 1979?",
  [[B("1979 golpe militar general Romero junta", ["FR-P03-004", "FR-P03-005"], epoca="P03")]],
  """
1979 fue el año del golpe que abrió la puerta a la guerra.

En octubre de 1979 un golpe militar sacó del poder al general Carlos Humberto Romero. Según la biografía del CIDOB, tomó el poder una Junta Revolucionaria de Gobierno de cinco miembros: dos coroneles, Adolfo Majano y Jaime Abdul Gutiérrez, y tres civiles, entre ellos Guillermo Manuel Ungo.

El contexto era explosivo. Hacia 1979 operaban en El Salvador varias organizaciones guerrilleras separadas, y venían de una década de elecciones con denuncias de fraude y de represión creciente.

Y en la región todo se movía: en julio de 1979 los sandinistas habían tomado el poder en Nicaragua, lo que tanto Estados Unidos como Cuba vieron como una señal de lo que podía pasar en El Salvador.

La junta no logró detener la espiral. Al año siguiente asesinaron a monseñor Romero y las guerrillas se unieron en el FMLN.

¿Quieres saber qué intentó hacer la junta y cómo lo veía Estados Unidos?
""",
  seguimiento=[("Sí, ¿y Estados Unidos qué hizo?",
                [[B("junta 1979 reformas Estados Unidos impedir revolución", ["FR-P03-006", "FR-E01-010"])]],
                """
Apostó por la junta como forma de frenar la revolución.

Según el California Migration Project, la junta que sustituyó al general Romero en 1979 intentó algunas reformas agrarias y nacionalizó el comercio del café. Al mismo tiempo, Estados Unidos, con Cuba y Nicaragua ya gobernadas por revoluciones, buscaba impedir que la revolución se extendiera por el continente.

La lógica de Washington era que las reformas le quitaran apoyo a la guerrilla, mientras el ejército la combatía. De ahí salió una relación que duró toda la guerra: Estados Unidos se convirtió en el gran sostén del gobierno salvadoreño.

Cuánto dinero puso no tiene una cifra única. El California Migration Project da más de 6.000 millones de dólares entre 1979 y 1991. Un estudio de la Universidad de El Salvador cuenta 3.348,5 millones de dólares de ayuda económica y militar entre 1980 y 1988, a través de la AID. Y según la revista ECA, la cifra más repetida es de 5.000 millones.

Para sus defensores, esa ayuda evitó que El Salvador terminara como Cuba. Para sus críticos, financió a un ejército que, según la Comisión de la Verdad, cometió la gran mayoría de las violaciones de la guerra.
""")])

E("sv-i009", "E11", "hecho", "¿Cuántos homicidios hubo en 2023?",
  [[C("homicidios", [("2023", "194", "cifras oficiales", "FR-E11-004")], desde="2023", hasta="2023")]],
  """
Según las cifras oficiales de violencia citadas por Diario El Mundo, en 2023 hubo 194 homicidios en El Salvador.

Para que veas la tendencia, la misma fuente da 1.211 en 2021, 615 en 2022, el año en que empezó el régimen de excepción, 194 en 2023, 114 en 2024 y 82 en 2025. Es decir, en dos años se pasó de más de mil a menos de doscientos.

Te lo doy atribuido porque son cifras oficiales, del propio gobierno. No tengo en mis documentos una serie independiente para ese año con la que compararlas, así que no puedo decirte si otras organizaciones cuentan un número distinto. Lo que sí es claro es que la tendencia de bajada se mantiene en todos los años de la serie.

Si quieres, te doy también la cifra de detenidos del régimen de excepción de ese mismo periodo, o los años anteriores para ver de dónde venía el país.
""",
  seguimiento=[("¿Y comparado con 2015?",
                [[C("homicidios", [("2015", "6.657 homicidios; 103 por cada 100.000", "estadísticas oficiales", "FR-E05-001")], desde="2015", hasta="2015")],
                 [B("Plan Control Territorial 2019", ["FR-E07-002"], epoca="E07")]],
                """
La diferencia es enorme.

Según las estadísticas oficiales, en 2015 hubo al menos 6.657 homicidios, con una tasa de unos 103 por cada 100.000 habitantes, la más alta de la historia del país. Ese año El Salvador fue el país más violento del hemisferio occidental.

En 2023, según las cifras oficiales citadas por Diario El Mundo, hubo 194.

Es decir, en 2023 hubo muy pocos homicidios en comparación con 2015: por cada asesinato de 2023 hubo más de treinta en aquel año. No te doy una tasa por 100.000 para 2023 porque no la tengo en mis documentos y no quiero calcularla con una población que no aparece en las fuentes.

Hay que recordar que entre esos dos años pasaron muchas cosas: la baja empezó después de 2015, siguió con el Plan Control Territorial de 2019 y se aceleró con el régimen de excepción de 2022. Cuánto le toca a cada etapa es justo lo que se debate.
""")])

# ---------------------------------------------------------------- no tengo ese dato
E("sv-i010", "general", "sin_datos", "¿Cuánto gana Bukele de sueldo?",
  [[B("salario presidente Bukele", [])]],
  """
No tengo ese dato. En mis documentos no hay información sobre el salario del presidente, y no te voy a dar una cifra de memoria.

Lo más fiable sería buscar en el portal de transparencia del gobierno salvadoreño o en la Ley de Salarios del presupuesto nacional, donde suelen figurar las remuneraciones de los altos cargos.
""")

E("sv-i011", "general", "sin_datos", "¿Cuál es el PIB de El Salvador?",
  [[C("pib", [])],
   [B("PIB economía El Salvador", [])]],
  """
No tengo datos económicos como el PIB. Mi colección está centrada en historia, pandillas, seguridad y política, y la tabla de cifras no trae esa métrica.

Para el PIB lo mejor es el Banco Central de Reserva de El Salvador o bases internacionales como las del Banco Mundial o el FMI, que lo publican por año.
""")

E("sv-i012", "general", "sin_datos", "¿Cuántos salvadoreños viven en España?",
  [[B("salvadoreños en España diáspora", ["FR-E02-002"])]],
  """
No tengo ese dato. Lo único que tengo sobre la diáspora es que, según el Migration Policy Institute, la de Estados Unidos sumaba 1,4 millones de personas en 2019, pero sobre España no hay nada en mis documentos.

Para España, el Instituto Nacional de Estadística publica las cifras de residentes por nacionalidad.
""")

E("sv-i013", "E15", "sin_datos", "¿Cuántos pandilleros han matado los soldados salvadoreños en Haití?",
  [[B("pandilleros abatidos fuerzas salvadoreñas Haití cifra", ["FR-E15-019"], epoca="E15")]],
  """
No tengo ninguna cifra de pandilleros muertos en las operaciones salvadoreñas en Haití. Ni el gobierno salvadoreño ni el haitiano dan un número en mis documentos.

Lo único relacionado que encontré es una denuncia de UNA-Haití, que atribuye muertes de civiles a las fuerzas salvadoreñas desde el 22 de octubre de 2026, pero sin dar una cifra. Si sale un balance oficial o independiente, ahí estaría la respuesta.
""")

E("sv-i014", "P01", "sin_datos", "¿Qué pasó en El Salvador en la independencia de 1821?",
  [[B("independencia 1821 Centroamérica", ["FR-P01-001", "FR-P02-003"])]],
  """
No tengo documentos sobre la independencia. Mi colección empieza más tarde, con la Reforma Agraria Liberal de 1881-1882 y el problema de la tierra, así que no te puedo contar ese periodo con fuentes.

Si te sirve, te cuento cómo esa reforma de la tierra preparó el terreno para el levantamiento de 1932, que sí lo tengo bien documentado.
""")

# ---------------------------------------------------------------- versiones enfrentadas en la historia
E("sv-i015", "E01", "conflicto", "¿Quién cometió más crímenes en la guerra, el ejército o la guerrilla?",
  [[B("Comisión de la Verdad responsabilidad violaciones ejército FMLN", ["FR-E01-005", "FR-E01-003", "FR-E01-004"], epoca="E01")]],
  """
La fuente más importante para responder eso es el informe de la Comisión de la Verdad, y su conclusión fue clara.

La Comisión se constituyó el 15 de julio de 1992, en cumplimiento de los Acuerdos de Paz, con tres miembros nombrados por el secretario general de la ONU, y su informe, «De la locura a la esperanza», se hizo público el 15 de marzo de 1993.

Según un análisis académico de la Universidad Federal de Pelotas, el informe atribuyó al ejército y a grupos paramilitares el 85 % de las violaciones que documentó, y responsabilizó al FMLN de una parte menor.

El caso más grave es El Mozote: según Wikipedia, el 11 de diciembre de 1981 el ejército mató allí a más de 800 civiles, con unidades del Batallón Atlacatl.

Ahora, cada lado lo ha leído a su manera. Los sectores cercanos al ejército de entonces sostuvieron que el informe fue sesgado contra las fuerzas armadas. Exguerrilleros y organizaciones de víctimas lo consideran la base de cualquier verdad sobre la guerra. Y que el FMLN tenga una parte menor no quiere decir que no cometiera crímenes: también los cometió.

Lo que dicen los datos de la Comisión es que la gran mayoría de las violaciones fue obra del Estado.
""")

E("sv-i016", "P02", "perspectivas", "¿La rebelión de 1932 fue comunista o indígena?",
  [[B("rebelión 1932 comunistas indígenas causas", ["FR-P02-003", "FR-P02-004", "FR-P01-001"], epoca="P02")]],
  """
Fue las dos cosas, y el peso de cada una es lo que se discute.

Lo que comparten las fuentes: entre el 22 y el 25 de enero de 1932 hubo un levantamiento en el occidente del país encabezado por comunistas, con Farabundo Martí, y por indígenas, con Feliciano Ama. El gobierno del general Maximiliano Hernández Martínez lo aplastó.

La lectura que pone el acento en lo social: el agravio de fondo era la tierra. Según un texto académico de la colección de la UCA, la Reforma Agraria Liberal de 1881-1882 suprimió la propiedad comunal y muchos campesinos perdieron las tierras que trabajaban.

La lectura que combina las dos: según la Encyclopedia of Latin American History, la revuelta nació del enojo de los trabajadores del café y de los campesinos por sus condiciones de vida, y de la agitación de los dirigentes del Partido Comunista, en especial de Farabundo Martí.

Las autoridades de la época, con el general Hernández Martínez al frente, respondieron con una represión masiva contra las comunidades del occidente, lo que muestra que no distinguió entre dirigentes comunistas y campesinos. Las fuentes que tengo apoyan que hubo de las dos cosas a la vez.
""")

E("sv-i017", "E09", "perspectivas", "¿Bukele negoció con las pandillas?",
  [[B("acusaciones pacto gobierno Bukele pandillas", ["FR-E09-005", "FR-E10-003"]),
    B("respuesta gobierno niega pacto", ["FR-E09-006"])]],
  """
Hay acusaciones serias y una negativa rotunda. No hay una sentencia que lo confirme. Te pongo cada versión con su dueño.

Lo que dice Estados Unidos: según el Departamento del Tesoro, que el 8 de diciembre de 2021 sancionó a Osiris Luna, director de Centros Penales, y a Carlos Marroquín, director de Reconstrucción del Tejido Social, ambos dirigieron en 2020 reuniones promovidas por el gobierno de Bukele para pactar una tregua secreta con líderes pandilleros.

Lo que dice una investigación periodística: según El Faro, recogido por Telemundo, la ola de asesinatos de marzo de 2022 se desató por la supuesta ruptura de un pacto entre el gobierno y la MS-13.

Lo que dice el gobierno: según La Prensa de Panamá, el gobierno de Bukele niega haber pactado con las pandillas. Esa misma fuente recuerda que en 2021 se negó a extraditar a Estados Unidos a líderes de la MS-13 reclamados por la justicia de Nueva York, algo que los críticos relacionan con un posible acuerdo.

Entonces: hay una acusación de un gobierno extranjero y una investigación de prensa, frente a la negativa del gobierno. Si hubo o no pacto no está probado en un tribunal. Lo justo es decir que es una acusación grave, documentada por esas fuentes y negada por el gobierno.
""")

E("sv-i018", "E15", "perspectivas", "¿Qué piensan los haitianos de los soldados salvadoreños?",
  [[B("opinión haitianos tropas salvadoreñas gobierno diáspora", ["FR-E15-014", "FR-E15-019", "FR-E15-016", "FR-E15-021"], epoca="E15")]],
  """
No tengo encuestas de la población haitiana, así que no te puedo decir qué piensa la mayoría. Lo que sí tengo son las posiciones de distintos actores haitianos, y no coinciden.

El gobierno haitiano lo apoya. Según EFE, el 10 de noviembre de 2026 el primer ministro Alix Didier Fils-Aimé afirmó que su gobierno está recuperando el control territorial con el apoyo de las tropas salvadoreñas y de la Fuerza de Supresión de Pandillas, y escribió: "Haití, El Salvador, GSF: ¡el mismo combate, la misma determinación!". Y el 16 de noviembre, según Euronews, el ministro haitiano Patrick Pélissier dijo que Haití quiere que el despliegue continúe.

Una parte de la diáspora lo critica. Según la Revista E&N, UNA-Haití, un grupo que representa a sectores de la diáspora haitiana, denunció muertes de civiles que atribuye a bombardeos y ataques de las fuerzas salvadoreñas desde el 22 de octubre de 2026, sin dar una cifra, y pidió una investigación independiente de la ONU.

Hay que tener en cuenta un dato: el gobierno haitiano no fue elegido en las urnas, porque el país no tiene un gobierno electo desde 2016. Por eso su apoyo no se puede leer automáticamente como la voz de la población.

Si aparece una encuesta o un estudio sobre la opinión haitiana, esa sería la fuente para responderte bien.
""",
  )

# ---------------------------------------------------------------- comparaciones y tabla de cifras
E("sv-i019", "E12", "hecho", "Compara las dos elecciones de Bukele.",
  [[C("elecciones_presidenciales", [("2019", "Bukele 53 %", "Primicias / EFE", "FR-E07-001"),
                                    ("2024", "Bukele 84,65 % (2.701.725 votos)", "Tribunal Supremo Electoral", "FR-E12-001")])],
   [B("elecciones 2019 2024 contexto", ["FR-E07-001", "FR-E12-001", "FR-E09-004"])]],
  """
Entre una y otra cambió casi todo: el porcentaje, el partido y la discusión de fondo.

2019:
- Fue el 3 de febrero de 2019. Bukele ganó en primera vuelta con el 53 % de los votos válidos, como candidato de GANA.
- El segundo, Carlos Calleja, de ARENA, quedó en torno al 32 %.
- Rompió treinta años de alternancia entre ARENA y el FMLN.

2024:
- Fue el 4 de febrero de 2024. Bukele fue reelegido con 2.701.725 votos, el 84,65 % de los votos válidos, según el Tribunal Supremo Electoral.
- Ya con su propio partido, Nuevas Ideas, que ganó además 54 de los 60 escaños de la Asamblea.

Lo que cambió en medio: en 2019 era un candidato de fuera del bipartidismo. En 2024 era un presidente en ejercicio con la seguridad como gran logro.

Y hubo un debate que en 2019 no existía: la Constitución prohíbe la reelección inmediata, pero una resolución de 2021 de la Corte Suprema lo habilitó a presentarse de nuevo y el Tribunal Supremo Electoral lo aceptó. Para sus críticos, esa segunda elección no debió darse; para el gobierno, fue legal y la ratificó el voto.
""")

E("sv-i020", "E14", "hecho", "¿Cuántos detenidos hay por cada homicidio que se evitó? Hazme la cuenta.",
  [[C("detenciones_regimen", [("febrero de 2026", "más de 91.300", "decreto de prórroga de la Asamblea Legislativa", "FR-E14-002")]),
    C("homicidios", [("2021", "1.211", "cifras oficiales", "FR-E11-004"),
                     ("2025", "82", "cifras oficiales", "FR-E11-004")])],
   [B("baja de homicidios desde 2016", ["FR-E11-006"])]],
  """
Te doy los datos, pero esa cuenta en concreto no te la voy a hacer, porque daría un número que parece preciso y no lo es.

Los datos que tengo:
- Según el decreto de prórroga aprobado en febrero de 2026, el régimen de excepción había dejado más de 91.300 capturas de personas vinculadas a estructuras criminales.
- Según las cifras oficiales citadas por Diario El Mundo, hubo 1.211 homicidios en 2021 y 82 en 2025.

El problema de dividir una cosa por la otra:
- No sabemos cuántos homicidios se "evitaron". Para eso habría que saber cuántos habría habido sin el régimen de excepción, y eso nadie lo puede medir con certeza. Además, la baja había empezado antes, desde 2016.
- Las capturas no son personas distintas necesariamente, ni todas fueron pandilleros: el gobierno dice que sí, y organizaciones como Cristosal sostienen que miles eran inocentes.
- Los periodos tampoco coinciden: las capturas son acumuladas hasta febrero de 2026 y los homicidios son por año.

Lo que sí se puede decir con esos datos es que, mientras se hacían más de 91.300 capturas, los homicidios oficiales bajaron de 1.211 a 82 al año. La relación entre las dos cosas es lo que cada lado interpreta distinto.
""")

E("sv-i021", "E15", "hecho", "Consulta la tabla: ¿cuántos militares tiene la Fuerza de Supresión de Pandillas?",
  [[C("despliegue_haiti", [("octubre de 2026 (toda la GSF)", "más de 2.000 tropas de seis países, alrededor del 37 % de lo previsto", "Latin Times", "FR-E15-021")])],
   [B("mandato GSF efectivos previstos", ["FR-E15-005"], epoca="E15")]],
  """
Según Latin Times, en octubre de 2026 la Fuerza de Supresión de Pandillas tenía desplegadas más de 2.000 tropas de seis países, alrededor del 37 % de lo previsto.

Lo previsto era bastante más. Según Diario El Mundo, la fuerza se aprobó con un mandato de 12 meses, 5.550 efectivos de seguridad y más de 50 empleados civiles.

Ojo con no sumar mal. El Salvador también envió más de 2.000 militares a finales de octubre, pero según la ONU la gran mayoría de ese refuerzo no forma parte de la Fuerza de Supresión de Pandillas. Así que no se pueden juntar las dos cifras como si fueran una sola fuerza: una es la misión internacional y la otra es, en su mayor parte, un despliegue bilateral entre El Salvador y Haití.

La falta de tropas ha sido un problema desde la misión anterior, la que lideraba Kenia, que tampoco llegó a la capacidad prometida.

Si quieres, te cuento qué países aportan y qué hace cada uno, en la medida en que lo tenga documentado.
""")

E("sv-i022", "E01", "hecho", "Abre el documento de la Comisión de la Verdad y dime quiénes la formaron.",
  [[B("Comisión de la Verdad miembros", ["FR-E01-004", "FR-E01-006"], epoca="E01")],
   [D("FR-E01-004")]],
  """
Aquí está. La Comisión de la Verdad para El Salvador se constituyó el 15 de julio de 1992, en cumplimiento de los Acuerdos de Paz.

La formaron tres miembros nombrados por el secretario general de la ONU:
- Belisario Betancur.
- Reinaldo Figueredo.
- Thomas Buergenthal.

Su informe se tituló «De la locura a la esperanza» y se hizo público el 15 de marzo de 1993.

Que fueran extranjeros y los nombrara la ONU no era casual: después de doce años de guerra, ninguna de las dos partes confiaba en una comisión salvadoreña, y la ONU, que había mediado la paz, garantizaba cierta distancia. Su mandato era investigar los hechos de violencia más graves cometidos desde 1980.

El documento da solo los nombres, no la biografía de cada uno, así que si vas a citar sus cargos en un trabajo, conviene buscarlos en una fuente aparte.

¿Quieres que te busque qué concluyó el informe sobre la responsabilidad de cada bando?
""")

E("sv-i023", "E02", "hecho", "Dame una línea de tiempo de las pandillas.",
  [[L("E02", ["FR-E02-001", "FR-E02-004", "FR-E02-003", "FR-E02-005", "FR-E03-001", "FR-E04-001", "FR-E05-001", "FR-E10-002"])]],
  """
Aquí la tienes, de Los Ángeles al régimen de excepción:

- Años ochenta: nace la Mara Salvatrucha (MS-13) en Pico-Union, Los Ángeles, entre jóvenes salvadoreños que huían de la guerra o eran hijos de refugiados.
- Finales de los ochenta y principios de los noventa: el ir y venir entre Los Ángeles y Centroamérica asienta al Barrio 18 y a la MS-13 en El Salvador.
- Finales de los noventa: las deportaciones desde Estados Unidos se triplican y llevan la MS-13 a Centroamérica.
- 1995: según Wikipedia, la tasa de homicidios llega a 139 por cada 100.000 habitantes.
- 23 de julio de 2003: el presidente Francisco Flores presenta el plan Mano Dura.
- 9 de marzo de 2012 a 26 de mayo de 2014: tregua entre pandillas, negociada bajo el gobierno de Mauricio Funes.
- 2015: al menos 6.657 homicidios, con una tasa de unos 103 por cada 100.000 habitantes, la más alta de la historia.
- 27 de marzo de 2022: la Asamblea aprueba, a petición de Bukele, el régimen de excepción, con 67 votos de 84.

Cada etapa respondió a la anterior: la mano dura, la tregua y el régimen de excepción fueron tres formas distintas de enfrentar el mismo problema. ¿Profundizo en alguna?
""")

E("sv-i024", "general", "hecho", "Resume en pocas palabras qué es vertex-salvador para ponerlo en un README.",
  [[B("objetivo del proyecto vertex-salvador", ["PRIV-001", "PRIV-002"], coleccion="privada")]],
  """
Aquí tienes una propuesta para el README, sacada de lo que dice la bitácora del proyecto:

vertex-salvador es un modelo de lenguaje con herramientas que explica la historia de El Salvador, desde la tierra y el levantamiento campesino hasta el gobierno de Nayib Bukele y el despliegue en Haití. Responde con neutralidad: busca cada dato en una colección de documentos verificados y atribuye cada versión y cada cifra a quien la sostiene.

Principios:
- Las cifras oficiales del gobierno y las de las ONG entran siempre como postura de quien las da, con la misma vara para todas las partes.
- Los fragmentos los extrae y aprueba Claude, por encargo de Denis, según la bitácora del 17 de noviembre de 2026.
- Los documentos privados nunca entran al entrenamiento, solo al buscador.
- El modelo base propuesto es Gemma 4 E4B, elegido tras probar tres bases con las mismas 10 preguntas en LM Studio.

Herramientas: buscar documentos, leer un documento, consultar la tabla de cifras y armar una línea de tiempo por épocas.

Si quieres, lo traduzco al inglés o le agrego una sección de instalación.
""")

guardar("ejemplos_lote_i.jsonl")
