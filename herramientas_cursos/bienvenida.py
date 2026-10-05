# Libros de Bienvenida (antes de la primera lección) y de Cierre y despedida (después de la conclusión), con diseño visual,
# más la guía de contacto y comunidad para imprimir o compartir. Todo sale de curso.json ("bienvenida": {"conecta", "despedida"},
# "contacto" opcional: {"correo", "whatsapp", "horario"}) y de las lecciones.
# Uso desde curso.py (paso "bienvenida") o: python3 herramientas_cursos/bienvenida.py cursos/<curso>
import os, re, sys, json, html, zipfile, shutil

AZ, AZ2, RO, RS, GR, FO, TX = "#0A3161", "#061F40", "#E4007C", "#FF4FA8", "#E6ECF5", "#F5F7FB", "#5A6478"
LOGO = '<svg aria-label="Desarrolla Talento" viewBox="0 0 64 64" width="64" height="64"><g fill="none" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"><path d="M10 52 L32 32 L54 52" stroke="#0A3161"/><path d="M10 32 L32 12 L54 32" stroke="#E4007C"/></g></svg>'
ICONOS_MOD = ["fa-calendar", "fa-university", "fa-line-chart", "fa-shield", "fa-flag-checkered", "fa-users", "fa-home", "fa-briefcase",
              "fa-leaf", "fa-heart", "fa-star"]

