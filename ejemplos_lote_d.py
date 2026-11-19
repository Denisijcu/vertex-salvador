"""
ejemplos_lote_d.py — Ejemplos de entrenamiento, lote D: época E15, Haití (2024–2026).
Regla del lote: las declaraciones de los gobiernos salvadoreño, haitiano y estadounidense, y las de Amnistía o
UNA-Haití, siempre atribuidas. El caso de los cuatro aerotécnicos está abierto: los datos llegan al 18 de
noviembre de 2026 y el modelo lo dice en vez de inventar el desenlace.
Uso (desde E:\\vertex-salvador):  python ejemplos_lote_d.py  ->  datos\\ejemplos_lote_d.jsonl
"""
from ejemplos_base import B, C, D, E, L, guardar

E("sv-d001", "E15", "hecho", "¿Qué está haciendo El Salvador en Haití?",
  [[B("El Salvador militares en Haití", ["FR-E15-004", "FR-E15-006", "FR-E15-007", "FR-E15-008"], epoca="E15")]],
  """
Hay dos capas, y conviene separarlas porque la ONU también las separa.

La primera es la misión internacional. El 30 de septiembre de 2025 el Consejo de Seguridad aprobó la resolución 2793, que convirtió la misión que lideraba Kenia en la Fuerza de Supresión de Pandillas (GSF), con un periodo inicial de 12 meses. El Salvador ya tenía militares dentro de esa fuerza, y el 29 de septiembre de 2026 la Asamblea Legislativa aprobó con 57 votos una ley que extiende esa participación 12 meses más, hasta octubre de 2027, prorrogables.

La segunda capa empezó con un golpe. El domingo 18 de octubre de 2026 cuatro aerotécnicos salvadoreños de la Fuerza de Tarea Libertad II sufrieron una emboscada de grupos armados en Santo, en Croix-des-Bouquets, a unos 12 kilómetros de Puerto Príncipe. Según la Fuerza Armada, salieron del vehículo blindado, que fue incendiado, y se perdió el contacto con ellos.

A raíz de eso, a finales de octubre El Salvador envió más de 2.000 militares, con blindados y helicópteros, para buscarlos. Los primeros refuerzos llegaron el 22 de octubre y el 28 la Cancillería confirmó que el contingente superaba los 2.000 efectivos.

Si quieres, te cuento qué dicen el gobierno de Bukele, el de Haití y la ONU sobre ese despliegue, porque no lo ven igual.
""")

E("sv-d002", "E15", "hecho", "cuéntame lo de los soldados en Haití",
  [[B("soldados salvadoreños desaparecidos Haití emboscada", ["FR-E15-007", "FR-E15-010", "FR-E15-022"], epoca="E15")]],
  """
Te cuento lo que está confirmado y lo que no, con fecha, porque el caso sigue abierto.

Lo confirmado: el domingo 18 de octubre de 2026 cuatro aerotécnicos salvadoreños de la Fuerza de Tarea Libertad II, que formaban parte de la Fuerza de Supresión de Pandillas, cayeron en una emboscada de grupos armados en Santo, una localidad de Croix-des-Bouquets, a unos 12 kilómetros de Puerto Príncipe. Según la Fuerza Armada salvadoreña, regresaban a su campamento después de comprar alimentos, salieron del vehículo blindado, que fue incendiado, y se perdió el contacto con ellos.

Lo que circuló sin confirmar: el 24 de octubre hubo informes de que unos cuerpos podían ser de ellos, y Bukele lo rechazó con la frase "No son nuestros hombres". Un cabecilla de pandilla, Wilson Joseph, alias Lanmò San Jou, le dijo a la agencia AP que los cuatro estaban muertos, pero no dio pruebas y las autoridades salvadoreñas no lo confirmaron.

Dónde estaba el caso al cierre de mis datos: al cumplirse un mes, el 18 de noviembre de 2026, las autoridades no habían confirmado ni su paradero ni su estado. El 2 de noviembre la Policía Nacional de Haití recuperó el vehículo incendiado en Santo, sin pistas sobre los ocupantes, y el 10 de noviembre el vicepresidente Félix Ulloa dijo: "No hay rastro de ellos".

Lo que haya pasado después de esa fecha no lo tengo.
""")

E("sv-d003", "E15", "sin_datos", "¿Ya rescataron a los cuatro militares salvadoreños?",
  [[B("rescate militares salvadoreños Haití", ["FR-E15-022"], epoca="E15")]],
  """
Hasta donde llegan mis datos, no. Al cumplirse un mes de la emboscada, el 18 de noviembre de 2026, las autoridades no habían confirmado ni el paradero ni el estado de los cuatro aerotécnicos. El vicepresidente Félix Ulloa había dicho el 10 de noviembre: "No hay rastro de ellos".

Si hubo un rescate o alguna noticia después de esa fecha, no la tengo. Para eso conviene revisar los comunicados de la Fuerza Armada salvadoreña o la prensa del día.
""")

