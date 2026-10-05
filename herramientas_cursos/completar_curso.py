# Completa un curso nuevo para que pase por todo el generador (curso.py todo) y por estandares.py:
#   1. agrega a curso.json lo que falta (ux 3, nombres, apoyo_leads, instalacion, carpeta, encuesta, catalogo, ocde, hojas, constancia.mods),
#      sin tocar lo que ya existe;
#   2. escribe el libro de apoyo a partir de las lecciones: 01 bienvenida, 03 prácticas, 05 ayuda y 06 referencias
#      (04 glosario lo genera curso.py; 02 casos integradores se escribe a mano).
# Uso: python3 herramientas_cursos/completar_curso.py cursos/<curso> [--forzar]   (--forzar reescribe 01, 03, 05 y 06)
import json, os, re, sys, unicodedata
from collections import OrderedDict

HOY_ES, HOY_EN = "5 de octubre de 2026", "October 5, 2026"

# Lo propio de cada curso: catálogo, encuesta, hojas de cálculo y nombre corto en Moodle.
SPEC = {
 "tu_regreso": dict(corto="TRDF-MX-ES", encuesta="mx", hojas=[], idiomas="Español (también en inglés y en grupo bilingüe)",
   desc=["Tus papeles, una cuenta a tu nombre, crédito desde cero, lo que dejaste en Estados Unidos, tu Afore y tus primeros 90 días.",
         "Lecciones cortas con casos de personas que regresan a Michoacán, Guanajuato, Puebla y Oaxaca."]),
 "your_return_en": dict(corto="TRDF-MX-EN", encuesta="mx_en", hojas=[], idiomas="English (also in Spanish and as a bilingual group)",
   desc=["Your papers, an account in your name, credit from scratch, what you left in the U.S., your Afore and your first 90 days.",
         "Short lessons with cases of people returning to Michoacán, Guanajuato, Puebla and Oaxaca."]),
 "tu_pension": dict(corto="TPPF-MX", encuesta="mx", hojas=["pension"], idiomas="Español",
   desc=["Cuida tu pensión, tu tarjeta y tu casa; evita fraudes y abusos, y deja todo en orden.",
         "Lecciones cortas, con letra grande, para sesiones presenciales con acompañante de confianza."]),
 "tu_costa": dict(corto="TCDF-MX", encuesta="mx", hojas=["ingreso_variable"], idiomas="Español",
   desc=["Protege lo tuyo ante huracanes, ordena el ingreso de temporada, usa crédito con cuidado, reclama y cuida tu patrimonio.",
         "Lecciones cortas con casos de familias de la Costa Chica de Guerrero y Oaxaca."]),
 "tu_comunidad": dict(corto="TCMF-MX", encuesta="mx", hojas=[], idiomas="Español, con intérprete o facilitadora bilingüe en la sesión",
   desc=["Cobra tus apoyos sin intermediarios, ten una cuenta a tu nombre, ahorra en grupo con reglas y protege tu tierra y tu familia.",
         "Lecciones cortas para sesiones presenciales en comunidades rurales."]),
 "tu_autonomia": dict(corto="TADF-MX", encuesta="mx", hojas=["bienes"], idiomas="Español",
   desc=["Dinero y documentos a tu nombre, un presupuesto que cuenta los cuidados, tu retiro, tus seguros y salida de la violencia económica.",
         "Lecciones cortas en línea y dos círculos presenciales, con casos de mujeres de distintas edades."]),
 "tu_ruta": dict(corto="TRTA-MX", encuesta="mx", hojas=["semana_apps", "ingreso_variable"], idiomas="Español",
   desc=["Tu ingreso real, tus derechos con la reforma de plataformas, IMSS, impuestos, vehículo, accidentes y tu futuro.",
         "Lecciones cortas para el celular, para tomar entre viajes."]),
 "tu_temporada": dict(corto="TTMP-MX", encuesta="mx", hojas=["envios", "ingreso_variable"], idiomas="Español",
   desc=["Contrato sin fraudes, tu pago y tus derechos en Canadá o en Estados Unidos, envíos que rinden, impuestos, regreso y futuro.",
         "Lecciones cortas con casos de jornaleros y de las familias que se quedan en México."]),
}


def slug(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^A-Za-z0-9]+", "_", s).strip("_")


