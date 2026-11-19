"""
agregar_lote1.py — Lote 1 de vertex-salvador: registro de fuentes y fragmentos de las épocas P01–P05 y E01–E05.

Uso (desde E:\\vertex-salvador):
    python agregar_lote1.py
Escribe (o completa sin duplicar):
    fuentes\\registro_fuentes.csv
    fuentes\\fragmentos_lote1.jsonl
Después:
    python validar.py fuentes\\fragmentos_lote1.jsonl --fragmentos

Todos los textos están redactados con palabras propias a partir de la fuente; ninguno copia párrafos.
Revisión: Claude, por encargo de Denis (17 de noviembre de 2026).
"""
import csv
import json
from pathlib import Path

HOY = "2026-11-17"
REVISOR = "Claude (por encargo de Denis)"

# id, título, autor/institución, url, tipo, licencia, perspectiva, uso, notas
FUENTES = [
    ("S001", "La insurrección campesina de 1932 (texto académico)", "Colección digital UCA", "https://coleccion.uca.edu.sv/files/original/9b48cc6897c41023c6f104b8d6a98e8508ce5cc6.pdf", "secundaria", "sin_revisar", "academica", "hechos", ""),
    ("S002", "La Matanza", "Wikipedia", "https://en.wikipedia.org/wiki/La_Matanza", "enciclopedia", "CC BY-SA", "enciclopedia", "hechos", ""),
    ("S003", "Matanza", "Encyclopedia.com (Encyclopedia of Latin American History)", "https://www.encyclopedia.com/humanities/encyclopedias-almanacs-transcripts-and-maps/matanza", "enciclopedia", "sin_revisar", "enciclopedia", "hechos", ""),
    ("S004", "El Salvador, la última revolución impulsada por Fidel en América", "T13 (con despacho de AFP)", "https://www.t13.cl/noticia/mundo/el-salvador-ultima-revolucion-impulsada-fidel-america", "prensa", "sin_revisar", "prensa", "ambos", "Sus datos sirven; sus valoraciones, como postura"),
    ("S005", "Special Report No. 90: Cuba's Renewed Support for Violence in Latin America", "Departamento de Estado de EE. UU. (1981)", "https://latinamericanstudies.org/guerrilla/report-90.htm", "primaria", "dominio_publico (obra del gobierno de EE. UU.)", "gobierno_eeuu", "postura", "Parte interesada en la Guerra Fría: solo documenta lo que afirmó el gobierno de EE. UU."),
    ("S006", "Cuba and the FMLN (artículo con entrevistas a excomandantes)", "Cold War History (Taylor & Francis)", "https://informahealthcare.com/doi/abs/10.1080/14682745.2010.545566", "secundaria", "sin_revisar", "academica", "hechos", ""),
    ("S007", "Farabundo Martí National Liberation Front", "Wikipedia", "https://en.wikipedia.org/wiki/Farabundo_Mart%C3%AD_National_Liberation_Front", "enciclopedia", "CC BY-SA", "enciclopedia", "hechos", ""),
    ("S008", "La intervención comunista en El Salvador (E/CN.4/1467)", "Delegación de EE. UU. ante la Comisión de Derechos Humanos de la ONU (1981)", "https://digitallibrary.un.org/record/645808/files/E_CN.4_1467-ES.pdf", "primaria", "documento_ONU", "gobierno_eeuu", "postura", "Informe de parte; solo como postura del gobierno de EE. UU."),
    ("S009", "OLAS - Organización Latinoamericana de Solidaridad", "Emir Sader, Enciclopedia Latinoamericana (USP)", "https://sites.usp.br/portalatinoamericano/es/espanol-olas", "enciclopedia", "sin_revisar", "academica", "hechos", ""),
    ("S010", "Murió Barbarroja (obituario de Manuel Piñeiro)", "El Tiempo (Colombia)", "https://www.eltiempo.com/archivo/documento/MAM-807828", "prensa", "sin_revisar", "prensa", "ambos", ""),
    ("S011", "El Príncipe armado: el estudio de la Tricontinental y la OLAS", "Intellèctus (revista académica, 2020)", "https://dialnet.unirioja.es/descarga/articulo/9145322.pdf", "secundaria", "acceso_abierto", "academica", "hechos", ""),
    ("S012", "El Salvador: Military dictatorships", "Encyclopaedia Britannica", "https://www.britannica.com/place/El-Salvador/Military-dictatorships", "enciclopedia", "sin_revisar", "enciclopedia", "hechos", ""),
    ("S013", "1972 Salvadoran presidential election", "Wikipedia", "https://en.wikipedia.org/wiki/1972_Salvadoran_presidential_election", "enciclopedia", "CC BY-SA", "enciclopedia", "hechos", ""),
    ("S014", "Napoleón Duarte Fuentes (biografía)", "CIDOB", "https://www.cidob.org/lider-politico/napoleon-duarte-fuentes", "secundaria", "sin_revisar", "academica", "hechos", ""),
    ("S015", "De la locura a la esperanza: un análisis de la Comisión de la Verdad", "Universidade Federal de Pelotas (2024)", "https://anais-siiepe.ufpel.edu.br/2024/CH_06227.pdf", "secundaria", "acceso_abierto", "academica", "hechos", ""),
    ("S016", "La comisión de la verdad para El Salvador", "Thomas Buergenthal, revista ECA (UCA)", "https://revistas.uca.edu.sv/index.php/eca/article/download/6925/6908/20061", "secundaria", "sin_revisar", "academica", "hechos", "El autor fue uno de los tres comisionados"),
    ("S017", "Informe de la CIDH sobre el caso Parada Cea y otros", "CIDH (vía Equipo Nizkor)", "https://www.derechos.org/nizkor/salvador/doc/parada.html", "primaria", "documento_OEA", "organismo_internacional", "ambos", "Los hechos documentados sirven; las valoraciones son de la CIDH"),
    ("S018", "El Salvador buscará nuevos acuerdos de paz (EFE)", "La Prensa (Honduras)", "https://www.laprensa.hn/mundo/el-salvador-buscara-nuevos-acuerdos-de-paz-CXLP1035564", "prensa", "sin_revisar", "prensa", "hechos", ""),
    ("S019", "El Salvador, 20 años después de la guerra civil", "Infobae (2012)", "https://www.infobae.com/2012/01/15/1042114-el-salvador-20-anos-despues-la-guerra-civil-la-paz-tiene-luces-y-sombras/", "prensa", "sin_revisar", "prensa", "hechos", ""),
    ("S020", "Ofensiva militar y firma Acuerdos de Paz", "Voz de América", "https://www.vozdeamerica.com/a/6398410.html", "prensa", "dominio_publico (obra del gobierno de EE. UU.)", "prensa", "ambos", ""),
    ("S021", "Así fue el asesinato de monseñor Romero", "Diario El Mundo (El Salvador)", "https://diario.elmundo.sv/ampArticle/asi-fue-el-asesinato-de-monsenor-romero-se-cumplen-45-anos-del-magnicidio-del-primer-santo-salvadoreno?amp=1", "prensa", "sin_revisar", "prensa", "hechos", ""),
    ("S022", "Archbishop Óscar Romero assassinated", "JURIST", "https://www.jurist.org/thisday/2010/03/24/oscar-romero-assassinated", "prensa", "sin_revisar", "prensa", "hechos", ""),
    ("S023", "March 24, 1980: Archbishop Romero Assassinated", "Zinn Education Project", "https://www.zinnedproject.org/news/tdih/romero-assassinated/", "secundaria", "sin_revisar", "academica", "ambos", ""),
    ("S024", "El Mozote massacre", "Wikipedia", "https://en.wikipedia.org/wiki/El_Mozote_massacre", "enciclopedia", "CC BY-SA", "enciclopedia", "hechos", ""),
    ("S025", "Atrocities of the Civil War in El Salvador", "ArcGIS StoryMaps (trabajo académico)", "https://storymaps.arcgis.com/stories/664e6e15950b45c9a4488750909f921b", "secundaria", "sin_revisar", "academica", "hechos", ""),
    ("S026", "De la locura a la esperanza (ficha del informe)", "Biblioteca Digital de la ONU", "https://digitallibrary.un.org/record/183599", "primaria", "documento_ONU", "organismo_internacional", "hechos", ""),
    ("S027", "Truth Commission: Commission on the Truth for El Salvador", "United States Institute of Peace", "https://usip.org/node/81361", "secundaria", "sin_revisar", "academica", "hechos", ""),
    ("S028", "Acuerdos de Chapultepec (aniversario)", "Centro de Estudios CDDRL, Universidad de Stanford", "https://cddrl.fsi.stanford.edu/taxonomy/term/215?page=5", "secundaria", "sin_revisar", "academica", "hechos", ""),
    ("S029", "16 de enero de 1992: oportunidad perdida", "El Diario de Hoy", "https://www.eldiariodehoy.com/?p=57405", "prensa", "sin_revisar", "prensa", "ambos", "Columna: sus fechas sirven; su lectura política es postura"),
    ("S030", "The Civil War (capítulo)", "California Migration Project", "https://calmigration.org/civilwar", "secundaria", "sin_revisar", "academica", "hechos", ""),
    ("S031", "La ayuda económica y militar de EE. UU.: el pilar de la contrainsurgencia", "Revista Coyuntura Económica, Universidad de El Salvador", "https://revistas.ues.edu.sv/index.php/coyunec/article/view/582/496", "secundaria", "sin_revisar", "academica", "hechos", ""),
    ("S032", "Artículo sobre el costo de la guerra (nota con cifras de EE. UU.)", "Revista ECA (UCA)", "https://revistas.uca.edu.sv/index.php/eca/article/download/6331/6289", "secundaria", "sin_revisar", "academica", "hechos", ""),
    ("S033", "Gang Membership in Central America: More Complex than It Meets the Eye", "Migration Policy Institute", "https://www.migrationpolicy.org/journal/feature/gang-membership-central-america-more-complex-meets-eye", "secundaria", "sin_revisar", "academica", "hechos", ""),
    ("S034", "National Policies and the Rise of Transnational Gangs", "Migration Policy Institute", "https://www.migrationpolicy.org/journal/feature/national-policies-and-rise-transnational-gangs", "secundaria", "sin_revisar", "academica", "hechos", ""),
    ("S035", "Mara Salvatrucha (MS-13)", "Centro Nacional Antiterrorista de EE. UU. (archivo DNI)", "https://archive.dni.gov/nctc/terrorist_groups/ms13.html", "primaria", "dominio_publico (obra del gobierno de EE. UU.)", "gobierno_eeuu", "postura", "Parte interesada: solo como postura"),
    ("S036", "MS-13", "Wikipedia", "https://www.Wikipedia.org/wiki/MS-13", "enciclopedia", "CC BY-SA", "enciclopedia", "hechos", ""),
    ("S037", "El Salvador: Mara Salvatrucha (MS-13)", "PBS Wide Angle", "https://www.pbs.org/wnet/wideangle/?p=2239", "prensa", "sin_revisar", "prensa", "hechos", ""),
    ("S038", "Central America's gang problem began in Los Angeles", "The Christian Science Monitor (2014)", "https://proof.csmonitor.com/World/Americas/2014/0806/US-export-Central-America-s-gang-problem-began-in-Los-Angeles", "prensa", "sin_revisar", "prensa", "hechos", ""),
    ("S039", "Barrio 18 (perfil)", "InSight Crime", "https://insightcrime.org/es/noticias-crimen-organizado-el-salvador/barrio-18-perfil/", "secundaria", "sin_revisar", "academica", "hechos", ""),
    ("S040", "Pandillas y extorsión en el Triángulo Norte", "InSight Crime", "https://insightcrime.org/es/?p=99326", "secundaria", "sin_revisar", "academica", "hechos", ""),
    ("S041", "Mano Dura", "Wikipedia", "https://en.wikipedia.org/wiki/Mano_Dura", "enciclopedia", "CC BY-SA", "enciclopedia", "hechos", ""),
    ("S042", "El Salvador se alista para la guerra (EFE)", "La Prensa (Honduras)", "https://www.laprensa.hn/mundo/el-salvador-se-alista-para-la-guerra-con-armas-viejas-y-atascadas-GWLP938907", "prensa", "sin_revisar", "prensa", "ambos", "Cifras de la Policía: atribuirlas"),
    ("S043", "Historia judicial fracasada contra las pandillas", "InSight Crime", "https://insightcrime.org/es/?p=8405", "secundaria", "sin_revisar", "academica", "hechos", ""),
    ("S044", "¿Quién enseñó política a las maras?", "InSight Crime", "https://insightcrime.org/es/?p=93294", "secundaria", "sin_revisar", "academica", "ambos", ""),
    ("S045", "Lanzan en El Salvador el plan Súper Mano Dura", "Infobae (2004)", "https://www.infobae.com/2004/07/19/126795-lanzan-el-salvador-el-plan-super-mano-dura/", "prensa", "sin_revisar", "prensa", "hechos", ""),
    ("S046", "Mano Dura: Gang Suppression in El Salvador", "ALAI", "https://alainet.org/es/node/148812", "secundaria", "sin_revisar", "academica", "hechos", ""),
    ("S047", "2012–2014 Salvadoran gang truce", "Wikipedia", "https://en.wikipedia.org/wiki/2012%E2%80%932014_Salvadoran_gang_truce", "enciclopedia", "CC BY-SA", "enciclopedia", "hechos", ""),
    ("S048", "Entre gritos y silencios: la narrativa de la prensa salvadoreña sobre la tregua", "Nueva Sociedad (2014)", "https://www.nuso.org/articulo/entre-gritos-y-silencios-la-narrativa-de-la-prensa-salvadorena-sobre-la-tregua-entre-pandillas/", "secundaria", "sin_revisar", "academica", "hechos", ""),
    ("S049", "Cómo se consiguió la tregua con las pandillas (Sala Negra de El Faro)", "El Faro, reproducido en Rebelión", "https://rebelion.org/como-se-consiguio-la-tregua-con-las-pandillas/", "prensa", "sin_revisar", "prensa", "ambos", "Entrevistas: lo que dicen los entrevistados es postura"),
    ("S050", "Tregua mara", "El Diario NY", "https://eldiariony.com/?p=350766", "prensa", "sin_revisar", "prensa", "ambos", ""),
    ("S051", "Condenan a Munguía Payés y al expresidente Funes por la tregua", "El Diario de Hoy", "https://www.elsalvador.com/?p=1064551", "prensa", "sin_revisar", "prensa", "hechos", ""),
    ("S052", "¿Cómo fue el pacto entre las pandillas y el gobierno por el que Funes fue condenado?", "Voz de América", "https://www.vozdeamerica.com/a/como-fue-el-pacto-entre-las-pandillas-y-el-gobierno-de-el-salvador-por-el-que-funes-fue-condenado-/7096086.html", "prensa", "dominio_publico (obra del gobierno de EE. UU.)", "prensa", "ambos", ""),
    ("S053", "Balance de homicidios 2015 en Latinoamérica", "InSight Crime", "https://insightcrime.org/?p=3653", "secundaria", "sin_revisar", "academica", "hechos", ""),
    ("S054", "El Salvador: Homicides keep rising after record-worst year (AP)", "AP vía FOX 5 DC", "https://www.fox5dc.com/news/el-salvador-homicides-keep-rising-after-record-worst-year", "prensa", "sin_revisar", "prensa", "hechos", ""),
    ("S055", "El Salvador cierra 2018 con nuevo descenso en cifra de homicidios", "El Heraldo (Honduras)", "https://www.elheraldo.hn/mundo/el-salvador-cierra-2018-con-nuevo-descenso-en-cifra-de-homicidios-ECEH1246640", "prensa", "sin_revisar", "prensa", "ambos", "Cifras de la Policía: atribuirlas"),
    ("S056", "El Salvador: registro de asesinatos alcanzó los 3.340 en 2018 (AFP)", "Revista E&N", "https://www.revistaeyn.com/centroamericaymundo/el-salvador-registro-de-asesinatos-alcanzo-los-3340-en-2018-PVEN1246810", "prensa", "sin_revisar", "prensa", "ambos", "Cifras oficiales: atribuirlas"),
    ("S057", "El Salvador is most violent nation in western hemisphere", "InSight Crime", "https://www.insightcrime.org/news/brief/el-salvador-is-most-violent-nation-in-western-hemisphere/", "secundaria", "sin_revisar", "academica", "hechos", ""),
    ("S058", "Manifiesto del PCS, las FPL y la RN al pueblo salvadoreño (10 de enero de 1980)", "Archivo Histórico Revolucionario Salvadoreño (Marxists Internet Archive)", "https://www.marxists.org/espanol/tematica/elsalvador/organizaciones/fmln/1980/ene/10.htm", "primaria", "sin_revisar", "fmln_guerrilla", "postura", "Solo documenta lo que afirmaban las organizaciones guerrilleras"),
    ("S059", "Revolutionary Party of the Central American Workers – El Salvador", "Wikipedia", "https://en.wikipedia.org/wiki/Revolutionary_Party_of_the_Central_American_Workers_%E2%80%93_El_Salvador", "enciclopedia", "CC BY-SA", "enciclopedia", "hechos", ""),
    ("S060", "Cuba-Nicaragua: Support for Central American Insurgencies (memorando de 1980)", "CIA, Sala de Lectura FOIA", "https://www.cia.gov/readingroom/node/2072180", "primaria", "dominio_publico (obra del gobierno de EE. UU.)", "gobierno_eeuu", "postura", "Evaluación de inteligencia de parte"),
    ("S061", "Departamento América y la política de Cuba hacia las guerrillas", "Estudios Interdisciplinarios de América Latina (EIAL)", "https://eialonline.org/index.php/eial/article/download/1519/1623/6174", "secundaria", "acceso_abierto", "academica", "hechos", ""),
    ("S062", "Entrevista al comandante Manuel Piñeiro sobre el Che", "Archivo Chile", "https://www.archivochile.cl/America_latina/Doc_paises_al/Cuba/Escritos_sobre_che/escritossobreche0019.pdf", "primaria", "sin_revisar", "academica", "ambos", ""),
    ("S063", "La Tricontinental y la radicalización política latinoamericana", "Jornadas de Sociología, UNLP", "https://congresos.fahce.unlp.edu.ar/jornadassociologia/x-jornadas/actas/ponencia-220822224002493806/@@display-file/file/BozzaPonmesa10.pdf", "secundaria", "acceso_abierto", "academica", "hechos", ""),
    ("S064", "The 1970s: The Road to Revolt", "Library of Congress Country Studies (vía countrystudies.us)", "https://countrystudies.us/el-salvador/12.htm", "secundaria", "dominio_publico (obra del gobierno de EE. UU.)", "academica", "hechos", ""),
    ("S065", "El Salvador en la década de los 70: las oportunidades perdidas", "Héctor Grenni, Teoría y Praxis (2014)", "https://core.ac.uk/download/236034915.pdf", "secundaria", "acceso_abierto", "academica", "hechos", ""),
    ("S066", "Anniversary of La Matanza", "El Salvador Perspectives", "https://www.elsalvadorperspectives.com/2020/01/anniversary-of-la-matanza.html", "secundaria", "sin_revisar", "academica", "hechos", ""),
    ("S067", "Dead Communists in Nahuizalco", "Universidad del Sur de California (Scalar)", "https://scalar.usc.edu/works/felix-panameno/media/dead-communists", "secundaria", "sin_revisar", "academica", "hechos", ""),
    ("S068", "Farabundo Martí", "Wikipedia", "https://www.wikipedia.com/wiki/Farabundo_Mart%C3%AD", "enciclopedia", "CC BY-SA", "enciclopedia", "hechos", ""),
]

