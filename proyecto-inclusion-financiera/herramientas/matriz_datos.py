# Datos de la matriz comparativa. Fecha de verificación: 2026-09-28 (búsqueda web).
# Campos: id, categoria, nombre, costo_mensual, costos_clave, identificacion, ssn_itin, efectivo, cobertura, ventaja, cuidado, fuente, estado
import json, os
F = "2026-09-28"
V, P = "verificado", "por confirmar"
rows = []
def add(cat, nombre, costo, clave, ident, ssn, efectivo, cob, ventaja, cuidado, fuente, estado=V):
    rows.append(dict(categoria=cat, nombre=nombre, costo_mensual=costo, costos_clave=clave, identificacion=ident,
        ssn_itin=ssn, efectivo=efectivo, cobertura=cob, ventaja=ventaja, cuidado=cuidado, fuente=fuente, fecha=F, estado=estado))

B = "Banco"
add(B,"Bank of America Advantage SafeBalance","$4.95","Exento si <25 años, saldo diario $500 o Preferred Rewards; apertura $25","Pasaporte y otras; confirmar en sucursal","SSN; ITIN por confirmar","Sí, en cajeros y sucursales","Nacional","Sin sobregiros","Cobro mensual si no cumples exención","https://www.bankofamerica.com/deposits/checking/advantage-banking/",P)
add(B,"Chase Secure Banking","$4.95","Exento de 17 a 24 años o con $250 en depósitos electrónicos","Pasaporte y matrícula consular","SSN o ITIN para tarjeta de débito","Sí, en cajeros y sucursales","Nacional","Sin sobregiros; Zelle incluido","Cobro mensual si no cumples exención","https://www.chase.com/personal/checking/secure-banking")
add(B,"Wells Fargo Clear Access Banking","$5","Exento de 13 a 24 años o con depósito militar","Pasaporte y otras; confirmar en sucursal","SSN; ITIN no indicado","Sí, en cajeros y sucursales","Nacional","Sin sobregiros","Exención limitada a jóvenes","https://www.wellsfargo.com/checking/clear-access-banking/",P)
add(B,"Citi Access Checking","$5","Exento con $250 en depósitos directos o transacciones; ≤23 años desde 18 jul 2026","Confirmar en sucursal","Confirmar","Sí, en cajeros Citi","Nacional (sucursales en CA)","Sin sobregiros","Requisitos de exención cambian","https://www.citi.com/banking/access-account",P)
add(B,"U.S. Bank Safe Debit","$4.95","No se puede exentar; apertura $25","Matrícula consular como ID principal en sucursal + ID secundaria","SSN o ITIN para la mayoría de cuentas","Sí","Nacional","Acepta matrícula","Sin cheques; cobro fijo","https://www.usbank.com/bank-accounts/checking-accounts/safe-debit-account.html")
add(B,"Capital One 360 Checking","$0","Sin mínimos","Confirmar","SSN o ITIN","Gratis en CVS y Walgreens (hasta $1,500 al día y $5,000 al mes)","Nacional","Sin cuotas; depósito en efectivo gratis","Pocas sucursales","https://www.capitalone.com/bank/checking-accounts/online-checking-account/")
add(B,"BMO Smart Advantage","$0 con estados de cuenta digitales ($3 en papel)","Exento a los 65 años o más; sobregiro $20","No residentes abren en sucursal","SSN o ITIN","Sí","Nacional (fuerte en IL)","Sin cuota con estados digitales","Cobro de sobregiro","https://www.bmo.com/en-us/main/personal/checking-accounts/smart-advantage/")

