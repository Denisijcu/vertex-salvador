"""
agregar_lote2.py — Lote 2 de vertex-salvador: fuentes y fragmentos de E06–E14, T01, T03 y T04.

Uso (desde E:\\vertex-salvador, después de agregar_lote1.py):
    python agregar_lote2.py
    python validar.py fuentes\\fragmentos_lote2.jsonl --fragmentos

Regla de este lote: las cifras del gobierno salvadoreño (PNC, Asamblea, Presidencia) y las de las ONG (Cristosal,
Socorro Jurídico, HRW) se dan SIEMPRE atribuidas. Ninguna de las dos pasa como hecho por sí sola.
Revisión: Claude, por encargo de Denis (17 de noviembre de 2026).
"""
import csv
import json
from pathlib import Path

from agregar_lote1 import HOY, REVISOR

FUENTES = [
    ("S069", "Nayib Bukele, un exalcalde de izquierda que gobernará El Salvador con la derecha (EFE)", "Panamá América", "https://www.panamaamerica.com.pa/mundo/nayib-bukele-un-exalcalde-de-izquierda-que-gobernara-el-salvador-con-la-derecha-1127365", "prensa", "sin_revisar", "prensa", "hechos", ""),
    ("S070", "Nayib Bukele (biografía)", "Encyclopaedia Britannica", "https://www.britannica.com/biography/Nayib-Bukele", "enciclopedia", "sin_revisar", "enciclopedia", "hechos", ""),
    ("S071", "Nayib Bukele", "Wikipedia", "https://en.wikipedia.org/wiki/Nayib_Bukele", "enciclopedia", "CC BY-SA", "enciclopedia", "hechos", ""),
    ("S072", "Bukele, el expresidente millennial (BBC Mundo)", "MDZ / BBC Mundo", "https://www.mdzol.com/bbc-mundo/2019/6/1/quien-es-el-joven-empresario-millennial-que-asume-como-presidente-de-el-salvador-30573.html/amp", "prensa", "sin_revisar", "prensa", "hechos", ""),
    ("S073", "Nayib Bukele se proclama presidente electo de El Salvador", "Revista E&N", "https://www.revistaeyn.com/lasclavesdeldia/nayib-bukele-se-proclama-presidente-electo-de-el-salvador-JUEN1255905", "prensa", "sin_revisar", "prensa", "hechos", ""),
    ("S074", "Nuevo gobierno en El Salvador", "IDEA Internacional", "https://www.idea.int/es/news-media/news/es/nuevo-gobierno-en-el-salvador", "secundaria", "sin_revisar", "organismo_internacional", "hechos", ""),
    ("S075", "El Salvador: cinco años del terremoto político que llevó a Bukele al poder", "Primicias (con EFE)", "https://primicias.ec/noticias/internacional/elsalvador-bukele-aniversario-elecciones", "prensa", "sin_revisar", "prensa", "hechos", ""),
    ("S076", "2020 Salvadoran political crisis", "Wikipedia", "https://en.wikipedia.org/wiki/2020_Salvadoran_political_crisis", "enciclopedia", "CC BY-SA", "enciclopedia", "hechos", ""),
    ("S077", "El día que Bukele entró con militares a la Asamblea Legislativa", "El Diario de Hoy", "https://www.elsalvador.com/?p=1199467", "prensa", "sin_revisar", "prensa", "hechos", ""),
    ("S078", "Bukele irrumpe con militares en el Congreso salvadoreño (EFE)", "La Prensa (Honduras)", "https://www.laprensa.hn/mundo/bukele-irrumpe-militares-congreso-salvadoreno-crisis-interna-EDLP1355450", "prensa", "sin_revisar", "prensa", "ambos", ""),
    ("S079", "#9F: el diputado de GANA dice que nunca se intentó un golpe", "El Salvador Solidarity (recoge tuit de Guillermo Gallegos)", "https://www.elsalvadorsolidarity.org/?p=21475", "secundaria", "sin_revisar", "gobierno_salvadoreno", "postura", "Declaración de un diputado aliado del gobierno"),
    ("S080", "¿Qué pasó el 9 de febrero de 2020 en El Salvador?", "Revista E&N", "https://www.revistaeyn.com/lasclavesdeldia/que-paso-el-9-de-febrero-de-2020-en-el-salvador-PXEN1511619", "prensa", "sin_revisar", "prensa", "ambos", ""),
    ("S081", "Las claves para entender qué sucede con la Sala Constitucional", "El Financiero (Costa Rica)", "https://www.elfinancierocr.com/economia-y-politica/ef-explica-las-claves-para-entender-que-sucede-con/XZXFQ6CTVZCFNN3CVWRTE4WDDU/story/", "prensa", "sin_revisar", "prensa", "hechos", ""),
    ("S082", "Congreso en El Salvador destituye a jueces (AFP)", "La Nación (Costa Rica)", "https://www.nacion.com/cables/congreso-en-el-salvador-destituye-a-jueces/RWN2CS3RQBB3RPXU3GFELTTL4A/story/", "prensa", "sin_revisar", "prensa", "hechos", ""),
    ("S083", "Nueva Asamblea Legislativa de El Salvador destituye a magistrados", "El Financiero (México)", "https://www.elfinanciero.com.mx/mundo/2021/05/02/nueva-asamblea-legislativa-de-el-salvador-destituye-a-magistrados/", "prensa", "sin_revisar", "prensa", "ambos", ""),
    ("S084", "Comunidad internacional ante la crisis en El Salvador", "El Diario", "https://eldiario.com/2021/05/03/comunidad-internacional-crisis-el-salvador/", "prensa", "sin_revisar", "prensa", "hechos", ""),
    ("S085", "EE.UU. sanciona a altos funcionarios de El Salvador por tratos con pandillas", "El Observador (Costa Rica)", "https://observador.cr/ee-uu-sanciona-a-altos-funcionarios-de-el-salvador-por-tratos-con-pandillas/", "prensa", "sin_revisar", "prensa", "ambos", "Lo que afirma el Tesoro es postura de EE. UU."),
    ("S086", "Estados Unidos sanciona a altos funcionarios del gobierno de Nayib Bukele", "La Prensa (Panamá)", "https://www.prensa.com/impresa/panorama/eu-sanciona-a-altos-funcionarios-del-gobierno-de-nayib-bukele/", "prensa", "sin_revisar", "prensa", "ambos", ""),
    ("S087", "Es engañoso que EE. UU. solo haya sancionado a funcionarios anteriores (verificación)", "El Salvador Now / Infodemia", "https://elsalvadornow.org/2024/09/02/misleading-claim-us-only-sanctioned-previous-officials-for-negotiating-with-gangs-says-bukele-to-time-es-enganoso-que-eeuu-solo-haya-sancionado-a-funcionarios-anteriores-por-negociar-con-p", "prensa", "sin_revisar", "prensa", "hechos", ""),
    ("S088", "Cuatro años del régimen de excepción: balance", "Infobae (2026)", "https://www.infobae.com/el-salvador/2026/03/27/cuatro-anos-del-regimen-de-excepcion-en-el-salvador-balance-de-una-era-de-cambios-legales-y-sociales/", "prensa", "sin_revisar", "prensa", "ambos", "Cifras de la PNC: atribuirlas"),
    ("S089", "El día más sangriento desde la guerra civil (marzo de 2022)", "InSight Crime", "https://insightcrime.org/es/?p=181042", "secundaria", "sin_revisar", "academica", "hechos", ""),
    ("S090", "Los audios del pacto entre el gobierno y la MS-13 (sobre la investigación de El Faro)", "Telemundo", "https://www.telemundo.com/noticias/noticias-telemundo/internacional/bukele-pandillas-audios-pacto-rcna29509", "prensa", "sin_revisar", "prensa", "ambos", "La tesis del pacto roto es de El Faro: atribuirla"),
    ("S091", "El Salvador bajo régimen de excepción a pedido de Bukele (AFP)", "TVN Panamá", "https://www.tvn-2.com/mundo/centroamerica/salvador-excepcion-bukele-enfrentar-pandillas_1_1021223.html", "prensa", "sin_revisar", "prensa", "hechos", ""),
    ("S092", "El Salvador cumple cuatro años bajo régimen de excepción (EFE)", "Revista E&N", "https://www.revistaeyn.com/centroamericaymundo/el-salvador-cumple-cuatro-anos-bajo-regimen-de-excepcion-con-nueva-prorroga-MK29898370", "prensa", "sin_revisar", "prensa", "ambos", ""),
    ("S093", "Megacárcel de El Salvador recibe a los primeros 2.000 pandilleros", "El Heraldo (Honduras)", "https://www.elheraldo.hn/mundo/megacarcel-el-salvador-recibe-primeros-2000-pandilleros-EC12321995", "prensa", "sin_revisar", "prensa", "hechos", ""),
    ("S094", "Terrorism Confinement Center", "Wikipedia", "https://en.wikipedia.com/wiki/CECOT", "enciclopedia", "CC BY-SA", "enciclopedia", "hechos", ""),
    ("S095", "El Cecot cumple dos años", "Centroamérica 360", "https://centroamerica360.com/?p=151109", "prensa", "sin_revisar", "prensa", "hechos", ""),
    ("S096", "La Asamblea prorroga por 51.ª vez el régimen de excepción", "Diario El Mundo (El Salvador)", "https://diario.elmundo.sv/politica/asamblea-prorroga-por-51a-vez-el-regimen-de-excepcion-con-92300-capturados", "prensa", "sin_revisar", "prensa", "ambos", "Cifras oficiales y de ONG: atribuirlas"),
    ("S097", "El Salvador alcanzará los cuatro años bajo régimen de excepción (EFE)", "Revista E&N", "https://www.revistaeyn.com/centroamericaymundo/el-salvador-alcanzara-los-cuatro-anos-bajo-regimen-de-excepcion-tras-nueva-prorroga-EK29452237", "prensa", "sin_revisar", "prensa", "ambos", ""),
    ("S098", "El Salvador extiende el régimen de excepción en su prórroga número 52", "Infobae (2026)", "https://www.infobae.com/el-salvador/2026/06/24/el-salvador-extiende-el-regimen-de-excepcion-por-30-dias-mas-en-su-prorroga-numero-52/", "prensa", "sin_revisar", "prensa", "ambos", "Cifras de la Asamblea: atribuirlas"),
    ("S099", "Félix Ulloa: las condiciones del régimen no se han superado (EFE)", "El Diario de Hoy", "https://www.eldiariodehoy.com/?p=99547", "prensa", "sin_revisar", "prensa", "ambos", "Cifras de la PNC: atribuirlas"),
    ("S100", "Bukele destaca disminución de homicidios desde antes del régimen", "Diario El Mundo (El Salvador)", "https://diario.elmundo.sv/nacionales/bukele-destaca-disminucion-de-homicidios-desde-antes-del-regimen-de-excepcion", "prensa", "sin_revisar", "prensa", "ambos", ""),
    ("S101", "Cuatro años de régimen de excepción: por qué se aprobó y por qué sigue (EFE)", "Tu Nota", "https://www.tunota.com/mundo/cuatro-anos-regimen-de-excepcion-el-salvador-por-que-se-aprobo-y-sigue-vigente-2026-03-25", "prensa", "sin_revisar", "prensa", "ambos", ""),
    ("S102", "El régimen de excepción cumple cuatro años entre respaldo y denuncias (EFE)", "Metro Puerto Rico", "https://www.metro.pr/noticias/2026/03/27/el-regimen-de-excepcion-en-el-salvador-cumple-cuatro-anos-entre-respaldo-y-denuncias-de-abusos/", "prensa", "sin_revisar", "prensa", "ambos", ""),
    ("S103", "Bukele arranca el último año de su segundo mandato entre popularidad y demandas", "El Diario de Hoy", "https://www.eldiariodehoy.com/noticias/nacionales/bukele-arranca-ultimo-ano-de-segundo-mandato-entre-popularidad-y-demandas-de-salvadorenos/78073/2026/", "prensa", "sin_revisar", "prensa", "hechos", ""),
    ("S104", "Tribunal Electoral confirma la reelección de Bukele con el 84,65 %", "Voz de América", "https://www.vozdeamerica.com/a/tribunal-electoral-salvador-confirma-reeleccion-de-bukele-con-mas-de-84-porciento/7492416.html", "prensa", "dominio_publico (obra del gobierno de EE. UU.)", "prensa", "hechos", ""),
    ("S105", "2024 Salvadoran general election", "Wikipedia", "https://Www.wikipedia.org/wiki/2024_Salvadoran_local_elections", "enciclopedia", "CC BY-SA", "enciclopedia", "hechos", ""),
    ("S106", "El Salvador - February 2024", "IDEA Internacional, Democracy Tracker", "https://www.idea.int/democracytracker/report/el-salvador/february-2024?pid=7005", "secundaria", "sin_revisar", "organismo_internacional", "hechos", ""),
    ("S107", "Participación en las elecciones de 2024", "El Diario de Hoy", "https://www.elsalvador.com/?p=1124390", "prensa", "sin_revisar", "prensa", "hechos", ""),
    ("S108", "Trump y Bukele pasan por encima de las leyes con encarcelamientos en CECOT", "El Diario de Hoy", "https://www.elsalvador.com/noticias/nacional/trump-bukele-pasan-por-encima-leyes-con-encarcelamientos-en-cecot/1210728/2025/", "prensa", "sin_revisar", "prensa", "ambos", "Titular valorativo: solo sus datos"),
    ("S109", "La secretaria de Seguridad de Trump visita la cárcel que recluye a venezolanos (AFP)", "Diario El Mundo (El Salvador)", "https://diario.elmundo.sv/politica/secretaria-de-seguridad-de-trump-visita-carcel-salvadorena-que-recluye-a-venezolanos-y-agradece-a-bukele", "prensa", "sin_revisar", "prensa", "hechos", ""),
    ("S110", "EE. UU. deporta a El Salvador a más de 200 presos venezolanos", "Orain", "https://orain.eus/es/actualidad/internacional/2025/03/17/eeuu-expulsa-a-el-salvador-a-238-miembros-del-tren-de-aragua-usando-ley-bajo-disputa-judicial/", "prensa", "sin_revisar", "prensa", "ambos", ""),
    ("S111", "El Salvador: la Ley de Agentes Extranjeros amenaza a la sociedad civil", "Human Rights Watch", "https://www.hrw.org/es/news/2025/05/23/el-salvador-la-ley-de-agentes-extranjeros-amenaza-la-sociedad-civil-y-medios-de", "secundaria", "sin_revisar", "ong_ddhh", "postura", ""),
    ("S112", "Las 5 claves de la nueva Ley de Agentes Extranjeros", "Diario El Mundo (El Salvador)", "https://diario.elmundo.sv/politica/las-5-claves-de-la-nueva-ley-de-agentes-extranjeros-en-el-salvador", "prensa", "sin_revisar", "prensa", "hechos", ""),
    ("S113", "Congreso aprueba Ley de Agentes Extranjeros con impuesto del 30 %", "Prensa Libre (con EFE)", "https://www.prensalibre.com/?p=22669937", "prensa", "sin_revisar", "prensa", "hechos", ""),
    ("S114", "Ley de Agentes Extranjeros: nuevos trámites e impuestos", "LexLatin", "https://lexlatin.com/opinion/ley-agentes-extranjeros-el-salvador-tramites-impuestos-donaciones-financiamiento-internacional", "secundaria", "sin_revisar", "academica", "hechos", ""),
    ("S115", "Human rights attorney who criticized Bukele is detained (Los Angeles Times)", "Yahoo News", "https://www.yahoo.com/news/el-salvador-arrests-human-rights-215955711.html", "prensa", "sin_revisar", "prensa", "ambos", ""),
    ("S116", "El Salvador: abogada de derechos humanos sigue presa un año después", "Human Rights Watch", "https://www.hrw.org/news/2026/05/18/el-salvador-human-rights-lawyer-still-in-jail-one-year-on", "secundaria", "sin_revisar", "ong_ddhh", "postura", ""),
    ("S117", "Una ONG dice que Bukele tiene 86 presos políticos", "Tico Times (2026)", "https://ticotimes.net/2026/03/05/an-ngo-says-bukele-has-86-political-prisoners-in-el-salvador", "prensa", "sin_revisar", "prensa", "ambos", "La cifra es de Cristosal: atribuirla"),
    ("S118", "Bukele descarta las acusaciones de presos políticos", "Tico Times (2026)", "https://ticotimes.net/2026/03/12/bukele-dismisses-political-prisoners-accusations-in-el-salvador-gang-crackdown", "prensa", "sin_revisar", "prensa", "ambos", ""),
    ("S119", "500 presos muertos bajo custodia durante la ofensiva contra pandillas", "Tico Times (2026)", "https://ticotimes.net/2026/03/29/500-prisoners-die-in-el-salvador-custody-during-bukele-anti-gang-crackdown", "prensa", "sin_revisar", "prensa", "ambos", "La cifra es de una ONG: atribuirla"),
    ("S120", "Informe señala crímenes de lesa humanidad; Bukele lo niega (EFE)", "El Salvador Now", "https://www.elsalvadornow.org/2026/03/15/report-points-to-crimes-against-humanity-in-el-salvador-bukele-denies-it-informe-senala-crimenes-de-lesa-humanidad-en-el-salvador-bukele-lo-niega", "prensa", "sin_revisar", "prensa", "ambos", ""),
    ("S121", "World Report 2026: El Salvador", "Human Rights Watch (vía ecoi.net)", "https://www.ecoi.net/en/document/2136209.html", "secundaria", "sin_revisar", "ong_ddhh", "postura", ""),
    ("S122", "International Echoes of El Salvador's Public Security Model", "Instituto Polaco de Asuntos Internacionales (PISM)", "https://pism.pl/publications/international-echoes-of-el-salvadors-public-security-model", "secundaria", "sin_revisar", "academica", "hechos", ""),
    ("S123", "La receta de Bukele no funciona en Honduras, donde mata más el narco que las maras", "Universidad de Navarra, Global Affairs", "https://www.unav.edu/web/global-affairs/la-receta-de-bukele-no-funciona-en-honduras-donde-mata-mas-el-narco-que-las-maras", "secundaria", "sin_revisar", "academica", "ambos", "Análisis: sus valoraciones son postura"),
    ("S124", "Megacárceles, estado de excepción y mano dura: el modelo Bukele inspira a la región", "Voz Media", "https://voz.us/es/mundo/240311/10211/megacarceles-estado-de-excepcion-y-mano-dura-contra-el-crimen-el-modelo-bukele-esta-inspirando-a-la-region.html", "prensa", "sin_revisar", "prensa", "ambos", ""),
    ("S125", "El espejismo de las megacárceles (CONNECTAS)", "El Búho", "https://elbuho.pe/?p=433171", "prensa", "sin_revisar", "prensa", "ambos", ""),
    ("S126", "Bukele insiste en que periodistas y ONG quieren la liberación de los pandilleros", "Diario El Mundo (El Salvador)", "https://diario.elmundo.sv/politica/bukele-insiste-que-periodistas-y-ong-quieren-liberacion-de-todos-los-pandilleros", "prensa", "sin_revisar", "prensa", "ambos", ""),
    ("S127", "Tres días de problemas para Bukele, «el CEO de El Salvador»", "El Salto", "https://www.elsaltodiario.com/el-salvador/problemas-bukele-autoritarismo-bitcoin-relacion-estados-unidos", "prensa", "sin_revisar", "prensa", "ambos", ""),
    ("S128", "La conversión del presidente millennial", "Diálogo Político (Fundación Konrad Adenauer)", "https://dialogopolitico.org/agenda/la-conversion-del-presidente-millennial/", "secundaria", "sin_revisar", "academica", "ambos", "Análisis: sus valoraciones son postura"),
    ("S130", "3 claves que explican por qué Bukele arrasó en las elecciones (BBC News Mundo)", "Grupo Animal / BBC Mundo", "https://grupoanimal.mx/internacional/claves-bukele-reelegido-presidente-el-salvador", "prensa", "sin_revisar", "prensa", "hechos", ""),
    ("S129", "Bukele: siete años de gobierno más allá de los límites constitucionales", "CISPES", "https://cispes.org/node/9163", "secundaria", "sin_revisar", "ong_ddhh", "postura", "Organización de solidaridad crítica del gobierno"),
]

