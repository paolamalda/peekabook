# Genera los entregables de un módulo en el formato nuevo (v3):
#   libro de Moodle (zip), glosario (XML), texto legible (md para Word), vista previa (HTML) y conteo de palabras.
# Uso: python3 herramientas/build_v3.py M1 [M2 ...]
import re, os, sys, html, json, zipfile, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from leccion_ux2 import build, page, parse, blocks

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(BASE, "manual", "v3", "es")
OUT = os.path.join(BASE, "moodle", "v3")
ASSETS = os.path.join(BASE, "manual", "muestras", "vista_previa", "assets")
TITULOS = {"M1": "Módulo 1. Entiende tu dinero y organiza tu economía", "M2": "Módulo 2. Entiende el sistema financiero y planea tus remesas",
           "M3": "Módulo 3. Construye tu crédito y maneja tus deudas", "M4": "Módulo 4. Protege tu dinero, tu identidad y tu familia",
           "M5": "Módulo 5. Construye patrimonio y prepara tu futuro"}

def module_text(mod):
    files = sorted(f for f in os.listdir(SRC) if f.startswith(mod) and f.endswith(".md"))
    return "\n\n".join(open(os.path.join(SRC, f)).read().strip() for f in files)

def words(s):
    # Palabras visibles para el lector: incluye títulos de bloques; excluye definiciones ocultas, iconos y marcas de formato.
    s = re.sub(r"\{\{([^|}]+)\|[^}]+\}\}", r"\1", s)
    s = re.sub(r"https?://\S+|fa-[a-z0-9-]+|\b(paso|pasos|tarjetas|ecuacion|tema|tabla|comprueba|recuerda|casos|errores)\b(?=\s*\||\s*$)", " ", s)
    s = re.sub(r"\|\||[|*=#>?]|---|\b(si|no|igual)\s*$", " ", s, flags=re.M)
    return len([w for w in s.split() if re.search(r"\w", w)])

def conteo(text):
    rows = []
    for b in [b for b in re.split(r"(?m)^# ", text) if b.strip()]:
        code, title, meta, secs = parse(b)
        rows.append((code, words(secs["esencial"]), words(secs["profundiza"])))
    return rows

def legible(text, mod):
    t = re.sub(r"\{\{([^|}]+)\|[^}]+\}\}", r"\1", text)
    out = [f"# {TITULOS[mod]}", ""]
    names = {"esencial": "Lo esencial (5 minutos)", "profundiza": "Profundiza (5 minutos más)", "practica": "Practica",
             "recursos": "Para saber más", "palabras": "Palabras clave", "fuentes": "Fuentes"}
    for les in [b for b in re.split(r"(?m)^# ", t) if b.strip()]:
        head, rest = les.split("\n", 1)
        code, title = [x.strip() for x in head.split("|", 1)]
        out += [f"## {code}. {title}", ""]
        for k, v in re.findall(r"(?m)^(objetivo|gancho):\s*(.+)$", rest):
            out += [f"**{'Lo que lograrás' if k == 'objetivo' else 'Para empezar'}:** {v}", ""]
        for sec in re.split(r"(?m)^== ", rest)[1:]:
            name, body = sec.split("\n", 1)
            out += [f"### {names.get(name.strip(), name.strip())}", ""]
            if name.strip() in ("recursos",):
                out += [l.replace(" | Qué buscar:", " — **Qué buscar:**") for l in body.strip().splitlines()] + [""]
                continue
            if name.strip() in ("palabras", "fuentes"):
                out += [body.strip(), ""]
                continue
            for b in re.split(r"(?m)^--- ", body):
                if not b.strip():
                    continue
                hd, ct = (b.split("\n", 1) + [""])[:2]
                parts = [p.strip() for p in hd.split("|")]
                kind = parts[0]
                ttl = {"comprueba": "Comprueba lo que entendiste", "recuerda": "Para recordar", "casos": "Casos", "errores": "Errores frecuentes",
                       "actividad": "Actividad interactiva", "quiz": "Quiz", "ponlo": "Ponlo en práctica", "plan": "A tu plan"}.get(kind, parts[2] if len(parts) > 2 else "")
                out += [f"#### {ttl}", ""]
                if kind == "tarjetas":
                    out += ["| Tipo | Descripción | Qué significa para ti |", "|---|---|---|"]
                    out += [f"| {c[1]} | {c[2]} | {c[3]} |" for c in ([x.strip() for x in l[2:].split("|")] for l in ct.splitlines() if l.startswith("* "))]
                    resto = [l for l in ct.splitlines() if l.strip() and not l.startswith("* ")]
                    if resto: out += [""] + resto
                elif kind == "ecuacion":
                    for l in ct.splitlines():
                        m = re.match(r"^([=\-+×÷]) (.+?)\s*\|\s*(.+)$", l)
                        out.append(f"- {m.group(3)}: **{m.group(2)}**" if m else l)
                elif kind == "comprueba":
                    for l in ct.splitlines():
                        if "||" in l:
                            q, a = l.split("||")
                            out += [q.strip(), f"*Respuesta:* {a.strip()}", ""]
                elif kind == "casos":
                    for l in ct.splitlines():
                        if l.startswith("### "):
                            out += ["", f"**{l[4:]}**", ""]
                        elif l.startswith("? "):
                            q, a = l[2:].split("||")
                            out.append(f"- *{q.strip()}* {a.strip()}")
                        else:
                            out.append(l)
                elif kind == "errores":
                    out += ["| Error | Qué pasa | Qué hacer |", "|---|---|---|"]
                    out += [f"| {' | '.join(x.strip() for x in l[2:].split('|'))} |" for l in ct.splitlines() if l.startswith("* ")]
                else:
                    out.append(ct.replace("respuestas:", "**Respuestas:**").replace("respuesta:", "**Respuesta:**"))
                out.append("")
        out += ["---", ""]
    return "\n".join(out).replace("****", "**")