FRAGMENTOS = []


def F(fid, etapa, tipo, fuente, ubic, texto, corr=(), actor=None, testigo=None):
    d = {"id": fid, "etapa": etapa, "tipo": tipo, "id_fuente": fuente, "ubicacion": ubic,
         "corroborado_por": list(corr), "texto": texto, "notas": "", "revisado": True, "estado": "aprobado",
         "revisor": REVISOR, "fecha_revision": HOY}
    if actor:
        d["actor"] = actor
    if testigo:
        d["testigo"] = testigo
    FRAGMENTOS.append(d)


# ---------------------------------------------------------------- P01 · Reforma agraria y café
F("FR-P01-001", "P01", "hecho_atribuido", "S001", "Sección sobre las causas de 1932",
  "Según un texto académico de la colección de la UCA, la Reforma Agraria Liberal de 1881-1882 suprimió la "
  "propiedad comunal de la tierra; eso llevó a concentrar la tierra en pocas manos y a dedicarla al café, y muchos "
  "campesinos perdieron las tierras que trabajaban.")

# ---------------------------------------------------------------- P02 · Crisis, Partido Comunista y 1932
F("FR-P02-001", "P02", "hecho_atribuido", "S001", "Sección sobre las causas de 1932",
  "Según el mismo texto de la colección de la UCA, con la crisis de 1929 se hundieron los precios internacionales "
  "del café: la economía salvadoreña quedó con excedentes de café y sin liquidez, los salarios cayeron por debajo "
  "de lo necesario para subsistir y hubo desempleo masivo.")