FRAGMENTOS = []


def F(fid, etapa, tipo, fuente, ubic, texto, corr=(), actor=None):
    d = {"id": fid, "etapa": etapa, "tipo": tipo, "id_fuente": fuente, "ubicacion": ubic,
         "corroborado_por": list(corr), "texto": texto, "notas": "", "revisado": True, "estado": "aprobado",
         "revisor": REVISOR, "fecha_revision": HOY}
    if actor:
        d["actor"] = actor
    FRAGMENTOS.append(d)


# ---------------------------------------------------------------- T01 · Perfil de Bukele
F("FR-T01-001", "T01", "hecho_atribuido", "S071", "Ficha y primeros años",
  "Según su biografía en Wikipedia, Nayib Armando Bukele Ortez nació el 24 de julio de 1981 en San Salvador. Es hijo del empresario Armando Bukele "
  "Kattán, que murió en 2015, y de Olga Marina Ortez. Estudió en la Universidad Centroamericana (UCA) sin "
  "terminar la carrera.")
F("FR-T01-002", "T01", "hecho_atribuido", "S072", "Perfil de BBC Mundo",
  "Según BBC Mundo, quienes conocen a Bukele destacan su inteligencia, su capacidad de innovar y su conocimiento "
  "de los problemas del país, y lo describen como un político difícil de encasillar: fue alcalde por el FMLN, de "
  "izquierda, y ganó la presidencia con GANA, un partido de derecha nacido de una escisión de ARENA.")

