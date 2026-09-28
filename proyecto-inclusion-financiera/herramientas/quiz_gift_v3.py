# Banco de preguntas (GIFT) a partir de los quizzes de manual/v3/es, con tres opciones por pregunta.
import re, os, glob, sys
sys.path.insert(0, os.path.dirname(__file__))
from datos_banco import EXTRA
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def esc(t): return re.sub(r"([~=#{}:])", r"\\\1", re.sub(r"\{\{([^|}]+)\|[^}]+\}\}", r"\1", t).replace("*", "").strip())
out, cur, n, probs = [], None, 0, []
for f in sorted(glob.glob(os.path.join(BASE, "manual/v3/es/M*.md"))):
    for les in re.split(r"(?m)^# (?=M\d U\d\d)", open(f).read())[1:]:
        code, title = [x.strip() for x in les.split("\n", 1)[0].split("|", 1)]
        q = re.search(r"--- quiz\n(.*?)\nrespuestas:\s*(.*?)\n", les, re.S)
        ans = {k: (l, why.strip()) for k, l, why in re.findall(r"(\d+)-([a-c]):\s*(.*?)(?=\s\d+-[a-c]:|$)", q.group(2))}
        mod = code.split()[0]
        if mod != cur:
            out.append(f"$CATEGORY: $course$/Tu Dinero v3/{mod}\n"); cur = mod
        for k, line in re.findall(r"(?m)^(\d+)\.\s+(.*)$", q.group(1)):
            parts = re.split(r"\s+(?=[a-c]\)\s)", line)
            stem, opts = parts[0], [re.sub(r"\s*·\s*$", "", o) for o in parts[1:]]
            key = f"{code} P{k}"
            if k not in ans: probs.append(key); continue
            good, why = ans[k]
            why = why[:1].upper() + why[1:]
            body = []
            for o in opts:
                body.append(("=" if o[0] == good else "~") + esc(o[3:]) + (f" #¡Correcto! {esc(why)}" if o[0] == good else f" #No es la mejor opción. {esc(why)}"))
            if len(opts) == 2:
                if key not in EXTRA: probs.append(key + " sin tercera opción")
                else: body.append("~" + esc(EXTRA[key]) + f" #No es la mejor opción. {esc(why)}")
            out.append(f"::{key}::{esc(stem)} {{\n" + "\n".join("\t" + b for b in body) + "\n}\n")
            n += 1
p = os.path.join(BASE, "moodle/v3/banco_preguntas_v3_es.gift.txt")
open(p, "w").write("\n".join(out))
print(n, "preguntas ·", p, "· problemas:", probs)
