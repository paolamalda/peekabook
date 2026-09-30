# Paquete de actualización: compara la salida de Moodle de una versión entregada con la actual y arma un zip
# solo con lo que cambió (lecciones, H5P, preguntas, glosario, resúmenes y libro de apoyo) y un README para Claude.
# Uso: python3 herramientas_cursos/actualizacion.py <moodle_viejo> <moodle_nuevo> <config.json>
import re, os, sys, json, glob, zipfile, io, html, difflib

VIEJO, NUEVO, CONF = sys.argv[1], sys.argv[2], json.load(open(sys.argv[3]))
EN = CONF.get("lang") == "en"
T = lambda es, en: en if EN else es


def pag_libro(ruta):
    """{lección: {'titulo', 'nombre', 'paginas': {archivo: html}}} en orden."""
    out = {}
    if not os.path.exists(ruta): return out
    with zipfile.ZipFile(ruta) as z:
        for f in sorted(z.namelist()):
            m = re.match(r"\d+_m(\d+)u(\d+)_", f)
            if not m: continue
            cod = f"M{int(m.group(1))} U{m.group(2)}"
            h = z.read(f).decode("utf-8")
            d = out.setdefault(cod, {"paginas": {}})
            d["paginas"][f] = h
            if f.endswith("_0.html"):
                t = html.unescape(re.search(r"<title>(.*?)</title>", h).group(1))
                d["titulo"] = t
                d["nombre"] = re.sub(r"^M\d+ U\d+\.\s*", "", t)
    return out


def cuerpo(p):  # contenido comparable de una lección (sin nombres de archivo)
    return "\n".join(p["paginas"][k] for k in sorted(p["paginas"]))


def texto(h): return html.unescape(re.sub(r"<[^>]+>", "", h)).strip()


def edicion_menor(pv, pn):
    """Si la lección solo cambia en una línea corta por página, devuelve [(subcapítulo, antes, después)]."""
    if sorted(pv["paginas"]) != sorted(pn["paginas"]): return None
    out = []
    for f in sorted(pn["paginas"]):
        a, b = pv["paginas"][f], pn["paginas"][f]
        if a == b: continue
        x, y = re.sub(r">", ">\n", a).splitlines(), re.sub(r">", ">\n", b).splitlines()
        d = [l for l in difflib.ndiff(x, y) if l[:2] in ("- ", "+ ")]
        if len(d) != 2 or not d[0].startswith("- ") or not d[1].startswith("+ "): return None
        antes, despues = texto(d[0][2:]), texto(d[1][2:])
        if not antes or len(despues) > 300: return None
        t = html.unescape(re.search(r"<title>(.*?)</title>", b).group(1))
        out.append((t, antes, despues))
    return out


def h5p_json(ruta):
    with zipfile.ZipFile(ruta) as z:
        return z.read("content/content.json").decode() + z.read("h5p.json").decode()


def h5p_de(base, cod):
    m, u = cod.split()
    r = glob.glob(os.path.join(base, "**", f"{m}_{u}_*.h5p"), recursive=True)
    return r[0] if r else None


def gift(ruta):
    """lista de (categoría, nombre, cuerpo)"""
    out, cat = [], ""
    for bloque in re.split(r"\n\s*\n", open(ruta, encoding="utf-8").read()):
        b = bloque.strip()
        if b.startswith("$CATEGORY"): cat = b; continue
        m = re.match(r"::(.+?)::(.*)", b, re.S)
        if m: out.append((cat, m.group(1), m.group(2).strip()))
    return out


def glos(base):
    ent = {}
    for f in sorted(glob.glob(os.path.join(base, "M*", "M*_glosario_Moodle.xml"))):
        x = open(f, encoding="utf-8").read()
        for e in re.findall(r"<ENTRY>.*?</ENTRY>", x, re.S):
            c = re.search(r"<CONCEPT>(.*?)</CONCEPT>", e, re.S).group(1).strip().lower()
            ent.setdefault(c, e)
    return ent, x


