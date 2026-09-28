# Agrega la sección "Para saber más" / "Learn more" a cada lección y genera el catálogo.
import re, json, csv, os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# id: (nombre ES, nombre EN, organización, url, idioma del recurso)
R = {
 "MS": ("Money Smart para adultos", "Money Smart for Adults", "FDIC", "https://www.fdic.gov/consumer-resource-center/money-smart-adults", "ES/EN"),
 "EDU": ("Herramientas para educación financiera (incluye Your Money, Your Goals)", "Financial education tools (includes Your Money, Your Goals)", "CFPB", "https://www.consumerfinance.gov/consumer-tools/educator-tools/", "EN, algunas en ES"),
 "CFPBES": ("CFPB en español", "CFPB in Spanish", "CFPB", "https://www.consumerfinance.gov/es/", "ES"),
 "CFPBWB": ("Bienestar financiero: cuestionario y herramientas", "Financial well-being questionnaire and tools", "CFPB", "https://www.consumerfinance.gov/consumer-tools/financial-well-being/", "ES/EN"),
 "NEWC": ("Guías para recién llegados: cómo manejar el dinero", "Newcomer's guides to managing money", "CFPB", "https://www.consumerfinance.gov/about-us/blog/the-newcomers-guides-to-managing-money/", "ES/EN"),
 "CHECK": ("Lista para abrir una cuenta bancaria", "Checklist for opening a bank account", "CFPB", "https://files.consumerfinance.gov/f/documents/cfpb_checklist_opening_bank_account_web.pdf", "EN; versión ES en la misma serie"),
 "PAYBILLS": ("Formas de pagar tus cuentas", "Ways to pay your bills", "CFPB", "https://files.consumerfinance.gov/f/documents/cfpb_ways-to-pay-your-bills_2022-08.pdf", "EN; versión ES en la misma serie"),
 "REMIT": ("¿Qué es una remesa y cuáles son mis derechos?", "What is a remittance transfer and what are my rights?", "CFPB", "https://www.consumerfinance.gov/ask-cfpb/what-is-a-remittance-transfer-and-what-are-my-rights-en-1161/", "EN; ES en CFPB en español"),
 "CRED": ("Reportes y puntajes de crédito", "Credit reports and scores", "CFPB", "https://www.consumerfinance.gov/consumer-tools/credit-reports-and-scores/", "ES/EN"),
 "COLL": ("Cobranza de deudas: tus derechos", "Debt collection: your rights", "CFPB", "https://www.consumerfinance.gov/consumer-tools/debt-collection/", "ES/EN"),
 "AUTO": ("Préstamos para auto", "Auto loans", "CFPB", "https://www.consumerfinance.gov/consumer-tools/auto-loans/", "ES/EN"),
 "HOME": ("Comprar una casa", "Buying a house", "CFPB", "https://www.consumerfinance.gov/owning-a-home/", "ES/EN"),
 "HCOUNS": ("Buscador de consejeros de vivienda", "Find a housing counselor", "CFPB / HUD", "https://www.consumerfinance.gov/find-a-housing-counselor/", "EN"),
 "ACR": ("Reportes de crédito gratuitos", "Free credit reports", "AnnualCreditReport.com", "https://www.annualcreditreport.com", "EN"),
 "IDT": ("Robo de identidad: reportar y plan de recuperación", "Identity theft: report and recovery plan", "FTC", "https://www.identitytheft.gov", "ES/EN (robodeidentidad.gov)"),
 "RF": ("Reportar un fraude", "Report fraud", "FTC", "https://reportefraude.ftc.gov", "ES (EN: reportfraud.ftc.gov)"),
 "CONS": ("Consejos para consumidores en español", "FTC consumer advice", "FTC", "https://consumidor.ftc.gov", "ES (EN: consumer.ftc.gov)"),
 "FTCIMM": ("Estafas contra inmigrantes", "Scams against immigrants", "FTC", "https://consumer.ftc.gov/features/scams-against-immigrants", "EN/ES"),
 "FTCIMM2": ("Cómo evitar estafas de inmigración y obtener ayuda real", "How to avoid immigration scams and get real help", "FTC", "https://consumer.ftc.gov/articles/how-avoid-immigration-scams-and-get-real-help", "EN/ES"),
 "IRSES": ("IRS en español", "IRS in Spanish", "IRS", "https://www.irs.gov/es", "ES"),
 "ITIN": ("Cómo solicitar un ITIN", "How to apply for an ITIN", "IRS", "https://www.irs.gov/tin/itin/how-to-apply-for-an-itin", "EN/ES"),
 "CAA": ("Buscador de agentes certificadores (ITIN)", "ITIN acceptance agents locator", "IRS", "https://www.irs.gov/tin/itin/itin-acceptance-agents", "EN"),
 "VITA": ("Preparación gratuita de impuestos (VITA y TCE)", "Free tax return preparation (VITA and TCE)", "IRS", "https://www.irs.gov/individuals/free-tax-return-preparation-for-qualifying-taxpayers", "EN/ES"),
 "GIG": ("Centro de impuestos de la economía de plataformas", "Gig Economy Tax Center", "IRS", "https://www.irs.gov/businesses/gig-economy-tax-center", "EN/ES"),
 "SE": ("Centro para trabajadores por cuenta propia", "Self-Employed Individuals Tax Center", "IRS", "https://www.irs.gov/businesses/small-businesses-self-employed/self-employed-individuals-tax-center", "EN/ES"),
 "EIN": ("Solicitar un número de identificación del empleador (EIN)", "Get an Employer Identification Number (EIN)", "IRS", "https://www.irs.gov/businesses/small-businesses-self-employed/get-an-employer-identification-number", "EN/ES"),
 "CALEITC": ("CalEITC: crédito por ingreso del trabajo de California", "California Earned Income Tax Credit (CalEITC)", "FTB", "https://www.ftb.ca.gov/file/personal/credits/california-earned-income-tax-credit.html", "EN/ES"),
 "YCTC": ("Crédito tributario por hijos menores (YCTC)", "Young Child Tax Credit (YCTC)", "FTB", "https://www.ftb.ca.gov/file/personal/credits/young-child-tax-credit-es.html", "ES (EN disponible)"),
 "FTBFREE": ("Ayuda fiscal gratuita en California", "Free tax help in California", "FTB", "https://www.ftb.ca.gov/help/free-tax-help/index.html", "EN"),
 "CTEC": ("Verificar a un preparador registrado", "Verify a registered tax preparer", "CTEC", "https://www.ctec.org", "EN"),
 "DIR": ("Salarios y reclamos laborales (Comisionado Laboral)", "Wages and wage claims (Labor Commissioner)", "DIR de California", "https://www.dir.ca.gov/dlse/", "EN/ES"),
 "DFPI": ("Directorio de remesadoras con licencia en California", "Directory of licensed money transmitters in California", "DFPI", "https://dfpi.ca.gov/regulated-industries/money-transmitters/directory-of-money-transmitters/", "EN"),
 "NMLS": ("Verificar licencias de empresas financieras", "Verify financial company licenses", "NMLS Consumer Access", "https://www.nmlsconsumeraccess.org", "EN"),
 "BANKFIND": ("Verificar un banco asegurado", "Verify an insured bank", "FDIC BankFind", "https://banks.data.fdic.gov/bankfind-suite/", "EN"),
 "NCUA": ("Buscar una cooperativa asegurada", "Find an insured credit union", "NCUA", "https://mapping.ncua.gov", "EN"),
 "BANKON": ("Cuentas certificadas Bank On", "Bank On certified accounts", "CFE Fund", "https://joinbankon.org", "EN/ES"),
 "AB60": ("Licencia de conducir AB 60", "AB 60 driver's license", "DMV de California", "https://www.dmv.ca.gov/portal/driver-licenses-identification-cards/assembly-bill-ab-60-driver-licenses/", "EN/ES"),
 "MICON": ("Citas en consulados de México (MiConsulado)", "Mexican consulate appointments (MiConsulado)", "SRE", "https://citas.sre.gob.mx", "ES"),
 "CONDUSEF": ("Remesas: compara envíos (Remesamex)", "Compare remittances (Remesamex)", "CONDUSEF", "https://www.condusef.gob.mx/?p=remesas", "ES"),
 "WB": ("Precios de remesas en el mundo", "Remittance Prices Worldwide", "Banco Mundial", "https://remittanceprices.worldbank.org", "EN"),
 "MAF": ("Círculos de préstamo", "Lending circles", "Mission Asset Fund", "https://www.missionassetfund.org/lending-circles/", "EN/ES"),
 "CALBAR": ("Buscar abogado y servicios de referencia", "Find a lawyer and referral services", "State Bar of California", "https://www.calbar.ca.gov", "EN/ES"),
 "EOIR": ("Lista oficial de representantes acreditados", "Recognized organizations and accredited representatives roster", "DOJ EOIR", "https://www.justice.gov/eoir/recognized-organizations-and-accredited-representatives-roster-state-and-city", "EN"),
 "CAAG": ("Recursos para comunidades inmigrantes", "Resources for immigrant communities", "Procuraduría General de California", "https://oag.ca.gov/immigrant", "EN/ES"),
 "PIF": ("Carga pública: ¿aplica a mí?", "Public charge: does it apply to me?", "Protecting Immigrant Families", "https://pifcoalition.org/resources/library/public-charge-does-this-apply-to-me/", "EN/ES"),
 "USCISPC": ("Manual de políticas: carga pública", "Policy Manual: public charge", "USCIS", "https://www.uscis.gov/policy-manual/volume-8-part-g", "EN"),
 "DHCS": ("Medi-Cal", "Medi-Cal", "DHCS de California", "https://www.dhcs.ca.gov", "EN/ES"),
 "COVERED": ("Seguros de salud de California", "Covered California health plans", "Covered California", "https://www.coveredca.com", "EN/ES"),
 "CDI": ("Guías y quejas de seguros", "Insurance guides and complaints", "Departamento de Seguros de California", "https://www.insurance.ca.gov", "EN/ES"),
 "HCAI": ("Programa de facturación justa en hospitales", "Hospital Fair Billing Program", "HCAI de California", "https://hcai.ca.gov/affordability/hospital-fair-billing-program/", "EN"),
 "DMHC": ("Presentar una queja sobre tu plan de salud", "File a complaint about your health plan", "DMHC", "https://www.dmhc.ca.gov/FileaComplaint.aspx", "EN/ES"),
 "READY": ("Prepárate para emergencias", "Prepare for emergencies", "Ready.gov", "https://www.ready.gov/es", "ES (EN: ready.gov)"),
 "CAREG": ("Declaración Jurada de Autorización del Cuidador", "Caregiver's Authorization Affidavit", "Tribunales de California", "https://courts.ca.gov/documents/caregiver.pdf", "EN"),
 "HOTLINE": ("Línea Nacional contra la Violencia Doméstica", "National Domestic Violence Hotline", "The Hotline", "https://www.thehotline.org", "EN/ES"),
 "INV": ("Calculadoras e introducción a la inversión", "Investing calculators and basics", "SEC Investor.gov", "https://www.investor.gov", "EN"),
 "INVES": ("Investor.gov en español", "Investor.gov in Spanish", "SEC", "https://www.investor.gov/informacion-en-espanol", "ES"),
 "BROKER": ("Verificar a un corredor o asesor", "Check a broker or adviser", "FINRA BrokerCheck", "https://brokercheck.finra.org", "EN"),
 "SSA": ("Mi cuenta del Seguro Social", "my Social Security", "SSA", "https://www.ssa.gov/myaccount/", "EN/ES"),
 "SSAINT": ("Acuerdos internacionales de seguridad social", "International social security agreements", "SSA", "https://www.ssa.gov/international/agreements_overview.html", "EN"),
 "CALSAV": ("CalSavers", "CalSavers", "Estado de California", "https://www.calsavers.com", "EN/ES"),
 "ESAR": ("Localiza tu AFORE (e-SAR)", "Find your AFORE (e-SAR)", "CONSAR", "https://www.esar.com.mx/PortalEsar/public/index.do", "ES"),
 "TENANT": ("Guía de derechos de inquilinos y propietarios 2026", "2026 guide to tenants' and landlords' rights", "Departamento de Bienes Raíces de California", "https://www.dre.ca.gov/publications/ResourceGuidebook/2026_Landlord_Tenant_Guide.pdf", "EN"),
 "STUDENT": ("Ayuda federal para estudiar", "Federal student aid", "Departamento de Educación", "https://studentaid.gov", "EN/ES"),
 "SBA": ("Asesoría local para pequeños negocios (SBDC)", "Local small business assistance (SBDC)", "SBA", "https://www.sba.gov/local-assistance", "EN/ES"),
 "CDTFA": ("Permisos de vendedor e impuesto sobre ventas", "Seller's permits and sales tax", "CDTFA", "https://www.cdtfa.ca.gov", "EN/ES"),
}

