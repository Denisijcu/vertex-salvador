"""
ejemplos_lote_h.py — Ejemplos de entrenamiento, lote H: preguntas cortas, informales o ambiguas.
El modelo de la primera prueba pedía aclaración en vez de buscar. Aquí cada pregunta corta o mal escrita se
contesta buscando primero y, si hace falta, ofreciendo seguir por otro lado al final.
Uso (desde E:\\vertex-salvador):  python ejemplos_lote_h.py  ->  datos\\ejemplos_lote_h.jsonl
"""
from ejemplos_base import B, C, D, E, L, guardar

E("sv-h001", "E10", "hecho", "regimen de excepcion",
  [[B("régimen de excepción", ["FR-E10-002", "FR-E10-004", "FR-E14-001"])]],
  """
Te resumo lo básico del régimen de excepción en El Salvador.

Empezó el 27 de marzo de 2022, cuando la Asamblea Legislativa lo aprobó a petición de Bukele, por 30 días, por las graves perturbaciones del orden público causadas por grupos delincuenciales. Votaron a favor 67 de los 84 diputados. Venía de un fin de semana con decenas de asesinatos.

Lo que cambia: suspende garantías como la inviolabilidad de las comunicaciones y el derecho a la defensa de los detenidos, y amplía la detención administrativa a 15 días.

Cuánto dura: la Asamblea lo ha prorrogado cada 30 días desde entonces. El 24 de junio de 2026 aprobó la prórroga número 52, cuando la medida llevaba más de cuatro años en vigor sin interrupción.

Es la política más popular del gobierno y también la más criticada. El gobierno le atribuye la caída de los homicidios; las organizaciones de derechos humanos denuncian detenciones de inocentes y muertes bajo custodia.

¿Quieres las cifras de detenidos, las de homicidios o las críticas?
""")

E("sv-h002", "E11", "hecho", "cecot",
  [[B("CECOT", ["FR-E11-001", "FR-E11-002", "FR-E13-001"], epoca="E11")]],
  """
El CECOT, Centro de Confinamiento del Terrorismo, es la megacárcel del gobierno de Bukele para pandilleros.

Lo esencial:
- Está en Tecoluca, en el departamento de San Vicente.
- Se construyó entre julio de 2022 y enero de 2023 y abrió a finales de enero de 2023.
- Tiene capacidad para 40.000 presos y es la cárcel más grande de América Latina.
- Recibió a sus primeros 2.000 reclusos el 24 de febrero de 2023.

Cuántos presos tiene hoy no se sabe con precisión. Según Centroamérica 360, las autoridades no han dado cifras oficiales actualizadas; en octubre de 2023 se dijo que operaba al 30 % de su capacidad.

También se hizo famoso fuera del país en 2025. El 15 de marzo de ese año llegaron a El Salvador 238 deportados de Estados Unidos, la mayoría venezolanos acusados de pertenecer al Tren de Aragua y 23 salvadoreños señalados como pandilleros de la MS-13, y todos fueron recluidos en el CECOT.

¿Te interesa más la parte de los deportados o lo que dicen las organizaciones de derechos humanos?
""")

E("sv-h003", "T01", "hecho", "bukele",
  [[B("Nayib Bukele perfil carrera", ["FR-T01-001", "FR-E06-001", "FR-E07-001", "FR-E12-001"], epoca="T01")]],
  """
Te doy el perfil corto de Nayib Bukele.

Según su biografía en Wikipedia, Nayib Armando Bukele Ortez nació el 24 de julio de 1981 en San Salvador. Es hijo del empresario Armando Bukele Kattán, que murió en 2015, y de Olga Marina Ortez. Estudió en la Universidad Centroamericana (UCA) sin terminar la carrera.

Su carrera política:
- En 2012, a los 31 años, fue elegido alcalde de Nuevo Cuscatlán con el FMLN.
- En 2015 ganó la alcaldía de San Salvador, también con el FMLN, y la ejerció hasta 2018.
- El 3 de febrero de 2019 ganó la presidencia en primera vuelta con el 53 % de los votos válidos, como candidato de GANA.
- El 4 de febrero de 2024 fue reelegido con 2.701.725 votos, el 84,65 % de los votos válidos, y Nuevas Ideas ganó 54 de los 60 escaños de la Asamblea.

Es conocido sobre todo por su guerra contra las pandillas y el régimen de excepción, que le dan mucha popularidad y también muchas críticas por la concentración del poder.

¿Por dónde sigo: la seguridad, la reelección o las críticas?
""")

