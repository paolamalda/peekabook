# Encuestas del programa de bienestar financiero: inicio, final y seguimiento a 30 y 90 días.
# Índice de bienestar financiero (0 a 100): promedio de 8 preguntas con puntaje (gastar, ahorrar, deber y planear),
# redacción propia inspirada en el marco de salud financiera de Financial Health Network. Más señales de estrés (sin puntaje),
# hábitos y, en la final, la evaluación del programa. Todos los textos tienen menos de 255 caracteres.
# Uso desde curso.py: encuesta.generar(carpeta_salida, variante, negocio, titulo)  · variante: mx | mx_en | us_es | us_en | joven_mx
import os, json, html

# (id, dimensión, texto, [(puntos, opción)]) · puntos None = sin puntaje
def items(v, negocio=False):
    en = v in ("us_en", "mx_en"); mx = v in ("mx", "joven_mx", "mx_en"); joven = v == "joven_mx"
    T = (lambda es, en_: en_) if en else (lambda es, en_: es)
    seg = T("IMSS, ISSSTE o IMSS-Bienestar" if mx else "Medi-Cal, Medicaid o seguro del trabajo", "IMSS, ISSSTE or IMSS-Bienestar" if mx else "Medi-Cal, Medicaid or work coverage")
    hogar = T("tu hogar" if not joven else "tu casa (tú y quienes aportan dinero)", "your household")
    S = []
    S.append(("P1", "gastar", T(f"En los últimos 12 meses, comparado con lo que entró a {hogar}, lo que gastaron fue…",
                               "In the last 12 months, compared with what came into your household, what you spent was…"),
              [(100, T("Mucho menos", "Much less")), (75, T("Un poco menos", "A little less")), (50, T("Más o menos igual", "About the same")),
               (25, T("Un poco más", "A little more")), (0, T("Mucho más", "Much more"))]))
    S.append(("P2", "gastar", T("En los últimos 12 meses, ¿cómo pagaron sus cuentas y compromisos (renta, luz, créditos, tandas)?",
                               "In the last 12 months, how did your household pay its bills and commitments (rent, utilities, loans)?"),
              [(100, T("Todos a tiempo", "All on time")), (60, T("Casi todos a tiempo", "Nearly all on time")), (40, T("La mayoría a tiempo", "Most on time")),
               (20, T("Algunos a tiempo", "Some on time")), (0, T("Muy pocos a tiempo", "Very few on time"))]))
    S.append(("P3", "ahorrar", T("Si hoy dejaran de entrar ingresos, ¿cuánto tiempo podrían cubrir sus gastos con el dinero que tienen disponible, sin pedir prestado?",
                                "If your income stopped today, how long could you cover your expenses with money you have available, without borrowing?"),
              [(100, T("6 meses o más", "6 months or more")), (75, T("De 3 a 5 meses", "3 to 5 months")), (50, T("De 1 a 2 meses", "1 to 2 months")),
               (25, T("De 1 a 3 semanas", "1 to 3 weeks")), (0, T("Menos de 1 semana", "Less than 1 week"))]))
    S.append(("P4", "ahorrar", T("Pensando en metas como tus estudios, una casa, un negocio o tu retiro, ¿qué tan segura o seguro estás de que hoy haces lo necesario para lograrlas?",
                                "Thinking about goals like school, a home, a business or retirement, how confident are you that you're doing what's needed to reach them?"),
              [(100, T("Muy segura o seguro", "Very confident")), (75, T("Bastante", "Quite confident")), (50, T("Algo", "Somewhat confident")),
               (25, T("Poco", "Slightly confident")), (0, T("Nada", "Not at all confident"))]))
    S.append(("P5", "deber", T("Hoy, sus deudas (tarjetas, préstamos, fiado, dinero que deben a personas, pagos atrasados) son…",
                              "Today, your household's debts (cards, loans, money owed to people, past-due bills) are…"),
              [(100, T("No tenemos deudas", "We have no debt")), (85, T("Manejables", "Manageable")),
               (40, T("Un poco más de lo que podemos manejar", "A bit more than we can manage")), (0, T("Mucho más de lo que podemos manejar", "Far more than we can manage"))]))
    S.append(("P6", "deber", T("Si mañana tuvieras un gasto urgente igual a un mes de tus gastos, ¿podrías cubrirlo?",
                              "If tomorrow you had an urgent expense equal to one month of your expenses, could you cover it?"),
              [(100, T("Sí, con mi ahorro", "Yes, with my savings")), (70, T("Sí, con ayuda de familia o un crédito formal que puedo pagar", "Yes, with family help or formal credit I can repay")),
               (30, T("Con dificultad: con un préstamo caro o empeñando algo", "With difficulty: an expensive loan or pawning something")), (0, T("No podría", "I couldn't"))]))
    S.append(("P7", "planear", T(f"Contando seguros de salud, vida, casa o auto y {seg}, ¿qué tan segura o seguro estás de que te protegerían en una emergencia?",
                                f"Counting health, life, home or car insurance and {seg}, how confident are you that they'd protect you in an emergency?"),
              [(100, T("Muy segura o seguro", "Very confident")), (75, T("Bastante", "Quite confident")), (50, T("Algo", "Somewhat confident")),
               (25, T("Poco", "Slightly confident")), (10, T("Nada", "Not at all confident")), (0, T("No tenemos ningún seguro ni seguridad social", "We have no insurance or coverage"))]))
    S.append(("P8", "planear", T("«En mi hogar planeamos el dinero con anticipación.»", '"My household plans ahead financially."'),
              [(100, T("Totalmente de acuerdo", "Strongly agree")), (65, T("De acuerdo", "Agree")), (35, T("Ni de acuerdo ni en desacuerdo", "Neither agree nor disagree")),
               (15, T("En desacuerdo", "Disagree")), (0, T("Totalmente en desacuerdo", "Strongly disagree"))]))
    E = [("E1", "estres", T("En el último mes, ¿qué tan seguido te preocupó el dinero al grado de no dormir bien?", "In the last month, how often did money worries keep you from sleeping well?"),
          [(None, T("Nunca", "Never")), (None, T("Pocas veces", "A few times")), (None, T("Seguido", "Often")), (None, T("Casi siempre", "Almost always"))]),
         ("E2", "estres", T("En el último mes, ¿discutiste en casa por dinero?", "In the last month, did you argue at home about money?"),
          [(None, T("Nunca", "Never")), (None, T("Una vez", "Once")), (None, T("Varias veces", "Several times")), (None, T("Muy seguido", "Very often"))]),
         ("E3", "estres", T("En los últimos 3 meses, ¿dejaste de comprar comida o medicinas por falta de dinero?", "In the last 3 months, did you skip buying food or medicine because of money?"),
          [(None, T("No", "No")), (None, T("Una vez", "Once")), (None, T("Varias veces", "Several times"))]),
         ("E4", "estres", T("En los últimos 3 meses, ¿pediste a un prestamista, a una app de préstamo o empeñaste algo para cubrir gastos básicos?",
                            "In the last 3 months, did you use a payday lender, a loan app or a pawn shop to cover basic expenses?"),
          [(None, T("No", "No")), (None, T("Una vez", "Once")), (None, T("Varias veces", "Several times"))]),
         ("E5", "estres", T("Hoy, ¿cómo te sientes con tu situación de dinero?", "Today, how do you feel about your money situation?"),
          [(None, T("Tranquila o tranquilo", "Calm")), (None, T("Algo preocupada o preocupado", "Somewhat worried")), (None, T("Muy preocupada o preocupado", "Very worried"))])]
    H = [("H1", "habitos", T("¿Tienes un presupuesto que revisas al menos cada mes?", "Do you have a budget you review at least monthly?"),
          [(None, T("Sí", "Yes")), (None, T("A veces", "Sometimes")), (None, T("No", "No"))]),
         ("H2", "habitos", T("¿Apartas dinero para ahorrar cuando recibes tu ingreso?", "Do you set money aside to save when you get paid?"),
          [(None, T("Siempre", "Always")), (None, T("A veces", "Sometimes")), (None, T("Nunca", "Never"))]),
         ("H3", "habitos", T("¿Tienes ahorro para emergencias en un lugar seguro?", "Do you have emergency savings in a safe place?"),
          [(None, T("Sí", "Yes")), (None, T("Estoy empezando", "I'm starting")), (None, T("No", "No"))]),
         ("H4", "habitos", T("¿Revisaste tu historial de crédito en el último año?", "Did you check your credit report in the last year?"),
          [(None, T("Sí", "Yes")), (None, T("No", "No")), (None, T("No sé qué es", "I don't know what it is"))]),
         ("H5", "habitos", T("¿Sabes a dónde reclamar si una institución financiera te cobra mal?", "Do you know where to complain if a financial institution overcharges you?"),
          [(None, T("Sí", "Yes")), (None, T("No", "No"))]),
         ("H6", "habitos", T("¿Sabes reconocer y reportar un fraude?", "Do you know how to spot and report a scam?"),
          [(None, T("Sí", "Yes")), (None, T("Más o menos", "Somewhat")), (None, T("No", "No"))]),
         ("H7", "habitos", T("Si alguien te pide ser aval o dar tus datos como referencia, ¿sabes qué te pueden cobrar en cada caso?",
                             "If someone asks you to cosign or be a reference, do you know what you could be charged in each case?"),
          [(None, T("Sí", "Yes")), (None, T("Más o menos", "Somewhat")), (None, T("No", "No"))])]
    if negocio:
        H += [("H8", "habitos", T("¿Separas el dinero del negocio del de tu casa?", "Do you keep business money separate from household money?"),
               [(None, T("Sí", "Yes")), (None, T("A veces", "Sometimes")), (None, T("No", "No"))]),
              ("H9", "habitos", T("¿Sabes cada mes si tu negocio gana o pierde dinero?", "Do you know each month whether your business makes or loses money?"),
               [(None, T("Sí", "Yes")), (None, T("A veces", "Sometimes")), (None, T("No", "No"))])]
    if joven:
        H += [("H8", "habitos", "¿Has ganado dinero por tu cuenta (vender, un servicio, un trabajo de medio tiempo) en los últimos 6 meses?",
               [(None, "Sí, varias veces"), (None, "Una vez"), (None, "No")]),
              ("H9", "habitos", "¿Tienes una idea de negocio o proyecto que quieras probar este año?",
               [(None, "Sí, ya la estoy probando"), (None, "Sí, pero no he empezado"), (None, "No")])]
    D = [("D1", "perfil", T("Tu edad (opcional)", "Your age (optional)"),
          [(None, x) for x in (["15 a 16", "17 a 18", "19 o más", "Prefiero no decir"] if joven else
                               T(["18 a 29", "30 a 44", "45 a 59", "60 o más", "Prefiero no decir"], ["18 to 29", "30 to 44", "45 to 59", "60 or older", "Prefer not to say"]))])]
    if not joven:
        rangos = (T(["Menos de 10,000 pesos", "De 10,000 a 20,000 pesos", "De 20,000 a 40,000 pesos", "Más de 40,000 pesos", "Prefiero no decir"],
                    ["Less than 10,000 pesos", "10,000 to 20,000 pesos", "20,000 to 40,000 pesos", "More than 40,000 pesos", "Prefer not to say"]) if mx else
                  T(["Menos de $2,500", "De $2,500 a $5,000", "De $5,000 a $8,000", "Más de $8,000", "Prefiero no decir"],
                    ["Less than $2,500", "$2,500 to $5,000", "$5,000 to $8,000", "More than $8,000", "Prefer not to say"]))
        D.append(("D2", "perfil", T("Ingreso aproximado de tu hogar al mes (opcional)", "Your household's approximate monthly income (optional)"), [(None, x) for x in rangos]))
    F = [("F1", "programa", T("¿Qué tanto te ayudó el programa a manejar mejor tu dinero?", "How much did the program help you manage your money better?"),
          [(None, T("Mucho", "A lot")), (None, T("Algo", "Some")), (None, T("Poco", "A little")), (None, T("Nada", "Not at all"))]),
         ("F2", "programa", T("¿Qué hiciste gracias al programa? (puedes marcar varias)", "What did you do thanks to the program? (check all that apply)"),
          [(None, x) for x in T(["Hice un presupuesto", "Empecé a ahorrar", "Pagué o reorganicé deudas", "Revisé mi historial de crédito", "Me protegí de un fraude",
                                 "Revisé mis seguros o mi retiro", "Mejoré mi negocio o mi forma de ganar dinero", "Otra"],
                                ["Made a budget", "Started saving", "Paid down or reorganized debt", "Checked my credit report", "Protected myself from a scam",
                                 "Reviewed my insurance or retirement", "Improved my business or how I earn money", "Other"])]),
         ("F3", "programa", T("Del 0 al 10, ¿qué tanto recomendarías el programa a alguien cercano?", "From 0 to 10, how likely are you to recommend the program to someone close to you?"),
          [(None, str(i)) for i in range(11)]),
         ("F4", "programa", T("¿Qué fue lo más útil y qué mejorarías? (opcional)", "What was most useful and what would you improve? (optional)"), [])]
    U = [("U1", "apoyos", T("¿Usaste algún programa de gobierno u orientación sin costo de los que viste en el curso?",
                            "Did you use any government program or no-cost guidance service you saw in the course?"),
          [(None, T("Sí", "Yes")), (None, T("Todavía no, pero lo voy a hacer", "Not yet, but I plan to")), (None, T("No", "No"))]),
         ("U2", "apoyos", T("¿Cuál o cuáles? (opcional; no escribas datos personales)", "Which one or ones? (optional; don't write personal data)"), [])]
    return S, E, H, D, F, U


