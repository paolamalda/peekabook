# Arma una carpeta por curso con la misma estructura: manual, contenido completo y guía, por separado.
# Cursos: Tu Dinero ES, Your Money EN, Tu Talento y Comunidad Tu Talento.
# Uso: python3 proyecto-inclusion-financiera/herramientas/carpetas_cursos.py
# Antes: regenerar libros, banco y H5P de cada curso (build_v3, quiz_gift_v3, build_ttmf, quiz_ttmf, comunidad_ttmf).
import re, os, glob, shutil, zipfile, subprocess, sys, importlib.util
H = os.path.dirname(os.path.abspath(__file__))
TD = os.path.dirname(H)
ROOT = os.path.dirname(TD)
TT = os.path.join(ROOT, "proyecto-entretenimiento")
ENT = os.path.join(ROOT, "entregas")
S = "/tmp/claude-0/-home-user-peekabook/2b8c84d1-874b-559e-a5dd-06af4ddd1637/scratchpad"
ENV = dict(os.environ, NODE_PATH=f"{S}/nodeenv/node_modules")
FECHA = "2026-09-29"


def casos(path):
    spec = importlib.util.spec_from_file_location(os.path.basename(path)[:-3], path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m.CASOS


def shift(md, n=1):
    return re.sub(r"(?m)^(#{1,5}) ", lambda m: "#" * min(6, len(m.group(1)) + n) + " ", md)


def sin_titulo(md):
    return re.sub(r"(?s)^#[^\n]*\n", "", md, count=1)


def plano(s):
    return re.sub(r"\{\{([^|}]+)\|[^}]+\}\}", r"\1", s)


def h5p(lecciones, CASOS, correcta):
    out = []
    for f in lecciones:
        for les in re.split(r"(?m)^# (?=M\d+ U\d\d)", open(f).read())[1:]:
            code, title = [x.strip() for x in les.split("\n", 1)[0].split("|", 1)]
            out.append(f"## {code}. {title}")
            cs = re.search(r"--- casos\n(.*?)\n--- ", les, re.S).group(1)
            for c, (ok, d1, d2) in zip(re.split(r"(?m)^### ", cs)[1:], CASOS[code]):
                h, b = c.split("\n", 1)
                ctx = plano(" ".join(l for l in b.splitlines() if l.strip() and not l.startswith("? ")))
                q = re.search(r"(?m)^\? (.+?)\s*\|\|", b).group(1)
                out.append(f"**{h.strip()}.** {ctx} **{q}**\n\n- ✔ {ok}\n- {d1}\n- {d2}")
    return out


def banco(gift, modulo):
    out, cur = [], None
    un = lambda s: re.sub(r"\\([~=#{}:])", r"\1", s)
    for name, stem, body in re.findall(r"::(.*?)::(.*?) \{\n(.*?)\n\}", open(gift).read(), re.S):
        mod = name.split()[0]
        if mod != cur: out.append(f"## {modulo} {mod[1:]}"); cur = mod
        lines, fb = [], ""
        for l in body.splitlines():
            l = l.strip(); ok = l[0] == "="; txt, _, f = l[1:].partition(" #")
            lines.append(("- ✔ " if ok else "- ") + un(txt))
            if ok: fb = un(f)
        out.append(f"**{name}.** {un(stem)}\n\n" + "\n".join(lines) + f"\n\n*{fb}*")
    return out


def docx(md_path, out, titulo, sub):
    subprocess.run(["node", f"{H}/md2docx.js", out, titulo, sub, md_path], env=ENV, check=True, capture_output=True)


def escribir(dest, nombre, partes, titulo, sub):
    md = "\n\n".join(partes) + "\n"
    p = os.path.join(dest, nombre + ".md"); open(p, "w").write(md)
    docx(p, os.path.join(dest, nombre + ".docx"), titulo, sub)
    return len(md.split())


def lecciones_legibles(paths, parte0, rotulo):
    out = []
    for i, p in enumerate(paths, parte0):
        t = open(p).read()
        out.append(re.sub(r"(?m)^# ", f"# {rotulo} {i}. ", t, count=1))
    return out


# ---------------------------------------------------------------------------
# Textos de cada carpeta

def leeme(c):
    L = [c["titulo"].upper(), c["sub"], "", c["intro"], "", c["t_estructura"], "-" * len(c["t_estructura"])]
    for carpeta, desc in c["carpetas"]:
        L.append(f"{carpeta:<22}{desc}")
    L += ["", c["t_lista"], "-" * len(c["t_lista"])] + [f"[ ] {x}" for x in c["lista"]]
    if c.get("notas"):
        L += ["", c["t_notas"], "-" * len(c["t_notas"])] + [f"- {x}" for x in c["notas"]]
    return "\n".join(L) + "\n"


def moodle_txt(c):
    L = [c["t_moodle"], "", c["moodle_intro"], ""] + [f"- {z}" for z in c["zips"]]
    return "\n".join(L) + "\n"


ES = dict(t_estructura="QUÉ HAY EN ESTA CARPETA", t_lista="LISTA PARA DAR EL CURSO POR COMPLETO",
          t_notas="A TENER EN CUENTA", t_moodle="PAQUETES DE MOODLE DE ESTE CURSO",
          moodle_intro="Copia aquí estos zips (están en la carpeta de entregas; no se incluyen en este zip por su tamaño). "
                       "Descomprime todas las partes en el mismo lugar y sigue la guía de 03_Guia.")
EN = dict(t_estructura="WHAT IS IN THIS FOLDER", t_lista="CHECKLIST FOR A COMPLETE COURSE",
          t_notas="KEEP IN MIND", t_moodle="MOODLE PACKAGES FOR THIS COURSE",
          moodle_intro="Copy these zips here (they are in the deliveries folder; they are not included in this zip because of their size). "
                       "Unzip all parts in the same place and follow the guide in 03_Guide.")


def construir(c):
    raiz = os.path.join("/tmp", "carpetas", c["carpeta"]); shutil.rmtree(raiz, ignore_errors=True)
    d = {k: os.path.join(raiz, k) for k, _ in c["carpetas"] if k.endswith("/")}
    for p in d.values(): os.makedirs(p)
    k = list(d)
    # 01 manual
    for src, nombre in c["manual"]:
        shutil.copy(src, os.path.join(d[k[0]], nombre))
    if c.get("manual_fn"): c["manual_fn"](d[k[0]])
    # 02 contenido
    w = escribir(d[k[1]], c["contenido_nombre"], c["contenido"](), c["titulo"], c["contenido_sub"])
    # 03 guía
    g = escribir(d[k[2]], c["guia_nombre"], c["guia"](), c["titulo"], c["guia_sub"])
    # 04 moodle
    open(os.path.join(d[k[3]], c["moodle_nombre"]), "w").write(moodle_txt(c))
    # 05 gráficos
    if len(k) > 4:
        for src in c.get("graficos", []):
            for f in sorted(glob.glob(src)): shutil.copy(f, d[k[4]])
    open(os.path.join(raiz, c["leeme_nombre"]), "w").write(leeme(c))
    z = os.path.join(ENT, f"{c['zip']}_{FECHA}.zip")
    with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
        for r, _, fs in os.walk(raiz):
            for f in sorted(fs):
                p = os.path.join(r, f); zf.write(p, os.path.join(c["carpeta"], os.path.relpath(p, raiz)))
            if not fs and r != raiz: zf.write(r, os.path.join(c["carpeta"], os.path.relpath(r, raiz)) + "/")
    print(f"{os.path.basename(z)} · {round(os.path.getsize(z) / 1024)} KB · contenido {w} palabras · guía {g} palabras")


# ---------------------------------------------------------------------------
# 1. Tu Dinero, Tu Familia, Tu Futuro (español)

def tdtf_es_contenido():
    P = ["# Tu Dinero, Tu Familia, Tu Futuro: contenido completo",
         "Versión 3.2 · Desarrolla Talento · Piloto California. Todo lo que ve la persona participante: las 59 lecciones, el libro de apoyo, las 59 actividades H5P y el banco de 177 preguntas.",
         "| Parte | Contenido |\n|---|---|\n| 1 | Personajes |\n| 2 a 6 | Módulos 1 a 5 |\n| 7 | Materiales de apoyo |\n| 8 | Actividades H5P «¿Qué harías?» |\n| 9 | Banco de preguntas |"]
    P.append("# Parte 1. Personajes\n\n" + shift(sin_titulo(open(f"{TD}/manual/personajes.md").read())))
    P += lecciones_legibles([f"{TD}/moodle/v3/M{i}/M{i}_legible.md" for i in range(1, 6)], 2, "Parte")
    P.append("# Parte 7. Materiales de apoyo")
    P += [shift(open(f).read()) for f in sorted(glob.glob(f"{TD}/manual/v3/es/apoyo/*.md"))]
    P.append("# Parte 8. Actividades H5P «¿Qué harías?»\n\nUna actividad por lección, con los tres casos de la lección. La opción marcada con ✔ es la correcta; en la plataforma las opciones aparecen en orden aleatorio.")
    P += h5p(sorted(glob.glob(f"{TD}/manual/v3/es/M*.md")), casos(f"{H}/datos_casos.py"), "✔")
    P.append("# Parte 9. Banco de preguntas\n\n177 preguntas para las autoevaluaciones de módulo. La opción marcada con ✔ es la correcta; debajo va la retroalimentación.")
    P += banco(f"{TD}/moodle/v3/banco_preguntas_v3_es.gift.txt", "Módulo")
    return P


def tdtf_es_guia():
    P = ["# Tu Dinero, Tu Familia, Tu Futuro: guía de implementación",
         "Para el equipo que monta y opera el curso en Moodle 3.10. Tiene tres partes: cómo instalarlo, cómo funcionan los puntos, las insignias y la constancia, y qué revisar para mantenerlo al día.",
         "**Si esta guía y el manual del operador v2.0 no coinciden** en la estructura de la lección, los tipos de H5P o la calificación en la plataforma, manda esta guía: describe el curso v3.2 tal como está en Moodle.",
         "# Parte 1. Instalación en Moodle, paso a paso\n\nEscrita para que Claude (o una persona con rol de administración) la siga en el navegador.\n\n" + shift(sin_titulo(open(f"{TD}/moodle/instalacion_v31/README_INSTALAR_DESDE_CERO_PARA_CLAUDE.md").read())),
         "# Parte 2. Actividades, puntos, insignias y constancia\n\n" + shift(sin_titulo(open(f"{TD}/moodle/v3/guia_gamificacion_v3.md").read())),
         """# Parte 3. Mantenimiento

| Cuándo | Qué revisar | Dónde |
|---|---|---|
| Cada mes | Matriz comparativa de productos | Manual del operador, sección 6 |
| Antes de la temporada de impuestos (enero) | M1 U09 a U13: créditos fiscales, ITIN, VITA, preparadores | IRS y Franchise Tax Board |
| Cada año | Todo el contenido, enlaces "Para saber más" y datos con fecha | Sitios oficiales de cada institución |
| Ante cambios de ley o programa | Carga pública, Medi-Cal, impuesto a remesas y otros temas sensibles | Fuente oficial del cambio |
| Después de cada cambio | Regenerar libros, H5P y banco, y reemplazarlos en Moodle | Guía de actualización (README_ACTUALIZAR_CURSO_PARA_CLAUDE.md) |"""]
    return P


TDTF_ES = dict(ES,
    carpeta="Tu_Dinero_Tu_Familia_Tu_Futuro_ES", zip="TDTF_26_Carpeta_curso_ES",
    titulo="Tu Dinero, Tu Familia, Tu Futuro", sub=f"Curso en español · Versión 3.2 · Desarrolla Talento · {FECHA}",
    intro="Curso gratuito de finanzas personales para personas migrantes en EE. UU. (piloto California): 5 módulos, 59 lecciones.",
    carpetas=[("00_LEEME.txt", "Este archivo."),
              ("01_Manual/", "Manual del operador: qué es el programa, reglas, evaluación, métricas, privacidad y trazabilidad."),
              ("02_Contenido/", "Contenido completo: personajes, 59 lecciones, libro de apoyo, H5P y banco (.docx y .md)."),
              ("03_Guia/", "Guía de implementación: instalación en Moodle, gamificación y mantenimiento (.docx y .md)."),
              ("04_Moodle/", "Aquí van los zips del curso para Moodle (ver la lista dentro)."),
              ("05_Graficos/", "Insignias y fondo y muestra de la constancia.")],
    lista=["Manual del operador leído por coordinación", "Contenido revisado por el equipo (y por especialistas en impuestos y migración)",
           "Zips de Moodle copiados en 04_Moodle", "Curso instalado siguiendo 03_Guia, parte 1",
           "Level Up, insignias y constancia configurados (03_Guia, parte 2)", "Revisión con rol de estudiante",
           "Calendario de mantenimiento asignado a una persona (03_Guia, parte 3)"],
    notas=["El manual del operador es la versión 2.0: su marco (reglas, privacidad, métricas, expansión por estados) sigue vigente, "
           "pero la estructura de lección, los tipos de H5P y la calificación en la plataforma cambiaron en la versión 3. En esos puntos manda 03_Guia.",
           "El Manual del participante v2.1 quedó reemplazado por el contenido v3.2 (las mismas 59 lecciones, reescritas). No se incluye para no tener dos versiones.",
           "Nunca pedir SSN, ITIN, estatus migratorio ni contraseñas; no dar asesoría migratoria."],
    manual=[(f"{TD}/entregables/Manual_operador_ES_v2.docx", "Manual_del_operador_ES_v2.docx")],
    contenido=tdtf_es_contenido, contenido_nombre="Contenido_completo_TDTF_ES_v3.2", contenido_sub="Contenido completo · Versión 3.2 · Septiembre de 2026",
    guia=tdtf_es_guia, guia_nombre="Guia_implementacion_TDTF_ES_v3.2", guia_sub="Guía de implementación · Versión 3.2 · Septiembre de 2026",
    moodle_nombre="LEEME_zips_de_Moodle.txt",
    zips=["TDTF_18_Curso_completo_v3.2_parte1_curso_2026-09-28.zip", "TDTF_18_Curso_completo_v3.2_parte2_H5P_M1-M2_2026-09-28.zip",
          "TDTF_18_Curso_completo_v3.2_parte3_H5P_M3-M5_2026-09-28.zip"],
    graficos=[f"{TD}/moodle/v3/insignias/*.png", f"{TD}/moodle/v3/certificado/*.png"], leeme_nombre="00_LEEME.txt")


# ---------------------------------------------------------------------------
# 2. Your Money, Your Family, Your Future (inglés)

def tdtf_en_contenido():
    P = ["# Your Money, Your Family, Your Future: full content",
         "Version 3.2 · Desarrolla Talento · California pilot. Everything participants see: the 59 lessons, the support book, the 59 H5P activities and the 177-question bank.",
         "| Part | Content |\n|---|---|\n| 1 to 5 | Modules 1 to 5 |\n| 6 | Support materials |\n| 7 | H5P activities \"What would you do?\" |\n| 8 | Question bank |"]
    P += lecciones_legibles([f"{TD}/moodle/v3/en/M{i}/M{i}_legible.md" for i in range(1, 6)], 1, "Part")
    P.append("# Part 6. Support materials")
    P += [shift(open(f).read()) for f in sorted(glob.glob(f"{TD}/manual/v3/en/apoyo/*.md"))]
    P.append("# Part 7. H5P activities \"What would you do?\"\n\nOne activity per lesson, with the lesson's three cases. The option marked ✔ is correct; on the platform the options appear in random order.")
    P += h5p(sorted(glob.glob(f"{TD}/manual/v3/en/M*.md")), casos(f"{H}/datos_casos_en.py"), "✔")
    P.append("# Part 8. Question bank\n\n177 questions for the module self-assessments. The option marked ✔ is correct; the feedback is below it.")
    P += banco(f"{TD}/moodle/v3/en/banco_preguntas_v3_en.gift.txt", "Module")
    return P


def tdtf_en_guia():
    return ["# Your Money, Your Family, Your Future: implementation guide",
            "For the team that sets up and runs the English course in Moodle 3.10. Part 1 (installation) is written in Spanish because it is addressed to Claude and the site administrator; part 2 is in English.",
            "**If this guide and the Operator Manual v2.0 differ** on lesson structure, H5P types or platform grading, follow this guide: it describes course v3.2 as it is in Moodle.",
            "# Part 1. Installation in Moodle, step by step (Spanish)\n\n" + shift(sin_titulo(open(f"{TD}/moodle/instalacion_en/README_INSTALAR_CURSO_INGLES_PARA_CLAUDE.md").read())),
            "# Part 2. Activities, points, badges and certificate\n\n" + shift(sin_titulo(open(f"{TD}/moodle/v3/en/gamification_guide_v3.md").read())),
            """# Part 3. Maintenance

| When | What to review | Where |
|---|---|---|
| Every month | Product comparison matrix | Operator Manual, section 6 |
| Before tax season (January) | M1 U09 to U13: tax credits, ITIN, VITA, preparers | IRS and Franchise Tax Board |
| Every year | All content, "Learn more" links and dated figures | Official sites |
| When a law or program changes | Public charge, Medi-Cal, remittance tax and other sensitive topics | Official source of the change |
| After every change | Rebuild books, H5P and bank in both languages and replace them in Moodle | Spanish course update guide |"""]


TDTF_EN = dict(EN,
    carpeta="Your_Money_Your_Family_Your_Future_EN", zip="TDTF_27_Course_folder_EN",
    titulo="Your Money, Your Family, Your Future", sub=f"English course · Version 3.2 · Desarrolla Talento · {FECHA}",
    intro="Free personal finance course for immigrants in the U.S. (California pilot): 5 modules, 59 lessons. Same content as the Spanish course.",
    carpetas=[("00_README.txt", "This file."),
              ("01_Manual/", "Operator Manual: the program, rules, assessment, metrics, privacy and traceability."),
              ("02_Content/", "Full content: 59 lessons, support book, H5P and question bank (.docx and .md)."),
              ("03_Guide/", "Implementation guide: Moodle installation, gamification and maintenance (.docx and .md)."),
              ("04_Moodle/", "Put the Moodle course zips here (see the list inside)."),
              ("05_Graphics/", "Badges and certificate background and sample.")],
    lista=["Operator Manual read by the coordinator", "Content reviewed by the team and subject experts",
           "Moodle zips copied into 04_Moodle", "Course installed following 03_Guide, part 1",
           "Level Up, badges and certificate set up (03_Guide, part 2)", "Review with the student role",
           "Maintenance calendar assigned to a person (03_Guide, part 3)"],
    notas=["The Operator Manual is version 2.0: its framework (rules, privacy, metrics, state expansion) still applies, "
           "but lesson structure, H5P types and platform grading changed in version 3. On those points, follow 03_Guide.",
           "The Participant Manual v2.1 was replaced by the v3.2 content (same 59 lessons, rewritten). It is not included, to avoid two versions.",
           "Never ask for SSN, ITIN, immigration status or passwords; never give immigration advice."],
    manual=[(f"{TD}/entregables/Operator_Manual_EN_v2.docx", "Operator_Manual_EN_v2.docx")],
    contenido=tdtf_en_contenido, contenido_nombre="Full_content_TDTF_EN_v3.2", contenido_sub="Full content · Version 3.2 · September 2026",
    guia=tdtf_en_guia, guia_nombre="Implementation_guide_TDTF_EN_v3.2", guia_sub="Implementation guide · Version 3.2 · September 2026",
    moodle_nombre="README_Moodle_zips.txt",
    zips=["TDTF_25_Full_course_EN_v3.2_parte1_curso_2026-09-28.zip", "TDTF_25_Full_course_EN_v3.2_parte2_H5P_M1-M2_2026-09-28.zip",
          "TDTF_25_Full_course_EN_v3.2_parte3_H5P_M3-M5_2026-09-28.zip"],
    graficos=[f"{TD}/moodle/v3/en/insignias/*.png", f"{TD}/moodle/v3/en/certificado/*.png"], leeme_nombre="00_README.txt")


# ---------------------------------------------------------------------------
# 3. Tu Talento, Tu Marca, Tu Futuro

def ttmf_contenido():
    from_man = open(f"{TT}/manual/TTMF_manual_v2.md").read()
    pers = re.search(r"(?s)\n## Personajes\n(.*?)\n## ", from_man).group(1)
    mods = [f"M{i}" for i in range(1, 12)]
    P = ["# Tu Talento, Tu Marca, Tu Futuro: contenido completo",
         "Versión 1.2 · Desarrolla Talento. Todo lo que ve la persona participante: las 73 lecciones, el libro de apoyo, las 73 actividades H5P y el banco de 219 preguntas.",
         "| Parte | Contenido |\n|---|---|\n| 1 | Personajes |\n| 2 a 12 | Módulos 1 a 11 |\n| 13 | Materiales de apoyo |\n| 14 | Actividades H5P «¿Qué harías?» |\n| 15 | Banco de preguntas |",
         "# Parte 1. Personajes\n\n" + shift(pers.strip(), 1)]
    P += lecciones_legibles([f"{TT}/moodle/{m}/{m}_legible.md" for m in mods], 2, "Parte")
    P.append("# Parte 13. Materiales de apoyo")
    P += [shift(open(f).read()) for f in sorted(glob.glob(f"{TT}/manual/apoyo/*.md"))]
    P.append("# Parte 14. Actividades H5P «¿Qué harías?»\n\nUna actividad por lección, con los tres casos de la lección. La opción marcada con ✔ es la correcta; en la plataforma las opciones aparecen en orden aleatorio.")
    P += h5p([f"{TT}/manual/lecciones/{m}.md" for m in mods], casos(f"{TT}/herramientas/datos_casos_ttmf.py"), "✔")
    P.append("# Parte 15. Banco de preguntas\n\n219 preguntas para las autoevaluaciones de módulo. La opción marcada con ✔ es la correcta; debajo va la retroalimentación.")
    P += banco(f"{TT}/moodle/banco_preguntas_ttmf.gift.txt", "Módulo")
    return P


def ttmf_guia():
    I = f"{TT}/moodle/instalacion"
    return ["# Tu Talento, Tu Marca, Tu Futuro: guía de implementación",
            "Para el equipo que monta y opera el curso en Moodle 3.10: instalación, gamificación, comunidad y canales, y mantenimiento de los datos con fecha.",
            "# Parte 1. Instalación en Moodle, paso a paso\n\nEscrita para que Claude (o una persona con rol de administración) la siga en el navegador.\n\n" + shift(sin_titulo(open(f"{I}/README_INSTALAR_TU_TALENTO_PARA_CLAUDE.md").read())),
            "# Parte 2. Actividades, puntos, insignias y constancia\n\n" + shift(sin_titulo(open(f"{I}/guia_gamificacion_ttmf.md").read())),
            "# Parte 3. Comunidad y canales\n\nEl curso Comunidad Tu Talento tiene su propia carpeta. Aquí va el resumen de cómo se conecta con este curso.\n\n" + shift(sin_titulo(open(f"{I}/comunidad_y_canales.md").read())),
            """# Parte 4. Mantenimiento de los datos con fecha

Cada cifra de las lecciones va en un recuadro «Dato vigente» con fecha y fuente. La tabla completa está en el manual del programa, sección 7.

| Cuándo | Qué revisar | Lecciones |
|---|---|---|
| Enero | Nueva UMA (se publica en enero y rige desde el 1 de febrero): topes de deducciones, cuotas IMSS, exenciones | M2, M10, M11 |
| Enero | Resolución Miscelánea Fiscal del año (RESICO, declaración anual) | M2 |
| Enero | Salario mínimo y porcentajes de Modalidad 40 (suben cada año hasta 2030) | M10 U02, M11 U03 |
| Enero | Tarifas de INDAUTOR e IMPI | M10 U05 |
| Cada seis meses | Precios de Buró de Crédito y Círculo de Crédito (reportes, score, bloqueo, alertas) | M7 |
| Cada seis meses | Padrón de la CNBV e IPAB para las cuentas del fondo de sequía | M1, M5 |
| Cada año | REPEP, REUS y registro de líneas con CURP | M9 U08 |
| Septiembre | Mes del Testamento | M10 U06 |
| Después de cada cambio | Regenerar libros, H5P y banco, y reemplazarlos en Moodle | LEEME del paquete |"""]


TTMF = dict(ES,
    carpeta="Tu_Talento_Tu_Marca_Tu_Futuro", zip="TTMF_07_Carpeta_curso",
    titulo="Tu Talento, Tu Marca, Tu Futuro", sub=f"Versión 1.2 · Desarrolla Talento · {FECHA}",
    intro="Curso de educación financiera para personas que trabajan en el entretenimiento en México: 11 módulos, 73 lecciones, con el crédito como eje.",
    carpetas=[("00_LEEME.txt", "Este archivo."),
              ("01_Manual/", "Manual del programa v2.3: público, reglas, módulos y lecciones, personajes y datos verificados (E01 a E22)."),
              ("02_Contenido/", "Contenido completo: personajes, 73 lecciones, libro de apoyo, H5P y banco (.docx y .md)."),
              ("03_Guia/", "Guía de implementación: instalación en Moodle, gamificación, comunidad y canales, mantenimiento (.docx y .md)."),
              ("04_Moodle/", "Aquí van los zips del curso para Moodle (ver la lista dentro)."),
              ("05_Graficos/", "Insignias y fondo y muestra de la constancia.")],
    lista=["Manual del programa leído por coordinación", "Contenido revisado (fiscal y contratos por especialistas)",
           "Datos vigentes confirmados en el sitio oficial antes de publicar (manual, sección 7)",
           "Zips de Moodle copiados en 04_Moodle", "Curso instalado siguiendo 03_Guia, parte 1",
           "Level Up, insignias y constancia configurados (03_Guia, parte 2)", "Comunidad creada (carpeta Comunidad Tu Talento)",
           "Revisión con rol de estudiante", "Calendario de mantenimiento asignado a una persona (03_Guia, parte 4)"],
    notas=["Las lecciones no tienen recomendaciones comerciales; las referencias van solo en los canales y están marcadas.",
           "No se recomiendan SOFIPO, SOCAP ni SOFOM.",
           "Pendientes del manual: confirmar en la CNBV los productos de ahorro de Nu y los precios del día de Buró y Círculo."],
    manual=[(f"{TT}/manual/TTMF_manual_v2.docx", "Manual_del_programa_TTMF_v2.3.docx"), (f"{TT}/manual/TTMF_manual_v2.md", "Manual_del_programa_TTMF_v2.3.md")],
    contenido=ttmf_contenido, contenido_nombre="Contenido_completo_TTMF_v1.2", contenido_sub="Contenido completo · Versión 1.2 · Septiembre de 2026",
    guia=ttmf_guia, guia_nombre="Guia_implementacion_TTMF_v1.2", guia_sub="Guía de implementación · Versión 1.2 · Septiembre de 2026",
    moodle_nombre="LEEME_zips_de_Moodle.txt",
    zips=["TTMF_06_Curso_completo_v1.2_parte1_curso_2026-09-29.zip", "TTMF_06_Curso_completo_v1.2_parte2_H5P_M1-M6_2026-09-29.zip",
          "TTMF_06_Curso_completo_v1.2_parte3_H5P_M7-M11_2026-09-29.zip"],
    graficos=[f"{TT}/moodle/insignias/*.png", f"{TT}/moodle/certificado/*.png"], leeme_nombre="00_LEEME.txt")


# ---------------------------------------------------------------------------
# 4. Comunidad Tu Talento

def com_manual_md():
    C = f"{TT}/comunidad"
    return ["# Comunidad Tu Talento: manual de la comunidad",
            "Para coordinación y moderación. Explica para qué existe la comunidad, cómo se organiza y cómo se modera. Acompaña al curso Tu Talento, Tu Marca, Tu Futuro.",
            "# Parte 1. Comunidad y canales\n\n" + shift(sin_titulo(open(f"{TT}/moodle/instalacion/comunidad_y_canales.md").read())),
            "# Parte 2. Guía de moderación\n\n" + shift(sin_titulo(open(f"{C}/guia_moderacion.md").read()))]


def com_contenido():
    C = f"{TT}/comunidad/libro"
    P = ["# Comunidad Tu Talento: contenido",
         "El libro «Guía de la comunidad» que ven las personas participantes, en 6 capítulos."]
    P += [shift(open(f).read()) for f in sorted(glob.glob(f"{C}/*.md"))]
    return P


def com_guia():
    C = f"{TT}/comunidad"
    return ["# Comunidad Tu Talento: guía de implementación",
            "Cómo crear el espacio en Moodle y qué publicar cada mes en los foros y el canal de WhatsApp.",
            "# Parte 1. Crear la comunidad en Moodle, paso a paso\n\n" + shift(sin_titulo(open(f"{C}/README_CREAR_COMUNIDAD_PARA_CLAUDE.md").read())),
            "# Parte 2. Calendario editorial\n\n" + shift(sin_titulo(open(f"{C}/calendario_editorial.md").read()))]


def com_manual_build(dest):
    escribir(dest, "Manual_de_la_comunidad_v1.1", com_manual_md(), "Comunidad Tu Talento", "Manual de la comunidad · Versión 1.1 · Septiembre de 2026")


COM = dict(ES,
    carpeta="Comunidad_Tu_Talento", zip="TTMF_08_Carpeta_comunidad",
    titulo="Comunidad Tu Talento", sub=f"Versión 1.1 · Desarrolla Talento · {FECHA}",
    intro="Espacio en Moodle, aparte del curso, para avisos, dudas por tema, alertas de fraude, logros, sesión mensual y un foro separado de referencias comerciales. Se complementa con un canal de WhatsApp.",
    carpetas=[("00_LEEME.txt", "Este archivo."),
              ("01_Manual/", "Manual de la comunidad: propósito, espacios, canal, referencias comerciales y moderación."),
              ("02_Contenido/", "Libro «Guía de la comunidad» (6 capítulos) en .docx y .md."),
              ("03_Guia/", "Guía de implementación: creación en Moodle paso a paso y calendario editorial."),
              ("04_Moodle/", "Aquí va el zip de la comunidad para Moodle (ver la lista dentro).")],
    lista=["Equipo de moderación nombrado y con el manual leído", "Canal de WhatsApp creado (solo publica el equipo)",
           "Fecha y enlace de la primera sesión mensual", "Zip de Moodle copiado en 04_Moodle",
           "Comunidad creada siguiendo 03_Guia, parte 1", "Primeras publicaciones programadas con el calendario editorial"],
    notas=["Nunca se piden datos personales; los foros no aceptan archivos adjuntos.",
           "Las referencias comerciales solo van en su foro y en el canal, siempre marcadas; usarlas no afecta el acceso ni la constancia."],
    manual=[], manual_fn=com_manual_build, contenido=com_contenido, contenido_nombre="Guia_de_la_comunidad_contenido_v1.1", contenido_sub="Contenido · Versión 1.1 · Septiembre de 2026",
    guia=com_guia, guia_nombre="Guia_implementacion_comunidad_v1.1", guia_sub="Guía de implementación · Versión 1.1 · Septiembre de 2026",
    moodle_nombre="LEEME_zip_de_Moodle.txt", zips=["TTMF_05_Comunidad_Tu_Talento_v1.1_2026-09-29.zip"], leeme_nombre="00_LEEME.txt")


if __name__ == "__main__":
    for c in [TDTF_ES, TDTF_EN, TTMF, COM]:
        construir(c)
