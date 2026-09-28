# Documento Word con todo el contenido v3: módulos, libro de apoyo, actividades H5P, banco, pendientes y prompt.
# Uso: python3 herramientas/contenido_completo_v3.py  (antes: build_v3.py M1..M5 y quiz_gift_v3.py)
import re, os, glob, json, subprocess, sys
sys.path.insert(0, os.path.dirname(__file__))
from datos_casos import CASOS
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S = "/tmp/claude-0/-home-user-peekabook/2b8c84d1-874b-559e-a5dd-06af4ddd1637/scratchpad"
def shift(md, n=1):  # baja un nivel los títulos para que quepan bajo una parte
    return re.sub(r"(?m)^(#{1,5}) ", lambda m: "#" * min(6, len(m.group(1)) + n) + " ", md)
P = ["# Tu Dinero, Tu Familia, Tu Futuro: contenido completo (versión 3.2)",
     "Programa gratuito de educación financiera para personas migrantes · Desarrolla Talento · Piloto California · 28 de septiembre de 2026.",
     "Este documento reúne todo el contenido del curso en el formato nuevo: las 59 lecciones (Lo esencial, Profundiza y Practica), el libro de apoyo, las 59 actividades H5P, el banco de preguntas, los datos por confirmar y el prompt para escribir o corregir lecciones.",
     "| Parte | Contenido |\n|---|---|\n| 1 | Personajes y reglas de lenguaje |\n| 2 a 6 | Módulos 1 a 5 |\n| 7 | Materiales de apoyo |\n| 8 | Actividades H5P «¿Qué harías?» |\n| 9 | Banco de preguntas |\n| 10 | Datos por confirmar |\n| 11 | Prompt de reescritura |"]
P.append("# Parte 1. Personajes y reglas de lenguaje\n\n" + shift(re.sub(r"(?s)^#[^\n]*\n", "", open(f"{BASE}/manual/personajes.md").read())))
for i, m in enumerate(["M1", "M2", "M3", "M4", "M5"], 2):
    t = open(f"{BASE}/moodle/v3/{m}/{m}_legible.md").read()
    t = re.sub(r"(?m)^# ", f"# Parte {i}. ", t, count=1)
    P.append(t)
P.append("# Parte 7. Materiales de apoyo")
for f in sorted(glob.glob(f"{BASE}/manual/v3/es/apoyo/*.md")):
    P.append(shift(open(f).read()))
P.append("# Parte 8. Actividades H5P «¿Qué harías?»\n\nUna actividad por lección, con los tres casos de la lección. La opción marcada con ✔ es la correcta; en la plataforma las opciones aparecen en orden aleatorio.")
for f in sorted(glob.glob(f"{BASE}/manual/v3/es/M*.md")):
    for les in re.split(r"(?m)^# (?=M\d U\d\d)", open(f).read())[1:]:
        code, title = [x.strip() for x in les.split("\n", 1)[0].split("|", 1)]
        P.append(f"## {code}. {title}")
        cs = re.search(r"--- casos\n(.*?)\n--- ", les, re.S).group(1)
        for c, (ok, d1, d2) in zip(re.split(r"(?m)^### ", cs)[1:], CASOS[code]):
            h, b = c.split("\n", 1)
            ctx = re.sub(r"\{\{([^|}]+)\|[^}]+\}\}", r"\1", " ".join(l for l in b.splitlines() if l.strip() and not l.startswith("? ")))
            q = re.search(r"(?m)^\? (.+?)\s*\|\|", b).group(1)
            P.append(f"**{h.strip()}.** {ctx} **{q}**\n\n- ✔ {ok}\n- {d1}\n- {d2}")
P.append("# Parte 9. Banco de preguntas\n\n177 preguntas para las autoevaluaciones de módulo (formato GIFT en la plataforma). La opción marcada con ✔ es la correcta; debajo va la retroalimentación.")
g = open(f"{BASE}/moodle/v3/banco_preguntas_v3_es.gift.txt").read()
cur = None
for name, stem, body in re.findall(r"::(.*?)::(.*?) \{\n(.*?)\n\}", g, re.S):
    mod = name[:2]
    if mod != cur: P.append(f"## Módulo {mod[1]}"); cur = mod
    un = lambda s: re.sub(r"\\([~=#{}:])", r"\1", s)
    lines, fb = [], ""
    for l in body.splitlines():
        l = l.strip(); ok = l[0] == "="; txt, _, f = l[1:].partition(" #")
        lines.append(("- ✔ " if ok else "- ") + un(txt))
        if ok: fb = un(f)
    P.append(f"**{name}.** {un(stem)}\n\n" + "\n".join(lines) + f"\n\n*{fb}*")
P.append("# Parte 10. Datos por confirmar\n\n## Pendientes de revisión (plan maestro)")
for t in json.load(open(f"{BASE}/entregables/plan-maestro.json"))["todo"]:
    if t["id"] in [f"K{i:02d}" for i in range(6, 14)]:
        P.append(f"- **{t['id']}** ({t['resp']}): {t['tarea']}")
P.append("## Frases marcadas [POR CONFIRMAR] en las lecciones")
for f in sorted(glob.glob(f"{BASE}/manual/v3/es/**/*.md", recursive=True)):
    cur = ""
    for l in open(f):
        m = re.match(r"# (M\d U\d\d)", l)
        if m: cur = m.group(1)
        if "[POR CONFIRMAR]" in l:
            s = re.sub(r"\{\{([^|}]+)\|[^}]+\}\}", r"\1", l.strip().lstrip("-*>| "))
            P.append(f"- **{cur or os.path.basename(f)}:** {s[:300]}")
P.append("# Parte 11. Prompt de reescritura de lecciones\n\n" + shift(re.sub(r"(?s)^#[^\n]*\n", "", open(f"{BASE}/manual/prompt_reescritura_lecciones.md").read())))
md = "\n\n".join(P) + "\n"
out_md = f"{BASE}/entregables/TDTF_Contenido_completo_v3_ES.md"
open(out_md, "w").write(md)
out = f"{BASE}/entregables/TDTF_Contenido_completo_v3_ES.docx"
subprocess.run(["node", "herramientas/md2docx.js", out, "Tu Dinero, Tu Familia, Tu Futuro", "Contenido completo · Versión 3.2 · Septiembre de 2026", out_md],
               cwd=BASE, env=dict(os.environ, NODE_PATH=f"{S}/nodeenv/node_modules"), check=True)
print(out, len(md.split()), "palabras")
