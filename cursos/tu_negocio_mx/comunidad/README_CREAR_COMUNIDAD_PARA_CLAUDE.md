# Instrucciones para Claude: crear "Comunidad Tu Negocio" (Moodle 3.10)

Vas a crear el curso **Comunidad Tu Negocio** en academia.desarrollatalento.com. Es un espacio aparte del curso *Tu Negocio, Tu Dinero, Tu Futuro* (TNDF-MX). No toques otros cursos.

Reglas:

- Usa solo la interfaz web.
- No uses SSH.
- No instales complementos.
- No cambies la configuración del sitio.
- Si algo no coincide con estas instrucciones, detente y pregunta.

## 0. Antes de empezar

1. Confirma que no existe un curso con nombre corto `TNDF-COM`. Si existe, detente y pregunta.
2. Pregunta a la persona:
   - la fecha y el enlace de la primera sesión mensual en vivo;
   - el enlace del canal de WhatsApp;
   - si quiere inscribir a las personas con una cohorte (la crea la persona administradora del sitio) o de forma manual.
   Si no tiene esos datos, deja el texto "[por definir]" y repórtalo.

## 1. Crear el curso

| Campo | Valor |
|---|---|
| Nombre | Comunidad Tu Negocio |
| Nombre corto | TNDF-COM |
| Visibilidad | **Mostrar** |
| Inscripción | Autoinscripción con la clave que te dé la persona («[por definir]» si no la tienes) |
| Formato | Temas, 4 secciones |
| Seguimiento de finalización | No |
| Mostrar calificaciones | No |
| Resumen | "El espacio de la comunidad de Tu Negocio, Tu Dinero, Tu Futuro: dudas, avisos, fechas fiscales, alertas de fraude, presenta tu negocio, logros y sesión mensual en vivo." |

## 2. Secciones y actividades

### General · Bienvenida

1. Ya existe el foro **Avisos** (foro de noticias). Configúralo:
   - Nombre: `Avisos`.
   - Descripción: "Fechas fiscales, recordatorios, alertas de fraude, retos del mes y sesión mensual. Solo publica el equipo. Desarrolla Talento nunca te pide tu RFC, contraseñas, e.firma ni números de cuenta."
   - Suscripción: forzosa.
2. **Libro** `Guía de la comunidad`: formato de capítulo "Nada". Menú del libro > Importar capítulo > `1_libro/Comunidad_libro_Moodle.zip`, "Cada archivo HTML representa un capítulo" (6 capítulos).
3. **URL** `Canal de avisos en WhatsApp`: enlace que te dé la persona; abrir en ventana nueva. Descripción: "Solo publica el equipo; nadie ve tu número. Las dudas se resuelven en los foros."

### Sección 1 · Participa

Crea estos foros. En **todos**:

- Número máximo de archivos adjuntos: **0**.
- Tamaño máximo de archivo adjunto: no se permite subir archivos.
- Calificación: ninguna. Evaluaciones (ratings): desactivadas.
- Modo de grupo: sin grupos.
- Suscripción: opcional.
- Copia la advertencia al inicio de cada descripción: "No publiques RFC, CURP, contraseñas del SAT, e.firma, números de cuenta, montos reales ni capturas de tu banco, del SAT o de tus facturas."

| Nombre | Tipo de foro | Descripción (después de la advertencia) |
|---|---|---|
| Lo que quiero lograr | Foro para uso general | "En una frase, qué quieres lograr este año. Sin nombre completo, datos personales ni montos reales." |
| Dudas: dinero, precio, flujo y cobros | Foro estándar que aparece en un formato similar a un blog | "Módulos 1 a 4. Usa la plantilla del capítulo 3 de la guía." |
| Dudas: SAT y formalidad | Foro estándar que aparece en un formato similar a un blog | "Módulo 5. Orientación general; tu caso lo revisas con el SAT o un contador. Usa la plantilla del capítulo 3." |
| Dudas: crédito, protección, crecer y futuro | Foro estándar que aparece en un formato similar a un blog | "Módulos 6 a 9. Usa la plantilla del capítulo 3 de la guía." |
| Presenta tu negocio | Foro para uso general | "Una publicación al mes por persona, con la plantilla del capítulo 3. Sin préstamos, inversiones, tandas ni facturas." |
| Alertas de fraude | Foro para uso general | "Avisa de llamadas «del SAT», proveedores falsos, capturas falsas o extorsiones, sin datos personales. Si ya te afectó, sigue M4 U03 y M7 U03." |
| Logros | Foro para uso general | "Comparte tus avances y los retos del mes que cumpliste." |

