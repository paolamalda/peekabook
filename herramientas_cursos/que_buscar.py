# Agrega «Qué buscar» / «What to look for» a los recursos de las lecciones que no lo tienen.
# Uso: python3 herramientas_cursos/que_buscar.py   (todos los cursos)
import glob, json, re

ES = {
    "SIPRES": "escribe el nombre de la institución y revisa que aparezca como autorizada y para qué productos.",
    "Pensión para el Bienestar de las Personas Adultas Mayores": "los requisitos, el monto vigente y dónde registrarte según tu edad.",
    "IMSS-Bienestar": "tu unidad médica más cercana y qué servicios dan sin costo.",
    "Reporte de crédito especial:": "cómo pedir tu reporte sin costo una vez al año y cómo levantar una aclaración.",
    "Reporte de crédito especial": "cómo pedir tu reporte sin costo una vez al año y cómo levantar una aclaración.",
    "Reclamaciones": "cómo presentar una queja contra un banco o financiera y qué papeles tener a la mano.",
    "Procuraduría de Protección de Niñas, Niños y Adolescentes": "la procuraduría de tu estado y cómo pedir orientación.",
    "Quién es Quién en el Envío de Dinero": "compara cuánto recibe tu familia con cada empresa, no solo la comisión.",
    "Protección Civil": "las alertas de tu zona y cómo armar tu plan familiar de emergencia.",
    "Acta en línea": "cómo obtener tu acta certificada con tu CURP y cuánto cuesta en tu estado.",
    "CURP": "«Consulta tu CURP»: la consulta y la impresión no tienen costo.",
    "Quejas por discriminación": "cómo presentar una queja y qué datos del hecho anotar.",
    "Registro Agrario Nacional": "cómo consultar a nombre de quién está la parcela y los trámites del ejido.",
    "Defensoría pública": "la oficina más cercana y en qué casos te asesoran sin costo.",
    "Lista de sucesión": "cómo registrar o cambiar tu lista de sucesión de la parcela.",
    "Quejas contra despachos de cobranza": "si el despacho está registrado y cómo quejarte si te amenazan o cobran a terceros.",
    "Líneas con tu CURP": "qué líneas están a tu nombre y cómo desvincular las que no reconoces.",
    "Aseguradoras autorizadas": "si la aseguradora está autorizada antes de contratar.",
    "Obligaciones fiscales": "tu régimen y qué declaraciones te tocan; todo trámite en el portal es sin costo.",
    "Estadísticas y precios": "la inflación del último año para comparar si tu ingreso alcanza lo mismo.",
    "Capacitación para negocios": "los cursos para negocios sin costo y sus fechas.",
    "Línea Nacional sobre la Violencia Doméstica": "cómo hablar o chatear en español, a cualquier hora y de forma confidencial.",
    "Índice de precios al consumidor": "cuánto subieron los precios en el último año.",
    "Índice de precios": "cuánto subieron los precios en el último año.",
    "Reporte de crédito sin costo": "el sitio oficial para pedir tus reportes sin costo de las tres agencias.",
    "Reportes de crédito sin costo": "el sitio oficial para pedir tus reportes sin costo de las tres agencias.",
    "Mercado de seguros": "las fechas de inscripción y si calificas para ayuda con la cuota mensual.",
    "Reporta un fraude": "cómo reportar en español y qué hacer después según el tipo de fraude.",
    "Robo de identidad": "el plan de pasos según lo que robaron y las cartas modelo.",
    "Registro No Llame": "cómo inscribir tu número y reportar llamadas que siguen.",
    "Asistencia por desastre": "si tu zona tiene una declaración de desastre y cómo pedir ayuda.",
    "CDFI certificadas": "la lista de instituciones financieras comunitarias certificadas de tu estado.",
    "Impuestos de pequeños negocios": "qué formularios te tocan como dueño y las fechas de pago.",
    "Capacitación": "los centros de apoyo para negocios cerca de ti (SBDC, SCORE) y sus talleres sin costo.",
    "Quién es quién en los precios": "compara precios de productos básicos en tu ciudad.",
    "Saldo y trámites de vivienda": "tu saldo, tus puntos y si ya puedes precalificar para un crédito.",
    "Vivienda para trabajadores del Estado": "tu saldo y los tipos de crédito para trabajadores del Estado.",
    "Notarías y escrituras": "el colegio de notarios de tu estado y los programas de escrituración a bajo costo.",
    "Política monetaria e inflación": "la inflación anual más reciente y la tasa de interés de referencia.",
    "Tasa de referencia e inflación": "la inflación anual más reciente y la tasa de interés de referencia.",
    "PROFEDET": "cómo pedir asesoría laboral sin costo por teléfono o en línea.",
    "Semanas cotizadas": "tu constancia de semanas cotizadas, que se descarga sin costo.",
    "Avisos oficiales": "los avisos sobre fraudes que usan el nombre del SAT.",
    "Ofertas H-2A": "las ofertas de trabajo vigentes con salario, horas y vivienda.",
    "Servicio Nacional de Empleo": "las vacantes de tu estado y los programas de trabajo temporal en el extranjero.",
    "Agencias de colocación registradas": "si la agencia que te ofrece trabajo está registrada.",
    "Protecciones H-2A": "tus derechos de pago, vivienda, transporte y cómo reportar abusos.",
    "Derechos de pago H-2A": "la garantía de 3/4 de las horas y cómo se calcula tu pago por pieza.",
    "División de Horas y Salarios": "cómo poner una queja en español; no te preguntan tu situación migratoria.",
    "Cuentas en EE. UU.": "cómo elegir una cuenta y qué comisiones revisar antes de abrirla.",
    "Cuentas en Canadá": "las cuentas básicas de bajo costo y qué documentos piden.",
    "Trabajadores agrícolas extranjeros": "qué impuestos te retienen con la visa H-2A y cómo declarar.",
    "IRS en español:": "las guías en español y cómo pedir una copia de tus declaraciones.",
    "Consulados de México en Canadá": "el consulado de tu provincia y su teléfono de protección.",
    "Consulados de México": "el consulado más cercano y su teléfono de protección.",
    "Contrato PTAT 2026": "tu contrato de la temporada: salario, horas, descuentos y vivienda.",
    "AforeMóvil": "cómo descargar la app, ver tu Afore y hacer aportaciones voluntarias.",
    "Cetesdirecto": "cómo abrir tu cuenta desde 100 pesos sin intermediarios.",
}
EN = {
    "National Domestic Violence Hotline": "how to call or chat in English or Spanish, any time and confidentially.",
    "Consumer Price Index": "how much prices went up in the last year.",
    "Report fraud": "how to report and what to do next for each type of scam.",
    "No-cost credit report": "the official site to get your no-cost reports from the three agencies.",
    "No-cost credit reports": "the official site to get your no-cost reports from the three agencies.",
    "Health insurance marketplace": "enrollment dates and whether you qualify for help with the monthly cost.",
    "Identity theft": "the step-by-step plan for what was stolen, and sample letters.",
    "Do Not Call Registry": "how to add your number and report calls that keep coming.",
    "Disaster assistance": "whether your area has a disaster declaration and how to apply.",
    "Certified CDFIs": "the list of certified community lenders in your state.",
    "Small business taxes": "which forms you file as an owner and the payment dates.",
    "Training": "business help centers near you (SBDC, SCORE) and their no-cost workshops.",
}

def label(line, en):
    m = re.match(r"-\s*\*\*([^*]+)\*\*", line.strip())
    if not m: return None
    return (EN if en else ES).get(m.group(1).strip())

n = falt = 0
for c in sorted(glob.glob("cursos/*/curso.json")):
    d = c.rsplit("/", 1)[0]; en = json.load(open(c)).get("lang") == "en"
    for f in sorted(glob.glob(d + "/lecciones/M*.md")):
        L = open(f).read().split("\n"); cambio = False
        for i, l in enumerate(L):
            s = l.strip()
            if not (s.startswith("-") and "http" in s): continue
            if en and "| What to search:" in s:
                L[i] = l.replace("| What to search:", "| What to look for:"); cambio = True; n += 1; continue
            if "Qué buscar" in s or "What to look" in s: continue
            t = label(s, en)
            if not t: falt += 1; print("SIN TEXTO", f, s[:100]); continue
            L[i] = l.rstrip().rstrip(".") + (" | What to look for: " if en else " | Qué buscar: ") + t
            cambio = True; n += 1
        if cambio: open(f, "w").write("\n".join(L))
print(n, "recursos completados ·", falt, "sin texto")