E("sv-h004", "E09", "hecho", "lo del 1 de mayo",
  [[B("1 de mayo 2021 destitución Sala de lo Constitucional", ["FR-E09-001", "FR-E09-003"], epoca="E09")]],
  """
Supongo que te refieres al 1 de mayo de 2021, que es la fecha que más pesa en la política salvadoreña reciente. Te lo cuento.

Ese día, en su primera sesión, la nueva Asamblea Legislativa, con mayoría de Nuevas Ideas tras las elecciones del 28 de febrero, destituyó a los cinco magistrados de la Sala de lo Constitucional y al fiscal general, Raúl Melara, y los sustituyó esa misma noche. La destitución se aprobó con 64 votos a favor y 19 en contra.

Media hora después, la Sala saliente declaró inconstitucional su destitución. La OEA rechazó las destituciones y el secretario de Estado de Estados Unidos, Antony Blinken, expresó a Bukele una profunda preocupación.

Por qué importa: fue el día en que el partido del presidente pasó a controlar, además de la Asamblea, el tribunal que debía revisar la constitucionalidad de sus actos. Meses después, una resolución de la Corte Suprema lo habilitó para la reelección.

Si buscabas otro 1 de mayo, por ejemplo el día del trabajo o alguna marcha, dímelo y lo busco.
""")

E("sv-h005", "E15", "hecho", "haiti",
  [[B("Haití El Salvador", ["FR-E15-004", "FR-E15-007", "FR-E15-008", "FR-E15-022"], epoca="E15")]],
  """
Te resumo lo de El Salvador en Haití, con los datos hasta el 18 de noviembre de 2026.

El marco: el 30 de septiembre de 2025 el Consejo de Seguridad de la ONU aprobó la resolución 2793, que creó la Fuerza de Supresión de Pandillas (GSF) a partir de la misión que lideraba Kenia, por un periodo inicial de 12 meses. El Salvador participa en ella.

El giro: el domingo 18 de octubre de 2026 cuatro aerotécnicos salvadoreños de la Fuerza de Tarea Libertad II sufrieron una emboscada en Santo, en Croix-des-Bouquets, a unos 12 kilómetros de Puerto Príncipe. Salieron del vehículo blindado, que fue incendiado, y se perdió el contacto con ellos.

La respuesta: a finales de octubre El Salvador envió más de 2.000 militares, con blindados y helicópteros, para buscarlos. El 28 de octubre la Cancillería confirmó la cifra.

El estado: al cumplirse un mes, el 18 de noviembre, las autoridades no habían confirmado ni el paradero ni el estado de los cuatro. El 10 de noviembre el vicepresidente Félix Ulloa dijo: "No hay rastro de ellos".

¿Quieres lo que dicen la ONU, el gobierno haitiano o los críticos?
""")

E("sv-h006", "E04", "hecho", "tregua",
  [[B("tregua entre pandillas", ["FR-E04-001", "FR-E04-002", "FR-E04-006"], epoca="E04")]],
  """
Te cuento la tregua entre pandillas de El Salvador, que es la más conocida.

Duró del 9 de marzo de 2012 al 26 de mayo de 2014. Sus principales negociadores fueron el ministro de Seguridad, David Munguía Payés, el exdiputado y exguerrillero Raúl Mijango y el obispo Fabio Colindres, bajo la supervisión del presidente Mauricio Funes.

Se supo por la prensa: el 14 de marzo de 2012 El Faro informó del traslado de 30 líderes pandilleros de la cárcel de máxima seguridad a otros penales, y dijo que respondía a una negociación del gobierno con las pandillas a cambio de bajar los homicidios. Las autoridades dieron explicaciones contradictorias, pero los homicidios cayeron un 53 % a partir del traslado.

El final fue judicial. En 2023 un tribunal de San Salvador condenó al exministro Munguía Payés a 18 años de cárcel y al expresidente Funes, juzgado en ausencia, a 14 años, por agrupaciones ilícitas e incumplimiento de deberes. Mijango fue absuelto en 2017 y en 2019.

Si buscabas otra cosa, como la acusación de que el gobierno de Bukele también negoció con las pandillas, dímelo y te la busco.
""")

