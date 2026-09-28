# Convierte una lección en Markdown en HTML interactivo para el Libro de Moodle (Boost, Bootstrap 4).
# Selector de versión (5 o 10 minutos) con pestañas, tarjetas, respuestas plegables y términos con significado.
# El Libro de Moodle 3.10 muestra el capítulo con noclean, así que las clases y data-* de Bootstrap funcionan.
import re, html, markdown

AZUL, AZUL2, ROSA, TINTE, NIEBLA, BORDE, GRIS = "#0A3161", "#061F40", "#E4007C", "#E6ECF5", "#F5F7FB", "#E5E8F0", "#5A6478"
TXT = {
 "es": dict(corta="Versión corta", amplia="Versión amplia", min5="5 min", min10="10 min", elige="¿Cuánto tiempo tienes hoy?",
            corta_d="Lo indispensable para actuar", amplia_d="Explicación completa, casos y errores frecuentes",
            profundiza="Para profundizar", practica="Practica lo que aprendiste", ver="Ver respuesta", verq="Ver respuestas",
            logro="Lo que lograrás", saber="Para saber más", claves="Palabras clave", fuentes="Fuentes", plan="A tu plan",
            actividad="Actividad interactiva", quiz="Quiz", ponlo="Ponlo en práctica", caso="Caso", sig="Siguiente paso",
            sig_t="Termina la actividad y el quiz de esta lección para sumar puntos."),
 "en": dict(corta="Short version", amplia="Extended version", min5="5 min", min10="10 min", elige="How much time do you have today?",
            corta_d="What you need to act", amplia_d="Full explanation, cases and common mistakes",
            profundiza="Go deeper", practica="Practice what you learned", ver="Show answer", verq="Show answers",
            logro="What you will achieve", saber="Learn more", claves="Key words", fuentes="Sources", plan="Your plan",
            actividad="Interactive activity", quiz="Quiz", ponlo="Put it into practice", caso="Case", sig="Next step",
            sig_t="Finish this lesson's activity and quiz to earn points."),
}
TERM = f'class="tdtf-termino" style="color:{ROSA};font-weight:600;text-decoration:underline dotted {ROSA};cursor:help;border-bottom:0"'

def terms(md):
    return re.sub(r"\{\{([^|}]+)\|([^}]+)\}\}",
                  lambda m: f'<abbr {TERM} tabindex="0" title="{html.escape(m.group(2), quote=True)}">{m.group(1)}</abbr>', md)

def prep(md):
    md = re.sub(r"(?<![(<\[])(https?://[^\s)]+?)([.,;]?)(?=\s|$)", r"<\1>\2", md)
    md = re.sub(r"(?m)^(?!\s*([-*]|\d+\.)\s)(.+)\n(?=\s*([-*]|\d+\.)\s)", r"\2\n\n", md)
    md = re.sub(r"(?m)^  (?=[-*] )", "    ", md)
    return terms(md)

def md2h(md):
    h = markdown.markdown(prep(md), extensions=["tables"])
    h = h.replace("<table>", f'<div class="table-responsive mb-3"><table class="table table-sm mb-0" style="border:1px solid {BORDE}">').replace("</table>", "</table></div>")
    h = h.replace("<th>", f'<th style="background:{AZUL};color:#fff;border-color:{BORDE}">')
    h = re.sub(r"<blockquote>\s*<p><strong>(Idea clave|Key idea):?</strong>:?", lambda m: box("fa-lightbulb-o", ROSA, TINTE, m.group(1)), h)
    h = re.sub(r"<blockquote>\s*<p><strong>(Dato adicional|Did you know|Extra fact):?</strong>:?", lambda m: box("fa-info-circle", AZUL, "#FFFFFF", m.group(1)), h)
    h = re.sub(r"<blockquote>\s*<p><strong>(Antes de actuar, verifica|Before you act, check):?</strong>:?", lambda m: box("fa-check-square-o", "#B35C00", "#FFF6EC", m.group(1)), h)
    h = h.replace("<blockquote>", f'<div class="p-3 my-3" style="background:{TINTE};border-radius:12px"><p>').replace("</blockquote>", "</div>")
    return h

