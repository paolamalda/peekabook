# Generador común de cursos (formato v3): libros de Moodle, H5P «¿Qué harías?», banco GIFT, libro de apoyo,
# libro de comunidad, insignias y constancia, verificación y carpeta final (manual, contenido, guía y Moodle).
#
# Cada curso vive en cursos/<carpeta>/ con:
#   curso.json            configuración (títulos, módulos, insignias, textos de la constancia…)
#   lecciones/M1.md …     lecciones en la sintaxis v3 (ver prompt de reescritura)
#   casos.py              CASOS = {"M1 U01": [(correcta, incorrecta, incorrecta), …]}
#   apoyo/01…06.md        libro de apoyo
#   manual/manual.md      manual del programa
#   instalacion/          README de instalación y guía de gamificación
#   comunidad/            (opcional) libro, manual del profesor, moderación, calendario y README
#
# Uso: python3 herramientas_cursos/curso.py cursos/<carpeta> [libros h5p banco apoyo comunidad insignias constancia encuesta catalogo ocde whatsapp kit herramientas verificar carpeta | todo]
import re, os, sys, json, glob, html, zipfile, shutil, subprocess, importlib.util

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HF = os.path.join(RAIZ, "proyecto-inclusion-financiera", "herramientas")
sys.path.insert(0, HF)
import build_v3 as B
from leccion_ux2 import build, page, CSS, md, terms
import leccion_ux3 as UX3
from i18n_en import tr as tr_en, tr_ux3

S = "/tmp/claude-0/-home-user-peekabook/2b8c84d1-874b-559e-a5dd-06af4ddd1637/scratchpad"
ENV = dict(os.environ, NODE_PATH=f"{S}/nodeenv/node_modules")
H5PLIB = "/tmp/h5plib"

D = os.path.abspath(sys.argv[1])
CFG = json.load(open(os.path.join(D, "curso.json"), encoding="utf-8"))
EN = CFG.get("lang") == "en"
tr = tr_en if EN else (lambda s: s)
tr3 = tr_ux3 if EN else (lambda s: s)
MODS = CFG["modulos"]  # {"M1": "Módulo 1. …"}
OUT = os.path.join(D, "moodle")
LEC = os.path.join(D, "lecciones")


def leer(p):
    return open(p, encoding="utf-8").read()


def lecciones(mod):
    """[(code, title, bloque)] de un módulo."""
    t = leer(os.path.join(LEC, f"{mod}.md"))
    out = []
    for b in re.split(r"(?m)^# (?=M\d+ U\d\d)", t)[1:]:
        code, title = [x.strip() for x in b.split("\n", 1)[0].split("|", 1)]
        out.append((code, title, b))
    return out