F("FR-P02-002", "P02", "hecho", "S002", "Sección 'Social unrest'",
  "Farabundo Martí, uno de los dirigentes rurales de la Federación Regional de Trabajadores, fundó en 1930 el "
  "Partido Comunista de El Salvador junto con Miguel Mármol. Antes había luchado en Nicaragua junto a Augusto "
  "César Sandino contra la ocupación estadounidense.", corr=["S068"])
F("FR-P02-003", "P02", "hecho", "S002", "Encabezado y sección 'Rebellion'",
  "Entre el 22 y el 25 de enero de 1932 hubo un levantamiento en el occidente de El Salvador encabezado por "
  "comunistas, con Farabundo Martí, y por indígenas, con Feliciano Ama. El gobierno del general Maximiliano "
  "Hernández Martínez lo aplastó, y esa represión se conoce como La Matanza.", corr=["S003", "S066"])
F("FR-P02-004", "P02", "hecho_atribuido", "S003", "Entrada 'Matanza'",
  "Según la Encyclopedia of Latin American History, la revuelta de 1932 nació del enojo de los trabajadores del "
  "café y de los campesinos por sus condiciones de vida, y de la agitación de los dirigentes del Partido "
  "Comunista, en especial de su secretario general, Farabundo Martí.")
F("FR-P02-005", "P02", "cifra_disputada", "S066", "Párrafo inicial",
  "El número de muertos de La Matanza de 1932 no está fijado: El Salvador Perspectives habla de decenas de miles "
  "de campesinos muertos en la represión del ejército, y un trabajo de la Universidad del Sur de California da "
  "más de 30.000 hombres, mujeres y niños. Durante el levantamiento, según Wikipedia, los rebeldes mataron a unas "
  "2.000 personas.", corr=["S067", "S002"])