# ---------------------------------------------------------------- E06 · Bukele alcalde
F("FR-E06-001", "E06", "hecho", "S070", "Sección 'Political career'",
  "En 2012, a los 31 años, Bukele fue elegido alcalde del pequeño municipio de Nuevo Cuscatlán, junto a San "
  "Salvador, como miembro del FMLN. En 2015 ganó la alcaldía de la capital, San Salvador, también con el FMLN, y "
  "la ejerció de 2015 a 2018.", corr=["S069", "S071"])
F("FR-E06-002", "E06", "hecho", "S069", "Despacho de EFE",
  "Las diferencias de Bukele con la dirección del FMLN terminaron con su expulsión del partido en 2017. Ese año "
  "fundó Nuevas Ideas, que al principio no pudo inscribirse como partido porque no cumplía los requisitos de la "
  "ley electoral, y para 2019 se presentó con GANA.", corr=["S070"])

# ---------------------------------------------------------------- E07 · Elección de 2019 y Plan Control Territorial
F("FR-E07-001", "E07", "hecho", "S075", "Párrafo inicial",
  "El 3 de febrero de 2019 Bukele ganó la elección presidencial en primera vuelta con el 53 % de los votos "
  "válidos, como candidato de GANA. Rompió así treinta años de alternancia entre ARENA y el FMLN; el segundo, "
  "Carlos Calleja, de ARENA, quedó en torno al 32 %.", corr=["S073", "S074"])