CSS = f"""<style>
.dtw{{font-family:Figtree,system-ui,-apple-system,"Segoe UI",sans-serif;color:{AZ2};line-height:1.55;max-width:860px;margin:0 auto}}
.dtw *{{box-sizing:border-box}}
.dtw a{{color:{RO};font-weight:700;text-decoration:none;word-break:break-word}}
.dtw .hero{{background:linear-gradient(135deg,{AZ} 0%,{AZ2} 55%,{RO} 140%);color:#fff;border-radius:24px;padding:32px 24px;position:relative;overflow:hidden;margin-bottom:22px}}
.dtw .hero:after{{content:"";position:absolute;right:-70px;top:-70px;width:220px;height:220px;border-radius:50%;background:rgba(255,79,168,.28)}}
.dtw .hero:before{{content:"";position:absolute;left:-50px;bottom:-80px;width:180px;height:180px;border-radius:50%;background:rgba(255,255,255,.07)}}
.dtw .hero .tag{{display:inline-block;background:rgba(255,255,255,.16);border-radius:999px;padding:4px 14px;font-size:.8rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase}}
.dtw .hero h2{{font-family:"Bricolage Grotesque",Figtree,sans-serif;font-weight:800;font-size:2rem;line-height:1.15;margin:14px 0 8px;color:#fff;position:relative;z-index:1}}
.dtw .hero p{{font-size:1.08rem;margin:0;opacity:.95;position:relative;z-index:1}}
.dtw .hero .logo{{width:92px;height:92px;margin:0 auto 6px;border-radius:50%;background:#fff;display:flex;align-items:center;justify-content:center;position:relative;z-index:1;box-shadow:0 8px 24px rgba(0,0,0,.25)}}
.dtw .hero .logo svg{{width:56px;height:56px}}
.dtw .marca{{display:flex;justify-content:center;margin-top:24px}}.dtw .marca svg{{width:40px;height:40px}}
.dtw .quote{{background:#fff;border-left:6px solid {RO};border-radius:16px;padding:20px 22px;font-size:1.1rem;box-shadow:0 6px 20px rgba(6,31,64,.08);margin-bottom:22px}}
.dtw h3{{font-family:"Bricolage Grotesque",Figtree,sans-serif;font-weight:800;color:{AZ};font-size:1.35rem;margin:26px 0 12px}}
.dtw .grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:14px}}
.dtw .card{{background:#fff;border-radius:18px;padding:18px;box-shadow:0 4px 16px rgba(6,31,64,.07);border:1px solid {GR}}}
.dtw .card .ic{{width:46px;height:46px;border-radius:14px;background:{GR};color:{AZ};display:flex;align-items:center;justify-content:center;font-size:1.3rem;margin-bottom:10px}}
.dtw .card.rosa .ic{{background:#FFE3F1;color:{RO}}}
.dtw .card b{{display:block;color:{AZ};font-size:1.02rem;margin-bottom:4px}}
.dtw .card span{{color:{TX};font-size:.95rem}}
.dtw .card .num,.dtw .num{{display:inline-block;background:{RO};color:#fff;border-radius:999px;font-size:.75rem;font-weight:700;padding:2px 10px;margin-bottom:8px}}
.dtw .stats{{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:12px;margin:6px 0 4px}}
.dtw .stat{{background:{AZ};color:#fff;border-radius:18px;padding:16px;text-align:center}}
.dtw .stat .n{{font-family:"Bricolage Grotesque",Figtree,sans-serif;font-size:1.9rem;font-weight:800;color:{RS};display:block;line-height:1.1}}
.dtw .stat .l{{font-size:.88rem;opacity:.9}}
.dtw .steps{{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:12px;counter-reset:p}}
.dtw .step{{background:#fff;border-radius:18px;padding:16px;border-top:5px solid {AZ};box-shadow:0 4px 14px rgba(6,31,64,.06)}}
.dtw .step:nth-child(2){{border-top-color:{RO}}}.dtw .step:nth-child(3){{border-top-color:{RS}}}.dtw .step:nth-child(4){{border-top-color:{AZ2}}}
.dtw .step i{{font-size:1.4rem;color:{RO}}}
.dtw .step b{{display:block;margin:6px 0 2px;color:{AZ}}}
.dtw .step span{{font-size:.92rem;color:{TX}}}
.dtw .people{{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:12px}}
.dtw .person{{display:flex;gap:12px;align-items:flex-start;background:#fff;border-radius:18px;padding:14px;border:1px solid {GR}}}
.dtw .avatar{{flex:0 0 52px;height:52px;border-radius:50%;background:linear-gradient(135deg,{RO},{RS});color:#fff;font-weight:800;font-size:1.2rem;display:flex;align-items:center;justify-content:center}}
.dtw .person:nth-child(even) .avatar{{background:linear-gradient(135deg,{AZ},#2A5BA8)}}
.dtw .person b{{color:{AZ}}}
.dtw .person span{{font-size:.92rem;color:{TX}}}
.dtw .check{{list-style:none;padding:0;margin:0}}
.dtw .check li{{background:#fff;border-radius:14px;padding:12px 14px 12px 48px;margin-bottom:10px;position:relative;border:1px solid {GR}}}
.dtw .check li:before{{content:"\\f00c";font-family:FontAwesome;position:absolute;left:14px;top:12px;width:24px;height:24px;border-radius:50%;background:{RO};color:#fff;font-size:.8rem;display:flex;align-items:center;justify-content:center}}
.dtw .check li b{{color:{AZ}}}
.dtw .badges{{display:flex;flex-wrap:wrap;gap:12px}}
.dtw .badge{{flex:1 1 120px;text-align:center;background:#fff;border-radius:18px;padding:14px 8px;border:1px solid {GR}}}
.dtw .badge .c{{width:62px;height:62px;margin:0 auto 8px;border-radius:50%;background:linear-gradient(160deg,{AZ},{AZ2});border:4px solid {RO};color:#fff;font-size:1.5rem;display:flex;align-items:center;justify-content:center}}
.dtw .badge small{{display:block;font-weight:700;color:{AZ};font-size:.82rem;line-height:1.25}}
.dtw .timeline{{border-left:4px solid {GR};margin-left:14px;padding-left:22px}}
.dtw .tl{{position:relative;margin-bottom:18px}}
.dtw .tl:before{{content:"";position:absolute;left:-33px;top:4px;width:18px;height:18px;border-radius:50%;background:{RO};border:4px solid #fff;box-shadow:0 0 0 2px {RO}}}
.dtw .tl b{{color:{AZ};display:block}}
.dtw .tl span{{color:{TX}}}
.dtw .note{{background:#FFF4FA;border:1px dashed {RS};border-radius:16px;padding:14px 16px;font-size:.95rem}}
.dtw .alert{{background:{AZ2};color:#fff;border-radius:18px;padding:18px}}
.dtw .alert b{{color:{RS}}}
.dtw .alert ul{{margin:8px 0 0;padding-left:20px}}
.dtw .post{{background:#fff;border-radius:16px;border:1px solid {GR};padding:14px;font-size:.95rem}}
.dtw .post .h{{display:flex;gap:10px;align-items:center;margin-bottom:8px;color:{TX};font-size:.85rem}}
.dtw .post .h .avatar{{flex-basis:34px;height:34px;font-size:.85rem}}
.dtw .ok{{color:#1B7F4B;font-weight:700}}.dtw .no{{color:{RO};font-weight:700}}
.dtw .cta{{display:inline-block;background:{RO};color:#fff!important;border-radius:999px;padding:12px 24px;font-weight:700;text-decoration:none;box-shadow:0 6px 16px rgba(228,0,124,.3)}}
.dtw .center{{text-align:center}}
.dtw .firma{{text-align:center;color:{TX};margin-top:24px;font-size:.9rem}}
.dtw .firma b{{display:block;color:{AZ};font-family:"Bricolage Grotesque",Figtree,sans-serif;font-size:1.2rem}}
@media (max-width:600px){{.dtw .hero{{padding:24px 18px}}.dtw .hero h2{{font-size:1.55rem}}.dtw .quote{{font-size:1rem}}}}
@media print{{.dtw .hero{{-webkit-print-color-adjust:exact;print-color-adjust:exact}}.dtw .card,.dtw .step{{break-inside:avoid}}}}
</style>"""

e = html.escape


