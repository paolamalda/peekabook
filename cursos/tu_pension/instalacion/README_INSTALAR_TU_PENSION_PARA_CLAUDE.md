# Instrucciones para Claude: instalar "Tu Pensión, Tu Tranquilidad, Tu Futuro" (Moodle 3.10)

Vas a crear el curso **Tu Pensión, Tu Tranquilidad, Tu Futuro** en academia.desarrollatalento.com. El sitio usa Moodle 3.10, el tema Boost, Level Up 3.15.2 y el complemento **Certificado personalizado** (mod_customcert).

Si en el sitio existen otros cursos, **no los toques.**

Trabaja con el navegador y con la sesión de administrador que la persona abrió.

Reglas:

- Usa solo la interfaz web.
- No uses SSH.
- No instales complementos.
- No cambies la configuración del sitio.
- No toques otros cursos.
- Si algo no coincide con estas instrucciones, detente y pregunta.

## 0. Antes de empezar

1. Confirma que no existe un curso con nombre corto `TPPF-MX`. Si existe, detente y pregunta.
2. Revisa en *Administración del sitio > Extensiones > Resumen de extensiones* si existen **Certificado personalizado** y **Level Up**. Anótalo para el reporte.
3. Si el sitio todavía no tiene actividades H5P, la primera que subas instala sus librerías: súbela con la cuenta de administración. Si aparece un error de librerías, detente y reporta el mensaje exacto.

## 1. Crear el curso

| Campo | Valor |
|---|---|
| Nombre | Tu Pensión, Tu Tranquilidad, Tu Futuro |
| Nombre corto | TPPF-MX |
| Visibilidad | **Mostrar** |
| Formato | **Mosaicos** (Tiles). 10 secciones |
| Seguimiento de finalización | Sí |

**Formato Mosaicos:**
- *Mostrar progreso en los mosaicos*: **como porcentaje**.
- **Usar submosaicos para las actividades: Sí** (cada lección se ve como un mosaico dentro de su parte).
- Un ícono por parte acorde a su tema; la sección General arriba de los mosaicos.
- Oculta el bloque *Tabla de posiciones* o *Ranking* de Level Up si aparece en la columna derecha.

**Inscripción:** *Métodos de inscripción* > activa **Autoinscripción** con la **clave de inscripción** que te dé la persona (si no la tienes, deja "[por definir]" y repórtalo). Desactiva el acceso de invitados.

## 2. Secciones

| Sección | Nombre | Descripción |
|---|---|---|
| General | Bienvenida | Libro «Bienvenida», foro "Dudas y comentarios", encuesta de inicio, «Tu punto de partida» y «Mi meta» |
| 1 | Tu pensión y tu mes | Contenido de `1_libros/M1_resumen.html` |
| 2 | Tu tarjeta y el cajero, sin riesgos | `M2_resumen.html` |
| 3 | Llamadas, mensajes y «el nieto en apuros» | `M3_resumen.html` |
| 4 | Cuando el abuso viene de casa | `M4_resumen.html` |
| 5 | Préstamos a cuenta de tu pensión | `M5_resumen.html` |
| 6 | Decidir con apoyo, sin perder el control | `M6_resumen.html` |
| 7 | Testamento y beneficiarios | `M7_resumen.html` |
| 8 | Tu salud y tus seguros | `M8_resumen.html` |
| 9 | Materiales de apoyo | "Casos, prácticas, glosario y dónde pedir ayuda." |
| 10 | Cierre y constancia | "Lo que lograste, tu constancia y hasta pronto." |

Descripción del foro "Dudas y comentarios": "No compartas números de cuenta, NIP, contraseñas, tu CURP, documentos ni montos reales de tus deudas."

### Bienvenida y despedida (libros con diseño)

Son lo primero y lo último que ve la persona: no los omitas.

