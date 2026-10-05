# Revisión de accesibilidad y legibilidad (E06)

Versión 1 · 5 de octubre de 2026 · 702 lecciones de 18 cursos · generada con `herramientas_cursos/accesibilidad.py` (se vuelve a correr después de cada corrección).

## Cómo se mide

- **Legibilidad:** índice INFLESZ (Szigriszt-Pazos) en español y Flesch en inglés, sobre el gancho, «Lo esencial» y «Profundiza». Meta: «normal» o más fácil (INFLESZ 55 o más; Flesch 60 o más). El conteo de sílabas es automático y aproximado: sirve para comparar lecciones, no como calificación exacta.
- **Frases largas:** más de 25 palabras. **Párrafos largos:** más de 60 palabras (en el celular ocupan más de una pantalla).
- **Siglas sin explicar:** siglas de 3 letras o más que no están en «Palabras», ni en una definición emergente, ni con su nombre entre paréntesis. Se excluyen las de uso común (IMSS, INE, CURP, SAT, IRS…).
- **Enlaces:** direcciones sueltas dentro de la lectura, textos de enlace genéricos («aquí», «da clic») y recursos sin la guía «Qué buscar».
- **Contraste:** colores de los libros contra la norma WCAG 2.1 AA (4.5 a 1 en texto normal; 3 a 1 en texto grande o íconos).

## Resumen por curso

| Curso | Lecciones | Legibilidad media | Lecciones difíciles | Frases largas | Párrafos largos | Lecciones con siglas sin explicar | URL en la lectura | Enlaces genéricos | Recursos sin «Qué buscar» | Palabras de «Lo esencial» (mediana) |
|---|---|---|---|---|---|---|---|---|---|---|
| Tu Autonomía, Tu Dinero, Tu Futuro | 24 | 76.9 (bastante fácil) | 0 | 23 | 0 | 0 | 0 | 0 | 7 | 100 |
| Tu Comunidad, Tu Dinero, Tu Futuro | 14 | 79.2 (bastante fácil) | 0 | 16 | 0 | 0 | 0 | 0 | 4 | 107 |
| Tu Costa, Tu Dinero, Tu Futuro | 16 | 78.4 (bastante fácil) | 0 | 17 | 0 | 0 | 0 | 0 | 12 | 109 |
| Tu Dinero, Tu Familia, Tu Futuro | 63 | 73.7 (bastante fácil) | 0 | 154 | 39 | 0 | 0 | 0 | 0 | 252 |
| Tu Idea, Tu Dinero, Tu Futuro | 37 | 75.4 (bastante fácil) | 0 | 71 | 0 | 0 | 0 | 0 | 0 | 125 |
| Tu Negocio, Tu Dinero, Tu Futuro | 46 | 76.0 (bastante fácil) | 0 | 97 | 6 | 0 | 0 | 0 | 6 | 124 |
| Tu Negocio, Tu Dinero, Tu Futuro · EE. UU. | 45 | 74.1 (bastante fácil) | 0 | 109 | 6 | 0 | 0 | 0 | 15 | 141 |
| Tu Patrimonio, Tu Tranquilidad, Tu Futuro | 66 | 72.4 (bastante fácil) | 0 | 149 | 3 | 1 | 0 | 0 | 8 | 134 |
| Tu Pensión, Tu Tranquilidad, Tu Futuro | 16 | 81.2 (muy fácil) | 0 | 21 | 0 | 0 | 0 | 0 | 3 | 110 |
| Tu Regreso, Tu Dinero, Tu Futuro | 24 | 78.1 (bastante fácil) | 0 | 26 | 0 | 0 | 0 | 0 | 0 | 116 |
| Tu Ruta, Tu Dinero, Tu Futuro | 24 | 79.5 (bastante fácil) | 0 | 25 | 0 | 0 | 0 | 0 | 5 | 97 |
| Tu Talento, Tu Marca, Tu Futuro | 82 | 72.4 (bastante fácil) | 0 | 161 | 13 | 0 | 0 | 0 | 3 | 139 |
| Tu Temporada, Tu Dinero, Tu Futuro | 24 | 76.0 (bastante fácil) | 0 | 31 | 1 | 0 | 0 | 0 | 21 | 108 |
| Tu Trabajo, Tu Familia, Tu Futuro | 45 | 79.6 (bastante fácil) | 0 | 88 | 3 | 0 | 0 | 0 | 0 | 130 |
| Tu Turno, Tu Dinero, Tu Futuro | 44 | 77.9 (bastante fácil) | 0 | 79 | 1 | 0 | 0 | 0 | 3 | 114 |
| Your Business, Your Money, Your Future · U.S. | 45 | 71.3 (fácil) | 2 | 109 | 4 | 0 | 0 | 0 | 17 | 145 |
| Your Money, Your Family, Your Future | 63 | 75.8 (fácil) | 1 | 176 | 50 | 0 | 0 | 0 | 5 | 264 |
| Your Return, Your Money, Your Future | 24 | 77.7 (fácil) | 0 | 29 | 0 | 0 | 0 | 0 | 0 | 127 |