M = {
 "M1 U01": ["MS","CFPBES"], "M1 U02": ["MS","INV"], "M1 U03": ["EDU","CFPBWB"], "M1 U04": ["EDU","GIG"],
 "M1 U05": ["DIR","CFPBES"], "M1 U06": ["MS","EDU"], "M1 U07": ["EDU","PAYBILLS"], "M1 U08": ["EDU","MS"],
 "M1 U09": ["IRSES","ITIN","FTBFREE"], "M1 U10": ["GIG","SE"], "M1 U11": ["ITIN","CAA","CALEITC","YCTC","VITA"],
 "M1 U12": ["CTEC","VITA","FTBFREE"], "M1 U13": ["PIF","USCISPC","DHCS"], "M1 U14": ["EDU","CFPBWB"],
 "M2 U01": ["MS","CFPBES","BANKFIND"], "M2 U02": ["BANKFIND","NCUA","BANKON"], "M2 U03": ["AB60","MICON","CHECK"],
 "M2 U04": ["BANKON","CHECK","NEWC"], "M2 U05": ["PAYBILLS","CFPBES"], "M2 U06": ["REMIT","CONDUSEF"],
 "M2 U07": ["REMIT","EDU"], "M2 U08": ["CONDUSEF","WB","REMIT"], "M2 U09": ["DFPI","NMLS","REMIT"],
 "M2 U10": ["REMIT","CFPBES"], "M2 U11": ["CONS","RF"], "M2 U12": ["CONDUSEF","NEWC"], "M2 U13": ["NEWC","BANKON","REMIT"],
 "M3 U01": ["CRED","MS"], "M3 U02": ["ACR","CRED"], "M3 U03": ["CRED","MAF","NEWC"], "M3 U04": ["CRED","CONS"],
 "M3 U05": ["CFPBES","AUTO"], "M3 U06": ["MS","EDU"], "M3 U07": ["COLL","CALBAR"], "M3 U08": ["CFPBES","MS"],
 "M3 U09": ["MAF"], "M3 U10": ["ACR","CRED"],
 "M4 U01": ["CONS","RF","FTCIMM"], "M4 U02": ["FTCIMM2","EOIR","CALBAR","CAAG"], "M4 U03": ["CONS","IDT"],
 "M4 U04": ["IDT","CRED","RF"], "M4 U05": ["HOTLINE","CFPBES"], "M4 U06": ["EDU","MS"], "M4 U07": ["CDI","COVERED"],
 "M4 U08": ["HCAI","DMHC","DHCS"], "M4 U09": ["READY","CDI"], "M4 U10": ["CAREG","EOIR","READY"], "M4 U11": ["IDT","READY"],
 "M5 U01": ["MS","CFPBWB"], "M5 U02": ["INVES","INV"], "M5 U03": ["BROKER","INVES"], "M5 U04": ["TENANT","HCOUNS","HOME"],
 "M5 U05": ["AUTO","STUDENT"], "M5 U06": ["SSA","CALSAV","INV"], "M5 U07": ["ESAR","SSAINT"], "M5 U08": ["CFPBES","CALBAR"],
 "M5 U09": ["EDU","CFPBES"], "M5 U10": ["EIN","SBA","CDTFA"], "M5 U11": ["EDU","CFPBWB"],
}

