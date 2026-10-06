# Manual del programa a partir de curso.json y las lecciones (cursos nuevos en borrador, sin Moodle).
# Uso: python3 herramientas_cursos/manual_borrador.py cursos/<carpeta>
import os, re, sys, json

D = os.path.abspath(sys.argv[1])
C = json.load(open(os.path.join(D, "curso.json"), encoding="utf-8"))
LEC = os.path.join(D, "lecciones")
EN = C.get("lang") == "en"
T = (lambda es, en: en) if EN else (lambda es, en: es)

REGLAS_EN = [
    "**Educate, don't sell:** lessons don't recommend banks, lenders or products; they teach how to verify any institution with CONDUSEF.",
    "**No SOFIPO, SOCAP or SOFOM recommendations.**",
    "**Never ask for personal data**, passwords, PINs or real debt or savings amounts.",
    "**Financial well-being program:** that's the name used in all materials.",
    "**Nothing is free or a gift:** public services are described as «at no cost».",
    "**Every figure with a date and source**; where two official sources differ, both are cited.",
    "**Names not used for characters:** Jorge, José, Ángeles, David, Luis, Ana, Jonathan, Paola, Ernesto, Marisa, Tomás, Leonardo, Esther, Liliana and Alberto (the generator's check detects them).",
]
REGLAS = [
    "**Educar, no vender:** las lecciones no recomiendan bancos, prestamistas ni productos; enseñan a verificar cualquier institución en CONDUSEF.",
    "**No se recomiendan SOFIPO, SOCAP ni SOFOM.**",
    "**Nunca se piden datos personales**, contraseñas, NIP ni montos reales de deudas o ahorros.",
    "**Programa de bienestar financiero:** así se nombra en todos los materiales.",
    "**Nada es gratis ni se regala:** los trámites públicos se describen como «sin costo».",
    "**Cada dato con fecha y fuente**; donde dos fuentes oficiales difieren, se citan ambas.",
    "**Nombres que no se usan para personajes:** Jorge, José, Ángeles, David, Luis, Ana, Jonathan, Paola, Ernesto, Marisa, Tomás, Leonardo, Esther, Liliana y Alberto (la verificación del generador los detecta).",
]


def lecciones(mod):
    t = open(os.path.join(LEC, f"{mod}.md"), encoding="utf-8").read()
    out = []
    for b in re.split(r"(?m)^# (?=M\d+ U\d\d)", t)[1:]:
        code, title = [x.strip() for x in b.split("\n", 1)[0].split("|", 1)]
        obj = re.search(r"(?m)^(?:objetivo|objective):\s*(.*)$", b).group(1)
        out.append((code, title, obj))
    return out


L = [f"# {C['titulo']}", "",
     T("Manual del programa", "Program manual") + f" · {C['subtitulo']}", "",
     C["intro"], "", "[[TOC]]", "", "---", "",
     T("# 1. Datos generales", "# 1. General information"), "", T("| Campo | Valor |", "| Field | Value |"), "|---|---|",
     T("| Programa | ", "| Program | ") + f"{C['titulo']} |", T("| Público | ", "| Audience | ") + f"{C['publico']} |",
     T("| Tono | Tuteo cálido y directo, español de México, frases cortas, sin tecnicismos ni culpas |", "| Tone | Warm and direct, plain English, short sentences, no jargon or blame |"),
     T("| Formato | ", "| Format | ") + f"{C['formato']} |"]
tot = sum(len(lecciones(m)) for m in C["modulos"])
L += [T("| Duración | ", "| Length | ") + f"{len(C['modulos'])} " + T("módulos", "modules") + f", {tot} " + T("lecciones de 5 a 10 minutos |", "lessons of 5 to 10 minutes |"), ""]
if C.get("problema"):
    L += [T("## El problema que resuelve", "## The problem it solves"), ""] + [f"- {p}" for p in C["problema"]] + [""]
L += [T("## Reglas del programa", "## Program rules"), ""] + [f"{i}. {r}" for i, r in enumerate((REGLAS_EN if EN else REGLAS) + C.get("reglas_extra", []), 1)] + [""]
L += [T("## Personajes", "## Characters"), "", T("| Personaje | Quién es |", "| Character | Who they are |"), "|---|---|"] + [f"| {k} | {v} |" for k, v in C["personajes"].items()] + [""]
L += [T("# 2. Mapa de módulos", "# 2. Module map"), "", T("| Módulo | Resultado | Insignia |", "| Module | Outcome | Badge |"), "|---|---|---|"]
ins = {i[1]: i[2] for i in C["insignias"]}
for m, t in C["modulos"].items():
    L.append(f"| {t} | {C['resultados'][m]} | {ins.get(m, '')} |")
L += ["", T("Al terminar todo el programa: insignia ", "At the end of the program: badge ") + f"**{C['insignias'][-1][2]}** " + T("y constancia con los temas: ", "and certificate with the topics: ") + f"{', '.join(C['constancia'].get('temas') or C['constancia'].get('mods', []))}.", ""]
L += [T("# 3. Lecciones", "# 3. Lessons"), ""]
for m, t in C["modulos"].items():
    L += [f"## {t}", "", T("| Clave | Lección | Lo que logra la persona |", "| Code | Lesson | What the person achieves |"), "|---|---|---|"]
    L += [f"| {c} | {ti} | {o} |" for c, ti, o in lecciones(m)] + [""]
L += [T("# 4. Estructura de cada lección", "# 4. Structure of each lesson"), "",
      "- **Lo esencial (5 minutos):** pasos, tarjetas, un cálculo y un caso en un minuto; cierra con una idea clave, dos preguntas para comprobar y un recordatorio.",
      "- **Profundiza (5 minutos más):** tabla para llenar, un tema extra, tres casos y errores frecuentes.",
      "- **Practica:** actividad «¿Qué harías?» con tres casos, autoevaluación de tres preguntas, un ejercicio y un plan de acción.",
      "- **Recursos, palabras y fuentes** al final de cada lección.", ""] if not EN else ["# 4. Structure of each lesson", "",
      "- **Start:** the hook and what you'll learn.",
      "- **The essentials (5 minutes):** steps, cards, a calculation and a one-minute case; it ends with a key idea and common mistakes.",
      "- **Go deeper (5 more minutes):** a table to fill in, an extra topic and three cases.",
      "- **Practice:** «What would you do?» with situations, a review and an action plan.",
      "- **Resources, key words and sources** at the end of each lesson.", ""]
if C.get("datos"):
    L += [T("# 5. Datos verificados", "# 5. Verified data"), "", T("| Dato | Valor | Fuente |", "| Fact | Value | Source |"), "|---|---|---|"] + [f"| {a} | {b} | {c} |" for a, b, c in C["datos"]] + [""]
os.makedirs(os.path.join(D, "manual"), exist_ok=True)
open(os.path.join(D, "manual", "manual.md"), "w", encoding="utf-8").write("\n".join(L))
print("manual:", tot, "lecciones")
