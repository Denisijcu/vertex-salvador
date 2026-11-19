"""
ejemplos_lote_b.py — Ejemplos de entrenamiento, lote B: de 2012 a 2026 (E06–E14, T01, T03).
Uso (desde E:\\vertex-salvador):  python ejemplos_lote_b.py  ->  datos\\ejemplos_lote_b.jsonl
"""
from ejemplos_base import B, C, E, guardar

E("sv-b001", "T01", "hecho", "¿Quién es Nayib Bukele?",
  [[B("Nayib Bukele biografía trayectoria", ["FR-T01-001", "FR-T01-002", "FR-E06-001", "FR-E07-001"], epoca="T01")]],
  """
Nayib Bukele es el presidente de El Salvador y una de las figuras políticas más conocidas de América Latina en esta década.

Según su biografía en Wikipedia, nació el 24 de julio de 1981 en San Salvador. Es hijo del empresario Armando Bukele Kattán, que murió en 2015, y de Olga Marina Ortez, y estudió en la Universidad Centroamericana sin terminar la carrera.

Su carrera política empezó en lo local. En 2012, con 31 años, ganó la alcaldía de Nuevo Cuscatlán como miembro del FMLN, y en 2015 la de San Salvador, que ejerció hasta 2018. Después saltó a la presidencia: el 3 de febrero de 2019 ganó en primera vuelta con el 53 % de los votos, rompiendo treinta años de alternancia entre ARENA y el FMLN.

Según un perfil de BBC Mundo, quienes lo conocen destacan su inteligencia, su capacidad de innovar y su conocimiento de los problemas del país, y lo describen como alguien difícil de encasillar: fue alcalde por un partido de izquierda y llegó a la presidencia con GANA, de derecha.

Su gobierno es conocido sobre todo por la guerra contra las pandillas, que tiene defensores y críticos. Si quieres, te cuento qué dice cada lado.
""")

E("sv-b002", "E06", "hecho", "¿Bukele era del FMLN? ¿Por qué se fue?",
  [[B("Bukele FMLN expulsión Nuevas Ideas", ["FR-E06-001", "FR-E06-002"], epoca="E06")]],
  """
Sí, Bukele empezó su carrera política en el FMLN, el partido que nació de la antigua guerrilla.

En 2012, con 31 años, fue elegido alcalde del pequeño municipio de Nuevo Cuscatlán, junto a San Salvador, como miembro del FMLN. En 2015 ganó con el mismo partido la alcaldía de la capital, San Salvador, y la ejerció hasta 2018.

No se fue por su cuenta: lo expulsaron. Las diferencias con la dirección del FMLN terminaron con su expulsión del partido en 2017. Ese mismo año fundó su propio movimiento, Nuevas Ideas, que al principio no pudo inscribirse como partido porque no cumplía los requisitos de la ley electoral. Por eso, para las elecciones de 2019 se presentó con otro partido, GANA.

Es una de las paradojas de su trayectoria: llegó a la presidencia derrotando tanto al FMLN, el partido que lo lanzó, como a ARENA, su rival histórico. Sobre los motivos exactos de la expulsión no tengo detalle en estos fragmentos; si te interesa, puedo buscarlo.
""")

E("sv-b003", "E07", "hecho", "¿Cómo ganó Bukele las elecciones de 2019?",
  [[B("elección presidencial 2019 resultados Bukele", ["FR-E07-001", "FR-E06-002"], epoca="E07")]],
  """
Ganó en primera vuelta y de forma amplia, algo que no se veía en El Salvador desde hacía mucho.

La elección fue el 3 de febrero de 2019. Bukele se presentó como candidato de GANA, porque su propio movimiento, Nuevas Ideas, no había podido inscribirse como partido a tiempo. Obtuvo el 53 % de los votos válidos, lo que le permitió evitar la segunda vuelta. El segundo, Carlos Calleja, de ARENA, quedó en torno al 32 %.

El dato político más importante es que rompió treinta años de alternancia entre ARENA y el FMLN, los dos partidos que habían gobernado desde el final de la guerra. Bukele venía precisamente del FMLN, del que había sido expulsado en 2017, y se presentó como una alternativa a los dos. Ese resultado cambió el mapa político del país, que hasta entonces se repartían esos dos partidos.

Si quieres, te busco qué pasó después con su plan de seguridad, que fue la gran apuesta de su primer gobierno.
""")

E("sv-b004", "E07", "hecho", "¿Qué es el Plan Control Territorial?",
  [[B("Plan Control Territorial seguridad 2019", ["FR-E07-002", "FR-E07-003", "FR-E08-001"], epoca="E07")]],
  """
El Plan Control Territorial es la estrategia de seguridad contra las pandillas con la que Bukele empezó su gobierno.

Bukele asumió la presidencia el 1 de junio de 2019 y el 20 de junio puso en marcha el plan. El gobierno le atribuye la baja de los homicidios que hubo desde junio de 2019.

Según un balance de EFE publicado por Primicias, Bukele logró acentuar la disminución de los homicidios que había empezado en 2016 y, de acuerdo con las autoridades, quitó a las pandillas el control de los barrios populares. Ese mismo balance recuerda que, hasta mayo de 2021, su mandato estuvo marcado por los choques con una Asamblea de mayoría opositora y con la Sala de lo Constitucional.

El plan también estuvo en el centro de una de las crisis más sonadas de su gobierno. El 9 de febrero de 2020 Bukele entró en la Asamblea Legislativa acompañado de militares y policías armados para presionar a los diputados a aprobar un préstamo de 109 millones de dólares para la fase III del plan.

Así que es, a la vez, la base de su política de seguridad y el origen de un choque institucional que todavía se discute.
""")