F("FR-E07-002", "E07", "hecho", "S076", "Antecedentes",
  "Bukele asumió el 1 de junio de 2019 y el 20 de junio puso en marcha el Plan Control Territorial, su estrategia "
  "de seguridad contra las pandillas. El gobierno atribuye a ese plan la baja de los homicidios desde junio de "
  "2019.", corr=["S078"])
F("FR-E07-003", "E07", "hecho_atribuido", "S075", "Balance de 2019 a 2021",
  "Según un balance de EFE publicado por Primicias, Bukele logró acentuar la disminución de los homicidios que "
  "había empezado en 2016 y, de acuerdo con las autoridades, quitó a las pandillas el control de los barrios "
  "populares; hasta mayo de 2021 su mandato estuvo marcado por los choques con la Asamblea, entonces de mayoría "
  "opositora, y con la Sala de lo Constitucional.")

# ---------------------------------------------------------------- E08 · El 9F
F("FR-E08-001", "E08", "hecho", "S077", "Crónica",
  "El 9 de febrero de 2020 Bukele entró en la Asamblea Legislativa acompañado de militares y policías armados para "
  "presionar a los diputados, entonces de mayoría opositora, a aprobar un préstamo de 109 millones de dólares para "
  "la fase III del Plan Control Territorial. Se sentó en la silla del presidente de la Asamblea y rezó en el "
  "Salón Azul.", corr=["S076", "S078", "S128"])