E("sv-h007", "E14", "hecho", "asere que bola con el salvador, como esta la cosa alla?",
  [[B("situación actual El Salvador 2026", ["FR-E14-003", "FR-E14-005", "FR-E14-001", "FR-E14-006"])]],
  """
¡Qué bolá! Te cuento cómo estaba la cosa al cierre de mis datos, en noviembre de 2026.

En seguridad, el cambio es enorme. Según los reportes oficiales de la Policía Nacional Civil citados por El Diario de Hoy, en octubre de 2026 hubo cuatro homicidios en todo el país, y 48 entre enero y octubre. Para un país que fue de los más violentos del mundo, eso es otra realidad.

El régimen de excepción sigue. El 24 de junio de 2026 la Asamblea aprobó la prórroga número 52, y para entonces llevaba más de cuatro años en vigor sin interrupción.

Bukele llegó a 2026 con índices altos de popularidad, que se han mantenido sin grandes cambios en sus siete años en el poder, y que descansan sobre todo en la baja de los homicidios y en el régimen de excepción.

Pero la otra cara también está ahí. Según un informe de Cristosal de marzo de 2026, el gobierno tiene al menos 86 presos políticos, entre ellos periodistas y sindicalistas, algo que el gobierno rechaza.

Y afuera, el tema del momento es el despliegue de militares salvadoreños en Haití. ¿Te cuento eso?
""")

E("sv-h008", "E02", "hecho", "de donde salieron los mareros",
  [[B("origen pandillas mareros Los Ángeles deportaciones", ["FR-E02-001", "FR-E02-003", "FR-E02-004"], epoca="E02")]],
  """
Salieron de Los Ángeles, y llegaron a El Salvador con las deportaciones.

La Mara Salvatrucha (MS-13) nació en los años ochenta en el barrio de Pico-Union, en Los Ángeles. La formaron jóvenes salvadoreños que habían huido de la guerra civil o eran hijos de refugiados, y al principio servía para protegerse de otras pandillas de la zona.

El ir y venir constante entre Los Ángeles y Centroamérica permitió que el Barrio 18 y la MS-13 se asentaran en El Salvador entre finales de los ochenta y principios de los noventa.

El gran empujón vino después. Las deportaciones desde Estados Unidos se triplicaron a finales de los años noventa y llevaron la MS-13 a Centroamérica, donde los miembros deportados abrieron nuevos grupos. Esas deportaciones se apoyaban en las leyes de la época del presidente Clinton, que facilitaron expulsar a inmigrantes con antecedentes penales. En esa década la pandilla pasó de ser juvenil a carcelaria y luego transnacional.

O sea, el marero salvadoreño es, en buena parte, un producto de la guerra, del exilio y de las deportaciones. ¿Quieres que te cuente cómo se organizan?
""")

E("sv-h009", "E01", "hecho", "romero",
  [[B("monseñor Óscar Arnulfo Romero", ["FR-E01-001", "FR-E01-002", "FR-P03-004"], epoca="E01")]],
  """
Te cuento de monseñor Óscar Arnulfo Romero, arzobispo de San Salvador.

Lo asesinaron de un disparo el 24 de marzo de 1980 mientras celebraba misa en la capilla de un hospital de San Salvador. Es uno de los hechos que marcan el inicio de la guerra civil.

Romero se había convertido en una voz contra la violencia del Estado. Según el Zinn Education Project, en febrero de 1980, un mes antes de su muerte, escribió al presidente de Estados Unidos, Jimmy Carter, para pedirle que detuviera la ayuda militar al gobierno salvadoreño.

Para muchos salvadoreños es una figura moral, más allá de la religión. Su asesinato, junto con otros crímenes de la guerra, fue investigado después por la Comisión de la Verdad.

Si buscabas a otro Romero, por ejemplo al general Carlos Humberto Romero, el presidente al que derrocó el golpe de octubre de 1979, dímelo y te busco sobre él.
""")

E("sv-h010", "E03", "hecho", "mano dura",
  [[B("plan Mano Dura Súper Mano Dura", ["FR-E03-001", "FR-E03-002", "FR-E03-004"], epoca="E03")]],
  """
Te resumo los planes de mano dura contra las pandillas de los años dos mil.

Mano Dura: a mediados de 2003 el presidente Francisco Flores, de ARENA, lanzó el plan, con capturas sistemáticas de pandilleros y apoyo de la Fuerza Armada a la Policía en las calles. Lo presentó en cadena nacional el 23 de julio de 2003. Según InSight Crime, la Ley Antimaras entró en vigor el 10 de octubre de ese año. Según la Policía, el plan dejó 19.275 arrestos entre julio de 2003 y agosto de 2004, y 17.540 de esos detenidos quedaron libres por falta de pruebas.

Súper Mano Dura: el 30 de agosto de 2004, a los 60 días de asumir, el presidente Antonio Saca, también de ARENA, presentó el plan Súper Mano Dura para aumentar las capturas. Lo acompañó de programas de prevención y reinserción llamados Mano Amiga y Mano Extendida.

Sobre si funcionaron, las fuentes no coinciden: unas muestran más muertes violentas en esos años y otras una baja temporal. Varias coinciden en que las cárceles se volvieron centros de reclutamiento.

¿Quieres que te compare esos planes con el régimen de excepción?
""")