E("sv-b005", "E08", "hecho", "¿Qué pasó el 9F?",
  [[B("9 de febrero de 2020 militares Asamblea", ["FR-E08-001", "FR-E08-002", "FR-E08-003"], epoca="E08")]],
  """
El 9F es como se conoce en El Salvador lo que pasó el 9 de febrero de 2020 en la Asamblea Legislativa.

Ese día Bukele entró en el edificio acompañado de militares y policías armados. Quería presionar a los diputados, que entonces eran mayoría de oposición, para que aprobaran un préstamo de 109 millones de dólares destinado a la fase III del Plan Control Territorial, su estrategia contra las pandillas. Se sentó en la silla del presidente de la Asamblea y rezó en el Salón Azul, la sala de sesiones.

Según EFE, la sesión extraordinaria que el propio Bukele había convocado no pudo celebrarse por falta de quórum, porque solo se presentaron 20 diputados. Ante sus seguidores, que se habían concentrado fuera, Bukele dio una semana a los legisladores para aprobar el préstamo.

El episodio provocó una fuerte polémica dentro y fuera del país, y todavía se discute cómo debe llamarse: según la Revista E&N, para un diputado de la oposición fue una toma a la fuerza del Parlamento, y un diputado de GANA, aliado del gobierno, sostuvo que nunca hubo un intento de golpe. Si quieres, te cuento esas dos versiones con detalle.
""")

E("sv-b006", "E08", "conflicto", "¿Lo del 9F fue un intento de golpe de Estado?",
  [[B("9F interpretaciones golpe de Estado Asamblea", ["FR-E08-001", "FR-E08-003"], epoca="E08")]],
  """
Esa es justamente la parte en la que no hay acuerdo, y conviene separar lo que pasó de cómo lo llama cada lado.

Lo que está documentado: el 9 de febrero de 2020 Bukele entró en la Asamblea Legislativa con militares y policías armados para presionar a los diputados, entonces de mayoría opositora, a aprobar un préstamo de 109 millones de dólares para su plan de seguridad. Se sentó en la silla del presidente de la Asamblea y rezó en el Salón Azul.

Las interpretaciones chocan. Según la Revista E&N, para un diputado de la oposición, del PCN, lo ocurrido fue una toma a la fuerza de la Asamblea con intención de disolverla. En cambio, el diputado Guillermo Gallegos, de GANA, aliado del gobierno de Bukele, sostuvo que nunca se intentó un golpe de Estado y llamó absurdo conmemorar esa fecha.

Así que no te puedo dar un veredicto: llamarlo así o no es una postura política. Lo que sí puedo darte son los hechos documentados, para que saques tu propia conclusión.
""")

E("sv-b007", "E09", "hecho", "¿Qué pasó el 1 de mayo de 2021 en El Salvador?",
  [[B("1 de mayo 2021 destitución Sala de lo Constitucional fiscal", ["FR-E09-001", "FR-E09-003"], epoca="E09")]],
  """
Ese día cambió el equilibrio de poderes en El Salvador.

El 1 de mayo de 2021, en su primera sesión, la nueva Asamblea Legislativa, donde Nuevas Ideas tenía mayoría tras las elecciones del 28 de febrero, destituyó a los cinco magistrados de la Sala de lo Constitucional y al fiscal general, Raúl Melara. Esa misma noche nombró a sus sustitutos. La destitución se aprobó con 64 votos a favor y 19 en contra.

La reacción fue inmediata. Media hora después, la Sala saliente declaró inconstitucional su propia destitución, aunque eso no la detuvo: esa misma noche los nuevos magistrados ya estaban nombrados. En el exterior, la OEA rechazó las destituciones y el secretario de Estado de Estados Unidos, Antony Blinken, le expresó a Bukele una profunda preocupación.

Sobre los motivos de la destitución hay dos versiones enfrentadas, la de Nuevas Ideas y la de quienes la rechazaron; si quieres, te cuento los argumentos de cada lado.
""")