1. **Sección General, arriba de todo:** crea el libro `Bienvenida` (formato de capítulo "Nada", navegación "Texto") e importa `1_libros/Bienvenida_libro_Moodle.zip`, tipo "Cada archivo HTML representa un capítulo". Deben quedar 4 capítulos: Te damos la bienvenida, Cómo funciona el curso, Guía de contacto y comunidad, Antes de empezar. Finalización: "Ver".
2. Debajo, el foro **"Dudas y comentarios"** (foro general). **No crees un foro de presentaciones:** pedir que la gente se presente invita a compartir datos personales.
   Después, la tarea **"Mi meta"**: tipo *Tarea*, entrega "Texto en línea" (límite de 60 palabras), **sin calificación**, sin fecha límite, sin avisos a otros participantes; las entregas solo las ven la persona y el equipo del curso. Instrucciones: "En una frase: qué esperas del programa y qué quieres lograr. No escribas datos personales ni montos reales. Al final del curso la vuelves a abrir." Permite editar la entrega en cualquier momento. Finalización: "Enviar".
3. Debajo, la **Encuesta de inicio** (sección 8) y el cuestionario **«Tu punto de partida»**: importa `4_preguntas/diagnostica.gift.txt` (crea su propia categoría «Diagnóstica»), todas las preguntas, calificación sobre 0 (no cuenta para la calificación), **un intento**, tiempo máximo 10 minutos, revisión con respuesta correcta al terminar.
4. **Restringir acceso** de la primera lección de la Parte 1: el libro `Bienvenida` debe estar visto.
5. **Sección 10, arriba de todo:** crea el libro `Cierre y despedida` con la misma configuración e importa `1_libros/Cierre_libro_Moodle.zip` (4 capítulos: Lo que lograste, Tu plan sigue, Encuesta final y constancia, Hasta pronto). Restringir acceso: la autoevaluación de la última parte debe estar completa. Debajo van la encuesta final y la constancia.
6. **Guía para imprimir o compartir:** `7_guias/Guia_de_contacto_y_comunidad.html`. Ábrela en el navegador > Imprimir > Guardar como PDF, y compártela en la sesión presencial o por WhatsApp.

## 3. Lecciones: un libro por lección

La estructura completa (nombres, orden, archivos y minutos) está en `estructura_moodle.json`. En cada sección, por cada lección y en orden:

1. Crea un **Libro** con el nombre de la lección **tal cual** (la pregunta, sin claves como «M1 U01»). Formato de capítulo "Nada"; estilo de navegación "Texto".
2. Menú del libro > **Importar capítulo** > el zip de la lección (`1_libros/MN/NN_MN_UYY.zip`), tipo "Cada archivo HTML representa un capítulo". Deben quedar 4 capítulos: Empieza, Lo esencial, Profundiza, Practica.
3. **Finalización:** "Ver".
4. **Restringir acceso:** la lección anterior debe estar completa (la primera de cada parte, sin restricción; la primera de la parte 2 en adelante pide la última de la parte anterior). Muestra la lección bloqueada en gris, no oculta.

| Parte | Lecciones | Carpeta |
|---|---|---|
| Tu pensión y tu mes | 2 | `1_libros/M1/` |
| Tu tarjeta y el cajero, sin riesgos | 2 | `1_libros/M2/` |
| Llamadas, mensajes y «el nieto en apuros» | 2 | `1_libros/M3/` |
| Cuando el abuso viene de casa | 2 | `1_libros/M4/` |
| Préstamos a cuenta de tu pensión | 2 | `1_libros/M5/` |
| Decidir con apoyo, sin perder el control | 2 | `1_libros/M6/` |
| Testamento y beneficiarios | 2 | `1_libros/M7/` |
| Tu salud y tus seguros | 2 | `1_libros/M8/` |

## 4. Libro de apoyo

En la sección 9, crea el libro `Materiales de apoyo` con la misma configuración e importa `1_libros/Apoyo_libro_Moodle.zip` (6 capítulos).

En la misma sección 9, agrega un recurso **Archivo** llamado `Herramientas para tus cuentas (Excel)` con el archivo de `10_herramientas/`. Mostrar: "Forzar descarga". Descripción: "Presupuesto, lista de deudas, fondo de emergencia y meta con interés compuesto; además: tus pensiones y tu mes. Escribe solo en las celdas rosas; el archivo es tuyo y no se comparte." Finalización: "Ver".

## 5. Glosario

En la sección 9, crea el glosario `Palabras clave del curso` e importa `3_glosario/Glosario_curso_Moodle.xml`, destino "glosario actual".

## 6. Banco de preguntas y autoevaluaciones