F("FR-P02-006", "P02", "hecho", "S068", "Ficha biográfica",
  "Farabundo Martí fue fusilado el 1 de febrero de 1932 en San Salvador, a los 38 años. Casi medio siglo después, "
  "la coalición guerrillera de 1980 tomó su nombre: Frente Farabundo Martí para la Liberación Nacional.",
  corr=["S007"])

# ---------------------------------------------------------------- P03 · Gobiernos militares
F("FR-P03-001", "P03", "hecho", "S013", "Resultados",
  "En las elecciones presidenciales del 20 de febrero de 1972, Arturo Armando Molina, del Partido de Conciliación "
  "Nacional (PCN), fue declarado ganador con el 43 % de los votos. La junta electoral de San Salvador había "
  "anunciado que ganaba José Napoleón Duarte, candidato de la oposición unida, por unos 6.000 votos.",
  corr=["S012"])
F("FR-P03-002", "P03", "hecho", "S012", "Sección 'Military dictatorships'",
  "Tras las elecciones de 1972 hubo un intento de golpe que solo sirvió para que Duarte fuera arrestado y "
  "desterrado a Venezuela, donde vivió hasta 1979.", corr=["S014"])
F("FR-P03-003", "P03", "hecho", "S065", "Palabras clave y sección sobre 1972 y 1977",
  "Las elecciones presidenciales de 1972 y de 1977 estuvieron marcadas por denuncias de fraude. Según los "
  "estudios de país de la Biblioteca del Congreso de EE. UU., la votación de 1977 se manipuló de forma aún más "
  "descarada que la de 1972. En los años setenta crecieron la represión y la frustración de la oposición.",
  corr=["S064"])
