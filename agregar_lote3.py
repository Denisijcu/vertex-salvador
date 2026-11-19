"""
agregar_lote3.py — Lote 3 de vertex-salvador: época E15, Haití (2024–2026).

Uso (desde E:\\vertex-salvador, después de agregar_lote1.py y agregar_lote2.py):
    python agregar_lote3.py
    python validar.py fuentes\\fragmentos_lote3.jsonl --fragmentos

Reglas de este lote:
- Lo que dicen Bukele, su gabinete, el gobierno de Haití, el de EE. UU., Amnistía Internacional o UNA-Haití va
  SIEMPRE como postura atribuida. Ninguna de esas voces pasa como hecho por sí sola.
- Los hechos (la resolución de la ONU, las leyes, la emboscada, el despliegue, el estadio) llevan fuente y,
  cuando se puede, otra que lo corrobora.
- El caso de los cuatro aerotécnicos sigue abierto: los datos llegan al 18 de noviembre de 2026 y el modelo
  tiene que decir esa fecha en vez de inventar un desenlace.
Revisión: Claude, por encargo de Denis (18 de noviembre de 2026).
"""
import csv
import json
from pathlib import Path

REVISOR = "Claude (por encargo de Denis)"
HOY = "2026-11-18"

FUENTES = [
    ("S131", "Ley de participación de la Fuerza Armada en la Fuerza de Supresión de Pandillas en Haití", "El Diario de Hoy", "https://www.eldiariodehoy.com/?p=97321", "prensa", "sin_revisar", "prensa", "hechos", ""),
    ("S132", "El Salvador autoriza que sus militares en Haití participen en fuerza antipandillas un año más (EFE)", "Diario El Mundo", "https://diario.elmundo.sv/politica/el-salvador-autoriza-que-sus-militares-en-haiti-participen-en-fuerza-antipandillas-durante-un-ano-mas-prorrogable", "prensa", "sin_revisar", "prensa", "hechos", ""),
    ("S133", "Prorrogan por un año más misión de militares salvadoreños en Haití", "Diario El Mundo", "https://diario.elmundo.sv/politica/prorrogan-por-un-ano-mas-mision-de-militares-salvadorenos-en-haiti", "prensa", "sin_revisar", "prensa", "hechos", ""),
    ("S134", "Security Council Authorizes Transition of Multinational Security Support Mission in Haiti to 'Gang Suppression Force' (SC/16185)", "Naciones Unidas", "https://press.un.org/en/2025/sc16185.doc.htm", "primaria", "dominio_publico", "organismo_internacional", "hechos", ""),
    ("S135", "UNSC Votes to Deploy Gang Suppression Force in Haiti", "AllAfrica / Capital FM", "https://allafrica.com/stories/202510010087.html", "prensa", "sin_revisar", "prensa", "hechos", ""),
    ("S136", "Soldados de El Salvador se unen a misión en Haití para combatir violencia", "Voz de América", "https://www.vozdeamerica.com/a/soldados-el-salvador-se-unen-mision-respaldada-onu-en-haiti-/7962909.html", "prensa", "sin_revisar", "prensa", "hechos", ""),
    ("S137", "Cuatro soldados salvadoreños permanecen desaparecidos tras una emboscada en Haití", "Infobae", "https://www.infobae.com/el-salvador/2026/10/19/cinco-soldados-salvadorenos-permanecen-desaparecidos-tras-una-emboscada-en-haiti/", "prensa", "sin_revisar", "prensa", "hechos", ""),
    ("S138", "Se cumple un mes de la desaparición de cuatro salvadoreños en Haití, esto se sabe", "El Diario de Hoy", "https://www.elsalvador.com/noticias/nacional/-cuatro-salvadorenos-desaparecidos-haiti-mes/1304753/2026/", "prensa", "sin_revisar", "prensa", "ambos", "Cronología al 18 de noviembre de 2026"),
    ("S139", "EE. UU. cree que los cuatro militares salvadoreños desaparecidos en Haití sobrevivieron (AP)", "Diario Libre", "https://www.diariolibre.com/mundo/estados-unidos/2026/10/20/militares-salvadorenos-desaparecidos-en-haiti-tras-emboscada/3694694", "prensa", "sin_revisar", "prensa", "ambos", "Lo que dice el embajador de EE. UU. es postura"),
    ("S140", "Bukele moviliza blindados y helicópteros a Haití (EFE)", "Emol", "https://www.emol.com/noticias/Internacional/2026/10/29/1215603/bukele-moviliza-blindados-helicopteros-haiti.html", "prensa", "sin_revisar", "prensa", "ambos", ""),
    ("S141", "Bukele a haitianos: esto no es una operación contra el pueblo haitiano ni una invasión", "Diario El Mundo", "https://diario.elmundo.sv/politica/bukele-a-haitianos-esto-no-es-una-operacion-contra-el-pueblo-haitiano-ni-una-invasion-a-haiti", "prensa", "sin_revisar", "prensa", "ambos", "Declaraciones de Bukele: atribuirlas"),
    ("S142", "Bukele anuncia una base operativa en el principal estadio de Haití (EFE)", "TuNota", "https://www.tunota.com/mundo/bukele-anuncia-una-base-operativa-una-fuerte-ofensiva-estadio-haiti-2026-11-12", "prensa", "sin_revisar", "prensa", "ambos", ""),
    ("S143", "Bukele redobla su ofensiva en Haití: base operativa en el estadio de la selección", "NTN24", "https://www.ntn24.com/noticias-actualidad/bukele-redobla-su-ofensiva-armada-en-haiti-anuncio-base-operativa-en-estadio-de-la-seleccion-y-advirtio-a-pandilleros-665942", "prensa", "sin_revisar", "prensa", "hechos", ""),
    ("S144", "Bukele dice que ayudará a los haitianos a retomar el país (EFE)", "Revista E&N", "https://www.revistaeyn.com/centroamericaymundo/el-presidente-nayib-bukele-dice-que-ayudara-a-los-haitianos-a-retomar-el-pais-DH32535655", "prensa", "sin_revisar", "prensa", "ambos", ""),
    ("S145", "Con ayuda de El Salvador, Haití asegura estar recuperando control de territorio (EFE)", "Revista E&N", "https://www.revistaeyn.com/centroamericaymundo/con-ayuda-de-el-salvador-haiti-asegura-estar-recuperando-control-de-territorio-PH32606955", "prensa", "sin_revisar", "prensa", "ambos", "Lo que dice el gobierno haitiano es postura"),
    ("S146", "Mayoría del despliegue salvadoreño en Haití no está bajo la fuerza antipandillas, dice la ONU", "Diario El Mundo", "https://diario.elmundo.sv/politica/mayoria-de-despliegue-salvadoreno-en-haiti-no-esta-bajo-fuerza-antipandillas-dice-la-onu", "prensa", "sin_revisar", "prensa", "hechos", ""),
    ("S147", "Amnistía Internacional pide a El Salvador y Haití respetar derechos en el despliegue; diputado critica a la organización", "Diario El Mundo", "https://diario.elmundo.sv/politica/amnistia-internacional-pide-a-el-salvador-y-haiti-respetar-derechos-en-despliegue-diputado-critica-a-organizacion", "prensa", "sin_revisar", "prensa", "ambos", ""),
    ("S148", "El Salvador retirará sus tropas de Haití en cuanto rescate a sus cuatro militares", "Euronews", "https://es.euronews.com/2026/11/17/el-salvador-retirara-sus-tropas-de-haiti-en-cuanto-rescate-a-sus-4-militares", "prensa", "sin_revisar", "prensa", "ambos", ""),
    ("S149", "UNA-Haití denuncia muertes de civiles que atribuye a soldados salvadoreños", "Revista E&N", "https://www.revistaeyn.com/centroamericaymundo/una-haiti-denuncia-muertes-de-civiles-que-atribuye-a-soldados-salvadorenos-BM32497556", "prensa", "sin_revisar", "prensa", "ambos", "Las acusaciones de UNA-Haití son postura"),
    ("S150", "Bukele al rescate: El Salvador se presta a resolver la crisis de violencia en Haití", "Última Hora", "https://www.ultimahora.es/noticias/internacional/2024/03/11/2122417/bukele-rescate-salvador-presta-resolver-crisis-violencia-haiti.html", "prensa", "sin_revisar", "prensa", "ambos", ""),
    ("S151", "Nayib Bukele aclara que operación salvadoreña en Haití no es una invasión (DW)", "Teletica / Deutsche Welle", "https://www.teletica.com/deutsche-welle/nayib-bukele-aclara-que-operacion-salvadorena-en-haiti-no-es-una-invasion_420187", "prensa", "sin_revisar", "prensa", "hechos", ""),
    ("S152", "Pandillas de Haití destruyen blindado; cuatro soldados salvadoreños desaparecidos", "Latin Times", "https://www.latintimes.com/espanol/pandillas-de-haiti-destruyen-blindado-4-soldados-salvadorenos-desaparecidos-545430", "prensa", "sin_revisar", "prensa", "hechos", ""),
    ("S153", "Haití, a un mes de la desaparición de militares salvadoreños", "El Diario de Hoy", "https://www.eldiariodehoy.com/noticias/nacionales/mes-desaparicion-militares-haiti/101011/2026/", "prensa", "sin_revisar", "prensa", "hechos", ""),
]