E("sv-h011", "E01", "hecho", "paz 92",
  [[B("acuerdos de paz 1992 Chapultepec", ["FR-E01-007", "FR-E01-004", "FR-E01-008"], epoca="E01")]],
  """
Te cuento los acuerdos de paz de 1992.

El 16 de enero de 1992, en el castillo de Chapultepec, en Ciudad de México, el gobierno de Alfredo Cristiani y la comandancia del FMLN firmaron, con mediación de la ONU, los acuerdos de paz que pusieron fin a doce años de guerra.

Los acuerdos no solo pararon los combates. También crearon instituciones nuevas y mecanismos para revisar el pasado. El más conocido es la Comisión de la Verdad para El Salvador, que se constituyó el 15 de julio de 1992 con tres miembros nombrados por el secretario general de la ONU: Belisario Betancur, Reinaldo Figueredo y Thomas Buergenthal. Su informe, «De la locura a la esperanza», se hizo público el 15 de marzo de 1993.

Tras la firma, el FMLN dejó las armas y se convirtió en partido político, y durante casi tres décadas se alternó en el poder con ARENA.

Si quieres, te cuento cómo se llegó a la firma, desde el primer acercamiento en 1984, o qué concluyó la Comisión de la Verdad.
""")

E("sv-h012", "E12", "hecho", "reeleccion",
  [[B("reelección Bukele 2024 Constitución", ["FR-E09-004", "FR-E12-001"], epoca="E12")]],
  """
Te resumo lo de la reelección de Bukele.

El problema legal: la Constitución salvadoreña prohíbe la reelección presidencial inmediata. Pero una resolución de 2021 de la Corte Suprema de Justicia habilitó a Bukele a presentarse de nuevo, y el Tribunal Supremo Electoral aceptó su candidatura. Esa resolución la dictaron magistrados nombrados por la Asamblea de Nuevas Ideas después de destituir a los anteriores, y por eso es tan discutida.

El resultado: el 4 de febrero de 2024 Bukele fue reelegido con 2.701.725 votos, el 84,65 % de los votos válidos, según el Tribunal Supremo Electoral. Nuevas Ideas ganó 54 de los 60 escaños de la Asamblea.

Las dos lecturas: para el gobierno y sus aliados, la reelección fue legal porque la autorizaron las instituciones competentes y la ratificaron los votantes. Para sus críticos, fue inconstitucional, porque la prohibición está escrita y la reinterpretaron jueces puestos por el oficialismo.

¿Quieres que te busque cómo se reparte la participación electoral de 2024, o las críticas de las organizaciones sobre la concentración del poder?
""")

E("sv-h013", "general", "hecho", "y tu q eres?",
  [[B("qué es vertex-salvador herramientas documentos", ["PRIV-001", "PRIV-002"], coleccion="privada")]],
  """
Soy el asistente de vertex-salvador, un modelo pensado para hablar de El Salvador: su historia, las pandillas y el gobierno de Nayib Bukele, y también lo que hoy pasa con los militares salvadoreños en Haití.

Funciono con herramientas. Antes de darte un dato, una fecha o una cifra, la busco en una colección de documentos revisados. Puedo leer un documento completo, armarte una línea de tiempo por épocas y consultar una tabla de cifras. También busco en tus documentos privados si los guardas.

La regla de fondo está en la bitácora del proyecto: las cifras oficiales del gobierno y las de las ONG entran siempre como postura de quien las da, con la misma vara para todas las partes. Por eso te digo de quién es cada cosa. Y según esa misma bitácora, los documentos privados nunca entran al entrenamiento, solo al buscador, así que tus papeles no quedan dentro de mí.

Si algo no lo encuentro, te lo digo en vez de inventarlo. ¿Qué quieres saber?
""")

