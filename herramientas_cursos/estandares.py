# Documentos para los estándares EC0366 (cursos en línea) y EC0217 (impartición presencial) de un curso.
# Uso: python3 herramientas_cursos/estandares.py cursos/<carpeta> [--inicio AAAA-MM-DD]
# Salida: cursos/<carpeta>/estandares/ (12 documentos en Markdown, diagnóstica en GIFT y encuesta de satisfacción en XML).
import unicodedata, os, re, sys, json, math, datetime, html

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "proyecto-inclusion-financiera", "herramientas"))
import leccion_ux3 as UX3

ELABORA = "Paola Malda Arozarena · Desarrolla Talento"
HOY = datetime.date(2026, 10, 5)
MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
fecha = lambda d: f"{d.day} de {MESES[d.month - 1]} de {d.year}"

AREA = {  # verbo inicial → (área de aprendizaje, nivel de dominio)
    "Identificar": ("cognoscitiva", "conocimiento"), "Reconocer": ("cognoscitiva", "conocimiento"), "Ubicar": ("cognoscitiva", "conocimiento"),
    "Explicar": ("cognoscitiva", "comprensión"), "Distinguir": ("cognoscitiva", "comprensión"), "Describir": ("cognoscitiva", "comprensión"),
    "Calcular": ("cognoscitiva", "aplicación"), "Comprobar": ("cognoscitiva", "aplicación"), "Usar": ("cognoscitiva", "aplicación"), "Aplicar": ("cognoscitiva", "aplicación"),
    "Comparar": ("cognoscitiva", "análisis"), "Revisar": ("cognoscitiva", "análisis"), "Leer": ("cognoscitiva", "análisis"), "Detectar": ("cognoscitiva", "análisis"),
    "Decidir": ("cognoscitiva", "evaluación"), "Elegir": ("cognoscitiva", "evaluación"), "Evaluar": ("cognoscitiva", "evaluación"),
    "Hacer": ("psicomotriz", "manipulación"), "Armar": ("psicomotriz", "manipulación"), "Preparar": ("psicomotriz", "manipulación"), "Llenar": ("psicomotriz", "manipulación"),
    "Registrar": ("psicomotriz", "manipulación"), "Abrir": ("psicomotriz", "manipulación"), "Separar": ("psicomotriz", "manipulación"), "Reunir": ("psicomotriz", "manipulación"),
    "Poner": ("psicomotriz", "manipulación"), "Organizar": ("psicomotriz", "manipulación"), "Cobrar": ("psicomotriz", "manipulación"), "Sacar": ("psicomotriz", "manipulación"),
    "Mandar": ("psicomotriz", "manipulación"), "Recibir": ("psicomotriz", "manipulación"), "Guardar": ("psicomotriz", "manipulación"), "Acordar": ("afectiva", "valoración"),
    "Proteger": ("afectiva", "valoración"), "Platicar": ("afectiva", "respuesta"), "Cuidar": ("afectiva", "valoración"), "Prepararse": ("afectiva", "organización"),
}


def leer(p): return open(p, encoding="utf-8").read()


def limpia(s):
    s = re.sub(r"\{\{([^|}]+)\|[^}]+\}\}", r"\1", s)
    return re.sub(r"\*\*|\*", "", s).strip()


V2 = {"tienes": "tiene", "puedes": "puede", "necesitas": "necesita", "trabajas": "trabaja", "sales": "sale", "puedas": "pueda", "pagas": "paga",
      "cobras": "cobra", "haces": "hace", "ganas": "gana", "debes": "debe", "recibes": "recibe", "quieres": "quiere", "vives": "vive", "usas": "usa",
      "compras": "compra", "mandas": "manda", "envías": "envía", "llegas": "llega", "cumples": "cumple", "lastimas": "lastima", "enfermas": "enferma",
      "regresas": "regresa", "vas": "va", "estás": "está", "eres": "es", "sabes": "sabe", "ahorras": "ahorra", "gastas": "gasta", "decides": "decide",
      "pides": "pide", "firmas": "firma", "rentas": "renta", "prestas": "presta", "declaras": "declara", "vendes": "vende", "empiezas": "empieza",
      "dejaste": "dejó", "trabajaste": "trabajó", "tuviste": "tuvo", "ganaste": "ganó", "recibiste": "recibió", "faltes": "falte", "conoces": "conoce",
      "cambias": "cambia", "pierdes": "pierde", "juegas": "juega", "vendas": "venda", "tengas": "tenga", "manejas": "maneja", "cuidas": "cuida",
      "llegues": "llegue", "entiendas": "entienda", "tomarás": "tomará", "verificaste": "verificó", "confirmaste": "confirmó", "harás": "hará",
      "pagarás": "pagará", "usarás": "usará", "necesitarás": "necesitará", "hiciste": "hizo", "pagaste": "pagó", "recibirás": "recibirá", "quieras": "quiera",
      "debas": "deba", "tienes que": "tiene que", "sepas": "sepa", "uses": "use", "pagues": "pague", "ganes": "gane", "cobres": "cobre", "mudas": "muda", "separas": "separa", "enviudas": "enviuda", "inviertes": "invierte", "contratas": "contrata", "apuestas": "apuesta"}
REFLEX = {"lastimas", "enfermas", "mudas", "separas"}
V2.update({"controlas": "controla", "faltas": "falta", "tuyo": "suyo", "tuya": "suya", "tuyos": "suyos", "tuyas": "suyas", "conoces": "conoce",
           "entiendes": "entiende", "vendes": "vende", "rentas": "renta", "manejas": "maneja", "cuidas": "cuida", "dependes": "depende"})
NO_ENCLITICO = {"parte", "aparte", "transporte", "deporte", "reporte", "soporte", "aporte", "corte", "norte", "arte", "suerte", "fuerte", "muerte"}