def box(icon, color, bg, title):
    return (f'<div class="p-3 my-3" style="background:{bg};border:1px solid {BORDE};border-left:5px solid {color};border-radius:12px">'
            f'<p><i class="fa {icon}" style="color:{color}"></i> <strong style="color:{color}">{title}:</strong>')

def card(inner, title=None, icon=None, accent=AZUL, extra=""):
    head = ""
    if title:
        ic = f'<i class="fa {icon} mr-2" style="color:{accent}"></i>' if icon else ""
        head = f'<h4 class="h5 mb-3" style="color:{AZUL2};font-weight:800">{ic}{title}</h4>'
    return f'<div class="card mb-3" style="border:1px solid {BORDE};border-radius:16px;{extra}"><div class="card-body">{head}{inner}</div></div>'

def collapse(uid, label, inner):
    return (f'<button class="btn btn-sm mt-2" type="button" data-toggle="collapse" data-target="#{uid}" aria-expanded="false" aria-controls="{uid}" '
            f'style="border:2px solid {AZUL};color:{AZUL};border-radius:999px;font-weight:600"><i class="fa fa-eye mr-1"></i>{label}</button>'
            f'<div class="collapse mt-2" id="{uid}"><div class="p-3" style="background:{NIEBLA};border-radius:12px">{inner}</div></div>')

def split_h3(body):
    parts = re.split(r"(?m)^### ", body)
    return parts[0], {p.split("\n", 1)[0].strip(): (p.split("\n", 1)[1] if "\n" in p else "") for p in parts[1:]}

def find(secs, *names):
    for k in secs:
        for n in names:
            if k.startswith(n):
                return secs[k]
    return None

def render_casos(md, uid, t):
    items = re.split(r"(?m)^(?=\*\*(?:Caso|Case) \d)", md.strip())
    out = [md2h(items[0])] if items[0].strip() and not items[0].startswith("**") else []
    for i, it in enumerate(i for i in items if re.match(r"\*\*(?:Caso|Case) \d", i)):
        lines = it.strip().split("\n")
        ans = [l for l in lines if re.match(r"\s*- \*", l)]
        rest = "\n".join(l for l in lines if l not in ans)
        inner = md2h(rest)
        if ans:
            inner += collapse(f"{uid}-caso{i+1}", t["ver"], md2h("\n".join(a.strip() for a in ans)))
        out.append(card(inner, extra=f"border-left:5px solid {ROSA} !important"))
    return "".join(out)

def render_amplia(md, uid, t):
    subs = re.split(r"(?m)^#### ", md)
    out = [md2h(subs[0])] if subs[0].strip() else []
    icons = {"Casos": "fa-users", "Cases": "fa-users", "Errores frecuentes": "fa-exclamation-triangle", "Common mistakes": "fa-exclamation-triangle"}
    for s in subs[1:]:
        title, body = (s.split("\n", 1) + [""])[:2]
        title = title.strip()
        if title in ("Casos", "Cases"):
            out.append(f'<h4 class="h5 mt-4 mb-3" style="color:{AZUL2};font-weight:800"><i class="fa fa-users mr-2" style="color:{ROSA}"></i>{title}</h4>')
            out.append(render_casos(body, uid, t))
        else:
            out.append(card(md2h(body), title, icons.get(title, "fa-bookmark-o"), ROSA if title in icons else AZUL))
    return "".join(out)

def render_quiz(md, uid, t):
    qs = re.findall(r"(?m)^(\d+)\.\s+(.*)$", md)
    ans = re.search(r"\*\*(?:Respuestas|Answers):\*\*\s*(.*)", md)
    inner = ""
    for n, q in qs:
        parts = re.split(r"\s+(?=[a-e]\)\s)", q)
        opts = "".join(f'<li class="list-group-item py-2" style="border-color:{BORDE}">{html.escape(o.rstrip(" ·"))}</li>' for o in parts[1:])
        inner += f'<p class="mb-1 mt-3"><strong>{n}. {terms(html.escape(parts[0]))}</strong></p><ul class="list-group mb-2" style="border-radius:12px">{opts}</ul>'
    if ans:
        inner += collapse(f"{uid}-quiz", t["verq"], md2h(ans.group(1)))
    return inner