C = "Cooperativa (credit union)"
add(C,"Self-Help Federal Credit Union","Varía por cuenta","Membresía","Identificación estatal, green card, pasaporte, SF City ID; matrícula no listada","SSN o ITIN (solo el número)","Sí, en sucursales","CA, CT, IL, SC, WA, WI","Acepta ITIN; enfoque en comunidades latinas","Matrícula no aparece en lista","https://www.self-helpfcu.org/")
add(C,"Golden 1 Credit Union","$0 en varias cuentas","$1 en ahorro para mantener membresía","Confirmar","SSN; ITIN por confirmar","Sí, en sucursales y cajeros","Quien vive o trabaja en CA","Cuentas certificadas Bank On","Confirmar documentos","https://www.golden1.com/",P)
add(C,"Kinecta Federal Credit Union","$0 con $250 en depósito directo o depósito móvil","Classic Checking","Confirmar","Confirmar ITIN","Sí","Sur de CA","Cuota exentable fácilmente","Confirmar ITIN","https://www.kinecta.org/",P)
add(C,"SchoolsFirst Federal Credit Union","$0","Apertura $25","Confirmar","Confirmar ITIN","Sí","Empleados escolares y familia en CA","Sin cuota","Membresía restringida","https://www.schoolsfirstfcu.org/",P)
add(C,"Patelco Credit Union","$0","Free Checking","Confirmar","Confirmar ITIN","Sí","Norte de CA","Sin cuota","Confirmar ITIN","https://www.patelco.org/",P)
add(C,"San Diego County Credit Union (SDCCU)","$0 con estados digitales","Membresía sur de CA o asociación de $8","Confirmar","Confirmar ITIN","Sí","Sur de CA","Sin cuota","Confirmar ITIN","https://www.sdccu.com/",P)
add(C,"Valley Strong Credit Union","$0","Basic Access Account","Confirmar","Confirmar","Sí","Valle Central de CA","Certificada Bank On","Confirmar documentos","https://www.valleystrong.com/",P)
add(C,"CU SoCal","$0 con estados digitales","Classic Checking; apertura $25","Confirmar","SSN o ITIN","Sí","Sur de CA","Acepta ITIN","Apertura $25","https://www.cusocal.org/")
add(C,"Atchison Village Credit Union","Varía","Designación Juntos Avanzamos","Acepta ID alternativa","Acepta ITIN","Sí","Richmond, CA","Designada para inmigrantes","Una sola sucursal","https://www.avcu.org/")
add(C,"Community First Credit Union","Varía","Designación Juntos Avanzamos","Acepta ID alternativa","Acepta ITIN","Sí","CA (Santa Rosa)","Designada para inmigrantes","Confirmar cobertura","https://www.comfirstcu.org/",P)
add(C,"Comunidad Latina Federal Credit Union","Varía","Designación Juntos Avanzamos","Acepta ID alternativa","Acepta ITIN","Sí","Santa Ana, CA","Enfocada en comunidad latina","Cobertura local","https://www.comunidadlatinafcu.org/",P)
add(C,"Downey Federal Credit Union","Varía","Designación Juntos Avanzamos","Acepta ID alternativa","Acepta ITIN","Sí","Downey, CA","Designada para inmigrantes","Cobertura local","https://www.downeyfcu.org/",P)
add(C,"Excite Credit Union","Varía","Designación Juntos Avanzamos","Acepta ID alternativa","Acepta ITIN","Sí","San José, CA","Designada para inmigrantes","Cobertura local","https://www.excitecu.org/",P)
add(C,"Merco Credit Union","Varía","Designación Juntos Avanzamos","Acepta ID alternativa","Acepta ITIN","Sí","Merced, CA","Designada para inmigrantes","Cobertura local","https://www.mercocu.org/",P)
add(C,"USC Credit Union","Varía","Designación Juntos Avanzamos","Acepta ID alternativa","Acepta ITIN","Sí","Los Ángeles, CA","Designada para inmigrantes","Membresía por vínculo con USC o zona","https://www.usccreditunion.org/",P)
add(C,"Altura Credit Union","Varía","Designación Juntos Avanzamos","Acepta ID alternativa","Acepta ITIN","Sí","Inland Empire, CA","Designada para inmigrantes","Cobertura regional","https://www.alturacu.com/",P)
add(C,"LA Federal Credit Union CONNECT","$0 o bajo","Certificada Bank On","Confirmar","Confirmar","Sí","Los Ángeles, CA","Cuenta Bank On","Confirmar documentos","https://joinbankon.org/accounts/",P)
add(C,"Ventura County Credit Union Simply Essential Checking","$0 o bajo","Certificada Bank On","Confirmar","Confirmar","Sí","Condado de Ventura, CA","Cuenta Bank On","Confirmar documentos","https://joinbankon.org/accounts/",P)

