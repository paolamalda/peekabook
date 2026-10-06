# Reporte mensual: qué vence en los próximos N días (programas, fechas y datos de lecciones).
# Uso: python3 herramientas_cursos/vencimientos.py [días=30]
import datetime, glob, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import programas as PG, verificacion as VER

dias = int(sys.argv[1]) if len(sys.argv) > 1 else 30
hoy = datetime.date.today(); lim = hoy + datetime.timedelta(days=dias)
cat = json.load(open(os.path.join(PG.RAIZ, "programas", "programas.json"), encoding="utf-8"))["programas"]
pro = [(PG.vence(p), p["id"], p["titulo"]["es"] or p["titulo"]["en"]) for p in cat if PG.vence(p) <= lim]
F = json.load(open(os.path.join(PG.RAIZ, "programas", "fechas.json"), encoding="utf-8"))["fechas"]
fe = [(x["hasta"], (x.get("es") or x.get("en")).replace("**", "")[:90]) for x in F if hoy <= datetime.date.fromisoformat(x["hasta"]) <= lim]
lec = []
for D in sorted(glob.glob(os.path.join(PG.RAIZ, "cursos", "*"))):
    for cod, t, f, fu in VER.datos_lecciones(D):
        v = VER.suma_meses(f, VER.MESES_VIGENCIA) if f else hoy
        if v <= lim: lec.append((v, os.path.basename(D), cod, t[:90]))
print(f"# Vencimientos al {PG.fecha(lim.isoformat(), False)} (revisado el {PG.fecha(hoy.isoformat(), False)})\n")
print(f"## Programas del módulo extra que vencen o ya vencieron: {len(pro)}")
for v, i, t in sorted(pro): print(f"- {v} · {i} · {t}" + (" (YA NO SE MUESTRA)" if v < hoy else ""))
print(f"\n## Fechas del calendario que terminan pronto: {len(fe)}")
for h, t in sorted(fe): print(f"- {h} · {t}")
print(f"\n## Datos de lecciones por revisar: {len(lec)}")
for v, c, cod, t in sorted(lec)[:200]: print(f"- {v} · {c} {cod} · {t}")