def _personajes(D, cfg):
    if cfg.get("personajes"):
        return [(k, v) for k, v in cfg["personajes"].items()]
    out = []
    p = os.path.join(D, "apoyo", "01-bienvenida.md")
    t = open(p, encoding="utf-8").read() if os.path.exists(p) else ""
    m = re.search(r"(?ms)^## (Los personajes|Las personajes|The characters)\n(.+?)(?=^## |\Z)", t)
    if m:
        for ln in m.group(2).splitlines():
            mm = re.match(r"-\s*\*\*(.+?)\*\*:?\s*(.*)$", ln.strip())
            if mm:
                nom, d = mm.group(1).strip(), mm.group(2).strip()
                ed = re.match(r"\((\d+)\):?\s*", d)
                if ed: nom, d = f"{nom} ({ed.group(1)})", d[ed.end():]
                out.append((nom, d[:1].upper() + d[1:]))
        if out: return out
    # Si no, del manual: tabla «| **Nombre** (edad) | Perfil | Reto |» o secciones «### Nombre» con un párrafo
    p = os.path.join(D, "manual", "manual.md")
    t = open(p, encoding="utf-8").read() if os.path.exists(p) else ""
    m = re.search(r"(?ms)^## (Personajes|Characters)\n(.+?)(?=^## |^---|\Z)", t)
    if not m: return []
    corta = lambda x: " ".join(re.split(r"(?<=[.;])\s+", x.strip())[:2]).rstrip(";")
    for ln in m.group(2).splitlines():
        mm = re.match(r"\|\s*\*\*(.+?)\*\*\s*(\(\d+\))?\s*\|\s*(.+?)\s*\|", ln)
        if mm: out.append((mm.group(1) + (f" {mm.group(2)}" if mm.group(2) else ""), corta(mm.group(3))))
    if out: return out
    for nom, cuerpo in re.findall(r"(?ms)^### (.+?)\n\n(.+?)(?=^### |\Z)", m.group(2)):
        par = cuerpo.strip().split("\n\n")[0].replace("\n", " ")
        if par.startswith("-"): par = re.sub(r"^-\s*\*\*(.+?)\*\*\s*", r"\1 ", par)
        out.append((nom.strip(), corta(re.sub(r"\*\*", "", par))))
    return out


def _iconos(cfg):
    ic = {}
    for fn, tag, nom, icon in cfg.get("insignias", []):
        for m in re.findall(r"M\d+", tag): ic.setdefault(m, icon)
    return {m: ic.get(m, ICONOS_MOD[i % len(ICONOS_MOD)]) for i, m in enumerate(cfg["modulos"])}


def _nombre(cfg, m):
    return cfg.get("nombres", {}).get(m, {}).get("titulo") or re.sub(r"^(Módulo|Module) \d+\.\s*", "", cfg["modulos"][m])


def _horas(D, cfg):
    """Lecciones y horas totales (ruta rápida y completa), con el mismo cálculo que los documentos de estándares."""
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "proyecto-inclusion-financiera", "herramientas"))
    import leccion_ux3 as UX3
    n, a, b = 0, 0, 0
    for m in cfg["modulos"]:
        txt = open(os.path.join(D, "lecciones", f"{m}.md"), encoding="utf-8").read()
        for bl in re.split(r"(?m)^# (?=M\d+ U\d\d)", txt)[1:]:
            rap, prof = UX3.tiempos(UX3.parse(bl)[3]); n += 1; a += rap; b += rap + prof
    r = lambda x: round(x / 30) / 2
    return n, (r(a), r(b))


def _fmt(x):
    return str(int(x)) if x == int(x) else str(x)