E("sv-d004", "E15", "hecho", "¿Cuántos soldados mandó Bukele a Haití?",
  [[C("despliegue_haiti", [("primer contingente (misión liderada por Kenia)", "70 soldados para evacuaciones médicas", "Voz de América", "FR-E15-003"),
                           ("28 de octubre de 2026", "más de 2.000 militares", "Cancillería salvadoreña, según El Diario de Hoy", "FR-E15-008")])],
   [B("contingente salvadoreño Haití más numeroso", ["FR-E15-009", "FR-E15-007"], epoca="E15")]],
  """
Depende del momento, porque el despliegue cambió mucho de tamaño.

Al principio fue pequeño. Según la Voz de América, el primer contingente militar salvadoreño que llegó a Haití para la misión liderada por Kenia fue de 70 soldados, destinados a las evacuaciones médicas.

El salto vino tras la emboscada del 18 de octubre de 2026 contra cuatro aerotécnicos salvadoreños. A finales de ese mes El Salvador envió más de 2.000 militares, con blindados y helicópteros, para buscarlos; el 28 de octubre la Cancillería confirmó que el contingente superaba esa cifra.

Para darte la escala, según DW es el contingente más numeroso que un país ha desplegado en Haití desde que terminó la Misión de Estabilización de las Naciones Unidas (Minustah). Incluye fuerzas especiales.

Un matiz importante: no todos esos militares están bajo la fuerza de la ONU. La organización aclaró que la gran mayoría de los enviados en esa segunda ola no forma parte de la Fuerza de Supresión de Pandillas. Si quieres, te explico qué implica eso.
""")

E("sv-d005", "E15", "perspectivas", "¿Es una invasión lo que está haciendo El Salvador en Haití?",
  [[B("Bukele invasión Haití declaraciones", ["FR-E15-012", "FR-E15-014"], epoca="E15"),
    B("ONU UNA-Haití críticas despliegue salvadoreño", ["FR-E15-017", "FR-E15-019"], epoca="E15")]],
  """
Es justo lo que se discute, y cada parte lo ve distinto. Te pongo las versiones con nombre.

El gobierno salvadoreño lo niega. Según Diario El Mundo, Bukele dijo el 29 de octubre de 2026: "Esto no es una operación contra el pueblo haitiano, ni una invasión al país de Haití". Sostiene que su objetivo principal es que vuelvan los cuatro técnicos de aviación y que su gobierno paga el 90 % de los gastos, aunque otros países aportan parte de la logística.

El gobierno de Haití lo respalda. Según EFE, el primer ministro Alix Didier Fils-Aimé afirmó el 10 de noviembre que está recuperando el control territorial con el apoyo de las tropas salvadoreñas y escribió: "Haití, El Salvador, GSF: ¡el mismo combate, la misma determinación!".

La ONU marcó distancia. El 2 de noviembre aclaró que la gran mayoría de los militares salvadoreños enviados adicionalmente no forma parte de la Fuerza de Supresión de Pandillas, así que quedan fuera de sus mecanismos de supervisión, y recordó que toda operación debe respetar el derecho internacional.

Y hay críticos haitianos. UNA-Haití, un grupo que representa a sectores de la diáspora, denunció muertes de civiles que atribuye a las fuerzas salvadoreñas, sin dar una cifra, y pidió una investigación independiente.

Que el gobierno haitiano lo haya pedido y lo apoye pesa contra la idea de invasión; que buena parte del contingente actúe fuera del mando de la ONU es lo que alimenta las críticas.
""")

E("sv-d006", "E15", "hecho", "¿Qué es la Fuerza de Supresión de Pandillas?",
  [[B("Fuerza de Supresión de Pandillas GSF resolución 2793", ["FR-E15-004", "FR-E15-005", "FR-E15-021", "FR-E15-007"])]],
  """
Es la fuerza internacional que hoy combate a las bandas armadas en Haití con aval de la ONU. Se la conoce por sus siglas en inglés, GSF.

Nació el 30 de septiembre de 2025, cuando el Consejo de Seguridad aprobó la resolución 2793. Esa resolución convirtió la misión multinacional que lideraba Kenia en la Fuerza de Supresión de Pandillas, con un periodo inicial de 12 meses. La votación fue de 12 a favor, ninguno en contra y 3 abstenciones: China, Rusia y Pakistán.

Según Diario El Mundo, se aprobó con un mandato para 5.550 efectivos de seguridad y más de 50 empleados civiles. La diferencia de fondo con la misión anterior es que esta puede detener a presuntos pandilleros.

En la práctica le ha costado llenarse. Según Latin Times, en octubre de 2026 tenía desplegadas más de 2.000 tropas de seis países, alrededor del 37 % de lo previsto.

El Salvador es uno de los países que aportan militares, y su papel creció mucho tras la emboscada del 18 de octubre de 2026. ¿Quieres que te cuente esa parte?
""")