def render_practica(md, uid, t):
    m = re.search(r"\*\*(?:Respuesta|Answer):\*\*(.*?)(?=\n>|\Z)", md, re.S)
    q = md[:m.start()] if m else md
    rest = md[m.end():] if m else ""
    inner = md2h(q)
    if m:
        inner += collapse(f"{uid}-prac", t["ver"], md2h(m.group(1).strip()))
    return inner + md2h(rest)

def render_links(md):
    items = re.findall(r"(?m)^- \*\*(.+?)\*\* \((.+?)\):\s*(\S+)(?:\s*\|\s*(?:Qué buscar|What to look for):\s*(.*))?", md)
    if not items:
        return md2h(md)
    look = lambda b: f'<br><span style="color:#0B1220"><i class="fa fa-search mr-1" style="color:{ROSA}"></i><strong>Qué buscar:</strong> {html.escape(b)}</span>' if b else ""
    li = "".join(f'<a class="list-group-item list-group-item-action d-flex align-items-start" href="{u}" target="_blank" rel="noopener" style="border-color:{BORDE}">'
                 f'<i class="fa fa-external-link mr-3 mt-1" style="color:{ROSA}"></i><span><strong style="color:{AZUL}">{html.escape(n)}</strong> <small style="color:{GRIS}">({html.escape(o)})</small>{look(b)}</span></a>'
                 for n, o, u, b in items)
    return f'<div class="list-group" style="border-radius:12px">{li}</div>'

def render_claves(md):
    items = re.findall(r"\*([^*:]+):\*\s*([^*\n]+)", md)
    chips = "".join(f'<span class="d-inline-block mr-2 mb-2 px-3 py-1" style="background:{TINTE};border-radius:999px">'
                    f'<abbr {TERM} tabindex="0" title="{html.escape(d.strip(), quote=True)}">{html.escape(k.strip())}</abbr></span>' for k, d in items)
    return chips