N = "Neobanco o app"
add(N,"Comun","$0","Sin saldo mínimo; remesas desde $2.99","Pasaporte, matrícula consular o ID nacional","No requiere SSN ni ITIN","Confirmar","Nacional","Abre sin SSN; Zelle; banco aliado asegurado por FDIC","No es banco; revisa el banco aliado","https://www.comun.app/")
add(N,"Majority","$6.99","Membresía mensual","Pasaporte, matrícula","ITIN; no requiere SSN","Confirmar","Nacional","Diseñada para migrantes","Cuota mensual","https://majority.com/")
add(N,"Zolve","$0","Cuenta y tarjeta","Pasaporte + visa","SSN o ITIN (tarjeta sin SSN)","Confirmar","Nacional","Tarjeta de crédito sin historial","Enfoque en personas con visa","https://zolve.com/")
add(N,"Chime","$0","Depósitos gratis en Walgreens; $3 a $5 en otras tiendas","Confirmar","Fuentes contradictorias: SSN solo o SSN/ITIN","Walgreens gratis; otros con costo","Nacional","Sin cuotas; SpotMe","Confirmar si acepta ITIN","https://www.chime.com/",P)
add(N,"Varo","$0","Sin cuotas mensuales","Confirmar","SSN o ITIN","Gratis en CVS","Nacional","Es banco con licencia propia","Pocas opciones de efectivo","https://www.varomoney.com/")
add(N,"Current","$0","Depósito en efectivo $3.50","Confirmar","Requiere SSN","$3.50 por depósito","Nacional","Sin cuotas","Requiere SSN","https://current.com/")
add(N,"SoFi Checking and Savings","$0","Intereses en ahorro","Confirmar","SSN o ITIN","Limitado","Nacional","Sin cuotas; interés alto","Poco efectivo","https://www.sofi.com/banking/")
add(N,"Revolut US","$0 plan básico","Transferencia internacional $5","Pasaporte + visa","SSN o ITIN","Confirmar","Nacional","Multimoneda","Costos por transferencia","https://www.revolut.com/en-US/")
add(N,"OnePay (Walmart)","$0","Sin cuotas","Confirmar","SSN o ITIN","Gratis en Walmart y otras","Nacional","Efectivo en Walmart","Confirmar requisitos","https://www.onepay.com/")
add(N,"Cash App","$0","Depósito en tienda desde $1","Confirmar","Últimos 4 de SSN o ITIN; funciones completas pueden requerir SSN","En tiendas participantes","Nacional","Fácil de usar","Estafas frecuentes por pagos entre personas","https://cash.app/")
add(N,"PayPal / Venmo","$0","Transferencia instantánea 1.75% (mín $0.25, máx $25)","Confirmar","Confirmar ITIN","Limitado","Nacional","Muy usada","Cobro por transferencia instantánea","https://www.paypal.com/us/",P)