E("sv-h014", "E13", "hecho", "deportados venezolanos",
  [[B("deportados venezolanos CECOT 2025", ["FR-E13-001", "FR-E13-002"], epoca="E13")]],
  """
Te cuento lo de los deportados venezolanos que fueron a parar al CECOT.

El 15 de marzo de 2025 el presidente Donald Trump invocó la Ley de Enemigos Extranjeros de 1798 contra la banda venezolana Tren de Aragua. Ese mismo día, pese a que el juez federal James Boasberg había prohibido esos vuelos mientras decidía, llegaron a El Salvador 238 deportados, 23 de ellos salvadoreños señalados como pandilleros de la MS-13. Todos fueron recluidos en el CECOT.

El acuerdo económico: según la Casa Blanca, Washington pagó aproximadamente 6 millones de dólares al gobierno de Bukele por recluir a esos deportados durante un año. El acuerdo lo cerraron Bukele y el secretario de Estado, Marco Rubio, y no se ha hecho público.

El caso generó un choque judicial en Estados Unidos, porque los vuelos salieron pese a la orden del juez, y críticas de organizaciones que defienden a los migrantes. El gobierno salvadoreño lo presentó como cooperación con Estados Unidos contra el crimen organizado.

¿Quieres que te busque qué pasó con ellos después, o el resto de la relación de Bukele con Washington?
""")

E("sv-h015", "P05", "hecho", "fmln",
  [[B("FMLN origen guerrilla partido", ["FR-P05-002", "FR-P02-006", "FR-E01-007", "FR-E06-002"])]],
  """
Te resumo el FMLN, de guerrilla a partido.

Nació como guerrilla: se formó el 10 de octubre de 1980 como coalición de cinco organizaciones de izquierda, las FPL, el ERP, la Resistencia Nacional, el Partido Comunista Salvadoreño y el PRTC, que se sumó el 5 de diciembre de 1980. Su nombre, Frente Farabundo Martí para la Liberación Nacional, recoge el de Farabundo Martí, fusilado en 1932.

Combatió en la guerra civil hasta el 16 de enero de 1992, cuando su comandancia firmó en Chapultepec, con el gobierno de Alfredo Cristiani y con mediación de la ONU, los acuerdos de paz.

Después se convirtió en partido político y llegó a gobernar. Hay un dato curioso de su historia reciente: Nayib Bukele empezó su carrera política en el FMLN, pero sus diferencias con la dirección terminaron con su expulsión en 2017. Ese año fundó Nuevas Ideas, el partido con el que después desplazó a los partidos tradicionales.

¿Te interesa más la etapa de la guerra, el apoyo cubano o su papel como partido?
""")

E("sv-h016", "E14", "hecho", "presos politicos",
  [[C("presos_politicos", [("marzo de 2026", "al menos 86", "Cristosal (el gobierno lo rechaza)", "FR-E14-006")])],
   [B("presos políticos respuesta gobierno", ["FR-E14-007", "FR-E13-006"], epoca="E14")]],
  """
Es uno de los temas más disputados. Te doy la cifra con su dueño y la respuesta del gobierno.

Según un informe de Cristosal presentado en Guatemala en marzo de 2026, el gobierno de Bukele tiene al menos 86 presos políticos, sobre todo defensores de derechos humanos, periodistas, funcionarios judiciales, sindicalistas y ambientalistas. Cristosal, ojo, es una organización crítica del gobierno, y una de sus directivas, Ruth López, fue detenida en mayo de 2025 y acusada por la Fiscalía de enriquecimiento ilícito, algo que la organización calificó de represalia política.

Un grupo internacional de expertos, el GIPES, concluyó ese mismo mes ante la CIDH que hay bases razonables para creer que se cometen crímenes de lesa humanidad, según el Tico Times.

El gobierno lo rechaza todo: según el Tico Times, Bukele rechazó tanto esa conclusión como la acusación de que hay presos políticos.

Así que la cifra de 86 es la de Cristosal, no un dato oficial ni independiente, y el gobierno sostiene que no hay ninguno. ¿Quieres que te busque más sobre algún caso?
""")