FRAGMENTOS = []


def F(fid, etapa, tipo, fuente, ubic, texto, corr=(), actor=None):
    d = {"id": fid, "etapa": etapa, "tipo": tipo, "id_fuente": fuente, "ubicacion": ubic,
         "corroborado_por": list(corr), "texto": texto, "notas": "", "revisado": True, "estado": "aprobado",
         "revisor": REVISOR, "fecha_revision": HOY}
    if actor:
        d["actor"] = actor
    FRAGMENTOS.append(d)


# ---------------------------------------------------------------- E15 · Antecedentes y marco legal
F("FR-E15-001", "E15", "hecho_atribuido", "S150", "Despacho de marzo de 2024",
  "Según Última Hora, en marzo de 2024 Bukele aseguró que El Salvador podía arreglar la crisis de violencia de "
  "Haití si contaba con el visto bueno de las autoridades haitianas y de la ONU, y dijo que era posible acabar "
  "con las bandas haitianas como lo había hecho con las pandillas en El Salvador.")
F("FR-E15-002", "E15", "hecho", "S133", "Nota sobre la prórroga",
  "Una ley aprobada el 19 de diciembre de 2024 autorizó la participación de la Fuerza Armada de El Salvador en la "
  "misión multinacional de apoyo a la seguridad en Haití, liderada por Kenia, con aeronaves de ala rotativa para "
  "evacuaciones médicas. Después la Asamblea la prorrogó un año más.", corr=["S132"])