E("sv-d007", "E15", "hecho", "¿Qué ley aprobó la Asamblea para lo de Haití?",
  [[B("ley Asamblea Fuerza Armada Haití", ["FR-E15-002", "FR-E15-006", "FR-E15-008"], epoca="E15")]],
  """
Han sido dos leyes, una tras otra.

La primera se aprobó el 19 de diciembre de 2024. Autorizó a la Fuerza Armada de El Salvador a participar en la misión multinacional de apoyo a la seguridad en Haití, la que lideraba Kenia, con aeronaves de ala rotativa, es decir, helicópteros, para evacuaciones médicas. Después la Asamblea la prorrogó un año más.

La segunda llegó cuando la misión cambió de nombre y de mandato. El 29 de septiembre de 2026 la Asamblea aprobó con 57 votos, con dispensa de trámite, la Ley Especial Transitoria para la Participación de la Fuerza Armada de El Salvador en la Fuerza de Supresión de Pandillas en Haití. Esa ley autoriza la participación por 12 meses más, hasta octubre de 2027, prorrogables mientras dure la misión.

La dispensa de trámite quiere decir que se aprobó sin pasar por el estudio normal en comisión, algo que la Asamblea ha hecho a menudo con iniciativas del Ejecutivo.

Ojo con un detalle: esa ley cubre la participación dentro de la fuerza de la ONU. El gran despliegue de finales de octubre, el de más de 2.000 militares, según el vicepresidente Ulloa se apoya en un acuerdo bilateral con Haití. Te lo busco si te interesa.
""")

E("sv-d008", "E15", "hecho", "¿Qué pasó con el estadio en Haití?",
  [[B("estadio Sylvio Cator base operativa", ["FR-E15-015"], epoca="E15")]],
  """
Se trata del estadio Sylvio Cator, en Puerto Príncipe, el principal de Haití y donde jugaba como local la selección haitiana de fútbol.

Según EFE, el 12 de noviembre de 2026 Bukele anunció que, tras una operación conjunta con la Policía Nacional de Haití y fuerzas haitianas, se tomó el control del estadio, que estaba en manos de las bandas desde febrero de 2024. Dijo que allí se instalará una base operativa para seguir avanzando hacia otras zonas controladas por las pandillas.

Bukele también informó que dentro del estadio se encontraron varios cráneos humanos, y aprovechó para amenazar a las pandillas con una ofensiva.

Fíjate que casi todo lo que se sabe de la operación viene del anuncio del propio Bukele y de las fuerzas que participaron. La recuperación del estadio la reportaron varios medios; lo que no tengo es una evaluación independiente de cómo fue la operación ni de su efecto en la zona.

Si quieres, te cuento cómo reaccionó el gobierno haitiano a la presencia salvadoreña, o qué dijo la ONU.
""")

E("sv-d009", "E15", "conflicto", "¿Los soldados salvadoreños están matando civiles en Haití?",
  [[B("muertes de civiles fuerzas salvadoreñas Haití denuncia", ["FR-E15-019", "FR-E15-020"], epoca="E15")],
   [B("respuesta gobierno salvadoreño críticas Haití", ["FR-E15-018", "FR-E15-012"], epoca="E15")]],
  """
Hay una denuncia, pero no está comprobada, y conviene ver quién la hace y qué dice cada parte.

La acusación viene de UNA-Haití, la Asociación de las Naciones Unidas de Haití, un grupo que representa a sectores de la diáspora haitiana. Según la Revista E&N, en una carta al secretario general de la ONU denunció muertes de civiles que atribuye a bombardeos y ataques de las fuerzas salvadoreñas desde el 22 de octubre de 2026 en Croix-des-Bouquets, Canaan y Plaine du Cul-de-Sac. No dio una cifra y pidió una investigación independiente. El artículo no recoge una respuesta directa del gobierno salvadoreño.

Las advertencias de organismos son más generales. El 17 de noviembre la oficina de derechos humanos de la ONU pidió a todo el personal desplegado en Haití priorizar a los civiles y usar la fuerza letal solo como último recurso. Amnistía Internacional pidió a El Salvador y Haití garantizar que las operaciones respeten los derechos humanos.

Desde el oficialismo la respuesta fue de rechazo a ese tipo de críticas: el diputado William Soriano, de Nuevas Ideas, contestó a Amnistía en X con la frase "Los Derechos de Pandilleros". Y Bukele insiste en que su operación no va contra el pueblo haitiano.

En resumen: hay una acusación de un grupo de la diáspora y llamados de prudencia de la ONU y de Amnistía, pero no tengo ninguna investigación que confirme o descarte esas muertes.
""")

