# Paquete del curso completo 3.1: libros, H5P, glosario, banco, insignias, certificado, guías y README.
# Uso: python3 herramientas/curso_completo_v31.py <carpeta TDTF_05 descomprimida> <num>
import re, os, shutil, zipfile, sys, subprocess, glob
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V1, num = sys.argv[1], sys.argv[2]
name = f"TDTF_{num}_Curso_completo_v3.1"
out = os.path.join("/tmp", name); shutil.rmtree(out, ignore_errors=True)
D = {k: os.path.join(out, k) for k in ["1_libros", "2_h5p", "3_glosario", "4_preguntas", "5_insignias", "6_certificado", "7_guias"]}
for d in D.values(): os.makedirs(d)
V3 = os.path.join(BASE, "moodle/v3")
entries, seen = [], set()
for m in ["M1", "M2", "M3", "M4", "M5"]:
    shutil.copy(f"{V3}/{m}/{m}_libro_Moodle.zip", D["1_libros"])
    shutil.copy(f"{V1}/libros/es/{m}_resumen.html", D["1_libros"])
    x = open(f"{V3}/{m}/{m}_glosario_Moodle.xml", encoding="utf-8").read()
    for e in re.findall(r"<ENTRY>.*?</ENTRY>", x, re.S):
        c = re.search(r"<CONCEPT>(.*?)</CONCEPT>", e, re.S).group(1).strip().lower()
        if c not in seen: seen.add(c); entries.append(e)
    os.makedirs(f"{D['2_h5p']}/{m}")
    for h in sorted(glob.glob(f"{V3}/h5p/{m}_U*.h5p")): shutil.copy(h, f"{D['2_h5p']}/{m}")
shutil.copy(f"{V3}/Apoyo/Apoyo_libro_Moodle.zip", D["1_libros"])
head = x.split("<ENTRIES>")[0].replace("Palabras clave · M5", "Palabras clave del curso")
open(f"{D['3_glosario']}/Glosario_curso_Moodle.xml", "w", encoding="utf-8").write(head + "<ENTRIES>\n" + "\n".join(entries) + "\n</ENTRIES></INFO></GLOSSARY>\n")
shutil.copy(f"{V3}/banco_preguntas_v3_es.gift.txt", D["4_preguntas"])
for p in glob.glob(f"{V3}/insignias/*.png"): shutil.copy(p, D["5_insignias"])
for p in glob.glob(f"{V3}/certificado/*.png"): shutil.copy(p, D["6_certificado"])
shutil.copy(f"{V3}/guia_gamificacion_v3.md", D["7_guias"])
S = "/tmp/claude-0/-home-user-peekabook/2b8c84d1-874b-559e-a5dd-06af4ddd1637/scratchpad"
subprocess.run(["node", "herramientas/md2docx.js", f"{D['7_guias']}/guia_gamificacion_v3.docx", "Tu Dinero, Tu Familia, Tu Futuro",
                "Actividades, puntos, insignias y constancia · Versión 3 · Septiembre de 2026", f"{V3}/guia_gamificacion_v3.md"],
               cwd=BASE, env=dict(os.environ, NODE_PATH=f"{S}/nodeenv/node_modules"), check=True, capture_output=True)
for f in glob.glob(os.path.join(BASE, "moodle/instalacion_v31/*")): shutil.copy(f, out)
z = os.path.join(os.path.dirname(BASE), "entregas", f"{name}_2026-09-28.zip")
with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
    for r, _, fs in os.walk(out):
        for f in sorted(fs):
            p = os.path.join(r, f); zf.write(p, os.path.join(name, os.path.relpath(p, out)))
print(z, os.path.getsize(z) // 1024 // 1024, "MB ·", len(entries), "términos ·", len(glob.glob(f"{out}/2_h5p/*/*.h5p")), "H5P")