def leccion(code, title, body, lang="es"):
    t = TXT[lang]
    uid = "tdtf-" + code.lower().replace(" ", "")
    pre, secs = split_h3(body)
    logro = re.search(r"\*\*(?:Lo que lograrás|What you will achieve):\*\*\s*(.*)", pre)
    palabras = re.search(r"\*\*(?:Palabras clave|Key words):\*\*\s*(.*?)(?=\n\*\*(?:Fuentes|Sources)|\Z)", body, re.S)
    fuentes = re.search(r"\*\*(?:Fuentes|Sources):\*\*\s*(.*)", body)
    corta = find(secs, "Versión corta", "Short version") or ""
    amplia = find(secs, "Versión amplia", "Extended version") or ""
    for x in ("corta", "amplia"):
        pass
    strip_tail = lambda s: re.split(r"\n\*\*(?:Palabras clave|Key words|Fuentes|Sources):\*\*", s)[0]
    out = [f'<div class="tdtf-leccion" style="max-width:860px">']
    if logro:
        out.append(f'<div class="p-3 mb-3" style="background:{AZUL};color:#fff;border-radius:16px">'
                   f'<small style="color:#FF4FA8;font-weight:700;text-transform:uppercase;letter-spacing:.05em">{t["logro"]}</small>'
                   f'<p class="mb-0 mt-1" style="font-size:1.1rem">{terms(html.escape(logro.group(1)))}</p></div>')
    # Selector de versión
    pill = lambda key, icon, mins, desc, active: (
        f'<li class="nav-item flex-fill"><a class="nav-link text-left h-100{" active" if active else ""}" id="{uid}-{key}-tab" data-toggle="pill" href="#{uid}-{key}" role="tab" '
        f'aria-controls="{uid}-{key}" aria-selected="{"true" if active else "false"}" data-tdtf-version="{key}" style="border:2px solid {AZUL};border-radius:16px;margin:4px">'
        f'<i class="fa {icon} mr-2"></i><strong>{t[key]}</strong> <span class="badge ml-1" style="background:{ROSA};color:#fff;border-radius:999px">{mins}</span>'
        f'<br><small>{desc}</small></a></li>')
    out.append(f'<p class="mb-2" style="color:{GRIS};font-weight:600">{t["elige"]}</p>')
    out.append(f'<ul class="nav nav-pills mb-3 d-flex flex-column flex-sm-row" role="tablist">'
               f'{pill("corta", "fa-bolt", t["min5"], t["corta_d"], True)}{pill("amplia", "fa-book", t["min10"], t["amplia_d"], False)}</ul>')
    cort_html = md2h(corta)
    out.append(f'<div class="tab-content">'
               f'<div class="tab-pane fade show active" id="{uid}-corta" role="tabpanel" aria-labelledby="{uid}-corta-tab">{card(cort_html)}</div>'
               f'<div class="tab-pane fade" id="{uid}-amplia" role="tabpanel" aria-labelledby="{uid}-amplia-tab">{card(cort_html)}'
               f'<h3 class="h4 mt-4 mb-3" style="color:{AZUL2};font-weight:800"><i class="fa fa-book mr-2" style="color:{ROSA}"></i>{t["profundiza"]}</h3>'
               f'{render_amplia(amplia, uid, t)}</div></div>')
    # Práctica común
    out.append(f'<h3 class="h4 mt-4 mb-3" style="color:{AZUL2};font-weight:800"><i class="fa fa-pencil mr-2" style="color:{ROSA}"></i>{t["practica"]}</h3>')
    act = find(secs, "Actividad interactiva", "Interactive activity")
    if act: out.append(card(md2h(act), t["actividad"], "fa-hand-pointer-o", ROSA))
    qz = find(secs, "Quiz")
    if qz: out.append(card(render_quiz(qz, uid, t), t["quiz"], "fa-question-circle", ROSA))
    pp = find(secs, "Ponlo en práctica", "Put it into practice")
    if pp: out.append(card(render_practica(pp, uid, t), t["ponlo"], "fa-calculator", ROSA))
    pl = find(secs, "A tu plan", "Your plan")
    if pl: out.append(card(md2h(strip_tail(pl)), t["plan"], "fa-map-signs", ROSA, f"background:{TINTE}"))
    sm = find(secs, "Para saber más", "Learn more")
    if sm: out.append(card(render_links(strip_tail(sm)), t["saber"], "fa-external-link", AZUL))
    if palabras:
        out.append(card(render_claves(palabras.group(1)), t["claves"], "fa-tags", AZUL))
    out.append(f'<div class="p-3 my-3 d-flex align-items-center" style="background:{ROSA};color:#fff;border-radius:16px">'
               f'<i class="fa fa-arrow-circle-up fa-2x mr-3"></i><div><strong>{t["sig"]}</strong><br>{t["sig_t"]}</div></div>')
    if fuentes:
        out.append(f'<p class="small mt-2" style="color:{GRIS}"><strong>{t["fuentes"]}:</strong> {html.escape(fuentes.group(1))}</p>')
    # Recordar la versión elegida entre capítulos (opcional; sin JavaScript, la versión corta queda por defecto).
    out.append('<script>(function(){try{var v=localStorage.getItem("tdtf-version");'
               'document.querySelectorAll("[data-tdtf-version]").forEach(function(a){a.addEventListener("click",function(){try{localStorage.setItem("tdtf-version",a.getAttribute("data-tdtf-version"))}catch(e){}})});'
               'if(v==="amplia"){window.addEventListener("load",function(){var a=document.querySelector(\'[data-tdtf-version="amplia"]\');if(a)a.click();});}}catch(e){}})();</script>')
    out.append("</div>")
    return "".join(out)

def pagina(title, inner):
    return f'<!DOCTYPE html>\n<html><head><meta charset="utf-8"><title>{html.escape(title)}</title></head><body>\n{inner}\n</body></html>\n'