mods = sorted({os.path.basename(os.path.dirname(p)) for p in glob.glob(os.path.join(NUEVO, "M*", "M*_libro_Moodle.zip"))},
              key=lambda m: int(m[1:]))
salida = os.path.join(CONF["entregas"], CONF["nombre"])
raiz = CONF["nombre"]
zf = zipfile.ZipFile(salida + ".zip", "w", zipfile.ZIP_DEFLATED)
put = lambda rel, data: zf.writestr(f"{raiz}/{rel}", data)
F = {"lib": T("1_libros", "1_books"), "h5p": "2_h5p", "glo": T("3_glosario", "3_glossary"),
     "pre": T("4_preguntas", "4_questions"), "res": T("5_resumenes", "5_section_summaries")}

libro_n = CONF.get("libro", T("Lecciones del Módulo {n}", "Module {n} lessons"))
h5p_n = CONF.get("h5p", T("{c} · ¿Qué harías?", "{c} · What would you do?"))
autoev = CONF.get("autoev", T("Autoevaluación del Módulo {n}", "Module {n} self-assessment"))
R = []  # pasos por módulo
resumen_cambios = []
nuevos_h5p = cambiados_h5p = 0
for mod in mods:
    n = mod[1:]
    vie = pag_libro(os.path.join(VIEJO, mod, f"{mod}_libro_Moodle.zip"))
    nue = pag_libro(os.path.join(NUEVO, mod, f"{mod}_libro_Moodle.zip"))
    por_nombre = {v["nombre"]: k for k, v in vie.items()}
    pasos, lec_cambio = [], []
    borrar, importar = [], []
    for cod, p in nue.items():
        viejo = por_nombre.get(p["nombre"])
        if viejo is None:
            estado = "nueva"
        elif cuerpo(vie[viejo]) != cuerpo(p):
            estado = "cambia"
        else:
            estado = "igual"
        if estado == "igual" and viejo == cod: continue
        if estado == "igual": estado = "cambia"  # renumerada: su portada y ruta cambian
        lec_cambio.append((cod, p, estado, viejo))
    if not lec_cambio and not os.path.exists(os.path.join(VIEJO, mod)):
        pass
    # libro
    if lec_cambio:
        orden = list(nue.values())
        ediciones = []
        for cod, p, estado, viejo in lec_cambio:
            if estado == "cambia" and viejo == cod:
                em = edicion_menor(vie[viejo], p)
                if em:
                    ediciones += [(p["titulo"], *e) for e in em]; continue
            z = io.BytesIO()
            with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as lz:
                for f in sorted(p["paginas"]): lz.writestr(f, p["paginas"][f])
            nom = f"{mod}_{cod.split()[1]}_{T('leccion', 'lesson')}.zip"
            put(f"{F['lib']}/{mod}/{nom}", z.getvalue())
            if estado == "cambia": borrar.append(vie[viejo]["titulo"])
            importar.append((nom, p["titulo"], estado))
        paso = [T(f"**Libro `{libro_n.format(n=n)}`**", f"**Book `{libro_n.format(n=n)}`**")]
        if borrar:
            paso.append(T("1. Borra estos capítulos (cada uno con sus 3 subcapítulos; la finalización del libro no se pierde): ",
                          "1. Delete these chapters (each with its 3 subchapters; book completion is not lost): ")
                        + "; ".join(f"«{b}»" for b in borrar) + ".")
        k = 2 if borrar else 1
        for tit, sub, antes, despues in ediciones:
            paso.append(T(f"{k}. En «{tit}», subcapítulo «{sub}», *Editar*: cambia el texto «{antes}» por «{despues}» y guarda.",
                          f"{k}. In \"{tit}\", subchapter \"{sub}\", *Edit*: change the text \"{antes}\" to \"{despues}\" and save."))
            k += 1
        for nom, tit, est in importar:
            paso.append(T(f"{k}. *Importar capítulo* > `{F['lib']}/{mod}/{nom}`, tipo \"Cada archivo HTML representa un capítulo\". Crea «{tit}» con 3 subcapítulos.",
                          f"{k}. *Import chapter* > `{F['lib']}/{mod}/{nom}`, type \"Each HTML file represents one chapter\". It creates \"{tit}\" with 3 subchapters."))
            k += 1
        if importar: paso.append(T(f"{k}. Moodle agrega lo importado al final. Con las flechas de *Editar*, deja los capítulos principales en este orden (cada uno con sus subcapítulos): ",
                      f"{k}. Moodle adds imported chapters at the end. Use the arrows in *Edit* to leave the main chapters in this order (each with its subchapters): ")
                    + " → ".join(f"«{v['titulo']}»" for v in orden) + ".")
        pasos.append("\n".join(paso))
    # resumen de sección
    rv, rn = os.path.join(VIEJO, mod, f"{mod}_resumen.html"), os.path.join(NUEVO, mod, f"{mod}_resumen.html")
    if os.path.exists(rn) and (not os.path.exists(rv) or open(rv).read() != open(rn).read()):
        put(f"{F['res']}/{mod}_resumen.html", open(rn).read())
        pasos.append(T(f"**Resumen de la sección:** *Editar sección* del Módulo {n} > descripción, vista de código HTML, reemplaza todo con `{F['res']}/{mod}_resumen.html`.",
                       f"**Section summary:** *Edit section* for Module {n} > summary, HTML source view, replace everything with `{F['res']}/{mod}_resumen.html`."))
    # H5P
    hp = []
    for cod, p in nue.items():
        hn = h5p_de(os.path.join(NUEVO, "h5p"), cod)
        viejo = por_nombre.get(p["nombre"])
        hv = h5p_de(os.path.join(VIEJO, "h5p"), viejo) if viejo else None
        if not hn: continue
        nombre_act = h5p_n.format(c=cod)
        if hv is None:
            hp.append(("nueva", cod, hn, nombre_act, None)); nuevos_h5p += 1
        elif viejo != cod or h5p_json(hv) != h5p_json(hn):
            hp.append(("cambia", cod, hn, nombre_act, h5p_n.format(c=viejo))); cambiados_h5p += 1
    hp.sort(key=lambda x: x[0] != "cambia")
    if hp:
        paso = [T("**Actividades H5P**", "**H5P activities**")]
        for est, cod, hn, act, ant in hp:
            put(f"{F['h5p']}/{mod}/{os.path.basename(hn)}", open(hn, "rb").read())
            if est == "nueva":
                paso.append(T(f"- Nueva: *Agregar actividad > Actividad H5P*, nombre `{act}`, archivo `{F['h5p']}/{mod}/{os.path.basename(hn)}`, con la misma configuración que las demás (descarga no, incrustar no, derechos de autor sí; calificación más alta; finalización \"debe recibir una calificación\").",
                              f"- New: *Add an activity > H5P*, name `{act}`, file `{F['h5p']}/{mod}/{os.path.basename(hn)}`, same settings as the others (download no, embed no, copyright yes; highest grade; completion \"must receive a grade\")."))
            else:
                paso.append(T(f"- Cambia: abre `{ant}` > *Editar ajustes*" + (f", cambia el nombre a `{act}`" if ant != act else "") + f" y reemplaza el archivo por `{F['h5p']}/{mod}/{os.path.basename(hn)}`. Los intentos anteriores se conservan.",
                              f"- Changed: open `{ant}` > *Edit settings*" + (f", rename it to `{act}`" if ant != act else "") + f" and replace the file with `{F['h5p']}/{mod}/{os.path.basename(hn)}`. Previous attempts are kept."))
        paso.append(T("- Orden final de la sección: libro, H5P en orden de lección, autoevaluación.", "- Final section order: book, H5P in lesson order, self-assessment."))
        pasos.append("\n".join(paso))
    if pasos:
        R.append((mod, n, pasos))
        resumen_cambios.append((mod, [(c, p["titulo"], e) for c, p, e, _ in lec_cambio]))