def casos():
    spec = importlib.util.spec_from_file_location("casos_curso", os.path.join(D, "casos.py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m.CASOS


# ---------------------------------------------------------------------------
def paso_libros():
    B.TITULOS.clear(); B.TITULOS.update(MODS)
    if CFG.get("ux") == 3: return paso_libros_ux3()
    for mod in MODS:
        text = leer(os.path.join(LEC, f"{mod}.md"))
        pages = [(fn, tr(t), tr(b)) for fn, t, b in build(text)]
        d = os.path.join(OUT, mod); os.makedirs(d, exist_ok=True)
        with zipfile.ZipFile(os.path.join(d, f"{mod}_libro_Moodle.zip"), "w", zipfile.ZIP_DEFLATED) as z:
            for fn, t, b in pages: z.writestr(fn, page(t, b))
        xml, n = B.glosario(text, ("Key words · " if EN else "Palabras clave · ") + mod)
        open(os.path.join(d, f"{mod}_glosario_Moodle.xml"), "w").write(tr(xml))
        open(os.path.join(d, f"{mod}_legible.md"), "w").write(tr(B.legible(text, mod)))
        shutil.rmtree(os.path.join(d, "vista_previa"), ignore_errors=True)
        B.preview(pages, os.path.join(d, "vista_previa"))
        if EN:
            for f in glob.glob(os.path.join(d, "vista_previa", "*.html")):
                t = tr(leer(f)); open(f, "w").write(t)
        c = B.conteo(text)
        json.dump({"lecciones": len(c), "paginas": len(pages), "terminos": n, "conteo": c}, open(os.path.join(d, "conteo.json"), "w"), ensure_ascii=False)
        # resumen de la sección de Moodle
        les = lecciones(mod)
        k = len(les); a, b = k * CFG.get("min_leccion", [10, 15])[0], k * CFG.get("min_leccion", [10, 15])[1]
        res = CFG.get("resultados", {}).get(mod, "")
        if EN:
            html_res = (f"<p><strong>Module outcome:</strong> {html.escape(res)}</p>" if res else "") + \
                f"<p><strong>Lessons:</strong> {k} · <strong>Estimated time:</strong> {a} to {b} minutes, plus activities and self-assessment.</p>" + \
                "<ol>" + "".join(f"<li>{html.escape(t)}</li>" for _, t, _ in les) + "</ol>" + \
                "<p>In this section: the lesson book, one \"What would you do?\" activity per lesson and the module self-assessment.</p>"
        else:
            html_res = (f"<p><strong>Resultado del módulo:</strong> {html.escape(res)}</p>" if res else "") + \
                f"<p><strong>Lecciones:</strong> {k} · <strong>Tiempo estimado:</strong> de {a} a {b} minutos, más actividades y autoevaluación.</p>" + \
                "<ol>" + "".join(f"<li>{html.escape(t)}</li>" for _, t, _ in les) + "</ol>" + \
                "<p>En esta sección: el libro de lecciones, una actividad «¿Qué harías?» por lección y la autoevaluación del módulo.</p>"
        open(os.path.join(d, f"{mod}_resumen.html"), "w").write(html_res)
        print(mod, "lecciones", len(c), "páginas", len(pages), "términos", n, "·", " ".join(f"{e}/{p}" for _, e, p in c))


# ---------------------------------------------------------------------------
def vista_previa_ux3(les, folder):
    """Vista previa local: cada lección con solo sus 4 capítulos; el índice aparece a un lado en pantallas grandes y no en el celular."""
    shutil.rmtree(folder, ignore_errors=True); os.makedirs(folder)
    if os.path.isdir(B.ASSETS): shutil.copytree(B.ASSETS, os.path.join(folder, "assets"), dirs_exist_ok=True)
    css = ("body{margin:0;background:#F5F7FB;font-family:Figtree,system-ui,sans-serif}.w{display:flex;gap:24px;max-width:1200px;margin:0 auto;padding:16px}"
           ".toc{flex:0 0 260px;align-self:flex-start;position:sticky;top:12px;background:#fff;border:1px solid #E5E8F0;border-radius:16px;padding:16px}"
           ".toc a{display:block;padding:6px 0;color:#0A3161;text-decoration:none}.toc a.on{font-weight:700;color:#E4007C}.toc small{color:#5A6478}"
           ".main{flex:1;min-width:0}.lista{display:flex;justify-content:space-between;gap:8px;margin:0 0 12px;font-size:.85rem}.lista a{color:#5A6478}"
           "@media(max-width:900px){.toc{display:none}.w{padding:12px}}")
    for k, L in enumerate(les, 1):
        for j, (fn, tt, b) in enumerate(L["pages"]):
            name = f"{k:02d}_{fn}"
            toc = "".join(f'<a href="{k:02d}_{f2}" class="{"on" if f2 == fn else ""}">{tr3(t2)}</a>' for f2, t2, _ in L["pages"])
            prev_l = f'<a href="{k - 1:02d}_01_empieza.html">' + ("← Previous lesson" if EN else "← Lección anterior") + '</a>' if k > 1 else "<span></span>"
            next_l = f'<a href="{k + 1:02d}_01_empieza.html">' + ("Next lesson →" if EN else "Lección siguiente →") + '</a>' if k < len(les) else "<span></span>"
            body = tr3(b).replace('href="0', f'href="{k:02d}_0')
            open(os.path.join(folder, name), "w").write(
                f'<!DOCTYPE html><html lang="{"en" if EN else "es"}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
                f'<title>{html.escape(L["title"])} · {tr3(tt)}</title><link rel="stylesheet" href="assets/fa.css">'
                f'<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800&family=Figtree:wght@400;500;600;700&display=swap" rel="stylesheet">'
                f'<style>{css}</style></head><body><div class="w"><nav class="toc"><small>{"PREVIEW · lesson" if EN else "VISTA PREVIA · lección"} {k} {"of" if EN else "de"} {len(les)}</small>'
                f'<p style="font-weight:800;color:#061F40;margin:8px 0">{html.escape(L["title"])}</p>{toc}</nav>'
                f'<div class="main"><div class="lista">{prev_l}{next_l}</div>{body}</div></div></body></html>')
    open(os.path.join(folder, "ABRIR_AQUI.html"), "w").write('<meta http-equiv="refresh" content="0; url=01_01_empieza.html">')


def paso_libros_ux3():
    """Un Libro de Moodle por lección (4 capítulos), nombre = la pregunta de la lección, y un manifiesto por módulo."""
    NOMB = CFG.get("nombres", {})  # nombres amables de cada parte: {"M1": {"titulo": …, "descripcion": …}}
    manif = {"curso": CFG["titulo"], "partes": []}
    for i, mod in enumerate(MODS):
        text = leer(os.path.join(LEC, f"{mod}.md"))
        d = os.path.join(OUT, mod); shutil.rmtree(d, ignore_errors=True); os.makedirs(os.path.join(d, "lecciones"))
        les = UX3.build(text)
        prev = []
        for k, L in enumerate(les, 1):
            zp = os.path.join(d, "lecciones", f"{k:02d}_{L['code'].replace(' ', '_')}.zip")
            with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED) as z:
                for fn, tt, b in L["pages"]: z.writestr(fn, page(tr3(tt), tr3(b)))
            prev += [(f"{k:02d}_{fn}", (L["title"] if j == 0 else tr3(tt)), tr3(b).replace('href="0', f'href="{k:02d}_0'))
                     for j, (fn, tt, b) in enumerate(L["pages"])]
        xml, n = B.glosario(text, ("Key words · " if EN else "Palabras clave · ") + mod)
        open(os.path.join(d, f"{mod}_glosario_Moodle.xml"), "w").write(tr(xml))
        open(os.path.join(d, f"{mod}_legible.md"), "w").write(tr(B.legible(text, mod)))
        vista_previa_ux3(les, os.path.join(d, "vista_previa"))
        nm = NOMB.get(mod, {})
        titulo = nm.get("titulo", MODS[mod]); desc = nm.get("descripcion", "")
        lo, hi = sum(L["min"][0] for L in les), sum(L["min"][1] for L in les)
        h = lambda m: f"{round(m / 30) / 2:g}"
        tiempo = f"unas {h(lo)} a {h(hi)} horas" if lo >= 60 else f"{lo} a {hi} minutos"
        res = CFG.get("resultados", {}).get(mod, "")
        html_res = (f"<p>{html.escape(desc)}</p>" if desc else "") + \
            (f"<p><strong>Al terminar tendrás:</strong> {html.escape(res[0].lower() + res[1:])}</p>" if res else "") + \
            f"<p><strong>{len(les)} lecciones</strong> de 10 a 15 minutos · {tiempo} en total.</p>"
        open(os.path.join(d, f"{mod}_resumen.html"), "w").write(html_res)
        manif["partes"].append({"modulo": mod, "seccion": titulo, "orden": i + 1, "resumen": html_res, "minutos": [lo, hi],
                                "lecciones": [{"orden": k, "nombre_actividad": L["title"], "zip": f"lecciones/{k:02d}_{L['code'].replace(' ', '_')}.zip",
                                               "h5p": f"h5p/{L['h5p']}", "minutos": L["min"], "clave_interna": L["code"]} for k, L in enumerate(les, 1)]})
        print(mod, titulo, "·", len(les), "lecciones ·", tiempo)
    json.dump(manif, open(os.path.join(OUT, "estructura_moodle.json"), "w"), ensure_ascii=False, indent=1)


def paso_h5p():
    LIBS = [("H5P.SingleChoiceSet", "scs"), ("H5P.JoubelUI", "h5p-joubel-ui"), ("H5P.Question", "h5p-question"),
            ("H5P.Transition", "h5p-transition"), ("H5P.FontIcons", "h5p-font-icons"), ("FontAwesome", "fa")]
    OK = re.compile(r"\.(js|css|json|png|jpg|jpeg|gif|svg|eot|ttf|woff|woff2|otf|mp3|ogg|wav)$", re.I)
    lib_files, deps = [], []
    for mach, dd in LIBS:
        meta = json.load(open(os.path.join(H5PLIB, dd, "library.json")))
        folder = f"{mach}-{meta['majorVersion']}.{meta['minorVersion']}"
        deps.append({"machineName": mach, "majorVersion": meta["majorVersion"], "minorVersion": meta["minorVersion"]})
        for r, ds, fs in os.walk(os.path.join(H5PLIB, dd)):
            ds[:] = [x for x in ds if not x.startswith(".") and x not in ("node_modules", "test", "tests")]
            for f in fs:
                if f.startswith(".") or not OK.search(f): continue
                if os.path.basename(r) == "language" and f not in ("es.json", "es-mx.json", ".en.json"): continue
                p = os.path.join(r, f)
                lib_files.append((p, folder + "/" + os.path.relpath(p, os.path.join(H5PLIB, dd))))
    if EN:
        L10N = {"nextButtonLabel": "Next case", "showSolutionButtonLabel": "See answers", "retryButtonLabel": "Try again",
                "solutionViewTitle": "Answers", "correctText": "Correct!", "incorrectText": "Not the best option",
                "shouldSelect": "This was the best option", "shouldNotSelect": "This wasn't the best option",
                "muteButtonLabel": "Mute sounds", "closeButtonLabel": "Close", "slideOfTotal": "Case :num of :total",
                "scoreBarLabel": "You got :num out of :total points", "solutionListQuestionNumber": "Case :num",
                "a11yShowSolution": "Show the answers.", "a11yRetry": "Restart the activity."}
        FB = ["Review the cases in Go deeper and try again.", "Great job! You know what to do in these situations."]
    else:
        L10N = {"nextButtonLabel": "Siguiente caso", "showSolutionButtonLabel": "Ver respuestas", "retryButtonLabel": "Intentar de nuevo",
                "solutionViewTitle": "Respuestas", "correctText": "¡Correcto!", "incorrectText": "No es la mejor opción",
                "shouldSelect": "Esta era la mejor opción", "shouldNotSelect": "Esta no era la mejor opción",
                "muteButtonLabel": "Silenciar sonidos", "closeButtonLabel": "Cerrar", "slideOfTotal": "Caso :num de :total",
                "scoreBarLabel": "Obtuviste :num de :total puntos", "solutionListQuestionNumber": "Caso :num",
                "a11yShowSolution": "Mostrar las respuestas.", "a11yRetry": "Reiniciar la actividad."}
        FB = ["Revisa los casos en Profundiza e inténtalo otra vez.", "¡Muy bien! Ya sabes qué hacer en estas situaciones."]
    if CFG.get("ux") == 3:
        L10N.update({"slideOfTotal": ":num de :total" if not EN else ":num of :total", "nextButtonLabel": "Siguiente" if not EN else "Next",
                     "solutionListQuestionNumber": "Pregunta :num" if not EN else "Question :num"})
        FB = ["Repasa Lo esencial e inténtalo otra vez.", "¡Muy bien! Ya sabes qué hacer."] if not EN else ["Review The essentials and try again.", "Great job! You know what to do."]
    CASOS = casos()
    dest_dir = os.path.join(OUT, "h5p"); shutil.rmtree(dest_dir, ignore_errors=True); os.makedirs(dest_dir)
    n = 0
    for mod in MODS:
        for code, title, les in lecciones(mod):
            cs = re.search(r"--- casos\n(.*?)\n--- ", les, re.S).group(1)
            choices = []
            for c, opts in zip(re.split(r"(?m)^### ", cs)[1:], CASOS[code]):
                h, b = c.split("\n", 1)
                ctx = re.sub(r"\{\{([^|}]+)\|[^}]+\}\}", r"\1", " ".join(l for l in b.splitlines() if l.strip() and not l.startswith("? ")))
                q = re.search(r"(?m)^\? (.+?)\s*\|\|", b).group(1)
                name = re.sub(r"^(Caso|Case) \d+\.\s*", "", h.strip())
                choices.append({"question": f"<p><strong>{html.escape(name)}.</strong> {html.escape(ctx)}</p><p><strong>{html.escape(q)}</strong></p>",
                                "answers": [f"<p>{html.escape(o)}</p>" for o in opts]})
            if CFG.get("ux") == 3:
                pr = dict((k, c) for k, _, _, c in UX3.blocks(UX3.parse(code + " | " + les.split("\n", 1)[1])[3]["practica"]))
                for q, opts, key, _ in UX3.quiz_items(pr):
                    idx = "abcde".index(key)
                    orden = [opts[idx]] + [o for j, o in enumerate(opts) if j != idx]
                    choices.append({"question": f"<p><strong>{html.escape(q)}</strong></p>", "answers": [f"<p>{html.escape(o)}</p>" for o in orden]})
            content = {"choices": choices,
                       "overallFeedback": [{"from": 0, "to": 66, "feedback": FB[0]}, {"from": 67, "to": 100, "feedback": FB[1]}],
                       "behaviour": {"autoContinue": False, "timeoutCorrect": 2000, "timeoutWrong": 3000, "soundEffectsEnabled": False,
                                     "enableRetry": True, "enableSolutionsButton": True, "passPercentage": 67},
                       "l10n": L10N}
            lab = "What would you do?" if EN else "¿Qué harías?"
            h5pjson = {"title": f"{code} {lab}", "language": "en" if EN else "es", "mainLibrary": "H5P.SingleChoiceSet",
                       "embedTypes": ["div", "iframe"], "license": "U", "defaultLanguage": "en" if EN else "es", "preloadedDependencies": deps}
            if CFG.get("ux") == 3:
                h5pjson["title"] = ("Practice · " if EN else "Practica · ") + title
                dest = os.path.join(dest_dir, UX3.h5p_nombre(code))
            else:
                dest = os.path.join(dest_dir, f"{code.replace(' ', '_')}_" + ("what_would_you_do" if EN else "que_harias") + ".h5p")
            with zipfile.ZipFile(dest, "w", zipfile.ZIP_DEFLATED) as z:
                z.writestr("h5p.json", json.dumps(h5pjson, ensure_ascii=False, indent=1))
                z.writestr("content/content.json", json.dumps(content, ensure_ascii=False))
                for p, a in lib_files: z.write(p, a)
            n += 1
    print(n, "actividades H5P")


# ---------------------------------------------------------------------------
def paso_banco():
    def esc(t): return re.sub(r"([~=#{}:])", r"\\\1", re.sub(r"\{\{([^|}]+)\|[^}]+\}\}", r"\1", t).replace("*", "").strip())
    ok_t, no_t = ("Correct!", "Not the best option.") if EN else ("¡Correcto!", "No es la mejor opción.")
    out, n, probs = [], 0, []
    for mod in MODS:
        out.append(f"$CATEGORY: $course$/{CFG['categoria']} v{CFG['version']}/{mod}\n")
        for code, title, les in lecciones(mod):
            q = re.search(r"--- quiz\n(.*?)\n(?:respuestas|answers):\s*(.*?)\n", les, re.S)
            ans = {k: (l, why.strip()) for k, l, why in re.findall(r"(\d+)-([a-c]):\s*(.*?)(?=\s\d+-[a-c]:|$)", q.group(2))}
            for k, line in re.findall(r"(?m)^(\d+)\.\s+(.*)$", q.group(1)):
                parts = re.split(r"\s+(?=[a-c]\)\s)", line)
                stem, opts = parts[0], [re.sub(r"\s*·\s*$", "", o) for o in parts[1:]]
                if k not in ans or len(opts) != 3: probs.append(f"{code} P{k}"); continue
                good, why = ans[k]; why = why[:1].upper() + why[1:]
                body = [("=" if o[0] == good else "~") + esc(o[3:]) + (f" #{ok_t} {esc(why)}" if o[0] == good else f" #{no_t} {esc(why)}") for o in opts]
                out.append(f"::{code} P{k}::{esc(stem)} {{\n" + "\n".join("\t" + b for b in body) + "\n}\n")
                n += 1
    p = os.path.join(OUT, CFG["banco"]); open(p, "w").write("\n".join(out))
    print(n, "preguntas ·", os.path.basename(p), "· problemas:", probs)


# ---------------------------------------------------------------------------
def libro(src, out_dir, zipname, sufijo, cab, leads, icons, faq_title, casos_num="02"):
    L = dict(key="See the key", ans="See the answers", hdr="Answers", keyre=r"(Key|Answers)", taskre=r"Additional task") if EN else \
        dict(key="Ver la clave", ans="Ver las respuestas", hdr="Respuestas", keyre=r"(Clave|Respuestas)", taskre=r"Tarea adicional")

    def hide(sec_md):
        m = re.search(r"(?m)^\*\*" + L["keyre"] + r"\.?\*\*", sec_md)
        if not m: return md(sec_md)
        before, rest = sec_md[:m.start()], sec_md[m.start():]
        t = re.search(r"(?m)^\*\*" + L["taskre"] + r"\.\*\*", rest)
        tail = rest[t.start():] if t else ""
        rest = rest[:t.start()] if t else rest
        return md(before) + f'<details><summary>{L["key"]}</summary><div class="a">{md(rest)}</div></details>' + md(tail)

    def faq(sec_md):
        items = re.findall(r"(?m)^\*\*(¿?[^*]+\?)\*\*\s*(.+)$", sec_md)
        return "".join(f'<details><summary>{html.escape(q)}</summary><div class="a">{md(a)}</div></details>' for q, a in items)

    os.makedirs(out_dir, exist_ok=True)
    files = []
    for p in sorted(glob.glob(os.path.join(src, "*.md"))):
        num = os.path.basename(p)[:2]
        text = leer(p).replace("[[TOC]]", "")
        tops = re.split(r"(?m)^# ", text)[1:]
        title = tops[0].split("\n", 1)[0].strip()
        body = f'<div class="hero"><span class="code"><i class="fa {icons.get(num, "fa-book")}"></i> {cab}</span><h3>{title}</h3><p class="obj">{leads.get(num, "")}</p></div>'
        for ti, top in enumerate(tops):
            h, rest = (top.split("\n", 1) + [""])[:2]
            if ti: body += f'<div class="pagehead mt-4"><h3>{h.strip()}</h3></div>'
            secs = re.split(r"(?m)^## ", rest)
            intro = secs[0].strip().strip("-").strip()
            if intro:
                body += faq(intro) if h.strip() == faq_title else f'<div class="card2">{md(intro)}</div>'
            for s in secs[1:]:
                sh, sb = (s.split("\n", 1) + [""])[:2]
                sb = sb.strip().rstrip("-").strip()
                if sh.strip() == L["hdr"]:
                    inner = f'<details><summary>{L["ans"]}</summary><div class="a">{md(sb)}</div></details>'
                elif num == casos_num:
                    inner = hide(sb)
                else:
                    inner = md(sb)
                body += f'<div class="card2"><h4>{terms(sh.strip())}</h4>{inner}</div>'
        fn = f"{num}_{sufijo}.html"
        open(os.path.join(out_dir, fn), "w", encoding="utf-8").write(page(title, f'{CSS}<div class="tdtf">{body}</div>'))
        files.append((fn, title))
    with zipfile.ZipFile(os.path.join(out_dir, zipname), "w", zipfile.ZIP_DEFLATED) as zf:
        for fn, _ in files: zf.write(os.path.join(out_dir, fn), fn)
    pages = [(fn, t, leer(os.path.join(out_dir, fn)).split("<body>")[1].split("</body>")[0]) for fn, t in files]
    shutil.rmtree(os.path.join(out_dir, "vista_previa"), ignore_errors=True)
    B.preview(pages, os.path.join(out_dir, "vista_previa"))
    print(len(files), "capítulos ·", zipname)


def paso_glosario():
    """Genera apoyo/04-glosario.md con las palabras clave de las lecciones, por módulo, sin repetir."""
    if not CFG.get("glosario_apoyo", True): return
    vistos, out = set(), ["# Glossary" if EN else "# Glosario", "",
                          ("Plain-language definitions of the course words, grouped by module." if EN else
                           "Definiciones en lenguaje sencillo de las palabras del curso, agrupadas por módulo.")]
    for mod, titulo in MODS.items():
        filas = []
        for code, title, les in lecciones(mod):
            m = re.search(r"== (?:palabras|words)\n(.*?)(?:\n== |\Z)", les, re.S)
            if not m: continue
            for k, v in re.findall(r"(?m)^- \*([^*:]+):\*\s*(.+)$", m.group(1)):
                if k.lower() in vistos: continue
                vistos.add(k.lower()); filas.append(f"- **{k.strip()}:** {v.strip()}")
        if filas:
            out += ["", "## " + re.sub(r"^(Módulo|Module) \d+\. ", "", titulo), ""] + sorted(filas, key=str.lower)
    open(os.path.join(D, "apoyo", "04-glosario.md"), "w").write("\n".join(out) + "\n")
    print(len(vistos), "términos en el glosario de apoyo")


def paso_apoyo():
    icons = {"01": "fa-home", "02": "fa-users", "03": "fa-calculator", "04": "fa-book", "05": "fa-life-ring", "06": "fa-list"}
    libro(os.path.join(D, "apoyo"), os.path.join(OUT, "Apoyo"), "Apoyo_libro_Moodle.zip", "apoyo",
          "Support materials" if EN else "Materiales de apoyo", CFG["apoyo_leads"], icons,
          "Frequently asked questions" if EN else "Preguntas frecuentes")


def paso_fondo():
    """Genera la guía «Para ir a fondo»: por parte y lección, los enlaces oficiales (con Qué buscar) y las fuentes, sin repetir."""
    F = os.path.join(D, "fondo"); shutil.rmtree(F, ignore_errors=True); os.makedirs(F)
    if EN:
        intro = """# How to go deeper

## Who this guide is for

The lessons give you the essentials. This guide is for you if you want to read the original sources, check the rules or prepare questions for an expert. You don't need it to finish the course.

## How to use it

1. Find the part and the lesson you're interested in.
2. Open the official links and follow "What to look for."
3. Check the sources: the laws, rules and documents we used to write the lesson.
4. Write down your questions and take them to the right institution.

## How to spot a source you can trust

- The site is official: it ends in .gov (U.S.) or gob.mx (Mexico), or it belongs to the institution named.
- It has a date. Rules, amounts and rates change every year: look for the current version.
- It doesn't ask you to pay or to give personal data just to get information.
- If a site or a person promises sure results, be careful.

## When to ask an expert

When your case has many details: taxes, inheritances, debts in court or contracts. First look for no-cost guidance at the public institutions in this guide, before paying anyone. This program doesn't give legal or tax advice: it helps you understand and ask better questions.
"""
        lead_i, lead_m = "For people who want to know more: official sources, rules and documents for each topic.", "Official links and sources for each lesson in this part."
        h_rec, h_fue, cab = "To read and check", "Sources for this lesson", "Further reading"
    else:
        intro = """# Cómo ir a fondo

## Para quién es esta guía

Las lecciones te dan lo esencial. Esta guía es para ti si quieres leer las fuentes originales, revisar las reglas o preparar preguntas para una persona experta. No la necesitas para terminar el curso.

## Cómo usarla

1. Busca la parte y la lección que te interesa.
2. Abre los enlaces oficiales y sigue «Qué buscar».
3. Revisa las fuentes: son las leyes, reglas y documentos que usamos para escribir la lección.
4. Anota tus preguntas y llévalas a la institución que corresponda.

## Cómo reconocer una fuente confiable

- El sitio es oficial: termina en gob.mx (México) o .gov (EE. UU.), o es de la institución que se nombra.
- Tiene fecha. Las reglas, los montos y las tasas cambian cada año: busca la versión vigente.
- No te pide pagar ni dar datos personales para informarte.
- Si un sitio o una persona te promete resultados seguros, desconfía.

## Cuándo pedir ayuda a una persona experta

Cuando tu caso tiene muchos detalles: impuestos, herencias, deudas en juicio o contratos. Antes de pagarle a alguien, busca orientación sin costo en las instituciones públicas de esta guía. Este programa no da asesoría legal ni fiscal: te ayuda a entender y a preguntar mejor.
"""
        lead_i, lead_m = "Para quien quiere saber más: fuentes oficiales, reglas y documentos de cada tema.", "Enlaces oficiales y fuentes de cada lección de esta parte."
        h_rec, h_fue, cab = "Para leer y revisar", "Fuentes de la lección", "Para ir a fondo"
    open(os.path.join(F, "01-como-ir-a-fondo.md"), "w").write(intro)
    leads, vistos = {"01": lead_i}, set()
    def enlaza(t):
        dom = lambda u: re.sub(r"^www[.]", "", u.split("://", 1)[1].split("/", 1)[0])
        return re.sub(r"(?<!\()https?://[^\s|)]+?(?=[.,;]?(?:\s|$|\|))", lambda m: "[" + dom(m.group(0)) + "](" + m.group(0) + ")", t)
    for i, (mod, titulo) in enumerate(MODS.items(), 2):
        num = f"{i:02d}"; leads[num] = lead_m
        nombre = CFG.get("nombres", {}).get(mod, {}).get("titulo") or re.sub(r"^(Módulo|Module) \d+\. ", "", titulo)
        out = [f"# {nombre}", ""]
        for code, title, les in lecciones(mod):
            rec = re.search(r"(?m)^== recursos\n(.*?)(?=^== |\Z)", les, re.S)
            fue = re.search(r"(?m)^== fuentes\n(.*?)(?=^== |\Z)", les, re.S)
            items = []
            for l in (rec.group(1).splitlines() if rec else []):
                l = l.strip()
                if not l.startswith("- "): continue
                u = re.search(r"https?://[^\s|]+", l)
                k = u.group(0).rstrip(".,/").lower() if u else l
                if k in vistos: continue
                l = re.sub(r"\s*\|\s*(Qué buscar|What to look for):\s*", lambda m: "  \n  **" + m.group(1) + ":** ", l)
                vistos.add(k); items.append(enlaza(l))
            f = re.sub(r"\[[SR]\d+\]\s*", "", " ".join(x.strip() for x in fue.group(1).splitlines() if x.strip())) if fue else ""
            if not items and not f: continue
            out += [f"## {title}", ""]
            if items: out += [f"**{h_rec}**", ""] + items + [""]
            if f: out += [f"**{h_fue}:** {f.strip()}", ""]
        open(os.path.join(F, f"{num}-{mod.lower()}.md"), "w").write("\n".join(out) + "\n")
    libro(F, os.path.join(OUT, "Fondo"), "Fondo_libro_Moodle.zip", "fondo", cab, leads, {"01": "fa-compass"}, "")


def paso_programas():
    """Módulo extra «Programas y apoyos»: aparte del curso, se oculta o se quita sin afectar nada. Solo programas vigentes."""
    import programas as PG
    F = os.path.join(D, "programas"); O = os.path.join(OUT, "Programas")
    shutil.rmtree(F, ignore_errors=True); shutil.rmtree(O, ignore_errors=True)
    ok, venc = PG.vigentes(os.path.basename(os.path.normpath(D)), EN)
    for p in venc: print(f"  AVISO: «{p['id']}» venció sin revisión ({p['revisado']}); queda fuera del libro.")
    if not ok: print("sin programas vigentes: no hay módulo extra"); return
    L = "en" if EN else "es"; os.makedirs(F)
    rev = max(p["revisado"] for p in ok)
    if EN:
        intro = f"""# About this section

## An extra section

This section is **extra**: it doesn't count toward finishing the course. It brings together government programs and public services that may help you.

## Check before you act

Information reviewed on {PG.fecha(rev, True)}. Programs change: confirm on the official site before doing any paperwork. No government program charges you to sign up.
"""
        mas, revt, cab, lead = "Learn more", "Reviewed on", "Programs and support", "Government programs and public services. Extra and optional."
    else:
        intro = f"""# Sobre esta sección

## Una sección extra

Esta sección es **extra**: no cuenta para terminar el curso. Reúne programas de gobierno y servicios públicos que pueden servirte.

## Confirma antes de actuar

Información revisada al {PG.fecha(rev, False)}. Los programas cambian: confirma en el sitio oficial antes de hacer un trámite. Ningún programa de gobierno te cobra por inscribirte.
"""
        mas, revt, cab, lead = "Para saber más", "Revisado el", "Programas y apoyos", "Programas de gobierno y servicios públicos. Extra y opcional."
    open(os.path.join(F, "01-sobre-esta-seccion.md"), "w").write(intro)
    leads = {"01": lead}
    curso = os.path.basename(os.path.normpath(D))
    # ¿Cuál es para mí? (sin pedir ni guardar datos: solo una tabla para ubicarse)
    if EN:
        cual = ["# Which one is for me?", "", "Find your situation and go to that chapter. Nothing you choose here is saved.", "", "| If… | Go to |", "|---|---|"]
    else:
        cual = ["# ¿Cuál es para mí?", "", "Busca tu situación y ve a ese capítulo. Nada de lo que elijas aquí se guarda.", "", "| Si… | Ve a |", "|---|---|"]
    def sit(p):
        t = p.get("para_quien", {}).get(L) or p["titulo"][L]
        t = re.sub(r"^(Si|If) ", "", t)
        return t[:1].upper() + t[1:]
    cual += [f"| {sit(p)} | {p['titulo'][L]} |" for p in ok]
    open(os.path.join(F, "02-cual-es-para-mi.md"), "w").write("\n".join(cual) + "\n")
    leads["02"] = lead
    for i, p in enumerate(ok, 3):
        num = f"{i:02d}"; leads[num] = lead
        rec = p.get("recurso", {}).get(L, "")
        rec = re.sub(r"(https?://[^\s|]+)", lambda m: "[" + re.sub(r"^www[.]", "", m.group(1).split("://", 1)[1].split("/", 1)[0]) + "](" + m.group(1) + ")", rec)
        rec = re.sub(r"\s*\|\s*(Qué buscar|What to look for):\s*", lambda m: "  \n  **" + m.group(1) + ":** ", rec)
        body = f"# {p['titulo'][L]}\n\n{p['texto'][L]}\n"
        if rec: body += f"\n## {mas}\n\n{rec}\n\n*{revt} {PG.fecha(p['revisado'], EN)}.*\n"
        open(os.path.join(F, f"{num}-{p['id']}.md"), "w").write(body)
    fe = PG.fechas(curso, EN)
    if fe:
        num = f"{len(ok) + 3:02d}"; leads[num] = lead
        t = ("# Dates to keep in mind" if EN else "# Fechas que conviene saber")
        txt = [t, "", ("Each date disappears on its own once it has passed." if EN else "Cada fecha desaparece sola cuando ya pasó."), ""]
        txt += [f"- **{PG.rango(f, EN)}:** {f['en' if EN else 'es']}" for f in fe]
        open(os.path.join(F, f"{num}-fechas.md"), "w").write("\n".join(txt) + "\n")
    libro(F, O, "Programas_libro_Moodle.zip", "programas", cab, leads, {"01": "fa-life-ring", "02": "fa-compass"}, "")


def paso_comunidad():
    if not CFG.get("comunidad"): return
    icons = {"01": "fa-users", "02": "fa-shield", "03": "fa-comments", "04": "fa-calendar", "05": "fa-video-camera", "06": "fa-handshake-o"}
    libro(os.path.join(D, "comunidad", "libro"), os.path.join(D, "comunidad", "moodle"), "Comunidad_libro_Moodle.zip", "comunidad",
          "Community guide" if EN else "Guía de la comunidad", CFG["comunidad"]["leads"], icons,
          "Frequently asked questions" if EN else "Preguntas frecuentes", casos_num="--")


# ---------------------------------------------------------------------------
def paso_insignias():
    A, F = "/tmp/assets_tdtf", "/tmp/fnt"
    FONTS = "<style>" + "".join(f"@font-face{{font-family:'{fam}';font-weight:{w};src:url(file://{F}/fontsource-{pk}-5.3.0/package/files/{pk}-latin-{w}-normal.woff2)}}" for fam, pk in (("Figtree", "figtree"), ("Bricolage Grotesque", "bricolage-grotesque")) for w in (500, 600, 700, 800)) + "</style>"
    T = CFG["constancia"]
    MODH = "".join(f"<span>{m}</span>" for m in T["mods"])
    curso_tag = "COURSE" if EN else "CURSO"

    def badge(tag, name, icon, gold):
        ring = "linear-gradient(135deg,#E4007C,#FF4FA8)" if gold else "linear-gradient(135deg,#0A3161,#061F40)"
        size = 34 if len(name) <= 20 else 28
        return f'''<!doctype html><html><head><meta charset=utf-8><link rel=stylesheet href="file://{A}/fa.css">{FONTS}
<style>html,body{{margin:0;background:transparent}}.b{{width:512px;height:512px;position:relative}}
.o{{position:absolute;inset:16px;border-radius:50%;background:{ring};box-shadow:0 10px 30px rgba(6,31,64,.35)}}
.i{{position:absolute;inset:44px;border-radius:50%;background:#fff;border:6px solid #E6ECF5}}
.c{{position:absolute;inset:70px;border-radius:50%;background:linear-gradient(160deg,#0A3161,#061F40);display:flex;flex-direction:column;align-items:center;justify-content:center;color:#fff}}
.c i{{font-size:120px;color:#fff}}.tag{{font:700 26px Figtree;letter-spacing:3px;color:#FF4FA8;margin-top:14px}}
.r{{position:absolute;left:18px;right:18px;bottom:38px;background:#E4007C;color:#fff;border-radius:18px;text-align:center;font:800 {size}px 'Bricolage Grotesque';padding:12px 6px;box-shadow:0 6px 16px rgba(228,0,124,.35)}}</style></head>
<body><div class=b><div class=o></div><div class=i></div><div class=c><i class="fa {icon}"></i><div class=tag>{tag}</div></div><div class=r>{name}</div></div></body></html>'''

    def cert(sample):
        return f'''<!doctype html><html><head><meta charset=utf-8><link rel=stylesheet href="file://{A}/fa.css">{FONTS}
<style>html,body{{margin:0}}.p{{width:2339px;height:1654px;position:relative;background:#fff;font-family:Figtree;overflow:hidden}}
.f{{position:absolute;inset:60px;border:10px solid #0A3161;border-radius:40px}}.f2{{position:absolute;inset:92px;border:3px solid #E4007C;border-radius:28px}}
.band{{position:absolute;left:0;top:0;bottom:0;width:26px;background:#E4007C}}
.circ{{position:absolute;right:-260px;top:-260px;width:760px;height:760px;border-radius:50%;background:#E6ECF5}}
.circ2{{position:absolute;left:-200px;bottom:-260px;width:620px;height:620px;border-radius:50%;background:#F5F7FB}}
.top{{position:absolute;top:190px;width:100%;text-align:center;color:#5A6478;font:600 44px Figtree;letter-spacing:10px}}
.t{{position:absolute;top:270px;width:100%;text-align:center;color:#0A3161;font:800 150px 'Bricolage Grotesque'}}
.otorga{{position:absolute;top:500px;width:100%;text-align:center;color:#5A6478;font:500 46px Figtree}}
.line{{position:absolute;top:760px;left:520px;right:520px;border-top:4px solid #E5E8F0}}
.name{{position:absolute;top:610px;width:100%;text-align:center;color:#0B1220;font:700 110px 'Bricolage Grotesque'}}
.txt{{position:absolute;top:810px;left:330px;right:330px;text-align:center;color:#0B1220;font:500 46px/1.45 Figtree}}
.txt b{{color:#0A3161}}.mods{{position:absolute;top:1010px;width:100%;text-align:center;font:600 32px Figtree;color:#5A6478}}
.mods span{{display:inline-block;margin:0 14px;padding:10px 26px;border-radius:40px;background:#E6ECF5;color:#0A3161}}
.foot{{position:absolute;bottom:170px;left:260px;right:260px;display:flex;justify-content:space-between;align-items:flex-end;color:#5A6478;font:500 34px Figtree}}
.foot .c{{text-align:center;width:560px}}.foot .c div{{border-top:3px solid #0A3161;padding-top:14px;margin-top:70px}}
.seal{{position:absolute;bottom:150px;left:50%;margin-left:-150px;width:300px;height:300px;border-radius:50%;background:linear-gradient(135deg,#E4007C,#FF4FA8);display:flex;align-items:center;justify-content:center;box-shadow:0 10px 30px rgba(228,0,124,.3)}}
.seal i{{font-size:140px;color:#fff}}.brand{{position:absolute;top:120px;left:150px;font:800 40px 'Bricolage Grotesque';color:#0A3161}}.brand span{{color:#E4007C}}
.nota{{position:absolute;bottom:108px;width:100%;text-align:center;font:500 24px Figtree;color:#5A6478}}.ph{{color:#E4007C}}</style></head><body><div class=p>
<div class=circ></div><div class=circ2></div><div class=band></div><div class=f></div><div class=f2></div>
<div class=brand>Desarrolla <span>Talento</span></div>
<div class=top>{T['top']}</div><div class=t>{T['titulo']}</div>
<div class=otorga>{T['otorga']}</div>{'<div class=name>' + T['nombre'] + '</div>' if sample else ''}<div class=line></div>
<div class=txt>{T['texto']}</div>
<div class=mods>{MODH}</div>
<div class=seal><i class="fa fa-trophy"></i></div>
<div class=foot><div class=c>{'<span class=ph>' + T['fecha_muestra'] + '</span>' if sample else '&nbsp;'}<div>{T['fecha']}</div></div><div class=c>{'<span class=ph>AbC123xYz9</span>' if sample else '&nbsp;'}<div>{T['codigo']}</div></div></div>
<div class=nota>{T['nota']}</div>
</div></body></html>'''

    OUTB = os.path.join(OUT, "insignias")
    shutil.rmtree(OUTB, ignore_errors=True); shutil.rmtree(os.path.join(OUT, "certificado"), ignore_errors=True)
    os.makedirs(OUTB)
    tmp = "/tmp/badges_html_curso"; shutil.rmtree(tmp, ignore_errors=True); os.makedirs(tmp)
    jobs = []
    for fn, tag, name, icon in CFG["insignias"]:
        p = f"{tmp}/{fn}.html"; open(p, "w").write(badge(tag, name, icon, tag == curso_tag))
        jobs.append((p, os.path.join(OUTB, fn + ".png"), 512, 512, True))
    js = "const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();for(const [f,o,w,h,t] of %s){const p=await b.newPage({viewport:{width:w,height:h}});await p.goto('file://'+f);await p.waitForTimeout(1200);await p.screenshot({path:o,omitBackground:t});await p.close();}await b.close();})();" % json.dumps(jobs)
    open(f"{tmp}/r.js", "w").write(js)
    subprocess.run(["node", f"{tmp}/r.js"], check=True, env={**os.environ, "NODE_PATH": subprocess.check_output(["npm", "root", "-g"]).decode().strip()})
    print(len(CFG["insignias"]), "insignias")


# ---------------------------------------------------------------------------
# Nombres que no se usan para personajes (decisión de Desarrolla Talento). Lugares como Los Ángeles o Santa Ana sí se permiten.
NOMBRES_PROHIBIDOS = r"(?<![\wÁÉÍÓÚáéíóúñÑ])(?<!Los )(?<!Santa )(Jorge|Jos[eé]|[ÁA]ngeles|David|Luis|Ana|Jonathan|Paola|Ernesto|Marisa|Tomás|Tomas(?! [a-záéíóúñ])|Leonardo|Esther|Liliana|Alberto)(?![\wáéíóúñ])(?! Potos)"


def paso_verificar():
    """Revisa estructura, conteos, balance de respuestas y largos."""
    CASOS = casos()
    tot, probs, largo_h5p, largo_q, pos = 0, [], 0, 0, {"a": 0, "b": 0, "c": 0}
    corto_h5p = 0
    nq = 0
    for mod in MODS:
        for code, title, les in lecciones(mod):
            tot += 1
            for sec in ["== esencial", "== profundiza", "== practica", "== recursos", "== palabras", "== fuentes", "--- casos", "--- errores", "--- quiz", "--- ponlo", "--- plan", "--- comprueba", "--- recuerda"]:
                if sec not in les: probs.append(f"{code}: falta {sec}")
            for nom in re.findall(NOMBRES_PROHIBIDOS, les): probs.append(f"{code}: nombre prohibido «{nom}»")
            if not EN and re.search(r"\b[Gg]ratis\b", les): probs.append(f"{code}: dice «gratis» (usar «sin costo»)")
            if not EN and re.search(r"(?m)^objetivo: (Saber|Conocer|Entender) ", les): probs.append(f"{code}: objetivo con verbo no observable")
            ncas = len(re.findall(r"(?m)^### ", les))
            if ncas != 3: probs.append(f"{code}: {ncas} casos")
            if code not in CASOS: probs.append(f"{code}: sin CASOS"); continue
            if len(CASOS[code]) != 3: probs.append(f"{code}: CASOS con {len(CASOS[code])}")
            for t in CASOS[code]:
                if len(t) != 3: probs.append(f"{code}: tupla de {len(t)}")
                else:
                    if len(t[0]) > max(len(t[1]), len(t[2])): largo_h5p += 1
                    if len(t[0]) < min(len(t[1]), len(t[2])): corto_h5p += 1
            q = re.search(r"--- quiz\n(.*?)\n(?:respuestas|answers):\s*(.*?)\n", les, re.S)
            if not q: probs.append(f"{code}: quiz sin respuestas"); continue
            ans = dict(re.findall(r"(\d+)-([a-c]):", q.group(2)))
            for k, line in re.findall(r"(?m)^(\d+)\.\s+(.*)$", q.group(1)):
                parts = re.split(r"\s+(?=[a-c]\)\s)", line)
                opts = {o[0]: re.sub(r"\s*·\s*$", "", o)[3:] for o in parts[1:]}
                if len(opts) != 3 or k not in ans: probs.append(f"{code} P{k}: formato"); continue
                nq += 1; pos[ans[k]] += 1
                if len(opts[ans[k]]) > max(len(v) for x, v in opts.items() if x != ans[k]): largo_q += 1
    extra = set(CASOS) - {c for m in MODS for c, _, _ in lecciones(m)}
    if extra: probs.append(f"CASOS sin lección: {sorted(extra)}")
    print(f"{tot} lecciones · {nq} preguntas · posiciones {pos} · correcta más larga: H5P {largo_h5p}/{tot*3}, quiz {largo_q}/{nq} · correcta más corta en H5P: {corto_h5p}/{tot*3}")
    print("problemas:", probs or "ninguno")
    import verificacion as VER
    viejos = VER.vencidos(D)
    if viejos: print(f"AVISO datos por revisar (más de {VER.MESES_VIGENCIA} meses o sin fecha): {len(viejos)} · " + ", ".join(sorted({c for c, *_ in viejos})))
    return probs


# ---------------------------------------------------------------------------
def nombre_insignia(nom):
    """Nombre único en la plataforma: insignia · curso."""
    return f"{nom} · {CFG['categoria']}"


def paso_constancia():
    """Datos para la plantilla estándar de la plataforma: título, línea y 5 temas de 25 caracteres o menos."""
    T = CFG["constancia"]; temas = T["mods"]
    assert len(temas) == 5 and all(len(x) <= 25 for x in temas), temas
    linea = (f"for completing the financial well-being program {CFG['titulo']}" if EN else
             f"por concluir el programa de bienestar financiero {CFG['titulo']}")
    d = os.path.join(OUT, "constancia"); os.makedirs(d, exist_ok=True)
    L = [("# Certificate: data for the standard template" if EN else "# Constancia: datos para la plantilla estándar"), "",
         ("Use the platform's standard template, with no background image. Only these data change:" if EN else
          "Usa la plantilla estándar de la plataforma, sin imagen de fondo. Solo cambian estos datos:"), "",
         "| " + ("Field" if EN else "Campo") + " | " + ("Text" if EN else "Texto") + " |", "|---|---|",
         f"| {'Course title' if EN else 'Título del curso'} | {CFG['titulo']} |",
         f"| {'Line' if EN else 'Línea'} | {linea} |"] + [f"| {'Topic' if EN else 'Tema'} {i} | {t} |" for i, t in enumerate(temas, 1)]
    open(os.path.join(d, "certificate.md" if EN else "constancia.md"), "w").write("\n".join(L) + "\n")
    print("constancia:", linea, "·", " / ".join(temas))


def paso_encuesta():
    import encuesta
    v = CFG.get("encuesta", "us_en" if EN else "mx")
    r = encuesta.generar(os.path.join(OUT, "encuesta"), v, CFG.get("negocio", False), CFG["titulo"])
    print("encuestas (inicio, final, seguimiento):", r)


def paso_catalogo():
    K = CFG["catalogo"]; nl = sum(len(lecciones(m)) for m in MODS); nm = len(MODS)
    assert len(K["descripcion"]) == 2
    if EN:
        L = ["# Catalog card", "", "| Field | Text |", "|---|---|", f"| Course | {CFG['titulo']} |",
             f"| Description | {K['descripcion'][0]}<br>{K['descripcion'][1]} |", f"| Who it's for | {K['para_quien']} |",
             f"| Languages | {K['idiomas']} |", f"| Modules and lessons | {nm} modules · {nl} lessons |"]
    else:
        L = ["# Tarjeta de catálogo", "", "| Campo | Texto |", "|---|---|", f"| Curso | {CFG['titulo']} |",
             f"| Descripción | {K['descripcion'][0]}<br>{K['descripcion'][1]} |", f"| Para quién es | {K['para_quien']} |",
             f"| Idiomas | {K['idiomas']} |", f"| Módulos y lecciones | {nm} módulos · {nl} lecciones |"]
    open(os.path.join(OUT, "catalog_card.md" if EN else "tarjeta_catalogo.md"), "w").write("\n".join(L) + "\n")
    print("tarjeta de catálogo:", nm, "módulos ·", nl, "lecciones")



def paso_ocde():
    """Mapa de competencias OCDE: cada tema del marco con sus competencias y las lecciones que lo trabajan."""
    O = CFG.get("ocde")
    if not O: return
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "ocde"))
    import mapa as MP
    les, res = MP.mapa(LEC, O["marcos"])
    extra = O.get("extra", {})
    tit = {l["codigo"]: l["titulo"] for l in les}
    DIM = {"C": "Conocimiento", "H": "Conducta", "A": "Actitud"}
    L = [f"# Mapa de competencias OCDE · {CFG['titulo']}", "",
         "Cruce de todas las competencias de los marcos de la OCDE aplicables con las lecciones del curso. Paráfrasis en español de los marcos: "
         + ", ".join(sorted({r['marco'] for r in res})) + ".", "",
         "| Marco | Tema | Competencias | Lecciones |", "|---|---|---|---|"]
    cub = 0
    for r in res:
        lecs = list(dict.fromkeys(extra.get(r["id"], []) + r["lecciones"]))[:6]
        r["lecs"] = lecs; cub += bool(lecs)
        L.append(f"| {r['marco']} | {r['id']} {r['tema']} | {len(r['competencias'])} | {', '.join(lecs) or 'Pendiente'} |")
    L += ["", f"Temas cubiertos: {cub} de {len(res)}.", ""]
    for r in res:
        L += [f"## {r['id']} · {r['tema']}", "", "**Lecciones:** " + ("; ".join(f"{c} {tit.get(c, '')}" for c in r["lecs"]) or "pendiente"), ""]
        for d in "CHA":
            cs = [t for dd, t in r["competencias"] if dd == d]
            if cs: L += [f"*{DIM[d]}*", ""] + [f"- {t}" for t in cs] + [""]
    os.makedirs(os.path.join(D, "manual"), exist_ok=True)
    open(os.path.join(D, "manual", "mapa_ocde.md"), "w").write("\n".join(L) + "\n")
    print("mapa OCDE:", cub, "de", len(res), "temas cubiertos")


