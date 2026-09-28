# Genera zips de capítulos HTML para "Importar capítulo" del Libro de Moodle (un zip por módulo e idioma).
import re, os, zipfile, html, markdown
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "moodle", "libros")
MODS = {"M1": ["M1a.md","M1b.md"], "M2": ["M2a.md","M2b.md"], "M3": ["M3.md"], "M4": ["M4a.md","M4b.md"], "M5": ["M5a.md","M5b.md"]}
EXTRA = ["00-inicio.md","90-casos.md","91-practicas.md","92-glosario.md","93-ayuda.md","94-referencias.md"]
def to_html(title, md):
    md = re.sub(r"(?<![(<])(https?://[^\s)]+?)([.,;]?)(?=\s|$)", r"<\1>\2", md)
    md = re.sub(r"(?m)^(?!\s*([-*]|\d+\.)\s)(.+)\n(?=\s*([-*]|\d+\.)\s)", r"\2\n\n", md)
    md = re.sub(r"(?m)^  (?=[-*] )", "    ", md)
    body = markdown.markdown(md, extensions=["tables"])
    body = body.replace("<table>", '<table class="table table-bordered">')
    return f'<!DOCTYPE html>\n<html><head><meta charset="utf-8"><title>{html.escape(title)}</title></head><body>\n{body}\n</body></html>\n'
def write_zip(path, chapters):
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        for i, (t, md) in enumerate(chapters, 1):
            z.writestr(f"{i:02d}.html", to_html(t, md))
resumen = []
for lang in ("es", "en"):
    os.makedirs(os.path.join(OUT, lang), exist_ok=True)
    for mod, files in MODS.items():
        text = "\n".join(open(os.path.join(BASE, "manual", lang, f)).read() for f in files)
        parts = re.split(r"(?m)^## (?=M\d U\d\d\.)", text)
        intro = parts[0]
        modtitle = re.search(r"(?m)^# (.+)$", intro).group(1)
        chapters = []
        for p in parts[1:]:
            title, rest = p.split("\n", 1)
            rest = rest.replace("\n---\n", "\n")
            chapters.append((title.strip(), rest))
        write_zip(os.path.join(OUT, lang, f"{mod}.zip"), chapters)
        summ = re.sub(r"(?m)^# .+$|^---$", "", intro).strip()
        open(os.path.join(OUT, lang, f"{mod}_resumen.html"), "w").write(markdown.markdown(summ))
        resumen.append((lang, mod, modtitle, len(chapters)))
    # Materiales de apoyo: cada archivo es un capítulo
    ch = []
    for f in EXTRA:
        t = open(os.path.join(BASE, "manual", lang, f)).read().replace("\n---\n", "\n")
        title = re.search(r"(?m)^# (.+)$", t).group(1)
        ch.append((title, re.sub(r"(?m)^# (.+)$", r"## \1", t, count=0)))
    write_zip(os.path.join(OUT, lang, "Apoyo.zip"), ch)
    resumen.append((lang, "Apoyo", "materiales", len(ch)))
for r in resumen: print(*r)