Si en tu versión de Moodle el tipo "similar a un blog" no aparece con ese nombre, usa "Foro para uso general" y repórtalo.

### Sección 2 · Sesión mensual en vivo

1. **Página** `Sesión mensual en vivo`: copia el contenido del capítulo 5 (primera parte) y agrega la fecha y el enlace que te dio la persona.
2. **Consulta** (Choice) `¿Qué tema quieres en la próxima sesión?`:
   - Opciones: "Precio y costos", "Flujo y fiado", "Cobros y fraudes al vender", "RFC y RESICO", "Facturas e IVA", "Crédito", "IMSS Modalidad 10 y seguros", "Vender en línea", "Retiro".
   - Permitir actualizar la respuesta: sí. Mostrar resultados: después de responder. Privacidad: publicar resultados anónimos.
3. **Encuesta** (Feedback) `Encuesta de la comunidad`, anónima, con estas preguntas:
   - Opción múltiple: "¿Qué tan útil te resulta la comunidad?" (Muy útil / Útil / Poco útil / Nada útil).
   - Opción múltiple: "¿Qué espacio usas más?" (Avisos / Foros de dudas / Presenta tu negocio / Alertas / Logros / Sesión mensual / Canal de WhatsApp).
   - Texto largo: "¿Qué tema te gustaría que agregáramos al curso?"
   - Texto largo: "¿Qué mejorarías de la comunidad?"

### Sección 3 · Referencias comerciales

1. **Etiqueta** con este texto: "Referencias comerciales. Aquí publicamos servicios con acuerdo comercial. Desarrolla Talento puede recibir una comisión. Usarlos es voluntario y no afecta tu acceso, tus puntos ni tu constancia. Compara siempre con al menos otra opción (capítulo 6 de la guía)."
2. **Foro** `Referencias comerciales`, tipo "Foro de noticias" o, si no se puede agregar otro, "Foro para uso general" con esta restricción: en *Permisos* del foro, quita a Estudiante la capacidad `mod/forum:startdiscussion` y `mod/forum:replypost`. Si no puedes cambiar permisos, detente y pregunta.

## 3. Enlazar desde el curso principal

En el curso **TNDF-MX**, sección General, agrega una **URL** `Comunidad Tu Negocio` al curso nuevo, con la descripción: "Dudas, fechas fiscales, alertas de fraude, presenta tu negocio y sesión mensual."

## 4. Inscripción

- Si la persona creó la cohorte "Tu Negocio MX": en ambos cursos, *Participantes > Métodos de inscripción > Agregar método > Sincronización de cohortes*, cohorte "Tu Negocio MX", rol Estudiante.
- Si no: activa la **Autoinscripción** con la clave que te dé la persona («[por definir]» si no la tienes) y repórtalo.
- Agrega al equipo de moderación con rol **Profesor sin permiso de edición** (o Profesor, si lo pide la persona).

## 5. Revisión (con rol de estudiante)

- No se pueden adjuntar archivos en los foros.
- El estudiante puede publicar en Lo que quiero lograr, Dudas, Presenta tu negocio, Alertas y Logros.
- El estudiante no puede publicar en Avisos ni en Referencias comerciales.
- El libro muestra 6 capítulos.
- La consulta y la encuesta funcionan.

## 6. Reporte

Enlace del curso; lista de foros con su configuración; estado de la consulta y la encuesta; método de inscripción; lo que quedó "[por definir]"; capturas de la página principal del curso y de un foro con la advertencia.

El curso queda **visible**, con inscripción por clave.
