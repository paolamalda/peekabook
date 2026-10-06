# Genera cada lección como 4 páginas del Libro de Moodle (1 capítulo + 3 subcapítulos):
#   Portada (elige ruta) · Lo esencial (5 min) · Profundiza (+5 min) · Practica.
# Pensado para Moodle 3.10 + Boost: el Libro muestra el HTML sin limpiar (noclean), respeta <style> en el cuerpo,
# convierte enlaces entre archivos del zip en enlaces a capítulos y trata "*_sub.html" como subcapítulo.
# Las respuestas usan <details> (sin JavaScript), así que también funcionan en la app de Moodle.
import re, html, markdown

C = dict(azul="#0A3161", azul2="#061F40", rosa="#E4007C", rosa2="#FF4FA8", tinte="#E6ECF5", niebla="#F5F7FB",
         borde="#E5E8F0", texto="#0B1220", gris="#5A6478", ambar="#A35200", ambar_bg="#FFF6EC")

CSS = """<style>
.tdtf{max-width:880px;margin:0 auto;color:%(texto)s;font-size:1.02rem;line-height:1.6}
.tdtf p{margin:0 0 .8rem}
.tdtf h3,.tdtf h4{font-family:"Bricolage Grotesque","Figtree",sans-serif;font-weight:800;color:%(azul2)s;letter-spacing:-.02em}
.tdtf .ruta{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 18px;padding:0;list-style:none}
.tdtf .ruta a,.tdtf .ruta span{display:inline-flex;align-items:center;gap:6px;padding:6px 14px;border-radius:999px;border:2px solid %(borde)s;color:%(gris)s;font-weight:600;font-size:.88rem;text-decoration:none;background:#fff}
.tdtf .ruta .on{background:%(azul)s;border-color:%(azul)s;color:#fff}
.tdtf .ruta a:hover{border-color:%(rosa)s;color:%(rosa)s}
.tdtf .hero{background:%(azul)s;color:#fff;border-radius:20px;padding:24px 24px 20px;margin-bottom:18px;position:relative;overflow:hidden}
.tdtf .hero:after{content:"";position:absolute;right:-40px;top:-40px;width:180px;height:180px;border-radius:50%%;background:rgba(255,79,168,.18)}
.tdtf .hero .code{display:inline-block;background:%(rosa)s;color:#fff;border-radius:999px;padding:2px 12px;font-weight:700;font-size:.8rem;letter-spacing:.04em}
.tdtf .hero h3{color:#fff;font-size:1.6rem;margin:10px 0 8px}
.tdtf .hero .obj{font-size:1.08rem;opacity:.95;margin:0}
.tdtf .hero .lbl{color:#FF7ABD;font-weight:700;font-size:.78rem;text-transform:uppercase;letter-spacing:.06em}
.tdtf .card2{background:#fff;border:1px solid %(borde)s;border-radius:16px;padding:18px 20px;margin-bottom:14px}
.tdtf .gancho{display:flex;gap:14px;align-items:flex-start;background:%(tinte)s;border-radius:16px;padding:18px 20px;margin-bottom:18px}
.tdtf .avatar{flex:0 0 48px;height:48px;border-radius:50%%;background:%(rosa)s;color:#fff;display:flex;align-items:center;justify-content:center;font-size:1.3rem}
.tdtf .rutas{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px;margin:8px 0 18px}
.tdtf .rutabox{display:block;background:#fff;border:2px solid %(azul)s;border-radius:18px;padding:18px 20px;color:%(texto)s;text-decoration:none;transition:.15s}
.tdtf .rutabox:hover{border-color:%(rosa)s;box-shadow:0 0 0 4px rgba(228,0,124,.15);text-decoration:none;color:%(texto)s}
.tdtf .rutabox.full{background:%(azul)s;color:#fff}
.tdtf .rutabox.full:hover{color:#fff}
.tdtf .rutabox .t{font-family:"Bricolage Grotesque","Figtree",sans-serif;font-weight:800;font-size:1.25rem;display:flex;align-items:center;gap:8px}
.tdtf .pill{display:inline-block;background:%(rosa)s;color:#fff;border-radius:999px;padding:1px 10px;font-size:.8rem;font-weight:700;vertical-align:middle}
.tdtf .rutabox ol{margin:10px 0 12px 1.1rem;padding:0}
.tdtf .rutabox .go{font-weight:700}
.tdtf .aprende li{margin-bottom:4px}
.tdtf .pagehead{display:flex;align-items:center;gap:10px;margin:4px 0 16px}
.tdtf .pagehead h3{margin:0;font-size:1.5rem}
.tdtf .timeline{position:relative;margin-left:22px;padding-left:28px;border-left:3px solid %(tinte)s}
.tdtf .step{position:relative;margin-bottom:18px}
.tdtf .step .num{position:absolute;left:-52px;top:14px;width:44px;height:44px;border-radius:50%%;background:%(azul)s;color:#fff;display:flex;align-items:center;justify-content:center;font-size:1.15rem;box-shadow:0 0 0 5px #fff}
.tdtf .step h4{font-size:1.15rem;margin:0 0 10px}
.tdtf .tiles{display:grid;grid-template-columns:repeat(auto-fit,minmax(165px,1fr));gap:12px}
.tdtf .st.si abbr.term,.tdtf .st.no abbr.term,.tdtf .recuerda abbr.term,.tdtf .hero abbr.term{color:#fff;text-decoration-color:#fff}
.tdtf .tile{border:1px solid %(borde)s;border-radius:14px;padding:14px;background:%(niebla)s}
.tdtf .tile .ic{width:40px;height:40px;border-radius:12px;background:%(azul)s;color:#fff;display:flex;align-items:center;justify-content:center;margin-bottom:8px}
.tdtf .tile .nm{font-weight:700;margin-bottom:4px}
.tdtf .tile .ex{color:%(gris)s;font-size:.93rem;margin-bottom:8px}
.tdtf .tile .st{font-size:.9rem;font-weight:600;border-radius:10px;padding:6px 10px}
.tdtf .st.si{background:%(azul)s;color:#fff}.tdtf .st.no{background:%(rosa)s;color:#fff}.tdtf .st.igual{background:%(tinte)s;color:%(azul2)s}
.tdtf .eq{display:flex;flex-wrap:wrap;align-items:stretch;gap:8px;margin:12px 0}
.tdtf .eq .n{flex:1 1 120px;text-align:center;border-radius:14px;padding:12px 8px;background:%(tinte)s}
.tdtf .eq .n b{display:block;font-family:"Bricolage Grotesque","Figtree",sans-serif;font-size:1.9rem;color:%(azul2)s;line-height:1.1}
.tdtf .eq .n span{font-size:.85rem;color:%(gris)s}
.tdtf .eq .n.res{background:%(azul)s}.tdtf .eq .n.res b,.tdtf .eq .n.res span{color:#fff}
.tdtf .eq .op{display:flex;align-items:center;font-size:1.6rem;font-weight:800;color:%(rosa)s}
.tdtf .box{border-radius:14px;padding:12px 16px;margin:12px 0;border:1px solid %(borde)s;border-left:5px solid %(rosa)s;background:%(tinte)s}
.tdtf .box p:last-child{margin:0}
.tdtf .box.dato{background:#fff;border-left-color:%(azul)s}
.tdtf .box.verifica{background:%(ambar_bg)s;border-left-color:%(ambar)s}
.tdtf .box .h{font-weight:700;color:%(rosa)s}
.tdtf .box.dato .h{color:%(azul)s}.tdtf .box.verifica .h{color:%(ambar)s}
.tdtf ol.check{list-style:none;counter-reset:c;padding:0;margin:0}
.tdtf ol.check li{counter-increment:c;position:relative;padding:10px 12px 10px 52px;margin-bottom:8px;background:%(niebla)s;border-radius:12px}
.tdtf ol.check li:before{content:counter(c);position:absolute;left:12px;top:9px;width:28px;height:28px;border-radius:50%%;background:%(rosa)s;color:#fff;font-weight:700;display:flex;align-items:center;justify-content:center}
.tdtf details{border:1px solid %(borde)s;border-radius:12px;margin:8px 0;background:#fff}
.tdtf details summary{cursor:pointer;padding:10px 14px;font-weight:600;color:%(azul)s;list-style:none}
.tdtf details summary::-webkit-details-marker{display:none}
.tdtf details summary:before{content:"\\f059";font-family:FontAwesome;color:%(rosa)s;margin-right:8px}
.tdtf details[open] summary{border-bottom:1px solid %(borde)s}
.tdtf details .a{padding:10px 14px;background:%(niebla)s;border-radius:0 0 12px 12px}
.tdtf details .a p:last-child{margin:0}
.tdtf .recuerda{background:%(rosa)s;color:#fff;border-radius:16px;padding:16px 20px;margin:18px 0}
.tdtf .recuerda h4{color:#fff;margin:0 0 8px;font-size:1.1rem}
.tdtf .recuerda ul{margin:0;padding-left:1.2rem}
.tdtf .cta{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:12px;margin:22px 0 8px}
.tdtf .btnp{display:flex;align-items:center;justify-content:center;gap:8px;min-height:48px;border-radius:999px;font-weight:700;text-decoration:none;padding:10px 20px;border:2px solid %(azul)s}
.tdtf .btnp.pri{background:%(azul)s;color:#fff}.tdtf .btnp.pri:hover{background:%(azul2)s;color:#fff;text-decoration:none}
.tdtf .btnp.sec{background:#fff;color:%(azul)s}.tdtf .btnp.sec:hover{border-color:%(rosa)s;color:%(rosa)s;text-decoration:none}
.tdtf .topic{display:flex;gap:14px}
.tdtf .topic .ic{flex:0 0 42px;height:42px;border-radius:12px;background:%(tinte)s;color:%(azul)s;display:flex;align-items:center;justify-content:center;font-size:1.15rem}
.tdtf .topic .body{flex:1;min-width:0}
.tdtf .topic h4{font-size:1.12rem;margin:6px 0 10px}
.tdtf table{width:100%%;border-collapse:collapse;margin:6px 0 12px;font-size:.95rem}
.tdtf th{background:%(azul)s;color:#fff;padding:8px;text-align:left}
.tdtf td{padding:8px;border-bottom:1px solid %(borde)s}
.tdtf .tw{overflow-x:auto}
.tdtf .caso{border-left:5px solid %(rosa)s}
.tdtf .caso h4{font-size:1.08rem;margin:0 0 8px}
.tdtf .errs{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:12px}
.tdtf .err{border:1px solid %(borde)s;border-radius:14px;overflow:hidden;background:#fff}
.tdtf .err .e{background:%(rosa)s;color:#fff;padding:10px 14px;font-weight:700}
.tdtf .err .p{padding:10px 14px;color:%(gris)s;font-size:.93rem}
.tdtf .err .s{padding:10px 14px;border-top:1px dashed %(borde)s;font-weight:600;color:%(azul2)s}
.tdtf .res a.r{display:flex;gap:12px;padding:12px 14px;border:1px solid %(borde)s;border-radius:14px;margin-bottom:10px;text-decoration:none;color:%(texto)s;background:#fff}
.tdtf .res a.r:hover{border-color:%(rosa)s;text-decoration:none}
.tdtf .res .nm{font-weight:700;color:%(azul)s}
.tdtf .res .org{font-size:.85rem;color:%(gris)s}
.tdtf .res .qb{margin-top:4px;font-size:.93rem}
.tdtf .chips span{display:inline-block;background:%(tinte)s;border-radius:999px;padding:4px 12px;margin:0 6px 8px 0}
.tdtf .opts{list-style:none;padding:0;margin:6px 0 10px}
.tdtf .opts li{border:1px solid %(borde)s;border-radius:10px;padding:8px 12px;margin-bottom:6px;background:#fff}
.tdtf .h5p{border:2px dashed %(rosa)s;border-radius:16px;padding:18px;text-align:center;background:%(niebla)s}
.tdtf .h5p .fa{color:%(rosa)s}
.tdtf .fuentes{font-size:.85rem;color:%(gris)s}
.tdtf abbr.term{position:relative;color:%(rosa)s;font-weight:600;text-decoration:underline dotted %(rosa)s;cursor:help;border-bottom:0;outline:none}
.tdtf abbr.term:hover:after,.tdtf abbr.term:focus:after{content:attr(title);position:absolute;left:0;top:1.7em;z-index:1000;width:max-content;max-width:260px;background:%(azul2)s;color:#fff;font-weight:500;font-size:.88rem;line-height:1.35;padding:8px 12px;border-radius:12px;box-shadow:0 6px 18px rgba(6,31,64,.25);white-space:normal;text-align:left}
@media (max-width:576px){.tdtf .hero h3{font-size:1.3rem}.tdtf .timeline{margin-left:0;padding-left:0;border-left:0}.tdtf .step .num{position:static;margin-bottom:8px;width:36px;height:36px;font-size:1rem}.tdtf .topic .ic{display:none}}
</style>""" % C