# preguntas: por nombre (M1 U01 P1). Nombre nuevo → importar; mismo nombre con otro texto → corregir en su lugar.
gv, gn = gift(os.path.join(VIEJO, CONF["banco"])), gift(os.path.join(NUEVO, CONF["banco"]))
pv = {nm: b for _, nm, b in gv}
nuevas = [q for q in gn if q[1] not in pv]
corregidas = [q for q in gn if q[1] in pv and pv[q[1]] != q[2]]
salen = [nm for nm in pv if nm not in {q[1] for q in gn}]
def gift_txt(lista):
    txt, cat = [], None
    for c, nm, b in lista:
        if c != cat: txt.append(c + "\n"); cat = c
        txt.append(f"::{nm}::{b}\n")
    return "\n".join(txt)
if nuevas: put(f"{F['pre']}/{T('preguntas_nuevas', 'new_questions')}.gift.txt", gift_txt(nuevas))
if corregidas: put(f"{F['pre']}/{T('preguntas_corregidas_referencia', 'corrected_questions_reference')}.gift.txt", gift_txt(corregidas))
por_mod_n = {}
for c, nm, b in nuevas: por_mod_n.setdefault(nm.split()[0], []).append(nm)
cat_vieja = (re.search(r"\$course\$/(.+)/M\d+", gv[0][0]).group(1) if gv else "")
cat_nueva = (re.search(r"\$course\$/(.+)/M\d+", gn[0][0]).group(1) if gn else "")

