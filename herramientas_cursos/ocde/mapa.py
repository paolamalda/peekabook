# Mapa de competencias: cruza cada tema de los marcos OCDE con las lecciones de un curso.
# Uso: python3 herramientas_cursos/ocde/mapa.py <carpeta_lecciones> <marco: adultos|negocios|jovenes> [inversion] [--salida archivo.md]
import re, os, sys, glob, importlib, json
sys.path.insert(0, os.path.dirname(__file__))

# Palabras que indican que una lección trabaja un tema (en español e inglés). Se busca en título, objetivo y «Lo esencial».
CLAVES = {
 "A1": r"inflaci|poder de compra|remesa|tipo de cambio|transferencia|SPEI|billete|efectivo|inflation|remittance|exchange rate|wire",
 "A2": r"ingreso|salario|sueldo|recibo de (pago|nómina)|bruto|neto|apoyo|beca|pensión del bienestar|income|paycheck|wage|salary",
 "A3": r"precio|compra|oferta|publicidad|suscrip|costo de oportunidad|comparar precios|price|purchase|subscription|advertis",
 "A4": r"contrato|letra chica|document|carpeta|comprobante|recibo|contract|fine print|record",
 "B1": r"presupuesto|budget",
 "B2": r"gasto fijo|gastos? variable|imprevist|gasto irregular|necesidad|deseo|separa|fixed|irregular expense|needs and wants",
 "B3": r"ahorr|fondo de emergencia|colchón|saving|emergency fund",
 "B4": r"invers|invertir|Cetes|fondo de inversi|bolsa|diversific|invest|index fund|stock",
 "B5": r"largo plazo|meta|patrimonio|testamento|plan de una página|long-term|goal|will\b|estate",
 "B6": r"retiro|AFORE|pensión|jubila|Modalidad 40|retirement|401\(k\)|IRA|Social Security",
 "B7": r"crédito|préstamo|tarjeta de crédito|tasa|CAT|meses sin intereses|aval|credit|loan|APR|interest rate",
 "B8": r"deuda|atraso|cobranza|reestructur|quita|debt|collection|past due",
 "C1": r"riesgo|imprevist|desastre|sismo|inundaci|enfermedad|risk|disaster|flood|earthquake",
 "C2": r"seguro|IMSS|colchón|fondo de emergencia|insurance|coverage|safety net",
 "C3": r"rendimiento|riesgo y|demasiado bueno|diversific|return|too good to be true",
 "D1": r"CONDUSEF|CNBV|IPAB|regulad|autorizad|reclam|queja|CFPB|FDIC|NCUA|regulat|complain",
 "D2": r"derecho|obligaci|letra chica|aval|rights|responsibilit",
 "D3": r"asesor|informaci[oó]n confiable|fuente|calculadora|simulador|advice|advisor|calculator|reliable source",
 "D4": r"cuenta|banco|producto financiero|comisi|institución|account|bank|credit union|fee",
 "D5": r"fraude|estafa|phishing|extorsi|robo de identidad|scam|fraud|identity theft",
 "D6": r"impuesto|SAT|ISR|IVA|RFC|declaraci|tax|IRS",
 "D7": r"economía|recesión|reforma|tasa de interés sube|cambio de ley|external|recession|economy|policy change",
 # negocios
 "N-A1": r"cuenta del negocio|terminal|cobrar con tarjeta|pagos digitales|CoDi|link de pago|business account|payment processor|card reader",
 "N-A2": r"financiar|capital|préstamo para el negocio|inversionista|apoyo|financiamiento|garantía|crowdfunding|financ|investor|SBA|CDFI|microloan",
 "N-B1": r"RESICO|RFC|registr|licencia|permiso|marca|figura legal|impuesto|LLC|EIN|license|permit|trademark|sole proprietor",
 "N-B2": r"registro|contabil|ganancia|costo fijo|costo variable|estado de resultados|record|bookkeep|profit|fixed cost",
 "N-B3": r"flujo|separa|sueldo fijo|inventario|punto de equilibrio|cobrar|cash flow|separate|owner.?s pay|break-even|inventory",
 "N-B4": r"crecer|plan de negocio|largo plazo|contratar|precio|grow|business plan|hire|pricing",
 "N-C1": r"seguro de gastos|IMSS|Modalidad 10|retiro|seguro de vida|health insurance|retirement|life insurance",
 "N-C2": r"seguro del negocio|riesgo|contingencia|desastre|temporada baja|business insurance|risk|disaster|slow season",
 "N-D1": r"competencia|inflaci|economía|comunidad|competit|inflation|economy",
 "N-D2": r"fraude|estafa|ciberseguridad|prestamista|informal|scam|fraud|cyber|predatory",
 "N-D3": r"asesor|contador|mentor|capacita|incubadora|advisor|accountant|mentor|SCORE|SBDC",
 # inversión
 "I1": r"ahorrar e invertir|especula|interés compuesto|diversific|riesgo y rendimiento|compound|diversif",
 "I2": r"comisi|rendimiento real|clase de activo|fondo|Cetes|bono|acci[oó]n|fee|real return|bond|stock|fund",
 "I3": r"intermediario|casa de bolsa|plataforma|asesor|broker|platform|advisor",
 "I4": r"estado de cuenta de inversi|rebalance|dar seguimiento|statement|rebalanc",
 "I5": r"derecho|reclam|autorizad|CNBV|regulad|rights|complain|SEC|FINRA",
 "I6": r"emoci|sesgo|pánico|impuls|manada|bias|emotion|panic",
 "I7": r"pirámide|fraude|demasiado bueno|rendimiento garantizado|Ponzi|scam|guaranteed return",
}
# los temas de jóvenes usan las mismas claves que su equivalente de adultos
JOV = {"J-A1": "A1", "J-A2": "A2", "J-A3": "A3", "J-A4": "A3", "J-A5": "A4", "J-A6": "A1", "J-B1": "B1", "J-B2": "B2", "J-B3": "B3",
       "J-B4": "B5", "J-B5": "B7", "J-C1": "C3", "J-C2": "C1", "J-C3": "C2", "J-C4": "C3", "J-D1": "D1", "J-D2": "D3", "J-D3": "D2",
       "J-D4": "D4", "J-D5": "D5", "J-D6": "D6"}