F("FR-P03-004", "P03", "hecho", "S012", "Sección 'Military dictatorships'",
  "Hacia 1979 operaban en El Salvador varias organizaciones guerrilleras separadas. En octubre de 1979 un golpe "
  "militar sacó del poder al general Carlos Humberto Romero.", corr=["S014"])
F("FR-P03-005", "P03", "hecho_atribuido", "S014", "Biografía de Duarte",
  "Según la biografía del CIDOB, tras el golpe de octubre de 1979 tomó el poder una Junta Revolucionaria de "
  "Gobierno de cinco miembros: dos coroneles, Adolfo Majano y Jaime Abdul Gutiérrez, y tres civiles, entre ellos "
  "Guillermo Manuel Ungo.")
F("FR-P03-006", "P03", "hecho_atribuido", "S030", "Capítulo sobre la guerra civil",
  "Según el California Migration Project, la junta que sustituyó al general Romero en 1979 intentó algunas "
  "reformas agrarias y nacionalizó el comercio del café, mientras Estados Unidos, con Cuba y Nicaragua ya "
  "gobernadas por revoluciones, buscaba impedir que la revolución se extendiera por el continente.")

# ---------------------------------------------------------------- P04 · Revolución cubana y su expansión
F("FR-P04-001", "P04", "hecho", "S011", "Introducción",
  "Del 3 al 15 de enero de 1966 La Habana acogió la Conferencia Tricontinental, con 512 delegados de 82 países de "
  "Asia, África y América Latina. De ella nació la Organización de Solidaridad de los Pueblos de Asia, África y "
  "América Latina (OSPAAAL), y la conferencia declaró su apoyo a la lucha armada.", corr=["S063"])
F("FR-P04-002", "P04", "hecho_atribuido", "S009", "Entrada 'OLAS'",
  "Según el sociólogo Emir Sader, tras la Tricontinental Cuba convocó en 1967 la Organización Latinoamericana de "
  "Solidaridad (OLAS), que optó abiertamente por la lucha armada y las guerrillas. Cuando la lucha armada se "
  "reanudó en la década siguiente, con el centro en Centroamérica, la OLAS ya se había convertido en un órgano de "
  "difusión sin capacidad real de coordinar a los movimientos.")
F("FR-P04-003", "P04", "cifra_disputada", "S010", "Obituario",
  "Manuel Piñeiro, apodado Barbarroja, dirigió durante años el Departamento América del Comité Central del "
  "Partido Comunista de Cuba, encargado de centralizar el control y la ayuda a los grupos insurgentes de América "
  "Latina. El diario El Tiempo fecha en 1974 el inicio de su mando y una entrevista recogida por Archivo Chile lo "
  "sitúa desde 1975.", corr=["S062"])
F("FR-P04-004", "P04", "hecho_atribuido", "S061", "Resumen e introducción",
  "Según un estudio publicado en la revista EIAL, el Departamento América fue el aparato de enlace de Cuba con "
  "las guerrillas de América Latina y el Caribe y, más tarde, también representó al Partido en la diplomacia "
  "cubana.")
F("FR-P04-005", "P04", "postura", "S005", "Sección sobre la teoría cubana de la revolución",
  "Según un informe especial del Departamento de Estado de EE. UU. de 1981, el gobierno de Castro quiso desde el "
  "principio reproducir en otros países la guerra de guerrillas rural del Movimiento 26 de Julio, y Fidel Castro "
  "declaró el 26 de julio de 1980 que Guatemala, El Salvador, Chile y Bolivia enseñaban que no había otra fórmula "
  "que la lucha armada revolucionaria.", actor="gobierno de EE. UU.")

# ---------------------------------------------------------------- P05 · Unificación y nacimiento del FMLN
F("FR-P05-001", "P05", "hecho_atribuido", "S004", "Despacho de AFP",
  "Según un despacho de AFP publicado por T13, Fidel Castro, animado por el triunfo sandinista de julio de 1979, "
  "apoyó con decisión a la guerrilla salvadoreña, entonces dispersa; las cinco organizaciones guerrilleras "
  "fundaron el FMLN en La Habana el 10 de octubre de 1980, y en noviembre de 1989 Castro apoyó la ofensiva "
  "guerrillera sobre San Salvador.")
F("FR-P05-002", "P05", "hecho", "S007", "Sección de historia",
  "El FMLN se formó el 10 de octubre de 1980 como coalición de cinco organizaciones de izquierda: las Fuerzas "
  "Populares de Liberación (FPL), el Ejército Revolucionario del Pueblo (ERP), la Resistencia Nacional (RN), el "
  "Partido Comunista Salvadoreño (PCS) y el Partido Revolucionario de los Trabajadores Centroamericanos (PRTC), "
  "que se sumó el 5 de diciembre de 1980.", corr=["S059"])