# glosario
ev, _ = glos(VIEJO)
en_, cab = glos(NUEVO)
g_nuevos = [e for c, e in en_.items() if c not in ev]
if g_nuevos:
    head = re.sub(r"<NAME>[^<]*</NAME>", "<NAME>" + T("Palabras clave del curso", "Course key words") + "</NAME>", cab.split("<ENTRIES>")[0], 1)
    put(f"{F['glo']}/{T('Glosario_terminos_nuevos', 'Glossary_new_terms')}.xml", head + "<ENTRIES>\n" + "\n".join(g_nuevos) + "\n</ENTRIES></INFO></GLOSSARY>\n")

# libro de apoyo
def apoyo(base):
    r = os.path.join(base, "Apoyo", "Apoyo_libro_Moodle.zip")
    if not os.path.exists(r): return {}
    with zipfile.ZipFile(r) as z: return {f: z.read(f).decode() for f in sorted(z.namelist())}
av, an = apoyo(VIEJO), apoyo(NUEVO)
ap_cambia = [f for f in an if av.get(f) != an[f]]
for f in ap_cambia:
    z = io.BytesIO()
    with zipfile.ZipFile(z, "w") as lz: lz.writestr(f, an[f])
    put(f"{F['lib']}/Apoyo/{f.replace('.html', '.zip')}", z.getvalue())

# ajustes de plataforma (una sola vez): encuestas, constancia, catálogo
CJ = json.load(open(CONF["curso_json"], encoding="utf-8")) if CONF.get("curso_json") else None
AJ = CONF.get("ajustes_plataforma") and CJ
if AJ:
    for f in glob.glob(os.path.join(NUEVO, "encuesta", "*")): put(f"{T('6_encuestas', '6_surveys')}/{os.path.basename(f)}", open(f, "rb").read())
    for f in glob.glob(os.path.join(NUEVO, "constancia", "*.md")): put(f"{T('7_constancia', '7_certificate')}/{os.path.basename(f)}", open(f, "rb").read())
    for f in glob.glob(os.path.join(NUEVO, T("tarjeta_catalogo.md", "catalog_card.md"))): put(os.path.basename(f), open(f, "rb").read())