def block(lesson, lang):
    ids = M[lesson]
    if lang == "es":
        lines = ["### Para saber más", "", "Recursos gratuitos y oficiales para profundizar (verificados el 28 de septiembre de 2026):", ""]
        for i in ids:
            n, _, org, url, idi = R[i]
            lines.append(f"- **{n}** ({org}; idioma: {idi}): {url}")
    else:
        lines = ["### Learn more", "", "Free, official resources to go further (verified September 28, 2026):", ""]
        for i in ids:
            _, n, org, url, idi = R[i]
            idi = idi.replace("algunas en ES","some in Spanish").replace("versión ES en la misma serie","Spanish version in the same series").replace("ES en CFPB en español","Spanish on CFPB en español").replace("EN disponible","EN available")
            lines.append(f"- **{n}** ({org}; language: {idi}): {url}")
    return "\n".join(lines) + "\n\n"

def process(lang, files, marker):
    done = set()
    for f in files:
        p = os.path.join(BASE, "manual", lang, f)
        s = open(p).read()
        s = re.sub(r"### (Para saber más|Learn more)\n.*?\n\n(?=\*\*(Palabras clave|Key words))", "", s, flags=re.S)
        out, cur = [], None
        for line in s.split("\n"):
            m = re.match(r"^## (M\d U\d\d)\.", line)
            if m: cur = m.group(1)
            if line.startswith(marker) and cur and cur not in done:
                out.append(block(cur, lang).rstrip("\n")); out.append("")
                done.add(cur)
            out.append(line)
        open(p, "w").write("\n".join(out))
    return done