E("sv-d010", "E15", "hecho", "¿Qué dijo el gobierno de Haití sobre Bukele?",
  [[B("Fils-Aimé Bukele declaraciones gobierno haitiano", ["FR-E15-013", "FR-E15-014", "FR-E15-016"], epoca="E15")]],
  """
El gobierno de Haití ha sido el principal defensor público del despliegue salvadoreño. Te lo doy en sus palabras y con fecha.

Según EFE, el 3 de noviembre de 2026 el primer ministro Alix Didier Fils-Aimé le agradeció a Bukele "haber comprendido la batalla que libra Haití, que es similar a la que enfrentó contra las pandillas salvadoreñas". Bukele respondió que ayudará a los haitianos a "retomar el país".

Una semana después, el 10 de noviembre, Fils-Aimé afirmó que su gobierno está recuperando el control territorial con el apoyo de las tropas salvadoreñas y de la Fuerza de Supresión de Pandillas, y escribió: "Haití, El Salvador, GSF: ¡el mismo combate, la misma determinación!".

Y el 16 de noviembre, en un acto en San Salvador, el ministro haitiano Patrick Pélissier dijo que Haití quiere que el despliegue continúe, justo cuando el ministro de Seguridad salvadoreño, Gustavo Villatoro, decía que se irán cuando aparezcan los cuatro desaparecidos.

Todo esto es la postura de un gobierno que pidió la ayuda y tiene interés en que funcione. Lo que dicen la ONU y los críticos lo tengo aparte, por si quieres comparar.
""")

E("sv-d011", "E15", "hecho", "¿Cuándo se van a ir las tropas salvadoreñas de Haití?",
  [[B("retirada tropas salvadoreñas Haití", ["FR-E15-016", "FR-E15-006", "FR-E15-007"], epoca="E15")]],
  """
No hay fecha anunciada. Lo que hay es una condición, y además una ley que va más lejos.

La condición la puso el gobierno. Según Euronews, el ministro de Seguridad, Gustavo Villatoro, dijo el 16 de noviembre de 2026 que El Salvador retirará sus más de 2.000 militares cuando localicen a los cuatro desaparecidos: "Si reaparecen mañana, nos iremos de Haití". En el mismo acto, el ministro haitiano Patrick Pélissier dijo que Haití quiere que el despliegue continúe.

La ley es otra cosa. El 29 de septiembre de 2026 la Asamblea aprobó la participación de la Fuerza Armada en la Fuerza de Supresión de Pandillas por 12 meses más, hasta octubre de 2027, prorrogables. Esa ley cubre a los militares que están dentro de la misión de la ONU.

O sea, son dos cosas distintas: el refuerzo grande de finales de octubre, que según el gobierno se va cuando aparezcan los cuatro, y la participación en la fuerza internacional, autorizada hasta octubre de 2027.

Mis datos llegan al 18 de noviembre de 2026; si después hubo un anuncio de retirada, no lo tengo.
""")

E("sv-d012", "E15", "contexto", "¿Desde cuándo Bukele quería meterse en Haití?",
  [[B("Bukele ofrece arreglar crisis Haití", ["FR-E15-001", "FR-E15-002"])],
   [L("E15", ["FR-E15-001", "FR-E15-002", "FR-E15-004", "FR-E15-006", "FR-E15-007", "FR-E15-008"])]],
  """
Bastante antes del despliegue grande. La idea viene por lo menos de 2024.

Según Última Hora, en marzo de 2024 Bukele aseguró que El Salvador podía arreglar la crisis de violencia de Haití si contaba con el visto bueno de las autoridades haitianas y de la ONU, y dijo que era posible acabar con las bandas como lo había hecho con las pandillas en su país.

Después vinieron los pasos formales, en este orden:

- El 19 de diciembre de 2024 una ley autorizó a la Fuerza Armada a participar en la misión que lideraba Kenia, con helicópteros para evacuaciones médicas.
- El 30 de septiembre de 2025 la ONU convirtió esa misión en la Fuerza de Supresión de Pandillas.
- El 29 de septiembre de 2026 la Asamblea extendió la participación salvadoreña hasta octubre de 2027.
- El 18 de octubre de 2026 cuatro aerotécnicos salvadoreños cayeron en una emboscada cerca de Puerto Príncipe.
- A finales de octubre El Salvador envió más de 2.000 militares para buscarlos.

Así que el interés es viejo, pero el salto de escala lo provocó la emboscada. Es lo que el gobierno da como razón principal de la operación actual.
""")