F("FR-E08-002", "E08", "hecho_atribuido", "S078", "Despacho de EFE",
  "Según EFE, la sesión extraordinaria que convocó Bukele aquel 9 de febrero no pudo celebrarse por falta de "
  "quórum, porque solo se presentaron 20 diputados; ante sus seguidores, Bukele dio una semana a los legisladores "
  "para aprobar el préstamo.")
F("FR-E08-003", "E08", "postura", "S080", "Entrevista",
  "Según la Revista E&N, para un diputado del PCN lo ocurrido el 9F fue una toma a la fuerza de la Asamblea con "
  "intención de disolverla; en cambio, el diputado Guillermo Gallegos, de GANA, aliado del gobierno, sostuvo que "
  "nunca se intentó un golpe de Estado y llamó absurdo conmemorar esa fecha.", corr=["S079"],
  actor="diputados de oposición y del oficialismo")

# ---------------------------------------------------------------- E09 · 2021: Asamblea, Sala y Fiscalía
F("FR-E09-001", "E09", "hecho", "S081", "Claves",
  "El 1 de mayo de 2021, en su primera sesión, la nueva Asamblea Legislativa, con mayoría de Nuevas Ideas tras las "
  "elecciones del 28 de febrero, destituyó a los cinco magistrados de la Sala de lo Constitucional y al fiscal "
  "general, Raúl Melara, y los sustituyó esa misma noche. La destitución se aprobó con 64 votos a favor y 19 en "
  "contra.", corr=["S082", "S083"])
F("FR-E09-002", "E09", "postura", "S083", "Despacho",
  "Según El Financiero, la iniciativa de Nuevas Ideas sostenía que los magistrados destituidos habían actuado "
  "contra la Constitución al anteponer intereses particulares a la salud de la población durante la pandemia.",
  actor="Nuevas Ideas")
F("FR-E09-003", "E09", "hecho", "S084", "Reacciones",
  "Media hora después de la destitución, la Sala de lo Constitucional saliente la declaró inconstitucional. La OEA "
  "rechazó las destituciones y el secretario de Estado de EE. UU., Antony Blinken, expresó a Bukele una profunda "
  "preocupación.", corr=["S082"])
