# Prompts para construir la app de complementos

Cómo usar este documento:

1. Pega siempre el **Bloque 0 (contexto común)** al inicio de cualquier conversación con la herramienta de IA o con el equipo de desarrollo.
2. Después pega el bloque que corresponda: **1 back end**, **2 front end**, **3 panel de administración**, **4 integraciones** o **5 un módulo específico**.
3. Construye por fases: primero el MVP (C01 a C05), luego la fase 2 y después la fase 3.

Los identificadores C01 a C13 corresponden a la lista de complementos del plan maestro.

---

## Bloque 0. Contexto común (pegar siempre)

```
Eres un equipo senior de producto e ingeniería. Vas a construir "Tu Dinero" (nombre de trabajo), la app gratuita que acompaña al programa de educación financiera "Tu Dinero, Tu Familia, Tu Futuro" para migrantes en Estados Unidos. El piloto es California; después Texas, Illinois, Nueva York y Florida.

Usuarios
- Adultos migrantes, principalmente hispanohablantes, con SSN, ITIN, matrícula consular o sin documento fiscal.
- Muchos usan un Android de gama media o baja, con datos limitados, y aprenden por WhatsApp.
- Niveles de lectura diversos; tiempo escaso; desconfianza justificada hacia apps que piden datos.

Principios no negociables
1. La app NUNCA recibe, guarda ni transfiere dinero. Solo registra, calcula y recuerda. (Así evitamos licencias de transmisor de dinero.)
2. No pedimos ni guardamos: SSN, ITIN, número de pasaporte, estatus migratorio, contraseñas bancarias, números completos de cuenta ni datos de tarjetas.
3. Local primero: todo funciona sin crear cuenta y sin conexión. La sincronización en la nube es opcional y la persona la activa.
4. No conectamos cuentas bancarias en MVP ni en fase 2.
5. Nada de asesoría personalizada legal, fiscal, migratoria ni de inversión. Mostramos cálculos con los datos que la persona escribe, explicamos supuestos y dirigimos a ayuda verificada.
6. Cada cifra externa (tipo de cambio, comisión, requisito) muestra su fuente y fecha de verificación. Si una ficha está vencida, se etiqueta "por confirmar".
7. Idiomas: español (predeterminado) e inglés, con archivos de traducción separados. Preparar la estructura para agregar otros idiomas y audio.
8. Accesibilidad WCAG 2.1 AA: contraste, tamaño de toque mínimo 44 px, lector de pantalla, textos cortos y claros.
9. Sin culpa: los mensajes nunca juzgan. "Esta semana falta dinero" en lugar de "gastaste de más".
10. Gratis de verdad: sin anuncios, sin venta de datos, sin compras dentro de la app, sin pedir reseñas como condición.

Estilo de redacción de la interfaz
- Frases de 15 palabras o menos. Verbos claros. Tú, no usted.
- Términos técnicos con explicación en la misma pantalla: "Saldo disponible (lo que el banco te deja usar hoy)".
- Botones que dicen exactamente qué pasa: "Guardar pago", "Comparar envíos".

Relación con el curso
- La plataforma de cursos es Moodle. La app enlaza a lecciones y recibe, con permiso, el avance y las insignias (Open Badges).
- Cada pantalla tiene un enlace "Aprende más" a la lección del curso que corresponde.
```

---

## Bloque 1. Back end