def moodle_xml(lista):
    """XML de importación del módulo Retroalimentación (Feedback) de Moodle."""
    out = ['<?xml version="1.0" encoding="UTF-8" ?>', '<FEEDBACK VERSION="200701" COMMENT="XML-Importfile for mod/feedback">', '     <ITEMS>']
    for n, (iid, dim, txt, ops) in enumerate(lista, 1):
        if not ops:
            typ, pres, req = "textarea", "60|4", "0"
        elif ops[0][0] is not None:
            typ, pres, req = "multichoicerated", "r>>>>>" + "\n|".join(f"{p}####{o}" for p, o in ops), "1"
        else:
            multi = "varias" in txt or "check all" in txt
            typ, pres, req = "multichoice", ("c" if multi else "r") + ">>>>>" + "\n|".join(o for _, o in ops), "0" if dim == "perfil" else "1"
        out += [f'          <ITEM TYPE="{typ}" REQUIRED="{req}">', f"               <ITEMID><![CDATA[{n}]]></ITEMID>",
                f"               <ITEMTEXT><![CDATA[{txt}]]></ITEMTEXT>", f"               <ITEMLABEL><![CDATA[{iid}]]></ITEMLABEL>",
                f"               <PRESENTATION><![CDATA[{pres}]]></PRESENTATION>", "               <OPTIONS><![CDATA[h]]></OPTIONS>",
                "               <DEPENDITEM><![CDATA[0]]></DEPENDITEM>", "               <DEPENDVALUE><![CDATA[]]></DEPENDVALUE>", "          </ITEM>"]
    return "\n".join(out + ["     </ITEMS>", "</FEEDBACK>", ""])