**Total:** 3 de 702 lecciones quedan en «algo difícil» o más difícil; 1381 frases largas; 126 párrafos largos; 1 lecciones con siglas sin explicar; 0 direcciones sueltas en la lectura; 0 enlaces genéricos; 109 recursos sin «Qué buscar».

## Contraste de colores (WCAG 2.1 AA)

| Uso | Texto | Fondo | Contraste | Mínimo | Resultado |
|---|---|---|---|---|---|
| Texto de lectura | `#0B1220` | `#FFFFFF` | 18.72 a 1 | 4.5 a 1 | Cumple |
| Texto gris (explicaciones y pies) | `#5A6478` | `#FFFFFF` | 5.95 a 1 | 4.5 a 1 | Cumple |
| Texto gris sobre fondo niebla | `#5A6478` | `#F5F7FB` | 5.55 a 1 | 4.5 a 1 | Cumple |
| Títulos azul oscuro | `#061F40` | `#FFFFFF` | 16.43 a 1 | 3 a 1 | Cumple |
| Texto blanco sobre azul (portadas, tablas) | `#FFFFFF` | `#0A3161` | 12.92 a 1 | 4.5 a 1 | Cumple |
| Texto blanco sobre magenta (recuerda, errores) | `#FFFFFF` | `#E4007C` | 4.58 a 1 | 4.5 a 1 | Cumple |
| Rosa claro sobre azul (etiquetas pequeñas) | `#FF7ABD` | `#0A3161` | 5.40 a 1 | 4.5 a 1 | Cumple |
| Rosa sobre azul (cifras grandes) | `#FF4FA8` | `#0A3161` | 4.27 a 1 | 3 a 1 | Cumple |
| Magenta sobre blanco (títulos de recuadros, enlaces) | `#E4007C` | `#FFFFFF` | 4.58 a 1 | 4.5 a 1 | Cumple |
| Magenta sobre rosa pálido (íconos y notas) | `#E4007C` | `#FFE3F1` | 3.81 a 1 | 3 a 1 | Cumple |
| Ámbar sobre fondo ámbar («Antes de actuar, verifica») | `#A35200` | `#FFF6EC` | 5.22 a 1 | 4.5 a 1 | Cumple |
| Azul oscuro sobre tinte (tarjetas «igual») | `#061F40` | `#E6ECF5` | 13.84 a 1 | 4.5 a 1 | Cumple |
| Azul sobre tinte (íconos) | `#0A3161` | `#E6ECF5` | 10.88 a 1 | 3 a 1 | Cumple |

Todos los pares cumplen.

## Lecciones prioritarias

Las 40 con más problemas juntos (legibilidad baja, frases y párrafos largos, siglas). El detalle de todas está en `auditoria_accesibilidad_detalle.csv`.