def lecciones(D, mods):
    """[(modulo, codigo, titulo, {seccion: texto})] en orden."""
    out = []
    for m in mods:
        p = os.path.join(D, "lecciones", f"{m}.md")
        if not os.path.exists(p): continue
        for bloque in re.split(r"(?m)^# (?=M\d+ U\d+)", open(p, encoding="utf-8").read())[1:]:
            cab, cuerpo = bloque.split("\n", 1)
            cod, tit = [x.strip() for x in cab.split("|", 1)]
            secs = {"_": cuerpo.split("\n== ", 1)[0]}
            for s in re.split(r"(?m)^== ", cuerpo)[1:]:
                n, t = (s.split("\n", 1) + [""])[:2]; secs[n.strip()] = t
            out.append((m, cod, tit, secs))
    return out


def minutos(secs):
    pal = len(re.findall(r"\w+", secs.get("esencial", "")))
    return round(pal / 130) + 6


def completar_config(D, cfg, en):
    nombre = os.path.basename(os.path.normpath(D)); sp = SPEC[nombre]
    T = (lambda es, e: e) if en else (lambda es, e: es)
    MODS = cfg["modulos"]; n = len(MODS)
    lecs = lecciones(D, MODS); nl = len(lecs)
    cambios = []

    def pon(k, v):
        if k not in cfg: cfg[k] = v; cambios.append(k)

    pon("ux", 3)
    pon("nombres", {m: {"titulo": re.sub(r"^(Módulo|Module) \d+\.\s*", "", t), "descripcion": cfg["resultados"][m]} for m, t in MODS.items()})
    pon("apoyo_leads", {
        "01": T("Empieza aquí: cómo funciona el curso, cuánto toma cada lección, los personajes, las insignias y la constancia.",
                "Start here: how the course works, how long each lesson takes, the characters, badges and certificate."),
        "02": T("Casos que reúnen lo aprendido en varios módulos. Resuélvelos antes de abrir la clave.",
                "Cases that bring together what you learned across modules. Solve them before opening the key."),
        "03": T("Ejercicios cortos para practicar los cálculos del curso. Las respuestas están al final.",
                "Short exercises to practice the course calculations. The answers are at the end."),
        "04": T("Las palabras del curso explicadas en lenguaje sencillo, por módulo.", "The course words explained in plain language, by module."),
        "05": T("Dónde pedir ayuda sin costo y respuestas a las dudas más comunes.", "Where to get help at no cost, and answers to common questions."),
        "06": T("Las fuentes que usamos en el curso, para que puedas verificarlas.", "The sources we used in the course, so you can check them.")})
    cfg.setdefault("constancia", {})
    if "mods" not in cfg["constancia"]:
        cfg["constancia"]["mods"] = cfg["constancia"].get("temas", [re.sub(r"^(Módulo|Module) \d+\.\s*", "", t) for t in MODS.values()])[:5]
        cambios.append("constancia.mods")

    total = 25 * nl
    nombres_niv = T(["Empiezo", "Me organizo", "Avanzo", "Me protejo", "Planeo", "Lo logré"],
                    ["Getting started", "Getting organized", "Moving forward", "Protecting what's mine", "Planning ahead", "I made it"])
    fr = [0, .15, .35, .55, .75, .95]
    niveles = []
    for nom, f in zip(nombres_niv, fr):
        p = int(round(total * f / 50) * 50)
        mod = min(n, max(1, int(f * n) + 1))
        niveles.append([nom, p, T("Al entrar", "On entry") if not p else T(f"Durante el Módulo {mod}", f"During Module {mod}")])

    def info(tag, nom):
        ms = re.findall(r"M(\d+)", tag)
        if not ms:
            return [T("Finalización del curso", "Course completion"), T(f"Concluiste los {n} módulos del programa.", f"You completed the program's {n} modules.")]
        if len(ms) == 1:
            return [T(f"Autoevaluación del Módulo {ms[0]} completada (aprobada)", f"Module {ms[0]} self-assessment completed (passed)"), cfg["resultados"][f"M{ms[0]}"]]
        return [T("Autoevaluaciones de los módulos " + " y ".join(ms), "Self-assessments for Modules " + " and ".join(ms)),
                " ".join(cfg["resultados"][f"M{x}"] for x in ms)]

    base = slug(cfg["titulo"].split(",")[0]).upper()
    pon("instalacion", {
        "nombre_corto": sp["corto"],
        "readme": T(f"README_INSTALAR_{base}_PARA_CLAUDE.md", f"README_INSTALL_{base}_FOR_CLAUDE.md"),
        "aviso_foro": T("No compartas números de cuenta, NIP, contraseñas, tu CURP, documentos ni montos reales de tus deudas.",
                        "Don't share account numbers, PINs, passwords, your CURP, documents or the real amounts of your debts."),
        "niveles": niveles,
        "insignias_info": [info(tag, nom) for fn, tag, nom, icon in cfg["insignias"]]})
    v = cfg["version"]; corto = slug(cfg["titulo"].split(",")[0])
    pon("carpeta", {
        "nombre": slug(cfg["titulo"]) + T("_ES", "_EN"),
        "zip": f"{corto}_v{v}",
        "manual": T(f"Manual_del_programa_{cfg['sigla']}_v{v}", f"Program_manual_{cfg['sigla']}_EN_v{v}"),
        "contenido": T(f"Contenido_completo_{cfg['sigla']}_v{v}", f"Full_content_{cfg['sigla']}_EN_v{v}"),
        "guia": T(f"Guia_implementacion_{cfg['sigla']}_v{v}", f"Implementation_guide_{cfg['sigla']}_EN_v{v}"),
        "descripciones": T(
            ["Manual del programa: público, reglas, módulos y lecciones, personajes y datos verificados.",
             "Contenido completo: lecciones, libro de apoyo, H5P y banco de preguntas (.docx y .md).",
             "Guía de implementación: instalación en Moodle, gamificación y mantenimiento (.docx y .md).",
             "Paquete para instalar: libros, H5P, glosario, banco, insignias, datos de la constancia, encuestas, guías, vista previa y el README para Claude."],
            ["Program manual: audience, rules, modules and lessons, characters and verified facts.",
             "Full content: lessons, support book, H5P and question bank (.docx and .md).",
             "Implementation guide: Moodle installation, gamification and maintenance (.docx and .md).",
             "Package to install: books, H5P, glossary, bank, badges, certificate data, surveys, guides, preview and the README for Claude."]),
        "lista": T(
            ["Coordinación leyó el manual del programa", "Contenido revisado por especialistas en los temas del curso",
             "Datos vigentes confirmados en los sitios oficiales",
             f"Curso instalado con 04_Moodle/README_INSTALAR_{base}_PARA_CLAUDE.md",
             "Level Up, insignias, constancia y encuestas configurados", "Revisión con rol de estudiante"],
            ["Coordination read the program manual", "Content reviewed by specialists in the course topics",
             "Current facts confirmed on official sites", f"Course installed with 04_Moodle/README_INSTALL_{base}_FOR_CLAUDE.md",
             "Level Up, badges, certificate and surveys configured", "Review with the student role"]),
        "notas": T(["El curso no recomienda instituciones ni productos: enseña a verificar (SIPRES de la CONDUSEF).",
                    "No se piden datos personales: ni cuentas, ni NIP, ni contraseñas, ni CURP, ni montos reales."],
                   ["The course doesn't recommend institutions or products: it teaches how to verify them (CONDUSEF's SIPRES).",
                    "No personal data is requested: no accounts, PINs, passwords, CURP or real amounts."])
                 + [x.replace("**", "") for x in cfg.get("reglas_extra", [])]})
    pon("encuesta", sp["encuesta"])
    pon("negocio", False)
    pon("catalogo", {"descripcion": sp["desc"], "para_quien": cfg.get("publico", ""), "idiomas": sp["idiomas"]})
    pon("ocde", {"marcos": ["adultos"], "extra": {}})
    pon("hojas", sp["hojas"])
    pon("banco", f"banco_preguntas_{cfg['sigla'].lower()}{'_en' if en else ''}.gift.txt")
    return cambios, lecs


