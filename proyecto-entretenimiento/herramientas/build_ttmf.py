# Tu Talento, Tu Marca, Tu Futuro: genera libro (zip), glosario, texto legible, vista previa y conteo por módulo.
# Reutiliza el generador v3 del curso Tu Dinero. Uso: python3 proyecto-entretenimiento/herramientas/build_ttmf.py M1 [M2 ...] | todos
import os, sys, json, zipfile
AQUI = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(AQUI)
sys.path.insert(0, os.path.join(os.path.dirname(BASE), "proyecto-inclusion-financiera", "herramientas"))
import build_v3 as B
from leccion_ux2 import build, page
TITULOS = {
 "M1": "Módulo 1. Tu dinero real: ingresos variables",
 "M2": "Módulo 2. Tu carrera como negocio: régimen fiscal e impuestos",
 "M3": "Módulo 3. Contratos, representación y regalías",
 "M4": "Módulo 4. Conoce el sistema financiero mexicano",
 "M5": "Módulo 5. Compara y elige: instituciones y productos",
 "M6": "Módulo 6. El crédito es deuda",
 "M7": "Módulo 7. Buró y Círculo de Crédito",
 "M8": "Módulo 8. Sal de deudas",
 "M9": "Módulo 9. No caigas: fraudes y robo de identidad",
 "M10": "Módulo 10. Protección y prevención",
 "M11": "Módulo 11. Tu futuro",
}
B.TITULOS.clear(); B.TITULOS.update(TITULOS)
SRC, OUT = os.path.join(BASE, "manual", "lecciones"), os.path.join(BASE, "moodle")
if __name__ == "__main__":
    mods = list(TITULOS) if "todos" in sys.argv else [a for a in sys.argv[1:] if not a.startswith("-")]
    for mod in mods:
        text = open(os.path.join(SRC, f"{mod}.md"), encoding="utf-8").read()
        pages = build(text)
        d = os.path.join(OUT, mod); os.makedirs(d, exist_ok=True)
        with zipfile.ZipFile(os.path.join(d, f"{mod}_libro_Moodle.zip"), "w", zipfile.ZIP_DEFLATED) as z:
            for fn, t, b in pages: z.writestr(fn, page(t, b))
        xml, n = B.glosario(text, f"Palabras clave · {mod}")
        open(os.path.join(d, f"{mod}_glosario_Moodle.xml"), "w").write(xml)
        open(os.path.join(d, f"{mod}_legible.md"), "w").write(B.legible(text, mod))
        B.preview(pages, os.path.join(d, "vista_previa"))
        c = B.conteo(text)
        json.dump({"lecciones": len(c), "paginas": len(pages), "terminos": n, "conteo": c}, open(os.path.join(d, "conteo.json"), "w"), ensure_ascii=False)
        print(mod, "lecciones", len(c), "páginas", len(pages), "términos", n, "· palabras (esencial/profundiza):", " ".join(f"{e}/{p}" for _, e, p in c))