def terms(s):
    return re.sub(r"\{\{([^|}]+)\|([^}]+)\}\}",
                  lambda m: f'<abbr class="term" tabindex="0" title="{html.escape(m.group(2), quote=True)}">{m.group(1)}</abbr>', s)

def md(s):
    s = re.sub(r"(?m)^(?!\s*([-*]|\d+\.)\s)(.+)\n(?=\s*([-*]|\d+\.)\s)", r"\2\n\n", s.strip())
    h = markdown.markdown(terms(s), extensions=["tables"])
    h = h.replace("<table>", '<div class="tw"><table>').replace("</table>", "</table></div>")
    def box(m):
        kind = m.group(1)
        cls = {"Dato adicional": "dato", "Antes de actuar, verifica": "verifica", "Good to know": "dato", "Before you act, check": "verifica", "Dato por confirmar": "verifica", "Dato vigente": "dato", "Current fact": "dato", "Fact to confirm": "verifica"}.get(kind, "")
        icon = {"dato": "fa-info-circle", "verifica": "fa-check-square-o"}.get(cls, "fa-lightbulb-o")
        return f'<div class="box {cls}"><p><i class="fa {icon}"></i> <span class="h">{kind}:</span>'
    h = re.sub(r"<blockquote>\s*<p><strong>([^<:]+):</strong>", box, h)
    h = h.replace("</blockquote>", "</div>").replace("<blockquote>", '<div class="box">')
    return h