F("FR-P05-003", "P05", "postura", "S008", "Resumen del informe",
  "Según el informe que la delegación de Estados Unidos presentó en 1981 ante la Comisión de Derechos Humanos de "
  "la ONU, Fidel Castro y el gobierno cubano tuvieron un papel tutelar directo entre finales de 1979 y principios "
  "de 1980 para agrupar a las facciones guerrilleras salvadoreñas en un frente unificado, y asesoraron a los "
  "guerrilleros en la planificación de sus operaciones militares.", actor="gobierno de EE. UU.")
F("FR-P05-004", "P05", "postura", "S060", "Memorando de inteligencia de 1980",
  "Según un memorando de la CIA de 1980, ya desclasificado, el papel personal de Fidel Castro en lograr cierta "
  "unidad entre las organizaciones guerrilleras centroamericanas estaba detallado en informes de otras fuentes.",
  actor="gobierno de EE. UU.")
F("FR-P05-005", "P05", "hecho_atribuido", "S006", "Notas 2 y 19 del artículo",
  "Según un artículo de Cold War History basado en entrevistas con excomandantes del FMLN como Ana Guadalupe "
  "Martínez, Salvador Sánchez Cerén y Facundo Guardado, los dirigentes coincidieron en que Cuba encarnaba la "
  "posibilidad del cambio y en que Fidel Castro y el Che Guevara eran ejemplos del revolucionario ideal; Joaquín "
  "Villalobos, Eduardo Sancho y Claudio Armijo contaron que el Departamento América era la vía para llegar a "
  "Castro.")
F("FR-P05-006", "P05", "postura", "S058", "Apartado I del manifiesto",
  "Según el manifiesto que el Partido Comunista, las FPL y la Resistencia Nacional publicaron el 10 de enero de "
  "1980, la lucha del pueblo salvadoreño tenía hondas raíces históricas propias: la oposición a los gobiernos de "
  "la familia Meléndez-Quiñónez y la lucha encabezada por Farabundo Martí.", actor="organizaciones guerrilleras")

# ---------------------------------------------------------------- E01 · Guerra civil y paz
F("FR-E01-001", "E01", "hecho", "S021", "Crónica del asesinato",
  "El arzobispo de San Salvador, monseñor Óscar Arnulfo Romero, fue asesinado de un disparo el 24 de marzo de "
  "1980 mientras celebraba misa en la capilla de un hospital de San Salvador.", corr=["S022"])
F("FR-E01-002", "E01", "hecho_atribuido", "S023", "Ficha del 24 de marzo",
  "Según el Zinn Education Project, en febrero de 1980 monseñor Romero escribió al presidente Jimmy Carter para "
  "pedirle que detuviera la ayuda militar de Estados Unidos al gobierno salvadoreño.")
F("FR-E01-003", "E01", "hecho_atribuido", "S024", "Introducción",
  "Según Wikipedia, el 11 de diciembre de 1981, en El Mozote y caseríos vecinos del departamento de Morazán, el "
  "ejército salvadoreño mató a más de 800 civiles. La operación la hicieron unidades del Batallón Atlacatl, una "
  "unidad de reacción rápida creada en 1980.", corr=["S025"])
F("FR-E01-004", "E01", "hecho", "S016", "Introducción del artículo de Buergenthal",
  "La Comisión de la Verdad para El Salvador se constituyó el 15 de julio de 1992 en cumplimiento de los Acuerdos "
  "de Paz, con tres miembros nombrados por el secretario general de la ONU: Belisario Betancur, Reinaldo Figueredo "
  "y Thomas Buergenthal. Su informe, «De la locura a la esperanza», se hizo público el 15 de marzo de 1993.",
  corr=["S026", "S027"])
F("FR-E01-005", "E01", "hecho_atribuido", "S015", "Introducción",
  "Según un análisis académico de la Universidad Federal de Pelotas, el informe de la Comisión de la Verdad "
  "atribuyó al ejército y a grupos paramilitares el 85 % de las violaciones que documentó, y responsabilizó al "
  "FMLN de una parte menor.")
F("FR-E01-006", "E01", "hecho_atribuido", "S017", "Párrafo 5",
  "Según la Comisión Interamericana de Derechos Humanos, el 18 de marzo de 1993, tres días después de publicarse "
  "el informe de la Comisión de la Verdad, el presidente Alfredo Cristiani anunció una amnistía general que dejó "
  "sin castigo los crímenes cometidos por agentes del Estado entre 1980 y 1992.")
F("FR-E01-007", "E01", "hecho", "S019", "Párrafo inicial",
  "El 16 de enero de 1992, en el castillo de Chapultepec, en Ciudad de México, el gobierno de Alfredo Cristiani y "
  "la comandancia del FMLN firmaron, con mediación de la ONU, los acuerdos de paz que pusieron fin a doce años de "
  "guerra.", corr=["S028", "S018"])
F("FR-E01-008", "E01", "hecho_atribuido", "S029", "Columna",
  "Según El Diario de Hoy, el camino a la paz empezó con un primer acercamiento en la iglesia de La Palma, "
  "Chalatenango, el 15 de octubre de 1984, y el primer acuerdo, el de Ginebra, se firmó el 4 de abril de 1990 y "
  "sirvió de base para los acuerdos de 1992.")
F("FR-E01-009", "E01", "cifra_disputada", "S018", "Despacho de EFE",
  "Las cifras del costo humano de la guerra varían según la fuente: un despacho de EFE da más de 75.000 muertos y "
  "7.000 desaparecidos, y la Voz de América habla de 75.000 muertos, 8.000 desaparecidos y 12.000 presos.",
  corr=["S020"])
