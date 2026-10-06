# Lista de verificación de datos vigentes: recuadros «Dato vigente» / «Current fact» de las lecciones,
# programas y fechas del módulo extra. Marca lo que pasó de 6 meses sin revisarse.
# Uso: python3 herramientas_cursos/verificacion.py   → entregables/verificacion_datos.md y .csv
import csv, datetime, glob, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import programas as PG

RAIZ = PG.RAIZ
ENT = os.path.join(RAIZ, "proyecto-inclusion-financiera", "entregables")
MES = {m: i for i, m in enumerate(PG.MESES, 1)}
MES_EN = {m: i for i, m in enumerate(["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"], 1)}
MESES_VIGENCIA = 6


def suma_meses(d, n):
    m = d.month - 1 + n
    return datetime.date(d.year + m // 12, m % 12 + 1, min(d.day, 28))


def fecha_de(t):
    m = re.search(r"(?i)consultad[oa]s? el (\d+) de ([a-z]+) de (\d{4})", t) or re.search(r"(?i)\bal (\d+) de ([a-z]+) de (\d{4})", t)
    if m and m.group(2).lower() in MES: return datetime.date(int(m.group(3)), MES[m.group(2).lower()], int(m.group(1)))
    m = re.search(r"(?i)(?:accessed|checked)(?: on)? ([A-Za-z]+) (\d+), (\d{4})", t)
    if m and m.group(1).lower() in MES_EN: return datetime.date(int(m.group(3)), MES_EN[m.group(1).lower()], int(m.group(2)))
    return None


def datos_lecciones(D):
    """[(leccion, texto, fecha, fuente)] de los recuadros de dato vigente de un curso."""
    out = []
    for f in sorted(glob.glob(os.path.join(D, "lecciones", "M*.md")), key=lambda p: int(re.search(r"M(\d+)", os.path.basename(p)).group(1))):
        cod = ""; L = open(f, encoding="utf-8").read().split("\n")
        for i, l in enumerate(L):
            m = re.match(r"# (M\d+ U\d+) \|", l)
            if m: cod = m.group(1); continue
            if re.match(r"> \*\*(Dato vigente|Current fact):\*\*", l):
                j = i + 1  # el recuadro sigue en las líneas «>» siguientes
                while j < len(L) and L[j].startswith(">") and not re.match(r"> \*\*", L[j]):
                    l += " " + L[j].lstrip(">").strip(); j += 1
                t = re.sub(r"\{\{([^|}]+)\|[^}]*\}\}", r"\1", l[2:].strip()).replace("**", "")
                fu = re.search(r"(?:a través de|through) (.+?)\.?$", t)
                out.append((cod, t, fecha_de(t), fu.group(1) if fu else ""))
    return out


def vencidos(D, hoy=None):
    hoy = hoy or datetime.date.today()
    return [x for x in datos_lecciones(D) if not x[2] or suma_meses(x[2], MESES_VIGENCIA) < hoy]


def main():
    hoy = datetime.date.today()
    filas = []
    for D in sorted(glob.glob(os.path.join(RAIZ, "cursos", "*"))):
        c = os.path.basename(D)
        for cod, t, f, fu in datos_lecciones(D):
            lim = suma_meses(f, MESES_VIGENCIA) if f else None
            filas.append(dict(tipo="lección", curso=c, donde=cod, dato=t, consultado=f.isoformat() if f else "sin fecha",
                              revisar_antes=lim.isoformat() if lim else "ya", fuente=fu, estado="vigente" if lim and lim >= hoy else "por revisar", confirmado=""))
    cat = json.load(open(os.path.join(RAIZ, "programas", "programas.json"), encoding="utf-8"))["programas"]
    for p in cat:
        lim = PG.vence(p)
        filas.append(dict(tipo="programa", curso=", ".join(p["cursos"]), donde=p["id"], dato=p["titulo"]["es"] or p["titulo"]["en"], consultado=p["revisado"],
                          revisar_antes=lim.isoformat(), fuente=re.sub(r"\s*\|.*", "", p["recurso"].get("es") or p["recurso"].get("en", "")).lstrip("- "),
                          estado="vigente" if lim >= hoy else "vencido (ya no se muestra)", confirmado=""))
    F = json.load(open(os.path.join(RAIZ, "programas", "fechas.json"), encoding="utf-8"))["fechas"]
    for x in F:
        filas.append(dict(tipo="fecha", curso=", ".join(x["cursos"]), donde=f'{x["desde"]} a {x["hasta"]}', dato=re.sub(r"\*\*", "", x.get("es") or x.get("en")),
                          consultado="2026-10-06", revisar_antes=x["desde"], fuente="", estado="vigente" if datetime.date.fromisoformat(x["hasta"]) >= hoy else "pasada (ya no se muestra)", confirmado=""))
    with open(os.path.join(ENT, "verificacion_datos.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(filas[0])); w.writeheader(); w.writerows(filas)
    n = lambda tipo, est=None: sum(1 for x in filas if x["tipo"] == tipo and (est is None or x["estado"].startswith(est)))
    L = ["# Lista de verificación de datos vigentes", "",
         f"Generada el {PG.fecha(hoy.isoformat(), False)}. Cada dato se revisa en su fuente oficial y se marca la casilla. Un dato de lección pasa a «por revisar» {MESES_VIGENCIA} meses después de su fecha de consulta; un programa del módulo extra se oculta solo al vencer.", "",
         "| Tipo | Total | Vigentes | Por revisar o vencidos |", "|---|---|---|---|",
         f"| Datos en lecciones | {n('lección')} | {n('lección', 'vigente')} | {n('lección') - n('lección', 'vigente')} |",
         f"| Programas (módulo extra) | {n('programa')} | {n('programa', 'vigente')} | {n('programa') - n('programa', 'vigente')} |",
         f"| Fechas (módulo extra) | {n('fecha')} | {n('fecha', 'vigente')} | {n('fecha') - n('fecha', 'vigente')} |", "",
         "## Cómo usar esta lista", "",
         "1. Abre la fuente oficial de cada dato y confirma montos, fechas, teléfonos y requisitos.",
         "2. Si cambió, corrige la lección (o `programas/programas.json`) y pon la fecha de hoy en «Consultado el…» o en `revisado`.",
         "3. Marca la casilla. El detalle completo, para filtrar y repartir, está en `verificacion_datos.csv`.", ""]
    for tipo, tit in (("programa", "Programas del módulo extra"), ("fecha", "Fechas del módulo extra"), ("lección", "Datos en lecciones")):
        L += [f"## {tit}", "", "| ✓ | Curso | Dónde | Dato | Consultado | Revisar antes de | Estado |", "|---|---|---|---|---|---|---|"]
        L += [f"| [ ] | {x['curso']} | {x['donde']} | {x['dato'][:160].replace('|', '/')}{'…' if len(x['dato']) > 160 else ''} | {x['consultado']} | {x['revisar_antes']} | {x['estado']} |"
              for x in filas if x["tipo"] == tipo]
        L += [""]
    open(os.path.join(ENT, "verificacion_datos.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    print(f"{len(filas)} datos · lecciones {n('lección')} · programas {n('programa')} · fechas {n('fecha')}")


if __name__ == "__main__":
    main()