E("sv-d013", "E15", "perspectivas", "¿Qué dice la ONU de los militares salvadoreños en Haití?",
  [[B("ONU militares salvadoreños fuera de la GSF", ["FR-E15-017", "FR-E15-020"], epoca="E15")]],
  """
La ONU ha dicho dos cosas, y ninguna es un respaldo ni una condena directa del despliegue.

La primera es una aclaración de mando. El 2 de noviembre de 2026 la ONU dijo que la gran mayoría de los militares salvadoreños enviados adicionalmente a Haití no forma parte de la Fuerza de Supresión de Pandillas. Por eso quedan fuera de los mecanismos de apoyo y supervisión de su oficina en Haití. El portavoz recordó que toda operación de seguridad en el país debe respetar el derecho internacional de los derechos humanos y el derecho internacional humanitario.

La segunda es un llamado de prudencia. Según Euronews, el 17 de noviembre la Oficina del Alto Comisionado para los Derechos Humanos pidió a todo el personal desplegado en Haití, no solo a los salvadoreños, priorizar la protección de los civiles y usar la fuerza letal solo como último recurso. Amnistía Internacional pidió además que se publique el acuerdo de seguridad entre el gobierno de Bukele y Haití.

Del otro lado, el gobierno salvadoreño presenta la operación como un rescate que no va contra el pueblo haitiano, y el gobierno de Haití la apoya abiertamente. La aclaración de la ONU no contradice eso; lo que deja claro es que esa parte del despliegue es responsabilidad de los dos gobiernos, no de la misión internacional.
""")

E("sv-d014", "E15", "hecho", "¿Hay un acuerdo entre El Salvador y Haití?",
  [[B("acuerdo de cooperación El Salvador Haití", ["FR-E15-023", "FR-E15-020"], epoca="E15")]],
  """
Sí, pero su contenido no se conoce.

Según El Diario de Hoy, el 17 de noviembre de 2026 el Consejo de Ministros de Haití, presidido por el primer ministro Alix Didier Fils-Aimé, aprobó un acuerdo de cooperación con El Salvador. El texto no se ha publicado. Antes, el 5 de noviembre, el vicepresidente Félix Ulloa había dicho que el despliegue salvadoreño se apoya en un acuerdo bilateral con Haití.

Eso importa porque la ONU ya había aclarado que la mayoría de los militares salvadoreños del segundo envío no está bajo la Fuerza de Supresión de Pandillas. Si no están bajo la ONU, la base legal de su presencia es ese acuerdo entre los dos gobiernos.

Por eso Amnistía Internacional, según Euronews, pidió que se haga público el acuerdo de seguridad y que incluya garantías de derechos humanos.

Lo que no puedo decirte es qué dice el acuerdo: cuánto tiempo, qué facultades da a los militares salvadoreños o quién responde si hay abusos. Mientras no se publique, cualquier detalle sería especulación.
""")

E("sv-d015", "E15", "reformulacion", "Bukele va a acabar con las pandillas de Haití igual que en El Salvador, ¿verdad?",
  [[B("Bukele promete acabar pandillas Haití", ["FR-E15-001", "FR-E15-015", "FR-E15-021"], epoca="E15")],
   [B("críticas despliegue salvadoreño Haití", ["FR-E15-017", "FR-E15-019"], epoca="E15")]],
  """
Eso es lo que promete Bukele, pero todavía no se puede saber si lo va a lograr. Te doy lo que hay.

La promesa es vieja. Según Última Hora, en marzo de 2024 Bukele dijo que se podía acabar con las bandas haitianas como lo había hecho con las pandillas en El Salvador. Y el 12 de noviembre de 2026, según EFE, tras la toma del estadio Sylvio Cator anunció una base operativa y amenazó a las pandillas con una ofensiva.

Ahora, las condiciones no son las de El Salvador. Allá el gobierno controla la Asamblea, la Policía y las cárceles de su propio país. En Haití actúa en un país ajeno, con un gobierno que no fue elegido en las urnas: según Latin Times, Haití no tiene un gobierno elegido desde 2016 y aplazó sin fecha las elecciones previstas para diciembre de 2026. Y la propia fuerza de la ONU tenía en octubre alrededor del 37 % de las tropas previstas.

También hay frenos. La ONU aclaró que la mayoría del refuerzo salvadoreño no está bajo su mando, y UNA-Haití denunció muertes de civiles que atribuye a las fuerzas salvadoreñas, sin dar cifras.

Así que lo justo es decir que el gobierno salvadoreño y el haitiano anuncian avances, pero el resultado está por verse.
""")