F("FR-E09-004", "E09", "hecho", "S104", "Reelección",
  "La Constitución salvadoreña prohíbe la reelección presidencial inmediata, pero una resolución de 2021 de la "
  "Corte Suprema de Justicia habilitó a Bukele a presentarse de nuevo, y el Tribunal Supremo Electoral lo aceptó.", corr=["S102"])
F("FR-E09-005", "E09", "postura", "S085", "Comunicado del Tesoro",
  "Según el Departamento del Tesoro de EE. UU., que el 8 de diciembre de 2021 sancionó a Osiris Luna, director de "
  "Centros Penales, y a Carlos Marroquín, director de Reconstrucción del Tejido Social, ambos dirigieron en 2020 "
  "reuniones promovidas por el gobierno de Bukele para pactar una tregua secreta con líderes pandilleros.", corr=["S087"], actor="gobierno de EE. UU.")
F("FR-E09-006", "E09", "postura", "S086", "Nota",
  "Según La Prensa de Panamá, el gobierno de Bukele niega haber pactado con las pandillas, y en 2021 se había "
  "negado a extraditar a Estados Unidos a líderes de la MS-13 reclamados por la justicia de Nueva York.",
  actor="gobierno de El Salvador")

# ---------------------------------------------------------------- E10 · Marzo de 2022
F("FR-E10-001", "E10", "hecho", "S089", "Crónica",
  "Entre el 25 y el 27 de marzo de 2022 hubo 87 homicidios en El Salvador; el sábado 26 se registraron 62, el día "
  "más violento desde el fin de la guerra civil. La Policía y el gobierno atribuyeron la ola a la MS-13.",
  corr=["S088", "S091"])
F("FR-E10-002", "E10", "hecho", "S091", "Despacho de AFP",
  "El 27 de marzo de 2022 la Asamblea Legislativa aprobó, a petición de Bukele, un régimen de excepción de 30 días "
  "por las graves perturbaciones del orden público causadas por grupos delincuenciales. Votaron a favor 67 de los "
  "84 diputados.", corr=["S089"])
F("FR-E10-003", "E10", "postura", "S090", "Nota sobre la investigación de El Faro",
  "Según una investigación de El Faro recogida por Telemundo, la ola de asesinatos de marzo de 2022 se desató por "
  "la supuesta ruptura de un pacto entre el gobierno de Bukele y la MS-13. El gobierno niega haber pactado con las "
  "pandillas.", corr=["S086"], actor="El Faro")
F("FR-E10-004", "E10", "hecho", "S092", "Despacho de EFE",
  "El régimen de excepción suspende garantías como la inviolabilidad de las comunicaciones y el derecho a la "
  "defensa de los detenidos, y amplía la detención administrativa a 15 días. La Asamblea lo ha prorrogado cada "
  "30 días desde marzo de 2022.", corr=["S096"])

# ---------------------------------------------------------------- E11 · Detenciones masivas, CECOT y caída de homicidios
F("FR-E11-001", "E11", "hecho", "S094", "Introducción",
  "El Centro de Confinamiento del Terrorismo (CECOT), en Tecoluca, departamento de San Vicente, se construyó entre "
  "julio de 2022 y enero de 2023 y abrió a finales de enero de 2023. Tiene capacidad para 40.000 presos y es la "
  "cárcel más grande de América Latina; recibió a sus primeros 2.000 reclusos el 24 de febrero de 2023.",
  corr=["S093", "S095"])
F("FR-E11-002", "E11", "hecho_atribuido", "S095", "Nota de 2025",
  "Según Centroamérica 360, las autoridades no han dado cifras oficiales actualizadas de cuántos presos hay en el "
  "CECOT; en octubre de 2023 se dijo que operaba al 30 % de su capacidad.")
F("FR-E11-003", "E11", "hecho_atribuido", "S094", "Introducción",
  "Según Wikipedia, cuando abrió el CECOT, en enero de 2023, el gobierno ya había arrestado a más de 62.000 "
  "supuestos pandilleros bajo el régimen de excepción.")
F("FR-E11-004", "E11", "postura", "S096", "Datos de la Policía",
  "Según las cifras oficiales de violencia citadas por Diario El Mundo, los homicidios bajaron de 1.211 en 2021 a "
  "615 en 2022, año en que empezó el régimen, y después a 194 en 2023, 114 en 2024 y 82 en 2025.",
  actor="gobierno de El Salvador (cifras oficiales)")
F("FR-E11-005", "E11", "postura", "S100", "Publicación de Bukele en X",
  "Según Diario El Mundo, Bukele explicó en X que la disminución de los homicidios empezó antes del régimen de "
  "excepción y se acentuó a partir de 2022, cuando se aprobó.", actor="Nayib Bukele")
F("FR-E11-006", "E11", "hecho_atribuido", "S101", "Despacho de EFE",
  "Según EFE, Bukele y su gabinete de Seguridad sostienen que el régimen permitió combatir a las maras, liberar "
  "territorios que dominaban y reducir mucho los homicidios en un país que durante años estuvo entre los más "
  "violentos del mundo, aunque El Salvador ya venía con bajas sostenidas de asesinatos desde 2016.")