E("sv-b008", "E09", "perspectivas", "¿Por qué destituyeron a los magistrados de la Sala de lo Constitucional?",
  [[B("motivos destitución magistrados 2021", ["FR-E09-001", "FR-E09-002", "FR-E09-003"], epoca="E09")]],
  """
Hay dos explicaciones enfrentadas: la de quienes tomaron la decisión y la de quienes la rechazaron.

El hecho es este: el 1 de mayo de 2021, la nueva Asamblea Legislativa, con mayoría de Nuevas Ideas, destituyó a los cinco magistrados de la Sala de lo Constitucional y al fiscal general, y los sustituyó esa misma noche.

La versión del oficialismo: según El Financiero, la iniciativa de Nuevas Ideas sostenía que los magistrados habían actuado contra la Constitución al anteponer intereses particulares a la salud de la población durante la pandemia. Es decir, presentaron la destitución como una respuesta a fallos que, a su juicio, habían bloqueado las medidas sanitarias del gobierno.

La otra versión: la Sala saliente declaró inconstitucional su destitución media hora después, la OEA la rechazó y el secretario de Estado de Estados Unidos, Antony Blinken, expresó a Bukele una profunda preocupación.

Es decir, el oficialismo presenta la destitución como una corrección a fallos que considera contrarios a la Constitución, y la Sala saliente, la OEA y Washington la vieron como una decisión grave. Con estos documentos no puedo darte un veredicto sobre quién tenía razón.
""")

E("sv-b009", "E09", "hecho", "Si la Constitución prohíbe la reelección, ¿cómo pudo Bukele reelegirse?",
  [[B("reelección presidencial Bukele Constitución resolución 2021", ["FR-E09-004", "FR-E12-001", "FR-E09-001"], epoca="E09")]],
  """
Por una resolución judicial que reinterpretó la prohibición, y es uno de los puntos más discutidos de su gobierno.

La Constitución salvadoreña prohíbe la reelección presidencial inmediata. Pero en 2021 la Corte Suprema de Justicia habilitó a Bukele a presentarse de nuevo, y el Tribunal Supremo Electoral aceptó su candidatura. Esa resolución llegó el mismo año en que la nueva Asamblea, el 1 de mayo de 2021, había destituido a los magistrados de la Sala de lo Constitucional y los había sustituido.

Con esa habilitación, Bukele se presentó y ganó con mucha diferencia. El 4 de febrero de 2024 fue reelegido con 2.701.725 votos, el 84,65 % de los votos válidos, según el Tribunal Supremo Electoral, y su partido, Nuevas Ideas, ganó 54 de los 60 escaños de la Asamblea.

Así que hay dos planos. En lo legal, sus partidarios dicen que se presentó con permiso de la máxima autoridad judicial y del tribunal electoral. En lo constitucional, sus críticos sostienen que ese permiso contradice el texto de la Constitución. El resultado electoral, en cambio, no está en discusión: ganó con una mayoría muy amplia.
""")

E("sv-b010", "E09", "conflicto", "¿Es verdad que el gobierno de Bukele pactó con las pandillas?",
  [[B("negociación del gobierno de Bukele con pandillas sanciones Tesoro", ["FR-E09-005", "FR-E09-006", "FR-E10-003"])]],
  """
Hay acusaciones serias y una negativa firme del gobierno, y con lo que tengo no puedo darlo por probado ni por descartado.

La acusación más fuerte viene de Estados Unidos. Según el Departamento del Tesoro, que el 8 de diciembre de 2021 sancionó a Osiris Luna, director de Centros Penales, y a Carlos Marroquín, director de Reconstrucción del Tejido Social, ambos dirigieron en 2020 reuniones promovidas por el gobierno de Bukele para pactar una tregua secreta con líderes pandilleros.

El periódico El Faro fue más allá. Según una investigación suya recogida por Telemundo, la ola de asesinatos de marzo de 2022, que llevó al régimen de excepción, se desató por la supuesta ruptura de un pacto entre el gobierno y la MS-13.

El gobierno lo niega. Según La Prensa de Panamá, el gobierno de Bukele rechaza haber pactado con las pandillas, y en 2021 se había negado a extraditar a Estados Unidos a líderes de la MS-13 reclamados por la justicia de Nueva York.

Lo que sí es un hecho es que hay dos altos funcionarios sancionados por Washington por ese motivo. Si hubo o no un acuerdo, y qué incluía, es lo que sigue en disputa.
""")

E("sv-b011", "E10", "hecho", "¿Por qué se decretó el régimen de excepción?",
  [[B("régimen de excepción marzo 2022 homicidios", ["FR-E10-001", "FR-E10-002", "FR-E10-004"], epoca="E10")]],
  """
Se decretó después del fin de semana más violento que El Salvador había vivido desde el final de la guerra.

Entre el 25 y el 27 de marzo de 2022 hubo 87 homicidios en el país, y solo el sábado 26 se registraron 62. La Policía y el gobierno atribuyeron esa ola de asesinatos a la MS-13.

La respuesta fue inmediata. El 27 de marzo de 2022 la Asamblea Legislativa aprobó, a petición de Bukele, un régimen de excepción de 30 días por las graves perturbaciones del orden público causadas por grupos delincuenciales. Votaron a favor 67 de los 84 diputados.

El régimen de excepción suspende garantías como la inviolabilidad de las comunicaciones y el derecho a la defensa de los detenidos, y amplía la detención administrativa a 15 días. Aunque se aprobó por un mes, la Asamblea lo ha prorrogado cada 30 días desde entonces, y se convirtió en la base de la ofensiva del gobierno contra las pandillas.

Sobre por qué las pandillas desataron esa ola de violencia hay versiones distintas, incluida la de un supuesto pacto roto con el gobierno, que este niega. Si quieres, te las cuento.
""")

