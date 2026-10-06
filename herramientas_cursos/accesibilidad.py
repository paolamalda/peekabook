# Revisión de accesibilidad y legibilidad de todas las lecciones (E06 del plan maestro).
# Mide por lección: legibilidad (INFLESZ en español, Flesch en inglés), frases y párrafos largos, siglas sin explicar,
# enlaces sin descripción y tiempo de lectura de «Lo esencial». Además revisa el contraste de los colores de los libros (WCAG 2.1).
# Uso: python3 herramientas_cursos/accesibilidad.py   → proyecto-inclusion-financiera/entregables/auditoria_accesibilidad.md y .csv
import os, re, glob, json, csv, statistics as st

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "proyecto-inclusion-financiera", "entregables")
FRASE_LARGA, PARRAFO_LARGO = 25, 60
VOC = "aeiouáéíóúüy"

# Siglas que se dan por conocidas en México y EE. UU., o que son nombres propios de instituciones que se presentan en la lección
SIGLAS_COMUNES = {"III", "BANCO", "XVI", "XVIII", "XXIX", "XXII", "XXIII", "START", "GAMBLER", "IMSS", "ISSSTE", "INE", "CURP", "RFC", "SAT", "NIP", "PIN", "CLABE", "SPEI", "CAT", "IVA", "ISR", "UMA", "EE", "UU", "USA",
                  "OK", "PDF", "SMS", "APP", "ID", "IRS", "SSN", "ITIN", "TV", "DIF", "INAPAM", "CDMX", "CONDUSEF", "PROFECO", "SIPRES",
                  "CONSAR", "AFORE", "INFONAVIT", "FONACOT", "MX", "US", "U", "S", "M", "W", "DC", "QR", "IA", "AI", "LLC", "FDIC", "NCUA",
                  "CFPB", "FTC", "ATM", "ACH", "EIN", "CPA", "HUD", "PTAT", "SIN", "CPP", "EI", "H", "A", "K", "CRA", "RAN", "SNE", "STPS",
                  "PROFEDET", "CONOCER", "SEGOB", "INM", "SRE", "SEP", "FINABIEN", "SSA", "UMAS", "BURÓ", "FICO", "VISA", "NSS", "SGMM"}


def silabas(w, en):
    w = w.lower()
    if en:
        w = re.sub(r"(?:[^laeiouy]es|ed|[^laeiouy]e)$", "", w) or w
        return max(1, len(re.findall(r"[aeiouy]+", w)))
    # Español: grupos vocálicos; dos vocales fuertes seguidas (a, e, o) forman hiato
    n = len(re.findall(f"[{VOC}]+", w))
    n += len(re.findall(r"[aeoáéó](?=[aeoáéó])", w))
    n += len(re.findall(r"[íú](?=[aeo])|[aeo](?=[íú])", w))
    return max(1, n)


def limpia(t):
    t = re.sub(r"\{\{([^|}]+)\|[^}]*\}\}", r"\1", t)
    t = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", t)
    t = re.sub(r"\*\*|__|\*", "", t)
    return t


def prosa(sec):
    """Párrafos de lectura de una sección: sin marcas de bloque, tablas, tarjetas, casos ni cuentas."""
    pars, cur = [], []
    for ln in sec.splitlines():
        s = ln.strip()
        if not s or s == ">" or re.match(r"^(---|\||\* fa-|\?|=|[-+×÷] ?\d|###|[0-9]+\.\s.*\|\||\* [^|]+\|.*\|)", s):
            if cur: pars.append(" ".join(cur)); cur = []
            continue
        if re.match(r"^(- |\d+\. )", s):
            # cada elemento de lista se lee aparte: es su propio párrafo
            if cur: pars.append(" ".join(cur)); cur = []
            s = re.sub(r"^(- |\d+\. )", "", s)
        if s.startswith("> "): s = s[2:]
        cur.append(s)
    if cur: pars.append(" ".join(cur))
    return [limpia(p) for p in pars if len(p.split()) >= 4]


def frases(p):
    return [f for f in re.split(r"(?:(?<=[.!?:;])|(?<=[.!?][\"»”’]))\s+(?=[A-ZÁÉÍÓÚÑ¿¡«\"“\d])", p) if f.strip()]


