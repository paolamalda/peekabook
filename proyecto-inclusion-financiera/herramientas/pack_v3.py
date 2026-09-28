# Empaqueta un módulo del formato nuevo: Word, LEEME y zip de entrega.
# Uso: python3 herramientas/pack_v3.py M2 10 "notas de cambios" "pendientes por revisar"
import json, os, sys, subprocess, shutil, zipfile
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
mod, num, cambios, revisar = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
S = "/tmp/claude-0/-home-user-peekabook/2b8c84d1-874b-559e-a5dd-06af4ddd1637/scratchpad"
d = os.path.join(BASE, "moodle", "v3", mod)
env = dict(os.environ, NODE_PATH=f"{S}/nodeenv/node_modules")
subprocess.run(["node", "herramientas/md2docx.js", f"{d}/{mod}_Lecciones_v3.docx", "Tu Dinero, Tu Familia, Tu Futuro",
                f"Módulo {mod[1]} · Formato nuevo (5 y 10 minutos) · Versión 3 · Septiembre de 2026", f"{d}/{mod}_legible.md"],
               cwd=BASE, env=env, check=True, capture_output=True)
c = json.load(open(f"{d}/conteo.json"))
L = [f"ENTREGA {num}: MÓDULO {mod[1]} EN FORMATO NUEVO", "Tu Dinero, Tu Familia, Tu Futuro · Desarrolla Talento · 28 de septiembre de 2026", "",
     "QUÉ CONTIENE", "------------",
     f"{mod}_Lecciones_v3.docx         Las {c['lecciones']} lecciones para leer y revisar en Word.",
     "vista_previa/ABRIR_AQUI.html  Ábrelo con doble clic: así se verá en Moodle.",
     f"{mod}_libro_Moodle.zip           {c['paginas']} páginas ({c['lecciones']} lecciones x 4) para importar en un Libro.",
     f"{mod}_glosario_Moodle.xml        Glosario con los {c['terminos']} términos del módulo.",
     f"{mod}a.md / {mod}b.md               Texto editable (formato para el generador).", "",
     "CÓMO SUBIRLO A MOODLE", "---------------------",
     f"1. En la sección del Módulo {mod[1]}: Agregar actividad > Libro > 'Lecciones del Módulo {mod[1]}' >",
     f"   Guardar y mostrar > Importar capítulo > sube {mod}_libro_Moodle.zip >",
     "   'Cada archivo HTML representa un capítulo'.",
     f"2. Agregar actividad > Glosario > 'Palabras clave del Módulo {mod[1]}' > Importar entradas >",
     f"   sube {mod}_glosario_Moodle.xml.",
     "3. No edites los capítulos con el editor de Moodle; corrige el archivo y reimporta.", "",
     "QUÉ CAMBIÓ EN ESTE MÓDULO", "------------------------"] + [l for l in cambios.split("\\n")] + ["",
     "EXTENSIÓN POR LECCIÓN (palabras: Lo esencial / lección completa)", "-------------------------------------------------------------"]
L += [f"{code}: {e} / {e+p}" for code, e, p in c["conteo"]]
L += ["", "A ritmo de lectura pausada (90 a 110 palabras por minuto) y con las pausas para",
      "responder, Lo esencial toma unos 4 a 5 minutos y la lección completa unos 9 a 10.", "",
      "POR REVISAR ANTES DE PUBLICAR (también en el plan maestro)", "--------------------------------------------------------"] + [l for l in revisar.split("\\n")]
open(f"{d}/LEEME.txt", "w").write("\n".join(L))
name = f"TDTF_{num}_Modulo{mod[1]}_v3"
st = f"{S}/pack_{mod}/{name}"
shutil.rmtree(f"{S}/pack_{mod}", ignore_errors=True)
os.makedirs(st)
shutil.copytree(f"{d}/vista_previa", f"{st}/vista_previa")
for f in [f"{mod}_Lecciones_v3.docx", f"{mod}_libro_Moodle.zip", f"{mod}_glosario_Moodle.xml", "LEEME.txt"]:
    shutil.copy(f"{d}/{f}", st)
for f in os.listdir(f"{BASE}/manual/v3/es"):
    if f.startswith(mod):
        shutil.copy(f"{BASE}/manual/v3/es/{f}", st)
out = f"/home/user/peekabook/entregas/{name}_2026-09-28.zip"
subprocess.run(["zip", "-qr", out, name], cwd=f"{S}/pack_{mod}", check=True)
print(out)