R = "Remesadora (EE. UU. a México)"
add(R,"Remitly","N/A","Express ~$1.99; Economy $0; margen cambiario ~1%","Confirmar","Confirmar","Sí, en efectivo según plan","EE. UU. a México","Mejor tipo de cambio desde $500","Revisa tipo de cambio","https://www.remitly.com/us/en/mexico")
add(R,"Western Union","N/A","$0 primer envío en línea; ~$5 en línea; $11 a $16 en agente; margen cambiario","ID oficial","Confirmar","Sí","EE. UU. a México","Red enorme de pago","Agente cuesta más; límite efectivo $7,499","https://www.westernunion.com/us/en/send-money-to-mexico.html")
add(R,"MoneyGram","N/A","$0 desde cuenta en línea; hasta ~$12 con débito; margen 1% a 3%","ID oficial","Confirmar","Sí","EE. UU. a México","Opciones de pago variadas","Retiro en efectivo más caro","https://www.moneygram.com/")
add(R,"Xoom (PayPal)","N/A","$0 desde banco o saldo PayPal; margen 1% a 3%","Confirmar","Confirmar","Pago en OXXO, Elektra, BanCoppel","EE. UU. a México","No paga impuesto de 1% si se fondea con banco","Margen cambiario","https://www.xoom.com/mexico/send-money")
add(R,"Wise","N/A","~0.5% a 0.7%; tipo de cambio real","Confirmar","Confirmar","No","EE. UU. a México (SPEI)","Tipo de cambio de mercado","Con tarjeta de débito cuesta más","https://wise.com/us/send-money/send-money-to-mexico")
add(R,"Ria / Walmart2Walmart","N/A","Desde $2.50; cuota $0.99 a $9; margen 0.25% a 3.5%","ID oficial","Confirmar","Sí; 48,000 puntos de pago","EE. UU. a México","Envío en efectivo en Walmart","Margen variable","https://www.riamoneytransfer.com/")
add(R,"Intermex","N/A","$0 primer envío; luego desde $2.99","ID oficial","Confirmar","Sí","EE. UU. a México","Red amplia en México","Revisa tipo de cambio","https://www.intermexonline.com/")
add(R,"Félix Pago","N/A","$2.99 a banco; $4.98 en efectivo","Confirmar","Confirmar","Pago en efectivo en México","EE. UU. a México","Envía por WhatsApp","Usa USDC internamente","https://www.felixpago.com/")
add(R,"BOSS Revolution","N/A","$0.99 a billeteras con débito (promoción al 30 sep 2026)","Confirmar","Confirmar","Confirmar","EE. UU. a México","Barato a billeteras","Promoción temporal","https://www.bossrevolution.com/",P)
add(R,"Pangea","N/A","Primer envío gratis","Confirmar","Confirmar","40,000 puntos de pago","EE. UU. a México","Primera transferencia gratis","Revisa tipo de cambio","https://pangeamoneytransfer.com/")
add(R,"Sendwave","N/A","Sin cuota; margen 1% a 3%","Confirmar","Confirmar","Confirmar","EE. UU. a México","Sin comisión visible","El costo va en el tipo de cambio","https://www.sendwave.com/")
add(R,"WorldRemit","N/A","Variable","Confirmar","Confirmar","Confirmar","EE. UU. a México","Varias formas de pago","Costos variables","https://www.worldremit.com/",P)
add(R,"Viamericas","N/A","No encontrado","Confirmar","Confirmar","Confirmar","EE. UU. a México","Red de agentes","Datos no verificados","https://www.viamericas.com/",P)