| Curso | Lección | Título | Legibilidad | Frases largas | Párrafos largos | Siglas sin explicar | Frase más larga |
|---|---|---|---|---|---|---|---|
| tu_patrimonio | M7 U05 | Si tú o tu pareja trabajaron para el gobierno: ISSSTE | 66.9 (bastante fácil) | 7 | 2 | — | Dato vigente: la pensión por viudez del ISSSTE equivale al 100% de la pensión que recibía la persona pensionada o que le habría correspondido; si la persona trabajadora falleció por causas ajenas al trabajo, necesitaba al menos 3 años de co |
| tu_negocio_mx | M9 U04 | Si faltas: tu casa, tus socios, lo digital y los impuestos de la herencia | 76.8 (bastante fácil) | 6 | 2 | — | Si quieres que tu local o tu casa pase a tus hijos pero seguir usándolo o cobrando la renta, puedes donar con reserva de usufructo ante notario: ellos quedan como dueños y tú conservas el uso hasta que fallezcas. |
| tu_negocio_us_es | M9 U04 | Si faltas: cuentas con beneficiario, tu casa, lo digital y los impuestos | 65.5 (bastante fácil) | 6 | 2 | — | Don Ramón puso a su hija como beneficiaria (POD) de sus cuentas, revisó con un abogado la escritura de traspaso al fallecer para su casa, hizo su testamento en el consulado para el terreno de Michoacán y dejó por escrito quién puede entrar  |
| your_money_en | M5 U12 | What happens if I inherit or leave something across two countries? | 61.3 (normal) | 7 | 0 | — |  Believing inheriting pays 40% / Needless fear / Only huge estates  Not reporting a foreign inheritance / Penalty up to 25% / Form 3520  Leaving the house in Mexico without a will / Court there / Notary or consulate  Paying gestores / You l |
| tu_negocio_us_es | M7 U05 | Robo de identidad y llamadas no deseadas | 68.4 (bastante fácil) | 6 | 1 | — | Dato vigente: congelar y descongelar tu crédito no tiene costo en Equifax, Experian y TransUnion (hay que pedirlo en las tres); una alerta de fraude inicial no tiene costo, dura un año y basta pedirla en una agencia; y puedes ver tus report |
| tu_talento | M3 U05 | Cómo cobro mis regalías y reviso mis pagos | 65.4 (bastante fácil) | 6 | 1 | — |  No afiliarte / Nadie cobra por ti / Afíliate  Dar tu INE a gestores / Riesgo de robo de identidad / Verifica con la sociedad  No guardar liquidaciones / No detectas errores / Guárdalas  No declarar regalías / Problemas con el SAT / Llévala |
| your_business_us_en | M7 U05 | Identity theft and unwanted calls | 67.7 (normal) | 6 | 1 | — | Current fact: freezing and unfreezing your credit costs nothing at Equifax, Experian and TransUnion (you must ask all three); an initial fraud alert costs nothing, lasts one year and you only need to ask one bureau; and you can see your rep |
| your_business_us_en | M9 U04 | If you're not there: beneficiary accounts, your home, digital access and taxes | 62.2 (normal) | 6 | 1 | — | Don Ramón named his daughter as POD beneficiary on his accounts, reviewed a transfer on death deed for his home with a lawyer, made a will at the consulate for the land in Michoacán and wrote down who can access the business accounts. |
| tu_dinero_es | M3 U08 | ¿Firmar para ayudar puede dejarme una deuda? | 78.4 (bastante fácil) | 4 | 3 | — |  Firmar porque "es solo un requisito" / Quedas obligado a pagar toda la deuda / Lee el aviso para cofirmantes y calcula si podrías pagar  Prestar sin fechas ni montos / Malentendidos y dinero que no regresa / Acuerden todo por escrito, aunq |
| tu_dinero_es | M5 U12 | ¿Qué pasa si heredo o dejo algo entre dos países? | 67.0 (bastante fácil) | 6 | 0 | — | Idea clave: en Estados Unidos, beneficiarios POD y TOD y la escritura de traspaso evitan la corte; heredar no paga impuesto federal salvo herencias enormes, pero lo heredado del extranjero de más de 100,000 dólares se reporta en el Formular |
| tu_negocio_us_es | M5 U02 | Números y permisos: EIN, ITIN y licencias | 75.5 (bastante fácil) | 6 | 0 | — | Lupita sacó su EIN sin costo en irs.gov con su ITIN, pidió su seller's permit al CDTFA sin costo y se registró como operación de comida casera en el departamento de salud de su condado. |
| tu_talento | M2 U05 | Deducciones personales y tu declaración anual | 70.4 (bastante fácil) | 6 | 0 | — |  Pagar en efectivo al médico / No se deduce / Paga con tarjeta o transferencia  No pedir factura a tu nombre / Pierdes la deducción / Da tu RFC al pagar  Poner una CLABE equivocada / Rechazan tu devolución / Revisa que la cuenta sea tuya  C |
| tu_negocio_mx | M7 U05 | Tu identidad y la de tu negocio | 81.4 (muy fácil) | 5 | 1 | — | Dato vigente: en 2026 cada línea de celular se vincula con la CURP de su titular, con plazo final el 31 de diciembre de 2026; consultar qué líneas están a tu nombre y desvincular las que no son tuyas no tiene costo en portal.crt.gob.mx. |
| tu_patrimonio | M8 U06 | Si llega un sismo o una inundación: tu patrimonio preparado | 71.2 (bastante fácil) | 5 | 1 | — | Idea clave: documentos en copia digital, fotos del antes, seguro con el riesgo de tu zona y un fondo en una cuenta; después del siniestro, reporta tú por el número oficial y no pagues por adelantado. |
| your_money_en | M1 U01 | Is all the money I receive money I earned? | 83.7 (fácil) | 5 | 1 | — |  Counting an advance or a loan as wages / You commit to expenses your job doesn't cover / Write down the loan and its due date  Counting everything you sell as profit / You run out of money to restock / Subtract your costs first  Thinking t |
| tu_dinero_es | M5 U08 | ¿Qué pasa con mi familia si algo me pasa? | 68.1 (bastante fácil) | 5 | 0 | — |  No tener nada escrito / Tu familia no sabe qué hacer / Empieza con lo básico  No actualizar beneficiarios / El dinero va a quien no quieres / Revisa cada cuenta  Dar un poder notarial a cualquiera / Pueden usar tu dinero / Solo a alguien d |
| tu_dinero_es | M5 U10 | ¿Cómo formalizo mi negocio? | 73.6 (bastante fácil) | 5 | 0 | — |  Mezclar dinero del negocio y de la casa / No sabes si ganas / Cuenta separada  No contar los costos / Crees que ganas más / Resta ingredientes y gastos  Abrir una LLC muy pronto / Pagas 800 aunque no ganes / Empieza sencillo  No apartar pa |
| tu_negocio_mx | M7 U06 | Fraudes con inteligencia artificial: voces, videos y mensajes falsos | 70.6 (bastante fácil) | 5 | 0 | — | Con unos segundos de audio o unas fotos de tus redes, la inteligencia artificial puede imitar la voz de un familiar, de un proveedor o de un cliente, crear videos falsos de famosos que «recomiendan» inversiones o escribir mensajes idénticos |
| tu_negocio_mx | M8 U07 | Adelantos y préstamos a tus empleados | 74.5 (bastante fácil) | 5 | 0 | — | Si descuentas un adelanto del sueldo, la Ley Federal del Trabajo pone límites: el descuento de cada pago no puede pasar de 30% de lo que la persona gana arriba del salario mínimo, el adelanto no puede ser mayor a un mes de sueldo y no se co |
| tu_negocio_us_es | M5 U01 | ¿Dueño único, LLC u otra forma? | 70.4 (bastante fácil) | 5 | 0 | — | Dato vigente: en California, una LLC paga un impuesto mínimo anual de $800 al Franchise Tax Board, aunque no tenga ingresos, hasta que se disuelve formalmente; también presenta una declaración de información cada dos años ante el Secretary  |
| tu_patrimonio | M5 U08 | Préstamos de nómina y a cuenta de tu pensión | 74.8 (bastante fácil) | 5 | 0 | — |  Dar tus datos por teléfono / Te roban la identidad / Verifica tú primero  Pagar para «liberar» un préstamo / Pierdes ese dinero / Nunca pagues por adelantado  Sacarlo para otra persona / La deuda es tuya / Di que no  Renovar sin comparar / |
| tu_patrimonio | M8 U07 | IMSS por tu cuenta: Seguro de Salud para la Familia y Modalidad 10 | 66.3 (bastante fácil) | 5 | 0 | — | Dato vigente: cuotas anuales del Seguro de Salud para la Familia (Modalidad 33) vigentes desde el 1 de marzo de 2026; en la Modalidad 10 se cotiza de un salario mínimo a 25 UMA y con el mínimo la cuota ronda 2,500 pesos al mes. |
| tu_patrimonio | M10 U06 | Tu casa: escrituras, predial y crédito en orden | 62.9 (normal) | 5 | 0 | — |  No inscribir la liberación / La casa sigue gravada / Notaría  Predial atrasado / Recargos / Paga a tiempo  Comprar sin revisar / Pierdes el dinero / Libertad de gravamen  Olvidar el seguro del crédito / Tu familia paga / Guárdalo |
| tu_talento | M11 U09 | Tu plan de una página | 74.5 (bastante fácil) | 5 | 0 | — |  Esperar el plan perfecto / Nunca empiezas / Una página basta  Metas sin fecha / No avanzan / Pon fecha a cada acción  No revisarlo / Se vuelve inútil / Cada tres meses  Sentir culpa si algo falla / Abandonas / Ajusta y sigue |
| tu_trabajo_hogar | M6 U01 | Cuando la casa te inscribe al IMSS | 72.0 (bastante fácil) | 5 | 0 | — |  Creer que solo es para quien trabaja de planta / Te quedas sin nada / Cada casa puede inscribirte  No saber tu NSS / Retrasas el trámite / Consúltalo con tu CURP  No preguntar / Nadie te lo ofrece / Propónlo con la página  Pagar a gestores |
| tu_turno | M6 U05 | Tu identidad y que dejen de llamarte | 77.9 (bastante fácil) | 5 | 0 | — | Dato vigente: en 2026 cada línea de celular se vincula con la CURP de su titular, con plazo final el 31 de diciembre de 2026; consultar qué líneas están a tu nombre y desvincular las que no son tuyas no tiene costo en portal.crt.gob.mx. |
| your_business_us_en | M5 U01 | Sole proprietor, LLC or something else? | 62.3 (normal) | 5 | 0 | — | Current fact: in California, an LLC pays an $800 minimum annual tax to the Franchise Tax Board, even with no income, until it is formally dissolved; it also files a Statement of Information every two years with the Secretary of State. |
| your_business_us_en | M5 U02 | Numbers and permits: EIN, ITIN and licenses | 67.1 (normal) | 5 | 0 | — |  Paying for an EIN / Unnecessary cost / irs.gov  Selling without permits / Fines or shutdown / Check with your city  Big jobs without a license / Fines and no pay / Check the CSLB  Trusting "notarios" / Fraud / Attorney or accredited organi |
| your_business_us_en | M6 U05 | Cosigner, guarantor, authorized user and reference: what are you signing? | 75.7 (fácil) | 5 | 0 | — |  Signing without reading / Someone else's debt / Read your role  Thinking the LLC always protects you / You pay with your money / Check the guarantee  Thinking a reference pays / You pay what you don't owe / It doesn't obligate you  Cosigni |
| your_money_en | M1 U14 | How do I turn what I learned into something I can actually do? | 80.1 (fácil) | 5 | 0 | — |  Writing goals without dates / They never start / Give each action a day  Choosing too many priorities / You get overwhelmed and give up / Start with three  Keeping an impossible savings amount / The plan breaks / Adjust to your real income |
| your_money_en | M2 U13 | How do I bring my account and my remittances into one plan? | 79.9 (fácil) | 5 | 0 | — |  Comparing each piece separately / One cheap piece makes the total more expensive / Look at the full path  Not reviewing after a promotion / You pay more without noticing / Review every three months  Sending everything in cash / You pay the |
| your_money_en | M3 U08 | Can signing to help someone leave me with a debt? | 78.5 (fácil) | 3 | 3 | — |  Signing because "it's just a formality" / You're obligated to pay the whole debt / Read the cosigner notice and calculate whether you could pay  Lending without dates or amounts / Misunderstandings and money that doesn't come back / Agree  |
| your_money_en | M5 U04 | Rent or buy? What rights do I have as a tenant? | 70.5 (fácil) | 5 | 0 | — |  Accepting any increase without checking / You pay more than allowed / Check whether the cap applies  Ignoring eviction papers / You can be removed without defending yourself / Get legal help right away  Comparing only rent to mortgage / Yo |
| your_money_en | M5 U10 | How do I formalize my business? | 69.0 (normal) | 5 | 0 | — |  Mixing business and household money / You don't know if you make money / A separate account  Not counting costs / You think you make more / Subtract ingredients and expenses  Opening an LLC too soon / You pay 800 even without profit / Star |
| your_money_en | M5 U11 | What's my financial plan? | 74.9 (fácil) | 5 | 0 | — |  Waiting for the perfect plan / You never start / Start with one page  Writing goals without dates / They don't move forward / Put a date on each action  Not reviewing the plan / It becomes useless / Review it every three or six months  Fee |
| tu_dinero_es | M1 U06 | ¿Una compra pequeña puede sumar mucho? | 75.9 (bastante fácil) | 4 | 1 | — |  Recortar solo los gastos pequeños / El ahorro es mínimo y te frustras / Revisa primero renta, transporte y deudas  Cancelar la tarjeta para dejar de pagar un servicio / El cobro sigue o queda una deuda / Cancela con el proveedor y guarda e |
| tu_dinero_es | M2 U02 | ¿Una app de dinero es siempre un banco? | 74.0 (bastante fácil) | 4 | 1 | — |  Creer que toda app es un banco / Tu dinero puede no estar asegurado / Busca y verifica el banco aliado  Pensar que las inversiones están aseguradas / Puedes perder dinero sin protección / Separa depósitos de inversiones  Depender solo del  |
| tu_dinero_es | M2 U12 | ¿Cómo ahorro para algo que se pagará en pesos? | 78.2 (bastante fácil) | 4 | 1 | — |  Planear la meta en dólares / No te alcanza si el dólar baja / Planea en la moneda en que se paga  Ahorrar con el tipo de cambio de hoy / Te quedas corto / Usa un escenario menos favorable  Enviar sin saber a nombre de quién queda / Pierdes |
| tu_dinero_es | M4 U08 | ¿Este documento médico me está pidiendo pagar? | 71.0 (bastante fácil) | 4 | 1 | — |  Retrasar una atención urgente por miedo al costo / Tu salud empeora / Atiéndete primero  Pagar la EOB como si fuera factura / Pagas de más / La EOB solo informa  Pagar sin pedir ayuda financiera / Pierdes descuentos a los que tienes derech |
| tu_dinero_es | M5 U01 | ¿Cómo convierto un deseo en una meta? | 76.8 (bastante fácil) | 4 | 1 | — |  Tener deseos sin números / Nunca sabes si avanzas / Ponle monto y fecha  Asignar el mismo dinero a varias metas / Crees que tienes más / Cada dólar, un destino  Confundir patrimonio con dinero disponible / No puedes pagar una emergencia /  |