# lista de cambios
cambios = []
for mod, lst in resumen_cambios:
    nue_ = [c.split()[1] for c, t, e in lst if e == "nueva"]
    if nue_: cambios.append(f"{mod}: " + T("lección nueva " if len(nue_) == 1 else "lecciones nuevas ", "new lesson " if len(nue_) == 1 else "new lessons ") + ", ".join(nue_))
    cambios += [f"{c}: " + T("texto corregido", "text corrected") for c, t, e in lst if e != "nueva"]
if ap_cambia: cambios.append(T("Apoyo: capítulos ", "Support book: chapters ") + ", ".join(str(int(f[:2])) for f in ap_cambia) + T(" corregidos", " corrected"))
if nuevas: cambios.append(T(f"Preguntas: {len(nuevas)} nuevas", f"Questions: {len(nuevas)} new"))
if corregidas: cambios.append(T(f"Preguntas: {len(corregidas)} con texto corregido", f"Questions: {len(corregidas)} with corrected text"))
if g_nuevos: cambios.append(T(f"Glosario: {len(g_nuevos)} términos nuevos", f"Glossary: {len(g_nuevos)} new terms"))
if AJ: cambios.append(T("Plataforma: categoría con versión, insignias con nombre del curso, constancia estándar, encuestas, curso visible con clave y mosaicos",
                        "Platform: versioned category, badges with course name, standard certificate, surveys, visible course with key and tiles"))

# README
nombre_curso, apoyo_n = CONF["curso"], CONF.get("apoyo", T("Materiales de apoyo", "Support materials"))
L = []
if EN:
    L += [f"# Update {CONF['de']} → {CONF['a']} · {nombre_curso} · for Claude", "",
          f"This package updates a course **already installed** in Moodle 3.10 from version {CONF['de']} to {CONF['a']}. It only contains what changed. Activity names stay the same. **Do not reinstall the course and do not delete activities, attempts, grades, badges or Level Up points.**", "",
          "Before starting: make a course backup (*Course administration > Backup*, no user data is fine) and turn editing on. If a step can't be done, skip it and report it at the end.", ""]
else:
    L += [f"# Actualización {CONF['de']} → {CONF['a']} · {nombre_curso} · para Claude", "",
          f"Este paquete actualiza un curso **ya instalado** en Moodle 3.10 de la versión {CONF['de']} a la {CONF['a']}. Solo trae lo que cambió. Los nombres de las actividades se mantienen. **No reinstales el curso ni borres actividades, intentos, calificaciones, insignias o puntos de Level Up.**", "",
          "Antes de empezar: haz una copia de seguridad del curso (*Administración del curso > Copia de seguridad*, sin datos de usuarios basta) y activa la edición. Si un paso no se puede, sáltalo y repórtalo al final.", ""]
