# Carpeta final de un curso generado con curso.py:
#   00_LEEME · 01_Manual · 02_Contenido · 03_Guia · 04_Moodle, en uno o varios zips (por tamaño) en entregas/.
# Si el curso tiene comunidad, arma además su carpeta propia.
import os, re, glob, shutil, zipfile
import curso as C
import carpetas_cursos as K

RAIZ = C.RAIZ
ENT = os.path.join(RAIZ, "entregas")
TMP = "/tmp/carpetas"
LIM = 24 * 1048576  # tamaño máximo aproximado de las H5P por zip


def txt(en, es_, en_):
    return en_ if en else es_


def zips(raiz, carpeta, nombre, leeme):
    """Divide en partes: la 1 sin H5P; las demás con grupos de módulos de H5P de hasta LIM bytes."""
    h5p_dirs = sorted(glob.glob(os.path.join(raiz, "04_Moodle", "2_h5p", "M*")), key=lambda p: int(os.path.basename(p)[1:]))
    grupos, cur, tam = [], [], 0
    for d in h5p_dirs:
        s = sum(os.path.getsize(f) for f in glob.glob(d + "/*"))
        if cur and tam + s > LIM: grupos.append(cur); cur, tam = [], 0
        cur.append(os.path.basename(d)); tam += s
    if cur: grupos.append(cur)
    partes = [lambda rel: "04_Moodle/2_h5p/" not in rel] + [lambda rel, g=g: any(rel.startswith(f"04_Moodle/2_h5p/{m}/") for m in g) for g in grupos]
    if sum(os.path.getsize(os.path.join(r, f)) for r, _, fs in os.walk(raiz) for f in fs) < LIM + 4 * 1048576:
        partes = [lambda rel: True]
    n = len(partes)
    for i, keep in enumerate(partes, 1):
        z = os.path.join(ENT, f"{nombre}.zip" if n == 1 else f"{nombre}_parte{i}de{n}.zip")
        with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
            if i > 1: zf.write(os.path.join(raiz, leeme), os.path.join(carpeta, leeme))
            for r, _, fs in os.walk(raiz):
                for f in sorted(fs):
                    p = os.path.join(r, f); rel = os.path.relpath(p, raiz)
                    if i > 1 and rel == leeme: continue
                    if keep(rel): zf.write(p, os.path.join(carpeta, rel))
        print(os.path.basename(z), round(os.path.getsize(z) / 1048576, 1), "MB")
    return n


def leeme_txt(en, titulo, sub, intro, estructura, n, lista, notas, nombre_leeme):
    E = [titulo.upper(), sub, "", intro, "", txt(en, "QUÉ HAY EN ESTA CARPETA", "WHAT IS IN THIS FOLDER")]
    E += ["-" * len(E[-1]), f"{nombre_leeme:<16}" + txt(en, "Este archivo.", "This file.")]
    E += [f"{d + '/':<16}{t}" for d, t in estructura]
    if n > 1:
        h = txt(en, "CÓMO SE ARMA", "HOW IT FITS TOGETHER")
        E += ["", h, "-" * len(h), txt(en, f"La carpeta viene en {n} zips por su tamaño. Descomprímelos todos en el mismo lugar: se juntan en esta carpeta.",
                                          f"The folder comes in {n} zips because of size. Unzip them all in the same place: they merge into this folder.")]
    h = txt(en, "LISTA PARA DAR EL CURSO POR COMPLETO", "CHECKLIST FOR A COMPLETE COURSE")
    E += ["", h, "-" * len(h)] + [f"[ ] {x}" for x in lista]
    if notas:
        h = txt(en, "A TENER EN CUENTA", "KEEP IN MIND")
        E += ["", h, "-" * len(h)] + [f"- {x}" for x in notas]
    return "\n".join(E) + "\n"


