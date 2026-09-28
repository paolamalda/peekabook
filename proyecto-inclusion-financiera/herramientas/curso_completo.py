# Arma el paquete del curso completo (formato v3) para subir a Moodle 3.10.
import re, os, shutil, zipfile, sys
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V1 = sys.argv[1]            # carpeta descomprimida de TDTF_05 (libro de apoyo, resúmenes, preguntas, guías)
num, fecha = sys.argv[2], "2026-09-28"
name = f"TDTF_{num}_Curso_completo_v3"
out = os.path.join("/tmp", name); shutil.rmtree(out, ignore_errors=True)
for d in ["1_libros", "2_glosario", "3_preguntas", "4_guias"]: os.makedirs(os.path.join(out, d))
mods = ["M1", "M2", "M3", "M4", "M5"]
entries, seen = [], set()
for m in mods:
    v3 = os.path.join(BASE, "moodle/v3", m)
    shutil.copy(os.path.join(v3, f"{m}_libro_Moodle.zip"), os.path.join(out, "1_libros", f"{m}_libro_Moodle.zip"))
    shutil.copy(os.path.join(V1, "libros/es", f"{m}_resumen.html"), os.path.join(out, "1_libros", f"{m}_resumen.html"))
    x = open(os.path.join(v3, f"{m}_glosario_Moodle.xml"), encoding="utf-8").read()
    for e in re.findall(r"<ENTRY>.*?</ENTRY>", x, re.S):
        c = re.search(r"<CONCEPT>(.*?)</CONCEPT>", e, re.S).group(1).strip().lower()
        if c not in seen: seen.add(c); entries.append(e)
shutil.copy(os.path.join(V1, "libros/es/Apoyo.zip"), os.path.join(out, "1_libros", "Apoyo_libro_Moodle.zip"))
head = x.split("<ENTRIES>")[0].replace("Palabras clave · M5", "Palabras clave del curso")
open(os.path.join(out, "2_glosario", "Glosario_curso_Moodle.xml"), "w", encoding="utf-8").write(
    head + "<ENTRIES>\n" + "\n".join(entries) + "\n</ENTRIES></INFO></GLOSSARY>\n")
shutil.copy(os.path.join(V1, "preguntas/banco_preguntas_es.gift.txt"), os.path.join(out, "3_preguntas"))
for g in ["Guia_LevelUp_Insignias_ES.docx", "Guiones_H5P_ES.docx"]:
    shutil.copy(os.path.join(V1, "guias", g), os.path.join(out, "4_guias"))
shutil.copy(os.path.join(BASE, "moodle/instalacion_v3/LEEME.txt"), out)
shutil.copy(os.path.join(BASE, "moodle/instalacion_v3/README_PARA_CLAUDE.md"), out)
z = os.path.join(os.path.dirname(BASE), "entregas", f"{name}_{fecha}.zip")
with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
    for r, _, fs in os.walk(out):
        for f in sorted(fs):
            p = os.path.join(r, f); zf.write(p, os.path.join(name, os.path.relpath(p, out)))
print(z, len(entries), "términos")
