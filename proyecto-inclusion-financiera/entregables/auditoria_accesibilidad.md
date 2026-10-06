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
| Back Home, Your Money, Your Future | 24 | 80.4 (fácil) | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 127 |
| Tu Autonomía, Tu Dinero, Tu Futuro | 24 | 79.0 (bastante fácil) | 0 | 0 | 0 | 0 | 0 | 0 | 7 | 100 |
| Tu Comunidad, Tu Dinero, Tu Futuro | 14 | 81.5 (muy fácil) | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 107 |
| Tu Costa, Tu Dinero, Tu Futuro | 16 | 80.6 (muy fácil) | 0 | 0 | 0 | 0 | 0 | 0 | 12 | 109 |
| Tu Dinero, Tu Familia, Tu Futuro | 63 | 75.0 (bastante fácil) | 0 | 15 | 5 | 0 | 0 | 0 | 0 | 252 |
| Tu Idea, Tu Dinero, Tu Futuro | 37 | 78.2 (bastante fácil) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 125 |
| Tu Negocio, Tu Dinero, Tu Futuro | 46 | 78.8 (bastante fácil) | 0 | 1 | 6 | 0 | 0 | 0 | 6 | 124 |
| Tu Negocio, Tu Dinero, Tu Futuro · EE. UU. | 45 | 76.9 (bastante fácil) | 0 | 2 | 5 | 1 | 0 | 0 | 15 | 141 |
| Tu Patrimonio, Tu Tranquilidad, Tu Futuro | 66 | 75.2 (bastante fácil) | 0 | 1 | 3 | 1 | 0 | 0 | 8 | 134 |
| Tu Pensión, Tu Tranquilidad, Tu Futuro | 16 | 83.4 (muy fácil) | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 110 |
| Tu Regreso, Tu Dinero, Tu Futuro | 24 | 80.5 (muy fácil) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 116 |
| Tu Ruta, Tu Dinero, Tu Futuro | 24 | 82.3 (muy fácil) | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 98 |
| Tu Talento, Tu Marca, Tu Futuro | 82 | 74.6 (bastante fácil) | 0 | 3 | 9 | 0 | 0 | 0 | 3 | 139 |
| Tu Temporada, Tu Dinero, Tu Futuro | 24 | 78.7 (bastante fácil) | 0 | 1 | 1 | 0 | 0 | 0 | 21 | 110 |
| Tu Trabajo, Tu Familia, Tu Futuro | 45 | 82.2 (muy fácil) | 0 | 1 | 3 | 0 | 0 | 0 | 0 | 130 |
| Tu Turno, Tu Dinero, Tu Futuro | 44 | 80.6 (muy fácil) | 0 | 2 | 1 | 0 | 0 | 0 | 3 | 114 |
| Your Business, Your Money, Your Future · U.S. | 45 | 74.5 (fácil) | 1 | 0 | 4 | 0 | 0 | 0 | 17 | 145 |
| Your Money, Your Family, Your Future | 63 | 77.9 (fácil) | 1 | 17 | 5 | 0 | 0 | 0 | 5 | 264 |