def palabras(t):
    return re.findall(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+", t)


def legibilidad(pars, en):
    ws = [w for p in pars for w in palabras(p)]
    fs = [f for p in pars for f in frases(p)]
    if not ws or not fs: return None
    sp = sum(silabas(w, en) for w in ws) / len(ws)
    pf = len(ws) / len(fs)
    return 206.835 - 1.015 * pf - 84.6 * sp if en else 206.835 - 62.3 * sp - pf


def escala(v, en):
    if v is None: return "—"
    if en:
        return "muy difícil" if v < 30 else "difícil" if v < 50 else "algo difícil" if v < 60 else "normal" if v < 70 else "fácil"
    return "muy difícil" if v < 40 else "algo difícil" if v < 55 else "normal" if v < 65 else "bastante fácil" if v < 80 else "muy fácil"


def lecciones(D, cfg):
    for m in cfg["modulos"]:
        p = os.path.join(D, "lecciones", f"{m}.md")
        if not os.path.exists(p): continue
        for b in re.split(r"(?m)^# (?=M\d+ U\d+)", open(p, encoding="utf-8").read())[1:]:
            cab, cuerpo = b.split("\n", 1)
            cod, tit = [x.strip() for x in cab.split("|", 1)]
            secs = {"_": cuerpo.split("\n== ", 1)[0]}
            for s in re.split(r"(?m)^== ", cuerpo)[1:]:
                n, t = (s.split("\n", 1) + [""])[:2]; secs[n.strip()] = t
            yield cod, tit, secs, cuerpo


def revisa(curso):
    D = os.path.join(BASE, "cursos", curso)
    cfg = json.load(open(os.path.join(D, "curso.json"), encoding="utf-8"))
    en = cfg.get("lang") == "en"
    filas = []
    for cod, tit, secs, todo in lecciones(D, cfg):
        ess, prof = prosa(secs.get("esencial", "")), prosa(secs.get("profundiza", ""))
        gancho = re.search(r"(?m)^gancho:\s*(.+)$", secs["_"])
        pars = ([limpia(gancho.group(1))] if gancho else []) + ess + prof
        lg = legibilidad(pars, en)
        largas = [f for p in pars for f in frases(p) if len(palabras(f)) > FRASE_LARGA]
        parr = [p for p in pars if len(palabras(p)) > PARRAFO_LARGO]
        # siglas: 3+ mayúsculas; explicadas si aparecen en «palabras», en una definición emergente o con paréntesis cerca
        expl = (secs.get("palabras", "") + " " + " ".join(re.findall(r"\{\{([^|}]+)\|", todo))).upper()
        siglas = sorted({s for s in re.findall(r"\b[A-ZÁÉÍÓÚÑ]{3,}\b", " ".join(pars))
                         if s not in SIGLAS_COMUNES and s not in expl and not re.search(rf"\b{s}\b\s*\(|\(\s*{s}\s*\)", todo)})
        # enlaces: URL suelta en la lectura o texto de enlace genérico; recursos sin «Qué buscar»
        sin_md = re.sub(r"\[[^\]]+\]\([^)]+\)", "", " ".join(pars))
        urls = len(re.findall(r"https?://", sin_md))
        genericos = len(re.findall(r"\[\s*(aquí|aqui|da clic aquí|haz clic aquí|clic aquí|liga|enlace|here|click here|link)\s*\]\(", todo, re.I)) + \
                    len(re.findall(r"\b(da clic aquí|haz clic aquí|click here)\b", sin_md, re.I))
        rec = [l for l in secs.get("recursos", "").splitlines() if l.strip().startswith("-")]
        sin_busca = sum(1 for l in rec if "http" in l and "Qué buscar" not in l and "What to look" not in l)
        pal_ess = sum(len(palabras(p)) for p in ess)
        filas.append(dict(curso=curso, leccion=cod, titulo=tit, legibilidad=round(lg, 1) if lg is not None else "", nivel=escala(lg, en),
                          frases_largas=len(largas), parrafos_largos=len(parr), siglas=", ".join(siglas), urls_en_texto=urls,
                          enlaces_genericos=genericos, recursos_sin_que_buscar=sin_busca, palabras_esencial=pal_ess,
                          ejemplo_frase=(max(largas, key=lambda f: len(palabras(f))) if largas else "")[:240]))
    return cfg, en, filas


# ---------- Contraste (WCAG 2.1) ----------
def lum(h):
    h = h.lstrip("#"); r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def ratio(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


PARES = [("Texto de lectura", "#0B1220", "#FFFFFF", False), ("Texto gris (explicaciones y pies)", "#5A6478", "#FFFFFF", False),
         ("Texto gris sobre fondo niebla", "#5A6478", "#F5F7FB", False), ("Títulos azul oscuro", "#061F40", "#FFFFFF", True),
         ("Texto blanco sobre azul (portadas, tablas)", "#FFFFFF", "#0A3161", False), ("Texto blanco sobre magenta (recuerda, errores)", "#FFFFFF", "#E4007C", False),
         ("Rosa claro sobre azul (etiquetas pequeñas)", "#FF7ABD", "#0A3161", False), ("Rosa sobre azul (cifras grandes)", "#FF4FA8", "#0A3161", True), ("Magenta sobre blanco (títulos de recuadros, enlaces)", "#E4007C", "#FFFFFF", False),
         ("Magenta sobre rosa pálido (íconos y notas)", "#E4007C", "#FFE3F1", True), ("Ámbar sobre fondo ámbar («Antes de actuar, verifica»)", "#A35200", "#FFF6EC", False),
         ("Azul oscuro sobre tinte (tarjetas «igual»)", "#061F40", "#E6ECF5", False), ("Azul sobre tinte (íconos)", "#0A3161", "#E6ECF5", True)]


def main():
    cursos = sorted(os.listdir(os.path.join(BASE, "cursos")))
    todas, res = [], []
    for c in cursos:
        cfg, en, f = revisa(c)
        todas += f
        lg = [x["legibilidad"] for x in f if x["legibilidad"] != ""]
        dificil = sum(1 for x in f if x["nivel"] in ("muy difícil", "algo difícil", "difícil"))
        res.append(dict(curso=c, titulo=cfg["titulo"], en=en, n=len(f), media=round(st.mean(lg), 1) if lg else 0, nivel=escala(st.mean(lg), en) if lg else "—",
                        dificil=dificil, largas=sum(x["frases_largas"] for x in f), parr=sum(x["parrafos_largos"] for x in f),
                        siglas=sum(1 for x in f if x["siglas"]), urls=sum(x["urls_en_texto"] for x in f), gen=sum(x["enlaces_genericos"] for x in f),
                        sinb=sum(x["recursos_sin_que_buscar"] for x in f), ess=round(st.median(x["palabras_esencial"] for x in f))))
    with open(os.path.join(OUT, "auditoria_accesibilidad_detalle.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(todas[0].keys())); w.writeheader(); w.writerows(todas)

    L = ["# Revisión de accesibilidad y legibilidad (E06)", "",
         f"Versión 1 · 5 de octubre de 2026 · {len(todas)} lecciones de {len(cursos)} cursos · generada con `herramientas_cursos/accesibilidad.py` (se vuelve a correr después de cada corrección).", "",
         "## Cómo se mide", "",
         "- **Legibilidad:** índice INFLESZ (Szigriszt-Pazos) en español y Flesch en inglés, sobre el gancho, «Lo esencial» y «Profundiza». Meta: «normal» o más fácil (INFLESZ 55 o más; Flesch 60 o más). El conteo de sílabas es automático y aproximado: sirve para comparar lecciones, no como calificación exacta.",
         f"- **Frases largas:** más de {FRASE_LARGA} palabras. **Párrafos largos:** más de {PARRAFO_LARGO} palabras (en el celular ocupan más de una pantalla).",
         "- **Siglas sin explicar:** siglas de 3 letras o más que no están en «Palabras», ni en una definición emergente, ni con su nombre entre paréntesis. Se excluyen las de uso común (IMSS, INE, CURP, SAT, IRS…).",
         "- **Enlaces:** direcciones sueltas dentro de la lectura, textos de enlace genéricos («aquí», «da clic») y recursos sin la guía «Qué buscar».",
         "- **Contraste:** colores de los libros contra la norma WCAG 2.1 AA (4.5 a 1 en texto normal; 3 a 1 en texto grande o íconos).", "",
         "## Resumen por curso", "",
         "| Curso | Lecciones | Legibilidad media | Lecciones difíciles | Frases largas | Párrafos largos | Lecciones con siglas sin explicar | URL en la lectura | Enlaces genéricos | Recursos sin «Qué buscar» | Palabras de «Lo esencial» (mediana) |",
         "|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in res:
        L.append(f"| {r['titulo']} | {r['n']} | {r['media']} ({r['nivel']}) | {r['dificil']} | {r['largas']} | {r['parr']} | {r['siglas']} | {r['urls']} | {r['gen']} | {r['sinb']} | {r['ess']} |")
    tl = len(todas); td = sum(r["dificil"] for r in res)
    L += ["", f"**Total:** {td} de {tl} lecciones quedan en «algo difícil» o más difícil; {sum(r['largas'] for r in res)} frases largas; {sum(r['parr'] for r in res)} párrafos largos; "
          f"{sum(r['siglas'] for r in res)} lecciones con siglas sin explicar; {sum(r['urls'] for r in res)} direcciones sueltas en la lectura; {sum(r['gen'] for r in res)} enlaces genéricos; "
          f"{sum(r['sinb'] for r in res)} recursos sin «Qué buscar».", ""]

    L += ["## Contraste de colores (WCAG 2.1 AA)", "", "| Uso | Texto | Fondo | Contraste | Mínimo | Resultado |", "|---|---|---|---|---|---|"]
    for uso, a, b, grande in PARES:
        r = ratio(a, b); mn = 3 if grande else 4.5
        L.append(f"| {uso} | `{a}` | `{b}` | {r:.2f} a 1 | {mn} a 1 | {'Cumple' if r >= mn else '**No cumple**'} |")
    malos = [(u, a, b) for u, a, b, g in PARES if ratio(a, b) < (3 if g else 4.5)]
    L += ["", ("**Ajustes de color:** " + "; ".join(f"«{u}»" for u, a, b in malos) + ". Ver recomendaciones.") if malos else "Todos los pares cumplen.", ""]

    L += ["## Lecciones prioritarias", "", "Las 40 con más problemas juntos (legibilidad baja, frases y párrafos largos, siglas). El detalle de todas está en `auditoria_accesibilidad_detalle.csv`.", "",
          "| Curso | Lección | Título | Legibilidad | Frases largas | Párrafos largos | Siglas sin explicar | Frase más larga |", "|---|---|---|---|---|---|---|---|"]
    def puntaje(x):
        lg = x["legibilidad"] if x["legibilidad"] != "" else 60
        return max(0, 55 - lg) * 2 + x["frases_largas"] * 3 + x["parrafos_largos"] * 2 + (4 if x["siglas"] else 0) + x["urls_en_texto"] * 3
    for x in sorted(todas, key=puntaje, reverse=True)[:40]:
        L.append(f"| {x['curso']} | {x['leccion']} | {x['titulo']} | {x['legibilidad']} ({x['nivel']}) | {x['frases_largas']} | {x['parrafos_largos']} | {x['siglas'] or '—'} | {x['ejemplo_frase'].replace('|', '/')} |")

    sig = {}
    for x in todas:
        for s in filter(None, x["siglas"].split(", ")): sig.setdefault(s, []).append(f"{x['curso']} {x['leccion']}")
    L += ["", "## Siglas sin explicar", "", "| Sigla | Lecciones |", "|---|---|"]
    L += [f"| {s} | {', '.join(v[:6])}{' y ' + str(len(v) - 6) + ' más' if len(v) > 6 else ''} |" for s, v in sorted(sig.items(), key=lambda kv: -len(kv[1]))]

    L += ["", "## Lo que ya cumple", "",
          "- Lecciones cortas por partes, con ruta rápida y completa, y la práctica al final.",
          "- Términos difíciles con definición emergente y sección «Palabras» en cada lección.",
          "- Recursos con institución, idioma y la guía «Qué buscar», en lugar de «da clic aquí».",
          "- Sin imágenes con texto: todo el contenido es texto real, que leen los lectores de pantalla y se puede ampliar.",
          "- Íconos decorativos acompañados siempre de texto.",
          "- Diseño que se adapta al celular (probado a 390 px).", "",
          "## Recomendaciones", "",
          "1. **Frases largas:** partir en dos las frases de más de 25 palabras, empezando por las lecciones prioritarias. Una idea por frase.",
          "2. **Párrafos largos:** en «Lo esencial», máximo 3 frases por párrafo; lo demás pasa a «Profundiza» o a una lista.",
          "3. **Siglas:** la primera vez, nombre completo y sigla entre paréntesis, o una definición emergente; agregarlas a «Palabras».",
          "4. **Contraste:** los pares marcados como «No cumple» se corrigen en la hoja de estilos de los libros (un solo cambio para todos los cursos).",
          "5. **Moodle:** al instalar, revisar con el lector de pantalla del celular (TalkBack o VoiceOver) una lección por curso, y que los H5P se puedan responder sin ratón.",
          "6. **Videos (cuando existan):** sin voz, así que el texto en pantalla debe durar lo suficiente para leerse (al menos 3 segundos por línea) y cada video necesita una descripción en texto debajo.",
          "7. **Volver a correr** `python3 herramientas_cursos/accesibilidad.py` después de cada corrección y antes de cada entrega."]
    open(os.path.join(OUT, "auditoria_accesibilidad.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    print(f"{tl} lecciones · {td} difíciles · malos contrastes: {len(malos)}")


if __name__ == "__main__":
    main()
