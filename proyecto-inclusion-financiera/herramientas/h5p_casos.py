# Genera una actividad H5P (Single Choice Set) por lección con los casos de manual/v3/es.
# Incluye las librerías (versiones compatibles con el núcleo H5P 1.24 de Moodle 3.10).
# Uso: python3 herramientas/h5p_casos.py /ruta/librerias_h5p carpeta_salida
import re, os, sys, json, glob, zipfile, html
sys.path.insert(0, os.path.dirname(__file__))
EN = "--en" in sys.argv
sys.argv = [a for a in sys.argv if a != "--en"]
if EN:
    from datos_casos_en import CASOS
else:
    from datos_casos import CASOS
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIB, OUT = sys.argv[1], sys.argv[2]
LIBS = [("H5P.SingleChoiceSet", "scs"), ("H5P.JoubelUI", "h5p-joubel-ui"), ("H5P.Question", "h5p-question"),
        ("H5P.Transition", "h5p-transition"), ("H5P.FontIcons", "h5p-font-icons"), ("FontAwesome", "fa")]
OK = re.compile(r"\.(js|css|json|png|jpg|jpeg|gif|svg|eot|ttf|woff|woff2|otf|mp3|ogg|wav)$", re.I)
lib_files, deps = [], []
for mach, d in LIBS:
    meta = json.load(open(os.path.join(LIB, d, "library.json")))
    folder = f"{mach}-{meta['majorVersion']}.{meta['minorVersion']}"
    deps.append({"machineName": mach, "majorVersion": meta["majorVersion"], "minorVersion": meta["minorVersion"]})
    for r, ds, fs in os.walk(os.path.join(LIB, d)):
        ds[:] = [x for x in ds if not x.startswith(".") and x not in ("node_modules", "test", "tests")]
        for f in fs:
            if f.startswith(".") or not OK.search(f): continue
            if os.path.basename(r) == "language" and f not in ("es.json", "es-mx.json", ".en.json"): continue
            p = os.path.join(r, f)
            lib_files.append((p, folder + "/" + os.path.relpath(p, os.path.join(LIB, d))))
L10N = {"nextButtonLabel": "Siguiente caso", "showSolutionButtonLabel": "Ver respuestas", "retryButtonLabel": "Intentar de nuevo",
        "solutionViewTitle": "Respuestas", "correctText": "¡Correcto!", "incorrectText": "No es la mejor opción",
        "shouldSelect": "Esta era la mejor opción", "shouldNotSelect": "Esta no era la mejor opción",
        "muteButtonLabel": "Silenciar sonidos", "closeButtonLabel": "Cerrar", "slideOfTotal": "Caso :num de :total",
        "scoreBarLabel": "Obtuviste :num de :total puntos", "solutionListQuestionNumber": "Caso :num",
        "a11yShowSolution": "Mostrar las respuestas.", "a11yRetry": "Reiniciar la actividad."}
if EN:
    L10N = {"nextButtonLabel": "Next case", "showSolutionButtonLabel": "See answers", "retryButtonLabel": "Try again",
            "solutionViewTitle": "Answers", "correctText": "Correct!", "incorrectText": "Not the best option",
            "shouldSelect": "This was the best option", "shouldNotSelect": "This wasn't the best option",
            "muteButtonLabel": "Mute sounds", "closeButtonLabel": "Close", "slideOfTotal": "Case :num of :total",
            "scoreBarLabel": "You got :num out of :total points", "solutionListQuestionNumber": "Case :num",
            "a11yShowSolution": "Show the answers.", "a11yRetry": "Restart the activity."}
FB = (["Review the cases in Go deeper and try again.", "Great job! You know what to do in these situations."] if EN else
      ["Revisa los casos en Profundiza e inténtalo otra vez.", "¡Muy bien! Ya sabes qué hacer en estas situaciones."])
os.makedirs(OUT, exist_ok=True)
n = 0
for f in sorted(glob.glob(os.path.join(BASE, "manual/v3", "en" if EN else "es", "M*.md"))):
    for les in re.split(r"(?m)^# (?=M\d U\d\d)", open(f).read())[1:]:
        code, title = [x.strip() for x in les.split("\n", 1)[0].split("|", 1)]
        if code not in CASOS: continue
        cs = re.search(r"--- casos\n(.*?)\n--- ", les, re.S).group(1)
        choices = []
        for c, opts in zip(re.split(r"(?m)^### ", cs)[1:], CASOS[code]):
            h, b = c.split("\n", 1)
            ctx = " ".join(l for l in b.splitlines() if l.strip() and not l.startswith("? "))
            ctx = re.sub(r"\{\{([^|}]+)\|[^}]+\}\}", r"\1", ctx)
            q = re.search(r"(?m)^\? (.+?)\s*\|\|", b).group(1)
            name = re.sub(r"^(Caso|Case) \d+\.\s*", "", h.strip())
            choices.append({"question": f"<p><strong>{html.escape(name)}.</strong> {html.escape(ctx)}</p><p><strong>{html.escape(q)}</strong></p>",
                            "answers": [f"<p>{html.escape(o)}</p>" for o in opts]})
        content = {"choices": choices,
                   "overallFeedback": [{"from": 0, "to": 66, "feedback": FB[0]},
                                       {"from": 67, "to": 100, "feedback": FB[1]}],
                   "behaviour": {"autoContinue": False, "timeoutCorrect": 2000, "timeoutWrong": 3000, "soundEffectsEnabled": False,
                                 "enableRetry": True, "enableSolutionsButton": True, "passPercentage": 67},
                   "l10n": L10N}
        h5pjson = {"title": f"{code} " + ("What would you do?" if EN else "¿Qué harías?"), "language": "en" if EN else "es", "mainLibrary": "H5P.SingleChoiceSet",
                   "embedTypes": ["div", "iframe"], "license": "U", "defaultLanguage": "en" if EN else "es", "preloadedDependencies": deps}
        dest = os.path.join(OUT, f"{code.replace(' ', '_')}_" + ("what_would_you_do" if EN else "que_harias") + ".h5p")
        with zipfile.ZipFile(dest, "w", zipfile.ZIP_DEFLATED) as z:
            z.writestr("h5p.json", json.dumps(h5pjson, ensure_ascii=False, indent=1))
            z.writestr("content/content.json", json.dumps(content, ensure_ascii=False))
            for p, a in lib_files: z.write(p, a)
        n += 1
print(n, "actividades H5P en", OUT, "·", len(lib_files), "archivos de librerías por paquete")