F("FR-E15-003", "E15", "hecho_atribuido", "S136", "Despacho de la Voz de América",
  "Según la Voz de América, el primer contingente militar salvadoreño que llegó a Haití para la misión "
  "respaldada por la ONU y liderada por Kenia fue de 70 soldados destinados a las evacuaciones médicas.")
F("FR-E15-004", "E15", "hecho", "S134", "Comunicado SC/16185",
  "El 30 de septiembre de 2025 el Consejo de Seguridad de la ONU aprobó la resolución 2793, que convirtió la "
  "misión multinacional liderada por Kenia en la Fuerza de Supresión de Pandillas (GSF, por sus siglas en "
  "inglés), con un periodo inicial de 12 meses. La votación fue de 12 a favor, ninguno en contra y 3 "
  "abstenciones: China, Rusia y Pakistán.", corr=["S135"])
F("FR-E15-005", "E15", "hecho_atribuido", "S132", "Despacho de EFE",
  "Según Diario El Mundo, la Fuerza de Supresión de Pandillas se aprobó con un mandato de 12 meses, 5.550 "
  "efectivos de seguridad y más de 50 empleados civiles. A diferencia de la misión anterior, puede detener a "
  "presuntos pandilleros.")
F("FR-E15-006", "E15", "hecho", "S131", "Nota sobre la ley",
  "El 29 de septiembre de 2026 la Asamblea Legislativa aprobó con 57 votos, con dispensa de trámite, la Ley "
  "Especial Transitoria para la Participación de la Fuerza Armada de El Salvador en la Fuerza de Supresión de "
  "Pandillas en Haití. La ley autoriza esa participación por 12 meses más, hasta octubre de 2027, prorrogables "
  "mientras dure la misión.", corr=["S132"])

# ---------------------------------------------------------------- E15 · La emboscada del 18 de octubre
F("FR-E15-007", "E15", "hecho", "S137", "Despacho del 19 de octubre",
  "El domingo 18 de octubre de 2026 cuatro aerotécnicos salvadoreños de la Fuerza de Tarea Libertad II, que "
  "formaban parte de la Fuerza de Supresión de Pandillas, sufrieron una emboscada de grupos armados en Santo, una "
  "localidad de Croix-des-Bouquets, a unos 12 kilómetros de Puerto Príncipe. Según la Fuerza Armada salvadoreña, "
  "regresaban a su campamento después de comprar alimentos, salieron del vehículo blindado en el que viajaban, "
  "que fue incendiado, y se perdió el contacto con ellos.", corr=["S138"])
F("FR-E15-008", "E15", "hecho", "S138", "Cronología del caso",
  "A finales de octubre de 2026 El Salvador envió a Haití más de 2.000 militares, con blindados y helicópteros, "
  "para buscar a los cuatro aerotécnicos. Los primeros refuerzos llegaron a Puerto Príncipe el 22 de octubre y el "
  "28 de octubre la Cancillería confirmó que el contingente superaba los 2.000 efectivos.", corr=["S140"])