def parse(block):
    head, rest = block.split("\n", 1)
    code, title = [x.strip() for x in head.split("|", 1)]
    meta = dict(re.findall(r"(?m)^(objetivo|gancho):\s*(.+)$", rest))
    secs = {}
    for part in re.split(r"(?m)^== ", rest)[1:]:
        name, body = part.split("\n", 1)
        secs[name.strip()] = body
    return code, title, meta, secs

def blocks(body):
    out = []
    for b in re.split(r"(?m)^--- ", body)[1:]:
        head, content = (b.split("\n", 1) + [""])[:2]
        parts = [p.strip() for p in head.split("|")]
        out.append((parts[0], parts[1] if len(parts) > 1 else "", parts[2] if len(parts) > 2 else "", content.strip()))
    return out

def qa(content):
    return "".join(f'<details><summary>{terms(html.escape(q.strip()))}</summary><div class="a">{md(a)}</div></details>'
                   for q, a in re.findall(r"(?m)^\d+\.\s*(.+?)\s*\|\|\s*(.+)$", content))

def render_block(kind, icon, title, content, n=None):
    if kind == "tarjetas":
        tiles = []
        for ic, nm, ex, st, cls in [ [x.strip() for x in re.split(r"\|(?![^{]*\}\})", l[2:])] for l in content.splitlines() if l.startswith("* ")]:
            tiles.append(f'<div class="tile"><div class="ic"><i class="fa {ic}"></i></div><div class="nm">{terms(nm)}</div>'
                         f'<div class="ex">{terms(ex)}</div><div class="st {cls}">{terms(st)}</div></div>')
        inner = f'<div class="tiles">{"".join(tiles)}</div>'
        resto = "\n".join(l for l in content.splitlines() if not l.startswith("* ")).strip()
        if resto: inner += md(resto)
    elif kind == "ecuacion":
        lines = content.splitlines()
        eq = [l for l in lines if re.match(r"^[=\-+×÷] ", l)]
        intro = "\n".join(lines[:lines.index(eq[0])])
        outro = "\n".join(lines[lines.index(eq[-1]) + 1:])
        cells = []
        for i, l in enumerate(eq):
            op, rest = l[0], l[2:]
            num, lab = [x.strip() for x in rest.split("|", 1)]
            if i > 0:
                cells.append(f'<div class="op">{"=" if i == len(eq) - 1 else {"-": "−", "×": "×", "÷": "÷"}.get(op, "+")}</div>')
            cells.append(f'<div class="n{" res" if i == len(eq) - 1 else ""}"><b>{num}</b><span>{lab}</span></div>')
        inner = md(intro) + f'<div class="eq">{"".join(cells)}</div>' + md(outro)
    elif kind == "pasos":
        items = re.findall(r"(?m)^\d+\.\s+(.+)$", content)
        inner = '<ol class="check">' + "".join(f"<li>{md(i)[3:-4]}</li>" for i in items) + "</ol>"
        resto = "\n".join(l for l in content.splitlines() if not re.match(r"^\d+\.\s+", l)).strip()
        if resto: inner += md(resto)
    else:
        inner = md(content)
    num = f'<div class="num"><i class="fa {icon}"></i></div>' if n is not None else ""
    return f'<div class="step">{num}<div class="card2"><h4>{title}</h4>{inner}</div></div>'

