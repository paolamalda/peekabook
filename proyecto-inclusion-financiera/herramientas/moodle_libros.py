# Genera zips de capítulos HTML para "Importar capítulo" del Libro de Moodle (un zip por módulo e idioma).
import re, os, zipfile, html, markdown
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "moodle", "libros")
MODS = {"M1": ["M1a.md","M1b.md"], "M2": ["M2a.md","M2b.md"], "M3": ["M3.md"], "M4": ["M4a.md","M4b.md"], "M5": ["M5a.md","M5b.md"]}
EXTRA = ["00-inicio.md","90-casos.md","91-practicas.md","92-glosario.md","93-ayuda.md","94-referencias.md"]
# Estilos de marca Desarrolla Talento (en línea, para que funcionen sin tocar el tema).
TERM = 'class="tdtf-termino" style="color:#E4007C;font-weight:600;text-decoration:underline dotted #E4007C;cursor:help;border-bottom:0"'
CARD = 'style="background:#E6ECF5;border-left:4px solid #E4007C;border-radius:12px;padding:12px 16px;margin:16px 0"'
PILL = 'style="display:inline-block;background:#E4007C;color:#FFFFFF;border-radius:999px;padding:2px 12px;font-size:.85em;font-weight:600;margin-left:8px"'
def terms(md):
    return re.sub(r"\{\{([^|}]+)\|([^}]+)\}\}", lambda m: f'<abbr {TERM} title="{html.escape(m.group(2), quote=True)}">{m.group(1)}</abbr>', md)
def to_html(title, md):
    md = re.sub(r"(?<![(<\[])(https?://[^\s)]+?)([.,;]?)(?=\s|$)", r"<\1>\2", md)
    md = re.sub(r"(?m)^(?!\s*([-*]|\d+\.)\s)(.+)\n(?=\s*([-*]|\d+\.)\s)", r"\2\n\n", md)
    md = re.sub(r"(?m)^  (?=[-*] )", "    ", md)
    md = terms(md)
    body = markdown.markdown(md, extensions=["tables"])
    body = body.replace("<table>", '<table class="table" style="border:1px solid #E5E8F0;border-collapse:collapse;width:100%">')
    body = body.replace("<th>", '<th style="background:#0A3161;color:#FFFFFF;padding:8px;border:1px solid #E5E8F0">')
    body = body.replace("<td>", '<td style="padding:8px;border:1px solid #E5E8F0">')
    body = body.replace("<blockquote>", f"<blockquote {CARD}>")
    body = re.sub(r"<h3>Versión corta \((.+?)\)</h3>", lambda m: f'<h3>Versión corta <span {PILL}>{m.group(1)}</span></h3>', body)
    body = re.sub(r"<h3>Versión amplia \((.+?)\)</h3>", lambda m: f'<h3 style="border-top:2px solid #E5E8F0;padding-top:16px;margin-top:28px">Versión amplia <span {PILL}>{m.group(1)}</span></h3>', body)
    body = re.sub(r"<h3>(Short version|Extended version) \((.+?)\)</h3>", lambda m: f'<h3>{m.group(1)} <span {PILL}>{m.group(2)}</span></h3>', body)
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