F("FR-E15-009", "E15", "hecho_atribuido", "S151", "Despacho de DW",
  "Según DW, el contingente salvadoreño, que incluye fuerzas especiales, es el más numeroso desplegado por un "
  "país en Haití desde el final de la Misión de Estabilización de las Naciones Unidas en Haití (Minustah).")
F("FR-E15-010", "E15", "hecho_atribuido", "S138", "Cronología del caso",
  "Según la cronología de El Diario de Hoy, el 24 de octubre de 2026 circularon informes de que unos cuerpos "
  "podían ser de los cuatro salvadoreños y Bukele lo rechazó con la frase \"No son nuestros hombres\". Un cabecilla "
  "de pandilla, Wilson Joseph, alias Lanmò San Jou, dijo a la agencia AP que los cuatro estaban muertos, sin dar "
  "pruebas, y las autoridades salvadoreñas no lo confirmaron.")
F("FR-E15-011", "E15", "postura", "S139", "Despacho de AP recogido por Diario Libre",
  "Según la agencia AP, el embajador de Estados Unidos ante la ONU, Mike Waltz, dijo en el Consejo de Seguridad "
  "que su gobierno considera que los cuatro militares salvadoreños sobrevivieron a la emboscada, aunque las "
  "fuerzas internacionales todavía desconocían su paradero.", actor="gobierno de Estados Unidos")

# ---------------------------------------------------------------- E15 · Lo que dicen los gobiernos
F("FR-E15-012", "E15", "postura", "S141", "Declaraciones del 29 de octubre",
  "Según Diario El Mundo, Bukele dijo el 29 de octubre de 2026: \"Esto no es una operación contra el pueblo "
  "haitiano, ni una invasión al país de Haití\". Afirmó que su objetivo principal es que los cuatro técnicos de "
  "aviación vuelvan a El Salvador y que su gobierno cubre el 90 % de los gastos de la operación, aunque otros "
  "países aportan parte de la logística.", actor="gobierno salvadoreño")
F("FR-E15-013", "E15", "postura", "S144", "Despacho de EFE del 3 de noviembre",
  "Según EFE, el 3 de noviembre de 2026 Bukele afirmó que ayudará a los haitianos a \"retomar el país\", después de "
  "que el primer ministro de Haití, Alix Didier Fils-Aimé, le agradeciera \"haber comprendido la batalla que libra "
  "Haití, que es similar a la que enfrentó contra las pandillas salvadoreñas\".", actor="gobiernos salvadoreño y haitiano")
F("FR-E15-014", "E15", "postura", "S145", "Mensaje en X del 10 de noviembre",
  "Según EFE, el 10 de noviembre de 2026 el primer ministro haitiano Fils-Aimé afirmó que su gobierno está "
  "recuperando el control territorial con el apoyo de las tropas salvadoreñas y de la Fuerza de Supresión de "
  "Pandillas, y escribió: \"Haití, El Salvador, GSF: ¡el mismo combate, la misma determinación!\".",
  actor="gobierno haitiano")
F("FR-E15-015", "E15", "hecho_atribuido", "S142", "Despacho de EFE del 12 de noviembre",
  "Según EFE, el 12 de noviembre de 2026 Bukele anunció que, tras una operación conjunta con la Policía Nacional "
  "de Haití y fuerzas haitianas, se tomó el control del estadio Sylvio Cator de Puerto Príncipe, que estaba en "
  "manos de las bandas desde febrero de 2024, y que allí se instalará una base operativa. Bukele informó de que "
  "dentro del estadio se encontraron varios cráneos humanos y amenazó a las pandillas con una ofensiva.",
  corr=["S143"])
F("FR-E15-016", "E15", "postura", "S148", "Declaraciones del 16 de noviembre",
  "Según Euronews, el ministro de Seguridad salvadoreño, Gustavo Villatoro, dijo el 16 de noviembre de 2026 que El "
  "Salvador retirará sus más de 2.000 militares de Haití cuando sean localizados los cuatro desaparecidos: \"Si "
  "reaparecen mañana, nos iremos de Haití\". En el mismo acto, el ministro haitiano Patrick Pélissier dijo que Haití "
  "quiere que el despliegue continúe.", actor="gobiernos salvadoreño y haitiano")