files = ["M1a.md","M1b.md","M2a.md","M2b.md","M3.md","M4a.md","M4b.md","M5a.md","M5b.md"]
es = process("es", files, "**Palabras clave:**")
en = process("en", files, "**Key words:**")
print("ES", len(es), "EN", len(en), "missing", sorted(set(M) - es), sorted(set(M) - en))

# Catálogo y CSV para Moodle
rows = []
for les, ids in M.items():
    for i in ids:
        n_es, n_en, org, url, idi = R[i]
        rows.append([les, i, n_es, n_en, org, url, idi])
with open(os.path.join(BASE, "recursos", "para_saber_mas_moodle.csv"), "w", newline="") as fh:
    w = csv.writer(fh); w.writerow(["leccion","id_recurso","nombre_es","nombre_en","organizacion","url","idioma"]); w.writerows(rows)
with open(os.path.join(BASE, "recursos", "catalogo_recursos.md"), "w") as fh:
    fh.write("# Catálogo de recursos gratuitos oficiales\n\nVerificados por búsqueda web el 28 de septiembre de 2026. Revisar enlaces cada 6 meses.\n\n| ID | Recurso | Organización | Idioma | URL | Lecciones |\n|---|---|---|---|---|---|\n")
    for i,(n_es,n_en,org,url,idi) in R.items():
        les = ", ".join(l for l,ids in M.items() if i in ids)
        fh.write(f"| {i} | {n_es} | {org} | {idi} | {url} | {les} |\n")
json.dump({"recursos": R, "mapa": M}, open(os.path.join(BASE, "recursos", "para_saber_mas.json"), "w"), ensure_ascii=False, indent=1)
print("recursos", len(R), "filas", len(rows))