```
Construye el back end de "Tu Dinero" siguiendo el Bloque 0.

Stack
- Supabase: Postgres, Auth, Storage y Edge Functions (TypeScript/Deno).
- Row Level Security (RLS) en TODAS las tablas con datos de usuario: cada persona solo lee y escribe lo suyo.
- Migraciones SQL versionadas en /supabase/migrations. Semillas de datos en /supabase/seed.
- Pruebas: pgTAP para políticas RLS y Vitest para Edge Functions.

Autenticación
- La app funciona sin cuenta (modo local). La cuenta solo sirve para respaldar y sincronizar.
- Métodos: enlace mágico por correo y código por SMS o WhatsApp (OTP). Sin contraseñas.
- Perfil mínimo: id, idioma, estado (CA, TX, IL, NY, FL), fecha de alta, consentimientos. Nada más.

Modelo de datos (tablas principales)
- profiles(id, locale, state_code, created_at, consent_sync bool, consent_followup bool, consent_whatsapp bool, consent_version)
- cash_events(id, user_id, type[income|expense|debt|remittance|tax|reserve], label, amount_cents, currency, date, recurrence[none|weekly|biweekly|semimonthly|monthly|custom], certainty[confirmed|estimated], notes, created_at, updated_at)
- goals(id, user_id, name, target_amount_cents, currency, target_date, starting_allocated_cents, priority, status, created_at)
- goal_contributions(id, goal_id, amount_cents, currency, date)
- remittance_quotes(id, user_id, provider_id, send_amount_cents, fee_cents, fx_rate, tax_cents, receive_amount_minor, receive_currency, delivery_time, pickup_cost_minor, quoted_at, source[manual|matrix])
- family_agreements(id, user_id, purpose, min_amount_cents, max_amount_cents, currency, schedule, emergency_rule, verification_rule, review_trigger, share_token, updated_at)
- debts(id, user_id, creditor_label, type, balance_cents, apr_bp, min_payment_cents, due_day, collateral, status)
- tanda_groups(id, user_id, name, contribution_cents, frequency, members_count, my_turn, start_date) y tanda_turns(id, group_id, turn_number, date, paid bool, received bool)
- wellbeing_scores(id, user_id, instrument_version, score, taken_at)
- scam_reports_public(id, title_es, title_en, pattern, what_to_do_es, what_to_do_en, source_url, verified_at, active) — solo lectura para usuarios, escritura por admin.
- products(id, category[account|remittance|credit_builder|card|insurance|retirement], brand, legal_entity, regulator, state_codes[], accepts_itin, accepts_matricula, requires_ssn, cash_deposit, monthly_fee_cents, fee_waiver_rules jsonb, other_fees jsonb, apr_bp, apy_bp, fx_margin_note, languages[], source_url, verified_at, verified_by, review_due, notes_es, notes_en, status[active|pending|retired])
- help_directory(id, name, service_type, counties[], state_code, modality, languages[], credential_verified, cost_note, free_option bool, contact_url, verified_at, review_due)
- fx_reference(id, pair, rate, source, fetched_at)
- audit_log(id, actor, table_name, record_id, action, diff jsonb, created_at) — para cambios de admin.

Reglas de datos
- Montos en centavos (enteros). Tipo de cambio con 6 decimales. Moneda ISO 4217.
- La carpeta de continuidad (C08) NO se guarda en el servidor en texto plano: se cifra en el dispositivo (clave derivada de un PIN del usuario) y el servidor solo guarda el blob cifrado si la persona activa el respaldo.
- Borrado total: endpoint que elimina todos los datos de la persona en menos de 24 horas y deja registro anónimo del borrado.
- Retención: datos de seguimiento hasta 12 meses después del día 180; luego anonimizar.

Edge Functions
1. /fx-reference: obtiene diariamente el tipo de cambio de referencia USD/MXN de una fuente oficial pública (configurable) y lo guarda con fecha y fuente. Si falla, conserva el último valor y lo marca "desactualizado".
2. /remittance-calc: recibe presupuesto total o monto a recibir, comisión, tipo de cambio, impuesto aplicable y costo de cobro; devuelve monto recibido, costo total, costo efectivo en % y diferencia contra la referencia. Documentar fórmulas. Redondeo explícito.
3. /cashflow-project: recibe eventos y saldo inicial; devuelve saldos diarios y semanales de 8 semanas, primera fecha negativa y faltante máximo. Maneja cobros semanales, cada dos semanas, dos veces al mes, mensuales y variables.
4. /product-compare: dado un perfil de uso (cómo cobra, depósitos en efectivo al mes, uso de cajeros, documentos que tiene), devuelve el costo mensual estimado por producto y los requisitos que faltan confirmar. Nunca ordena por pago comercial.
5. /share-agreement: genera un enlace de solo lectura, con vencimiento, para compartir el acuerdo familiar.
6. /whatsapp-webhook: recibe y envía mensajes vía WhatsApp Business Cloud API solo a quien dio consentimiento; comandos "BAJA" y "AYUDA".
7. /moodle-sync: con permiso de la persona, recibe avance e insignias desde Moodle (Web Services o LTI 1.3).
8. /export: exporta los datos de la persona en JSON y CSV.

Seguridad
- RLS probado con pruebas automáticas (un usuario no puede leer datos de otro).
- Límite de peticiones por IP y por usuario. Registros sin datos personales.
- Secretos solo en variables de entorno. Nada de claves en el cliente.
- Copias de seguridad diarias y prueba de restauración mensual.

Entregables
- Migraciones, políticas RLS, funciones, pruebas y un README con cómo levantar el entorno local.
- Documento de fórmulas (remesa, flujo, costo de cuenta) con 5 casos de prueba cada una. Usa como casos de prueba los ejemplos del manual: E1 (Alex y Mar), E2 (remesas A, B y C) y M3 U05.
```

