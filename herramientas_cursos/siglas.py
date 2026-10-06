# Explica las siglas en su primera aparición en cada lección (E06, accesibilidad):
# si la sigla aparece en un párrafo de lectura, se convierte en definición emergente {{SIGLA|…}};
# si solo aparece en tablas o tarjetas, se agrega a «Palabras» de la lección.
# Uso: python3 herramientas_cursos/siglas.py [cursos/<curso> …]   (sin argumentos: todos los cursos)
import os, re, sys, json, glob

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import accesibilidad as A

S = {  # sigla: (español, inglés)
 "CNBV": ("Comisión Nacional Bancaria y de Valores, que supervisa a bancos y otras instituciones financieras en México.", "Comisión Nacional Bancaria y de Valores, Mexico's banking and securities regulator."),
 "VITA": ("Volunteer Income Tax Assistance: programa del IRS que prepara declaraciones sin costo a personas con ingresos bajos o medios.", "Volunteer Income Tax Assistance: an IRS program that prepares tax returns at no cost for people with low or moderate income."),
 "IPAB": ("Instituto para la Protección al Ahorro Bancario, que protege tus depósitos en bancos hasta un límite.", "Instituto para la Protección al Ahorro Bancario, which protects bank deposits up to a limit in Mexico."),
 "RESICO": ("Régimen Simplificado de Confianza del SAT, para personas con ingresos bajos y medios.", "Régimen Simplificado de Confianza, a simplified SAT tax regime for low and middle incomes."),
 "CNSF": ("Comisión Nacional de Seguros y Fianzas, que supervisa a las aseguradoras.", "Comisión Nacional de Seguros y Fianzas, Mexico's insurance regulator."),
 "DFPI": ("Departamento de Protección e Innovación Financiera de California, que supervisa a prestamistas y cobradores.", "California Department of Financial Protection and Innovation, which oversees lenders and debt collectors."),
 "LISR": ("Ley del Impuesto sobre la Renta.", "Ley del Impuesto sobre la Renta, Mexico's income tax law."),
 "SBA": ("Administración de Pequeños Negocios de EE. UU., que orienta y respalda créditos para negocios.", "U.S. Small Business Administration, which advises small businesses and backs business loans."),
 "EDD": ("Departamento de Desarrollo del Empleo de California: desempleo, incapacidad e impuestos de nómina.", "California Employment Development Department: unemployment, disability and payroll taxes."),
 "FTB": ("Franchise Tax Board: la oficina de impuestos estatales de California.", "Franchise Tax Board: California's state tax agency."),
 "SEC": ("Comisión de Bolsa y Valores de EE. UU., que supervisa inversiones y asesores.", "U.S. Securities and Exchange Commission, which oversees investments and advisers."),
 "SAR": ("Sistema de Ahorro para el Retiro: las cuentas de Afore.", "Sistema de Ahorro para el Retiro: Mexico's Afore retirement accounts system."),
 "INEGI": ("Instituto Nacional de Estadística y Geografía.", "Instituto Nacional de Estadística y Geografía, Mexico's statistics agency."),
 "CONASAMI": ("Comisión Nacional de los Salarios Mínimos, que fija el salario mínimo cada año.", "Comisión Nacional de los Salarios Mínimos, which sets Mexico's minimum wage."),
 "PRODECON": ("Procuraduría de la Defensa del Contribuyente: te orienta sin costo si tienes un problema con el SAT.", "Procuraduría de la Defensa del Contribuyente: no-cost help with SAT problems."),
 "SBDC": ("Centros de Desarrollo de Pequeños Negocios: asesoría sin costo o de bajo costo para negocios.", "Small Business Development Centers: no-cost or low-cost business advice."),
 "SCORE": ("Red de mentores voluntarios para negocios, con apoyo de la SBA.", "A network of volunteer business mentors, supported by the SBA."),
 "REDECO": ("Registro de Despachos de Cobranza de la CONDUSEF, donde puedes quejarte de un cobrador.", "CONDUSEF's registry of collection agencies, where you can complain about a collector."),
 "DOF": ("Diario Oficial de la Federación, donde se publican las leyes y reglas oficiales.", "Diario Oficial de la Federación, Mexico's official gazette."),
 "APR": ("Tasa de porcentaje anual: el costo de un crédito al año, con intereses y algunos cargos.", "Annual percentage rate: the yearly cost of credit, including interest and some fees."),
 "USCIS": ("Servicio de Ciudadanía e Inmigración de EE. UU.", "U.S. Citizenship and Immigration Services."),
 "FINRA": ("Autoridad que regula a las casas de bolsa en EE. UU.; tiene BrokerCheck para verificar asesores.", "Financial Industry Regulatory Authority; its BrokerCheck lets you verify brokers."),
 "UDIS": ("Unidades de Inversión: un valor que sube con la inflación.", "Unidades de Inversión: a Mexican unit of value that rises with inflation."),
 "SOFIPO": ("Sociedad Financiera Popular: institución de ahorro y crédito autorizada; verifícala en el SIPRES.", "Sociedad Financiera Popular: an authorized savings and loan institution; check it in SIPRES."),
 "INDAUTOR": ("Instituto Nacional del Derecho de Autor, donde registras tus obras.", "Instituto Nacional del Derecho de Autor, where you register your works in Mexico."),
 "FBI": ("Buró Federal de Investigaciones de EE. UU.; recibe denuncias de fraude en línea (ic3.gov).", "Federal Bureau of Investigation; it takes online fraud reports at ic3.gov."),
 "IRA": ("Cuenta individual de retiro en EE. UU., con beneficios de impuestos.", "Individual retirement account, with tax benefits."),
 "SARTEL": ("Línea telefónica de la CONSAR para dudas sobre tu Afore: 55 1328 5000.", "CONSAR's phone line for Afore questions: 55 1328 5000."),
 "SOFOM": ("Sociedad Financiera de Objeto Múltiple: institución que presta dinero; verifícala en el SIPRES.", "Sociedad Financiera de Objeto Múltiple: a lending institution; check it in SIPRES."),
 "SOCAP": ("Sociedad Cooperativa de Ahorro y Préstamo autorizada; verifícala en el SIPRES.", "Sociedad Cooperativa de Ahorro y Préstamo, an authorized savings cooperative; check it in SIPRES."),
 "CDTFA": ("Departamento de Administración de Impuestos y Tarifas de California: impuesto sobre ventas.", "California Department of Tax and Fee Administration: sales tax."),
 "YCTC": ("Crédito por Hijos Pequeños de California, para familias con hijos menores de 6 años.", "California Young Child Tax Credit, for families with children under 6."),
 "TCE": ("Tax Counseling for the Elderly: ayuda sin costo del IRS para declarar, sobre todo a personas de 60 años o más.", "Tax Counseling for the Elderly: no-cost IRS tax help, mainly for people 60 and older."),
 "WIC": ("Programa de nutrición para mujeres embarazadas, bebés y niños menores de 5 años.", "Nutrition program for pregnant women, infants and children under 5."),
 "DMV": ("Departamento de Vehículos Motorizados: licencias e identificaciones estatales.", "Department of Motor Vehicles: driver's licenses and state IDs."),
 "SIPC": ("Corporación que protege tus inversiones si quiebra la casa de bolsa (no si bajan de valor).", "Securities Investor Protection Corporation: protects your investments if the brokerage fails (not if they lose value)."),
 "DOJ": ("Departamento de Justicia de EE. UU.; acredita a representantes que pueden dar ayuda migratoria.", "U.S. Department of Justice; it accredits representatives who may give immigration help."),
 "TOD": ("Transfer on death: beneficiario que recibe una cuenta o bien al fallecer el dueño, sin juicio sucesorio.", "Transfer on death: a beneficiary who receives an account or asset when the owner dies, without probate."),
 "POD": ("Payable on death: beneficiario de una cuenta de banco.", "Payable on death: a bank account beneficiary."),
 "PTIN": ("Número que el IRS da a quien prepara declaraciones; pídeselo a tu preparador.", "The IRS number tax preparers must have; ask your preparer for it."),
 "CDI": ("Departamento de Seguros de California: verifica licencias de agentes y aseguradoras.", "California Department of Insurance: check agent and insurer licenses."),
 "CSLB": ("Junta Estatal de Licencias de Contratistas de California.", "California Contractors State License Board."),
 "FEMA": ("Agencia Federal para el Manejo de Emergencias de EE. UU.", "Federal Emergency Management Agency."),
 "DIR": ("Departamento de Relaciones Industriales de California: salarios y derechos laborales.", "California Department of Industrial Relations: wages and labor rights."),
 "CFE": ("Comisión Federal de Electricidad.", "Comisión Federal de Electricidad, Mexico's electricity company."),
 "CETES": ("Certificados de la Tesorería: deuda del gobierno de México en la que puedes invertir desde 100 pesos.", "Mexican government Treasury certificates you can invest in from 100 pesos."),
 "GAT": ("Ganancia Anual Total: lo que gana tu ahorro al año, para comparar cuentas e inversiones.", "Ganancia Anual Total: what your savings earn per year, to compare accounts and investments."),
 "PROFEDET": ("Procuraduría Federal de la Defensa del Trabajo: orientación laboral sin costo.", "Procuraduría Federal de la Defensa del Trabajo: no-cost labor advice."),
 "ICE": ("Servicio de Inmigración y Control de Aduanas de EE. UU.", "U.S. Immigration and Customs Enforcement."),
 "MTU": ("Monto Transaccional del Usuario: el límite de transferencias que pones en tu app del banco.", "Monto Transaccional del Usuario: the transfer limit you set in your bank app."),
 "BLS": ("Oficina de Estadísticas Laborales de EE. UU.", "U.S. Bureau of Labor Statistics."),
 "NEC": ("Formulario 1099-NEC: reporta pagos a personas que trabajan por su cuenta.", "Form 1099-NEC: reports payments to self-employed people."),
 "LSS": ("Ley del Seguro Social.", "Ley del Seguro Social, Mexico's social security law."),
 "PRLV": ("Pagaré con Rendimiento Liquidable al Vencimiento: inversión bancaria a plazo fijo.", "A Mexican fixed-term bank investment that pays at maturity."),
 "SIC": ("Sistema Internacional de Cotizaciones: acciones y fondos extranjeros que se compran en la bolsa mexicana.", "Sistema Internacional de Cotizaciones: foreign stocks and funds bought on the Mexican exchange."),
 "ANDA": ("Asociación Nacional de Actores.", "Asociación Nacional de Actores, Mexico's actors' union."),
 "BONDDIA": ("Fondo de Cetesdirecto que puedes retirar cualquier día hábil.", "A Cetesdirecto fund you can withdraw from any business day."),
 "CFDI": ("Comprobante Fiscal Digital por Internet: la factura electrónica del SAT.", "Comprobante Fiscal Digital por Internet: SAT's electronic invoice."),
 "IMPI": ("Instituto Mexicano de la Propiedad Industrial, donde registras tu marca.", "Instituto Mexicano de la Propiedad Industrial, where you register a trademark in Mexico."),
 "MSI": ("Meses sin intereses.", "Meses sin intereses: interest-free monthly installments."),
 "NAFTRAC": ("Fondo que cotiza en bolsa y sigue a las principales empresas de la Bolsa Mexicana.", "An exchange-traded fund that tracks the main companies on the Mexican stock exchange."),
 "PPR": ("Plan Personal de Retiro, con beneficios fiscales si lo dejas hasta el retiro.", "Plan Personal de Retiro, a Mexican retirement plan with tax benefits."),
 "RECA": ("Registro de Contratos de Adhesión de la CONDUSEF, donde puedes ver contratos autorizados.", "CONDUSEF's registry of standard financial contracts."),
 "REPEP": ("Registro Público para Evitar Publicidad, de Profeco.", "Profeco's registry to stop advertising calls."),
 "RMF": ("Resolución Miscelánea Fiscal: reglas del SAT que se publican cada año.", "Resolución Miscelánea Fiscal: SAT rules published every year."),
 "SACM": ("Sociedad de Autores y Compositores de México, que cobra regalías.", "Mexico's society of authors and composers, which collects royalties."),
 "SHCP": ("Secretaría de Hacienda y Crédito Público.", "Secretaría de Hacienda y Crédito Público, Mexico's finance ministry."),
 "SOMEXFON": ("Sociedad Mexicana de Productores de Fonogramas, que cobra regalías por música grabada.", "Mexican society of record producers, which collects royalties for recorded music."),
 "UDI": ("Unidad de Inversión: un valor que sube con la inflación.", "Unidad de Inversión: a Mexican unit of value that rises with inflation."),
 "UNE": ("Unidad Especializada de Atención a Usuarios: el área de cada institución financiera que recibe quejas.", "Each financial institution's complaints unit in Mexico."),
 "SIM": ("Tarjeta SIM: el chip de tu celular que tiene tu número.", "SIM card: the chip in your phone that holds your number."),
}
NO_SIGLA = {"XXII", "XXIII", "START", "GAMBLER", "XIII", "XVII", "VIII", "III", "XVI", "XVIII", "XXIX", "XIV", "XV", "XIX", "XXI"}
PROSA = re.compile(r"^(?!---|\||\* fa-|\?|=|[-+×÷] ?\d|#|[0-9]+\.\s.*\|\|)")