E("sv-b012", "E10", "hecho", "¿Qué derechos suspende el régimen de excepción?",
  [[B("garantías suspendidas régimen de excepción", ["FR-E10-004", "FR-E14-001", "FR-E14-006"], epoca="E10")]],
  """
El régimen de excepción suspende varias garantías constitucionales que normalmente protegen a cualquier persona frente al Estado.

En concreto, suspende la inviolabilidad de las comunicaciones, lo que permite intervenirlas, y el derecho a la defensa de los detenidos. Además, amplía la detención administrativa a 15 días, es decir, el tiempo que una persona puede estar detenida antes de pasar ante un juez.

Se aprobó en marzo de 2022 por 30 días, pero la Asamblea lo ha ido prorrogando cada 30 días desde entonces. El 24 de junio de 2026 aprobó la prórroga número 52, cuando la medida ya llevaba más de cuatro años en vigor sin interrupción.

Esto es lo que divide las opiniones. Para el gobierno y sus partidarios, esas facultades han sido necesarias para desarticular a las pandillas. Para organizaciones de derechos humanos como Cristosal, en las detenciones masivas cayeron miles de inocentes. Si quieres, te busco qué dicen exactamente unos y otros, con sus cifras.
""")

E("sv-b013", "E11", "hecho", "¿Qué es el CECOT?",
  [[B("CECOT Centro de Confinamiento del Terrorismo", ["FR-E11-001", "FR-E11-002", "FR-E13-001"], epoca="E11")]],
  """
El CECOT es la megacárcel que el gobierno de Bukele construyó para encerrar a los pandilleros detenidos bajo el régimen de excepción.

Su nombre completo es Centro de Confinamiento del Terrorismo. Está en Tecoluca, en el departamento de San Vicente, y se construyó entre julio de 2022 y enero de 2023. Abrió a finales de enero de 2023 con capacidad para 40.000 presos, lo que la convierte en la cárcel más grande de América Latina. Recibió a sus primeros 2.000 reclusos el 24 de febrero de 2023.

Lo que no se sabe con precisión es cuántas personas hay dentro. Según Centroamérica 360, las autoridades no han dado cifras oficiales actualizadas, y en octubre de 2023 se dijo que operaba al 30 % de su capacidad.

El CECOT se ha convertido en el símbolo de la política de seguridad de Bukele, tanto para quienes la admiran como para quienes la critican. Si te interesa, puedo buscarte qué relación tiene con los deportados que Estados Unidos envió a El Salvador en 2025.
""")

E("sv-b014", "E11", "sin_datos", "¿Cuántos presos hay ahora mismo en el CECOT?",
  [[B("número actual de presos en el CECOT", ["FR-E11-002", "FR-E11-001"], epoca="E11")]],
  """
No tengo esa cifra, y por lo que encuentro tampoco es pública.

Según Centroamérica 360, las autoridades no han dado cifras oficiales actualizadas de cuántos presos hay en el CECOT. El último dato que aparece en mis documentos es de octubre de 2023, cuando se dijo que la cárcel operaba al 30 % de su capacidad.

Lo que sí sé es la capacidad: 40.000 presos. Y que el 24 de febrero de 2023 llegaron los primeros 2.000 reclusos.

No voy a calcularte un número a partir de esos datos, porque sería una estimación mía sin fuente. Si encuentras un comunicado oficial reciente, una nota de prensa o un informe con la cifra, pásamelo o guárdalo en tus documentos y lo busco ahí.
""")

E("sv-b015", "E11", "hecho", "Dame los homicidios de cada año desde 2021.",
  [[C("homicidios", [("2021", "1.211", "cifras oficiales", "FR-E11-004"),
                     ("2022", "615", "cifras oficiales", "FR-E11-004"),
                     ("2023", "194", "cifras oficiales", "FR-E11-004"),
                     ("2024", "114", "cifras oficiales", "FR-E11-004"),
                     ("2025", "82", "cifras oficiales", "FR-E11-004"),
                     ("enero-octubre de 2026", "48", "Policía Nacional Civil", "FR-E14-003")], desde="2021")]],
  """
Estas son las cifras oficiales, y conviene tener presente que las da el propio gobierno.

Según las cifras oficiales de violencia citadas por Diario El Mundo, hubo 1.211 homicidios en 2021. En 2022, el año en que empezó el régimen de excepción, bajaron a 615, según esas mismas cifras oficiales. Siguieron cayendo después, también según los datos del gobierno: 194 en 2023, 114 en 2024 y 82 en 2025.

Para este año, según los reportes oficiales de la Policía Nacional Civil citados por El Diario de Hoy, hubo 48 homicidios entre enero y octubre de 2026, y solo cuatro en octubre en todo el país.

Son caídas enormes en muy poco tiempo, y por eso son el principal argumento del gobierno a favor de su política de seguridad. Lo único que te advierto es que no tengo en mis documentos una serie independiente para comparar: estas cifras son oficiales y no han sido auditadas por un tercero en lo que encontré. Si necesitas citarlas, ponlas siempre como «según cifras oficiales».
""")

