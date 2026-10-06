# Lecciones UX3: un Libro de Moodle por lección, con 4 capítulos sin claves técnicas:
#   Empieza · Lo esencial · Profundiza (opcional) · Practica.
# Cambios frente a UX2: el nombre de la lección es su pregunta (sin «M1 U01»), los tiempos se calculan
# con el número de palabras, los dos errores principales pasan a Lo esencial, los casos ya no se repiten
# en Profundiza (viven en la práctica interactiva) y la práctica va dentro de la lección.
import re, html, math
from leccion_ux2 import C, CSS as CSS2, md, terms, parse, blocks, render_block, qa

CSS = CSS2.replace("</style>", """
.tdtf .ruta .opc{font-weight:500;opacity:.8;border:0;padding:0;background:none;display:inline}
.tdtf .hero .num{display:inline-block;background:rgba(255,255,255,.16);color:#fff;border-radius:999px;padding:2px 12px;font-weight:700;font-size:.8rem}
.tdtf .rutabox .t{font-size:1.15rem}
.tdtf .rutabox .tm{font-weight:600;margin-top:6px}
.tdtf .cuidado{background:#fff;border:2px solid %(rosa)s;border-radius:16px;padding:16px 20px;margin:18px 0}
.tdtf .cuidado h4{color:%(rosa)s;margin:0 0 10px;font-size:1.1rem}
.tdtf .cuidado .it{display:flex;gap:12px;padding:10px 0;border-top:1px dashed %(borde)s}
.tdtf .cuidado .it:first-of-type{border-top:0}
.tdtf .cuidado .it i{color:%(rosa)s;margin-top:4px}
.tdtf .cuidado .s{color:%(azul2)s;font-weight:600}
.tdtf .practica-h5p{border:2px dashed %(rosa)s;border-radius:16px;padding:16px;background:%(niebla)s;margin:8px 0 12px}
.tdtf .practica-h5p .ph{font-weight:700;color:%(rosa)s}
.tdtf .fin{background:%(azul)s;color:#fff;border-radius:16px;padding:18px 20px;margin:18px 0;display:flex;gap:14px;align-items:center}
.tdtf .fin b{font-size:1.1rem}
@media (max-width:576px){
.tdtf .ruta{flex-wrap:nowrap;overflow-x:auto;gap:4px;margin:0 -4px 14px;padding:2px 4px;scrollbar-width:none}
.tdtf .ruta::-webkit-scrollbar{display:none}
.tdtf .ruta a{padding:6px 11px;font-size:.82rem;white-space:nowrap}
.tdtf .ruta .opc{display:none}
.tdtf .hero{padding:18px 18px 16px;border-radius:16px}
.tdtf .hero:after{display:none}
.tdtf .gancho{padding:14px 16px}
.tdtf .avatar{flex-basis:40px;height:40px;font-size:1.1rem}
.tdtf .rutas{grid-template-columns:1fr;gap:10px}
.tdtf .rutabox{padding:14px 16px}
.tdtf .card2{padding:14px 16px}
.tdtf .cta{grid-template-columns:1fr}
}
</style>""" % C)

PPM = 130          # palabras por minuto, ritmo pausado
MIN_PRACTICA = 6   # 3 situaciones, 3 preguntas, ejercicio y compromiso


def palabras(s):
    s = re.sub(r"\{\{([^|}]+)\|[^}]+\}\}", r"\1", s)
    return len(re.findall(r"\w+", s))


def redondea(m):
    return max(5, int(5 * round(m / 5)))


def errores(secs):
    c = next((c for k, _, _, c in blocks(secs.get("profundiza", "")) if k == "errores"), "")
    return [[x.strip() for x in re.split(r"\|(?![^{]*\}\})", l[2:])] for l in c.splitlines() if l.startswith("* ")]


def tiempos(secs):
    errs = errores(secs)
    ess = palabras(secs.get("esencial", "")) + sum(palabras(" ".join(e)) for e in errs[:2])
    prof_txt = "".join(c for k, _, _, c in blocks(secs.get("profundiza", "")) if k not in ("casos",))
    prof = palabras(prof_txt) - sum(palabras(" ".join(e)) for e in errs[:2])
    rapida = math.ceil(ess / PPM) + MIN_PRACTICA
    return redondea(rapida), max(5, redondea(math.ceil(max(prof, 0) / PPM)))


NOMBRES = ["Empieza", "Lo esencial", "Profundiza", "Practica"]
ARCH = ["01_empieza.html", "02_lo_esencial.html", "03_profundiza.html", "04_practica.html"]


def ruta(current):
    ics = ["fa-flag", "fa-bolt", "fa-book", "fa-pencil"]
    li = []
    for i, n in enumerate(NOMBRES):
        cls = ' class="on"' if i == current else ""
        extra = ' <span class="opc">(opcional)</span>' if i == 2 else ""
        li.append(f'<li><a href="{ARCH[i]}"{cls}><i class="fa {ics[i]}"></i> {n}{extra}</a></li>')
    return f'<ul class="ruta">{"".join(li)}</ul>'