def tercera(s):
    """Pasa un objetivo de «tú» a tercera persona para la versión formal."""
    s = re.sub(r"\btus\b", "sus", s); s = re.sub(r"\bTus\b", "Sus", s)
    s = re.sub(r"\btu\b", "su", s); s = re.sub(r"\bTu\b", "Su", s)
    s = re.sub(r"\b(\w+?)(ar|er|ir)te\b", lambda m: m.group(0) if m.group(0).lower() in NO_ENCLITICO else m.group(1) + m.group(2) + "se", s)
    s = re.sub(r"\bcuando faltas\b", "cuando falta", s)
    s = re.sub(r"\bte (\w+)\b", lambda m: ("se " if m.group(1) in REFLEX else "le ") + V2.get(m.group(1), m.group(1)), s)
    s = re.sub(r"\b(\w+)\b", lambda m: V2.get(m.group(1), m.group(1)), s)
    s = re.sub(r"\btú\b", "la persona", s)
    s = re.sub(r"\b(de|para|a) ti\b", r"\1 la persona", s)
    s = re.sub(r"\bpor ti\b", "por la persona", s)
    s = re.sub(r"\bcontigo\b", "con la persona", s)
    return s


PASADO = {"haz": "hizo", "anota": "anotó", "escribe": "escribió", "crea": "creó", "elige": "eligió", "completa": "completó", "arma": "armó", "marca": "marcó",
          "usa": "usó", "revisa": "revisó", "compara": "comparó", "pide": "pidió", "guarda": "guardó", "llena": "llenó", "busca": "buscó", "calcula": "calculó",
          "separa": "separó", "pon": "puso", "decide": "decidió", "localiza": "localizó", "define": "definió", "identifica": "identificó", "platica": "platicó",
          "acuerda": "acordó", "lleva": "llevó", "prepara": "preparó", "junta": "juntó", "reúne": "reunió", "abre": "abrió", "registra": "registró",
          "consulta": "consultó", "verifica": "verificó", "toma": "tomó", "comparte": "compartió", "apunta": "apuntó", "dibuja": "dibujó", "cuenta": "contó",
          "mide": "midió", "agenda": "agendó", "aparta": "apartó", "practica": "practicó", "confirma": "confirmó", "suma": "sumó", "resta": "restó",
          "organiza": "organizó", "investiga": "investigó", "pregunta": "preguntó", "ubica": "ubicó", "anótalo": "lo anotó", "escríbelo": "lo escribió",
          "llama": "llamó", "fija": "fijó", "planea": "planeó", "elabora": "elaboró", "actualiza": "actualizó", "ordena": "ordenó", "reparte": "repartió",
          "divide": "dividió", "programa": "programó", "piensa": "pensó en", "habla": "habló", "descarga": "descargó", "imprime": "imprimió", "copia": "copió",
          "valida": "validó", "contesta": "contestó", "responde": "respondió", "agrega": "agregó", "cambia": "cambió", "deja": "dejó", "inscríbete": "se inscribió",
          "regístrate": "se registró", "fíjate": "se fijó"}


PASADO.update({"activa": "activó", "entra": "entró", "empieza": "empezó", "entrega": "entregó", "resuelve": "resolvió", "manda": "mandó", "ajusta": "ajustó",
               "cotiza": "cotizó", "quita": "quitó", "inscribe": "inscribió", "vuelve": "volvió", "publica": "publicó", "tramita": "tramitó", "cancela": "canceló",
               "corrige": "corrigió", "averigua": "averiguó", "conecta": "conectó", "solicita": "solicitó", "multiplica": "multiplicó", "diseña": "diseñó",
               "encuentra": "encontró", "explora": "exploró", "reserva": "reservó", "pega": "pegó", "respalda": "respaldó", "cambia": "cambió", "avisa": "avisó",
               "bloquea": "bloqueó", "borra": "borró", "reclama": "reclamó", "denuncia": "denunció", "firma": "firmó", "negocia": "negoció", "cuelga": "colgó",
               "escoge": "escogió", "presenta": "presentó", "formaliza": "formalizó", "domicilia": "domicilió", "di": "dijo", "ten": "tuvo", "sal": "salió", "ve": "fue", "pide": "pidió", "sigue": "siguió"})
_CLIT = {"lo": "lo", "la": "la", "los": "los", "las": "las", "le": "le", "les": "les"}


def _sin_acento(w):
    return "".join(ch for ch in unicodedata.normalize("NFD", w) if unicodedata.category(ch) != "Mn")


def pasado(w):
    """Imperativo (con o sin pronombre pegado) a pretérito: «búscalo» → «lo buscó». None si no es un imperativo conocido."""
    k = w.lower().strip(",:")
    if k in PASADO: return PASADO[k]
    if k.endswith("te") and len(k) > 4:
        base = _sin_acento(k[:-2])
        if base in PASADO and k != base + "te": return "se " + PASADO[base]
    for cl in ("los", "las", "les", "lo", "la", "le"):
        if k.endswith(cl) and len(k) > len(cl) + 1:
            base = _sin_acento(k[:-len(cl)])
            if base in PASADO and k != base + cl:  # lleva acento: es imperativo con pronombre
                return f"{cl} {PASADO[base]}"
            if base == "di": return f"{cl} dijo"
            if base == "pon": return f"{cl} puso"
    return None


def criterio(plan):
    """Convierte la instrucción del «plan» de una lección en un criterio observable de lista de cotejo."""
    frases = [f for f in re.split(r"(?<=[.!?])\s+", plan) if f and not re.match(r"(No necesitas|No compartas|No tienes que|Usa datos|Puedes usar)", f)]
    out = []
    for f in frases:
        w = f.split()[0]
        if pasado(w): f = pasado(w) + f[len(w):]
        f = re.sub(r"(,? y |; |, |: )(\w+)\b", lambda m: m.group(1) + (pasado(m.group(2)) or m.group(2)), f)
        out.append(tercera(f).rstrip("."))
    s = "; ".join(out)
    return s[:1].upper() + s[1:]