F("FR-E01-010", "E01", "cifra_disputada", "S030", "Capítulo sobre la guerra civil",
  "La ayuda de Estados Unidos a El Salvador durante la guerra se calcula de formas distintas: el California "
  "Migration Project da más de 6.000 millones de dólares entre 1979 y 1991; un estudio de la Universidad de El "
  "Salvador cuenta 3.348,5 millones de dólares de ayuda económica y militar entre 1980 y 1988 a través de la AID; "
  "y una nota de la revista ECA señala que la cifra que más se repite es de 5.000 millones.",
  corr=["S031", "S032"])

# ---------------------------------------------------------------- E02 · Las maras nacen en Los Ángeles
F("FR-E02-001", "E02", "hecho", "S036", "Encabezado",
  "La Mara Salvatrucha (MS-13) nació en los años ochenta en el barrio de Pico-Union, en Los Ángeles, para proteger "
  "a los inmigrantes salvadoreños de otras pandillas de la zona. La formaron jóvenes salvadoreños que habían huido "
  "de la guerra civil o eran hijos de refugiados.", corr=["S035", "S037"])
F("FR-E02-002", "E02", "hecho_atribuido", "S033", "Sección sobre la diáspora",
  "Según el Migration Policy Institute, la diáspora salvadoreña en Estados Unidos es en gran parte producto de las guerras civiles centroamericanas, en "
  "las que Washington apoyó a los gobiernos que combatían a las guerrillas. En 2019 sumaba 1,4 millones de "
  "personas, y el grupo más grande vivía en Los Ángeles.")
F("FR-E02-003", "E02", "hecho", "S034", "Resumen",
  "Las deportaciones desde Estados Unidos se triplicaron a finales de los años noventa y llevaron la MS-13 a "
  "Centroamérica, donde los miembros deportados abrieron nuevos grupos. El paso de pandilla juvenil a pandilla "
  "carcelaria y a organización transnacional se dio en esa década, con la ola de deportaciones de inmigrantes con "
  "antecedentes penales que permitieron las leyes de la época del presidente Clinton.", corr=["S033", "S035"])
F("FR-E02-004", "E02", "hecho", "S038", "Artículo de 2014",
  "El ir y venir constante entre Los Ángeles y Centroamérica permitió que el Barrio 18 y la MS-13 se asentaran en "
  "El Salvador entre finales de los ochenta y principios de los noventa.", corr=["S034"])
F("FR-E02-005", "E02", "hecho_atribuido", "S041", "Sección de antecedentes",
  "Según Wikipedia, tras la llegada de las pandillas desde Los Ángeles, la tasa de homicidios de El Salvador llegó "
  "a 139 por cada 100.000 habitantes en 1995.")

# ---------------------------------------------------------------- T02 · Estructura de las pandillas
F("FR-T02-001", "T02", "hecho", "S040", "Sección sobre estructura",
  "La MS-13 y el Barrio 18 se dividen en células llamadas clicas, que funcionan con bastante autonomía; las clicas "
  "se agrupan en programas, que responden a una dirección llamada ranfla. La extorsión es una de sus fuentes de "
  "dinero más importantes, y en general se considera que la MS-13 es la más sofisticada de las dos.",
  corr=["S039"])
F("FR-T02-002", "T02", "hecho_atribuido", "S039", "Perfil",
  "Según InSight Crime, hacia 2005, peleas internas partieron al Barrio 18 en El Salvador en dos facciones rivales, los "
  "Revolucionarios y los Sureños, que desde entonces también se enfrentan entre sí. El Salvador declaró al Barrio "
  "18 organización terrorista el 24 de agosto de 2015.")

# ---------------------------------------------------------------- E03 · Mano Dura y Súper Mano Dura
F("FR-E03-001", "E03", "hecho", "S042", "Antecedentes",
  "A mediados de 2003 el presidente Francisco Flores, de ARENA, lanzó el plan Mano Dura: capturas sistemáticas de "
  "pandilleros y apoyo de la Fuerza Armada a la Policía en las calles. El plan se presentó en cadena nacional el "
  "23 de julio de 2003.", corr=["S041", "S046"])
F("FR-E03-002", "E03", "hecho_atribuido", "S043", "Sección sobre El Salvador",
  "Según InSight Crime, la Ley Antimaras entró en vigor el 10 de octubre de 2003; según la Policía, el plan Mano Dura dejó 19.275 "
  "arrestos entre julio de 2003 y agosto de 2004, y 17.540 de esos detenidos quedaron libres por falta de pruebas.")
F("FR-E03-003", "E03", "hecho_atribuido", "S044", "Artículo",
  "Según InSight Crime, a quienes sufrían a las pandillas no les importó que la Ley Antimaras de Flores fuera "
  "inconstitucional: el plan Mano Dura reanimó al presidente y devolvió a su partido al camino de la victoria "
  "electoral.")
F("FR-E03-004", "E03", "hecho", "S043", "Sección sobre El Salvador",
  "El 30 de agosto de 2004, a los 60 días de asumir, el presidente Antonio Saca, también de ARENA, presentó el "
  "plan Súper Mano Dura para aumentar las capturas de pandilleros. Lo acompañó de programas de prevención y "
  "reinserción llamados Mano Amiga y Mano Extendida.", corr=["S044", "S046"])
F("FR-E03-005", "E03", "postura", "S045", "Rueda de prensa de 2004",
  "Según Infobae, al anunciar su plan en 2004 Antonio Saca afirmó que, si lanzaba el Súper Mano Dura, era porque "
  "el Mano Dura había sido efectivo.", actor="Antonio Saca")
F("FR-E03-006", "E03", "hecho_atribuido", "S033", "Puntos clave",
  "Según el Migration Policy Institute, la Mano Dura arrestó a más de 30.000 supuestos pandilleros entre 2003 y "
  "2005 y, sin buscarlo, convirtió las cárceles en centros de reclutamiento de las pandillas.")
F("FR-E03-007", "E03", "cifra_disputada", "S042", "Cifras de la Policía",
  "Los resultados de la Mano Dura se leen de forma distinta según la fuente. Con cifras de la Policía citadas por "
  "EFE, hubo 2.340 muertes violentas en 1999, 2.388 en 2003 y 2.933 en 2004. Wikipedia, en cambio, recoge un "
  "descenso del 14 % de los asesinatos en 2004, seguido de una subida hasta 64,7 por cada 100.000 habitantes en "
  "2006.", corr=["S041"])