# ---------------------------------------------------------------- E15 · La ONU y los críticos
F("FR-E15-017", "E15", "hecho", "S146", "Declaración del portavoz de la ONU",
  "El 2 de noviembre de 2026 la ONU aclaró que la gran mayoría de los militares salvadoreños enviados "
  "adicionalmente a Haití no forma parte de la Fuerza de Supresión de Pandillas, por lo que queda fuera de los "
  "mecanismos de apoyo y supervisión de su oficina en Haití. El portavoz recordó que toda operación de seguridad "
  "en el país debe respetar el derecho internacional de los derechos humanos y el derecho internacional "
  "humanitario.", corr=["S138"])
F("FR-E15-018", "E15", "postura", "S147", "Nota sobre Amnistía Internacional",
  "Según Diario El Mundo, la directora para las Américas de Amnistía Internacional, Ana Piquer, pidió a los "
  "gobiernos de El Salvador y Haití garantizar que todas las operaciones de las fuerzas salvadoreñas respeten el "
  "derecho internacional de los derechos humanos. El diputado William Soriano, de Nuevas Ideas, respondió en X con "
  "la frase \"Los Derechos de Pandilleros\".", actor="Amnistía Internacional y oficialismo")
F("FR-E15-019", "E15", "postura", "S149", "Carta de UNA-Haití a la ONU",
  "Según la Revista E&N, la Asociación de las Naciones Unidas de Haití (UNA-Haití), un grupo que representa a "
  "sectores de la diáspora haitiana, denunció en una carta al secretario general de la ONU muertes de civiles que "
  "atribuye a bombardeos y ataques de las fuerzas salvadoreñas desde el 22 de octubre de 2026 en Croix-des-"
  "Bouquets, Canaan y Plaine du Cul-de-Sac, sin dar una cifra, y pidió una investigación independiente. El artículo "
  "no recoge una respuesta directa del gobierno salvadoreño a esas acusaciones.", actor="UNA-Haití")
F("FR-E15-020", "E15", "hecho_atribuido", "S148", "Declaración de la ONU en Ginebra",
  "Según Euronews, el 17 de noviembre de 2026 la Oficina del Alto Comisionado de la ONU para los Derechos Humanos "
  "pidió a todo el personal desplegado en Haití priorizar la protección de los civiles y usar la fuerza letal "
  "solo como último recurso. Amnistía Internacional pidió además que se publique el acuerdo de seguridad del "
  "gobierno de Bukele con Haití.")
F("FR-E15-021", "E15", "hecho_atribuido", "S152", "Contexto de la misión",
  "Según Latin Times, en octubre de 2026 la Fuerza de Supresión de Pandillas tenía desplegadas más de 2.000 "
  "tropas de seis países, alrededor del 37 % de lo previsto, y Haití había aplazado sin fecha las elecciones "
  "previstas para diciembre de 2026; el país no tiene un gobierno elegido en las urnas desde 2016.")

# ---------------------------------------------------------------- E15 · Estado del caso al cierre de los datos
F("FR-E15-022", "E15", "hecho", "S138", "Cronología del caso",
  "Al cumplirse un mes de la emboscada, el 18 de noviembre de 2026, las autoridades no habían confirmado ni el "
  "paradero ni el estado de los cuatro aerotécnicos. El 2 de noviembre la Policía Nacional de Haití recuperó el "
  "vehículo incendiado en Santo, sin pistas sobre sus ocupantes, y el 10 de noviembre el vicepresidente Félix "
  "Ulloa dijo: \"No hay rastro de ellos\".", corr=["S153"])
F("FR-E15-023", "E15", "hecho_atribuido", "S138", "Cronología del caso",
  "Según El Diario de Hoy, el 17 de noviembre de 2026 el Consejo de Ministros de Haití, presidido por el primer ministro Alix Didier "
  "Fils-Aimé, aprobó un acuerdo de cooperación con El Salvador cuyo texto no se ha publicado. El 5 de noviembre "
  "el vicepresidente Ulloa había dicho que el despliegue se apoya en un acuerdo bilateral con Haití.")


def main():
    reg = Path("fuentes") / "registro_fuentes.csv"
    if not reg.exists():
        raise SystemExit("Corre antes agregar_lote1.py y agregar_lote2.py. No hago nada.")
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
    destino = Path("fuentes") / "fragmentos_lote3.jsonl"
    with destino.open("w", encoding="utf-8", newline="\n") as f:
        for fr in FRAGMENTOS:
            f.write(json.dumps(fr, ensure_ascii=False) + "\n")
    print(f"Registro: {len(existentes)} fuentes | Fragmentos: {len(FRAGMENTOS)} en {destino}")


if __name__ == "__main__":
    main()
