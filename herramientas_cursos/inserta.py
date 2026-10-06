# Inserta bloques en una lección: esencial (antes de «--- comprueba»), profundiza (antes de «--- casos») o recursos (al final de la lista).
import re

def inserta(archivo, codigo, donde, texto):
    s = open(archivo).read()
    i = s.index(f"# {codigo} |")
    m = re.search(r"(?m)^# M\d+ U\d+ \|", s[i + 1:]); j = i + 1 + m.start() if m else len(s)
    les = s[i:j]
    if texto.strip().splitlines()[0] in les: return False  # ya está
    if donde == "recursos":
        k = les.index("== recursos\n") + len("== recursos\n")
        fin = re.search(r"(?m)^(?!- ).*$", les[k:]); k2 = k + fin.start()
        les = les[:k2] + texto.strip() + "\n" + les[k2:]
    else:
        ancla = "--- comprueba" if donde == "esencial" else "--- casos"
        k = les.index(ancla) if donde == "esencial" else les.index(ancla, les.index("== profundiza"))
        les = les[:k] + texto.strip() + "\n\n" + les[k:]
    open(archivo, "w").write(s[:i] + les + s[j:])
    return True