def glosario(text, name):
    terms = {}
    for k, v in re.findall(r"\{\{([^|}]+)\|([^}]+)\}\}", text):
        terms.setdefault(k.strip()[0].upper() + k.strip()[1:], v.strip())
    x = ['<?xml version="1.0" encoding="UTF-8"?>', f'<GLOSSARY><INFO><NAME>{html.escape(name)}</NAME><INTRO>Significado de los términos del curso, en palabras sencillas.</INTRO><INTROFORMAT>1</INTROFORMAT><ALLOWDUPLICATEDENTRIES>0</ALLOWDUPLICATEDENTRIES><DISPLAYFORMAT>dictionary</DISPLAYFORMAT><SHOWSPECIAL>1</SHOWSPECIAL><SHOWALPHABET>1</SHOWALPHABET><SHOWALL>1</SHOWALL><ALLOWCOMMENTS>0</ALLOWCOMMENTS><USEDYNALINK>0</USEDYNALINK><DEFAULTAPPROVAL>1</DEFAULTAPPROVAL><GLOBALGLOSSARY>0</GLOBALGLOSSARY><ENTBYPAGE>20</ENTBYPAGE><ENTRIES>']
    for k in sorted(terms, key=str.lower):
        x.append(f'<ENTRY><CONCEPT>{html.escape(k)}</CONCEPT><DEFINITION>{html.escape(terms[k])}</DEFINITION><FORMAT>1</FORMAT><USEDYNALINK>0</USEDYNALINK><CASESENSITIVE>0</CASESENSITIVE><FULLMATCH>1</FULLMATCH><TEACHERENTRY>1</TEACHERENTRY></ENTRY>')
    x.append("</ENTRIES></INFO></GLOSSARY>")
    return "\n".join(x), len(terms)

def preview(pages, folder):
    os.makedirs(folder, exist_ok=True)
    if os.path.isdir(ASSETS):
        shutil.copytree(ASSETS, os.path.join(folder, "assets"), dirs_exist_ok=True)
    toc = "".join(f'<a href="{fn}" style="display:block;padding:3px 0 3px {"16px" if "_sub" in fn else "0"};color:#0A3161;{"font-size:.9rem" if "_sub" in fn else "font-weight:700;margin-top:10px"}">{t}</a>' for fn, t, b in pages)
    for fn, t, b in pages:
        open(os.path.join(folder, fn), "w").write(
            f'<!DOCTYPE html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(t)}</title>'
            f'<link rel="stylesheet" href="assets/bootstrap.min.css"><link rel="stylesheet" href="assets/fa.css">'
            f'<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800&family=Figtree:wght@400;500;600;700&display=swap" rel="stylesheet">'
            f'<style>body{{background:#F5F7FB;font-family:Figtree,system-ui,sans-serif}}</style></head><body><div class="container-fluid py-3"><div class="row">'
            f'<div class="col-lg-3 d-none d-lg-block"><div class="card p-3" style="border-radius:16px;max-height:95vh;overflow:auto;position:sticky;top:10px"><small style="color:#5A6478">VISTA PREVIA · así se verá en el Libro de Moodle</small>{toc}</div></div>'
            f'<div class="col-lg-9"><h2 class="h4 mb-3" style="font-weight:800;color:#061F40">{html.escape(t)}</h2>{b}</div></div></div></body></html>')
    open(os.path.join(folder, "ABRIR_AQUI.html"), "w").write(f'<meta http-equiv="refresh" content="0; url={pages[0][0]}">')

EN = "--en" in sys.argv
if EN:  # versión en inglés: fuente manual/v3/en, salida moodle/v3/en, interfaz traducida
    from i18n_en import tr, TITLES
    SRC, OUT = os.path.join(BASE, "manual", "v3", "en"), os.path.join(BASE, "moodle", "v3", "en")
    TITULOS.update(TITLES)
else:
    tr = lambda s: s

if __name__ == "__main__":
    for mod in [a for a in sys.argv[1:] if not a.startswith("--")]:
        text = module_text(mod)
        pages = [(fn, tr(t), tr(b)) for fn, t, b in build(text)]
        d = os.path.join(OUT, mod)
        os.makedirs(d, exist_ok=True)
        with zipfile.ZipFile(os.path.join(d, f"{mod}_libro_Moodle.zip"), "w", zipfile.ZIP_DEFLATED) as z:
            for fn, t, b in pages:
                z.writestr(fn, page(t, b))
        xml, n = glosario(text, f"Palabras clave · {mod}")
        xml = tr(xml)
        open(os.path.join(d, f"{mod}_glosario_Moodle.xml"), "w").write(xml)
        open(os.path.join(d, f"{mod}_legible.md"), "w").write(tr(legible(text, mod)))
        preview(pages, os.path.join(d, "vista_previa"))
        if EN:
            for f in os.listdir(os.path.join(d, "vista_previa")):
                if f.endswith(".html"):
                    q = os.path.join(d, "vista_previa", f); s = open(q).read(); open(q, "w").write(tr(s))
        c = conteo(text)
        json.dump({"lecciones": len(c), "paginas": len(pages), "terminos": n, "conteo": c}, open(os.path.join(d, "conteo.json"), "w"), ensure_ascii=False)
        print(mod, "lecciones", len(c), "páginas", len(pages), "términos", n)
        for code, e, p in c:
            print(f"  {code}: esencial {e} · profundiza {p} · total {e+p}")
