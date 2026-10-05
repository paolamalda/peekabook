# Manual del programa a partir de curso.json y las lecciones (cursos nuevos en borrador, sin Moodle).
# Uso: python3 herramientas_cursos/manual_borrador.py cursos/<carpeta>
import os, re, sys, json

D = os.path.abspath(sys.argv[1])
C = json.load(open(os.path.join(D, "curso.json"), encoding="utf-8"))
LEC = os.path.join(D, "lecciones")

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
        obj = re.search(r"(?m)^objetivo:\s*(.*)$", b).group(1)
        out.append((code, title, obj))
    return out


L = [f"# {C['titulo']}", "",
     f"Manual del programa · {C['subtitulo']}", "",
     C["intro"], "", "[[TOC]]", "", "---", "",
     "# 1. Datos generales", "", "| Campo | Valor |", "|---|---|",
     f"| Programa | {C['titulo']} |", f"| Público | {C['publico']} |",
     "| Tono | Tuteo cálido y directo, español de México, frases cortas, sin tecnicismos ni culpas |",
     f"| Formato | {C['formato']} |"]
tot = sum(len(lecciones(m)) for m in C["modulos"])
L += [f"| Duración | {len(C['modulos'])} módulos, {tot} lecciones de 5 a 10 minutos |", ""]
if C.get("problema"):
    L += ["## El problema que resuelve", ""] + [f"- {p}" for p in C["problema"]] + [""]
L += ["## Reglas del programa", ""] + [f"{i}. {r}" for i, r in enumerate(REGLAS + C.get("reglas_extra", []), 1)] + [""]
L += ["## Personajes", "", "| Personaje | Quién es |", "|---|---|"] + [f"| {k} | {v} |" for k, v in C["personajes"].items()] + [""]
L += ["# 2. Mapa de módulos", "", "| Módulo | Resultado | Insignia |", "|---|---|---|"]
ins = {i[1]: i[2] for i in C["insignias"]}
for m, t in C["modulos"].items():
    L.append(f"| {t} | {C['resultados'][m]} | {ins.get(m, '')} |")
L += ["", f"Al terminar todo el programa: insignia **{C['insignias'][-1][2]}** y constancia con los temas: {', '.join(C['constancia']['temas'])}.", ""]
L += ["# 3. Lecciones", ""]
for m, t in C["modulos"].items():
    L += [f"## {t}", "", "| Clave | Lección | Lo que logra la persona |", "|---|---|---|"]
    L += [f"| {c} | {ti} | {o} |" for c, ti, o in lecciones(m)] + [""]
L += ["# 4. Estructura de cada lección", "",
      "- **Lo esencial (5 minutos):** pasos, tarjetas, un cálculo y un caso en un minuto; cierra con una idea clave, dos preguntas para comprobar y un recordatorio.",
      "- **Profundiza (5 minutos más):** tabla para llenar, un tema extra, tres casos y errores frecuentes.",
      "- **Practica:** actividad «¿Qué harías?» con tres casos, autoevaluación de tres preguntas, un ejercicio y un plan de acción.",
      "- **Recursos, palabras y fuentes** al final de cada lección.", ""]
if C.get("datos"):
    L += ["# 5. Datos verificados", "", "| Dato | Valor | Fuente |", "|---|---|---|"] + [f"| {a} | {b} | {c} |" for a, b, c in C["datos"]] + [""]
os.makedirs(os.path.join(D, "manual"), exist_ok=True)
open(os.path.join(D, "manual", "manual.md"), "w", encoding="utf-8").write("\n".join(L))
print("manual:", tot, "lecciones")
