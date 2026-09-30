# Arma la carpeta final de cada curso, completa y sin archivos de actualización:
#   00_LEEME · 01_Manual · 02_Contenido · 03_Guia · 04_Moodle (paquete listo para instalar)
# Cursos: Tu Dinero ES, Your Money EN, Tu Talento y Comunidad Tu Talento.
# Uso: python3 proyecto-inclusion-financiera/herramientas/carpetas_cursos.py
# Antes: regenerar libros, banco y H5P de cada curso (build_v3, quiz_gift_v3, h5p_casos, build_ttmf, quiz_ttmf,
# h5p_ttmf, apoyo_ttmf, comunidad_ttmf) y los manuales en Word.
import re, os, glob, shutil, zipfile, subprocess, importlib.util
H = os.path.dirname(os.path.abspath(__file__))
TD = os.path.dirname(H)
ROOT = os.path.dirname(TD)
TT = os.path.join(ROOT, "proyecto-entretenimiento")
ENT = os.path.join(ROOT, "entregas")
S = "/tmp/claude-0/-home-user-peekabook/2b8c84d1-874b-559e-a5dd-06af4ddd1637/scratchpad"
ENV = dict(os.environ, NODE_PATH=f"{S}/nodeenv/node_modules")
TMP = "/tmp/carpetas"


# ---------------------------------------------------------------------------
# Utilidades