def construir(D, CFG):
    en = CFG.get("lang") == "en"
    F = CFG["carpeta"]
    MODS = list(CFG["modulos"])
    M = os.path.join(D, "moodle")
    raiz = os.path.join(TMP, F["nombre"]); shutil.rmtree(raiz, ignore_errors=True)
    dirs = txt(en, ["01_Manual", "02_Contenido", "03_Guia", "04_Moodle"], ["01_Manual", "02_Content", "03_Guide", "04_Moodle"])
    d = [os.path.join(raiz, x) for x in dirs]
    for p in d: os.makedirs(p)
    tit = CFG["titulo"]; ver = CFG["version"]
    # 01 Manual
    man = C.leer(os.path.join(D, "manual", "manual.md"))
    K.escribir(d[0], F["manual"], [man], tit, txt(en, f"Manual del programa · Versión {ver}", f"Program manual · Version {ver}"))
    mo_ = os.path.join(D, "manual", "mapa_ocde.md")
    if os.path.exists(mo_):
        K.escribir(d[0], txt(en, "Mapa_competencias_OCDE", "OECD_competency_map"), [C.leer(mo_)], tit, txt(en, f"Mapa de competencias OCDE · Versión {ver}", f"OECD competency map (in Spanish) · Version {ver}"))
    # 02 Contenido
    pers = re.search(r"(?s)\n## (?:Personajes|Characters)\n(.*?)\n## ", man)
    P = [f"# {tit}: " + txt(en, "contenido completo", "full content"),
         txt(en, f"Versión {ver} · Desarrolla Talento. Todo lo que ve la persona participante: lecciones, libro de apoyo, actividades H5P y banco de preguntas.",
             f"Version {ver} · Desarrolla Talento. Everything participants see: lessons, support book, H5P activities and question bank.")]
    k = 1
    if pers:
        P.append(f"# {txt(en, 'Parte', 'Part')} {k}. {txt(en, 'Personajes', 'Characters')}\n\n" + K.shift(pers.group(1).strip())); k += 1
    P += K.lecciones_legibles([os.path.join(M, m, f"{m}_legible.md") for m in MODS], k, txt(en, "Parte", "Part")); k += len(MODS)
    P.append(f"# {txt(en, 'Parte', 'Part')} {k}. {txt(en, 'Materiales de apoyo', 'Support materials')}"); k += 1
    P += [K.shift(C.leer(f)) for f in sorted(glob.glob(os.path.join(D, "apoyo", "*.md")))]
    P.append(f"# {txt(en, 'Parte', 'Part')} {k}. " + txt(en, "Actividades H5P «¿Qué harías?»\n\nUna por lección. La opción marcada con ✔ es la correcta; en la plataforma las opciones aparecen en orden aleatorio.",
                                                          "H5P activities \"What would you do?\"\n\nOne per lesson. The option marked ✔ is correct; on the platform options appear in random order.")); k += 1
    P += K.h5p([os.path.join(D, "lecciones", f"{m}.md") for m in MODS], C.casos())
    P.append(f"# {txt(en, 'Parte', 'Part')} {k}. " + txt(en, "Banco de preguntas\n\nLa opción marcada con ✔ es la correcta; debajo va la retroalimentación.",
                                                          "Question bank\n\nThe option marked ✔ is correct; the feedback is below it."))
    P += K.banco(os.path.join(M, CFG["banco"]), txt(en, "Módulo", "Module"))
    w = K.escribir(d[1], F["contenido"], P, tit, txt(en, f"Contenido completo · Versión {ver}", f"Full content · Version {ver}"))
    # 03 Guía
    I = os.path.join(D, "instalacion")
    readme = os.path.basename(glob.glob(os.path.join(I, "README_*.md"))[0])
    G = [f"# {tit}: " + txt(en, "guía de implementación", "implementation guide"),
         txt(en, "Para el equipo que monta y opera el curso en Moodle 3.10.", "For the team that sets up and runs the course in Moodle 3.10."),
         f"# {txt(en, 'Parte', 'Part')} 1. " + txt(en, "Instalación en Moodle, paso a paso", "Installation in Moodle, step by step") +
         f"\n\n{txt(en, 'El mismo archivo está en', 'The same file is in')} `04_Moodle/{readme}`.\n\n" + K.shift(K.sin_titulo(C.leer(os.path.join(I, readme)))),
         f"# {txt(en, 'Parte', 'Part')} 2. " + txt(en, "Actividades, puntos, insignias y constancia", "Activities, points, badges and certificate") +
         "\n\n" + K.shift(K.sin_titulo(C.leer(os.path.join(I, txt(en, "guia_gamificacion.md", "gamification_guide.md")))))]
    extra = 3
    if os.path.exists(os.path.join(I, "comunidad_y_canales.md")):
        G.append(f"# {txt(en, 'Parte', 'Part')} {extra}. " + txt(en, "Comunidad y canales", "Community and channels") + "\n\n" + K.shift(K.sin_titulo(C.leer(os.path.join(I, "comunidad_y_canales.md"))))); extra += 1
    if os.path.exists(os.path.join(I, "mantenimiento.md")):
        G.append(f"# {txt(en, 'Parte', 'Part')} {extra}. " + txt(en, "Mantenimiento", "Maintenance") + "\n\n" + K.shift(K.sin_titulo(C.leer(os.path.join(I, "mantenimiento.md")))))
    g = K.escribir(d[2], F["guia"], G, tit, txt(en, f"Guía de implementación · Versión {ver}", f"Implementation guide · Version {ver}"))
    # 04 Moodle
    L, Gl, Pr, Bd, Ce, Gu, Vp, En = txt(en, ["1_libros", "3_glosario", "4_preguntas", "5_insignias", "6_constancia", "7_guias", "9_vista_previa", "8_encuestas"],
                                        ["1_books", "3_glossary", "4_questions", "5_badges", "6_certificate", "7_guides", "9_preview", "8_surveys"])
    mo = d[3]
    for m in MODS:
        K.copiar(os.path.join(M, m, f"{m}_libro_Moodle.zip"), os.path.join(mo, L))
        K.copiar(os.path.join(M, m, f"{m}_resumen.html"), os.path.join(mo, L))
        K.copiar(os.path.join(M, "h5p", f"{m}_U*.h5p"), os.path.join(mo, "2_h5p", m))
        shutil.copytree(os.path.join(M, m, "vista_previa"), os.path.join(mo, Vp, m))
    K.copiar(os.path.join(M, "Apoyo", "Apoyo_libro_Moodle.zip"), os.path.join(mo, L))
    os.makedirs(os.path.join(mo, Gl))
    nterm = K.glosario([os.path.join(M, m, f"{m}_glosario_Moodle.xml") for m in MODS], txt(en, "Palabras clave del curso", "Course key words"),
                       os.path.join(mo, Gl, txt(en, "Glosario_curso_Moodle.xml", "Course_glossary_Moodle.xml")))
    K.copiar(os.path.join(M, CFG["banco"]), os.path.join(mo, Pr))
    K.copiar(os.path.join(M, "insignias", "*.png"), os.path.join(mo, Bd))
    K.copiar(os.path.join(M, "constancia", "*.md"), os.path.join(mo, Ce))
    K.copiar(os.path.join(M, "encuesta", "*.xml"), os.path.join(mo, En)); K.copiar(os.path.join(M, "encuesta", "*.md"), os.path.join(mo, En))
    K.copiar(os.path.join(M, txt(en, "tarjeta_catalogo.md", "catalog_card.md")), mo)
    gn = txt(en, "guia_gamificacion", "gamification_guide")
    K.copiar(os.path.join(I, gn + ".md"), os.path.join(mo, Gu))
    K.docx(os.path.join(I, gn + ".md"), os.path.join(mo, Gu, gn + ".docx"), tit,
           txt(en, "Actividades, puntos, insignias y constancia", "Activities, points, badges and certificate"))
    if os.path.exists(os.path.join(I, "comunidad_y_canales.md")):
        os.makedirs(os.path.join(mo, Gu), exist_ok=True)
        shutil.copy(os.path.join(I, "comunidad_y_canales.md"), os.path.join(mo, Gu, txt(en, "comunidad_y_canales.md", "community_and_channels.md")))
    K.copiar(os.path.join(I, readme), mo)
    est = list(zip(dirs, F["descripciones"]))
    leeme = txt(en, "00_LEEME.txt", "00_README.txt")
    # primero calcula partes para el texto del LEEME
    open(os.path.join(raiz, leeme), "w").write("")
    h5p_total = sum(os.path.getsize(f) for f in glob.glob(os.path.join(mo, "2_h5p", "*", "*.h5p")))
    tot = sum(os.path.getsize(os.path.join(r, f)) for r, _, fs in os.walk(raiz) for f in fs)
    n_est = 1 if tot < LIM + 4 * 1048576 else 1 + max(1, -(-h5p_total // LIM))
    open(os.path.join(raiz, leeme), "w").write(leeme_txt(en, tit, CFG["subtitulo"], CFG["intro"], est, n_est, F["lista"], F.get("notas", []), leeme))
    for old in glob.glob(os.path.join(ENT, F["zip"] + "*.zip")): os.remove(old)
    n = zips(raiz, F["nombre"], F["zip"], leeme)
    print(f"  {F['nombre']}: contenido {w} palabras · guía {g} palabras · {len(glob.glob(os.path.join(mo, '2_h5p', '*', '*.h5p')))} H5P · {nterm} términos · {n} zip(s)")
    if CFG.get("comunidad"):
        construir_comunidad(D, CFG)


def construir_comunidad(D, CFG):
    en = CFG.get("lang") == "en"
    Cm = CFG["comunidad"]; F = Cm["carpeta"]
    CD = os.path.join(D, "comunidad")
    raiz = os.path.join(TMP, F["nombre"]); shutil.rmtree(raiz, ignore_errors=True)
    dirs = txt(en, ["01_Manual", "02_Contenido", "03_Guia", "04_Moodle"], ["01_Manual", "02_Content", "03_Guide", "04_Moodle"])
    d = [os.path.join(raiz, x) for x in dirs]
    for p in d: os.makedirs(p)
    tit = Cm["titulo"]; ver = Cm["version"]
    K.escribir(d[0], txt(en, "Manual_del_profesor", "Teacher_manual"), [C.leer(os.path.join(CD, "manual_profesor.md"))], tit,
               txt(en, f"Manual del profesor · Versión {ver}", f"Teacher manual · Version {ver}"))
    I = os.path.join(D, "instalacion")
    MC = [f"# {tit}: " + txt(en, "manual de la comunidad", "community manual")]
    if os.path.exists(os.path.join(I, "comunidad_y_canales.md")):
        MC.append(f"# {txt(en, 'Parte', 'Part')} 1. " + txt(en, "Comunidad y canales", "Community and channels") + "\n\n" + K.shift(K.sin_titulo(C.leer(os.path.join(I, "comunidad_y_canales.md")))))
    MC.append(f"# {txt(en, 'Parte', 'Part')} 2. " + txt(en, "Guía de moderación", "Moderation guide") + "\n\n" + K.shift(K.sin_titulo(C.leer(os.path.join(CD, "guia_moderacion.md")))))
    K.escribir(d[0], txt(en, "Manual_de_la_comunidad", "Community_manual"), MC, tit, txt(en, f"Manual de la comunidad · Versión {ver}", f"Community manual · Version {ver}"))
    K.escribir(d[1], txt(en, "Guia_de_la_comunidad_contenido", "Community_guide_content"),
               [f"# {tit}: " + txt(en, "contenido", "content")] + [K.shift(C.leer(f)) for f in sorted(glob.glob(os.path.join(CD, "libro", "*.md")))],
               tit, txt(en, f"Contenido · Versión {ver}", f"Content · Version {ver}"))
    readme = os.path.basename(glob.glob(os.path.join(CD, "README_*.md"))[0])
    K.escribir(d[2], txt(en, "Guia_implementacion_comunidad", "Community_implementation_guide"),
               [f"# {tit}: " + txt(en, "guía de implementación", "implementation guide"),
                f"# {txt(en, 'Parte', 'Part')} 1. " + txt(en, "Crear la comunidad en Moodle, paso a paso", "Create the community in Moodle, step by step") + "\n\n" + K.shift(K.sin_titulo(C.leer(os.path.join(CD, readme)))),
                f"# {txt(en, 'Parte', 'Part')} 2. " + txt(en, "Calendario editorial", "Editorial calendar") + "\n\n" + K.shift(K.sin_titulo(C.leer(os.path.join(CD, "calendario_editorial.md")))) ],
               tit, txt(en, f"Guía de implementación · Versión {ver}", f"Implementation guide · Version {ver}"))
    K.copiar(os.path.join(CD, "moodle", "Comunidad_libro_Moodle.zip"), os.path.join(d[3], txt(en, "1_libro", "1_book")))
    shutil.copytree(os.path.join(CD, "moodle", "vista_previa"), os.path.join(d[3], txt(en, "3_vista_previa", "3_preview")))
    K.copiar(os.path.join(CD, readme), d[3])
    leeme = txt(en, "00_LEEME.txt", "00_README.txt")
    open(os.path.join(raiz, leeme), "w").write(leeme_txt(en, tit, Cm["subtitulo"], Cm["intro"], list(zip(dirs, F["descripciones"])), 1, F["lista"], F.get("notas", []), leeme))
    for old in glob.glob(os.path.join(ENT, F["zip"] + "*.zip")): os.remove(old)
    zips(raiz, F["nombre"], F["zip"], leeme)