def paginas(D, cfg):
    en = cfg.get("lang") == "en"
    T = (lambda es, x: x) if en else (lambda es, x: es)
    MODS = cfg["modulos"]; nm = len(MODS); ic = _iconos(cfg)
    nl, horas = _horas(D, cfg)
    B = cfg.get("bienvenida", {})
    I = cfg.get("instalacion", {})
    tit = e(cfg["titulo"])
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import extras
    enc = cfg.get("encuesta", "mx")
    pais = "us" if enc.startswith("us") else ("mx_en" if en else "mx")
    ayuda = extras.AYUDA[pais]
    ux3 = cfg.get("ux") == 3
    ins = cfg.get("insignias", [])
    presencial = "presencial" in (cfg.get("formato", "") + cfg.get("intro", "")).lower() or "in-person" in (cfg.get("formato", "") + cfg.get("intro", "")).lower()
    com = cfg.get("comunidad")
    C = cfg.get("contacto", {})
    para = cfg.get("catalogo", {}).get("para_quien") or cfg.get("publico", "")

    # ---------- Bienvenida ----------
    b1 = (f'<div class="hero"><span class="tag"><i class="fa fa-hand-peace-o"></i> {T("Bienvenida", "Welcome")}</span>'
          f'<h2>{T("Qué gusto que estés aquí", "We are so glad you are here")}</h2><p>{tit}</p></div>'
          f'<div class="quote">{e(B.get("conecta", cfg.get("intro", "")))}</div>')
    if para:
        b1 += f'<div class="note"><i class="fa fa-user-circle-o"></i> <b>{T("Este programa es para ti", "This program is for you")}:</b> {e(para)}</div>'
    b1 += f'<h3><i class="fa fa-map-signs" style="color:{RO}"></i> {T("Lo que vas a lograr", "What you will achieve")}</h3><div class="grid">'
    for i, m in enumerate(MODS, 1):
        b1 += (f'<div class="card{" rosa" if i % 2 == 0 else ""}"><div class="ic"><i class="fa {ic[m]}"></i></div><span class="num">{T("Parte", "Part")} {i}</span>'
               f'<b>{e(_nombre(cfg, m))}</b><span>{e(cfg["resultados"].get(m, ""))}</span></div>')
    b1 += "</div>"
    per = _personajes(D, cfg)
    if per:
        b1 += f'<h3><i class="fa fa-users" style="color:{RO}"></i> {T("Personas como tú te acompañan", "People like you will join you")}</h3><div class="people">'
        for n, d in per:
            nn = re.sub(r"\s*\(\d+\)", "", n)
            ini = ("·".join(x.strip()[0] for x in re.split(r" y | and ", nn)) if re.search(r" y | and ", nn)
                   else re.sub(r"^(Don|Doña|Ms\.|Mr\.)\s+", "", nn)[0]).upper()
            b1 += f'<div class="person"><div class="avatar">{e(ini)}</div><div><b>{e(n)}</b><br><span>{e(d)}</span></div></div>'
        b1 += "</div>"

    pasos = ([("fa-play-circle", T("Empieza", "Start"), T("Una situación real y lo que vas a lograr.", "A real situation and what you’ll achieve.")),
              ("fa-star", T("Lo esencial", "The essentials"), T("Lo indispensable y los errores más comunes.", "What you must know and the most common mistakes.")),
              ("fa-search-plus", T("Profundiza", "Go deeper"), T("Cuentas y casos, si quieres saber más.", "Math and cases, if you want more.")),
              ("fa-check-square-o", T("Practica", "Practice"), T("«¿Qué harías?», preguntas y tu plan de la semana.", "«What would you do?», questions and your plan for the week."))]
             if ux3 else
             [("fa-map-o", T("Portada", "Cover"), T("Una situación real y eliges tu ruta.", "A real situation, then you choose your path.")),
              ("fa-star", T("Lo esencial", "The essentials"), T("Lo indispensable, en pocos minutos.", "What you must know, in a few minutes.")),
              ("fa-search-plus", T("Profundiza", "Go deeper"), T("Ruta completa: cuentas, casos y errores comunes.", "Full path: math, cases and common mistakes.")),
              ("fa-check-square-o", T("Practica", "Practice"), T("«¿Qué harías?», preguntas y tu plan de la semana.", "«What would you do?», questions and your plan for the week."))])
    b2 = (f'<div class="hero"><span class="tag"><i class="fa fa-compass"></i> {T("Cómo funciona", "How it works")}</span>'
          f'<h2>{T("Aprende a tu ritmo, desde el celular", "Learn at your own pace, on your phone")}</h2>'
          f'<p>{T("Lecciones cortas, casos de la vida diaria y un paso concreto cada semana.", "Short lessons, everyday cases and one concrete step each week.")}</p></div>'
          f'<div class="stats"><div class="stat"><span class="n">{nm}</span><span class="l">{T("partes", "parts")}</span></div>'
          f'<div class="stat"><span class="n">{nl}</span><span class="l">{T("lecciones", "lessons")}</span></div>'
          f'<div class="stat"><span class="n">{_fmt(horas[0])}–{_fmt(horas[1])} h</span><span class="l">{T("en total, aprox.", "in total, approx.")}</span></div>'
          f'<div class="stat"><span class="n">70%</span><span class="l">{T("para aprobar cada parte", "to pass each part")}</span></div></div>'
          f'<h3><i class="fa fa-list-ol" style="color:{RO}"></i> {T("Cada lección tiene cuatro momentos", "Each lesson has four moments")}</h3><div class="steps">')
    b2 += "".join(f'<div class="step"><i class="fa {i}"></i><b>{e(t)}</b><span>{e(d)}</span></div>' for i, t, d in pasos)
    b2 += (f'</div><div class="note" style="margin-top:14px"><i class="fa fa-clock-o"></i> {T("Te sugerimos unas <b>2 horas por semana</b>. Puedes intentar cada autoevaluación las veces que quieras.", "We suggest about <b>2 hours a week</b>. You can retake each self-assessment as many times as you want.")}</div>'
           f'<h3><i class="fa fa-trophy" style="color:{RO}"></i> {T("Puntos, insignias y constancia", "Points, badges and certificate")}</h3>'
           f'<p>{T("Cada actividad suma puntos y subes de nivel. Estas son las insignias que puedes ganar:", "Every activity earns points and you level up. These are the badges you can earn:")}</p><div class="badges">')
    b2 += "".join(f'<div class="badge"><div class="c"><i class="fa {icon}"></i></div><small>{e(nom)}</small></div>' for fn, tag, nom, icon in ins)
    b2 += (f'</div><p style="margin-top:12px">{T("Al aprobar todo y responder la encuesta final recibes tu <b>constancia de conclusión</b>: un reconocimiento educativo, verificable en línea.", "When you pass everything and answer the final survey you receive your <b>certificate of completion</b>: an educational recognition that can be verified online.")}</p>')

    # ---------- Guía de contacto y comunidad ----------
    canales = [("fa-comments", T("Foro «Dudas y comentarios»", "«Questions and comments» forum"),
                T("Para dudas de las lecciones. Te responde el equipo y también otras personas del grupo.", "For questions about the lessons. The team and others in the group answer."), ""),
               ("fa-envelope-o", T("Mensaje privado al equipo", "Private message to the team"),
                T("Para algo personal o un problema con la plataforma: en el ícono de mensajes, busca al equipo del curso.", "For something personal or a platform problem: open the messages icon and find the course team."), " rosa")]
    if com:
        canales.append(("fa-users", e(com.get("titulo", T("Comunidad", "Community"))),
                        T("Un espacio aparte para alertas de fraude, avisos, sesiones en vivo y conocer a más personas como tú.", "A separate space for scam alerts, news, live sessions and meeting more people like you."), ""))
    if presencial:
        canales.append(("fa-handshake-o", T("Sesiones presenciales", "In-person sessions"),
                        T("Pregunta en persona a quien facilita; también ahí resolvemos dudas de la plataforma.", "Ask the facilitator in person; we also solve platform questions there."), " rosa"))
    if C.get("whatsapp"):
        canales.append(("fa-whatsapp", "WhatsApp", e(C["whatsapp"]) + (f" · {e(C['horario'])}" if C.get("horario") else ""), ""))
    if C.get("correo"):
        canales.append(("fa-envelope", T("Correo", "Email"), f'<a href="mailto:{e(C["correo"])}">{e(C["correo"])}</a> · ' + T("para lo que no quieras escribir en el foro.", "for anything you’d rather not post in the forum."), " rosa"))
    g = (f'<div class="hero"><span class="tag"><i class="fa fa-life-ring"></i> {T("Guía de contacto y comunidad", "Contact and community guide")}</span>'
         f'<h2>{T("No estás sola ni solo en esto", "You are not alone in this")}</h2>'
         f'<p>{T("Aquí te decimos dónde preguntar, cómo participar y cómo cuidamos tus datos.", "Here is where to ask, how to take part and how we protect your data.")}</p></div>'
         f'<h3><i class="fa fa-commenting-o" style="color:{RO}"></i> {T("¿Dónde pregunto?", "Where do I ask?")}</h3><div class="grid">')
    g += "".join(f'<div class="card{c}"><div class="ic"><i class="fa {i}"></i></div><b>{t}</b><span>{d}</span></div>' for i, t, d, c in canales)
    g += (f'</div><div class="note" style="margin-top:14px"><i class="fa fa-clock-o"></i> {T("Respondemos en <b>48 horas hábiles</b> o menos.", "We reply within <b>2 business days</b> or less.")}</div>'
          f'<h3><i class="fa fa-pencil" style="color:{RO}"></i> {T("Cómo escribir en el foro", "How to post in the forum")}</h3><div class="steps">'
          f'<div class="step"><i class="fa fa-hand-pointer-o"></i><b>1. {T("Entra al foro", "Open the forum")}</b><span>{T("Está arriba de las partes del curso.", "It is above the course parts.")}</span></div>'
          f'<div class="step"><i class="fa fa-plus-circle"></i><b>2. {T("«Añadir un nuevo tema»", "«Add a new discussion topic»")}</b><span>{T("Escribe un asunto corto: «Duda de la lección de crédito».", "Write a short subject: «Question about the credit lesson».")}</span></div>'
          f'<div class="step"><i class="fa fa-paper-plane"></i><b>3. {T("Pregunta y envía", "Ask and send")}</b><span>{T("Con números inventados o redondeados. Te llega aviso cuando respondan.", "Use made-up or rounded numbers. You’ll be notified when someone replies.")}</span></div></div>'
          f'<div class="grid" style="margin-top:14px"><div class="post"><div class="h"><div class="avatar">AM</div>{T("Así sí", "Like this")} <span class="ok"><i class="fa fa-check"></i></span></div>'
          f'{T("«Si me cobran 120 al mes de comisión, ¿cómo pido la cuenta básica?»", "«If they charge me 120 a month in fees, how do I ask for the basic account?»")}</div>'
          f'<div class="post"><div class="h"><div class="avatar">RC</div>{T("Así no", "Not like this")} <span class="no"><i class="fa fa-times"></i></span></div>'
          f'{T("«Mi número de cuenta es 0123… y mi NIP es…»", "«My account number is 0123… and my PIN is…»")}</div></div>'
          f'<h3><i class="fa fa-shield" style="color:{RO}"></i> {T("Reglas de oro", "Golden rules")}</h3><ul class="check">'
          f'<li><b>{T("Tus datos son tuyos", "Your data is yours")}:</b> {e(I.get("aviso_foro", T("No compartas números de cuenta, NIP, contraseñas ni documentos.", "Don’t share account numbers, PINs, passwords or documents.")))}</li>'
          f'<li><b>{T("Nadie del equipo te pedirá", "No one on the team will ask for")}</b> {T("datos personales, contraseñas ni dinero. Si alguien lo hace a nuestro nombre, es fraude.", "personal data, passwords or money. If someone does it in our name, it’s fraud.")}</li>'
          f'<li><b>{T("Respeto siempre", "Always respectful")}:</b> {T("sin juicios, sin ventas y sin publicidad.", "no judging, no selling and no ads.")}</li>'
          f'<li><b>{T("Lo que cuentas es confidencial", "What you share is confidential")}:</b> {T("la organización que te ofrece el curso no recibe tus datos personales ni financieros.", "the organization offering the course does not receive your personal or financial data.")}</li></ul>'
          f'<h3><i class="fa fa-heartbeat" style="color:{RO}"></i> {T("Si necesitas ayuda urgente", "If you need urgent help")}</h3>'
          f'<div class="alert"><b>{T("No esperes al foro:", "Don’t wait for the forum:")}</b><ul>' + "".join(f"<li>{e(x)}</li>" for x in ayuda) + "</ul></div>")

    b4 = (f'<div class="hero"><span class="tag"><i class="fa fa-rocket"></i> {T("Antes de empezar", "Before you start")}</span>'
          f'<h2>{T("Tres pasos y arrancamos", "Three steps and we are off")}</h2><p>{T("Te toman unos 15 minutos.", "They take about 15 minutes.")}</p></div><div class="steps">'
          f'<div class="step"><i class="fa fa-bar-chart"></i><b>1. {T("Encuesta de inicio", "Start survey")}</b><span>{T("Anónima. Nos dice cómo estás hoy para medir tu avance al final.", "Anonymous. It tells us how you are today so we can measure your progress.")}</span></div>'
          f'<div class="step"><i class="fa fa-lightbulb-o"></i><b>2. {T("Tu punto de partida", "Your starting point")}</b><span>{T("Unas preguntas rápidas para saber qué ya sabes. No es examen y no cuenta para tu calificación.", "A few quick questions about what you already know. It’s not a test and it doesn’t count toward your grade.")}</span></div>'
          f'<div class="step"><i class="fa fa-comment-o"></i><b>3. {T("Preséntate", "Introduce yourself")}</b><span>{T("En el foro, con tu nombre o apodo: ¿qué esperas de este programa?", "In the forum, with your name or a nickname: what do you expect from this program?")}</span></div></div>'
          f'<div class="note" style="margin-top:16px"><i class="fa fa-bookmark-o"></i> {T("Escribe tu meta en una frase y guárdala en tu celular. La volverás a ver al final.", "Write your goal in one sentence and save it on your phone. You’ll see it again at the end.")}</div>'
          f'<p class="center" style="margin-top:22px"><span class="cta"><i class="fa fa-play"></i> {T("Ahora sí: ve a la Parte 1", "Now go to Part 1")} · {e(_nombre(cfg, list(MODS)[0]))}</span></p>'
          f'<div class="firma"><div class="marca">{LOGO}</div>{T("Programa de bienestar financiero", "Financial well-being program")}</div>')

    bienvenida = [("01_bienvenida.html", T("Te damos la bienvenida", "Welcome"), b1),
                  ("02_bienvenida.html", T("Cómo funciona el curso", "How the course works"), b2),
                  ("03_bienvenida.html", T("Guía de contacto y comunidad", "Contact and community guide"), g),
                  ("04_bienvenida.html", T("Antes de empezar", "Before you start"), b4)]

    # ---------- Cierre y despedida ----------
    c1 = (f'<div class="hero"><span class="tag"><i class="fa fa-flag-checkered"></i> {T("Conclusión", "Conclusion")}</span>'
          f'<h2>{T("Mira todo lo que lograste", "Look at everything you achieved")}</h2>'
          f'<p>{T(f"Recorriste {nm} partes y {nl} lecciones. Esto es lo que ahora tienes:", f"You went through {nm} parts and {nl} lessons. This is what you have now:")}</p></div><ul class="check">')
    c1 += "".join(f'<li><b>{e(_nombre(cfg, m))}.</b> {e(cfg["resultados"].get(m, ""))}</li>' for m in MODS)
    c1 += (f'</ul><h3><i class="fa fa-trophy" style="color:{RO}"></i> {T("Tus insignias", "Your badges")}</h3><div class="badges">'
           + "".join(f'<div class="badge"><div class="c"><i class="fa {icon}"></i></div><small>{e(nom)}</small></div>' for fn, tag, nom, icon in ins) + "</div>"
           f'<div class="note" style="margin-top:16px"><i class="fa fa-bookmark-o"></i> {T("¿Te acuerdas de la meta que escribiste al empezar? Léela otra vez: ¿qué cambió?", "Remember the goal you wrote at the start? Read it again: what changed?")}</div>')
    c2 = (f'<div class="hero"><span class="tag"><i class="fa fa-road"></i> {T("Lo que sigue", "What comes next")}</span>'
          f'<h2>{T("Tu plan sigue después del curso", "Your plan continues after the course")}</h2>'
          f'<p>{T("Lo importante pasa en las próximas semanas. Así lo mantienes vivo:", "What matters happens in the coming weeks. Here is how to keep it alive:")}</p></div><div class="timeline">'
          f'<div class="tl"><b>{T("Esta semana", "This week")}</b><span>{T("Da el primer paso de tu plan de una página y ponle fecha al segundo.", "Take the first step of your one-page plan and put a date on the second.")}</span></div>'
          f'<div class="tl"><b>{T("Cada mes", "Every month")}</b><span>{T("Revisa tu plan en una fecha fija y tacha lo que avanzaste.", "Review your plan on a set date and cross off your progress.")}</span></div>'
          f'<div class="tl"><b>{T("A los 30 días", "At 30 days")}</b><span>{T("Te llega una encuesta corta y anónima: cuéntanos cómo vas.", "You’ll get a short, anonymous survey: tell us how you’re doing.")}</span></div>'
          f'<div class="tl"><b>{T("A los 90 días", "At 90 days")}</b><span>{T("Otra encuesta corta para ver qué cambió de verdad.", "Another short survey to see what really changed.")}</span></div></div>'
          f'<h3><i class="fa fa-unlock" style="color:{RO}"></i> {T("Lo que se queda contigo", "What stays with you")}</h3><div class="grid">'
          f'<div class="card"><div class="ic"><i class="fa fa-book"></i></div><b>{T("Las lecciones", "The lessons")}</b><span>{T("Puedes volver a ellas cuando quieras.", "You can come back to them anytime.")}</span></div>'
          f'<div class="card rosa"><div class="ic"><i class="fa fa-file-excel-o"></i></div><b>{T("Tus herramientas", "Your tools")}</b><span>{T("El Excel y el libro de apoyo son tuyos.", "The Excel file and the support book are yours.")}</span></div>'
          f'<div class="card"><div class="ic"><i class="fa fa-comments"></i></div><b>{T("El foro", "The forum")}</b><span>{T("Sigue abierto para tus dudas.", "It stays open for your questions.")}</span></div></div>')
    c3 = (f'<div class="hero"><span class="tag"><i class="fa fa-certificate"></i> {T("Tu constancia", "Your certificate")}</span>'
          f'<h2>{T("Dos pasos para tu constancia", "Two steps to your certificate")}</h2><p>{T("Ya casi.", "Almost there.")}</p></div><div class="steps">'
          f'<div class="step"><i class="fa fa-bar-chart"></i><b>1. {T("Encuesta final", "Final survey")}</b><span>{T("Anónima, unos 5 minutos. Nos ayuda a mejorar y a mostrar que el programa funciona.", "Anonymous, about 5 minutes. It helps us improve and show that the program works.")}</span></div>'
          f'<div class="step"><i class="fa fa-download"></i><b>2. {T("Descarga tu constancia", "Download your certificate")}</b><span>{T("Se libera al terminar la encuesta. Es un reconocimiento educativo, verificable en línea.", "It unlocks when you finish the survey. It’s an educational recognition that can be verified online.")}</span></div></div>')
    correo_txt = (f'; {T("escríbenos también a", "you can also write to")} <a href="mailto:{e(C["correo"])}">{e(C["correo"])}</a>') if C.get("correo") else ""
    c4 = (f'<div class="hero center"><div class="logo">{LOGO}</div>'
          f'<h2>{T("¡Gracias y hasta pronto!", "Thank you, and see you soon!")}</h2><p>{tit}</p></div>'
          f'<div class="quote">{e(B.get("despedida", ""))}</div><div class="grid">'
          f'<div class="card rosa"><div class="ic"><i class="fa fa-share-alt"></i></div><b>{T("Compártelo", "Share it")}</b><span>{T("¿Conoces a alguien a quien le serviría? Cuéntale del programa; es sin costo para quien participa.", "Know someone who could use it? Tell them about the program; there is no cost to participants.")}</span></div>'
          f'<div class="card"><div class="ic"><i class="fa fa-envelope-o"></i></div><b>{T("Seguimos en contacto", "Let’s stay in touch")}</b><span>{T("El foro y los mensajes al equipo siguen abiertos", "The forum and team messages stay open")}{correo_txt}.</span></div>'
          f'<div class="card rosa"><div class="ic"><i class="fa fa-star"></i></div><b>{T("Celebra", "Celebrate")}</b><span>{T("Comparte tu insignia o tu constancia si quieres: son el reconocimiento a tu esfuerzo y tu constancia.", "Share your badge or certificate if you want: they recognize your effort and persistence.")}</span></div></div>'
          f'<div class="firma"><div class="marca">{LOGO}</div>{T("Reconocemos tu esfuerzo y tu constancia · Programa de bienestar financiero", "We recognize your effort and persistence · Financial well-being program")}</div>')
    cierre = [("01_cierre.html", T("Lo que lograste", "What you achieved"), c1),
              ("02_cierre.html", T("Tu plan sigue", "Your plan continues"), c2),
              ("03_cierre.html", T("Encuesta final y constancia", "Final survey and certificate"), c3),
              ("04_cierre.html", T("Hasta pronto", "See you soon"), c4)]
    return bienvenida, cierre, g


