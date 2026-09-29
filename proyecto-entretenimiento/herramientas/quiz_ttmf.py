# Tu Talento: banco de preguntas GIFT a partir de los quizzes de manual/lecciones (tres opciones por pregunta).
import re, os, glob
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def esc(t): return re.sub(r"([~=#{}:])", r"\\\1", re.sub(r"\{\{([^|}]+)\|[^}]+\}\}", r"\1", t).replace("*", "").strip())
out, cur, n, probs = [], None, 0, []
files = sorted(glob.glob(os.path.join(BASE, "manual/lecciones", "M*.md")), key=lambda p: int(re.search(r"M(\d+)", os.path.basename(p)).group(1)))
for f in files:
    for les in re.split(r"(?m)^# (?=M\d+ U\d\d)", open(f).read())[1:]:
        code = les.split("|", 1)[0].strip()
        q = re.search(r"--- quiz\n(.*?)\nrespuestas:\s*(.*?)\n", les, re.S)
        ans = {k: (l, why.strip()) for k, l, why in re.findall(r"(\d+)-([a-c]):\s*(.*?)(?=\s\d+-[a-c]:|$)", q.group(2))}
        mod = code.split()[0]
        if mod != cur:
            out.append(f"$CATEGORY: $course$/Tu Talento/{mod}\n"); cur = mod
        for k, line in re.findall(r"(?m)^(\d+)\.\s+(.*)$", q.group(1)):
            parts = re.split(r"\s+(?=[a-c]\)\s)", line)
            stem, opts = parts[0], [re.sub(r"\s*·\s*$", "", o) for o in parts[1:]]
            if k not in ans or len(opts) != 3: probs.append(f"{code} P{k}"); continue
            good, why = ans[k]; why = why[:1].upper() + why[1:]
            body = [("=" if o[0] == good else "~") + esc(o[3:]) + (f" #¡Correcto! {esc(why)}" if o[0] == good else f" #No es la mejor opción. {esc(why)}") for o in opts]
            out.append(f"::{code} P{k}::{esc(stem)} {{\n" + "\n".join("\t" + b for b in body) + "\n}\n")
            n += 1
p = os.path.join(BASE, "moodle", "banco_preguntas_ttmf.gift.txt")
open(p, "w").write("\n".join(out))
print(n, "preguntas ·", p, "· problemas:", probs)