1. *Banco de preguntas > Importar*: formato GIFT, `4_preguntas/banco_preguntas_tppf.gift.txt`. Se crean *Tu Pensión v0.1/M1* a *M8*, con 48 preguntas.
2. En cada sección de módulo, crea el cuestionario `Autoevaluación del Módulo N`: aprobatoria 70, intentos ilimitados, calificación más alta, respuestas al azar, revisión con correcta y retroalimentación, finalización "Requiere calificación aprobatoria".
3. Agrega **todas** las preguntas de *Tu Pensión v0.1/MN*, 10 por página:

| M1 | M2 | M3 | M4 | M5 | M6 | M7 | M8 |
|---|---|---|---|---|---|---|---|
| 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |

## 7. Práctica dentro de cada lección (16 H5P)

La práctica **no** va como actividad aparte en la sección: va incrustada en el capítulo «Practica» de su libro.

1. *Banco de contenido* del curso > **Subir** los 16 archivos de `2_h5p/MN/` (`MN_UYY_practica.h5p`).
2. Abre el capítulo «Practica» de cada libro en modo edición. Verás un recuadro rosa con el texto `[[H5P MN_UYY_practica.h5p]]`.
3. Borra **todo el recuadro** y en su lugar inserta el H5P con el botón **Insertar H5P** del editor, eligiendo ese archivo del banco de contenido.
4. Guarda y comprueba con *Cambiar rol a > Estudiante* que se vean las situaciones y preguntas, una por pantalla.

**Nota:** la práctica incrustada no registra calificación. El avance de cada lección se marca al verla, y la calificación del módulo sale de la autoevaluación.

**Orden final de cada sección:** las lecciones en orden y al final la autoevaluación (restringida a completar la última lección de la parte).

## 8. Encuestas del programa

En `8_encuestas/` están las encuestas y su documento `encuestas.md`. Usa el módulo **Retroalimentación** (Feedback), modo **anónimo**, y en cada una *Plantillas > Importar preguntas* con su XML (si la importación falla, créalas a mano con `encuestas.md`):

| Actividad | Sección | Archivo | Finalización |
|---|---|---|---|
| `Encuesta de inicio` | General | `encuesta_inicio.xml` | Enviar |
| `Encuesta final` | 10 | `encuesta_final.xml` | Enviar; es requisito de la constancia |
| `Seguimiento a 30 días` | 10 | `encuesta_seguimiento.xml` | Enviar |
| `Seguimiento a 90 días` | 10 | `encuesta_seguimiento.xml` | Enviar |

Restringe los seguimientos por fecha: 30 y 90 días después de la fecha de fin de la cohorte ("[por definir]"). La encuesta final es la evidencia de resultados del programa: no la omitas.

## 9. Level Up, insignias, finalización y constancia

Sigue `7_guias/guia_gamificacion.md`: secciones 2 (Level Up), 3 (8 insignias con `5_insignias/`; cada nombre lleva el curso para que sea único en la plataforma), 4 (finalización con las 8 autoevaluaciones) y 5 (constancia con la plantilla estándar y los datos de `6_constancia/constancia.md`). Si Level Up o Certificado personalizado no existen, no los instales: sáltate ese paso y repórtalo.

## 10. Revisión final (con rol de estudiante)

- La portada muestra un mosaico por parte con su porcentaje; dentro de cada parte, un submosaico por lección sin claves técnicas.
- La primera lección: capítulos Empieza, Lo esencial, Profundiza y Practica; «Cuidado con estos errores» al final de Lo esencial; la práctica incrustada funciona.
- La segunda lección aparece bloqueada hasta ver la primera.
- No hay ranking ni tabla de posiciones visible.
- Una autoevaluación muestra 3 opciones por pregunta.
- El libro de apoyo muestra "Ver la clave" en los casos integradores y las preguntas frecuentes desplegables.

## 11. Reporte para la persona

Enlace del curso; libros por parte; H5P incrustadas; preguntas por autoevaluación; encuestas creadas; insignias activas; configuración de Level Up; estado de la constancia; lo que no pudiste hacer y por qué; capturas de la portada en mosaicos, una H5P, una autoevaluación y la vista previa de la constancia.

El curso queda **visible**, con inscripción por clave. Para la ficha del catálogo usa `tarjeta_catalogo.md`.