E("sv-b016", "E11", "contexto", "¿La baja de los homicidios es gracias al régimen de excepción?",
  [[B("causas de la caída de homicidios régimen de excepción", ["FR-E11-005", "FR-E11-006", "FR-E07-003", "FR-E11-004"], epoca="E11")]],
  """
Es la pregunta del millón, y las fuentes dan matices distintos, aunque todas coinciden en que la caída es muy grande.

La caída en sí la muestran las cifras oficiales: según Diario El Mundo, los homicidios pasaron de 1.211 en 2021 a 615 en 2022, año en que empezó el régimen, y a 82 en 2025.

El gobierno lo atribuye a su política. Según EFE, Bukele y su gabinete de Seguridad sostienen que el régimen permitió combatir a las maras, liberar los territorios que dominaban y reducir mucho los homicidios.

Pero hay dos matices importantes. La misma nota de EFE recuerda que El Salvador ya venía con bajas sostenidas de asesinatos desde 2016. Y el propio Bukele, según Diario El Mundo, explicó en X que la disminución empezó antes del régimen y se acentuó a partir de 2022.

Así que lo más preciso es esto: la tendencia a la baja venía de antes, el gobierno de Bukele la aceleró y el régimen de excepción coincidió con la caída más fuerte. Cuánto pesa cada factor no se puede medir con exactitud con estos datos.
""")

E("sv-b017", "E12", "hecho", "¿Con cuánto ganó Bukele la reelección de 2024?",
  [[B("resultados elecciones 2024 participación", ["FR-E12-001", "FR-E12-003", "FR-E12-002"], epoca="E12")]],
  """
Ganó con uno de los porcentajes más altos que se recuerdan en la región, aunque con una participación que conviene mirar.

El 4 de febrero de 2024 Bukele fue reelegido con 2.701.725 votos, el 84,65 % de los votos válidos, según el Tribunal Supremo Electoral. Su partido, Nuevas Ideas, ganó además 54 de los 60 escaños de la Asamblea Legislativa.

Esa Asamblea era más pequeña que la anterior. En junio de 2023 se había aprobado, a propuesta de Bukele, reducir los diputados de 84 a 60 y los municipios de 262 a 44.

El otro dato es la participación. Según El Diario de Hoy, de los 6.214.399 salvadoreños habilitados para votar, más de 2,9 millones no votaron. Con eso, los votos de Bukele equivalen al 43,48 % del padrón electoral.

Las dos lecturas son posibles: sus partidarios destacan el aplastante 84,65 % de los votos emitidos, y sus críticos subrayan que menos de la mitad del padrón lo votó. Ninguna de las dos cambia el resultado: ganó con una mayoría enorme entre quienes votaron.
""")

E("sv-b018", "E12", "perspectivas", "¿Fue legal la reelección de Bukele?",
  [[B("legalidad de la reelección de Bukele críticas", ["FR-E09-004", "FR-E12-004", "FR-E09-003"])]],
  """
Depende de a quién le preguntes, porque aquí chocan una resolución judicial y el texto de la Constitución.

El punto de partida es este: la Constitución salvadoreña prohíbe la reelección presidencial inmediata. Pero en 2021 la Corte Suprema de Justicia habilitó a Bukele a presentarse de nuevo, y el Tribunal Supremo Electoral aceptó su candidatura.

Para el gobierno y sus partidarios, la reelección fue legal porque la autorizaron la máxima autoridad judicial y el tribunal electoral.

Para sus críticos, el problema está en cómo se llegó a esa resolución. Ese mismo año, la Asamblea controlada por Nuevas Ideas había destituido a los magistrados de la Sala de lo Constitucional, y esa decisión ya había sido rechazada por la OEA y había preocupado al gobierno de Estados Unidos. Según CISPES, una organización de solidaridad crítica del gobierno, sindicatos, grupos de víctimas y organizaciones comunitarias califican el gobierno de Bukele de inconstitucional.

No te puedo dar un fallo definitivo sobre algo que es, en el fondo, una disputa sobre quién interpreta la Constitución. Lo que sí puedo decirte es que la reelección se apoyó en una resolución judicial y que esa resolución es la que está en discusión.
""")

E("sv-b019", "E13", "hecho", "¿Por qué El Salvador recibió a deportados venezolanos en el CECOT?",
  [[B("deportados venezolanos CECOT Ley de Enemigos Extranjeros 2025", ["FR-E13-001", "FR-E13-002"], epoca="E13")]],
  """
Fue parte de un acuerdo entre los gobiernos de Bukele y de Donald Trump.

El 15 de marzo de 2025 Trump invocó la Ley de Enemigos Extranjeros de 1798 contra la banda venezolana Tren de Aragua. Aunque el juez federal James Boasberg había prohibido esos vuelos mientras decidía el caso, ese mismo día llegaron a El Salvador 238 deportados, 23 de ellos salvadoreños señalados como pandilleros de la MS-13. Los recluyeron en el CECOT.

A cambio, El Salvador recibió dinero. Según la Casa Blanca, Washington pagó aproximadamente 6 millones de dólares al gobierno de Bukele por recluir a esos deportados durante un año. El acuerdo lo cerraron Bukele y el secretario de Estado, Marco Rubio, y su texto no se ha hecho público.

El caso fue muy polémico, sobre todo por el uso de una ley de 1798 y porque los vuelos salieron pese a la orden del juez. Si te interesa, puedo buscarte qué pasó después con esos deportados, aunque no lo tengo en estos fragmentos.
""")