def lecciones(carpeta):
    out = []
    for f in sorted(glob.glob(os.path.join(carpeta, "*.md")), key=lambda p: [int(x) if x.isdigit() else x for x in re.split(r"(\d+)", os.path.basename(p))]):
        for les in re.split(r"(?m)^(?=# M\d+ U\d\d)", open(f, encoding="utf-8").read()):
            m = re.match(r"# (M\d+ U\d\d) \| (.+)", les)
            if not m: continue
            obj = re.search(r"(?m)^objetivo: (.*)$", les)
            ese = les.split("== profundiza")[0]
            out.append({"codigo": m.group(1), "titulo": m.group(2).strip(), "objetivo": obj.group(1) if obj else "",
                        "texto": m.group(2) + " " + (obj.group(1) if obj else "") + " " + ese})
    return out


def mapa(carpeta, marcos, extra=None):
    les = lecciones(carpeta)
    res = []
    for nombre in marcos:
        mod = importlib.import_module(nombre)
        for area, narea, tid, tema, comps in mod.TEMAS:
            clave = CLAVES.get(JOV.get(tid, tid), "")
            hits = []
            for l in les:
                n = len(re.findall(clave, l["texto"], re.I)) if clave else 0
                # fuerte: el tema está en título u objetivo; débil: solo menciones en Lo esencial
                fuerte = bool(clave and re.search(clave, l["titulo"] + " " + l["objetivo"], re.I))
                if fuerte or n >= 3: hits.append((l["codigo"], fuerte, n))
            hits.sort(key=lambda h: (-h[1], -h[2]))
            res.append({"marco": mod.MARCO, "area": narea, "id": tid, "tema": tema, "competencias": comps,
                        "lecciones": [h[0] for h in hits[:6]], "fuertes": sum(1 for h in hits if h[1])})
    if extra:
        for r in res: r.update(extra.get(r["id"], {}))
    return les, res


if __name__ == "__main__":
    carpeta = sys.argv[1]; marcos = [a for a in sys.argv[2:] if not a.startswith("--")]
    les, res = mapa(carpeta, marcos)
    print(len(les), "lecciones")
    for r in res:
        estado = "OK " if r["fuertes"] >= 1 else ("dé " if r["lecciones"] else "---")
        print(f"{estado} {r['id']:6} {r['tema'][:45]:45} {len(r['competencias']):3} comp · {', '.join(r['lecciones'])}")