---

## Bloque 2. Front end

```
Construye el front end de "Tu Dinero" siguiendo el Bloque 0 y conectado al back end del Bloque 1.

Stack
- Next.js (App Router) + TypeScript + Tailwind CSS, instalable como PWA.
- Local primero: IndexedDB (Dexie) como almacén principal; sincronización opcional con Supabase.
- Service worker para uso sin conexión y bajo consumo de datos.
- i18n con next-intl: /messages/es.json y /messages/en.json, sin textos fijos en el código.
- Gráficas ligeras (SVG propio o una librería pequeña); peso inicial de la app menor a 200 KB comprimido.
- Pruebas: Playwright (flujos) y Vitest (lógica). Revisión automática de accesibilidad con axe.

Navegación (barra inferior, 5 pestañas)
1. Inicio: "Tu semana" (saldo proyectado, próximo pago, alerta si hay faltante), misión activa del curso y acceso rápido a "¿Es estafa?".
2. Dinero: calendario (C01) y metas (C03).
3. Familia: remesa real (C02) y acuerdo familiar (C05).
4. Protección: ¿Es estafa? (C04), carpeta de continuidad (C08) y mapa de ayuda (C10).
5. Aprende: avance del curso, insignias y lecciones recomendadas.

Pantallas del MVP
- Bienvenida sin registro: idioma, estado donde vive y qué quiere lograr primero (3 opciones). Explica en 2 frases qué datos NO pedimos.
- C01 Calendario: agregar ingresos y pagos con frecuencia y certeza; vista semanal de 8 semanas con saldo inicial, entradas, salidas y saldo final; la primera semana negativa se marca con color y texto ("Faltan $420 el miércoles 3"). Botón "Ver opciones" que enlaza a la lección M1 U07.
- C02 Remesa real: dos modos ("Tengo X dólares" o "Mi familia necesita X pesos"); hasta 3 cotizaciones lado a lado; muestra monto que llega, costo total, % de costo, fecha de entrega y costo de cobro. Etiqueta de fecha de la referencia de tipo de cambio.
- C03 Metas: nombre, monto, moneda, fecha, dinero ya destinado; calcula aportación mensual; alerta si la suma de aportaciones supera el margen del calendario ("Estas metas piden $150 al mes y tu margen es $80").
- C04 ¿Es estafa?: 6 preguntas de sí o no (¿te piden actuar ya?, ¿piden secreto?, ¿piden código o contraseña?, ¿pagan primero para recibir?, ¿el contacto llegó por un número nuevo?, ¿dicen ser gobierno o banco?). Resultado con acción inmediata, dónde verificar y dónde reportar. Lista de alertas actuales.
- C05 Acuerdo familiar: formulario de 6 campos (propósito, rango, fecha, emergencia, verificación, revisión); vista para compartir por WhatsApp como imagen o enlace de solo lectura.
- Ajustes: idioma, estado, respaldo en la nube (opcional), exportar, borrar todo, avisos por WhatsApp (opcional).

Gamificación
- Misiones semanales ligadas a acciones reales (ej. "Registra tus pagos de 2 semanas", "Compara 2 envíos").
- Racha semanal (no diaria, para no presionar). Insignias sincronizadas con Moodle.
- Nunca premiar montos de dinero, compras ni contrataciones.

Diseño
- Tipografía grande (base 17 px), alto contraste, iconos con texto.
- Montos en formato local ($1,250.00 / MX$21,300.00) y números tabulares.
- Estados vacíos con ejemplos marcados como "Ejemplo" y botón para empezar con datos propios.
- Modo claro y oscuro.

Criterios de aceptación del MVP
- Funciona sin conexión después de la primera carga.
- Todo el flujo de C01 a C05 se completa sin crear cuenta.
- Los cálculos coinciden con los casos de prueba del manual (E1, E2).
- Lighthouse: Rendimiento ≥ 90 en un Android de gama media simulado; Accesibilidad ≥ 95.
- Ninguna pantalla pide SSN, ITIN, estatus migratorio ni contraseñas.
```