def procesa(D):
    cfg = json.load(open(os.path.join(D, "curso.json"), encoding="utf-8"))
    en = cfg.get("lang") == "en"; k = 1 if en else 0
    tot_t, tot_p, faltan = 0, 0, set()
    for m in cfg["modulos"]:
        p = os.path.join(D, "lecciones", f"{m}.md")
        if not os.path.exists(p): continue
        txt = open(p, encoding="utf-8").read()
        partes = re.split(r"(?m)^(?=# M\d+ U\d+)", txt)
        nuevas = []
        for b in partes:
            if not b.startswith("# M"): nuevas.append(b); continue
            cuerpo = b.split("\n", 1)[1]
            secs = {"_": cuerpo.split("\n== ", 1)[0]}
            for s in re.split(r"(?m)^== ", cuerpo)[1:]:
                n, t = (s.split("\n", 1) + [""])[:2]; secs[n.strip()] = t
            pars = A.prosa(secs.get("esencial", "")) + A.prosa(secs.get("profundiza", ""))
            expl = (secs.get("palabras", "") + " " + " ".join(re.findall(r"\{\{([^|}]+)\|", b))).upper()
            sig = sorted({s for s in re.findall(r"\b[A-ZÁÉÍÓÚÑ]{3,}\b", " ".join(pars))
                          if s not in A.SIGLAS_COMUNES and s not in NO_SIGLA and s not in expl
                          and not re.search(rf"\b{s}\b\s*\(|\(\s*{s}\s*\)", b)})
            agregar = []
            for s in sig:
                if s not in S: faltan.add(s); continue
                d = S[s][k]
                # primera aparición en una línea de prosa de «esencial» o «profundiza», fuera de enlaces y URL
                lineas = b.split("\n"); hecho = False; sec = None
                for i, ln in enumerate(lineas):
                    if ln.startswith("== "): sec = ln[3:].strip(); continue
                    if sec not in ("esencial", "profundiza") or not PROSA.match(ln.strip()) or not ln.strip(): continue
                    for mm in re.finditer(rf"\b{s}\b", ln):
                        antes = ln[:mm.start()]
                        if antes.count("[") > antes.count("]") or antes.count("{{") > antes.count("}}") or re.search(r"https?://\S*$", antes): continue
                        lineas[i] = ln[:mm.start()] + "{{" + s + "|" + d + "}}" + ln[mm.end():]
                        hecho = True; break
                    if hecho: break
                if hecho: b = "\n".join(lineas); tot_t += 1
                else: agregar.append(f"- *{s}:* {d}"); tot_p += 1
            if agregar:
                if re.search(r"(?m)^== palabras\n", b):
                    b = re.sub(r"(?m)^(== palabras\n)", lambda mm: mm.group(1) + "\n".join(agregar) + "\n", b, count=1)
                else:
                    b = b.rstrip("\n") + "\n\n== palabras\n" + "\n".join(agregar) + "\n\n"
            nuevas.append(b)
        nuevo = "".join(nuevas)
        if nuevo != txt: open(p, "w", encoding="utf-8").write(nuevo)
    return tot_t, tot_p, faltan


if __name__ == "__main__":
    ds = sys.argv[1:] or sorted(glob.glob(os.path.join(BASE, "cursos", "*")))
    for D in ds:
        t, p, f = procesa(D.rstrip("/"))
        if t or p or f: print(os.path.basename(D.rstrip("/")), f"· definiciones emergentes: {t} · en «Palabras»: {p}" + (f" · sin definición: {', '.join(sorted(f))}" if f else ""))
