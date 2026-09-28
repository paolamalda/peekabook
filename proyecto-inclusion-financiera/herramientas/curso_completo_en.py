# Paquete del curso completo en inglés 3.2, en 3 zips (curso, H5P M1-M2, H5P M3-M5).
# Uso: python3 herramientas/curso_completo_en.py <carpeta TDTF_05 descomprimida> <num>
import re, os, shutil, zipfile, sys, subprocess, glob
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V1, num = sys.argv[1], sys.argv[2]
name = f"TDTF_{num}_Full_course_EN_v3.2"
out = os.path.join("/tmp", name); shutil.rmtree(out, ignore_errors=True)
D = {k: os.path.join(out, k) for k in ["1_books", "2_h5p", "3_glossary", "4_questions", "5_badges", "6_certificate", "7_guides"]}
for d in D.values(): os.makedirs(d)
V3 = os.path.join(BASE, "moodle/v3/en")
entries, seen = [], set()
for m in ["M1", "M2", "M3", "M4", "M5"]:
    shutil.copy(f"{V3}/{m}/{m}_libro_Moodle.zip", f"{D['1_books']}/{m}_book_Moodle.zip")
    shutil.copy(f"{V1}/libros/en/{m}_resumen.html", f"{D['1_books']}/{m}_summary.html")
    x = open(f"{V3}/{m}/{m}_glosario_Moodle.xml", encoding="utf-8").read()
    for e in re.findall(r"<ENTRY>.*?</ENTRY>", x, re.S):
        c = re.search(r"<CONCEPT>(.*?)</CONCEPT>", e, re.S).group(1).strip().lower()
        if c not in seen: seen.add(c); entries.append(e)
    os.makedirs(f"{D['2_h5p']}/{m}")
    for h in sorted(glob.glob(f"{V3}/h5p/{m}_U*.h5p")): shutil.copy(h, f"{D['2_h5p']}/{m}")
shutil.copy(f"{V3}/Apoyo/Apoyo_libro_Moodle.zip", f"{D['1_books']}/Support_book_Moodle.zip")
head = re.sub(r"<NAME>[^<]*</NAME>", "<NAME>Course key words</NAME>", x.split("<ENTRIES>")[0], 1)
open(f"{D['3_glossary']}/Course_glossary_Moodle.xml", "w", encoding="utf-8").write(head + "<ENTRIES>\n" + "\n".join(entries) + "\n</ENTRIES></INFO></GLOSSARY>\n")
shutil.copy(f"{V3}/banco_preguntas_v3_en.gift.txt", f"{D['4_questions']}/question_bank_v3_en.gift.txt")
for p in glob.glob(f"{V3}/insignias/*.png"): shutil.copy(p, D["5_badges"])
shutil.copy(f"{V3}/certificado/certificado_fondo.png", f"{D['6_certificate']}/certificate_background.png")
shutil.copy(f"{V3}/certificado/certificado_muestra.png", f"{D['6_certificate']}/certificate_sample.png")
shutil.copy(f"{V3}/gamification_guide_v3.md", D["7_guides"])
S = "/tmp/claude-0/-home-user-peekabook/2b8c84d1-874b-559e-a5dd-06af4ddd1637/scratchpad"
subprocess.run(["node", "herramientas/md2docx.js", f"{D['7_guides']}/gamification_guide_v3.docx", "Your Money, Your Family, Your Future",
                "Activities, points, badges and certificate · Version 3 · September 2026", f"{V3}/gamification_guide_v3.md"],
               cwd=BASE, env=dict(os.environ, NODE_PATH=f"{S}/nodeenv/node_modules"), check=True, capture_output=True)
for f in glob.glob(os.path.join(BASE, "moodle/instalacion_en/*")): shutil.copy(f, out)
parts = [("parte1_curso", lambda r: "2_h5p" not in r), ("parte2_H5P_M1-M2", lambda r: re.search(r"2_h5p/M[12]", r)),
         ("parte3_H5P_M3-M5", lambda r: re.search(r"2_h5p/M[345]", r))]
for pn, keep in parts:
    z = os.path.join(os.path.dirname(BASE), "entregas", f"{name}_{pn}_2026-09-28.zip")
    with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
        for r, _, fs in os.walk(out):
            rel = os.path.relpath(r, out)
            if not keep(rel + "/"): continue
            for f in sorted(fs):
                p = os.path.join(r, f); zf.write(p, os.path.join(name, os.path.relpath(p, out)))
            if pn != "parte1_curso": zf.write(os.path.join(out, "LEEME.txt"), os.path.join(name, "LEEME.txt")) if rel.endswith(("M1", "M3")) else None
    print(z, round(os.path.getsize(z) / 1048576, 1), "MB")
print(len(entries), "términos ·", len(glob.glob(f"{out}/2_h5p/*/*.h5p")), "H5P")