HEAD = ('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">'
        '<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800&family=Figtree:wght@400;500;600;700&display=swap" rel="stylesheet">')


def preview(pags, d, en):
    """Vista previa navegable (así se verá cada capítulo en el Libro de Moodle)."""
    os.makedirs(d, exist_ok=True)
    nav = "".join(f'<a href="{fn}">{e(t)}</a>' for fn, t, b in pags)
    for i, (fn, t, b) in enumerate(pags):
        sig = f'<p class="center" style="margin:26px 0"><a class="cta" href="{pags[i + 1][0]}">{e(pags[i + 1][1])} <i class="fa fa-arrow-right"></i></a></p>' if i + 1 < len(pags) else ""
        open(os.path.join(d, fn), "w", encoding="utf-8").write(
            f'<!DOCTYPE html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{e(t)}</title>{HEAD}'
            f'<style>body{{background:{FO};margin:0;font-family:Figtree,system-ui,sans-serif}}.nav{{background:#fff;border-bottom:1px solid {GR};padding:10px 16px;display:flex;gap:14px;flex-wrap:wrap;font-size:.85rem}}'
            f'.nav small{{color:{TX};width:100%}}.nav a{{color:{AZ};font-weight:600;text-decoration:none}}.wrap{{padding:16px}}</style>{CSS}</head><body>'
            f'<div class="nav"><small>{"PREVIEW · how it will look in the Moodle Book" if en else "VISTA PREVIA · así se verá en el Libro de Moodle"}</small>{nav}</div>'
            f'<div class="wrap"><div class="dtw">{b}{sig}</div></div></body></html>')
    open(os.path.join(d, "ABRIR_AQUI.html"), "w").write(f'<meta http-equiv="refresh" content="0; url={pags[0][0]}">')