E("sv-h017", "general", "hecho", "dame datos",
  [[C("homicidios", [("2015", "6.657 homicidios; 103 por cada 100.000", "estadísticas oficiales", "FR-E05-001"),
                     ("2025", "82", "cifras oficiales", "FR-E11-004")]),
    C("detenciones_regimen", [("febrero de 2026", "más de 91.300", "decreto de prórroga de la Asamblea Legislativa", "FR-E14-002")]),
    C("elecciones_presidenciales", [("2024", "Bukele 84,65 % (2.701.725 votos)", "Tribunal Supremo Electoral", "FR-E12-001")])]],
  """
Te doy los datos más pedidos, cada uno con quién lo da, y luego me dices de qué tema quieres más.

Homicidios:
- 2015: al menos 6.657 homicidios, con una tasa de unos 103 por cada 100.000 habitantes, según las estadísticas oficiales. Es el récord histórico.
- 2025: 82 homicidios, según las cifras oficiales citadas por Diario El Mundo.

Detenciones:
- Según el decreto de prórroga aprobado en febrero de 2026, el régimen de excepción había dejado más de 91.300 capturas de personas vinculadas a estructuras criminales. Es la cifra del Estado.

Elecciones:
- El 4 de febrero de 2024 Bukele fue reelegido con 2.701.725 votos, el 84,65 % de los votos válidos, según el Tribunal Supremo Electoral.

En la tabla tengo también cifras de la guerra civil, de la ayuda de Estados Unidos, de las muertes bajo custodia, de los presos políticos que denuncia Cristosal y del despliegue en Haití.

¿Qué tema te interesa?
""")

E("sv-h018", "E08", "hecho", "9f",
  [[B("9F 9 de febrero 2020 Asamblea", ["FR-E08-001", "FR-E08-002", "FR-E08-003"], epoca="E08")]],
  """
El 9F es como se conoce lo que pasó el 9 de febrero de 2020 en la Asamblea Legislativa.

Ese día Bukele entró en la Asamblea acompañado de militares y policías armados para presionar a los diputados, entonces de mayoría opositora, a aprobar un préstamo de 109 millones de dólares para la fase III del Plan Control Territorial. Se sentó en la silla del presidente de la Asamblea y rezó en el Salón Azul.

Según EFE, la sesión extraordinaria que había convocado no pudo celebrarse por falta de quórum, porque solo se presentaron 20 diputados. Ante sus seguidores, Bukele dio una semana a los legisladores para aprobar el préstamo.

Lo que se discute es cómo llamarlo. Según la Revista E&N, para un diputado del PCN fue una toma a la fuerza de la Asamblea con intención de disolverla. En cambio, el diputado Guillermo Gallegos, de GANA, aliado del gobierno, sostuvo que nunca se intentó un golpe de Estado y llamó absurdo conmemorar esa fecha.

Los hechos del día están claros; la intención es lo que cada lado lee distinto.
""")

E("sv-h019", "E13", "hecho", "ley de agentes extranjeros",
  [[B("Ley de Agentes Extranjeros RAEX", ["FR-E13-003", "FR-E13-004", "FR-E13-005"], epoca="E13")]],
  """
Te resumo la Ley de Agentes Extranjeros de El Salvador.

Qué es: la aprobó la Asamblea el 20 de mayo de 2025, con 57 votos. Obliga a las personas y organizaciones que reciben fondos del exterior a inscribirse en un Registro de Agentes Extranjeros (RAEX) y les cobra un impuesto del 30 % sobre esas donaciones.

Para qué, según la ley: según LexLatin, declara como finalidad promover la transparencia sobre la influencia extranjera y resguardar la seguridad, la soberanía nacional y la estabilidad social y política del país.

Qué dicen los críticos: según Human Rights Watch, la ley da al gobierno amplias facultades para vigilar, sancionar y cerrar a las organizaciones que estigmatiza como agentes extranjeros, y se aprobó prácticamente sin debate ni consulta pública.

A quién afecta más: a las ONG de derechos humanos, a los medios independientes y a las organizaciones civiles que viven de la cooperación internacional, que son también las que más critican al gobierno. Por eso para unos es una ley de transparencia y para otros una forma de silenciar.

¿Quieres que te busque qué pasó con alguna organización después de la ley?
""")

E("sv-h020", "P04", "hecho", "tricontinental",
  [[B("Conferencia Tricontinental 1966 La Habana", ["FR-P04-001", "FR-P04-002"], epoca="P04")]],
  """
Te cuento la Conferencia Tricontinental.

Se celebró en La Habana del 3 al 15 de enero de 1966, con 512 delegados de 82 países de Asia, África y América Latina. De ella nació la Organización de Solidaridad de los Pueblos de Asia, África y América Latina (OSPAAAL), y la conferencia declaró su apoyo a la lucha armada.

Fue un momento clave para la proyección internacional de la Revolución Cubana: La Habana se presentó como el centro de los movimientos revolucionarios del llamado Tercer Mundo.

Tuvo una continuación regional. Según el sociólogo Emir Sader, en 1967 Cuba convocó la Organización Latinoamericana de Solidaridad (OLAS), que optó abiertamente por la lucha armada y las guerrillas. Pero cuando la lucha armada se reanudó en la década siguiente, con el centro en Centroamérica, la OLAS ya era un órgano de difusión sin capacidad real de coordinar a los movimientos.

Para El Salvador, la Tricontinental es parte del contexto: la idea de que el cambio se hacía con las armas, que Cuba promovió desde entonces, influyó en las guerrillas que surgieron en los setenta. ¿Quieres seguir por el Departamento América, que fue el aparato práctico de esa relación?
""")

