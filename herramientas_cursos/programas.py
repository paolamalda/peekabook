# Programas de gobierno del módulo extra «Programas y apoyos» (programas/programas.json).
# Cada programa se muestra solo si sigue vigente: fecha de revisión + vigencia_meses >= hoy.
import datetime, json, os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]


def fecha(iso, en):
    d = datetime.date.fromisoformat(iso)
    return d.strftime("%B %-d, %Y") if en else f"{d.day} de {MESES[d.month - 1]} de {d.year}"


def vence(p):
    d = datetime.date.fromisoformat(p["revisado"]); m = d.month - 1 + p.get("vigencia_meses", 6)
    return datetime.date(d.year + m // 12, m % 12 + 1, min(d.day, 28))


def vigentes(curso, en, hoy=None):
    """(vigentes, vencidos) para un curso y un idioma."""
    hoy = hoy or datetime.date.today()
    cat = json.load(open(os.path.join(RAIZ, "programas", "programas.json"), encoding="utf-8"))["programas"]
    L = "en" if en else "es"
    mios = [p for p in cat if curso in p["cursos"] and p["texto"].get(L)]
    return [p for p in mios if vence(p) >= hoy], [p for p in mios if vence(p) < hoy]


def bloque_readme(curso, en):
    """Sección del README para el módulo extra; vacío si no hay programas vigentes."""
    ok, _ = vigentes(curso, en)
    if not ok: return ""
    k = len(ok) + 1
    if en:
        return f"""## Extra section: Programs and support

This section is **separate**: nothing in the course depends on it.

1. Add a section **at the end** of the course called `Programs and support` (description: "Government programs and public services that may help you. Reviewed information; confirm it on the official site."). Pick a "help" icon for its tile.
2. Create the book `Programs and support` with the same settings and import `1_books/Programas_libro_Moodle.zip` ({k} chapters).
3. **Completion: none.** Don't add it to course completion or to any other activity's restrictions, and don't give it points.
4. **To remove it:** hide the section (eye icon > Hide) or delete it. The rest of the course stays the same.
5. If you get a new package for this book, replace only this book.

"""
    return f"""## Sección extra: Programas y apoyos

Esta sección va **aparte**: nada del curso depende de ella.

1. Agrega una sección **al final** del curso llamada `Programas y apoyos` (descripción: "Programas de gobierno y servicios públicos que pueden servirte. Información revisada; confírmala en el sitio oficial."). Elige un ícono de «ayuda» para su mosaico.
2. Crea el libro `Programas y apoyos` con la misma configuración e importa `1_libros/Programas_libro_Moodle.zip` ({k} capítulos).
3. **Finalización: ninguna.** No lo incluyas en la finalización del curso ni en las restricciones de otras actividades, y no le des puntos.
4. **Para quitarla:** oculta la sección (ojo > Ocultar) o bórrala. El resto del curso sigue igual.
5. Si llega un paquete nuevo de este libro, reemplaza solo este libro.

"""


def fechas(curso, en, hoy=None):
    """Fechas del calendario que siguen vigentes (hasta >= hoy) para un curso, en orden."""
    hoy = hoy or datetime.date.today()
    F = json.load(open(os.path.join(RAIZ, "programas", "fechas.json"), encoding="utf-8"))["fechas"]
    L = "en" if en else "es"
    return sorted([f for f in F if curso in f["cursos"] and f.get(L) and datetime.date.fromisoformat(f["hasta"]) >= hoy], key=lambda f: f["desde"])


def rango(f, en):
    a, b = f["desde"], f["hasta"]
    if a == b: return fecha(a, en)
    return (f"{fecha(a, True)} to {fecha(b, True)}" if en else f"Del {fecha(a, False)} al {fecha(b, False)}")
