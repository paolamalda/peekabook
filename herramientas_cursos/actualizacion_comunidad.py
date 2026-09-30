# Paquete de actualización de una comunidad ya creada en Moodle: solo los capítulos que cambiaron de la
# «Guía de la comunidad», los documentos del equipo que cambiaron y los ajustes de plataforma.
# Uso: python3 herramientas_cursos/actualizacion_comunidad.py <comunidad_vieja> <cursos/<c>> <version_de>
import os, re, sys, json, zipfile, io, html

VIEJO, D, DE = sys.argv[1], sys.argv[2], sys.argv[3]
CFG = json.load(open(os.path.join(D, "curso.json"), encoding="utf-8"))
C = CFG["comunidad"]; EN = CFG.get("lang") == "en"
T = lambda es, en: en if EN else es
NUEVO = os.path.join(D, "comunidad")
A = C["version"]
nombre = C["carpeta"]["nombre"]
nombre = T(f"{nombre}_actualizacion_v{DE}_a_v{A}", f"{nombre}_update_v{DE}_to_v{A}")
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
salida = os.path.join(RAIZ, "entregas", "actualizaciones", nombre + ".zip")
texto = lambda h: re.sub(r"\s+", " ", html.unescape(re.sub(r"<style.*?</style>|<[^>]+>", " ", h, flags=re.S))).strip()

zf = zipfile.ZipFile(salida, "w", zipfile.ZIP_DEFLATED)
put = lambda p, d: zf.writestr(f"{nombre}/{p}", d)
cap = []
for f in sorted(os.listdir(os.path.join(NUEVO, "moodle"))):
    if not re.match(r"\d\d_comunidad\.html$", f): continue
    n = open(os.path.join(NUEVO, "moodle", f), encoding="utf-8").read()
    pv = os.path.join(VIEJO, "moodle", f)
    v = open(pv, encoding="utf-8").read() if os.path.exists(pv) else ""
    if texto(v) != texto(n):
        tit = html.unescape(re.search(r"<title>(.*?)</title>", n).group(1))
        tv = html.unescape(re.search(r"<title>(.*?)</title>", v).group(1)) if v else None
        z = io.BytesIO()
        with zipfile.ZipFile(z, "w") as lz: lz.writestr(f, n)
        put(f"1_libro/{f.replace('.html', '.zip')}", z.getvalue()); cap.append((int(f[:2]), tit, tv, f.replace(".html", ".zip")))
docs = []
for f in ("guia_moderacion.md", "calendario_editorial.md", "manual_profesor.md"):
    pn, pv = os.path.join(NUEVO, f), os.path.join(VIEJO, f)
    if os.path.exists(pn) and (not os.path.exists(pv) or open(pn).read() != open(pv).read()):
        put(f"{T('2_para_el_equipo', '2_for_the_team')}/{f}", open(pn, "rb").read()); docs.append(f)

corto = re.search(r"Nombre corto \| ([^ |]+)|Short name \| ([^ |]+)", open(os.path.join(NUEVO, [x for x in os.listdir(NUEVO) if x.startswith("README")][0])).read())
corto = (corto.group(1) or corto.group(2)).strip("`*") if corto else C["titulo"]
cambios = [T(f"Guía: capítulo {k} corregido", f"Guide: chapter {k} corrected") for k, *_ in cap]
cambios += [T("Plataforma: curso visible con clave de inscripción", "Platform: visible course with enrolment key")]
if docs: cambios += [T("Equipo: ", "Team: ") + ", ".join(docs)]
guia = T("Guía de la comunidad", "Community guide")
L = [T(f"# Actualización {DE} → {A} · {C['titulo']} · para Claude", f"# Update {DE} → {A} · {C['titulo']} · for Claude"), "",
     T(f"Este paquete actualiza la comunidad **ya creada** (`{corto}`) en Moodle 3.10. Solo trae lo que cambió. No borres foros, publicaciones ni participantes.",
       f"This package updates the community **already created** (`{corto}`) in Moodle 3.10. It only contains what changed. Don't delete forums, posts or participants."), "",
     T("## Lista de cambios", "## Change list"), "", "; ".join(cambios) + ".", "",
     T("## 1. Visibilidad e inscripción", "## 1. Visibility and enrolment"), "",
     T("En *Editar ajustes* del curso: visibilidad **Mostrar**. En *Participantes > Métodos de inscripción*: **Autoinscripción** activa con la clave que te dé la persona («[por definir]» si no la tienes); sin acceso de invitados. Las fechas de sesiones y los enlaces de WhatsApp se quedan como «[por definir]» hasta que la persona los dé.",
       "In the course's *Edit settings*: visibility **Show**. In *Participants > Enrolment methods*: **Self enrolment** enabled with the key the person gives you (\"[TBD]\" if you don't have it); no guest access. Session dates and WhatsApp links stay as \"[TBD]\" until the person provides them."), ""]
if cap:
    L += [T(f"## 2. Libro «{guia}»", f"## 2. \"{guia}\" book"), ""]
    for k, tit, tv, z in cap:
        L.append(T(f"- Capítulo {k}: borra «{tv}» y usa *Importar capítulo* > `1_libro/{z}` (\"Cada archivo HTML representa un capítulo\"); crea «{tit}». Súbelo con las flechas a la posición {k}.",
                   f"- Chapter {k}: delete \"{tv}\" and use *Import chapter* > `1_libro/{z}` (\"Each HTML file represents one chapter\"); it creates \"{tit}\". Move it up with the arrows to position {k}."))
    L += [T("- Si alguna página o etiqueta copió texto de estos capítulos (por ejemplo, «Sesiones de acompañamiento»), actualiza ese texto igual.",
            "- If any page or label copied text from these chapters (for example, \"Support sessions\"), update that text too."), ""]
if docs:
    L += [T("La carpeta `2_para_el_equipo/` es para el equipo de moderación: **no se sube a Moodle**.", "The `2_for_the_team/` folder is for the moderation team: **don't upload it to Moodle**."), ""]
L += [T("## Reporte", "## Report"), "", T("Reporta los capítulos reemplazados, la clave usada (sin escribirla en foros) y lo que no pudiste hacer.",
                                           "Report the chapters replaced, that the key was set (don't post it in forums) and anything you couldn't do.")]
readme = "\n".join(L) + "\n"
put(T("README_ACTUALIZAR_COMUNIDAD_PARA_CLAUDE.md", "README_UPDATE_COMMUNITY_FOR_CLAUDE.md"), readme)
put(T("LISTA_DE_CAMBIOS.txt", "CHANGE_LIST.txt"), "; ".join(cambios) + ".\n")
zf.close()
print(os.path.basename(salida), "·", len(cap), "capítulos ·", len(docs), "documentos")