**Total:** 2 de 702 lecciones quedan en «algo difícil» o más difícil; 44 frases largas; 42 párrafos largos; 2 lecciones con siglas sin explicar; 0 direcciones sueltas en la lectura; 0 enlaces genéricos; 109 recursos sin «Qué buscar».

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
| tu_talento | M11 U04 | Plan Personal de Retiro (PPR) y aportaciones deducibles | 75.8 (bastante fácil) | 2 | 1 | — | Si retiras antes de los 65 años (salvo invalidez o incapacidad), te retienen 20% y el retiro se suma a tus ingresos (artículos 142, fracción XVIII, y 151, fracción V, de la LISR). |
| tu_dinero_es | M1 U07 | ¿Por qué me falta dinero si este mes gano suficiente? | 76.7 (bastante fácil) | 2 | 0 | — | una hoja de papel con 8 columnas, una por semana; el calendario de tu teléfono, con alertas en cada fecha de pago; las alertas de saldo bajo de la app de tu banco. |
| your_money_en | M1 U07 | Why am I short on money if I earn enough this month? | 80.2 (fácil) | 2 | 0 | — | set aside money from the previous paycheck; ask to change a payment date and confirm whether there are fees; agree on a partial payment; move an expense that can wait. |
| tu_dinero_es | M4 U10 | ¿Qué pasa con mi familia y mi dinero si no puedo estar? | 63.4 (normal) | 1 | 1 | — | UU., considera tramitar su pasaporte estadounidense y su registro de doble nacionalidad en el consulado; tarjetas de seguro médico, recetas y datos de salud; contrato de renta, títulos de vehículos, pólizas; si tienes un caso migratorio, el |
| tu_negocio_us_es | M6 U02 | Opciones de crédito y cómo verificarlas | 72.0 (bastante fácil) | 1 | 1 | — | Dato vigente: el programa de micropréstamos de la SBA ofrece préstamos de hasta $50,000 a través de organizaciones sin fines de lucro, que suelen dar también asesoría. |
| tu_negocio_us_es | M9 U04 | Si faltas: cuentas con beneficiario, tu casa, lo digital y los impuestos | 71.1 (bastante fácil) | 1 | 1 | — | Si tienes casa o terreno en México y quieres pasarlos a tus hijos en vida sin dejar de usarlos, allá existe la donación con reserva de usufructo. |
| tu_temporada | M2 U01 | No te endeudes para irte | 82.1 (muy fácil) | 1 | 1 | — | Son los trámites y el traslado a la ciudad donde se hacen, la cuota de la visa en la H-2A (que te reembolsan) y tus primeros gastos personales. |
| tu_trabajo_hogar | M6 U02 | IMSS por tu cuenta: inscríbete tú y paga tu cuota | 78.6 (bastante fácil) | 1 | 1 | — | Consultado el 30 de septiembre de 2026 a través de medios nacionales que citan las tablas del IMSS; confirma en tu clínica o en el IMSS antes de pagar. |
| tu_dinero_es | M3 U08 | ¿Firmar para ayudar puede dejarme una deuda? | 80.5 (muy fácil) | 0 | 2 | — |  |
| tu_negocio_mx | M9 U04 | Si faltas: tu casa, tus socios, lo digital y los impuestos de la herencia | 81.7 (muy fácil) | 0 | 2 | — |  |
| tu_negocio_us_es | M5 U05 | El impuesto sobre ventas (sales tax) | 76.9 (bastante fácil) | 0 | 0 | CDTFA |  |
| tu_patrimonio | M4 U03 | Mensajes y correos falsos | 77.4 (bastante fácil) | 0 | 0 | BANCO |  |
| tu_patrimonio | M7 U05 | Si tú o tu pareja trabajaron para el gobierno: ISSSTE | 72.0 (bastante fácil) | 0 | 2 | — |  |
| your_money_en | M3 U08 | Can signing to help someone leave me with a debt? | 82.7 (fácil) | 0 | 2 | — |  |
| back_home_en | M1 U01 | Your repatriation record and your CURP: the first two papers | 72.6 (fácil) | 1 | 0 | — | If you were sent back from the United States, the National Migration Institute (INM) gave you a Record of Reception of Repatriated Mexicans (Constancia de Recepción de Mexicanos Repatriados). |
| tu_dinero_es | M1 U01 | ¿Todo el dinero que recibo es dinero que gané? | 76.4 (bastante fácil) | 1 | 0 | — | viene de una app de adelantos de nómina o de tu patrón "a cuenta" de tu salario; alguien te dice que te lo prestó o que te lo "depositó por error"; es una transferencia desde otra cuenta tuya; en tu estado de cuenta dice refund, reversal o  |
| tu_dinero_es | M1 U03 | ¿Qué necesito cuidar primero? | 75.7 (bastante fácil) | 1 | 0 | — | cada adulto tiene una pequeña cantidad para uso personal, sin tener que explicar en qué la usa; las compras grandes se deciden juntos; nadie firma deudas a nombre de otro sin su permiso. |
| tu_dinero_es | M1 U06 | ¿Una compra pequeña puede sumar mucho? | 77.9 (bastante fácil) | 1 | 0 | — | cajeros de otro banco, que pueden cobrar dos veces: tu banco y el dueño del cajero; cuota mensual de la cuenta si no cumples un saldo mínimo; cargos por sobregiro. |
| tu_dinero_es | M1 U10 | ¿Todo lo que cobro por mi cuenta es para gastar? | 72.2 (bastante fácil) | 1 | 0 | — | una licencia de negocio de tu ciudad; un permiso de vendedor si vendes productos, por ejemplo comida; un número de identificación del empleador (EIN) si contratas a alguien. |
| tu_dinero_es | M1 U12 | ¿Cómo elijo a alguien que me ayude con impuestos? | 75.9 (bastante fácil) | 1 | 0 | — | promete "el máximo reembolso garantizado" antes de ver tus papeles; te pide firmar hojas en blanco; quiere que el reembolso llegue a su cuenta y no a la tuya; te sugiere inventar gastos o dependientes; no firma la declaración como preparado |
| tu_dinero_es | M2 U08 | ¿Sin comisión siempre llega más dinero? | 78.6 (bastante fácil) | 1 | 0 | — | evitas el impuesto de 1% por efectivo; muchas veces pagas menos comisión; tu familia recibe los pesos en su cuenta y no tiene que cargar efectivo en la calle. |
| tu_dinero_es | M2 U09 | ¿Qué reviso antes de enviar y qué hago si algo falla? | 75.2 (bastante fácil) | 1 | 0 | — | la fecha en que el dinero estará disponible; el monto enviado, las comisiones y los impuestos; el tipo de cambio; el monto que recibirá tu familia; tus derechos para cancelar y reclamar, y a quién contactar. |
| tu_dinero_es | M2 U11 | ¿Cómo digo cuánto puedo ayudar sin prometer de más? | 78.8 (bastante fácil) | 1 | 0 | — | ten un contacto de confianza para confirmar, como otro familiar; haz una pregunta que solo la familia sabría, por ejemplo el nombre de una mascota de la infancia; desconfía de números nuevos, de pedidos de pago con tarjetas de regalo o crip |
| tu_dinero_es | M2 U12 | ¿Cómo ahorro para algo que se pagará en pesos? | 79.2 (bastante fácil) | 1 | 0 | — | la escritura: a nombre de quién está; el Registro Público de la Propiedad: que no tenga problemas; si se necesita un contrato o un documento ante notario que reconozca tu parte. |
| tu_dinero_es | M2 U13 | ¿Cómo junto cuenta y remesas en un solo plan? | 72.1 (bastante fácil) | 1 | 0 | — | tu ingreso baja 20% y llega una solicitud extraordinaria; tu cuenta pide un documento que no tienes; el tipo de cambio empeora; el envío tarda dos días más. |
| tu_dinero_es | M3 U10 | ¿Cuál es mi siguiente paso con el crédito? | 72.4 (bastante fácil) | 1 | 0 | — | pon pagos automáticos del mínimo y paga el resto a mano; revisa tus reportes sin costo cada pocos meses; congela tu crédito si no planeas pedir préstamos pronto (M4 U04). |
| tu_dinero_es | M4 U02 | ¿Quién puede ayudarme de verdad con un trámite migratorio? | 63.0 (normal) | 1 | 0 | — | exigen un pago inmediato para "evitar una deportación", "liberar a un familiar" o "cancelar una multa"; piden pagar con tarjetas de regalo, criptomonedas, transferencias o apps; amenazan con arrestarte si cuelgas. |
| tu_negocio_mx | M7 U06 | Fraudes con inteligencia artificial: voces, videos y mensajes falsos | 75.6 (bastante fácil) | 1 | 0 | — | Con unos segundos de audio o unas fotos de tus redes, la inteligencia artificial puede imitar la voz de un familiar, un proveedor o un cliente. |
| tu_patrimonio | M10 U09 | Violencia económica y patrimonial: tu dinero y tus bienes también son tuyos | 76.6 (bastante fácil) | 1 | 0 | — | Dato vigente: la Ley General de Acceso de las Mujeres a una Vida Libre de Violencia define la violencia patrimonial y la económica (artículo 6, fracciones III y IV). |
| tu_talento | M10 U08 | Tus regalías cuando faltes: derechos, sociedades de gestión e impuestos | 69.1 (bastante fácil) | 1 | 0 | — | Dato vigente: en México, los derechos patrimoniales de autor duran toda la vida del autor y 100 años después de su muerte (Ley Federal del Derecho de Autor, artículo 29). |
| tu_turno | M4 U03 | Tu casa: Infonavit y el crédito de 100 puntos | 75.7 (bastante fácil) | 1 | 0 | — | Pueden precalificar con 100 puntos, en lugar de 1,080, quienes ganan entre uno y dos salarios mínimos, cotizan seis meses seguidos o más y no tienen vivienda propia. |
| tu_turno | M7 U08 | Tu dinero, tu decisión: violencia económica en casa | 77.9 (bastante fácil) | 1 | 0 | — | Dato vigente: la Ley General de Acceso de las Mujeres a una Vida Libre de Violencia define la violencia patrimonial y la económica (artículo 6, fracciones III y IV). |
| your_money_en | M1 U01 | Is all the money I receive money I earned? | 85.4 (fácil) | 1 | 0 | — | it comes from a payroll advance app, or from your boss "against" your wages; someone tells you they lent it to you or "deposited it by mistake"; it's a transfer from another account of yours; your statement says refund, reversal or credit a |
| your_money_en | M1 U03 | What do I need to take care of first? | 79.9 (fácil) | 1 | 0 | — | each adult has a small amount for personal use, without having to explain what it's for; big purchases are decided together; nobody signs debts in someone else's name without their permission. |
| your_money_en | M1 U06 | Can a small purchase add up to a lot? | 82.8 (fácil) | 1 | 0 | — | another bank's ATMs, which can charge twice: your bank and the ATM owner; a monthly account fee if you don't keep a minimum balance; overdraft fees. |
| your_money_en | M1 U10 | Is everything I earn on my own for spending? | 81.5 (fácil) | 1 | 0 | — | a business license from your city; a seller's permit if you sell products, for example food; an employer identification number (EIN) if you hire someone. |
| your_money_en | M1 U12 | How do I choose someone to help me with taxes? | 76.6 (fácil) | 1 | 0 | — | promises "the maximum refund guaranteed" before seeing your papers; asks you to sign blank pages; wants the refund sent to their account instead of yours; suggests making up expenses or dependents; doesn't sign the return as the preparer. |
| your_money_en | M1 U14 | How do I turn what I learned into something I can actually do? | 83.1 (fácil) | 1 | 0 | — | did you add gross and net pay from the same wages? did you count transfers between your accounts as income? do taxes and remittances have dates? did you assign the same savings to two things? does the plan depend on one-time income? |
| your_money_en | M2 U06 | How do I support my family without deciding at the last minute? | 79.9 (fácil) | 1 | 0 | — | you pay more fees with small sends; your family receives the money at different times; you may come up short between sends if you don't plan. |
| your_money_en | M2 U08 | Does "no fee" always mean more money arrives? | 80.3 (fácil) | 1 | 0 | — | you avoid the 1% cash tax; you often pay a lower fee; your family receives the pesos in their account and doesn't have to carry cash on the street. |

## Siglas sin explicar

| Sigla | Lecciones |
|---|---|
| CDTFA | tu_negocio_us_es M5 U05 |
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