# ---------------------------------------------------------------- E12 · Reelección de 2024
F("FR-E12-001", "E12", "hecho", "S104", "Resultados del TSE",
  "El 4 de febrero de 2024 Bukele fue reelegido con 2.701.725 votos, el 84,65 % de los votos válidos, según el "
  "Tribunal Supremo Electoral. Nuevas Ideas ganó 54 de los 60 escaños de la Asamblea Legislativa.",
  corr=["S105", "S106"])
F("FR-E12-002", "E12", "hecho", "S105", "Antecedentes",
  "En junio de 2023 la Asamblea aprobó, a propuesta de Bukele, reducir los municipios de 262 a 44 y los "
  "diputados de 84 a 60 para la legislatura que empezó en 2024.", corr=["S130"])
F("FR-E12-003", "E12", "hecho_atribuido", "S107", "Análisis de participación",
  "Según El Diario de Hoy, de los 6.214.399 salvadoreños habilitados para votar, más de 2,9 millones no votaron "
  "en la elección presidencial de 2024; con eso, los votos de Bukele equivalen al 43,48 % del padrón electoral.")
F("FR-E12-004", "E12", "postura", "S129", "Balance de siete años",
  "Según CISPES, una organización de solidaridad crítica del gobierno, sindicatos de la salud, grupos de víctimas "
  "y organizaciones comunitarias califican de inconstitucional el gobierno de Bukele y denuncian la realidad "
  "interna detrás del internacionalmente celebrado modelo Bukele.", actor="críticos del gobierno")

# ---------------------------------------------------------------- E13 · 2025
F("FR-E13-001", "E13", "hecho", "S108", "Nota",
  "El 15 de marzo de 2025 el presidente Donald Trump invocó la Ley de Enemigos Extranjeros de 1798 contra la banda "
  "venezolana Tren de Aragua y, pese a que el juez federal James Boasberg había prohibido esos vuelos mientras "
  "decidía, ese mismo día llegaron a El Salvador 238 deportados, 23 de ellos salvadoreños señalados como "
  "pandilleros de la MS-13. Fueron recluidos en el CECOT.", corr=["S109", "S110"])
F("FR-E13-002", "E13", "hecho", "S109", "Despacho de AFP",
  "Según la Casa Blanca, Washington pagó aproximadamente 6 millones de dólares al gobierno de Bukele por recluir a "
  "esos deportados durante un año. El acuerdo lo cerraron Bukele y el secretario de Estado, Marco Rubio, y no se "
  "ha hecho público.", corr=["S108", "S110"])
F("FR-E13-003", "E13", "hecho", "S112", "Claves de la ley",
  "El 20 de mayo de 2025 la Asamblea aprobó la Ley de Agentes Extranjeros, que obliga a las personas y "
  "organizaciones que reciben fondos del exterior a inscribirse en un Registro de Agentes Extranjeros (RAEX) y "
  "les cobra un impuesto del 30 % sobre esas donaciones. Se aprobó con 57 votos.",
  corr=["S113", "S114"])
F("FR-E13-004", "E13", "postura", "S114", "Finalidad de la ley",
  "Según LexLatin, la ley declara como finalidad promover la transparencia sobre la influencia extranjera y "
  "resguardar la seguridad, la soberanía nacional y la estabilidad social y política del país.",
  actor="gobierno de El Salvador (texto de la ley)")
F("FR-E13-005", "E13", "postura", "S111", "Comunicado",
  "Según Human Rights Watch, la Ley de Agentes Extranjeros da al gobierno amplias facultades para vigilar, "
  "sancionar y cerrar a las organizaciones que estigmatiza como agentes extranjeros, y se aprobó prácticamente sin "
  "debate ni consulta pública.", actor="Human Rights Watch")
F("FR-E13-006", "E13", "hecho_atribuido", "S115", "Nota",
  "Según Los Angeles Times, en mayo de 2025 la Policía detuvo en su casa a Ruth López, directora de anticorrupción y justicia de la ONG "
  "Cristosal y crítica de Bukele, y la Fiscalía la acusó de enriquecimiento ilícito. Cristosal calificó la "
  "detención de represalia política.", corr=["S116", "S121"])

# ---------------------------------------------------------------- E14 · 2026
F("FR-E14-001", "E14", "hecho", "S098", "Sesión del 24 de junio de 2026",
  "El 24 de junio de 2026 la Asamblea aprobó la prórroga número 52 del régimen de excepción. Para entonces la "
  "medida llevaba más de cuatro años en vigor sin interrupción.", corr=["S096", "S092"])
F("FR-E14-002", "E14", "postura", "S097", "Decreto de prórroga",
  "Según el decreto de prórroga aprobado en febrero de 2026, el régimen había dejado más de 91.300 capturas de "
  "personas vinculadas a estructuras criminales, y los vínculos transnacionales y los intentos de reorganización "
  "de las pandillas justificaban mantenerlo.", actor="Asamblea Legislativa")
F("FR-E14-003", "E14", "postura", "S099", "Cifras de la PNC",
  "Según los reportes oficiales de la Policía Nacional Civil citados por El Diario de Hoy, en octubre de 2026 hubo "
  "cuatro homicidios en todo el país y 48 entre enero y octubre.", actor="gobierno de El Salvador (PNC)")
F("FR-E14-004", "E14", "postura", "S099", "Entrevista con EFE",
  "Según EFE, el vicepresidente Félix Ulloa aseguró que las condiciones que llevaron a decretar el régimen de "
  "excepción en marzo de 2022 no se han superado.", actor="Félix Ulloa")