L += [T("## Lista de cambios", "## Change list"), "", "; ".join(cambios) + ".", ""]
s_ = 1
if AJ:
    ins = [f"«{nom}» → «{nom} · {CJ['categoria']}»" for _, _, nom, _ in CJ["insignias"]]
    tem = " · ".join(CJ["constancia"]["mods"])
    L += [T(f"## {s_}. Ajustes de plataforma (una sola vez)", f"## {s_}. Platform adjustments (one time)"), ""]
    if EN:
        L += [f"1. **Question category:** in *Question bank > Categories*, rename `{cat_vieja}` to `{cat_nueva}` (its M1… subcategories stay).",
              "2. **Badges:** rename each badge so it's unique on the platform: " + "; ".join(ins) + ". Badges already issued are kept.",
              f"3. **Certificate:** edit the Custom certificate, remove the background image and use the platform's standard template with: course title «{CJ['titulo']}», line «for completing the financial well-being program {CJ['titulo']}» and topics {tem} (also in `7_certificate/`). Add the **Final survey** as an access condition.",
              "4. **Visibility and enrolment:** course **visible**; *Enrolment methods* > **Self enrolment** with the enrolment key the person gives you (\"[TBD]\" if you don't have it). Guest access off.",
              "5. **Format:** if **Tiles** is installed, switch the course format to Tiles with progress on tiles **as a percentage**; otherwise leave Topics.",
              "6. **Surveys:** with the **Feedback** module (anonymous), create `Start survey` (General section), `Final survey`, `30-day follow-up` and `90-day follow-up` (last section) and import the XML files in `6_surveys/` (`surveys.md` explains them). Restrict the follow-ups by date (\"[TBD]\").",
              "7. **Catalog:** update the course listing with `catalog_card.md`.", ""]
    else:
        L += [f"1. **Categoría de preguntas:** en *Banco de preguntas > Categorías*, renombra `{cat_vieja}` a `{cat_nueva}` (sus subcategorías M1… se quedan).",
              "2. **Insignias:** renombra cada insignia para que sea única en la plataforma: " + "; ".join(ins) + ". Las insignias ya otorgadas se conservan.",
              f"3. **Constancia:** edita el Certificado personalizado, quita la imagen de fondo y usa la plantilla estándar de la plataforma con: título «{CJ['titulo']}», línea «por concluir el programa de bienestar financiero {CJ['titulo']}» y temas {tem} (también en `7_constancia/`). Agrega la **Encuesta final** como condición de acceso.",
              "4. **Visibilidad e inscripción:** curso **visible**; *Métodos de inscripción* > **Autoinscripción** con la clave que te dé la persona («[por definir]» si no la tienes). Sin acceso de invitados.",
              "5. **Formato:** si **Mosaicos** (Tiles) está instalado, cambia el formato del curso a Mosaicos con el progreso en los mosaicos **como porcentaje**; si no, deja Temas.",
              "6. **Encuestas:** con el módulo **Retroalimentación** (anónima), crea `Encuesta de inicio` (sección General), `Encuesta final`, `Seguimiento a 30 días` y `Seguimiento a 90 días` (última sección) e importa los XML de `6_encuestas/` (`encuestas.md` los explica). Restringe los seguimientos por fecha («[por definir]»).",
              "7. **Catálogo:** actualiza la ficha del curso con `tarjeta_catalogo.md`.", ""]
    s_ += 1
L += [T(f"## {s_}. Por módulo", f"## {s_}. By module"), ""]
for mod, n, pasos in R:
    L += [T(f"### Módulo {n}", f"### Module {n}"), ""] + [p + "\n" for p in pasos]
s_ += 1
if ap_cambia:
    L += [T(f"## {s_}. Libro «{apoyo_n}»", f"## {s_}. \"{apoyo_n}\" book"), ""]
    for f in ap_cambia:
        k = int(f[:2]); t = html.unescape(re.search(r"<title>(.*?)</title>", an[f]).group(1))
        L.append(T(f"- Capítulo {k} «{t}»: bórralo, *Importar capítulo* > `{F['lib']}/Apoyo/{f.replace('.html', '.zip')}` y súbelo con las flechas a la posición {k}.",
                   f"- Chapter {k} \"{t}\": delete it, *Import chapter* > `{F['lib']}/Apoyo/{f.replace('.html', '.zip')}` and move it up with the arrows to position {k}."))
    L.append(""); s_ += 1
if g_nuevos:
    L += [T(f"## {s_}. Glosario", f"## {s_}. Glossary"), "",
          T(f"En el glosario `Palabras clave del curso`: *Importar entradas* > `{F['glo']}/Glosario_terminos_nuevos.xml`, destino \"glosario actual\". Solo trae los {len(g_nuevos)} términos nuevos.",
            f"In the `Course key words` glossary: *Import entries* > `{F['glo']}/Glossary_new_terms.xml`, destination \"current glossary\". It only has the {len(g_nuevos)} new terms."), ""]
    s_ += 1