def escribir_apoyo(D, cfg, lecs, en, forzar):
    T = (lambda es, e: e) if en else (lambda es, e: es)
    A = os.path.join(D, "apoyo"); os.makedirs(A, exist_ok=True)
    MODS = cfg["modulos"]; n = len(MODS); nl = len(lecs)
    hechos = []

    def w(fn, L):
        p = os.path.join(A, fn)
        if os.path.exists(p) and not forzar: return
        open(p, "w", encoding="utf-8").write("\n".join(L).rstrip() + "\n"); hechos.append(fn)

    # 01 · Bienvenida
    mins = [minutos(s) for _, _, _, s in lecs]
    lo, hi = min(mins), max(mins)
    ins = cfg["insignias"]; final = ins[-1][2]
    L = [T("# Bienvenida", "# Welcome"), "", f"**{cfg['titulo']}** — {cfg['intro']}", "",
         T(f"Versión {cfg['version']} · Octubre de 2026.", f"Version {cfg['version']} · October 2026."), "",
         T("## Lo que vas a lograr", "## What you'll achieve"), ""]
    L += [f"- **{cfg['nombres'][m]['titulo']}:** {cfg['resultados'][m]}" for m in MODS]
    L += ["", T("## Cómo está hecha cada lección", "## How each lesson works"), "",
          "| " + T("Parte", "Part") + " | " + T("Qué encuentras", "What you'll find") + " |", "|---|---|",
          T("| **Empieza** | Una situación corta y lo que vas a lograr. |", "| **Start** | A short situation and what you'll achieve. |"),
          T("| **Lo esencial** | Lo indispensable, con los errores más comunes. |", "| **The essentials** | What you must know, with the most common mistakes. |"),
          T("| **Profundiza** | Cuentas, casos y más datos, si quieres saber más. |", "| **Go deeper** | Math, cases and more facts, if you want to know more. |"),
          T("| **Practica** | «¿Qué harías?», tres preguntas y tu plan para esta semana. |", "| **Practice** | «What would you do?», three questions and your plan for this week. |"),
          "", T(f"Cada lección toma entre **{lo} y {hi} minutos** con la práctica. Son {nl} lecciones en {n} partes. Al final de cada parte hay una autoevaluación: apruebas con 70% y puedes intentarlo las veces que quieras.",
                f"Each lesson takes **{lo} to {hi} minutes** including practice. There are {nl} lessons in {n} parts. Each part ends with a self-assessment: you pass with 70% and can try as many times as you want."), ""]
    if cfg.get("personajes"):
        L += [T("## Los personajes", "## The characters"), ""] + [f"- **{k}:** {v}" for k, v in cfg["personajes"].items()] + [""]
    L += [T("## Reglas del programa", "## Program rules"), "",
          T("1. **Nunca te pediremos datos personales**, contraseñas, NIP, tu CURP ni montos reales.", "1. **We'll never ask for personal data**, passwords, PINs, your CURP or real amounts."),
          T("2. **No te vendemos nada** ni te recomendamos instituciones: te enseñamos a verificarlas.", "2. **We don't sell you anything** or recommend institutions: we teach you to verify them."),
          T("3. **Tu información es tuya.** Si una organización te ofrece el curso, no recibe tus datos personales ni financieros.", "3. **Your information is yours.** If an organization offers you the course, it doesn't receive your personal or financial data.")]
    for i, r in enumerate(cfg.get("reglas_extra", []), 4):
        L.append(f"{i}. {r}")
    L += ["", T("## Los datos cambian", "## Facts change"), "",
          T(f"Los datos del programa se consultaron el **{HOY_ES}** y cada lección indica sus fuentes. Antes de decidir, revisa la información vigente en el sitio oficial.",
            f"The program's facts were checked on **{HOY_EN}** and each lesson lists its sources. Before deciding, check the current information on the official site."), "",
          T("## Puntos, insignias y constancia", "## Points, badges and certificate"), "",
          T(f"Ganas puntos al completar cada actividad y hay {len(ins)} insignias. Al aprobar todas las autoevaluaciones recibes la insignia **{final}** y tu **constancia de conclusión**. Es un reconocimiento educativo, no una licencia ni una acreditación oficial.",
            f"You earn points for each activity and there are {len(ins)} badges. When you pass all the self-assessments you get the **{final}** badge and your **certificate of completion**. It's an educational recognition, not a license or official accreditation.")]
    w("01-bienvenida.md", L)

    # 03 · Prácticas (los «ponlo» de cada lección)
    P = []
    for m, cod, tit, s in lecs:
        b = re.search(r"(?ms)^--- ponlo\n(.+?)\nrespuesta:\s*(.+?)$", s.get("practica", ""))
        if b: P.append((cod, b.group(1).strip().replace("\n", " "), b.group(2).strip()))
    L = [T("# Prácticas de cálculo", "# Practice exercises"), "", T("Resuelve cada práctica. Las respuestas están al final.", "Solve each exercise. The answers are at the end."), "",
         "| " + T("Clave", "Key") + " | " + T("Lección", "Lesson") + " | " + T("Práctica", "Exercise") + " |", "|---|---|---|"]
    L += [f"| P{i:02d} | {c} | {q.replace('|', '/')} |" for i, (c, q, a) in enumerate(P, 1)]
    L += ["", T("## Respuestas", "## Answers"), ""] + [f"- **P{i:02d}:** {a}" for i, (c, q, a) in enumerate(P, 1)]
    w("03-practicas.md", L)

    # 05 · Ayuda (los recursos de las lecciones, sin repetir) y preguntas frecuentes
    R = OrderedDict()
    for m, cod, tit, s in lecs:
        for ln in s.get("recursos", "").splitlines():
            mm = re.match(r"-\s*\*\*(.+?)\*\*\s*\((.+?)\)\s*:?\s*(.*)$", ln.strip())
            if not mm: continue
            nom, inst, resto = mm.groups()
            inst = re.split(r"\s*·\s*", inst)[0]
            if inst == "Desarrolla Talento": continue
            url, _, busca = resto.partition("| Qué buscar:")
            key = (nom.lower(), inst.lower())
            if key in R: R[key][3].append(cod); continue
            R[key] = [nom, inst, url.strip().rstrip("."), [cod], busca.strip().rstrip(".")]
    L = [T("# Dónde encontrar ayuda", "# Where to find help"), "",
         T(f"Fuentes oficiales y sin costo que aparecen en las lecciones. Información consultada el {HOY_ES}; confírmala en el sitio oficial.",
           f"Official, no-cost sources that appear in the lessons. Information checked on {HOY_EN}; confirm it on the official site."), "",
         "| " + T("Tema", "Topic") + " | " + T("Dónde", "Where") + " | " + T("Qué buscar", "What to look for") + " | " + T("Lecciones", "Lessons") + " |", "|---|---|---|---|"]
    for nom, inst, url, cods, busca in R.values():
        L.append(f"| {nom} | {inst}: {url} | {busca.replace('|', '/') or '—'} | {', '.join(dict.fromkeys(cods))} |")
    L += ["", "---", "", T("# Preguntas frecuentes", "# Frequently asked questions"), "",
          T("**¿Tengo que dar datos reales?** No. Usa números inventados o redondeados; el curso nunca te pide datos personales.",
            "**Do I have to give real information?** No. Use made-up or rounded numbers; the course never asks for personal data."),
          "",
          T("**¿El curso me presta dinero o me recomienda una institución?** No. Te enseña a comparar y a verificar en el SIPRES de la CONDUSEF.",
            "**Does the course lend me money or recommend an institution?** No. It teaches you to compare and to verify in CONDUSEF's SIPRES."),
          "",
          T("**¿Alguien me puede cobrar por los trámites del curso?** Los trámites oficiales que vemos son sin costo. Si alguien te cobra por ellos, desconfía y pregunta en la ventanilla oficial.",
            "**Can someone charge me for the procedures in the course?** The official procedures we cover have no cost. If someone charges you for them, be wary and ask at the official service window."),
          "",
          T("**¿Puedo tomar el curso en el celular?** Sí. Está hecho para eso.", "**Can I take the course on my phone?** Yes. It's made for that."),
          "",
          T("**¿La constancia tiene validez oficial?** Es un reconocimiento educativo, verificable en línea. No es una licencia ni una acreditación oficial.",
            "**Is the certificate officially valid?** It's an educational recognition that can be verified online. It's not a license or official accreditation."),
          "",
          T("**¿Dónde reclamo si una institución financiera me cobra mal?** Primero en la institución, con folio; si no te resuelven, en la CONDUSEF: 55 5340 0999.",
            "**Where do I complain if a financial institution overcharges me?** First at the institution, with a reference number; if they don't solve it, at CONDUSEF: 55 5340 0999."),
          "",
          T("**¿Y si estoy pasando por un momento muy difícil?** Llama a la Línea de la Vida: 800 911 2000, sin costo y las 24 horas.",
            "**What if I'm going through a very hard time?** Call Línea de la Vida: 800 911 2000, no cost, 24 hours a day (Spanish).")]
    w("05-ayuda.md", L)

    # 06 · Referencias (las fuentes de cada lección)
    L = [T("# Referencias", "# References"), "", T(f"Fuentes que usamos en el curso, consultadas el {HOY_ES}.", f"Sources we used in the course, checked on {HOY_EN}."), ""]
    for m in MODS:
        L += [f"## {cfg['nombres'][m]['titulo']}", ""]
        for mm, cod, tit, s in lecs:
            if mm != m: continue
            f = " ".join(s.get("fuentes", "").split())
            if f: L.append(f"- **{cod} · {tit}.** {f}")
        L.append("")
    w("06-referencias.md", L)
    return hechos, len(P), len(R)


if __name__ == "__main__":
    D = sys.argv[1].rstrip("/"); forzar = "--forzar" in sys.argv
    p = os.path.join(D, "curso.json")
    cfg = json.load(open(p, encoding="utf-8"), object_pairs_hook=OrderedDict)
    en = cfg.get("lang") == "en"
    cambios, lecs = completar_config(D, cfg, en)
    json.dump(cfg, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    hechos, np_, nr = escribir_apoyo(D, cfg, lecs, en, forzar)
    print(os.path.basename(D), "· config:", ", ".join(cambios) or "sin cambios", "· apoyo:", ", ".join(hechos) or "sin cambios",
          f"· {len(lecs)} lecciones · {np_} prácticas · {nr} recursos")
