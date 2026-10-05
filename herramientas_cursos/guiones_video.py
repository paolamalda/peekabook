# Genera el guion visual de un video corto por lección («Lo esencial» animado, con texto breve en pantalla).
# Uso: python3 herramientas_cursos/guiones_video.py cursos/<carpeta> [...]
# Salida: cursos/<carpeta>/videos/guiones_videos.md (borrador para revisar; no sobrescribe guiones hechos a mano
# si el archivo empieza con «<!-- manual -->»).
import os, re, sys, json

ICONOS = {
    "fa-money": "monedas y billetes", "fa-calculator": "una calculadora con la cuenta", "fa-calendar": "un calendario",
    "fa-calendar-check-o": "un calendario con una fecha marcada", "fa-clock-o": "un reloj", "fa-shield": "un escudo",
    "fa-lock": "un candado", "fa-university": "un banco", "fa-mobile": "un celular", "fa-phone": "un teléfono",
    "fa-search": "una lupa", "fa-balance-scale": "una balanza", "fa-handshake-o": "un apretón de manos",
    "fa-file-text": "un documento", "fa-file-text-o": "un documento", "fa-id-card": "una identificación",
    "fa-id-card-o": "una identificación", "fa-home": "una casa", "fa-heart": "un corazón", "fa-users": "un grupo de personas",
    "fa-percent": "un signo de porcentaje", "fa-line-chart": "una gráfica que sube", "fa-exchange": "dos flechas de ida y vuelta",
    "fa-refresh": "flechas en círculo", "fa-exclamation-triangle": "una señal de alerta", "fa-exclamation-circle": "una señal de alerta",
    "fa-ban": "una señal de prohibido", "fa-life-ring": "un salvavidas", "fa-question-circle": "un signo de pregunta",
    "fa-comments": "dos globos de conversación", "fa-user-secret": "una figura sospechosa", "fa-globe": "un globo terráqueo",
    "fa-list": "una lista", "fa-list-ol": "una lista numerada", "fa-check-square-o": "una lista con palomitas",
    "fa-lightbulb-o": "un foco encendido", "fa-trophy": "un trofeo", "fa-folder-open": "una carpeta abierta",
    "fa-bullhorn": "un altavoz", "fa-credit-card": "una tarjeta", "fa-piggy-bank": "una alcancía", "fa-bus": "un autobús",
    "fa-plane": "un avión", "fa-car": "un auto", "fa-motorcycle": "una moto", "fa-bicycle": "una bicicleta", "fa-truck": "una camioneta",
    "fa-leaf": "una hoja", "fa-flag": "una bandera", "fa-gift": "un regalo", "fa-wrench": "una herramienta", "fa-medkit": "un botiquín",
    "fa-shopping-bag": "una bolsa de compras", "fa-shopping-basket": "una canasta", "fa-briefcase": "un portafolio",
    "fa-pie-chart": "una gráfica de pastel", "fa-th-large": "tarjetas", "fa-sign-in": "una flecha que entra",
    "fa-undo": "una flecha de regreso", "fa-envelope": "un sobre", "fa-pencil": "un lápiz", "fa-star": "una estrella",
}
T = {"es": dict(tit="Guiones visuales", sub="Un video corto por lección: «Lo esencial» animado, con texto breve en pantalla. Borrador generado desde el contenido de cada lección; revisar antes de producir.",
                reglas="""## Reglas para todos los videos

- **Duración:** 40 a 55 segundos; 6 a 8 escenas; una idea por escena.
- **Estructura fija:** título → la situación → lo esencial (2 a 3 ideas) → el error que más cuesta (✕) → lo que hizo el personaje (✓) → la idea clave.
- **Texto en pantalla:** una frase corta por escena, letra grande, máximo dos renglones en celular. Sin voz obligatoria; si se graba voz, lee el mismo texto.
- **Formato:** 16:9 para Moodle; copia 1:1 para WhatsApp. MP4 de menos de 2 MB. Subtítulos incluidos en la imagen.
- **Señales fijas:** ✓ azul marino = así sí; ✕ magenta = así no; monedas doradas = dinero; candado = protegido; lupa = revisar.
- **Personajes:** los del curso, con el elenco que se decida (personas o animales).
- **Estándar EC0366:** cada video cuenta como material multimedia con título, desarrollo del tema e imágenes.
""", col=("#", "Seg.", "Qué se ve", "Texto en pantalla"), titulo="Título", sit="La situación", err="Cuidado", res="Así lo resolvió", clave="Idea clave",
                debe="Debe entenderse", personaje="Personaje"),
     "en": dict(tit="Visual scripts", sub="One short video per lesson: an animated «The essentials», with brief on-screen text. Draft generated from each lesson; review before production.",
                reglas="""## Rules for every video

- **Length:** 40 to 55 seconds; 6 to 8 scenes; one idea per scene.
- **Fixed structure:** title → the situation → the essentials (2 to 3 ideas) → the costliest mistake (✕) → what the character did (✓) → key idea.
- **On-screen text:** one short sentence per scene, large type, two lines max on a phone. No voice required; if recorded, it reads the same text.
- **Format:** 16:9 for Moodle; 1:1 copy for WhatsApp. MP4 under 2 MB. Captions burned in.
- **Fixed signals:** navy ✓ = do this; magenta ✕ = don't; gold coins = money; padlock = protected; magnifier = check.
- **Characters:** the course characters, with the cast to be decided.
- **EC0366 standard:** each video counts as multimedia material with title, topic development and images.
""", col=("#", "Sec.", "What we see", "On-screen text"), titulo="Title", sit="The situation", err="Watch out", res="How they solved it", clave="Key idea",
                debe="Must be understood", personaje="Character")}