if nuevas or corregidas:
    L += [T(f"## {s_}. Preguntas y autoevaluaciones", f"## {s_}. Questions and self-assessments"), ""]
    k = 1
    if corregidas:
        L.append(T(f"{k}. **Texto corregido ({len(corregidas)}):** en el banco, abre cada pregunta y *Editar*; reemplaza el enunciado, las opciones y la retroalimentación con los de `{F['pre']}/preguntas_corregidas_referencia.gift.txt` (mismo nombre, no la importes). Editar no borra intentos. Preguntas: " + ", ".join(q[1] for q in corregidas) + ".",
                   f"{k}. **Corrected text ({len(corregidas)}):** in the bank, open each question and *Edit*; replace the stem, options and feedback with those in `{F['pre']}/corrected_questions_reference.gift.txt` (same name, don't import it). Editing doesn't delete attempts. Questions: " + ", ".join(q[1] for q in corregidas) + "."))
        k += 1
    if nuevas:
        L.append(T(f"{k}. **Nuevas ({len(nuevas)}):** *Banco de preguntas > Importar*, formato GIFT, `{F['pre']}/preguntas_nuevas.gift.txt`. Entran en `{cat_nueva}/MN`.",
                   f"{k}. **New ({len(nuevas)}):** *Question bank > Import*, GIFT format, `{F['pre']}/new_questions.gift.txt`. They go into `{cat_nueva}/MN`."))
        k += 1
        L.append(T(f"{k}. Agrega las nuevas a su autoevaluación, 10 por página. **Si el cuestionario ya tiene intentos, Moodle no deja agregar preguntas:** no borres intentos; déjalo y anótalo en tu reporte.",
                   f"{k}. Add the new ones to their self-assessment, 10 per page. **If the quiz already has attempts, Moodle won't let you add questions:** don't delete attempts; leave it and note it in your report."))
        for m in sorted(por_mod_n, key=lambda x: int(x[1:])):
            L.append(f"   - `{autoev.format(n=m[1:])}`: " + ", ".join(por_mod_n[m]) + ".")
    L.append(""); s_ += 1
L += [T(f"## {s_}. Comprueba y reporta", f"## {s_}. Check and report"), "",
      T("Con *Cambiar rol a > Estudiante*, abre una lección nueva y su H5P. Reporta: capítulos por libro cambiado, H5P nuevas o reemplazadas, preguntas corregidas e importadas, cuestionarios que no se pudieron cambiar por tener intentos, términos importados, ajustes de plataforma hechos y lo que no pudiste hacer.",
        "With *Switch role to > Student*, open one new lesson and its H5P. Report: chapters per changed book, new or replaced H5P, corrected and imported questions, quizzes that couldn't change because they have attempts, imported terms, platform adjustments done and anything you couldn't do.")]
readme = "\n".join(L) + "\n"
put(("README_ACTUALIZAR_PARA_CLAUDE.md" if not EN else "README_UPDATE_FOR_CLAUDE.md"), readme)
put(T("LISTA_DE_CAMBIOS.txt", "CHANGE_LIST.txt"), "; ".join(cambios) + ".\n")
zf.close()
open(os.path.join(CONF.get("readme_dir", "/tmp"), os.path.basename(salida) + ".md"), "w").write(readme)
print(salida + ".zip", round(os.path.getsize(salida + ".zip") / 1048576, 1), "MB ·",
      sum(len(l) for _, l in resumen_cambios), "lecciones ·", nuevos_h5p, "H5P nuevas ·", cambiados_h5p, "H5P cambiadas ·",
      len(nuevas), "preguntas nuevas ·", len(corregidas), "corregidas ·", len(salen), "salen ·", len(g_nuevos), "términos ·", len(ap_cambia), "cap. apoyo")