def sin_aplica(obj):
    return re.sub(r"\s*Aplica (a|solo|igual)\b.*$", "", obj).strip()


def curso(D, inicio):
    cfg = json.load(open(os.path.join(D, "curso.json"), encoding="utf-8"))
    global PASO3, INSTR
    if cfg.get("ux") == 3:
        PASO3 = "3. **Dentro de una lección:** cuatro pasos arriba de la pantalla: **Empieza**, **Lo esencial**, **Profundiza** (opcional) y **Practica**."
        INSTR = "Lee «Empieza» y «Lo esencial» (y «Profundiza» si eliges la ruta completa)."
    else:
        PASO3 = ("3. **Dentro de una lección:** una portada con la situación y dos rutas: **rápida** (Lo esencial y Practica) o **completa** "
                 "(agrega Profundiza). Cada parte es un capítulo del libro de la lección.")
        INSTR = "En la portada, elige tu ruta; lee «Lo esencial» (y «Profundiza» si eliges la ruta completa)."
    tit, MODS = cfg["titulo"], cfg["modulos"]
    nombres = {m: cfg.get("nombres", {}).get(m, {}).get("titulo") or re.sub(r"^Módulo \d+\.\s*", "", t) for m, t in MODS.items()}
    les = {}
    for m in MODS:
        txt = leer(os.path.join(D, "lecciones", f"{m}.md"))
        out = []
        for b in re.split(r"(?m)^# (?=M\d+ U\d\d)", txt)[1:]:
            code, title, meta, secs = UX3.parse(b)
            rap, prof = UX3.tiempos(secs)
            pr = dict((k, c) for k, _, _, c in UX3.blocks(secs.get("practica", "")))
            out.append(dict(code=code, title=title, obj=sin_aplica(limpia(meta.get("objetivo", ""))), min=(rap, rap + prof),
                            quiz=UX3.quiz_items(pr), plan=limpia(pr.get("plan", "")), ponlo=limpia(pr.get("ponlo", "").split("respuesta:")[0])))
        les[m] = out
    nl = sum(len(v) for v in les.values()); nm = len(MODS)
    mins = {m: (sum(l["min"][0] for l in v), sum(l["min"][1] for l in v)) for m, v in les.items()}
    tot = (sum(a for a, _ in mins.values()), sum(b for _, b in mins.values()))
    h = lambda x: f"{round(x / 30) / 2:g}"
    sem = {m: max(1, math.ceil(mins[m][1] / 120)) for m in MODS}  # ~2 horas por semana
    nsem = sum(sem.values()) + 1
    res = cfg.get("resultados", {})
    publico = cfg.get("publico") or cfg.get("catalogo", {}).get("para_quien") or cfg.get("intro", "")
    temas_txt = ", ".join(nombres[m][0].lower() + nombres[m][1:] for m in MODS)
    O = os.path.join(D, "estandares"); os.makedirs(O, exist_ok=True)
    W = lambda f, s: open(os.path.join(O, f), "w", encoding="utf-8").write(s)
    cab = lambda nombre: f"# {nombre} · {tit}\n\nElabora: {ELABORA} · Fecha: {fecha(HOY)} · Versión {cfg.get('version', '1.0')}\n\n"

    # ---------- 01 objetivos ----------
    og = (f"Al terminar el programa, la persona participante será capaz de {cfg['objetivo_general']}, " if cfg.get("objetivo_general") else
          f"Al terminar el programa, la persona participante será capaz de tomar decisiones informadas sobre {temas_txt}, ") + (
          f"aplicándolas a su propia situación con datos reales o de ejemplo, con la aprobación de las {nm} autoevaluaciones "
          f"(70% o más en cada una) y su plan de acción por escrito.")
    def particular(m):
        r = res.get(m, "")
        r = re.sub(r"^(Tu|Tus)\b", lambda x: "su" if x.group(1) == "Tu" else "sus", r)
        r = r[:1].lower() + r[1:] if r else f"las actividades de {nombres[m].lower()}"
        return (f"Al terminar el módulo, la persona participante habrá elaborado {tercera(r.rstrip('.'))}, con sus propios datos o datos de ejemplo, "
                f"y aprobará la autoevaluación del módulo con 70% o más.")
    def especifico(l):
        o = tercera(l["obj"].rstrip("."))
        v = o.split()[0]
        area, nivel = AREA.get(v, ("cognoscitiva", "comprensión"))
        return (f"Al terminar la lección, la persona participante será capaz de {o[:1].lower() + o[1:]}, a partir de un caso de la vida diaria "
                f"y de los ejercicios de la lección, con al menos 2 de 3 respuestas correctas en «Repasa».", area, nivel)
    s = cab("Objetivos de aprendizaje")
    s += ("Redactados con los cinco elementos del EC0217: **persona** (la persona participante), **conducta** (verbo observable), **contenido**, "
          "**condición** (a partir de un caso y los ejercicios) y **nivel** (aciertos o aprobación). El texto amable que ve la persona en cada lección "
          "es la versión corta del mismo objetivo.\n\n")
    s += f"## Objetivo general\n\n{og}\n\n## Objetivos particulares y específicos\n\n"
    for i, m in enumerate(MODS, 1):
        s += f"### {i}. {nombres[m]}\n\n**Objetivo particular:** {particular(m)}\n\n| Lección | Objetivo específico | Área | Nivel |\n|---|---|---|---|\n"
        for l in les[m]:
            e, a, n = especifico(l)
            s += f"| {l['title']} | {e} | {a} | {n} |\n"
        s += "\n"
    W("01_objetivos.md", s)

    # ---------- 02 información general ----------
    s = cab("Documento de información general (EC0366)")
    s += f"## Título\n\n{tit}\n\n## Objetivo general\n\n{og}\n\n## Introducción\n\n{limpia(cfg.get('intro', ''))}\n\n"
    s += "## Temas y objetivos particulares\n\n"
    for i, m in enumerate(MODS, 1):
        s += f"**{i}. {nombres[m]}** ({len(les[m])} lecciones, {h(mins[m][0])} a {h(mins[m][1])} horas). {particular(m)}\n\n"
        s += "".join(f"- {l['title']}\n" for l in les[m]) + "\n"
    s += ("""## Guía visual del curso

1. **Inicio del curso:** un mosaico por módulo con su porcentaje de avance y el botón para seguir donde te quedaste.
2. **Dentro de un módulo:** un mosaico por lección. Cada lección se abre al terminar la anterior y muestra si está terminada, en curso o pendiente.
""" + PASO3 + """
4. **Practica:** la actividad «¿Qué harías?» y «Repasa» (una pantalla a la vez), el ejercicio con tus números y tu compromiso.
5. **Al final de cada módulo:** la autoevaluación. Al aprobar todas y responder la encuesta final se libera la constancia.

(Agregar capturas de pantalla de cada punto al instalar el curso.)

## Metodología de trabajo

Curso en línea, asíncrono y a tu ritmo, en lecciones cortas. Cada lección empieza con un caso de la vida diaria y permite elegir entre dos rutas: **Lo esencial** (unos 10 minutos con práctica) o **Lo esencial + Profundiza** (unos 15 minutos). La práctica da retroalimentación inmediata y se puede repetir. Hay una comunidad (foro) para compartir dudas y compromisos sin datos personales, y materiales de apoyo con glosario, casos integradores y dónde pedir ayuda. Si una organización lo pide, se acompaña con sesiones presenciales (ver la carta descriptiva).

""")
    s += f"## Perfil de ingreso\n\n{limpia(publico)}\n\n**Requisitos:** saber leer textos sencillos en español, tener celular o computadora con internet y un correo o cuenta de Google para entrar. No se piden datos personales, números de cuenta ni documentos.\n\n"
    s += """## Requerimientos tecnológicos y materiales

- Celular, tableta o computadora con navegador actualizado (Chrome, Firefox, Safari o Edge), o la app oficial de Moodle.
- Conexión a internet; las lecciones y videos están optimizados para datos móviles.
- Audio opcional (los videos tienen texto en pantalla).
- Para las herramientas descargables: una app de hojas de cálculo (Excel, Google Sheets o similar).

"""
    s += (f"## Forma de evaluación\n\n| Elemento | Momento | Peso en la calificación final | Criterio |\n|---|---|---|---|\n"
          f"| Evaluación diagnóstica | Inicio | 0% (no cuenta) | Conocer el punto de partida |\n"
          f"| Práctica de cada lección («¿Qué harías?», «Repasa», ejercicio y compromiso) | Durante | 0% (formativa) | Retroalimentación inmediata; intentos ilimitados |\n")
    for i, m in enumerate(MODS, 1):
        s += f"| Autoevaluación del módulo {i} | Al terminar el módulo | {100 / nm:.4g}% | 70% o más para aprobar |\n"
    s += "| Encuesta final y de satisfacción | Al terminar | 0% | Requisito para la constancia |\n\n"
    s += "**Constancia:** se libera al aprobar todas las autoevaluaciones y responder la encuesta final.\n\n"
    s += f"## Duración\n\n**{h(tot[0])} a {h(tot[1])} horas** en total ({nl} lecciones de 10 a 15 minutos más autoevaluaciones), en **{nsem} semanas** con el calendario sugerido (unas 2 horas por semana).\n\n"
    s += "## Formato\n\nDigital: plataforma Moodle de Desarrolla Talento (academia.desarrollatalento.com). Este documento también se entrega impreso o en PDF.\n"
    W("02_informacion_general.md", s)

    # ---------- 03 cronograma de desarrollo ----------
    acts = [("Detección de necesidades y definición del perfil de ingreso", 5), ("Estructura temática: módulos, lecciones y objetivos", 5),
            ("Documento de información general", 2), ("Guías de actividades de aprendizaje por módulo y calendario", 3)]
    acts += [(f"Contenido del módulo {i} «{nombres[m]}»: {len(les[m])} lecciones, prácticas y videos", 3 + len(les[m])) for i, m in enumerate(MODS, 1)]
    acts += [("Instrumentos de evaluación: autoevaluaciones, diagnóstica y encuesta de satisfacción", 4), ("Materiales de apoyo, glosario y herramientas descargables", 4),
             ("Montaje en la plataforma", 5), ("Verificación del funcionamiento y reporte de revisión", 3), ("Ajustes finales y liberación", 2)]
    d = inicio
    s = cab("Cronograma de desarrollo (EC0366)")
    s += f"**Título del curso:** {tit}\n\n**Objetivo general:** {og}\n\n**Fecha de elaboración:** {fecha(HOY)}\n\n"
    s += "| # | Actividad | Días hábiles | Inicio | Fin |\n|---|---|---|---|---|\n"
    def suma_habiles(x, n):
        while n > 0:
            x += datetime.timedelta(days=1)
            if x.weekday() < 5: n -= 1
        return x
    for i, (a, n) in enumerate(acts, 1):
        f = suma_habiles(d, n - 1) if n > 1 else d
        s += f"| {i} | {a} | {n} | {d.isoformat()} | {f.isoformat()} |\n"
        d = suma_habiles(f, 1)
    s += f"\n**Total:** {sum(n for _, n in acts)} días hábiles.\n\n| Elabora | Autoriza |\n|---|---|\n| {ELABORA} | [Nombre y cargo] |\n| Firma: ______________________ | Firma: ______________________ |\n"
    W("03_cronograma_desarrollo.md", s)

    # ---------- 04 guías de actividades ----------
    s = cab("Guías de actividades de aprendizaje por módulo (EC0366)")
    semana = 1
    for i, m in enumerate(MODS, 1):
        a, b = semana + 1, semana + sem[m]
        s += f"## Módulo {i}. {nombres[m]}\n\n**Objetivo específico de la unidad:** {particular(m)}\n\n**Periodo sugerido:** semana{'s' if a != b else ''} {a}{'–' + str(b) if a != b else ''} · **Tiempo estimado:** {h(mins[m][0])} a {h(mins[m][1])} horas.\n\n"
        s += "| # | Actividad | Instrucciones | Recursos | Participación | Evaluación |\n|---|---|---|---|---|---|\n"
        for k, l in enumerate(les[m], 1):
            s += (f"| {k} | {l['title']} | {INSTR} En «Practica», resuelve «¿Qué harías?» y «Repasa», "
                  f"haz el ejercicio con tus números y escribe tu compromiso. | Libro de la lección, video, práctica interactiva"
                  f"{', herramienta descargable' if 'hoja' in l['plan'].lower() or 'tabla' in l['plan'].lower() else ''} | Individual | Formativa: retroalimentación inmediata; se marca completa al ver la lección |\n")
        s += (f"| {len(les[m]) + 1} | Comparte tu compromiso | En el foro de la comunidad, comparte un paso que darás esta semana, sin montos ni datos personales, y comenta el de otra persona. | Foro «Comunidad» | Colaborativa | Participación (no se califica) |\n"
              f"| {len(les[m]) + 2} | Autoevaluación del módulo {i} | Responde las preguntas de todas las lecciones del módulo. Puedes intentarlo las veces que quieras. | Cuestionario en la plataforma | Individual | Sumativa: {100 / nm:.4g}% de la calificación final; aprobado con 70% |\n\n")
        s += (f"**Criterios de evaluación:** la lección se acredita al verla completa; el módulo, al aprobar la autoevaluación con 70% o más. "
              f"La ponderación de cada reactivo está en el documento de instrumentos.\n\n")
        semana = b
    W("04_guias_actividades.md", s)

    # ---------- 05 calendario ----------
    s = cab("Calendario general de actividades (sugerido)")
    s += f"Curso a tu ritmo: las fechas son una guía de unas 2 horas por semana. Con fecha de inicio el {fecha(inicio)}:\n\n| Semana | Del | Al | Actividades |\n|---|---|---|---|\n"
    lunes = inicio - datetime.timedelta(days=inicio.weekday())
    filas = [(1, "Bienvenida, encuesta de inicio y evaluación diagnóstica; lectura de la información general")]
    semana = 2
    for i, m in enumerate(MODS, 1):
        n = sem[m]; ls = les[m]; per = math.ceil(len(ls) / n)
        for j in range(n):
            parte = ls[j * per:(j + 1) * per]
            if not parte: continue
            txt = f"Módulo {i} «{nombres[m]}»: lecciones {j * per + 1} a {j * per + len(parte)}"
            if j == n - 1: txt += f"; foro y autoevaluación del módulo {i}"
            filas.append((semana, txt)); semana += 1
    filas.append((semana, "Encuesta final y de satisfacción; descarga de la constancia"))
    for w, txt in filas:
        a = lunes + datetime.timedelta(weeks=w - 1); b = a + datetime.timedelta(days=6)
        s += f"| {w} | {a.isoformat()} | {b.isoformat()} | {txt} |\n"
    s += "\nSeguimiento: encuesta a los 30 y a los 90 días de terminar.\n"
    W("05_calendario_sugerido.md", s)

    # ---------- 06 instrumentos ----------
    s = cab("Instrumentos de evaluación del aprendizaje (EC0217 y EC0366)")
    s += "Cuestionarios de opción múltiple con una sola respuesta correcta, tres opciones y retroalimentación. Requisitos de diseño: objetividad, validez, confiabilidad y claridad; tres reactivos por lección, proporcionales a los contenidos.\n\n"
    for i, m in enumerate(MODS, 1):
        rs = [(l["title"], q) for l in les[m] for q in l["quiz"]]
        n = len(rs); val = 100 / n if n else 0; tmax = max(15, math.ceil(n * 0.75 / 5) * 5)
        s += (f"## Autoevaluación del módulo {i} · {nombres[m]}\n\n**Instrucciones:** lee cada pregunta y elige la mejor respuesta. Puedes intentarlo las veces que quieras; cuenta tu mejor intento. "
              f"Al terminar verás la respuesta correcta y por qué.\n\n**Tiempo máximo:** {tmax} minutos · **Reactivos:** {n} · **Valor de cada reactivo:** {val:.2f} puntos (total 100) · **Aprobación:** 70 puntos.\n\n"
              "| # | Lección | Reactivo | Opciones | Respuesta | Valor |\n|---|---|---|---|---|---|\n")
        for k, (lt, (q, opts, key, _)) in enumerate(rs, 1):
            ops = " · ".join(f"{chr(97 + j)}) {o}" for j, o in enumerate(opts))
            s += f"| {k} | {lt} | {q} | {ops} | {key} | {val:.2f} |\n"
        s += "\n"
    W("06_instrumentos_evaluacion.md", s)

    # ---------- 07 diagnóstica ----------
    elegidos = []
    for m in MODS:
        cand = [(l, q) for l in les[m] for q in l["quiz"][:1]]
        paso = max(1, len(cand) // 2)
        elegidos += cand[::paso][:2]
    s = cab("Evaluación diagnóstica de conocimientos")
    s += (f"Se aplica al inicio, junto con la encuesta de inicio. Explora lo que la persona ya sabe de cada módulo; **no cuenta para la calificación** y no se repite.\n\n"
          f"**Instrucciones:** responde sin consultar; si no sabes, elige la que te parezca mejor. **Tiempo máximo:** 10 minutos · **Reactivos:** {len(elegidos)} · **Valor de cada reactivo:** 1 punto.\n\n"
          "| # | Módulo | Reactivo | Opciones | Respuesta |\n|---|---|---|---|---|\n")
    g = f"$CATEGORY: $course$/{cfg.get('categoria', tit)}/Diagnóstica\n\n"
    for k, (l, (q, opts, key, e)) in enumerate(elegidos, 1):
        m = next(mm for mm in MODS if l in les[mm])
        s += f"| {k} | {nombres[m]} | {q} | {' · '.join(f'{chr(97 + j)}) {o}' for j, o in enumerate(opts))} | {key} |\n"
        esc = lambda t: re.sub(r"([~=#{}:])", r"\\\1", t)
        g += f"::DIAG {k}::{esc(q)} {{\n" + "".join(f"\t{'=' if chr(97 + j) == key else '~'}{esc(o)}\n" for j, o in enumerate(opts)) + "}\n\n"
    n = len(elegidos)
    cortes = [(math.ceil(n * .8), "Domina buena parte de los temas: puede tomar la ruta «Lo esencial»."), (math.ceil(n * .5), "Conoce algunos temas: se recomienda la ruta completa en los módulos con más errores."),
              (0, "Punto de partida inicial: se recomienda la ruta completa y, si hay sesiones, asistir a todas.")]
    s += "\n**Tabla de resultados**\n\n| Aciertos | Lectura |\n|---|---|\n" + "".join(f"| {c} o más | {t} |\n" if c else f"| Menos de {cortes[1][0]} | {t} |\n" for c, t in cortes)
    s += "\nArchivo para importar en el banco de preguntas: `07_diagnostica.gift.txt` (cuestionario sin calificación, un intento).\n"
    W("07_evaluacion_diagnostica.md", s); W("07_diagnostica.gift.txt", g)

    # ---------- 08 satisfacción ----------
    esc_ = ["Totalmente en desacuerdo", "En desacuerdo", "Ni de acuerdo ni en desacuerdo", "De acuerdo", "Totalmente de acuerdo"]
    bloques = [("El curso", ["El curso duró lo que se anunció.", "Me presentaron los objetivos y el temario desde el inicio.", "Los temas me sirven para mi vida diaria.",
                             "Las lecciones fueron claras y fáciles de entender.", "La práctica me ayudó a saber si había entendido."]),
               ("Los materiales", ["Los videos, imágenes y ejercicios fueron variados y útiles.", "Los materiales de apoyo me ayudaron a aprender.", "Pude descargar o consultar los materiales cuando los necesité."]),
               ("La plataforma", ["Fue fácil entrar y encontrar mis lecciones.", "Las lecciones se vieron bien en mi celular o computadora.", "Supe en todo momento cuánto me faltaba."]),
               ("La facilitación (solo si hubo sesiones presenciales o en vivo)", ["La facilitadora o el facilitador usó un lenguaje claro.", "Hizo preguntas para comprobar que entendíamos.",
                             "Usó dinámicas y trabajo en grupo.", "Respetó los horarios y el tiempo de cada sesión.", "Ajustó el ritmo cuando alguien no entendía."])]
    s = cab("Encuesta de satisfacción (evaluación de reacción)")
    s += "Anónima. Se responde al terminar, junto con la encuesta final. Escala: " + " · ".join(f"{i + 1} = {e}" for i, e in enumerate(esc_)) + ". El bloque de facilitación se omite en la versión 100% en línea.\n\n"
    items, k = [], 0
    for b, qs in bloques:
        s += f"## {b}\n\n"
        for q in qs:
            k += 1; s += f"**S{k}.** {q}\n\n"; items.append((f"S{k}", q))
    s += "## Para terminar\n\n**S%d.** Del 0 al 10, ¿qué tanto recomendarías el curso a alguien cercano?\n\n**S%d.** ¿Qué fue lo más útil? (abierta)\n\n**S%d.** ¿Qué mejorarías? (abierta)\n" % (k + 1, k + 2, k + 3)
    s += "\n**Lectura:** porcentaje de respuestas 4 y 5 por pregunta; meta: 85% o más en cada bloque. Archivo para Moodle (actividad Retroalimentación): `08_encuesta_satisfaccion.xml`.\n"
    W("08_encuesta_satisfaccion.md", s)
    pres = "r>>>>>" + "\n|".join(f"{i + 1}####{e}" for i, e in enumerate(esc_))
    x = '<?xml version="1.0" encoding="UTF-8" ?>\n<FEEDBACK VERSION="200701" COMMENT="XML-Importfile for mod/feedback">\n     <ITEMS>\n'
    allq = items + [(f"S{k + 1}", "Del 0 al 10, ¿qué tanto recomendarías el curso a alguien cercano?")]
    for n_, (lab, q) in enumerate(allq, 1):
        p = pres if lab != f"S{k + 1}" else "r>>>>>" + "\n|".join(f"{v}####{v}" for v in range(11))
        x += (f'          <ITEM TYPE="multichoicerated" REQUIRED="1">\n               <ITEMID><![CDATA[{n_}]]></ITEMID>\n               <ITEMTEXT><![CDATA[{q}]]></ITEMTEXT>\n'
              f'               <ITEMLABEL><![CDATA[{lab}]]></ITEMLABEL>\n               <PRESENTATION><![CDATA[{p}]]></PRESENTATION>\n               <OPTIONS><![CDATA[h]]></OPTIONS>\n'
              f'               <DEPENDITEM><![CDATA[0]]></DEPENDITEM>\n               <DEPENDVALUE><![CDATA[]]></DEPENDVALUE>\n          </ITEM>\n')
    for j, q in enumerate(["¿Qué fue lo más útil?", "¿Qué mejorarías?"], len(allq) + 1):
        x += (f'          <ITEM TYPE="textarea" REQUIRED="0">\n               <ITEMID><![CDATA[{j}]]></ITEMID>\n               <ITEMTEXT><![CDATA[{q}]]></ITEMTEXT>\n'
              f'               <ITEMLABEL><![CDATA[S{j}]]></ITEMLABEL>\n               <PRESENTATION><![CDATA[60|4]]></PRESENTATION>\n               <OPTIONS><![CDATA[]]></OPTIONS>\n'
              f'               <DEPENDITEM><![CDATA[0]]></DEPENDITEM>\n               <DEPENDVALUE><![CDATA[]]></DEPENDVALUE>\n          </ITEM>\n')
    W("08_encuesta_satisfaccion.xml", x + "     </ITEMS>\n</FEEDBACK>\n")

    # ---------- 09 carta descriptiva ----------
    s = cab("Carta descriptiva de las sesiones presenciales (EC0217)")
    s += (f"Para cuando una organización pide acompañar el curso en línea con sesiones de grupo: una sesión por módulo ({nm} sesiones). "
          f"La primera incluye el encuadre completo y la última el cierre completo. Grupo de 10 a 25 personas.\n\n**Objetivo general:** {og}\n\n")
    T = "| Momento | Actividades de quien facilita | Técnica grupal | Técnica instruccional | Recursos | Forma de evaluación | Instrumento | Tiempo |\n|---|---|---|---|---|---|---|---|\n"
    for i, m in enumerate(MODS, 1):
        prim, ult = i == 1, i == nm
        dur = 60 + (35 if prim else 0) + (35 if ult else 0)
        s += f"## Sesión {i} · {nombres[m]} ({dur} minutos)\n\n**Objetivo particular:** {particular(m)}\n\n" + T
        if prim:
            s += ("| Encuadre | Presentación del curso, de quien facilita y de cada participante | Presentación por parejas | Expositiva | Proyector o láminas | — | — | 10 min |\n"
                  "| Encuadre | Dinámica de integración | «Lo que me quita el sueño del dinero» en tarjetas anónimas | Interrogativa | Tarjetas y plumones | — | — | 5 min |\n"
                  "| Encuadre | Objetivos y temario; revisión y ajuste de expectativas | Lluvia de ideas | Expositiva e interrogativa | Rotafolio | — | — | 5 min |\n"
                  "| Encuadre | Reglas del grupo (respeto, confidencialidad, no compartir datos personales) y forma de trabajo | Consenso | Expositiva | Rotafolio | — | — | 5 min |\n"
                  "| Encuadre | Forma de evaluar y aplicación de la evaluación diagnóstica | — | Expositiva | Celular o formato impreso | Diagnóstica | Cuestionario diagnóstico | 10 min |\n")
        else:
            s += f"| Encuadre | Bienvenida, repaso de compromisos de la sesión anterior y objetivo de hoy | Ronda rápida | Interrogativa | Rotafolio | — | — | 5 min |\n"
        s += (f"| Desarrollo | Ideas clave del módulo; pedir que alguien explique una con sus palabras | Discusión en grupo | Expositiva y demostrativa | Video o libro de la lección, proyector | Formativa | Preguntas orales | 10 min |\n"
              f"| Desarrollo | Casos de la vida diaria del módulo | Grupos de 3 o 4 (estudio de casos) | Estudio de casos | Tarjetas con los casos | Formativa | Lista de cotejo del producto del módulo | 20 min |\n"
              f"| Desarrollo | Ejercicio con números y construcción del producto del módulo | Trabajo individual y en parejas | Demostración y práctica | Hojas de trabajo o herramienta descargable | Formativa | Lista de cotejo | 15 min |\n")
        if ult:
            s += ("| Cierre | Resumen general del curso y conclusiones | Recuperación en plenaria | Interrogativa | Rotafolio | — | — | 10 min |\n"
                  "| Cierre | Revisión del cumplimiento de expectativas | Plenaria | Interrogativa | Rotafolio de expectativas | — | — | 5 min |\n"
                  "| Cierre | Evaluación final (autoevaluación en línea) | — | — | Celular | Sumativa | Autoevaluaciones de módulo | 10 min |\n"
                  "| Cierre | Evaluación de satisfacción | — | — | Celular o formato impreso | Reacción | Encuesta de satisfacción | 5 min |\n"
                  "| Cierre | Compromiso por escrito con fecha y clausura con entrega de constancias | Ronda | — | Formato de compromiso y constancias | — | — | 10 min |\n\n")
        else:
            s += (f"| Cierre | Compromiso de la semana: un paso con fecha, dicho a su pareja de grupo | Parejas | — | Tarjeta de compromiso | — | — | 7 min |\n"
                  f"| Cierre | Recordar autoevaluación del módulo {i} y siguiente sesión | — | Expositiva | — | — | — | 3 min |\n\n")
    W("09_carta_descriptiva.md", s)

    # ---------- 10 listas de cotejo ----------
    s = cab("Listas de cotejo de los productos de cada módulo")
    s += "Sirven para revisar, en sesiones presenciales o por quien acompaña, el producto que la persona elabora en cada módulo. Se pueden usar datos de ejemplo: **nunca** se piden montos reales ni datos personales.\n\n"
    for i, m in enumerate(MODS, 1):
        s += f"## Módulo {i} · {nombres[m]}\n\n**Producto:** {tercera(res.get(m, nombres[m]))}\n\n| # | Criterio | Sí | No | Observaciones |\n|---|---|---|---|---|\n"
        crit = [criterio(l["plan"]) for l in les[m] if l["plan"]]
        for k, c in enumerate(crit, 1): s += f"| {k} | {c} | ☐ | ☐ | |\n"
        s += f"| {len(crit) + 1} | El producto está completo y la persona puede explicar para qué le sirve | ☐ | ☐ | |\n\n**Resultado:** cumple si marca «Sí» en al menos 80% de los criterios.\n\n"
    W("10_listas_cotejo.md", s)

    # ---------- 11 DNC ----------
    s = cab("Detección de necesidades de capacitación por cliente")
    s += ("Se llena con la organización que contrata (empresa, gobierno, fundación o cooperativa). **No se piden datos personales** de las personas participantes.\n\n"
          "| Dato | Respuesta |\n|---|---|\n| Organización | |\n| Persona de contacto y cargo | |\n| Fecha | |\n| Región o sede | |\n| Número aproximado de participantes | |\n"
          "| Perfil del grupo (ocupación, edades, escolaridad aproximada, idioma) | |\n| Modalidad deseada (en línea, híbrida, presencial) | |\n| Acceso a celular e internet del grupo | |\n| Fechas y horarios posibles | |\n\n"
          "## Necesidades por tema\n\n| Tema (módulo) | ¿Lo necesitan? (alta/media/baja) | Objetivo que buscan | Beneficio para la organización |\n|---|---|---|---|\n")
    s += "".join(f"| {nombres[m]} | | | |\n" for m in MODS)
    s += ("| Otro tema | | | |\n\n## Situaciones que motivan la capacitación\n\n☐ Deudas o descuentos de nómina · ☐ Estrés por dinero o ausentismo · ☐ Fraudes · ☐ Falta de ahorro para emergencias · "
          "☐ Retiro y pensión · ☐ Remesas · ☐ Otra: __________\n\n## Indicadores que quieren mover\n\n☐ Índice de bienestar financiero · ☐ Estrés financiero · ☐ Uso de productos formales · ☐ Ahorro de emergencia · ☐ Otro: __________\n\n"
          f"| Elaboró (Desarrolla Talento) | Validó (organización) |\n|---|---|\n| | |\n")
    W("11_deteccion_necesidades.md", s)

    # ---------- 12 reporte de revisión ----------
    urls = []
    for m in MODS:
        for u in re.findall(r"https?://[^\s)|>»\"]+", leer(os.path.join(D, "lecciones", f"{m}.md"))):
            u = u.rstrip(".,;")
            if u not in [x for x, _ in urls]: urls.append((u, m))
    s = cab("Reporte de revisión del funcionamiento del curso en la plataforma (EC0366)")
    s += (f"| Dato | |\n|---|---|\n| Nombre del curso | {tit} |\n| Desarrollador | {ELABORA} |\n| Fecha de revisión | [AAAA-MM-DD] |\n| Plataforma | Moodle · academia.desarrollatalento.com |\n\n"
          "## Comprobación contra los documentos\n\n| Se comprueba | Cumple | Observación |\n|---|---|---|\n"
          "| La información del curso en la plataforma coincide con el documento de información general | ☐ | |\n"
          "| El calendario de actividades en la plataforma coincide con el calendario sugerido | ☐ | |\n"
          "| Cada módulo tiene sus lecciones, práctica, foro y autoevaluación según la guía de actividades | ☐ | |\n"
          "| Las autoevaluaciones tienen los reactivos, tiempo y valores del documento de instrumentos | ☐ | |\n"
          "| La diagnóstica y la encuesta de satisfacción están activas | ☐ | |\n"
          "| La constancia se libera con las condiciones establecidas | ☐ | |\n\n"
          "## Observaciones\n\n| Tipo | Módulo o lección | Observación | Propuesta de modificación |\n|---|---|---|---|\n| Diseño | | | |\n| Contenido | | | |\n| Funcionalidad en la plataforma | | | |\n\n"
          f"## Enlaces externos del curso ({len(urls)})\n\nSe prueban todos antes de liberar el curso y cada 6 meses (`python3 herramientas_cursos/estandares.py --enlaces cursos/<curso>`).\n\n"
          "| # | Módulo | Enlace | Funciona | Fecha de prueba |\n|---|---|---|---|---|\n")
    s += "".join(f"| {k} | {m} | {u} | ☐ | |\n" for k, (u, m) in enumerate(urls, 1))
    s += "\n| Revisó | Firma |\n|---|---|\n| | |\n"
    W("12_reporte_revision.md", s)

    W("README.md", cab("Documentos de estándares") + "| # | Documento | Estándar |\n|---|---|---|\n" + "".join(f"| {a} | {b} | {c} |\n" for a, b, c in [
        ("01", "Objetivos de aprendizaje (general, particulares y específicos)", "EC0217 · EC0366"), ("02", "Información general del curso", "EC0366"),
        ("03", "Cronograma de desarrollo", "EC0366"), ("04", "Guías de actividades de aprendizaje por módulo", "EC0366"), ("05", "Calendario general sugerido", "EC0366"),
        ("06", "Instrumentos de evaluación con tiempo y valor por reactivo", "EC0217 · EC0366"), ("07", "Evaluación diagnóstica (+ GIFT)", "EC0217"),
        ("08", "Encuesta de satisfacción (+ XML)", "EC0217"), ("09", "Carta descriptiva con encuadre y cierre completos", "EC0217"),
        ("10", "Listas de cotejo de productos", "EC0217"), ("11", "Detección de necesidades por cliente", "EC0217"), ("12", "Reporte de revisión y enlaces", "EC0366")]))
    print(f"{os.path.basename(D)} · {nl} lecciones · {nm} módulos · {h(tot[0])}–{h(tot[1])} h · {nsem} semanas · {len(urls)} enlaces")


def enlaces(D):
    import urllib.request
    urls = set()
    for f in os.listdir(os.path.join(D, "lecciones")):
        urls |= {u.rstrip(".,;") for u in re.findall(r"https?://[^\s)|>»\"]+", leer(os.path.join(D, "lecciones", f)))}
    ok = mal = 0
    for u in sorted(urls):
        try:
            r = urllib.request.urlopen(urllib.request.Request(u, method="HEAD", headers={"User-Agent": "Mozilla/5.0"}), timeout=15); est = r.status
        except Exception as e:
            est = getattr(e, "code", None) or type(e).__name__
        bien = isinstance(est, int) and est < 400
        ok += bien; mal += not bien
        print(("OK  " if bien else "MAL ") + f"{est}  {u}")
    print(f"{ok} funcionan · {mal} con problema")


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--enlaces":
        for d in a[1:]: enlaces(d)
    else:
        ini = datetime.date(2026, 11, 2)
        if "--inicio" in a:
            i = a.index("--inicio"); ini = datetime.date.fromisoformat(a[i + 1]); a = a[:i] + a[i + 2:]
        for d in a: curso(os.path.abspath(d), ini)