def casos(path):
    spec = importlib.util.spec_from_file_location(os.path.basename(path)[:-3], path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m.CASOS


def shift(md, n=1):
    return re.sub(r"(?m)^(#{1,5}) ", lambda m: "#" * min(6, len(m.group(1)) + n) + " ", md)


def sin_titulo(md):
    return re.sub(r"(?s)^#[^\n]*\n", "", md, count=1)


def leer(p):
    return open(p, encoding="utf-8").read()


def docx(md_path, out, titulo, sub):
    subprocess.run(["node", f"{H}/md2docx.js", out, titulo, sub, md_path], env=ENV, check=True, capture_output=True)


def escribir(dest, nombre, partes, titulo, sub):
    md = "\n\n".join(partes) + "\n"
    p = os.path.join(dest, nombre + ".md"); open(p, "w", encoding="utf-8").write(md)
    docx(p, os.path.join(dest, nombre + ".docx"), titulo, sub)
    return len(md.split())


def lecciones_legibles(paths, parte0, rotulo):
    return [re.sub(r"(?m)^# ", f"# {rotulo} {i}. ", leer(p), count=1) for i, p in enumerate(paths, parte0)]


def h5p(lecciones, CASOS):
    out = []
    for f in lecciones:
        for les in re.split(r"(?m)^# (?=M\d+ U\d\d)", leer(f))[1:]:
            code, title = [x.strip() for x in les.split("\n", 1)[0].split("|", 1)]
            out.append(f"## {code}. {title}")
            cs = re.search(r"--- casos\n(.*?)\n--- ", les, re.S).group(1)
            for c, (ok, d1, d2) in zip(re.split(r"(?m)^### ", cs)[1:], CASOS[code]):
                h, b = c.split("\n", 1)
                ctx = re.sub(r"\{\{([^|}]+)\|[^}]+\}\}", r"\1", " ".join(l for l in b.splitlines() if l.strip() and not l.startswith("? ")))
                q = re.search(r"(?m)^\? (.+?)\s*\|\|", b).group(1)
                out.append(f"**{h.strip()}.** {ctx} **{q}**\n\n- ✔ {ok}\n- {d1}\n- {d2}")
    return out


def banco(gift, modulo):
    out, cur = [], None
    un = lambda s: re.sub(r"\\([~=#{}:])", r"\1", s)
    for name, stem, body in re.findall(r"::(.*?)::(.*?) \{\n(.*?)\n\}", leer(gift), re.S):
        mod = name.split()[0]
        if mod != cur: out.append(f"## {modulo} {mod[1:]}"); cur = mod
        lines, fb = [], ""
        for l in body.splitlines():
            l = l.strip(); ok = l[0] == "="; txt, _, f = l[1:].partition(" #")
            lines.append(("- ✔ " if ok else "- ") + un(txt))
            if ok: fb = un(f)
        out.append(f"**{name}.** {un(stem)}\n\n" + "\n".join(lines) + f"\n\n*{fb}*")
    return out


def glosario(xmls, nombre, destino):
    entries, seen, x = [], set(), ""
    for p in xmls:
        x = leer(p)
        for e in re.findall(r"<ENTRY>.*?</ENTRY>", x, re.S):
            c = re.search(r"<CONCEPT>(.*?)</CONCEPT>", e, re.S).group(1).strip().lower()
            if c not in seen: seen.add(c); entries.append(e)
    head = re.sub(r"<NAME>[^<]*</NAME>", f"<NAME>{nombre}</NAME>", x.split("<ENTRIES>")[0], 1)
    open(destino, "w", encoding="utf-8").write(head + "<ENTRIES>\n" + "\n".join(entries) + "\n</ENTRIES></INFO></GLOSSARY>\n")
    return len(entries)


def copiar(patron, destino, renombrar=None):
    os.makedirs(destino, exist_ok=True)
    for f in sorted(glob.glob(patron)):
        shutil.copy(f, os.path.join(destino, renombrar(os.path.basename(f)) if renombrar else os.path.basename(f)))


# ---------------------------------------------------------------------------
# Paquetes de Moodle (04_Moodle)

def moodle_tdtf(d, lang):
    en = lang == "en"
    V3 = f"{TD}/moodle/v3/en" if en else f"{TD}/moodle/v3"
    L, G, P, B, C, GU, VP = (["1_books", "3_glossary", "4_questions", "5_badges", "6_certificate", "7_guides", "8_preview"] if en else
                             ["1_libros", "3_glosario", "4_preguntas", "5_insignias", "6_certificado", "7_guias", "8_vista_previa"])
    mods = [f"M{i}" for i in range(1, 6)]
    for m in mods:
        copiar(f"{V3}/{m}/{m}_libro_Moodle.zip", f"{d}/{L}", (lambda n: n.replace("_libro_", "_book_")) if en else None)
        copiar(f"{TD}/moodle/libros/{lang}/{m}_resumen.html", f"{d}/{L}", (lambda n: n.replace("_resumen", "_summary")) if en else None)
        copiar(f"{V3}/h5p/{m}_U*.h5p", f"{d}/2_h5p/{m}")
        shutil.copytree(f"{V3}/{m}/vista_previa", f"{d}/{VP}/{m}")
    copiar(f"{V3}/Apoyo/Apoyo_libro_Moodle.zip", f"{d}/{L}", (lambda n: "Support_book_Moodle.zip") if en else None)
    os.makedirs(f"{d}/{G}")
    glosario([f"{V3}/{m}/{m}_glosario_Moodle.xml" for m in mods], "Course key words" if en else "Palabras clave del curso",
             f"{d}/{G}/" + ("Course_glossary_Moodle.xml" if en else "Glosario_curso_Moodle.xml"))
    copiar(f"{V3}/banco_preguntas_v3_{lang}.gift.txt", f"{d}/{P}", (lambda n: "question_bank_v3_en.gift.txt") if en else None)
    copiar(f"{V3}/insignias/*.png", f"{d}/{B}")
    copiar(f"{V3}/certificado/*.png", f"{d}/{C}",
           (lambda n: {"certificado_fondo.png": "certificate_background.png", "certificado_muestra.png": "certificate_sample.png"}[n]) if en else None)
    gm = f"{V3}/gamification_guide_v3.md" if en else f"{V3}/guia_gamificacion_v3.md"
    copiar(gm, f"{d}/{GU}")
    docx(gm, f"{d}/{GU}/" + os.path.basename(gm)[:-3] + ".docx",
         "Your Money, Your Family, Your Future" if en else "Tu Dinero, Tu Familia, Tu Futuro",
         "Activities, points, badges and certificate · Version 3.2" if en else "Actividades, puntos, insignias y constancia · Versión 3.2")
    copiar(f"{TD}/moodle/instalacion_en/README_INSTALAR_CURSO_INGLES_PARA_CLAUDE.md" if en else
           f"{TD}/moodle/instalacion_es/README_INSTALAR_TU_DINERO_PARA_CLAUDE.md", d)


def moodle_ttmf(d):
    M = f"{TT}/moodle"; mods = [f"M{i}" for i in range(1, 12)]
    for m in mods:
        copiar(f"{M}/{m}/{m}_libro_Moodle.zip", f"{d}/1_libros"); copiar(f"{M}/{m}/{m}_resumen.html", f"{d}/1_libros")
        copiar(f"{M}/h5p/{m}_U*.h5p", f"{d}/2_h5p/{m}")
        shutil.copytree(f"{M}/{m}/vista_previa", f"{d}/8_vista_previa/{m}")
    copiar(f"{M}/Apoyo/Apoyo_libro_Moodle.zip", f"{d}/1_libros")
    os.makedirs(f"{d}/3_glosario")
    glosario([f"{M}/{m}/{m}_glosario_Moodle.xml" for m in mods], "Palabras clave del curso", f"{d}/3_glosario/Glosario_curso_Moodle.xml")
    copiar(f"{M}/banco_preguntas_ttmf.gift.txt", f"{d}/4_preguntas")
    copiar(f"{M}/insignias/*.png", f"{d}/5_insignias"); copiar(f"{M}/certificado/*.png", f"{d}/6_certificado")
    for f in ["guia_gamificacion_ttmf.md", "comunidad_y_canales.md"]:
        copiar(f"{M}/instalacion/{f}", f"{d}/7_guias")
    docx(f"{M}/instalacion/guia_gamificacion_ttmf.md", f"{d}/7_guias/guia_gamificacion_ttmf.docx",
         "Tu Talento, Tu Marca, Tu Futuro", "Actividades, puntos, insignias y constancia · Versión 1.3")
    copiar(f"{M}/instalacion/README_INSTALAR_TU_TALENTO_PARA_CLAUDE.md", d)


def moodle_com(d):
    C = f"{TT}/comunidad"
    copiar(f"{C}/moodle/Comunidad_libro_Moodle.zip", f"{d}/1_libro")
    shutil.copytree(f"{C}/moodle/vista_previa", f"{d}/3_vista_previa")
    copiar(f"{C}/README_CREAR_COMUNIDAD_PARA_CLAUDE.md", d)


# ---------------------------------------------------------------------------
# Documentos: contenido y guía

def tdtf_contenido(lang):
    en = lang == "en"
    if en:
        P = ["# Your Money, Your Family, Your Future: full content",
             "Version 3.2 · Desarrolla Talento · California pilot. Everything participants see: the 59 lessons, the support book, the 59 H5P activities and the 177-question bank.",
             "| Part | Content |\n|---|---|\n| 1 to 5 | Modules 1 to 5 |\n| 6 | Support materials |\n| 7 | H5P activities \"What would you do?\" |\n| 8 | Question bank |"]
        P += lecciones_legibles([f"{TD}/moodle/v3/en/M{i}/M{i}_legible.md" for i in range(1, 6)], 1, "Part")
        P.append("# Part 6. Support materials")
        P += [shift(leer(f)) for f in sorted(glob.glob(f"{TD}/manual/v3/en/apoyo/*.md"))]
        P.append("# Part 7. H5P activities \"What would you do?\"\n\nOne activity per lesson, with the lesson's three cases. The option marked ✔ is correct; on the platform the options appear in random order.")
        P += h5p(sorted(glob.glob(f"{TD}/manual/v3/en/M*.md")), casos(f"{H}/datos_casos_en.py"))
        P.append("# Part 8. Question bank\n\n177 questions for the module self-assessments. The option marked ✔ is correct; the feedback is below it.")
        return P + banco(f"{TD}/moodle/v3/en/banco_preguntas_v3_en.gift.txt", "Module")
    P = ["# Tu Dinero, Tu Familia, Tu Futuro: contenido completo",
         "Versión 3.2 · Desarrolla Talento · Piloto California. Todo lo que ve la persona participante: las 59 lecciones, el libro de apoyo, las 59 actividades H5P y el banco de 177 preguntas.",
         "| Parte | Contenido |\n|---|---|\n| 1 | Personajes |\n| 2 a 6 | Módulos 1 a 5 |\n| 7 | Materiales de apoyo |\n| 8 | Actividades H5P «¿Qué harías?» |\n| 9 | Banco de preguntas |",
         "# Parte 1. Personajes\n\n" + shift(sin_titulo(leer(f"{TD}/manual/personajes.md")))]
    P += lecciones_legibles([f"{TD}/moodle/v3/M{i}/M{i}_legible.md" for i in range(1, 6)], 2, "Parte")
    P.append("# Parte 7. Materiales de apoyo")
    P += [shift(leer(f)) for f in sorted(glob.glob(f"{TD}/manual/v3/es/apoyo/*.md"))]
    P.append("# Parte 8. Actividades H5P «¿Qué harías?»\n\nUna actividad por lección, con los tres casos de la lección. La opción marcada con ✔ es la correcta; en la plataforma las opciones aparecen en orden aleatorio.")
    P += h5p(sorted(glob.glob(f"{TD}/manual/v3/es/M*.md")), casos(f"{H}/datos_casos.py"))
    P.append("# Parte 9. Banco de preguntas\n\n177 preguntas para las autoevaluaciones de módulo. La opción marcada con ✔ es la correcta; debajo va la retroalimentación.")
    return P + banco(f"{TD}/moodle/v3/banco_preguntas_v3_es.gift.txt", "Módulo")


def tdtf_guia(lang):
    if lang == "en":
        return ["# Your Money, Your Family, Your Future: implementation guide",
                "For the team that sets up and runs the English course in Moodle 3.10. Part 1 (installation) is written in Spanish because it is addressed to Claude and the site administrator; the names to type in Moodle are in English.",
                "# Part 1. Installation in Moodle, step by step\n\nThe same file is in `04_Moodle/README_INSTALAR_CURSO_INGLES_PARA_CLAUDE.md`.\n\n" + shift(sin_titulo(leer(f"{TD}/moodle/instalacion_en/README_INSTALAR_CURSO_INGLES_PARA_CLAUDE.md"))),
                "# Part 2. Activities, points, badges and certificate\n\n" + shift(sin_titulo(leer(f"{TD}/moodle/v3/en/gamification_guide_v3.md"))),
                """# Part 3. Maintenance

| When | What to review | Where |
|---|---|---|
| Every month | Product comparison matrix | Operator manual, section 6 |
| Before tax season (January) | M1 U09 to U13: tax credits, ITIN, VITA, preparers | IRS and Franchise Tax Board |
| Every year | All content, "Learn more" links and dated figures | Official sites |
| When a law or program changes | Public charge, Medi-Cal, remittance tax and other sensitive topics | Official source of the change |
| After any content change | Rebuild books, H5P and bank in both languages and rebuild this folder | Project tools |"""]
    return ["# Tu Dinero, Tu Familia, Tu Futuro: guía de implementación",
            "Para el equipo que monta y opera el curso en Moodle 3.10: instalación, puntos, insignias y constancia, y mantenimiento.",
            "# Parte 1. Instalación en Moodle, paso a paso\n\nEscrita para que Claude (o una persona con rol de administración) la siga en el navegador. El mismo archivo está en `04_Moodle/README_INSTALAR_TU_DINERO_PARA_CLAUDE.md`.\n\n" + shift(sin_titulo(leer(f"{TD}/moodle/instalacion_es/README_INSTALAR_TU_DINERO_PARA_CLAUDE.md"))),
            "# Parte 2. Actividades, puntos, insignias y constancia\n\n" + shift(sin_titulo(leer(f"{TD}/moodle/v3/guia_gamificacion_v3.md"))),
            """# Parte 3. Mantenimiento

| Cuándo | Qué revisar | Dónde |
|---|---|---|
| Cada mes | Matriz comparativa de productos | Manual del operador, sección 6 |
| Antes de la temporada de impuestos (enero) | M1 U09 a U13: créditos fiscales, ITIN, VITA, preparadores | IRS y Franchise Tax Board |
| Cada año | Todo el contenido, enlaces "Para saber más" y datos con fecha | Sitios oficiales de cada institución |
| Ante cambios de ley o programa | Carga pública, Medi-Cal, impuesto a remesas y otros temas sensibles | Fuente oficial del cambio |
| Después de cualquier cambio de contenido | Regenerar libros, H5P y banco en los dos idiomas y volver a armar esta carpeta | Herramientas del proyecto |"""]


def ttmf_contenido():
    pers = re.search(r"(?s)\n## Personajes\n(.*?)\n## ", leer(f"{TT}/manual/TTMF_manual_v2.md")).group(1)
    mods = [f"M{i}" for i in range(1, 12)]
    P = ["# Tu Talento, Tu Marca, Tu Futuro: contenido completo",
         "Versión 1.3 · Desarrolla Talento. Todo lo que ve la persona participante: las 77 lecciones, el libro de apoyo, las 77 actividades H5P y el banco de 231 preguntas.",
         "| Parte | Contenido |\n|---|---|\n| 1 | Personajes |\n| 2 a 12 | Módulos 1 a 11 |\n| 13 | Materiales de apoyo |\n| 14 | Actividades H5P «¿Qué harías?» |\n| 15 | Banco de preguntas |",
         "# Parte 1. Personajes\n\n" + shift(pers.strip())]
    P += lecciones_legibles([f"{TT}/moodle/{m}/{m}_legible.md" for m in mods], 2, "Parte")
    P.append("# Parte 13. Materiales de apoyo")
    P += [shift(leer(f)) for f in sorted(glob.glob(f"{TT}/manual/apoyo/*.md"))]
    P.append("# Parte 14. Actividades H5P «¿Qué harías?»\n\nUna actividad por lección, con los tres casos de la lección. La opción marcada con ✔ es la correcta; en la plataforma las opciones aparecen en orden aleatorio.")
    P += h5p([f"{TT}/manual/lecciones/{m}.md" for m in mods], casos(f"{TT}/herramientas/datos_casos_ttmf.py"))
    P.append("# Parte 15. Banco de preguntas\n\n219 preguntas para las autoevaluaciones de módulo. La opción marcada con ✔ es la correcta; debajo va la retroalimentación.")
    return P + banco(f"{TT}/moodle/banco_preguntas_ttmf.gift.txt", "Módulo")


def ttmf_guia():
    I = f"{TT}/moodle/instalacion"
    return ["# Tu Talento, Tu Marca, Tu Futuro: guía de implementación",
            "Para el equipo que monta y opera el curso en Moodle 3.10: instalación, gamificación, comunidad y canales, y mantenimiento de los datos con fecha.",
            "# Parte 1. Instalación en Moodle, paso a paso\n\nEscrita para que Claude (o una persona con rol de administración) la siga en el navegador. El mismo archivo está en `04_Moodle/README_INSTALAR_TU_TALENTO_PARA_CLAUDE.md`.\n\n" + shift(sin_titulo(leer(f"{I}/README_INSTALAR_TU_TALENTO_PARA_CLAUDE.md"))),
            "# Parte 2. Actividades, puntos, insignias y constancia\n\n" + shift(sin_titulo(leer(f"{I}/guia_gamificacion_ttmf.md"))),
            "# Parte 3. Comunidad y canales\n\nEl curso Comunidad Tu Talento tiene su propia carpeta. Aquí va cómo se conecta con este curso.\n\n" + shift(sin_titulo(leer(f"{I}/comunidad_y_canales.md"))),
            """# Parte 4. Mantenimiento de los datos con fecha

Cada cifra de las lecciones va en un recuadro «Dato vigente» con fecha y fuente. La tabla completa está en el manual del programa, sección 6.

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
| Después de cualquier cambio de contenido | Regenerar libros, H5P y banco y volver a armar esta carpeta | Herramientas del proyecto |"""]


def com_manual():
    C = f"{TT}/comunidad"
    return ["# Comunidad Tu Talento: manual de la comunidad",
            "Para coordinación y moderación: para qué existe la comunidad, cómo se organiza y cómo se modera. Acompaña al curso Tu Talento, Tu Marca, Tu Futuro.",
            "# Parte 1. Comunidad y canales\n\n" + shift(sin_titulo(leer(f"{TT}/moodle/instalacion/comunidad_y_canales.md"))),
            "# Parte 2. Guía de moderación\n\n" + shift(sin_titulo(leer(f"{C}/guia_moderacion.md")))]


def com_contenido():
    return ["# Comunidad Tu Talento: contenido", "El libro «Guía de la comunidad» que ven las personas participantes, en 6 capítulos."] + \
           [shift(leer(f)) for f in sorted(glob.glob(f"{TT}/comunidad/libro/*.md"))]


def com_guia():
    C = f"{TT}/comunidad"
    return ["# Comunidad Tu Talento: guía de implementación",
            "Cómo crear el espacio en Moodle y qué publicar cada mes en los foros y el canal de WhatsApp.",
            "# Parte 1. Crear la comunidad en Moodle, paso a paso\n\nEl mismo archivo está en `04_Moodle/README_CREAR_COMUNIDAD_PARA_CLAUDE.md`.\n\n" + shift(sin_titulo(leer(f"{C}/README_CREAR_COMUNIDAD_PARA_CLAUDE.md"))),
            "# Parte 2. Calendario editorial\n\n" + shift(sin_titulo(leer(f"{C}/calendario_editorial.md")))]


# ---------------------------------------------------------------------------
# Definición de cada curso

def manual_tdtf(lang):
    def f(d):
        if lang == "en":
            shutil.copy(f"{TD}/entregables/Operator_Manual_EN_v3.docx", f"{d}/Operator_Manual_EN_v3.0.docx")
            open(f"{d}/Operator_Manual_EN_v3.0.md", "w").write(leer(f"{TD}/operador/en/operator.md") + "\n\n---\n\n" + leer(f"{TD}/operador/en/traceability.md"))
        else:
            shutil.copy(f"{TD}/entregables/Manual_operador_ES_v3.docx", f"{d}/Manual_del_operador_ES_v3.0.docx")
            open(f"{d}/Manual_del_operador_ES_v3.0.md", "w").write(leer(f"{TD}/operador/es/operador.md") + "\n\n---\n\n" + leer(f"{TD}/operador/es/trazabilidad.md"))
    return f


def manual_ttmf(d):
    shutil.copy(f"{TT}/manual/TTMF_manual_v2.docx", f"{d}/Manual_del_programa_TTMF_v2.4.docx")
    shutil.copy(f"{TT}/manual/TTMF_manual_v2.md", f"{d}/Manual_del_programa_TTMF_v2.4.md")


def manual_com(d):
    escribir(d, "Manual_de_la_comunidad_v1.1", com_manual(), "Comunidad Tu Talento", "Manual de la comunidad · Versión 1.1 · Septiembre de 2026")
    escribir(d, "Manual_del_profesor_comunidad_v1", [leer(f"{TT}/comunidad/manual_profesor.md")], "Comunidad Tu Talento", "Manual del profesor · Versión 1 · Septiembre de 2026")


ES_TXT = dict(t_estructura="QUÉ HAY EN ESTA CARPETA", t_lista="LISTA PARA DAR EL CURSO POR COMPLETO",
              t_notas="A TENER EN CUENTA", t_armar="CÓMO SE ARMA", dirs=["01_Manual", "02_Contenido", "03_Guia", "04_Moodle"])
EN_TXT = dict(t_estructura="WHAT IS IN THIS FOLDER", t_lista="CHECKLIST FOR A COMPLETE COURSE",
              t_notas="KEEP IN MIND", t_armar="HOW IT FITS TOGETHER", dirs=["01_Manual", "02_Content", "03_Guide", "04_Moodle"])

CURSOS = [
 dict(ES_TXT, carpeta="Tu_Dinero_Tu_Familia_Tu_Futuro_ES", zip="Tu_Dinero_ES_v3.2", leeme="00_LEEME.txt",
      titulo="Tu Dinero, Tu Familia, Tu Futuro", sub="Curso en español · Versión 3.2 · Desarrolla Talento · Septiembre de 2026",
      intro="Curso sin costo de finanzas personales para personas migrantes en EE. UU. (piloto California): 5 módulos, 59 lecciones.",
      desc=["Manual del operador v3.0: programa, reglas, editorial, evaluación y claves, métricas, matriz, expansión por estados, privacidad y trazabilidad.",
            "Contenido completo v3.2: personajes, 59 lecciones, libro de apoyo, 59 H5P y banco de 177 preguntas (.docx y .md).",
            "Guía de implementación v3.2: instalación en Moodle, puntos, insignias y constancia, y mantenimiento (.docx y .md).",
            "Paquete para instalar: libros, H5P, glosario, banco, insignias, constancia, guía de gamificación, vista previa y el README para Claude."],
      lista=["Coordinación leyó el manual del operador", "Contenido revisado por especialistas en impuestos y en migración",
             "Curso instalado con 04_Moodle/README_INSTALAR_TU_DINERO_PARA_CLAUDE.md", "Level Up, insignias y constancia configurados",
             "Revisión con rol de estudiante", "Calendario de mantenimiento asignado (03_Guia, parte 3)"],
      notas=["Nunca pedir SSN, ITIN, estatus migratorio ni contraseñas; no dar asesoría migratoria.",
             "Algunos datos de las lecciones están marcados [POR CONFIRMAR]: confírmalos en la fuente oficial antes de abrir el curso."],
      manual=manual_tdtf("es"), contenido=lambda: tdtf_contenido("es"), guia=lambda: tdtf_guia("es"), moodle=lambda d: moodle_tdtf(d, "es"),
      n_cont="Contenido_completo_TDTF_ES_v3.2", s_cont="Contenido completo · Versión 3.2 · Septiembre de 2026",
      n_guia="Guia_implementacion_TDTF_ES_v3.2", s_guia="Guía de implementación · Versión 3.2 · Septiembre de 2026",
      h5p_partes=[["M1", "M2"], ["M3", "M4", "M5"]]),
 dict(EN_TXT, carpeta="Your_Money_Your_Family_Your_Future_EN", zip="Your_Money_EN_v3.2", leeme="00_README.txt",
      titulo="Your Money, Your Family, Your Future", sub="English course · Version 3.2 · Desarrolla Talento · September 2026",
      intro="Free personal finance course for immigrants in the U.S. (California pilot): 5 modules, 59 lessons. Same content as the Spanish course.",
      desc=["Operator manual v3.0: program, rules, editorial guide, assessment and keys, metrics, matrix, state expansion, privacy and traceability.",
            "Full content v3.2: 59 lessons, support book, 59 H5P activities and 177-question bank (.docx and .md).",
            "Implementation guide v3.2: Moodle installation, points, badges and certificate, and maintenance (.docx and .md).",
            "Installation package: books, H5P, glossary, bank, badges, certificate, gamification guide, preview and the README for Claude."],
      lista=["Coordinator read the operator manual", "Content reviewed by a native English speaker and subject experts",
             "Course installed with 04_Moodle/README_INSTALAR_CURSO_INGLES_PARA_CLAUDE.md", "Level Up, badges and certificate set up",
             "Review with the student role", "Maintenance calendar assigned (03_Guide, part 3)"],
      notas=["Never ask for SSN, ITIN, immigration status or passwords; never give immigration advice.",
             "Some lesson facts are marked [POR CONFIRMAR]: confirm them at the official source before opening the course.",
             "Mexican names (AFORE, CURP, IMSS, matrícula consular) stay in Spanish on purpose."],
      manual=manual_tdtf("en"), contenido=lambda: tdtf_contenido("en"), guia=lambda: tdtf_guia("en"), moodle=lambda d: moodle_tdtf(d, "en"),
      n_cont="Full_content_TDTF_EN_v3.2", s_cont="Full content · Version 3.2 · September 2026",
      n_guia="Implementation_guide_TDTF_EN_v3.2", s_guia="Implementation guide · Version 3.2 · September 2026",
      h5p_partes=[["M1", "M2"], ["M3", "M4", "M5"]]),
]


def leeme(c, n_partes):
    en = c is CURSOS[1]
    L = [c["titulo"].upper(), c["sub"], "", c["intro"], "", c["t_estructura"], "-" * len(c["t_estructura"]),
         f"{c['leeme']:<16}" + ("This file." if en else "Este archivo.")]
    L += [f"{d + '/':<16}{t}" for d, t in zip(c["dirs"], c["desc"])]
    if n_partes > 1:
        L += ["", c["t_armar"], "-" * len(c["t_armar"]),
              (f"The folder comes in {n_partes} zips because of size. Unzip them all in the same place: they merge into this folder." if en else
               f"La carpeta viene en {n_partes} zips por su tamaño. Descomprímelos todos en el mismo lugar: se juntan en esta carpeta."),
              ("Part 1 has everything except the H5P activities; the other parts add 04_Moodle/2_h5p." if en else
               "La parte 1 trae todo menos las actividades H5P; las otras partes agregan 04_Moodle/2_h5p.")]
    L += ["", c["t_lista"], "-" * len(c["t_lista"])] + [f"[ ] {x}" for x in c["lista"]]
    L += ["", c["t_notas"], "-" * len(c["t_notas"])] + [f"- {x}" for x in c["notas"]]
    return "\n".join(L) + "\n"


def construir(c):
    raiz = os.path.join(TMP, c["carpeta"]); shutil.rmtree(raiz, ignore_errors=True)
    d = [os.path.join(raiz, x) for x in c["dirs"]]
    for p in d: os.makedirs(p)
    c["manual"](d[0])
    w = escribir(d[1], c["n_cont"], c["contenido"](), c["titulo"], c["s_cont"])
    g = escribir(d[2], c["n_guia"], c["guia"](), c["titulo"], c["s_guia"])
    c["moodle"](d[3])
    partes = [("1", lambda rel: "04_Moodle/2_h5p" not in rel)]
    for i, grupo in enumerate(c["h5p_partes"], 2):
        partes.append((str(i), lambda rel, g=grupo: any(rel.startswith(f"04_Moodle/2_h5p/{m}/") for m in g)))
    n = len(partes)
    open(os.path.join(raiz, c["leeme"]), "w").write(leeme(c, n))
    for num, keep in partes:
        nombre = f"{c['zip']}.zip" if n == 1 else f"{c['zip']}_parte{num}de{n}.zip"
        z = os.path.join(ENT, nombre)
        with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
            if num != "1": zf.write(os.path.join(raiz, c["leeme"]), os.path.join(c["carpeta"], c["leeme"]))
            for r, _, fs in os.walk(raiz):
                for f in sorted(fs):
                    p = os.path.join(r, f); rel = os.path.relpath(p, raiz)
                    if rel == c["leeme"] and num != "1": continue
                    if keep(rel): zf.write(p, os.path.join(c["carpeta"], rel))
        print(f"{nombre} · {round(os.path.getsize(z) / 1048576, 1)} MB")
    h = len(glob.glob(f"{d[3]}/2_h5p/*/*.h5p"))
    print(f"  {c['carpeta']}: contenido {w} palabras · guía {g} palabras · {h} H5P")


if __name__ == "__main__":
    import sys
    for c in CURSOS:
        if len(sys.argv) == 1 or c["zip"] in sys.argv[1:]:
            construir(c)
