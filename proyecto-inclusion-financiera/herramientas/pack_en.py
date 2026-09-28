# Empaqueta un módulo en inglés: libro, glosario, H5P, banco (solo ese módulo), Word, vista previa y LEEME.
# Uso: python3 herramientas/pack_en.py M1 20   (antes: build_v3.py --en M1, h5p_casos.py --en, quiz_gift_v3.py --en)
import os, sys, json, re, shutil, zipfile, subprocess, glob
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
mod, num = sys.argv[1], sys.argv[2]
S = "/tmp/claude-0/-home-user-peekabook/2b8c84d1-874b-559e-a5dd-06af4ddd1637/scratchpad"
d = os.path.join(BASE, "moodle/v3/en", mod)
subprocess.run(["node", "herramientas/md2docx.js", f"{d}/{mod}_Lessons_EN.docx", "Your Money, Your Family, Your Future",
                f"Module {mod[1]} · New format (5 and 10 minutes) · Version 3.2 · September 2026", f"{d}/{mod}_legible.md"],
               cwd=BASE, env=dict(os.environ, NODE_PATH=f"{S}/nodeenv/node_modules"), check=True, capture_output=True)
g = open(os.path.join(BASE, "moodle/v3/en/banco_preguntas_v3_en.gift.txt")).read()
part = re.search(rf"(\$CATEGORY: \$course\$/Your Money v3/{mod}\n.*?)(?=\$CATEGORY|\Z)", g, re.S).group(1)
open(f"{d}/{mod}_question_bank_EN.gift.txt", "w").write(part)
c = json.load(open(f"{d}/conteo.json"))
name = f"TDTF_{num}_Module{mod[1]}_EN_v3.2"
out = os.path.join("/tmp", name); shutil.rmtree(out, ignore_errors=True); os.makedirs(out)
for f in [f"{mod}_libro_Moodle.zip", f"{mod}_glosario_Moodle.xml", f"{mod}_Lessons_EN.docx", f"{mod}_question_bank_EN.gift.txt"]:
    shutil.copy(f"{d}/{f}", out)
shutil.copytree(f"{d}/vista_previa", f"{out}/vista_previa")
os.makedirs(f"{out}/h5p")
for h in sorted(glob.glob(os.path.join(BASE, f"moodle/v3/en/h5p/{mod}_U*.h5p"))): shutil.copy(h, f"{out}/h5p")
L = [f"ENTREGA {num}: MÓDULO {mod[1]} EN INGLÉS (VERSIÓN 3.2)", "Your Money, Your Family, Your Future · Desarrolla Talento · 28 de septiembre de 2026", "",
     "QUÉ CONTIENE", "------------",
     f"{mod}_libro_Moodle.zip           {c['paginas']} páginas ({c['lecciones']} lecciones x 4) para 'Importar capítulo' en un Libro.",
     f"{mod}_glosario_Moodle.xml        Glosario en inglés ({c['terminos']} términos).",
     f"h5p/                        {len(glob.glob(out + '/h5p/*.h5p'))} actividades 'What would you do?' (una por lección).",
     f"{mod}_question_bank_EN.gift.txt   Banco de preguntas del módulo (categoría 'Your Money v3/{mod}').",
     f"{mod}_Lessons_EN.docx          Las lecciones en Word para revisar.",
     "vista_previa/ABRIR_AQUI.html  Así se verá en Moodle.", "",
     "CÓMO SE USA", "-----------",
     "Es la misma estructura que la versión en español (entrega 18), para un segundo curso en inglés.",
     "Se instala con los mismos pasos de README_ACTUALIZAR_CURSO_PARA_CLAUDE.md / README_INSTALAR_DESDE_CERO,",
     "cambiando los nombres de archivo. Nombre sugerido del curso: Your Money, Your Family, Your Future (California pilot),",
     "nombre corto TDTF-CA-EN.", "",
     "CRITERIOS DE LA TRADUCCIÓN", "--------------------------",
     "- Inglés de EE. UU., sencillo, en segunda persona; mismos personajes, casos, números y datos que la versión en español.",
     "- A Alex no se le asigna género (el elenco no lo define); Mar, Daniela y Rosa en femenino; Luis y Andrés en masculino.",
     "- Enlaces: versión en inglés de cada recurso oficial; se indica si también existe en español.",
     "- Las opciones de las actividades H5P tienen largo parecido para no dar pistas.", "",
     "EXTENSIÓN POR LECCIÓN (palabras: Lo esencial / lección completa)", "-------------------------------------------------------------"]
L += [f"{code}: {e} / {e + p}" for code, e, p in c["conteo"]]
L += ["", "PENDIENTES", "----------", "Los mismos de la versión en español (K06 a K13). Revisión recomendada por una persona nativa de inglés antes del piloto en inglés."]
open(f"{out}/LEEME.txt", "w").write("\n".join(L) + "\n")
z = os.path.join(os.path.dirname(BASE), "entregas", f"{name}_2026-09-28.zip")
with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
    for r, _, fs in os.walk(out):
        for f in sorted(fs):
            p = os.path.join(r, f); zf.write(p, os.path.join(name, os.path.relpath(p, out)))
print(z, round(os.path.getsize(z) / 1048576, 1), "MB")