E("sv-d016", "E15", "reformulacion", "Lo de Haití es puro show de Bukele para la propaganda, no le importan los soldados.",
  [[B("objetivo operación Haití rescate aerotécnicos", ["FR-E15-012", "FR-E15-016"], epoca="E15"),
    B("búsqueda militares desaparecidos estado del caso", ["FR-E15-008", "FR-E15-022"], epoca="E15")]],
  """
Lo que hay en la cabeza de Bukele no lo puedo saber, ni para un lado ni para el otro. Lo que sí puedo es ponerte los hechos y lo que dice cada parte, y que tú saques la conclusión.

Lo que dice el gobierno: según Diario El Mundo, Bukele afirmó que el objetivo principal de la operación es que los cuatro técnicos de aviación vuelvan a El Salvador y que su gobierno paga el 90 % del costo. Su ministro de Seguridad, Gustavo Villatoro, dijo que se irán de Haití cuando aparezcan.

Lo que se ha hecho: tras la emboscada del 18 de octubre de 2026, El Salvador envió más de 2.000 militares con blindados y helicópteros. Eso es un esfuerzo grande y caro para un país pequeño, y apunta a que la búsqueda va en serio.

Lo que alimenta la sospecha de los críticos: el despliegue también se usa para una ofensiva contra las pandillas que Bukele difunde en sus redes, como la toma del estadio Sylvio Cator. Y al cierre de mis datos, el 18 de noviembre de 2026, los cuatro seguían sin aparecer.

Las dos cosas pueden ser ciertas a la vez: un rescate real y una operación con mucha exposición pública. Lo que no tengo es evidencia de que la búsqueda sea falsa.
""")

E("sv-d017", "E15", "conflicto", "¿Están vivos los cuatro militares desaparecidos en Haití?",
  [[B("militares salvadoreños vivos o muertos Haití", ["FR-E15-010", "FR-E15-011", "FR-E15-022"], epoca="E15")]],
  """
No se sabe. Las versiones chocan y ninguna está confirmada, así que te doy cada una con quién la sostiene.

La de Estados Unidos: según la agencia AP, el embajador estadounidense ante la ONU, Mike Waltz, dijo en el Consejo de Seguridad que su gobierno considera que los cuatro sobrevivieron a la emboscada, aunque las fuerzas internacionales no sabían dónde estaban.

La de una pandilla: un cabecilla, Wilson Joseph, alias Lanmò San Jou, le dijo a AP que los cuatro estaban muertos. No dio pruebas y las autoridades salvadoreñas no lo confirmaron.

La del gobierno de Bukele: cuando el 24 de octubre circularon informes de que unos cuerpos podían ser de ellos, Bukele lo rechazó: "No son nuestros hombres". Y el 10 de noviembre el vicepresidente Félix Ulloa reconoció: "No hay rastro de ellos".

El estado al cierre de mis datos: el 18 de noviembre de 2026, al cumplirse un mes, las autoridades no habían confirmado ni el paradero ni el estado de los cuatro.

Cualquier persona que te diga hoy con seguridad si están vivos o muertos está yendo más allá de lo que se sabe públicamente, al menos hasta esa fecha.
""")

E("sv-d018", "E15", "hecho", "What is El Salvador doing in Haiti?",
  [[B("El Salvador troops Haiti", ["FR-E15-004", "FR-E15-007", "FR-E15-008", "FR-E15-017"], epoca="E15")]],
  """
There are two layers to it.

First, El Salvador takes part in the UN-backed Gang Suppression Force (GSF). On 30 September 2025 the Security Council adopted resolution 2793, which turned the Kenya-led mission into the GSF for an initial period of 12 months. The vote was 12 in favour, none against and 3 abstentions: China, Russia and Pakistan.

Second, there is a much larger Salvadoran deployment that began after an ambush. On Sunday 18 October 2026 four Salvadoran aviation technicians from Task Force Libertad II were ambushed by armed groups in Santo, in Croix-des-Bouquets, about 12 kilometres from Port-au-Prince. According to the Salvadoran armed forces, they left their armoured vehicle, which was set on fire, and contact with them was lost.

In late October El Salvador sent more than 2,000 troops, with armoured vehicles and helicopters, to search for them. The first reinforcements arrived on 22 October, and on 28 October the Foreign Ministry confirmed the contingent exceeded that number.

The UN drew a line: on 2 November it said that the great majority of these additional Salvadoran troops are not part of the GSF, so they fall outside its support and oversight mechanisms.

As of 18 November 2026, the four technicians had not been found. I don't have anything after that date.
""", idioma="en")

E("sv-d019", "E15", "perspectivas", "Is Bukele invading Haiti?",
  [[B("Bukele not an invasion Haiti statements", ["FR-E15-012", "FR-E15-014", "FR-E15-019"], epoca="E15")]],
  """
That is the dispute, and the answer depends on who you ask.

Bukele's government says no. According to Diario El Mundo, on 29 October 2026 Bukele said the operation is not against the Haitian people nor an invasion of Haiti. He said the main goal is to bring the four aviation technicians home and that his government covers 90 % of the cost, with other countries providing some logistics.

Haiti's government backs it. According to EFE, on 10 November 2026 Prime Minister Alix Didier Fils-Aimé said his government is regaining territorial control with the support of Salvadoran troops and the Gang Suppression Force, and wrote: "Haiti, El Salvador, GSF: the same fight, the same determination!"

Critics raise concerns. UNA-Haiti, a group representing parts of the Haitian diaspora, accused Salvadoran forces of killing civilians since 22 October 2026, without giving a figure, and asked for an independent UN investigation. The UN, for its part, clarified that most of the extra Salvadoran troops operate outside its force.

An invasion usually means entering a country without its government's consent. Here the Haitian government invited and supports the deployment, which weighs against that label. What critics question is the lack of UN oversight and a cooperation agreement whose text has not been published.
""", idioma="en")