# ---------------------------------------------------------------- E04 · La tregua
F("FR-E04-001", "E04", "hecho", "S047", "Ficha y resumen",
  "La tregua entre pandillas duró del 9 de marzo de 2012 al 26 de mayo de 2014. Sus principales negociadores "
  "fueron el ministro de Seguridad, David Munguía Payés, el exdiputado y exguerrillero Raúl Mijango y el obispo "
  "Fabio Colindres, bajo la supervisión del presidente Mauricio Funes.", corr=["S049"])
F("FR-E04-002", "E04", "hecho", "S048", "Párrafo inicial",
  "El 14 de marzo de 2012 el periódico El Faro informó del traslado de 30 líderes pandilleros de la cárcel de "
  "máxima seguridad a otros penales, y dijo que respondía a una negociación del gobierno con las pandillas a "
  "cambio de bajar los homicidios. Las autoridades dieron explicaciones contradictorias, pero los homicidios "
  "cayeron un 53 % a partir del traslado.", corr=["S049"])
F("FR-E04-003", "E04", "postura", "S048", "Párrafo sobre el ministro",
  "Según Nueva Sociedad, el ministro David Munguía Payés venía afirmando que la guerra entre pandillas causaba el "
  "90 % de los homicidios de los diez años anteriores; en una entrevista con El Faro dijo después que quien "
  "controlara esa guerra iba a controlar el 75 % de las muertes del país.", corr=["S049"],
  actor="David Munguía Payés")
F("FR-E04-004", "E04", "hecho_atribuido", "S048", "Párrafo inicial",
  "Según Nueva Sociedad, el 14 de abril de 2012, en la Cumbre de las Américas, el presidente Mauricio Funes anunció que El Salvador "
  "tenía su primer día sin homicidios en casi tres años.")
F("FR-E04-005", "E04", "hecho_atribuido", "S050", "Artículo",
  "Según El Diario NY, entre marzo y diciembre de 2011 hubo 3.697 homicidios, y en el mismo periodo de 2012, ya "
  "con la tregua, 1.761.")
F("FR-E04-006", "E04", "hecho", "S051", "Nota sobre la sentencia",
  "En 2023 un tribunal de San Salvador condenó al exministro David Munguía Payés a 18 años de cárcel y al "
  "expresidente Mauricio Funes, juzgado en ausencia, a 14 años, por la tregua de 2012, por agrupaciones ilícitas e "
  "incumplimiento de deberes. Raúl Mijango fue absuelto en 2017 y en 2019.", corr=["S047", "S052"])
F("FR-E04-007", "E04", "postura", "S052", "Artículo",
  "Según la Voz de América, la Fiscalía sostuvo que Munguía Payés fue el autor intelectual de la tregua, cuya "
  "ruptura convirtió a El Salvador en 2015 en el país más violento del mundo, y que Funes aprobó el acuerdo y "
  "dispuso dinero público para el proceso.", actor="Fiscalía de El Salvador")

# ---------------------------------------------------------------- E05 · Pico de violencia 2015-2018
F("FR-E05-001", "E05", "hecho", "S053", "Sección El Salvador",
  "En 2015 El Salvador fue el país más violento del hemisferio occidental. Según las estadísticas oficiales, hubo "
  "al menos 6.657 homicidios, con una tasa de unos 103 por cada 100.000 habitantes, la más alta de su historia.",
  corr=["S054", "S055"])
F("FR-E05-002", "E05", "hecho_atribuido", "S057", "Resumen",
  "Según InSight Crime, lo que llevó a El Salvador a ese récord en 2015 fue una combinación de fragmentación de las "
  "pandillas, choques internos y grupos de justicia por mano propia.")
F("FR-E05-003", "E05", "hecho", "S056", "Despacho de AFP",
  "Según fuentes oficiales, después de 2015 la tasa de homicidios fue bajando: 81 por cada 100.000 habitantes en "
  "2016, 60 en 2017 y 51 en 2018, año en que se registraron 3.340 asesinatos.", corr=["S055"])
F("FR-E05-004", "E05", "postura", "S055", "Declaraciones del ministro",
  "Según El Heraldo, en 2018 las autoridades salvadoreñas atribuían la mayor parte de los homicidios a las "
  "pandillas, a las que calculaban algo más de 70.000 miembros, unos 17.000 de ellos presos; el ministro de "
  "Seguridad atribuyó la baja de ese año al combate contra la delincuencia y a programas de prevención y "
  "rehabilitación.", actor="gobierno de El Salvador (2018)")


def main():
    base = Path(".")
    (base / "fuentes").mkdir(exist_ok=True)
    reg = base / "fuentes" / "registro_fuentes.csv"
    cab = ["id_fuente", "titulo", "autor_institucion", "url", "tipo", "licencia", "perspectiva", "uso",
           "fecha_consulta", "notas"]
    existentes = {}
    if reg.exists():
        with reg.open(encoding="utf-8-sig", newline="") as f:
            existentes = {r["id_fuente"]: r for r in csv.DictReader(f)}
    for s in FUENTES:
        if s[0] not in existentes:
            existentes[s[0]] = dict(zip(cab, [s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[7], HOY, s[8]]))
    with reg.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cab)
        w.writeheader()
        for k in sorted(existentes):
            w.writerow(existentes[k])

    destino = base / "fuentes" / "fragmentos_lote1.jsonl"
    with destino.open("w", encoding="utf-8", newline="\n") as f:
        for fr in FRAGMENTOS:
            f.write(json.dumps(fr, ensure_ascii=False) + "\n")
    print(f"Registro: {len(existentes)} fuentes en {reg}")
    print(f"Fragmentos: {len(FRAGMENTOS)} en {destino}")


if __name__ == "__main__":
    main()