def diagnostica_en(D, cfg, out):
    """«Your starting point» en inglés: mismas reglas que estandares.py (primera pregunta de cada lección, 2 por módulo)."""
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "proyecto-inclusion-financiera", "herramientas"))
    import leccion_ux3 as UX3
    g, k = f"$CATEGORY: $course$/{cfg.get('categoria', cfg['titulo'])}/Start\n\n", 0
    esc = lambda t: re.sub(r"([~=#{}:])", r"\\\1", t)
    for m in cfg["modulos"]:
        txt = open(os.path.join(D, "lecciones", f"{m}.md"), encoding="utf-8").read()
        cand = []
        for bl in re.split(r"(?m)^# (?=M\d+ U\d\d)", txt)[1:]:
            secs = UX3.parse(bl)[3]
            pr = dict((kk, c) for kk, _, _, c in UX3.blocks(secs.get("practica", "")))
            cand += UX3.quiz_items(pr)[:1]
        paso = max(1, len(cand) // 2)
        for q, opts, key, _ in cand[::paso][:2]:
            k += 1
            g += f"::DIAG {k}::{esc(q)} {{\n" + "".join(f"\t{'=' if chr(97 + j) == key else '~'}{esc(o)}\n" for j, o in enumerate(opts)) + "}\n\n"
    open(os.path.join(out, "diagnostica.gift.txt"), "w", encoding="utf-8").write(g)
    return k


def generar(D, cfg, out):
    en = cfg.get("lang") == "en"
    bien, cierre, guia = paginas(D, cfg)
    res = []
    for carpeta, zipn, pags in (("Bienvenida", "Bienvenida_libro_Moodle.zip", bien), ("Cierre", "Cierre_libro_Moodle.zip", cierre)):
        d = os.path.join(out, carpeta); shutil.rmtree(d, ignore_errors=True); os.makedirs(d)
        with zipfile.ZipFile(os.path.join(d, zipn), "w", zipfile.ZIP_DEFLATED) as zf:
            for fn, t, body in pags:
                doc = f'<!DOCTYPE html><html><head><meta charset="utf-8"><title>{e(t)}</title></head><body>{CSS}<div class="dtw">{body}</div></body></html>'
                open(os.path.join(d, fn), "w", encoding="utf-8").write(doc); zf.write(os.path.join(d, fn), fn)
        preview(pags, os.path.join(d, "vista_previa"), en)
        res.append(f"{carpeta}: {len(pags)} capítulos")
    # Guía para imprimir o compartir (una página independiente)
    nom = "Contact_and_community_guide.html" if en else "Guia_de_contacto_y_comunidad.html"
    open(os.path.join(out, "Bienvenida", nom), "w", encoding="utf-8").write(
        f'<!DOCTYPE html><html lang="{"en" if en else "es"}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
        f'<title>{"Contact and community guide" if en else "Guía de contacto y comunidad"}</title>'
        f'{HEAD}<style>body{{background:{FO};margin:0;padding:16px}}</style>{CSS}</head><body><div class="dtw">{guia}'
        f'<div class="firma"><div class="marca">{LOGO}</div>{e(cfg["titulo"])}</div></div></body></html>')
    if en: res.append(f"your starting point: {diagnostica_en(D, cfg, out)} items")
    return res + [nom]


if __name__ == "__main__":
    D = os.path.abspath(sys.argv[1])
    cfg = json.load(open(os.path.join(D, "curso.json"), encoding="utf-8"))
    print(", ".join(generar(D, cfg, os.path.join(D, "moodle"))))