E("sv-h021", "E05", "hecho", "2015",
  [[B("2015 El Salvador año más violento", ["FR-E05-001", "FR-E05-002", "FR-T02-002"], epoca="E05")]],
  """
2015 fue el año más violento de la historia moderna de El Salvador.

Ese año El Salvador fue el país más violento del hemisferio occidental. Según las estadísticas oficiales, hubo al menos 6.657 homicidios, con una tasa de unos 103 por cada 100.000 habitantes, la más alta de su historia.

Las causas, según InSight Crime, fueron una combinación de fragmentación de las pandillas, choques internos y grupos de justicia por mano propia. La tregua entre pandillas se había roto el año anterior y la violencia volvió con más fuerza.

Ese mismo año, el 24 de agosto de 2015, El Salvador declaró al Barrio 18 organización terrorista. Ya entonces el 18 estaba partido en dos facciones rivales, los Revolucionarios y los Sureños, que también se enfrentaban entre sí.

Después de 2015 los homicidios empezaron a bajar, varios años antes de que Bukele llegara a la presidencia. Ese dato es central en el debate sobre a quién atribuirle la caída.

¿Quieres que te dé la serie de homicidios desde ese año hasta hoy?
""")

E("sv-h022", "E14", "hecho", "muertos en las carceles",
  [[C("muertes_custodia", [("régimen de excepción (hasta 2026)", "530", "Socorro Jurídico Humanitario", "FR-E14-008"),
                           ("régimen de excepción (hasta marzo de 2026)", "al menos 500", "organización salvadoreña citada por el Tico Times", "FR-E14-008")])],
   [B("respuesta gobierno organizaciones derechos humanos 2026", ["FR-E14-009"], epoca="E14")]],
  """
Te doy las cifras de muertes bajo custodia durante el régimen de excepción, que es lo que más se discute.

Las llevan organizaciones civiles, y no coinciden entre sí:
- Según Diario El Mundo, Socorro Jurídico Humanitario registra 530 fallecidos.
- Según el Tico Times, una organización salvadoreña cuenta al menos 500 hasta marzo de 2026, y afirma que la mayoría no tenía vínculos con pandillas.

El gobierno no publica una cifra propia. Eso significa que no hay un dato oficial con el que contrastar las de las organizaciones, y que todo lo que se sabe viene de su trabajo de documentación, con nombres de familias y casos.

Por eso te las doy atribuidas: son las cifras de esas organizaciones, no un dato verificado de forma independiente. Al mismo tiempo, que el Estado no dé su propia cifra es en sí un dato que conviene tener en cuenta.

Si quieres, te busco qué dice el gobierno sobre las organizaciones que hacen estas denuncias, o el informe del grupo de expertos que habló de posibles crímenes de lesa humanidad.
""")

E("sv-h023", "general", "hecho", "¿Me haces un resumen para una exposición en clase sobre El Salvador?",
  [[L("T04", ["FR-P02-003", "FR-P05-002", "FR-E01-007", "FR-E02-003", "FR-E05-001", "FR-E10-002", "FR-E11-004"])]],
  """
Claro. Aquí tienes un guion por partes, con los datos clave y quién los da, para que lo puedas defender en clase.

- Raíces del conflicto. Entre el 22 y el 25 de enero de 1932 hubo un levantamiento en el occidente del país, que el gobierno del general Maximiliano Hernández Martínez aplastó. Esa represión se conoce como La Matanza.

- La guerra. El FMLN se formó el 10 de octubre de 1980 con cinco organizaciones de izquierda. La guerra terminó el 16 de enero de 1992 con los acuerdos de Chapultepec, firmados con mediación de la ONU.

- Las maras. Las deportaciones desde Estados Unidos se triplicaron a finales de los noventa y llevaron la MS-13 a Centroamérica.

- La violencia. En 2015 hubo al menos 6.657 homicidios, con una tasa de unos 103 por cada 100.000 habitantes, la más alta de la historia del país, según las estadísticas oficiales.

- El presente. El 27 de marzo de 2022 empezó el régimen de excepción. Según las cifras oficiales, los homicidios bajaron de 1.211 en 2021 a 82 en 2025. Las organizaciones de derechos humanos denuncian detenciones de inocentes.

Un consejo: en la parte final, presenta la baja de homicidios y las críticas juntas. Si tu profesor pregunta, podrás decir de dónde sale cada dato.
""")