E("sv-d020", "E15", "hecho", "Hazme una línea de tiempo de lo de Haití.",
  [[L("E15", ["FR-E15-001", "FR-E15-002", "FR-E15-004", "FR-E15-006", "FR-E15-007", "FR-E15-008",
              "FR-E15-017", "FR-E15-015", "FR-E15-016", "FR-E15-023", "FR-E15-022"])]],
  """
Aquí la tienes, con los hitos que están documentados:

- Marzo de 2024: Bukele dice que El Salvador podría arreglar la crisis de violencia de Haití con el visto bueno de Haití y de la ONU.
- 19 de diciembre de 2024: una ley autoriza a la Fuerza Armada a participar en la misión liderada por Kenia, con helicópteros para evacuaciones médicas.
- 30 de septiembre de 2025: la ONU aprueba la resolución 2793 y nace la Fuerza de Supresión de Pandillas.
- 29 de septiembre de 2026: la Asamblea extiende la participación salvadoreña hasta octubre de 2027, prorrogable.
- 18 de octubre de 2026: emboscada contra cuatro aerotécnicos salvadoreños en Santo, Croix-des-Bouquets.
- 22 de octubre: llegan los primeros refuerzos a Puerto Príncipe.
- 28 de octubre: la Cancillería confirma más de 2.000 militares desplegados.
- 2 de noviembre: la ONU aclara que la mayoría del refuerzo no está bajo su fuerza; ese mismo día se recupera el vehículo incendiado.
- 12 de noviembre: Bukele anuncia la toma del estadio Sylvio Cator y una base operativa allí.
- 16 de noviembre: el ministro Villatoro dice que se irán cuando aparezcan los cuatro.
- 17 de noviembre: Haití aprueba un acuerdo de cooperación con El Salvador, sin publicar su texto.
- 18 de noviembre: al cumplirse un mes, los cuatro siguen sin aparecer.

Mis datos llegan hasta esa última fecha.
""")

E("sv-d021", "E15", "hecho", "¿Por qué El Salvador ya tenía militares en Haití antes de la emboscada?",
  [[B("participación salvadoreña misión Kenia evacuaciones médicas", ["FR-E15-002", "FR-E15-003", "FR-E15-004", "FR-E15-007", "FR-E15-008"], epoca="E15")]],
  """
Porque ya participaba en la misión internacional desde antes, con un papel pequeño y muy concreto.

El 19 de diciembre de 2024 la Asamblea aprobó una ley que autorizó a la Fuerza Armada a participar en la misión multinacional de apoyo a la seguridad en Haití, la que lideraba Kenia, con aeronaves de ala rotativa para evacuaciones médicas. Según la Voz de América, el primer contingente salvadoreño fue de 70 soldados dedicados a esas evacuaciones.

Luego la misión cambió. El 30 de septiembre de 2025 el Consejo de Seguridad aprobó la resolución 2793, que la convirtió en la Fuerza de Supresión de Pandillas, con un periodo inicial de 12 meses y la facultad de detener a presuntos pandilleros. El Salvador siguió dentro.

Los cuatro aerotécnicos emboscados el 18 de octubre de 2026 eran justamente parte de ese esquema: técnicos de la Fuerza de Tarea Libertad II, ligados al apoyo aéreo, no tropas de combate.

Por eso la operación grande de finales de octubre es distinta: ya no es apoyo médico dentro de la fuerza de la ONU, sino un despliegue de más de 2.000 militares que, según la ONU, en su mayoría queda fuera de esa fuerza.
""")