F("FR-E14-005", "E14", "hecho", "S103", "Nota",
  "Bukele llegó a 2026 con índices altos de popularidad, que se han mantenido sin grandes cambios en sus siete "
  "años en el poder y que descansan sobre todo en la reducción de los homicidios y en el régimen de excepción.",
  corr=["S102"])
F("FR-E14-006", "E14", "postura", "S117", "Informe de Cristosal (5 de marzo de 2026)",
  "Según un informe de Cristosal presentado en Guatemala en marzo de 2026, el gobierno de Bukele tiene al menos 86 "
  "presos políticos, sobre todo defensores de derechos humanos, periodistas, funcionarios judiciales, "
  "sindicalistas y ambientalistas; Cristosal sostiene además que miles de inocentes cayeron en las detenciones "
  "masivas.", corr=["S118"], actor="Cristosal")
F("FR-E14-007", "E14", "postura", "S118", "Nota",
  "Según el Tico Times, un grupo internacional de expertos conocido como GIPES, respaldado por la Comisión "
  "Internacional de Juristas y la FIDH, concluyó en marzo de 2026 ante la CIDH que hay bases razonables para creer "
  "que se cometen crímenes de lesa humanidad; Bukele rechazó tanto esa conclusión como la acusación de presos "
  "políticos.", corr=["S120"], actor="GIPES")
F("FR-E14-008", "E14", "cifra_disputada", "S096", "Datos de ONG",
  "Las cifras de muertes bajo custodia durante el régimen las llevan organizaciones civiles y no coinciden entre "
  "sí: Diario El Mundo cita 530 fallecidos registrados por Socorro Jurídico Humanitario, y el Tico Times recoge "
  "al menos 500 según una organización salvadoreña, que afirma que la mayoría no tenía vínculos con pandillas. "
  "El gobierno no publica una cifra propia.", corr=["S119"])
F("FR-E14-009", "E14", "postura", "S119", "Nota",
  "Según el Tico Times, Bukele acusó en marzo de 2026 a las organizaciones de derechos humanos de actuar como "
  "bufetes de abogados de los criminales y dijo que su gobierno nunca atenderá sus críticas.",
  corr=["S126"], actor="Nayib Bukele")
F("FR-E14-010", "E14", "postura", "S121", "Informe mundial 2026",
  "Según el Informe Mundial 2026 de Human Rights Watch, el gobierno de Bukele siguió eliminando los controles al "
  "Poder Ejecutivo y aumentó la represión contra defensores de derechos humanos, periodistas, activistas y "
  "sindicalistas.", actor="Human Rights Watch")

# ---------------------------------------------------------------- T03 · El modelo Bukele fuera de El Salvador
F("FR-T03-001", "T03", "hecho", "S122", "Sección Honduras",
  "En Honduras, el gobierno de Xiomara Castro, de izquierda, decretó un estado de excepción en diciembre de 2022 "
  "inspirado en el salvadoreño, y en 2024 anunció planes para construir una cárcel al estilo del CECOT.",
  corr=["S123", "S124"])
F("FR-T03-002", "T03", "hecho", "S124", "Sección Ecuador",
  "En Ecuador, el presidente Daniel Noboa impuso un estado de excepción desde el 8 de enero de 2024 y presentó un "
  "plan para construir megacárceles al estilo salvadoreño.", corr=["S122"])
F("FR-T03-003", "T03", "hecho_atribuido", "S125", "Reportaje de CONNECTAS",
  "Según un reportaje de CONNECTAS publicado en agosto de 2026, en tres años los presidentes de Colombia, Ecuador, "
  "Perú, Costa Rica, Panamá y Guatemala prometieron una megacárcel como parte de su política contra el crimen.")
F("FR-T03-004", "T03", "postura", "S123", "Análisis",
  "Según un análisis de la Universidad de Navarra, la receta de Bukele no funciona igual en Honduras porque allí "
  "mata más el narcotráfico que las maras, el gobierno tiene menos poder y los cuerpos policiales son más "
  "complejos.", actor="analistas")

# ---------------------------------------------------------------- T04 · La cadena causal
F("FR-T04-001", "T04", "hecho_atribuido", "S033", "Sección sobre la diáspora",
  "Según el Migration Policy Institute, la evolución de la MS-13 y del Barrio 18 de pandillas juveniles a "
  "organizaciones transnacionales está ligada a la diáspora salvadoreña, que a su vez es producto de las guerras "
  "civiles centroamericanas de los años sesenta a noventa.")


def main():
    reg = Path("fuentes") / "registro_fuentes.csv"
    if not reg.exists():
        raise SystemExit("Corre antes agregar_lote1.py. No hago nada.")
    with reg.open(encoding="utf-8-sig", newline="") as f:
        lector = csv.DictReader(f)
        cab = lector.fieldnames
        existentes = {r["id_fuente"]: r for r in lector}
    for s in FUENTES:
        if s[0] not in existentes:
            existentes[s[0]] = dict(zip(cab, [s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[7], HOY, s[8]]))
    with reg.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cab)
        w.writeheader()
        for k in sorted(existentes):
            w.writerow(existentes[k])
    destino = Path("fuentes") / "fragmentos_lote2.jsonl"
    with destino.open("w", encoding="utf-8", newline="\n") as f:
        for fr in FRAGMENTOS:
            f.write(json.dumps(fr, ensure_ascii=False) + "\n")
    print(f"Registro: {len(existentes)} fuentes | Fragmentos: {len(FRAGMENTOS)} en {destino}")


if __name__ == "__main__":
    main()