E("sv-h024", "E10", "hecho", "¿Qué votos hubo para aprobar el régimen de excepción?",
  [[B("votación Asamblea régimen de excepción 27 de marzo", ["FR-E10-002", "FR-E09-001", "FR-E14-001", "FR-E10-004"], epoca="E10")]],
  """
El 27 de marzo de 2022 la Asamblea Legislativa aprobó el régimen de excepción con 67 votos a favor de los 84 diputados que tenía entonces.

Lo pidió Bukele, y la Asamblea lo aprobó por 30 días, alegando las graves perturbaciones del orden público causadas por grupos delincuenciales. Venía de un fin de semana con decenas de asesinatos.

Esos 67 votos superaban de lejos la mayoría necesaria. En ese momento Nuevas Ideas y sus aliados dominaban la Asamblea desde las elecciones de febrero de 2021, así que la aprobación estaba asegurada.

Mis documentos no recogen cómo votó cada partido ni qué hicieron los demás diputados, si votaron en contra, se abstuvieron o no estaban, así que no te lo detallo.

Lo que vino después es una cadena de prórrogas: la Asamblea lo renueva cada 30 días desde entonces, y en junio de 2026 ya iba por la número 52.

Si quieres, te busco qué garantías suspende el régimen de excepción, que es lo que los diputados aprobaron en esa votación.
""")

E("sv-h025", "E14", "hecho", "y la oposicion que dice",
  [[B("oposición críticas gobierno Bukele", ["FR-E12-004", "FR-E14-010", "FR-E14-009"])]],
  """
En mis documentos la crítica al gobierno viene sobre todo de organizaciones civiles y de derechos humanos, más que de los partidos de oposición, que hoy tienen muy poco peso en la Asamblea. Te doy lo que dicen, con nombre.

Según CISPES, una organización de solidaridad crítica del gobierno, sindicatos de la salud, grupos de víctimas y organizaciones comunitarias califican de inconstitucional el gobierno de Bukele y denuncian la realidad interna detrás del internacionalmente celebrado modelo Bukele.

Según el Informe Mundial 2026 de Human Rights Watch, el gobierno de Bukele siguió eliminando los controles al Poder Ejecutivo y aumentó la represión contra defensores de derechos humanos, periodistas, activistas y sindicalistas.

La respuesta del gobierno es dura. Según el Tico Times, en marzo de 2026 Bukele acusó a las organizaciones de derechos humanos de actuar como bufetes de abogados de los criminales y dijo que su gobierno nunca atenderá sus críticas.

No tengo declaraciones recientes de los partidos de oposición, como ARENA o el FMLN, sobre el gobierno. Si te interesan, habría que buscarlas en la prensa del día.
""")

E("sv-h026", "E06", "hecho", "nuevas ideas",
  [[B("Nuevas Ideas partido fundación", ["FR-E06-002", "FR-E09-001", "FR-E12-001"])]],
  """
Nuevas Ideas es el partido de Nayib Bukele, y hoy domina la política salvadoreña.

Lo fundó en 2017, después de que el FMLN lo expulsara por sus diferencias con la dirección. Al principio no pudo inscribirse como partido porque no cumplía los requisitos de la ley electoral, y por eso Bukele se presentó a la presidencia de 2019 con otro partido, GANA.

Su gran salto fue en las legislativas del 28 de febrero de 2021, que le dieron la mayoría en la Asamblea. En la primera sesión de esa nueva Asamblea, el 1 de mayo de 2021, destituyó a los cinco magistrados de la Sala de lo Constitucional y al fiscal general, con 64 votos a favor y 19 en contra.

En las elecciones del 4 de febrero de 2024 consolidó su dominio: ganó 54 de los 60 escaños de la Asamblea, el mismo día que Bukele fue reelegido.

Para sus seguidores, es el movimiento que acabó con el bipartidismo de ARENA y el FMLN. Para sus críticos, es el instrumento con el que el presidente concentró el poder.

¿Quieres que te cuente cómo pasó de no estar inscrito a controlar casi toda la Asamblea, paso a paso?
""")

guardar("ejemplos_lote_h.jsonl")