E("sv-b020", "E13", "perspectivas", "¿Qué es la Ley de Agentes Extranjeros?",
  [[B("Ley de Agentes Extranjeros 2025 impuesto ONG", ["FR-E13-003", "FR-E13-004", "FR-E13-005"], epoca="E13")]],
  """
Es una ley que regula a las organizaciones que reciben dinero del extranjero, y es una de las más criticadas del gobierno de Bukele.

La Asamblea la aprobó el 20 de mayo de 2025 con 57 votos. Obliga a las personas y organizaciones que reciben fondos del exterior a inscribirse en un Registro de Agentes Extranjeros, conocido como RAEX, y les cobra un impuesto del 30 % sobre esas donaciones.

Según el texto de la ley, citado por LexLatin, su finalidad es promover la transparencia sobre la influencia extranjera y resguardar la seguridad, la soberanía nacional y la estabilidad social y política del país. Esa es la justificación del gobierno.

Las organizaciones de derechos humanos la ven de otra manera. Según Human Rights Watch, la ley da al gobierno amplias facultades para vigilar, sancionar y cerrar a las organizaciones que estigmatiza como agentes extranjeros, y se aprobó prácticamente sin debate ni consulta pública.

Por eso el gobierno la presenta como una ley de transparencia y organizaciones como Human Rights Watch la ven como una forma de controlar a la sociedad civil crítica.
""")

E("sv-b021", "E13", "hecho", "¿Quién es Ruth López y por qué está presa?",
  [[B("Ruth López Cristosal detención", ["FR-E13-006", "FR-E14-010"], epoca="E13")]],
  """
Ruth López es una abogada salvadoreña de derechos humanos, directora de anticorrupción y justicia de la ONG Cristosal y crítica del gobierno de Bukele.

Según Los Angeles Times, en mayo de 2025 la Policía la detuvo en su casa y la Fiscalía la acusó de enriquecimiento ilícito. Cristosal calificó la detención de represalia política.

Su caso se ha convertido en uno de los más citados por quienes critican al gobierno. Según el Informe Mundial 2026 de Human Rights Watch, el gobierno de Bukele siguió eliminando los controles al Poder Ejecutivo y aumentó la represión contra defensores de derechos humanos, periodistas, activistas y sindicalistas.

La versión del gobierno es que se trata de un caso penal por enriquecimiento ilícito. Con lo que tengo no puedo decirte si las acusaciones tienen fundamento, porque no tengo acceso al expediente judicial ni a una resolución del tribunal. Lo que sí puedo decirte es quién afirma qué: la Fiscalía la acusa de un delito y su organización, junto con Human Rights Watch, sostiene que es persecución por su trabajo.
""")

E("sv-b022", "E14", "hecho", "¿Sigue vigente el régimen de excepción?",
  [[B("prórroga régimen de excepción 2026", ["FR-E14-001", "FR-E14-002", "FR-E14-004", "FR-E10-004"], epoca="E14")]],
  """
Sí, según lo último que tengo, sigue vigente.

El 24 de junio de 2026 la Asamblea Legislativa aprobó la prórroga número 52 del régimen de excepción. Para entonces la medida llevaba más de cuatro años en vigor sin interrupción, desde marzo de 2022.

El gobierno sostiene que todavía hace falta. Según el decreto de prórroga aprobado en febrero de 2026, el régimen había dejado más de 91.300 capturas de personas vinculadas a estructuras criminales, y los vínculos transnacionales y los intentos de reorganización de las pandillas justificaban mantenerlo. En la misma línea, según EFE, el vicepresidente Félix Ulloa aseguró que las condiciones que llevaron a decretarlo en marzo de 2022 no se han superado.

Ten en cuenta que el régimen se prorroga cada 30 días, así que puede haber prórrogas posteriores a la última que tengo registrada. Si necesitas saber el número exacto de la prórroga vigente hoy, lo mejor es consultar el Diario Oficial o la prensa salvadoreña del día.
""")

E("sv-b023", "E14", "conflicto", "¿Hay presos políticos en El Salvador?",
  [[B("presos políticos El Salvador Cristosal GIPES", ["FR-E14-006", "FR-E14-007", "FR-E14-009"], epoca="E14")]],
  """
Las organizaciones de derechos humanos dicen que sí y el gobierno lo rechaza. Te explico qué sostiene cada parte.

Según un informe de Cristosal presentado en Guatemala en marzo de 2026, el gobierno de Bukele tiene al menos 86 presos políticos. Serían sobre todo defensores de derechos humanos, periodistas, funcionarios judiciales, sindicalistas y ambientalistas. Cristosal sostiene además que miles de inocentes cayeron en las detenciones masivas del régimen de excepción.

A eso se suma un informe internacional. Según el Tico Times, un grupo de expertos conocido como GIPES, respaldado por la Comisión Internacional de Juristas y la FIDH, concluyó en marzo de 2026 ante la CIDH que hay bases razonables para creer que se cometen crímenes de lesa humanidad.

El gobierno niega todo esto. Bukele rechazó tanto esa conclusión como la acusación de presos políticos. Y según el Tico Times, acusó a las organizaciones de derechos humanos de actuar como bufetes de abogados de los criminales y dijo que su gobierno nunca atenderá sus críticas.

Con lo que tengo, no puedo decidir quién tiene razón: «preso político» es una calificación que Cristosal hace y el gobierno rechaza. Lo que sí puedo hacer es buscarte casos concretos para que veas qué se le imputa a cada persona.
""")

