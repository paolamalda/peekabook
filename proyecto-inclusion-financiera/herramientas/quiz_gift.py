# Convierte los quizzes del manual al formato GIFT de Moodle (banco de preguntas), ES y EN.
import re, os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = ["M1a.md","M1b.md","M2a.md","M2b.md","M3.md","M4a.md","M4b.md","M5a.md","M5b.md"]
CFG = {"es": ("### Quiz", "**Respuestas:**"), "en": ("### Quiz", "**Answers:**")}
def esc(t): return re.sub(r"([~=#{}:])", r"\\\1", t.replace("*", "").strip())
def parse(lang):
    qhead, ahead = CFG[lang]; out, problems = [], []
    for f in FILES:
        text = open(os.path.join(BASE, "manual", lang, f)).read()
        for les in re.split(r"(?m)^## (?=M\d U\d\d\.)", text)[1:]:
            code, title = re.match(r"(M\d U\d\d)\.\s*(.*)", les).groups()
            m = re.search(re.escape(qhead) + r"\n(.*?)\n###", les, re.S)
            if not m: problems.append(code + " sin quiz"); continue
            block = m.group(1)
            qs = re.findall(r"(?m)^(\d+)\.\s+(.*)$", block)
            am = re.search(re.escape(ahead) + r"\s*(.*)", block)
            if not am: problems.append(code + " sin respuestas"); continue
            ans = {n: (l, why) for n, l, why in re.findall(r"(\d+)-([a-e])\s*(?:\(([^)]*)\))?", am.group(1))}
            for n, q in qs:
                parts = re.split(r"\s+(?=[a-e]\)\s)", q)
                stem, opts = parts[0], parts[1:]
                opts = [re.sub(r"\s*·\s*$", "", o) for o in opts]
                if len(opts) < 2 or n not in ans: problems.append(f"{code} P{n}"); continue
                good, why = ans[n]
                body = []
                for o in opts:
                    letter, txt = o[0], o[3:].strip()
                    fb = f" #{esc(why)}" if letter == good and why else ""
                    body.append(("=" if letter == good else "~") + esc(txt) + fb)
                out.append((code, title, n, stem, body))
    return out, problems
for lang in ("es", "en"):
    qs, probs = parse(lang)
    p = os.path.join(BASE, "moodle", f"banco_preguntas_{lang}.gift.txt")
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w") as fh:
        cur = None
        for code, title, n, stem, body in qs:
            mod = code.split()[0]
            if mod != cur:
                fh.write(f"$CATEGORY: $course$/{'Tu Dinero' if lang=='es' else 'Your Money'}/{mod}\n\n"); cur = mod
            fh.write(f"::{code} P{n}::{esc(stem)} {{\n" + "\n".join("\t" + b for b in body) + "\n}\n\n")
    print(lang, len(qs), "preguntas; problemas:", probs)
