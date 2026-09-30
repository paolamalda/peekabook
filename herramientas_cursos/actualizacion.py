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

# preguntas
gv, gn = gift(os.path.join(VIEJO, CONF["banco"])), gift(os.path.join(NUEVO, CONF["banco"]))
cuerpos_v = {b for _, _, b in gv}
cuerpos_n = {b for _, _, b in gn}
nuevas = [q for q in gn if q[2] not in cuerpos_v]
quitar = [q for q in gv if q[2] not in cuerpos_n]
if nuevas:
    txt, cat = [], None
    for c, nm, b in nuevas:
        if c != cat: txt.append(c + "\n"); cat = c
        txt.append(f"::{nm}::{b}\n")
    put(f"{F['pre']}/{T('preguntas_nuevas', 'new_questions')}.gift.txt", "\n".join(txt))
por_mod_n, por_mod_q = {}, {}
for c, nm, b in nuevas: por_mod_n.setdefault(nm.split()[0], []).append(nm)
for c, nm, b in quitar: por_mod_q.setdefault(nm.split()[0], []).append(nm)

# glosario
ev, _ = glos(VIEJO)
en_, cab = glos(NUEVO)
g_nuevos = [e for c, e in en_.items() if c not in ev]
if g_nuevos:
    head = re.sub(r"<NAME>[^<]*</NAME>", "<NAME>" + T("Palabras clave del curso", "Course key words") + "</NAME>", cab.split("<ENTRIES>")[0], 1)
    put(f"{F['glo']}/{T('Glosario_terminos_nuevos', 'Glossary_new_terms')}.xml", head + "<ENTRIES>\n" + "\n".join(g_nuevos) + "\n</ENTRIES></INFO></GLOSSARY>\n")

# libro de apoyo
av, an = pag_apoyo = {}, {}
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

# README
nombre_curso, apoyo_n = CONF["curso"], CONF.get("apoyo", T("Materiales de apoyo", "Support materials"))
L = []
if EN:
    L += [f"# Update {CONF['de']} → {CONF['a']} · {nombre_curso} · for Claude", "",
          f"This package updates a course **already installed** in Moodle 3.10 from version {CONF['de']} to {CONF['a']}. It only contains what changed. **Do not reinstall the course and do not delete activities, attempts, grades, badges or Level Up points.**", "",
          "Before starting: make a course backup (*Course administration > Backup*, no user data is fine) and turn editing on. If a step can't be done, skip it and report it at the end.", ""]
else:
    L += [f"# Actualización {CONF['de']} → {CONF['a']} · {nombre_curso} · para Claude", "",
          f"Este paquete actualiza un curso **ya instalado** en Moodle 3.10 de la versión {CONF['de']} a la {CONF['a']}. Solo trae lo que cambió. **No reinstales el curso ni borres actividades, intentos, calificaciones, insignias o puntos de Level Up.**", "",
          "Antes de empezar: haz una copia de seguridad del curso (*Administración del curso > Copia de seguridad*, sin datos de usuarios basta) y activa la edición. Si un paso no se puede, sáltalo y repórtalo al final.", ""]
L += [T("## Qué cambia", "## What changes"), ""]
for mod, lst in resumen_cambios:
    for c, t, e in lst:
        L.append(f"- {t} · " + (T("nueva", "new") if e == "nueva" else T("actualizada", "updated")))
if ap_cambia: L.append(T(f"- Libro «{apoyo_n}»: capítulos ", f"- \"{apoyo_n}\" book: chapters ") + ", ".join(str(int(f[:2])) for f in ap_cambia))
L.append(T(f"- {len(nuevas)} preguntas nuevas" + (f" y {len(quitar)} que salen" if quitar else "") + f"; {len(g_nuevos)} términos nuevos de glosario.",
           f"- {len(nuevas)} new questions" + (f" and {len(quitar)} retired" if quitar else "") + f"; {len(g_nuevos)} new glossary terms."))
L += ["", T("## 1. Por módulo", "## 1. By module"), ""]
for mod, n, pasos in R:
    L += [T(f"### Módulo {n}", f"### Module {n}"), ""] + [p + "\n" for p in pasos]
s = 2
if ap_cambia:
    L += [T(f"## {s}. Libro «{apoyo_n}»", f"## {s}. \"{apoyo_n}\" book"), ""]
    for f in ap_cambia:
        k = int(f[:2]); t = html.unescape(re.search(r"<title>(.*?)</title>", an[f]).group(1))
        L.append(T(f"- Capítulo {k} «{t}»: bórralo, *Importar capítulo* > `{F['lib']}/Apoyo/{f.replace('.html', '.zip')}` y súbelo con las flechas a la posición {k}.",
                   f"- Chapter {k} \"{t}\": delete it, *Import chapter* > `{F['lib']}/Apoyo/{f.replace('.html', '.zip')}` and move it up with the arrows to position {k}."))
    L.append(""); s += 1