E("sv-b024", "E14", "conflicto", "¿Cuánta gente ha muerto en las cárceles durante el régimen de excepción?",
  [[B("muertes bajo custodia régimen de excepción", ["FR-E14-008", "FR-E14-009"], epoca="E14")]],
  """
No hay una cifra oficial, y las que existen las llevan organizaciones civiles que no coinciden del todo entre sí.

Según Diario El Mundo, Socorro Jurídico Humanitario registra 530 personas fallecidas bajo custodia del Estado durante el régimen. El Tico Times, por su parte, recoge al menos 500 muertes según una organización salvadoreña, que además afirma que la mayoría de esas personas no tenía vínculos con pandillas.

El gobierno no publica una cifra propia, así que no hay un dato oficial con el que contrastar esos registros. Y su posición frente a estas organizaciones es de rechazo: según el Tico Times, Bukele las acusó de actuar como bufetes de abogados de los criminales y dijo que no atenderá sus críticas.

Por eso, si vas a usar estas cifras, lo correcto es darlas siempre con su dueño: «según Socorro Jurídico Humanitario, 530 muertes bajo custodia». No son cifras inventadas, pero tampoco han sido verificadas por una fuente independiente del conflicto entre el gobierno y las ONG, al menos en lo que encontré.
""")

E("sv-b025", "E14", "hecho", "¿Bukele es popular de verdad o es propaganda?",
  [[B("popularidad de Bukele 2026", ["FR-E14-005", "FR-E12-001", "FR-E12-003"])]],
  """
Los datos apuntan a que es popular de verdad, aunque hay matices que vale la pena conocer.

Según El Diario de Hoy, Bukele llegó a 2026 con índices altos de popularidad, que se han mantenido sin grandes cambios en sus siete años en el poder. Esa popularidad descansa sobre todo en la reducción de los homicidios y en el régimen de excepción.

Las urnas van en la misma dirección. En 2024 fue reelegido con el 84,65 % de los votos válidos, según el Tribunal Supremo Electoral, y su partido ganó 54 de los 60 escaños de la Asamblea.

El matiz está en la participación. Según El Diario de Hoy, más de 2,9 millones de salvadoreños habilitados no votaron en 2024, de modo que los votos de Bukele equivalen al 43,48 % del padrón electoral.

Así que no es solo propaganda: tanto los índices de popularidad como los resultados electorales muestran un apoyo amplio. Lo que se discute es otra cosa, si ese apoyo justifica las medidas que sus críticos consideran abusos. Esa ya es una pregunta política, y ahí cada persona saca su conclusión.
""")

E("sv-b026", "E14", "perspectivas", "Dame un balance del modelo Bukele: lo bueno y lo malo.",
  [[C("homicidios", [("2021", "1.211", "cifras oficiales", "FR-E11-004"),
                     ("2025", "82", "cifras oficiales", "FR-E11-004")], desde="2021", hasta="2025"),
    B("críticas al régimen de excepción derechos humanos", ["FR-E14-006", "FR-E14-008", "FR-E14-010"])],
   [B("popularidad y argumentos del gobierno", ["FR-E14-005", "FR-E11-006"])]],
  """
Te lo doy como lo ven sus defensores y sus críticos, con las cifras de cada uno.

Lo que destacan sus defensores es la seguridad. Según las cifras oficiales citadas por Diario El Mundo, los homicidios pasaron de 1.211 en 2021 a 82 en 2025. Según EFE, el gobierno sostiene que el régimen de excepción permitió combatir a las maras y liberar los territorios que dominaban. Y Bukele mantiene, según El Diario de Hoy, índices altos de popularidad que descansan sobre todo en esa reducción de la violencia.

Lo que señalan sus críticos son los costos. Según el Informe Mundial 2026 de Human Rights Watch, el gobierno siguió eliminando los controles al Poder Ejecutivo y aumentó la represión contra defensores de derechos humanos y periodistas. Según Cristosal, hay al menos 86 presos políticos y miles de inocentes detenidos en las capturas masivas. Y según Socorro Jurídico Humanitario, 530 personas han muerto bajo custodia del Estado.

Un matiz que no conviene olvidar: según la misma nota de EFE, los asesinatos ya venían bajando desde 2016, antes del régimen.

El balance final depende de cuánto pese cada cosa para cada persona: la seguridad recuperada o las garantías perdidas. Esa es una decisión política que no me toca tomar por ti.
""")

