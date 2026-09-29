# Instrucciones para Claude: crear "Comunidad Tu Patrimonio" (Moodle 3.10)

Vas a crear el curso **Comunidad Tu Patrimonio** en academia.desarrollatalento.com. Es un espacio aparte del curso *Tu Patrimonio, Tu Tranquilidad, Tu Futuro* (TPTF-MX). No toques otros cursos.

Reglas:

- Usa solo la interfaz web.
- No uses SSH.
- No instales complementos.
- No cambies la configuración del sitio.
- Si algo no coincide con estas instrucciones, detente y pregunta.

## 0. Antes de empezar

1. Confirma que no existe un curso con nombre corto `TPTF-COM`. Si existe, detente y pregunta.
2. Pregunta a la persona:
   - la fecha y el lugar o enlace de la primera sesión de acompañamiento;
   - el horario y el número de la línea de apoyo;
   - el enlace del canal de WhatsApp;
   - si quiere inscribir a las personas con una cohorte (la crea la persona administradora del sitio) o de forma manual.
   Si no tiene esos datos, deja el texto "[por definir]" y repórtalo.

## 1. Crear el curso

| Campo | Valor |
|---|---|
| Nombre | Comunidad Tu Patrimonio |
| Nombre corto | TPTF-COM |
| Visibilidad | **Ocultar** |
| Formato | Temas, 4 secciones |
| Seguimiento de finalización | No |
| Mostrar calificaciones | No |
| Resumen | "El espacio de la comunidad de Tu Patrimonio, Tu Tranquilidad, Tu Futuro: dudas, avisos, alertas de fraude, logros y sesiones en vivo." |

## 2. Secciones y actividades

### General · Bienvenida

1. Ya existe el foro **Avisos** (foro de noticias). Configúralo:
   - Nombre: `Avisos`.
   - Descripción: "Fechas, recordatorios, alertas de fraude, retos del mes y sesiones de acompañamiento. Solo publica el equipo. Desarrolla Talento nunca te pide datos, contraseñas ni códigos."
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
- Copia la advertencia al inicio de cada descripción: "No publiques RFC, CURP, números de cuenta, contraseñas, montos reales ni capturas de tus documentos."

| Nombre | Tipo de foro | Descripción (después de la advertencia) |
|---|---|---|
| Preséntate | Foro para uso general | "Cuéntanos quién eres, a qué te dedicas y qué quieres lograr este año." |
| Dudas: mi dinero y el sistema financiero | Foro estándar que aparece en un formato similar a un blog | "Módulos 1, 2, 5 y 6. Usa la plantilla del capítulo 3 de la guía." |
| Dudas: celular, seguridad y fraudes | Foro estándar que aparece en un formato similar a un blog | "Módulos 3 y 4. Usa la plantilla del capítulo 3 de la guía." |
| Dudas: retiro, salud, impuestos y familia | Foro estándar que aparece en un formato similar a un blog | "Módulos 7 a 11. Usa la plantilla del capítulo 3 de la guía." |
| Alertas de fraude | Foro para uso general | "Avisa de llamadas, mensajes, visitas o páginas sospechosas, sin datos personales. Si ya te afectó, sigue M4 U08." |
| Logros | Foro para uso general | "Comparte tus avances y los retos del mes que cumpliste." |

Si en tu versión de Moodle el tipo "similar a un blog" no aparece con ese nombre, usa "Foro para uso general" y repórtalo.

### Sección 2 · Sesiones de acompañamiento

1. **Página** `Sesiones de acompañamiento`: copia el contenido del capítulo 5 (primera parte) y agrega las fechas, el lugar o enlace y el horario de la línea de apoyo que te dio la persona.
2. **Consulta** (Choice) `¿Qué tema quieres en la próxima sesión?`:
   - Opciones: "El celular sin miedo", "Fraudes", "Cuentas e IPAB", "Inversiones y asesores", "Pensiones y Modalidad 40", "Seguro de gastos médicos", "Impuestos", "Testamento y beneficiarios".
   - Permitir actualizar la respuesta: sí. Mostrar resultados: después de responder. Privacidad: publicar resultados anónimos.
3. **Encuesta** (Feedback) `Encuesta de la comunidad`, anónima, con estas preguntas:
   - Opción múltiple: "¿Qué tan útil te resulta la comunidad?" (Muy útil / Útil / Poco útil / Nada útil).
   - Opción múltiple: "¿Qué espacio usas más?" (Avisos / Foros de dudas / Alertas / Logros / Sesiones / Canal de WhatsApp).
   - Texto largo: "¿Qué tema te gustaría que agregáramos al curso?"
   - Texto largo: "¿Qué mejorarías de la comunidad?"

### Sección 3 · Referencias comerciales

1. **Etiqueta** con este texto: "Referencias comerciales. Aquí publicamos servicios con acuerdo comercial. Desarrolla Talento puede recibir una comisión. Usarlos es voluntario y no afecta tu acceso, tus puntos ni tu constancia. Compara siempre con al menos otra opción (capítulo 6 de la guía)."
2. **Foro** `Referencias comerciales`, tipo "Foro de noticias" o, si no se puede agregar otro, "Foro para uso general" con esta restricción: en *Permisos* del foro, quita a Estudiante la capacidad `mod/forum:startdiscussion` y `mod/forum:replypost`. Si no puedes cambiar permisos, detente y pregunta.

## 3. Enlazar desde el curso principal

En el curso **TPTF-MX**, sección General, agrega una **URL** `Comunidad Tu Patrimonio` al curso nuevo, con la descripción: "Dudas, avisos, alertas de fraude, logros y sesiones en vivo."

## 4. Inscripción

- Si la persona creó la cohorte "Tu Patrimonio": en ambos cursos, *Participantes > Métodos de inscripción > Agregar método > Sincronización de cohortes*, cohorte "Tu Patrimonio", rol Estudiante.
- Si no: deja activada la inscripción manual y repórtalo.
- Agrega al equipo de moderación con rol **Profesor sin permiso de edición** (o Profesor, si lo pide la persona).

## 5. Revisión (con rol de estudiante)

- No se pueden adjuntar archivos en los foros.
- El estudiante puede publicar en Preséntate, Dudas, Alertas y Logros.
- El estudiante no puede publicar en Avisos ni en Referencias comerciales.
- El libro muestra 6 capítulos.
- La consulta y la encuesta funcionan.

## 6. Reporte

Enlace del curso; lista de foros con su configuración; estado de la consulta y la encuesta; método de inscripción; lo que quedó "[por definir]"; capturas de la página principal del curso y de un foro con la advertencia.

El curso queda **oculto** hasta que la persona decida mostrarlo.