if g_nuevos:
    L += [T(f"## {s}. Glosario", f"## {s}. Glossary"), "",
          T(f"En el glosario `Palabras clave del curso`: *Importar entradas* > `{F['glo']}/Glosario_terminos_nuevos.xml`, destino \"glosario actual\". Solo trae los {len(g_nuevos)} términos nuevos, así que no se duplican los que ya tienes.",
            f"In the `Course key words` glossary: *Import entries* > `{F['glo']}/Glossary_new_terms.xml`, destination \"current glossary\". It only has the {len(g_nuevos)} new terms, so existing ones are not duplicated."), ""]
    s += 1
if nuevas or quitar:
    L += [T(f"## {s}. Preguntas y autoevaluaciones", f"## {s}. Questions and self-assessments"), ""]
    if nuevas:
        L.append(T(f"1. *Banco de preguntas > Importar*, formato GIFT, `{F['pre']}/preguntas_nuevas.gift.txt`. Entran en las categorías que ya existen ({len(nuevas)} preguntas).",
                   f"1. *Question bank > Import*, GIFT format, `{F['pre']}/new_questions.gift.txt`. They go into the existing categories ({len(nuevas)} questions)."))
    L.append(T("2. En cada autoevaluación de abajo, abre *Editar cuestionario*. **Si el cuestionario ya tiene intentos, Moodle no deja cambiar las preguntas:** no borres intentos; déjalo como está y anótalo en tu reporte (las lecciones nuevas igual tienen su libro y su H5P). Si no tiene intentos, haz los cambios, 10 por página:",
               "2. In each self-assessment below, open *Edit quiz*. **If the quiz already has attempts, Moodle won't let you change its questions:** do not delete attempts; leave it as is and note it in your report (the new lessons still have their book and H5P). If it has no attempts, make the changes, 10 per page:"))
    for m in sorted(set(por_mod_n) | set(por_mod_q), key=lambda x: int(x[1:])):
        linea = f"   - `{autoev.format(n=m[1:])}`: "
        if m in por_mod_n: linea += T("agrega ", "add ") + ", ".join(por_mod_n[m])
        if m in por_mod_q: linea += ("; " if m in por_mod_n else "") + T("quita ", "remove ") + ", ".join(por_mod_q[m]) + T(" (versión anterior)", " (previous version)")
        L.append(linea + ".")
    L.append(""); s += 1
L += [T(f"## {s}. Lo que no cambia", f"## {s}. What doesn't change"), "",
      T("Level Up (reglas y niveles), insignias, finalización del curso y constancia siguen igual: las H5P nuevas suman puntos solas con la regla de finalización. No hace falta volver a subir ningún otro archivo.",
        "Level Up (rules and levels), badges, course completion and certificate stay the same: new H5P activities earn points automatically through the completion rule. No other file needs to be uploaded again."), ""]
s += 1
L += [T(f"## {s}. Comprueba y reporta", f"## {s}. Check and report"), "",
      T("Con *Cambiar rol a > Estudiante*, abre una lección nueva y su H5P. Reporta: capítulos por libro cambiado, H5P nuevas o reemplazadas, preguntas importadas, cuestionarios que no se pudieron cambiar por tener intentos, términos importados y lo que no pudiste hacer.",
        "With *Switch role to > Student*, open one new lesson and its H5P. Report: chapters per changed book, new or replaced H5P, imported questions, quizzes that couldn't change because they have attempts, imported terms and anything you couldn't do.")]
readme = "\n".join(L) + "\n"
put(("README_ACTUALIZAR_PARA_CLAUDE.md" if not EN else "README_UPDATE_FOR_CLAUDE.md"), readme)
zf.close()
open(os.path.join(CONF.get("readme_dir", "/tmp"), os.path.basename(salida) + ".md"), "w").write(readme)
print(salida + ".zip", round(os.path.getsize(salida + ".zip") / 1048576, 1), "MB ·",
      sum(len(l) for _, l in resumen_cambios), "lecciones ·", nuevos_h5p, "H5P nuevas ·", cambiados_h5p, "H5P cambiadas ·",
      len(nuevas), "preguntas nuevas ·", len(quitar), "salen ·", len(g_nuevos), "términos ·", len(ap_cambia), "cap. apoyo")