E("sv-b027", "T03", "hecho", "¿Otros países han copiado el modelo de Bukele?",
  [[B("modelo Bukele en otros países Honduras Ecuador megacárceles", ["FR-T03-001", "FR-T03-002", "FR-T03-003", "FR-T03-004"], epoca="T03")]],
  """
Sí, varios gobiernos de la región han tomado elementos del modelo, aunque con resultados distintos.

En Honduras, el gobierno de Xiomara Castro, que es de izquierda, decretó un estado de excepción en diciembre de 2022 inspirado en el salvadoreño, y en 2024 anunció planes para construir una cárcel al estilo del CECOT.

En Ecuador, el presidente Daniel Noboa impuso un estado de excepción desde el 8 de enero de 2024 y presentó un plan para construir megacárceles al estilo salvadoreño.

La idea de la megacárcel se ha extendido todavía más. Según un reportaje de CONNECTAS publicado en agosto de 2026, en tres años los presidentes de Colombia, Ecuador, Perú, Costa Rica, Panamá y Guatemala prometieron una como parte de su política contra el crimen.

Pero copiarlo no garantiza el mismo resultado. Según un análisis de la Universidad de Navarra, la receta no funciona igual en Honduras porque allí mata más el narcotráfico que las maras, el gobierno tiene menos poder y los cuerpos policiales son más complejos.
""")

E("sv-b028", "E14", "reformulacion", "¿Verdad que Bukele acabó con las pandillas para siempre?",
  [[B("situación actual de las pandillas y régimen de excepción", ["FR-E11-004", "FR-E14-004", "FR-E14-002"])]],
  """
Que las debilitó muchísimo lo muestran las cifras; que haya acabado con ellas para siempre no lo afirma ni el propio gobierno.

Según las cifras oficiales citadas por Diario El Mundo, los homicidios bajaron de 1.211 en 2021 a 82 en 2025. Es un cambio enorme, y el gobierno lo atribuye a la ofensiva contra las pandillas.

Pero fíjate en lo que dice el propio gobierno cuando pide mantener el régimen de excepción. Según el decreto de prórroga de febrero de 2026, el régimen había dejado más de 91.300 capturas, y los vínculos transnacionales y los intentos de reorganización de las pandillas justificaban seguir con él. Y según EFE, el vicepresidente Félix Ulloa aseguró que las condiciones que llevaron a decretarlo en marzo de 2022 no se han superado.

Es decir, el propio gobierno considera que la amenaza sigue ahí, aunque mucho más débil. «Para siempre» es algo que nadie puede asegurar todavía: dependerá de lo que pase cuando el régimen de excepción termine, si termina, y de si las pandillas logran reorganizarse.
""")

E("sv-b029", "E14", "reformulacion", "Las ONG de derechos humanos solo defienden a los pandilleros, ¿no?",
  [[B("ONG derechos humanos críticas al gobierno y respuesta de Bukele", ["FR-E14-009", "FR-E14-006", "FR-E13-005"])]],
  """
Esa es la postura del gobierno, pero las organizaciones dicen algo distinto, así que te doy las dos.

La del gobierno: según el Tico Times, Bukele acusó en marzo de 2026 a las organizaciones de derechos humanos de actuar como bufetes de abogados de los criminales y dijo que su gobierno nunca atenderá sus críticas.

La de las organizaciones: lo que afirman no es que haya que soltar a los pandilleros, sino que en las detenciones masivas también cayeron inocentes. Según un informe de Cristosal de marzo de 2026, miles de personas sin relación con las pandillas fueron detenidas, y la organización cuenta además al menos 86 presos políticos, entre ellos defensores de derechos humanos, periodistas y sindicalistas. Human Rights Watch, por su parte, critica la Ley de Agentes Extranjeros porque, según dice, permite vigilar, sancionar y cerrar a las organizaciones que el gobierno estigmatiza.

O sea, la discusión real no es si se debe castigar a los pandilleros sino si se está respetando el derecho de los detenidos a defenderse y a ser juzgados. Si quieres, te busco casos concretos que citan esas organizaciones.
""")

E("sv-b030", "E09", "reformulacion", "¿Bukele es un dictador?",
  [[B("concentración de poder Bukele críticas y apoyos", ["FR-E09-001", "FR-E09-004", "FR-E14-005", "FR-E14-010"])]],
  """
«Dictador» es una calificación política, no un dato, así que no te voy a dar un sí o un no. Lo que sí puedo hacer es contarte los hechos que usan unos y otros para llegar a conclusiones distintas.

Los hechos que citan sus críticos: el 1 de mayo de 2021 la Asamblea controlada por Nuevas Ideas destituyó a los magistrados de la Sala de lo Constitucional y al fiscal general. La Constitución prohíbe la reelección inmediata, pero en 2021 la Corte Suprema habilitó a Bukele a presentarse de nuevo. Y según el Informe Mundial 2026 de Human Rights Watch, el gobierno siguió eliminando los controles al Poder Ejecutivo y aumentó la represión contra periodistas y defensores de derechos humanos.

Los hechos que citan sus partidarios: llegó al poder y fue reelegido en elecciones, la segunda vez con un porcentaje altísimo, y según El Diario de Hoy mantiene índices altos de popularidad desde hace siete años, sobre todo por la reducción de los homicidios.

Por eso unos hablan de autoritarismo y otros de un líder con un apoyo popular enorme. Las dos cosas pueden ser ciertas a la vez, y cómo se pesan es una decisión de cada persona.
""")

guardar("ejemplos_lote_b.jsonl")