def limpia(s):
    s = re.sub(r"\{\{([^|}]+)\|[^}]+\}\}", r"\1", s)
    s = re.sub(r"\*\*|\*|`", "", s)
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
    return re.sub(r"\s+", " ", s).strip()


def frase(s, n=110):
    s = limpia(s)
    m = re.match(r"(.+?[.!?])(\s|$)", s)
    s = m.group(1) if m else s
    if len(s) > n:
        s = s[:n].rsplit(" ", 1)[0].rstrip(",;:") + "…"
    return s


def bloques(body):
    out = []
    for b in re.split(r"(?m)^--- ", body)[1:]:
        head, content = (b.split("\n", 1) + [""])[:2]
        parts = [p.strip() for p in head.split("|")]
        out.append((parts[0], parts[1] if len(parts) > 1 else "", parts[2] if len(parts) > 2 else "", content.strip()))
    return out


CONOCIDOS = set()


def candidatos(texto):
    """Nombres que se repiten en los ganchos del curso: así se descartan palabras sueltas con mayúscula."""
    from collections import Counter
    c = Counter()
    for g in re.findall(r"(?m)^gancho:\s*(.+)$", texto):
        for m in re.finditer(r"(?:(?:Don|Doña|Doctora|Doctor)\s+)?[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+(?:\s+Carlos)?", limpia(g)):
            c[m.group(0)] += 1
    return {k for k, v in c.items() if v >= 2}


