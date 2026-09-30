# Tu Talento: arma el curso completo en 3 zips (curso, H5P M1-M6, H5P M7-M11). Uso: python3 herramientas/paquete_ttmf.py
import re, os, glob, shutil, zipfile, subprocess, sys
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE, "herramientas")); from build_ttmf import TITULOS
name = "TTMF_06_Curso_completo_v1.3"
out = os.path.join("/tmp", name); shutil.rmtree(out, ignore_errors=True)
D = {k: os.path.join(out, k) for k in ["1_libros", "2_h5p", "3_glosario", "4_preguntas", "5_insignias", "6_certificado", "7_guias", "8_vista_previa"]}
for d in D.values(): os.makedirs(d)
M = os.path.join(BASE, "moodle"); mods = list(TITULOS)
entries, seen, pend = [], set(), []
for m in mods:
    shutil.copy(f"{M}/{m}/{m}_libro_Moodle.zip", D["1_libros"]); shutil.copy(f"{M}/{m}/{m}_resumen.html", D["1_libros"])
    x = open(f"{M}/{m}/{m}_glosario_Moodle.xml", encoding="utf-8").read()
    for e in re.findall(r"<ENTRY>.*?</ENTRY>", x, re.S):
        c = re.search(r"<CONCEPT>(.*?)</CONCEPT>", e, re.S).group(1).strip().lower()
        if c not in seen: seen.add(c); entries.append(e)
    os.makedirs(f"{D['2_h5p']}/{m}")
    for h in sorted(glob.glob(f"{M}/h5p/{m}_U*.h5p")): shutil.copy(h, f"{D['2_h5p']}/{m}")
    shutil.copytree(f"{M}/{m}/vista_previa", f"{D['8_vista_previa']}/{m}")
    t = open(f"{BASE}/manual/lecciones/{m}.md").read()
    for les in re.split(r"(?m)^(?=# M\d+ U\d\d)", t):
        code = les.split("|")[0][2:].strip()
        for d in re.findall(r"\*\*Dato por confirmar:\*\*\s*(.+?)(?:\. Consultado|$)", les, re.M): pend.append(f"{code}: {d}.")
shutil.copy(f"{M}/Apoyo/Apoyo_libro_Moodle.zip", D["1_libros"])
head = re.sub(r"<NAME>[^<]*</NAME>", "<NAME>Palabras clave del curso</NAME>", x.split("<ENTRIES>")[0], 1)
open(f"{D['3_glosario']}/Glosario_curso_Moodle.xml", "w", encoding="utf-8").write(head + "<ENTRIES>\n" + "\n".join(entries) + "\n</ENTRIES></INFO></GLOSSARY>\n")
shutil.copy(f"{M}/banco_preguntas_ttmf.gift.txt", D["4_preguntas"])
for p in glob.glob(f"{M}/insignias/*.png"): shutil.copy(p, D["5_insignias"])
for p in glob.glob(f"{M}/certificado/*.png"): shutil.copy(p, D["6_certificado"])
I = f"{M}/instalacion"
for f in ["guia_gamificacion_ttmf.md", "comunidad_y_canales.md"]: shutil.copy(f"{I}/{f}", D["7_guias"])
shutil.copy(f"{BASE}/manual/TTMF_manual_v2.md", D["7_guias"]); shutil.copy(f"{BASE}/manual/TTMF_manual_v2.docx", D["7_guias"])
man = open(f"{BASE}/manual/TTMF_manual_v2.md").read()
open(f"{D['7_guias']}/datos_verificados.md", "w").write(man[man.index("# 6. Datos verificados"):])
legs = [f"{M}/{m}/{m}_legible.md" for m in mods]
open(f"/tmp/ttmf_legible.md", "w").write("\n\n---\n\n".join(open(p).read() for p in legs))
shutil.copy("/tmp/ttmf_legible.md", f"{D['7_guias']}/TTMF_lecciones_completas.md")
S = "/tmp/claude-0/-home-user-peekabook/2b8c84d1-874b-559e-a5dd-06af4ddd1637/scratchpad"
md2 = os.path.join(os.path.dirname(BASE), "proyecto-inclusion-financiera", "herramientas", "md2docx.js")
env = dict(os.environ, NODE_PATH=f"{S}/nodeenv/node_modules")
subprocess.run(["node", md2, f"{D['7_guias']}/TTMF_lecciones_completas.docx", "Tu Talento, Tu Marca, Tu Futuro", "Las 77 lecciones · Versión 1.3 · Septiembre de 2026", "/tmp/ttmf_legible.md"], env=env, check=True, capture_output=True)
subprocess.run(["node", md2, f"{D['7_guias']}/guia_gamificacion_ttmf.docx", "Tu Talento, Tu Marca, Tu Futuro", "Actividades, puntos, insignias y constancia · Septiembre de 2026", f"{I}/guia_gamificacion_ttmf.md"], env=env, check=True, capture_output=True)
for f in ["README_INSTALAR_TU_TALENTO_PARA_CLAUDE.md", "LEEME.txt"]: shutil.copy(f"{I}/{f}", out)
parts = [("parte1_curso", lambda r: "2_h5p" not in r),
         ("parte2_H5P_M1-M6", lambda r: re.search(r"2_h5p/M[1-6]/", r)),
         ("parte3_H5P_M7-M11", lambda r: re.search(r"2_h5p/M([7-9]|1[01])/", r))]
for pn, keep in parts:
    z = os.path.join(os.path.dirname(BASE), "entregas", f"{name}_{pn}_2026-09-29.zip")
    with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
        if pn != "parte1_curso": zf.write(f"{out}/LEEME.txt", f"{name}/LEEME.txt")
        for r, _, fs in os.walk(out):
            rel = os.path.relpath(r, out) + "/"
            if pn == "parte1_curso" and "2_h5p" in rel: continue
            if pn != "parte1_curso" and not keep(rel): continue
            for f in sorted(fs):
                if pn != "parte1_curso" and f == "LEEME.txt": continue
                p = os.path.join(r, f); zf.write(p, os.path.join(name, os.path.relpath(p, out)))
    print(z, round(os.path.getsize(z) / 1048576, 1), "MB")
print(len(entries), "términos ·", len(glob.glob(f"{out}/2_h5p/*/*.h5p")), "H5P ·", len(pend), "datos por confirmar en lecciones")