def ruta(files, current):
    names = [("Inicio", "fa-home"), ("Lo esencial · 5 min", "fa-bolt"), ("Profundiza · +5 min", "fa-book"), ("Practica", "fa-pencil")]
    li = []
    for i, (n, ic) in enumerate(names):
        cls = ' class="on"' if i == current else ""
        li.append(f'<li><a href="{files[i]}"{cls}><i class="fa {ic}"></i> {n}</a></li>')
    return f'<ul class="ruta">{"".join(li)}</ul>'

def lesson_pages(block, prefix, next_title=None):
    code, title, meta, secs = parse(block)
    f = [f"{prefix}_0.html", f"{prefix}_1_sub.html", f"{prefix}_2_sub.html", f"{prefix}_3_sub.html"]
    ess, prof = blocks(secs["esencial"]), blocks(secs["profundiza"])
    steps = [b for b in ess if b[0] not in ("comprueba", "recuerda")]
    wrap = lambda body: f'{CSS}<div class="tdtf">{body}</div>'
    # Portada
    aprende = "".join(f"<li>{t}</li>" for _, _, t, _ in steps)
    p0 = (ruta(f, 0) +
          f'<div class="hero"><span class="code">{code}</span><h3>{title}</h3><div class="lbl">Lo que lograrás</div><p class="obj">{meta["objetivo"]}</p></div>'
          f'<div class="gancho"><div class="avatar"><i class="fa fa-comments"></i></div><div>{md(meta["gancho"])}</div></div>'
          f'<h4>Elige tu ruta</h4><div class="rutas">'
          f'<a class="rutabox" href="{f[1]}" data-ruta="rapida"><div class="t"><i class="fa fa-bolt"></i> Ruta rápida <span class="pill">5 min</span></div>'
          f'<ol><li>Lo esencial</li><li>Practica</li></ol><div class="go">Para cuando tienes poco tiempo o ya conoces el tema <i class="fa fa-arrow-right"></i></div></a>'
          f'<a class="rutabox full" href="{f[1]}" data-ruta="completa"><div class="t"><i class="fa fa-book"></i> Ruta completa <span class="pill">10 min</span></div>'
          f'<ol><li>Lo esencial</li><li>Profundiza: casos, errores frecuentes y más datos</li><li>Practica</li></ol><div class="go">Para entender a fondo <i class="fa fa-arrow-right"></i></div></a></div>'
          f'<div class="card2 aprende"><h4><i class="fa fa-map-o" style="color:{C["rosa"]}"></i> En esta lección</h4><ol>{aprende}</ol></div>')
    # Lo esencial
    body = "".join(render_block(k, ic, t, c, i) for i, (k, ic, t, c) in enumerate(steps))
    comp = next((c for k, _, _, c in ess if k == "comprueba"), "")
    rec = next((c for k, _, _, c in ess if k == "recuerda"), "")
    p1 = (ruta(f, 1) + f'<div class="pagehead"><h3>Lo esencial</h3><span class="pill">5 min</span></div>'
          f'<div class="timeline">{body}</div>'
          + (f'<div class="card2"><h4><i class="fa fa-check-circle" style="color:{C["rosa"]}"></i> Comprueba lo que entendiste</h4>{qa(comp)}</div>' if comp else "")
          + (f'<div class="recuerda"><h4><i class="fa fa-thumb-tack"></i> Para recordar</h4>{md(rec)}</div>' if rec else "")
          + f'<div class="cta"><a class="btnp sec" href="{f[2]}"><i class="fa fa-book"></i> Profundizar (+5 min)</a>'
          f'<a class="btnp pri" href="{f[3]}"><i class="fa fa-pencil"></i> Ir a practicar</a></div>')
    # Profundiza
    parts = []
    for k, ic, t, c in prof:
        if k == "casos":
            cs = re.split(r"(?m)^### ", c)[1:]
            items = []
            for cc in cs:
                ct, cb = cc.split("\n", 1)
                text = "\n".join(l for l in cb.splitlines() if not l.startswith("? "))
                qs = "".join(f'<details><summary>{terms(html.escape(q))}</summary><div class="a">{md(a)}</div></details>'
                             for q, a in re.findall(r"(?m)^\? (.+?)\s*\|\|\s*(.+)$", cb))
                items.append(f'<div class="card2 caso"><h4>{ct.strip()}</h4>{md(text)}{qs}</div>')
            parts.append(f'<h4 class="mt-4"><i class="fa fa-users" style="color:{C["rosa"]}"></i> Casos: piensa y luego revisa</h4>' + "".join(items))
        elif k == "errores":
            es = [[x.strip() for x in re.split(r"\|(?![^{]*\}\})", l[2:])] for l in c.splitlines() if l.startswith("* ")]
            cards = "".join(f'<div class="err"><div class="e"><i class="fa fa-times-circle"></i> {e}</div><div class="p">{p}</div>'
                            f'<div class="s"><i class="fa fa-check" style="color:{C["rosa"]}"></i> {s}</div></div>' for e, p, s in es)
            parts.append(f'<h4 class="mt-4"><i class="fa fa-exclamation-triangle" style="color:{C["rosa"]}"></i> Errores frecuentes</h4><div class="errs">{cards}</div>')
        else:
            parts.append(f'<div class="card2 topic"><div class="ic"><i class="fa {ic}"></i></div><div class="body"><h4>{t}</h4>{md(c)}</div></div>')
    p2 = (ruta(f, 2) + f'<div class="pagehead"><h3>Profundiza</h3><span class="pill">+5 min</span></div>' + "".join(parts)
          + f'<div class="cta"><a class="btnp sec" href="{f[1]}"><i class="fa fa-arrow-left"></i> Volver a lo esencial</a>'
          f'<a class="btnp pri" href="{f[3]}"><i class="fa fa-pencil"></i> Ir a practicar</a></div>')
    # Practica
    pr = dict((k, c) for k, _, _, c in blocks(secs["practica"]))
    quiz = ""
    if "quiz" in pr:
        for n, q in re.findall(r"(?m)^(\d+)\.\s+(.*)$", pr["quiz"]):
            ps = re.split(r"\s+(?=[a-e]\)\s)", q)
            quiz += f'<p class="mb-1"><strong>{n}. {terms(ps[0])}</strong></p><ul class="opts">' + "".join(f"<li>{o.rstrip(' ·')}</li>" for o in ps[1:]) + "</ul>"
        a = re.search(r"(?m)^respuestas:\s*(.+)$", pr["quiz"])
        if a:
            quiz += f'<details><summary>Ver respuestas</summary><div class="a">{md(a.group(1))}</div></details>'
    ponlo = ""
    if "ponlo" in pr:
        q, a = re.split(r"(?m)^respuesta:\s*", pr["ponlo"])
        ponlo = md(q) + f'<details><summary>Ver respuesta</summary><div class="a">{md(a)}</div></details>'
    recs = re.findall(r"(?m)^- \*\*(.+?)\*\* \((.+?)\):\s*(\S+)\s*\|\s*(?:Qué buscar|What to look for):\s*(.+)$", secs.get("recursos", ""))
    res = "".join(f'<a class="r" href="{u}" target="_blank" rel="noopener"><i class="fa fa-external-link" style="color:{C["rosa"]};margin-top:4px"></i>'
                  f'<div><div class="nm">{n}</div><div class="org">{o}</div><div class="qb"><i class="fa fa-search" style="color:{C["rosa"]}"></i> <b>Qué buscar:</b> {html.escape(qb)}</div></div></a>'
                  for n, o, u, qb in recs)
    pal = re.findall(r"(?m)^- \*([^*:]+):\*\s*(.+)$", secs.get("palabras", ""))
    chips = "".join(f'<span><abbr class="term" tabindex="0" title="{html.escape(d, quote=True)}">{k}</abbr></span>' for k, d in pal)
    nxt = f'Siguiente lección: {next_title}' if next_title else "Siguiente lección"
    p3 = (ruta(f, 3) + f'<div class="pagehead"><h3>Practica</h3></div>'
          + (f'<div class="card2"><h4><i class="fa fa-hand-pointer-o" style="color:{C["rosa"]}"></i> Actividad interactiva</h4>{md(pr["actividad"])}'
             f'<div class="h5p"><i class="fa fa-puzzle-piece fa-2x"></i><p class="mb-0 mt-2">La actividad está justo después de este libro, en la sección del módulo.</p></div></div>' if "actividad" in pr else "")
          + (f'<div class="card2"><h4><i class="fa fa-question-circle" style="color:{C["rosa"]}"></i> Pon a prueba lo que sabes</h4>{quiz}</div>' if quiz else "")
          + (f'<div class="card2"><h4><i class="fa fa-calculator" style="color:{C["rosa"]}"></i> Ponlo en práctica</h4>{ponlo}</div>' if ponlo else "")
          + (f'<div class="card2" style="background:{C["tinte"]}"><h4><i class="fa fa-map-signs" style="color:{C["rosa"]}"></i> A tu plan</h4>{md(pr["plan"])}</div>' if "plan" in pr else "")
          + (f'<div class="card2 res"><h4><i class="fa fa-external-link" style="color:{C["rosa"]}"></i> Para saber más</h4>{res}</div>' if res else "")
          + (f'<div class="card2 chips"><h4><i class="fa fa-tags" style="color:{C["rosa"]}"></i> Palabras clave</h4><p class="fuentes">Toca o pasa el cursor sobre cada palabra para ver qué significa.</p>{chips}</div>' if chips else "")
          + f'<div class="recuerda" style="display:flex;gap:14px;align-items:center"><i class="fa fa-arrow-circle-up fa-2x"></i><div><b>¡Terminaste esta lección!</b><br>Completa la actividad y el quiz para sumar puntos. {nxt}.</div></div>'
          + (f'<p class="fuentes"><b>Fuentes:</b> {html.escape(secs["fuentes"].strip())}</p>' if secs.get("fuentes") else ""))
    titles = [f"{code}. {title}", "Lo esencial · 5 min", "Profundiza · +5 min", "Practica"]
    return [(f[i], titles[i], wrap(p)) for i, p in enumerate([p0, p1, p2, p3])]

def page(title, body):
    return f'<!DOCTYPE html>\n<html><head><meta charset="utf-8"><title>{html.escape(title)}</title></head><body>\n{body}\n</body></html>\n'

def build(md_text):
    blocks_ = [b for b in re.split(r"(?m)^# ", md_text) if b.strip()]
    heads = [b.split("\n", 1)[0].split("|", 1) for b in blocks_]
    pages = []
    for i, b in enumerate(blocks_):
        nxt = f"{heads[i+1][0].strip()}. {heads[i+1][1].strip()}" if i + 1 < len(blocks_) else None
        pages += lesson_pages(b, f"{i+1:02d}_" + heads[i][0].strip().lower().replace(" ", ""), nxt)
    return pages