def leccion(block, lang, personajes):
    L = T[lang]
    head, rest = block.split("\n", 1)
    code, title = [x.strip() for x in head.split("|", 1)]
    meta = dict(re.findall(r"(?m)^(objetivo|gancho):\s*(.+)$", rest))
    secs = {}
    for part in re.split(r"(?m)^== ", rest)[1:]:
        name, body = part.split("\n", 1); secs[name.strip()] = body
    ess = bloques(secs.get("esencial", ""))
    gancho = limpia(meta.get("gancho", ""))
    STOP = {"A", "Al", "El", "La", "Los", "Las", "Un", "Una", "En", "Cada", "Cuando", "Si", "Hace", "Desde", "Con", "Para", "Por", "Hoy", "Este", "Esta",
            "The", "A", "An", "In", "When", "Every", "Each", "If", "Last", "This", "Since", "For", "Today", "Mexico", "México", "Estados", "Unidos", "California"}
    quien = next((p for p in personajes if p.split()[-1] in gancho), None)
    if not quien:
        for m in re.finditer(r"(?:(?:Don|Doña|Doctora|Doctor)\s+)?[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+(?:\s+Carlos)?", gancho):
            if m.group(0) not in STOP and m.group(0).split()[-1] not in STOP and (not CONOCIDOS or m.group(0) in CONOCIDOS): quien = m.group(0); break
    clave = ""
    m = re.search(r"\*\*(?:Idea clave|Key idea):\*\*\s*(.+)", secs.get("esencial", ""))
    if m: clave = limpia(m.group(1)); clave = clave[:1].upper() + clave[1:]
    caso = next((c for k, ic, t, c in ess if k == "paso" and ic == "fa-user"), "")
    caso = re.sub(r"(?ms)^>.*$", "", caso)
    ideas = [b for b in ess if b[0] in ("paso", "tarjetas", "ecuacion", "pasos") and b[1] != "fa-user"][:3]
    errs = []
    for k, _, _, c in bloques(secs.get("profundiza", "")):
        if k == "errores":
            errs = [[x.strip() for x in re.split(r"\|(?![^{]*\}\})", l[2:])] for l in c.splitlines() if l.startswith("* ")]
    filas, t = [], 0
    def fila(dur, ve, txt):
        nonlocal t
        filas.append((len(filas), f"{t}–{t + dur}", ve, txt)); t += dur
    fila(3, f"Fondo azul marino; {ICONOS.get(ideas[0][1], 'el ícono del tema') if ideas else 'el ícono del tema'} y el título." if lang == "es" else "Navy background, topic icon and title.", limpia(title))
    sit_txt = frase(gancho, 120)
    fila(7, (f"{quien or 'El personaje'} en su día a día: " if lang == "es" else f"{quien or 'The character'} in daily life: ") + frase(gancho, 160), sit_txt)
    for k, ic, tt, c in ideas:
        vis = ICONOS.get(ic, "una ilustración del tema")
        if k == "tarjetas":
            items = [limpia(re.split(r"\|(?![^{]*\}\})", l[2:])[1]) for l in c.splitlines() if l.startswith("* ")]
            ve = (f"Aparecen {len(items)} tarjetas, una por una: " if lang == "es" else f"{len(items)} cards appear one by one: ") + ", ".join(items) + "."
            txt = limpia(tt)
            fila(8, ve, txt)
        elif k == "ecuacion":
            eq = [l for l in c.splitlines() if re.match(r"^[=\-+×÷] ", l)]
            partes = [f"{l[0] if i else ''} {limpia(l[2:].split('|')[0])} ({limpia(l[2:].split('|')[1])})".strip() for i, l in enumerate(eq)]
            ve = ("Los números aparecen uno por uno, con monedas que se suman o se quitan: " if lang == "es" else "Numbers appear one by one, with coins added or removed: ") + " ".join(partes) + "."
            fila(8, ve, limpia(tt))
        elif k == "pasos":
            items = [limpia(x) for x in re.findall(r"(?m)^\d+\.\s+(.+)$", c)][:4]
            ve = ("Una lista que se va palomeando: " if lang == "es" else "A checklist being ticked: ") + "; ".join(frase(x, 60) for x in items) + "."
            fila(7, ve, limpia(tt))
        else:
            ve = (f"{vis[:1].upper() + vis[1:]} en grande; " if lang == "es" else "Large icon; ") + frase(c, 140)
            fila(7, ve, frase(c, 100))
    if errs:
        e, p = errs[0][0], errs[0][1]
        fila(6, ("✕ magenta sobre la escena: " if lang == "es" else "Magenta ✕ over the scene: ") + f"{limpia(e)} → {limpia(p)}.", f"✕ {limpia(e)}")
    if caso:
        fila(7, (f"{quien or 'El personaje'} lo resuelve: " if lang == "es" else f"{quien or 'The character'} solves it: ") + frase(caso, 160), frase(caso, 100))
    fila(5, ("✓ azul marino grande y la idea clave." if lang == "es" else "Large navy ✓ and the key idea."), clave or frase(meta.get("objetivo", ""), 100))
    md = [f"### {code} · {limpia(title)}", f"**{L['debe']}:** {limpia(meta.get('objetivo', ''))}" + (f" · **{L['personaje']}:** {quien}" if quien else ""), "",
          "| " + " | ".join(L["col"]) + " |", "|---|---|---|---|"]
    md += [f"| {n} | {s} | {v.replace('|', '/')} | {x.replace('|', '/')} |" for n, s, v, x in filas]
    return "\n".join(md) + "\n", t


def curso(D):
    cfg = json.load(open(os.path.join(D, "curso.json"), encoding="utf-8"))
    lang = "en" if cfg.get("lang") == "en" else "es"
    L = T[lang]
    out = os.path.join(D, "videos", "guiones_videos.md")
    if os.path.exists(out) and open(out, encoding="utf-8").read().startswith("<!-- manual -->"):
        print(os.path.basename(D), "· guiones hechos a mano: no se tocan"); return
    pers = list((cfg.get("personajes") or {}).keys())
    todo = "".join(open(os.path.join(D, "lecciones", f"{m}.md"), encoding="utf-8").read() for m in cfg["modulos"])
    CONOCIDOS.clear(); CONOCIDOS.update(candidatos(todo) - {"El", "La", "Los", "Las", "En", "A", "Cuando", "Cada", "The", "When", "Each", "In", "Si", "Hace", "Una", "Un", "California", "México", "Mexico", "Estados", "Unidos", "Sinaloa", "Canadá", "Canada", "Ontario", "He", "She", "Whats", "WhatsApp", "Fresno", "Zelle", "Venmo", "Banco", "Bienestar", "App"})
    partes, n, tot = [], 0, 0
    for mod, mt in cfg["modulos"].items():
        txt = open(os.path.join(D, "lecciones", f"{mod}.md"), encoding="utf-8").read()
        partes.append(f"## {cfg.get('nombres', {}).get(mod, {}).get('titulo', mt)}\n")
        for b in re.split(r"(?m)^# (?=M\d+ U\d\d)", txt)[1:]:
            md, s = leccion(b, lang, pers); partes.append(md); n += 1; tot += s
    os.makedirs(os.path.dirname(out), exist_ok=True)
    head = f"# {L['tit']} · {cfg['titulo']} · {n} videos\n\n{L['sub']}\n\n{L['reglas']}\n"
    open(out, "w", encoding="utf-8").write(head + "\n".join(partes))
    print(f"{os.path.basename(D)} · {n} guiones · {tot // 60} min en total")


if __name__ == "__main__":
    for d in sys.argv[1:]: curso(os.path.abspath(d))