E("sv-d022", "E15", "multiple", "¿Qué tiene que ver lo de Haití con el régimen de excepción en El Salvador?",
  [[B("Bukele compara Haití con El Salvador pandillas", ["FR-E15-001", "FR-E15-013"], epoca="E15")],
   [B("régimen de excepción origen y resultados", ["FR-E10-002", "FR-E11-004", "FR-E14-006"])]],
  """
La conexión la hacen los propios gobiernos: presentan Haití como la misma guerra que El Salvador libró contra las maras.

Según Última Hora, en marzo de 2024 Bukele dijo que se podía acabar con las bandas haitianas como él lo había hecho con las pandillas salvadoreñas. Y según EFE, el 3 de noviembre de 2026 el primer ministro haitiano, Alix Didier Fils-Aimé, le agradeció "haber comprendido la batalla que libra Haití, que es similar a la que enfrentó contra las pandillas salvadoreñas".

Lo que El Salvador lleva a Haití como carta de presentación es el régimen de excepción. Recuerda cómo empezó: el 27 de marzo de 2022 la Asamblea lo aprobó a petición de Bukele, tras un fin de semana de asesinatos. Según las cifras oficiales citadas por Diario El Mundo, los homicidios bajaron de 1.211 en 2021 a 82 en 2025.

Pero ese modelo también arrastra críticas. Según Cristosal, el gobierno tiene al menos 86 presos políticos y miles de inocentes cayeron en las detenciones masivas, algo que el gobierno rechaza.

La diferencia es grande: en El Salvador el régimen de excepción descansa en leyes y cárceles propias. En Haití las tropas salvadoreñas actúan en un país ajeno, con un acuerdo bilateral cuyo texto no se ha publicado. Si quieres, comparo las dos cosas punto por punto.
""")

E("sv-d023", "E15", "sin_datos", "¿Cuánto le está costando a El Salvador la operación en Haití?",
  [[C("costo_operacion_haiti", [])],
   [B("costo operación Haití financiamiento", ["FR-E15-012"], epoca="E15")]],
  """
No tengo una cifra del costo. La tabla de cifras no trae esa métrica y en los documentos nadie da un monto en dólares.

Lo único que hay es una proporción que da el propio gobierno: según Diario El Mundo, Bukele dijo que El Salvador cubre el 90 % de los gastos de la operación y que otros países aportan parte de la logística. Es su versión; no he visto un presupuesto publicado que la respalde ni que la contradiga.

Si sale un dato oficial del Ministerio de Hacienda o de la Defensa, ahí estaría la respuesta.
""")

E("sv-d024", "E15", "hecho", "Busca en mis documentos si tengo algo sobre Haití.",
  [[B("Haití", [], coleccion="privada")],
   [B("Haití despliegue salvadoreño", ["FR-E15-007", "FR-E15-008", "FR-E15-022"], coleccion="publica", epoca="E15")]],
  """
En tus documentos privados no hay nada sobre Haití. Busqué en la colección privada y no salió ningún resultado.

Donde sí hay material es en la colección pública. Lo central es esto:

El domingo 18 de octubre de 2026 cuatro aerotécnicos salvadoreños de la Fuerza de Tarea Libertad II sufrieron una emboscada de grupos armados en Santo, una localidad de Croix-des-Bouquets, a unos 12 kilómetros de Puerto Príncipe. Según la Fuerza Armada, salieron del vehículo blindado, que fue incendiado, y se perdió el contacto con ellos.

A finales de octubre El Salvador envió a Haití más de 2.000 militares, con blindados y helicópteros, para buscarlos. Los primeros refuerzos llegaron el 22 de octubre y el 28 la Cancillería confirmó la cifra.

Al cumplirse un mes, el 18 de noviembre de 2026, las autoridades no habían confirmado ni el paradero ni el estado de los cuatro. El 2 de noviembre se recuperó el vehículo incendiado y el 10 de noviembre el vicepresidente Félix Ulloa dijo: "No hay rastro de ellos".

Si tienes informes o notas propias sobre el tema, guárdalos en la carpeta de documentos privados y los incluyo en la próxima búsqueda.
""")

E("sv-d025", "E15", "hecho", "oye y lo de haiti como va?",
  [[B("Haití situación actual despliegue salvadoreño", ["FR-E15-015", "FR-E15-016", "FR-E15-022", "FR-E15-023"], epoca="E15")]],
  """
Te doy cómo estaba al cierre de mis datos, el 18 de noviembre de 2026.

Los cuatro aerotécnicos emboscados el 18 de octubre seguían sin aparecer. Las autoridades no habían confirmado su paradero ni su estado; el vicepresidente Félix Ulloa dijo el 10 de noviembre que no había rastro de ellos.

En el terreno, el 12 de noviembre Bukele anunció, según EFE, que tras una operación conjunta con la Policía de Haití se tomó el control del estadio Sylvio Cator de Puerto Príncipe, en manos de las bandas desde febrero de 2024, y que allí se instalará una base operativa.

En lo político, el 16 de noviembre el ministro de Seguridad, Gustavo Villatoro, dijo que El Salvador retirará sus más de 2.000 militares cuando aparezcan los cuatro, mientras el ministro haitiano Patrick Pélissier dijo que Haití quiere que se queden. Y según El Diario de Hoy, el 17 de noviembre el gobierno de Haití aprobó un acuerdo de cooperación con El Salvador cuyo texto no se ha publicado.

Lo que haya pasado después no lo tengo. ¿Te interesa algún punto en particular, como lo que dice la ONU o las denuncias de los críticos?
""")

guardar("ejemplos_lote_d.jsonl")