def h5p_nombre(code):
    return f"{code.replace(' ', '_')}_practica.h5p"


def quiz_items(pr):
    """[(pregunta, [opciones], letra_correcta, explicación)] del bloque quiz."""
    out = []
    if "quiz" not in pr: return out
    resp = re.search(r"(?m)^respuestas:\s*(.+)$", pr["quiz"])
    trip = re.findall(r"(\d+)-([a-e]):\s*(.*?)(?=\s+\d+-[a-e]:|$)", resp.group(1)) if resp else []
    keys = {n: k for n, k, _ in trip}
    expl = {n: e.strip().rstrip(".") for n, _, e in trip}
    for n, q in re.findall(r"(?m)^(\d+)\.\s+(.*)$", pr["quiz"]):
        ps = re.split(r"\s+(?=[a-e]\)\s)", q)
        opts = [o[3:].rstrip(" ·").strip() for o in ps[1:]]
        out.append((ps[0].strip(), opts, keys.get(n, "a"), expl.get(n, "")))
    return out


def lesson_pages(block, num, total, next_title=None, en=False):
    code, title, meta, secs = parse(block)
    t_rap, t_prof = tiempos(secs)
    ess = blocks(secs["esencial"])
    steps = [b for b in ess if b[0] not in ("comprueba", "recuerda")]
    errs = errores(secs)
    wrap = lambda body: f'{CSS}<div class="tdtf">{body}</div>'

    # 1. Empieza
    p0 = (ruta(0) +
          f'<div class="hero"><span class="num">Lección {num} de {total}</span><h3>{title}</h3>'
          f'<div class="lbl">Al terminar podrás</div><p class="obj">{meta["objetivo"]}</p></div>'
          f'<div class="gancho"><div class="avatar"><i class="fa fa-comments"></i></div><div>{md(meta["gancho"])}</div></div>'
          f'<h4>Elige tu ruta</h4><div class="rutas">'
          f'<a class="rutabox" href="{ARCH[1]}"><div class="t"><i class="fa fa-bolt"></i> Lo esencial</div>'
          f'<div>Lo más importante y la práctica.</div><div class="tm"><i class="fa fa-clock-o"></i> Unos {t_rap} minutos</div></a>'
          f'<a class="rutabox full" href="{ARCH[1]}"><div class="t"><i class="fa fa-book"></i> Lo esencial + Profundiza</div>'
          f'<div>Suma más datos y explicaciones.</div><div class="tm"><i class="fa fa-clock-o"></i> Unos {t_rap + t_prof} minutos</div></a></div>'
          f'<p class="fuentes">Las dos rutas terminan en la práctica. Puedes abrir Profundiza cuando quieras.</p>')

    # 2. Lo esencial (con los dos errores principales)
    body = "".join(render_block(k, ic, t, c, i) for i, (k, ic, t, c) in enumerate(steps))
    comp = next((c for k, _, _, c in ess if k == "comprueba"), "")
    rec = next((c for k, _, _, c in ess if k == "recuerda"), "")
    cuidado = ""
    if errs:
        items = "".join(f'<div class="it"><i class="fa fa-exclamation-triangle"></i><div><b>{terms(e)}.</b> {terms(p)}.<br>'
                        f'<span class="s"><i class="fa fa-check"></i> {terms(s)}.</span></div></div>' for e, p, s in errs[:2])
        cuidado = f'<div class="cuidado"><h4><i class="fa fa-hand-paper-o"></i> Cuidado con estos errores</h4>{items}</div>'
    p1 = (ruta(1) + f'<div class="pagehead"><h3>Lo esencial</h3></div>'
          f'<div class="timeline">{body}</div>' + cuidado
          + (f'<div class="card2"><h4><i class="fa fa-check-circle" style="color:{C["rosa"]}"></i> Comprueba lo que entendiste</h4>{qa(comp)}</div>' if comp else "")
          + (f'<div class="recuerda"><h4><i class="fa fa-thumb-tack"></i> Para recordar</h4>{md(rec)}</div>' if rec else "")
          + f'<div class="cta"><a class="btnp sec" href="{ARCH[2]}"><i class="fa fa-book"></i> Profundizar (opcional, unos {t_prof} min)</a>'
          f'<a class="btnp pri" href="{ARCH[3]}"><i class="fa fa-pencil"></i> Ir a practicar</a></div>')

    # 3. Profundiza (sin los casos: viven en la práctica)
    parts = []
    for k, ic, t, c in blocks(secs["profundiza"]):
        if k == "casos":
            continue
        if k == "errores":
            resto = errs[2:]
            if not resto: continue
            cards = "".join(f'<div class="err"><div class="e"><i class="fa fa-times-circle"></i> {terms(e)}</div><div class="p">{terms(p)}</div>'
                            f'<div class="s"><i class="fa fa-check" style="color:{C["rosa"]}"></i> {terms(s)}</div></div>' for e, p, s in resto)
            parts.append(f'<h4 class="mt-4"><i class="fa fa-exclamation-triangle" style="color:{C["rosa"]}"></i> Otros errores frecuentes</h4><div class="errs">{cards}</div>')
        else:
            parts.append(f'<div class="card2 topic"><div class="ic"><i class="fa {ic}"></i></div><div class="body"><h4>{t}</h4>{md(c)}</div></div>')
    p2 = (ruta(2) + f'<div class="pagehead"><h3>Profundiza</h3><span class="pill">opcional · unos {t_prof} min</span></div>' + "".join(parts)
          + f'<div class="cta"><a class="btnp sec" href="{ARCH[1]}"><i class="fa fa-arrow-left"></i> Volver a lo esencial</a>'
          f'<a class="btnp pri" href="{ARCH[3]}"><i class="fa fa-pencil"></i> Ir a practicar</a></div>')

    # 4. Practica
    pr = dict((k, c) for k, _, _, c in blocks(secs["practica"]))
    cs = next((c for k, _, _, c in blocks(secs["profundiza"]) if k == "casos"), "")
    por_que = ""
    for cc in re.split(r"(?m)^### ", cs)[1:]:
        ct, cb = cc.split("\n", 1)
        a = re.search(r"(?m)^\? .+?\s*\|\|\s*(.+)$", cb)
        nombre = html.escape(re.sub(r"^(Caso|Case) \d+\.\s*", "", ct.strip()))
        if a: por_que += f"<li><b>{nombre}:</b> {terms(a.group(1))}</li>"
    for q, opts, k, e in quiz_items(pr):
        idx = "abcde".index(k)
        if idx < len(opts):
            por_que += f"<li><b>{terms(q)}</b> {terms(opts[idx])}" + (f". {terms(e[:1].upper() + e[1:])}." if e else ".") + "</li>"
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
    nxt = f'Sigue: <b>{html.escape(next_title)}</b>' if next_title else "Ya puedes hacer la autoevaluación del módulo."
    p3 = (ruta(3) + f'<div class="pagehead"><h3>Practica</h3></div>'
          f'<div class="card2"><h4><i class="fa fa-hand-pointer-o" style="color:{C["rosa"]}"></i> ¿Qué harías? y Repasa</h4>'
          f'<p>Tres situaciones y tres preguntas, una por pantalla. Si fallas, puedes intentarlo de nuevo.</p>'
          f'<div class="practica-h5p"><p class="ph">[[H5P {h5p_nombre(code)}]]</p>'
          f'<p class="fuentes mb-0">Instalación: sustituye este recuadro por la actividad {h5p_nombre(code)} incrustada desde el banco de contenido.</p></div>'
          + (f'<details><summary>¿Por qué son esas las mejores respuestas?</summary><div class="a"><ul>{por_que}</ul></div></details>' if por_que else "")
          + '</div>'
          + (f'<div class="card2"><h4><i class="fa fa-calculator" style="color:{C["rosa"]}"></i> Con tus números</h4>{ponlo}</div>' if ponlo else "")
          + (f'<div class="card2" style="background:{C["tinte"]}"><h4><i class="fa fa-map-signs" style="color:{C["rosa"]}"></i> Tu compromiso</h4>{md(pr["plan"])}'
             f'<p class="fuentes">No compartas montos reales ni datos de tus cuentas: esto es solo para ti.</p></div>' if "plan" in pr else "")
          + f'<div class="fin"><i class="fa fa-star fa-2x"></i><div><b>¡Terminaste esta lección!</b><br>{nxt}</div></div>'
          + (f'<details><summary>Para saber más</summary><div class="a res">{res}</div></details>' if res else "")
          + (f'<details><summary>Palabras clave</summary><div class="a chips">{chips}</div></details>' if chips else "")
          + (f'<p class="fuentes"><b>Fuentes:</b> {html.escape(secs["fuentes"].strip())}</p>' if secs.get("fuentes") else ""))
    return {"code": code, "title": title, "min": [t_rap, t_rap + t_prof], "h5p": h5p_nombre(code),
            "pages": [(ARCH[i], NOMBRES[i], wrap(p)) for i, p in enumerate([p0, p1, p2, p3])]}


def build(md_text):
    bs = [b for b in re.split(r"(?m)^# ", md_text) if b.strip()]
    heads = [b.split("\n", 1)[0].split("|", 1) for b in bs]
    return [lesson_pages(b, i + 1, len(bs), heads[i + 1][1].strip() if i + 1 < len(bs) else None) for i, b in enumerate(bs)]