## Siglas sin explicar

| Sigla | Lecciones |
|---|---|
| BANCO | tu_patrimonio M4 U03 |

## Lo que ya cumple

- Lecciones cortas por partes, con ruta rápida y completa, y la práctica al final.
- Términos difíciles con definición emergente y sección «Palabras» en cada lección.
- Recursos con institución, idioma y la guía «Qué buscar», en lugar de «da clic aquí».
- Sin imágenes con texto: todo el contenido es texto real, que leen los lectores de pantalla y se puede ampliar.
- Íconos decorativos acompañados siempre de texto.
- Diseño que se adapta al celular (probado a 390 px).

## Recomendaciones

1. **Frases largas:** partir en dos las frases de más de 25 palabras, empezando por las lecciones prioritarias. Una idea por frase.
2. **Párrafos largos:** en «Lo esencial», máximo 3 frases por párrafo; lo demás pasa a «Profundiza» o a una lista.
3. **Siglas:** la primera vez, nombre completo y sigla entre paréntesis, o una definición emergente; agregarlas a «Palabras».
4. **Contraste:** los pares marcados como «No cumple» se corrigen en la hoja de estilos de los libros (un solo cambio para todos los cursos).
5. **Moodle:** al instalar, revisar con el lector de pantalla del celular (TalkBack o VoiceOver) una lección por curso, y que los H5P se puedan responder sin ratón.
6. **Videos (cuando existan):** sin voz, así que el texto en pantalla debe durar lo suficiente para leerse (al menos 3 segundos por línea) y cada video necesita una descripción en texto debajo.
7. **Volver a correr** `python3 herramientas_cursos/accesibilidad.py` después de cada corrección y antes de cada entrega.