---

## Bloque 3. Panel de administración (matriz viva y directorio)

```
Construye un panel de administración web para el equipo editorial, siguiendo el Bloque 0.

Funciones
- CRUD de products, help_directory y scam_reports_public.
- Cada ficha exige: fuente (URL), fecha de verificación, persona que verificó y fecha de próxima revisión.
- Estados: activo, pendiente, retirado. Una ficha con review_due vencido pasa sola a "pendiente" y la app la muestra como "por confirmar".
- Tablero: fichas por vencer en 15 días, fichas vencidas, cambios de la semana.
- Historial de cambios (audit_log) con quién cambió qué y cuándo.
- Roles: editor (propone), revisor (aprueba), admin. Nada se publica sin aprobación del revisor.
- Exportar la matriz en CSV para el manual del curso y para Moodle.
- Campo "relación comercial" obligatorio (ninguna, referido, patrocinio). Si no es "ninguna", la app lo muestra. El orden de resultados nunca depende de este campo.

Stack sugerido: Next.js con autenticación de Supabase y roles por RLS, o Directus conectado a la misma base de datos.
```

---

## Bloque 4. Integraciones

```
Integra "Tu Dinero" con los servicios externos, siguiendo el Bloque 0.

Moodle
- Opción A: LTI 1.3 para abrir la app desde el curso con inicio de sesión único.
- Opción B: Moodle Web Services para leer avance e insignias (con permiso).
- Las misiones de la app pueden marcar actividades como completadas en Moodle.

WhatsApp Business Cloud API
- Plantillas aprobadas: recordatorio de pago, reto semanal, alerta de fraude nueva, recordatorio de revisión a 30/90/180 días.
- Doble consentimiento y comando BAJA. Máximo 2 mensajes por semana salvo alertas de fraude.

Tipo de cambio de referencia
- Fuente oficial pública configurable; guardar fecha, hora y fuente. Nunca presentarlo como la tasa que ofrecerá un proveedor.

Analítica
- PostHog o Plausible con hospedaje propio, sin datos personales ni montos. Eventos: pantalla vista, cálculo realizado, misión completada.
```

---

## Bloque 5. Módulos de fase 2 y fase 3 (pegar uno a la vez)