K = "Construcción de crédito"
add(K,"Self Credit Builder","$9 de administración","APR 15.82%; ~$89 de interés en plan $25 a 24 meses","Confirmar","SSN (ITIN no claro)","N/A","Nacional","Reporta a 3 burós","Pagas intereses por ahorrar","https://www.self.inc/",P)
add(K,"Capital One Platinum Secured","$0 anualidad","Depósito $49, $99 o $200","Confirmar","SSN o ITIN","N/A","Nacional","Depósito bajo; 3 burós","Tasa alta si no pagas completo","https://www.capitalone.com/credit-cards/platinum-secured/")
add(K,"OpenSky Secured Visa","$35 anual","Depósito $200 a $3,000","Confirmar","SSN o ITIN","N/A","Nacional","Sin revisión de crédito","Anualidad","https://www.openskycc.com/")
add(K,"OpenSky Plus Secured Visa","$0 anualidad","Depósito desde $300 (confirmar)","Confirmar","SSN o ITIN","N/A","Nacional","Sin anualidad ni revisión de crédito","Depósito mayor","https://www.openskycc.com/",P)
add(K,"Chime Card (antes Credit Builder)","$0","Requiere cuenta Chime y $200 en depósito directo","Confirmar","Ver Chime","N/A","Nacional","Sin revisión de crédito","Credit Builder ya no acepta nuevas solicitudes","https://www.chime.com/",P)
add(K,"Kikoff","$5, $20 o $35","Plan mensual","Confirmar","SSN o TIN","N/A","Nacional","Barato","Fuentes contradictorias sobre a qué burós reporta","https://kikoff.com/",P)
add(K,"Mission Asset Fund: círculos de préstamo","$0","Préstamos de $300 a $2,400 al 0%","Confirmar","Acepta ITIN","N/A","Nacional (sede en CA)","0% interés; reporta a 3 burós; tel. 888-274-4808","Requiere compromiso grupal","https://www.missionassetfund.org/lending-circles/")
add(K,"Discover it Secured","$0","Solicitudes pausadas desde 2 jun 2026","Confirmar","Aceptaba ITIN","N/A","Nacional","Aceptaba ITIN","Pausada; relanzamiento de Capital One pendiente","https://www.discover.com/credit-cards/secured/",P)
add(K,"Nova Credit","N/A","Usa historial de México vía Círculo de Crédito","Confirmar","Confirmar","N/A","Nacional (con emisores aliados)","Trae historial de México","Solo con emisores aliados","https://www.novacredit.com/")
add(K,"Zolve Classic (tarjeta)","$0","Tarjeta de crédito","Pasaporte + visa","No requiere SSN","N/A","Nacional","Sin historial en EE. UU.","Enfoque en personas con visa","https://zolve.com/")

T = "Tarjeta prepagada"
add(T,"Walmart MoneyCard","$5.94","Exento con $500 en depósito directo; recarga $3 (gratis por app en Walmart)","ID extranjera aceptada","SSN, TIN o ID extranjera","Sí, en Walmart","Nacional","Acepta ID extranjera","Cuota mensual sin depósito directo","https://www.walmartmoneycard.com/")
add(T,"Netspend","$9.95 o $1.95 por compra","$5 al mes con $500 en depósito directo","Confirmar","Confirmar","Sí, con costo","Nacional","Planes a elegir","Cuotas altas","https://www.netspend.com/",P)
add(T,"Green Dot","$7.95","Exento con $500 en depósito directo; plan por uso $1.50","Confirmar","Confirmar","Sí, con costo","Nacional","Muy disponible","Cuota mensual","https://www.greendot.com/",P)

for i, r in enumerate(rows, 1): r["id"] = f"P{i:03d}"
notas = ["Desde el 1 de enero de 2026 hay un impuesto federal de 1% a remesas fondeadas con efectivo, giro o cheque de caja; si se fondean desde cuenta bancaria o tarjeta no aplica.",
 "Todos los costos cambian. Antes de usar un producto, confirma en la página oficial o en sucursal.",
 "Bank On certifica cuentas de bajo costo sin sobregiros; en CA hay 79 cuentas certificadas (joinbankon.org).",
 "El programa no recomienda productos ni recibe pagos de ellos. La matriz sirve para comparar y hacer preguntas."]
out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "entregables", "matriz", "matriz-productos.json")
json.dump({"fecha_verificacion": F, "notas": notas, "productos": rows}, open(out, "w"), ensure_ascii=False, indent=1)
from collections import Counter
print(len(rows), Counter(r["categoria"] for r in rows), Counter(r["estado"] for r in rows))