def generar(dest, variante, negocio, titulo):
    en = variante in ("us_en", "mx_en")
    S, E, H, D, F, U = items(variante, negocio)
    todas = S + E + H + D + F + U
    largo = [(i, len(t)) for i, _, t, ops in todas for t in [t] + [o for _, o in ops] if len(t) >= 255]
    assert not largo, largo
    os.makedirs(dest, exist_ok=True)
    enc = {("inicio", "start"): S + E + H + D, ("final", "final"): S + E + H + F + U, ("seguimiento", "follow_up"): S + E + H + U}
    nombres = {}
    for (es_, en_), lst in enc.items():
        base = ("survey_" + en_) if en else ("encuesta_" + es_)
        open(os.path.join(dest, base + ".xml"), "w").write(moodle_xml(lst)); nombres[es_] = base
    # documento legible
    T = (lambda es, e: e) if en else (lambda es, e: es)
    L = [f"# {T('Encuestas del programa', 'Program surveys')} · {titulo}", "",
         T("Tres encuestas con las mismas preguntas base para medir el cambio: **inicio** (antes del Módulo 1), **final** (al terminar, antes de la constancia) y **seguimiento** (a los 30 y a los 90 días). Son anónimas y no piden datos personales. Cada texto tiene menos de 255 caracteres.",
           "Three surveys with the same core questions to measure change: **start** (before Module 1), **final** (at the end, before the certificate) and **follow-up** (at 30 and 90 days). They're anonymous and don't ask for personal data. Every text is under 255 characters."), "",
         "| " + T("Encuesta", "Survey") + " | " + T("Archivo", "File") + " | " + T("Preguntas", "Questions") + " |", "|---|---|---|"]
    for (es_, en_), lst in enc.items():
        L.append(f"| {T(es_.capitalize(), en_.replace('_', '-').capitalize())} | `{nombres[es_]}.xml` | {len(lst)} |")
    L += ["", T("## Índice de bienestar financiero", "## Financial well-being index"), "",
          T("Promedio de los puntos de P1 a P8 (0 a 100). De 0 a 39: en riesgo · de 40 a 79: en equilibrio frágil · de 80 a 100: con bienestar. Subíndices: gastar (P1, P2), ahorrar (P3, P4), deber (P5, P6) y planear (P7, P8). Las preguntas E son señales de estrés y no suman puntos.",
            "Average of the points from P1 to P8 (0 to 100). 0 to 39: at risk · 40 to 79: fragile balance · 80 to 100: well. Sub-scores: spend (P1, P2), save (P3, P4), borrow (P5, P6) and plan (P7, P8). E questions are stress signals and don't add points."), ""]
    for grupo, lst in ((T("Salud financiera (con puntaje)", "Financial health (scored)"), S), (T("Señales de estrés", "Stress signals"), E), (T("Hábitos", "Habits"), H),
                       (T("Perfil (opcional, solo en inicio)", "Profile (optional, start only)"), D), (T("Evaluación del programa (solo en la final)", "Program evaluation (final only)"), F),
                       (T("Uso de programas y orientaciones (final y seguimiento)", "Use of programs and guidance (final and follow-up)"), U)):
        L += [f"## {grupo}", ""]
        for iid, dim, txt, ops in lst:
            L.append(f"**{iid}.** {txt}")
            L += [f"- {o}" + (f" · {p} {T('puntos', 'points')}" if p is not None else "") for p, o in ops] or [T("- Respuesta abierta", "- Open answer")]
            L.append("")
    L += [T("## Privacidad", "## Privacy"), "",
          T("Configura cada encuesta como **anónima**. El rango de ingreso es opcional, amplio y con «Prefiero no decir». En los reportes muestra solo grupos de 5 respuestas o más, para que nadie pueda ser identificado.",
            "Set each survey as **anonymous**. The income range is optional, broad and includes \"Prefer not to say.\" In reports, show only groups of 5 or more responses so no one can be identified.")]
    open(os.path.join(dest, T("encuestas.md", "surveys.md")), "w").write("\n".join(L) + "\n")
    json.dump({"variante": variante, "puntaje": {i: {o: p for p, o in ops} for i, _, _, ops in S},
               "subindices": {"gastar": ["P1", "P2"], "ahorrar": ["P3", "P4"], "deber": ["P5", "P6"], "planear": ["P7", "P8"]}},
              open(os.path.join(dest, "puntaje.json"), "w"), ensure_ascii=False, indent=1)
    return len(S + E + H + D), len(S + E + H + F + U), len(S + E + H + U)