### C06 Ruta de crédito
```
Agrega el módulo "Ruta de crédito". Primero un diagnóstico de 5 preguntas que asigna una ruta: sin historial, error en el reporte, atraso o cobranza, saldos altos, o situación estable. Cada ruta muestra 3 acciones con fecha y recordatorio. Incluye:
- Inventario de deudas (tabla debts) con total de pagos mínimos contra el margen del calendario.
- Simulador que compara "tasa más alta primero" y "saldo más pequeño primero" con los mismos recursos, y muestra meses e intereses estimados. Aclara que es una simulación.
- Calculadora de utilización (saldo ÷ límite) sin prometer puntos.
Nunca consulta el buró ni pide datos del reporte completo.
```

### C07 Tandas y círculos
```
Agrega el módulo "Tandas". Registrar grupo, aportación, frecuencia, número de integrantes, mi turno y fechas. Calendario de pagos y del turno en que recibo. Las aportaciones aparecen automáticamente en el calendario (C01). Pantalla informativa que explica la diferencia entre una tanda informal y un círculo de préstamo que reporta a buró, con enlace al directorio. La app no cobra, no recibe ni reparte dinero.
```

### C08 Carpeta de continuidad
```
Agrega "Carpeta de continuidad": índice de documentos (qué es, dónde está guardado físicamente, quién sabe dónde está), contactos de emergencia, instrucciones de cuidado de hijos y lista de cuentas sin números completos. Cifrado en el dispositivo con PIN (AES-GCM, clave derivada con PBKDF2 o Argon2). Respaldo opcional del archivo cifrado. Plantilla de "plan de preparación familiar" con enlace a organizaciones de ayuda legal verificadas. Aviso claro: "Esto es un índice para tu familia. No sustituye documentos legales."
```

### C09 Calendario fiscal
```
Agrega "Calendario fiscal": fechas del año (configurables por el admin), lista de documentos según tipo de ingreso (salario, trabajo independiente, mixto), localizador de ayuda gratuita (VITA) desde el directorio y una verificación orientativa de créditos estatales con ITIN (ej. CalEITC en California). Mensaje fijo: "Esto te prepara para tu cita; no calcula tu impuesto."
```

### C10 Mapa de ayuda
```
Agrega "Mapa de ayuda" desde help_directory: filtros por tipo de ayuda, idioma, costo y condado. Lista primero (más ligera) y mapa opcional. Cada ficha muestra fecha de verificación y el guion para pedir información.
```

### C11 Tutor en español
```
Agrega un tutor conversacional que responde SOLO con base en el contenido del curso (búsqueda en los textos de las lecciones y el glosario). Usa la API de Claude de Anthropic con el modelo vigente, con estas reglas en el prompt del sistema:
- Explica conceptos con ejemplos cortos y cita la lección de origen.
- Si la pregunta es legal, fiscal, migratoria o de inversión personalizada, no responde el fondo: explica el concepto general y dirige al directorio de ayuda.
- Si detecta fraude en curso o emergencia, muestra primero el protocolo de respuesta.
- No pide ni guarda datos sensibles; si el usuario los escribe, recomienda borrarlos.
Registra solo métricas anónimas de uso.
```

### C12 Termómetro de bienestar
```
Agrega la escala de bienestar financiero del CFPB (versión oficial en español e inglés, con su método de puntuación oficial). Se ofrece al inicio y a los 90 y 180 días. La persona ve su propio avance; el programa solo recibe datos agregados y anónimos, con consentimiento.
```

### C13 Comparador de cuentas para mi uso
```
Agrega "¿Qué cuenta me conviene?": perfil de uso (cómo cobro, depósitos en efectivo al mes, retiros en cajero, documentos que tengo), y con /product-compare muestra el costo mensual estimado de cada cuenta de la matriz, requisitos que faltan confirmar y fecha de verificación. Orden por costo para ese perfil. Etiqueta visible de relación comercial cuando exista.
```
