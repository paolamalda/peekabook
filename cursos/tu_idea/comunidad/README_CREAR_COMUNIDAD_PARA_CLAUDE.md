# Instrucciones para Claude: crear "Comunidad Tu Idea" (Moodle 3.10)

Vas a crear el curso **Comunidad Tu Idea** en academia.desarrollatalento.com. Es un espacio aparte del curso *Tu Idea, Tu Dinero, Tu Futuro* (DT-IDEA-MX-ES). No toques otros cursos.

Reglas:

- Usa solo la interfaz web.
- No uses SSH.
- No instales complementos.
- No cambies la configuración del sitio.
- Si algo no coincide con estas instrucciones, detente y pregunta.

## 0. Antes de empezar

1. Confirma que no existe un curso con nombre corto `DT-IDEA-MX-ES-COM`. Si existe, detente y pregunta.
2. Pregunta a la persona:
   - la fecha y el lugar o enlace de la primera sesión de acompañamiento;
   - el enlace del canal de WhatsApp;
   - si quiere inscribir a las personas con una cohorte (la crea la persona administradora del sitio) o de forma manual.
   Si no tiene esos datos, deja el texto "[por definir]" y repórtalo.


## 0.1 Cuidado de menores (antes de crear el curso)

1. Pregunta a la persona si la escuela ya avisó a madres, padres o tutores. Si no, detente y repórtalo.
2. La mensajería entre participantes se configura en el sitio: no la cambies. Pregunta a la persona administradora si está restringida; si no lo está, repórtalo como pendiente.
3. Esta comunidad no tiene referencias comerciales (ver sección 3).

## 1. Crear el curso

| Campo | Valor |
|---|---|
| Nombre | Comunidad Tu Idea |
| Nombre corto | DT-IDEA-MX-ES-COM |
| Visibilidad | **Mostrar** |
| Inscripción | Autoinscripción con la clave que te dé la persona («[por definir]» si no la tienes) |
| Formato | Temas, 3 secciones |
| Seguimiento de finalización | No |
| Mostrar calificaciones | No |
| Resumen | "El espacio moderado de Tu Idea, Tu Dinero, Tu Futuro: dudas, retos, vitrina de ideas, alertas de fraude y sesiones con la escuela." |

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
- Copia la advertencia al inicio de cada descripción: "No publiques tu apellido, dirección, escuela, teléfono, redes, fotos, contraseñas ni códigos. No hay mensajes privados: todo se habla aquí."

| Nombre | Tipo de foro | Descripción (después de la advertencia) |
|---|---|---|
| Lo que quiero lograr | Foro para uso general | "En una frase, qué quieres lograr este año. Sin nombre completo, datos personales ni montos reales." |
| Dudas: mi dinero y lo digital | Foro estándar que aparece en un formato similar a un blog | "Módulos 1 y 2. Usa la plantilla del capítulo 3 de la guía." |
| Dudas: crear y crecer | Foro estándar que aparece en un formato similar a un blog | "Módulos 3 y 4. Usa la plantilla del capítulo 3 de la guía." |
| Vitrina de ideas | Foro para uso general | "Cuenta tu idea en tres líneas y pide retroalimentación. No se vende, no se cobra y no se publican datos de contacto." |
| Dudas: invertir, crédito, protección y futuro | Foro estándar que aparece en un formato similar a un blog | "Módulos 5 a 9. Usa la plantilla del capítulo 3 de la guía." |
| Alertas de fraude | Foro para uso general | "Avisa de llamadas, mensajes, visitas o páginas sospechosas, sin datos personales. Si ya te afectó, avisa a un adulto de confianza y sigue M7 U03." |
| Logros | Foro para uso general | "Comparte tus avances y los retos del mes que cumpliste." |

Si en tu versión de Moodle el tipo "similar a un blog" no aparece con ese nombre, usa "Foro para uso general" y repórtalo.

### Sección 2 · Sesiones de acompañamiento

1. **Página** `Sesiones de acompañamiento`: copia el contenido del capítulo 5 (primera parte) y agrega las fechas, el lugar o enlace que te dio la persona.
2. **Consulta** (Choice) `¿Qué tema quieres en la próxima sesión?`:
   - Opciones: "Presupuesto", "Dinero digital", "Mi idea de negocio", "Precio y ganancia", "Invertir", "Crédito", "Fraudes y cuentas mula", "Qué estudiar", "Primer trabajo".
   - Permitir actualizar la respuesta: sí. Mostrar resultados: después de responder. Privacidad: publicar resultados anónimos.
3. **Encuesta** (Feedback) `Encuesta de la comunidad`, anónima, con estas preguntas:
   - Opción múltiple: "¿Qué tan útil te resulta la comunidad?" (Muy útil / Útil / Poco útil / Nada útil).
   - Opción múltiple: "¿Qué espacio usas más?" (Avisos / Foros de dudas / Alertas / Logros / Sesiones / Canal de WhatsApp).
   - Texto largo: "¿Qué tema te gustaría que agregáramos al curso?"
   - Texto largo: "¿Qué mejorarías de la comunidad?"

### Sin referencias comerciales

En esta comunidad participan menores de edad: **no se crea foro de referencias comerciales**. En la sección General agrega una **etiqueta**: "En esta comunidad no hay referencias comerciales. Todo lo que ves es contenido del programa o publicaciones moderadas (capítulo 6 de la guía)."

## 3. Enlazar desde el curso principal

En el curso **DT-IDEA-MX-ES**, sección General, agrega una **URL** `Comunidad Tu Idea` al curso nuevo, con la descripción: "Dudas, avisos, alertas de fraude, logros y sesiones de acompañamiento."

## 4. Inscripción

- Si la persona creó la cohorte "Tu Idea": en ambos cursos, *Participantes > Métodos de inscripción > Agregar método > Sincronización de cohortes*, cohorte "Tu Idea", rol Estudiante.
- Si no: activa la **Autoinscripción** con la clave que te dé la persona («[por definir]» si no la tienes) y repórtalo.
- Agrega al equipo de moderación con rol **Profesor sin permiso de edición** (o Profesor, si lo pide la persona).

## 5. Revisión (con rol de estudiante)

- No se pueden adjuntar archivos en los foros.
- El estudiante puede publicar en Lo que quiero lograr, Dudas, Alertas y Logros.
- El estudiante no puede publicar en Avisos.
- La Vitrina de ideas muestra la advertencia de no vender ni publicar datos de contacto.
- El libro muestra 6 capítulos.
- La consulta y la encuesta funcionan.

## 6. Reporte

Enlace del curso; lista de foros con su configuración; estado de la consulta y la encuesta; método de inscripción; lo que quedó "[por definir]"; capturas de la página principal del curso y de un foro con la advertencia.

El curso queda **visible**, con inscripción por clave.