def paso_instalacion():
    import instalacion_en, instalacion_es
    (instalacion_en if EN else instalacion_es).generar(D, CFG, lecciones)


def paso_bienvenida():
    import bienvenida; print(", ".join(bienvenida.generar(D, CFG, OUT)))


def paso_whatsapp():
    import extras; extras.guiones(D, CFG, lecciones, EN); print("guiones de WhatsApp y audio")


def paso_kit():
    import extras; extras.kit(D, CFG, lecciones, EN); print("kit para facilitadores")


def paso_herramientas():
    import extras; n, h = extras.hojas(D, CFG, EN); print("herramientas:", n, h)


PASOS = {"bienvenida": paso_bienvenida, "whatsapp": paso_whatsapp, "kit": paso_kit, "herramientas": paso_herramientas, "instalacion": paso_instalacion, "glosario": paso_glosario, "libros": paso_libros, "h5p": paso_h5p, "banco": paso_banco, "apoyo": paso_apoyo, "fondo": paso_fondo, "programas": paso_programas, "comunidad": paso_comunidad,
         "insignias": paso_insignias, "verificar": paso_verificar, "constancia": paso_constancia, "encuesta": paso_encuesta, "catalogo": paso_catalogo, "ocde": paso_ocde}

if __name__ == "__main__":
    pedidos = sys.argv[2:] or ["todo"]
    if "todo" in pedidos: pedidos = [p for p in pedidos if p != "todo" and p != "carpeta"] + ["verificar", "instalacion", "glosario", "libros", "h5p", "banco", "apoyo", "fondo", "programas", "bienvenida", "comunidad", "insignias", "constancia", "encuesta", "catalogo", "ocde", "whatsapp", "kit", "herramientas"] + (["carpeta"] if "carpeta" in pedidos else [])
    for p in pedidos:
        if p == "carpeta":
            import carpeta; carpeta.construir(D, CFG)
        else:
            PASOS[p]()
