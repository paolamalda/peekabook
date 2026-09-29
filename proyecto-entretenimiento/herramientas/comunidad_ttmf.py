# Tu Talento: libro "Materiales de apoyo" con el diseño v3, un capítulo por archivo de manual/apoyo.
# Las claves y respuestas quedan ocultas en <details>. Uso: python3 herramientas/apoyo_v3.py
import re, os, glob, html, zipfile, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "proyecto-inclusion-financiera", "herramientas"))
from leccion_ux2 import CSS, C, md, page, terms
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EN = False
SRC, OUT = os.path.join(BASE, "comunidad/libro"), os.path.join(BASE, "comunidad/moodle")
ICON = {"01": "fa-users", "02": "fa-shield", "03": "fa-comments", "04": "fa-calendar", "05": "fa-video-camera", "06": "fa-handshake-o"}
LEAD = {"01": "Qué es la comunidad, qué encuentras y cómo empezar.",
        "02": "Las reglas que protegen tus datos y los de todas las personas.",
        "03": "Una plantilla para preguntar y recibir una buena respuesta.",
        "04": "Las fechas del año que importan a quien trabaja por su cuenta en el medio.",
        "05": "La sesión mensual de dudas, la encuesta de temas y los retos del mes.",
        "06": "Qué es educación y qué es una oferta comercial, con total transparencia."}
if EN:
    LEAD = {"01": "Start here: how the course works, your 5- or 10-minute paths, badges and certificate.",
            "02": "Five cases that bring together what you learned in each module. Solve them before opening the key.",
            "03": "Short exercises to practice the course calculations. The answers are at the end.",
            "04": "The course words explained in plain language, with their name in Spanish.",
            "05": "Where to get free or low-cost help, and answers to the most common questions.",
            "06": "The sources we used in the course, so you can check them."}
L = dict(mat="Support materials", key="See the key", ans="See the answers", faq="Frequently asked questions", hdr="Answers",
         keyre=r"(Key|Answers)", taskre=r"Additional task") if EN else \
    dict(mat="Guía de la comunidad", key="Ver la clave", ans="Ver las respuestas", faq="Preguntas frecuentes", hdr="Respuestas",
         keyre=r"(Clave|Respuestas)", taskre=r"Tarea adicional")
def hide(sec_md, label):
    m = re.search(r"(?m)^\*\*" + L["keyre"] + r"\.?\*\*", sec_md)
    if not m: return md(sec_md)
    before, rest = sec_md[:m.start()], sec_md[m.start():]
    t = re.search(r"(?m)^\*\*" + L["taskre"] + r"\.\*\*", rest)
    tail = rest[t.start():] if t else ""
    rest = rest[:t.start()] if t else rest
    return md(before) + f'<details><summary>{label}</summary><div class="a">{md(rest)}</div></details>' + md(tail)
def faq(sec_md):
    items = re.findall(r"(?m)^\*\*(¿?[^*]+\?)\*\*\s*(.+)$", sec_md)
    return "".join(f'<details><summary>{html.escape(q)}</summary><div class="a">{md(a)}</div></details>' for q, a in items)
def chapter(num, text):
    text = text.replace("[[TOC]]", "")
    tops = re.split(r"(?m)^# ", text)[1:]
    title = tops[0].split("\n", 1)[0].strip()
    body = f'<div class="hero"><span class="code"><i class="fa {ICON[num]}"></i> {L["mat"]}</span><h3>{title}</h3><p class="obj">{LEAD[num]}</p></div>'
    for ti, top in enumerate(tops):
        h, rest = (top.split("\n", 1) + [""])[:2]
        if ti: body += f'<div class="pagehead mt-4"><h3>{h.strip()}</h3></div>'
        secs = re.split(r"(?m)^## ", rest)
        intro = secs[0].strip().strip("-").strip()
        if intro:
            body += faq(intro) if h.strip() == L["faq"] else f'<div class="card2">{md(intro)}</div>'
        for s in secs[1:]:
            sh, sb = (s.split("\n", 1) + [""])[:2]
            sb = sb.strip().rstrip("-").strip()
            if sh.strip() == L["hdr"]:
                inner = f'<details><summary>{L["ans"]}</summary><div class="a">{md(sb)}</div></details>'
            elif num == "02":
                inner = hide(sb, L["key"])
            else:
                inner = md(sb)
            body += f'<div class="card2"><h4>{terms(sh.strip())}</h4>{inner}</div>'
    return title, f'{CSS}<div class="tdtf">{body}</div>'
os.makedirs(OUT, exist_ok=True)
files = []
for p in sorted(glob.glob(os.path.join(SRC, "*.md"))):
    num = os.path.basename(p)[:2]
    title, h = chapter(num, open(p, encoding="utf-8").read())
    fn = f"{num}_comunidad.html"
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(page(title, h))
    files.append(fn)
z = os.path.join(OUT, "Comunidad_libro_Moodle.zip")
with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
    for fn in files: zf.write(os.path.join(OUT, fn), fn)
print(len(files), "capítulos ·", z)

import build_v3 as B
B.preview([(fn, re.sub(r"<[^>]+>", "", open(os.path.join(OUT, fn)).read().split("<title>")[1].split("</title>")[0]), open(os.path.join(OUT, fn)).read().split("<body>")[1].split("</body>")[0]) for fn in files], os.path.join(OUT, "vista_previa"))
