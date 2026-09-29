# Instrucciones para Claude: instalar "Tu Turno, Tu Dinero, Tu Futuro" (Moodle 3.10)

Vas a crear el curso **Tu Turno, Tu Dinero, Tu Futuro** en academia.desarrollatalento.com. El sitio usa Moodle 3.10, el tema Boost, Level Up 3.15.2 y el complemento **Certificado personalizado** (mod_customcert).

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

1. Confirma que no existe un curso con nombre corto `TTDF-MX`. Si existe, detente y pregunta.
2. Revisa en *Administración del sitio > Extensiones > Resumen de extensiones* si existen **Certificado personalizado** y **Level Up**. Anótalo para el reporte.
3. Si el sitio todavía no tiene actividades H5P, la primera que subas instala sus librerías: súbela con la cuenta de administración. Si aparece un error de librerías, detente y reporta el mensaje exacto.

## 1. Crear el curso

| Campo | Valor |
|---|---|
| Nombre | Tu Turno, Tu Dinero, Tu Futuro |
| Nombre corto | TTDF-MX |
| Visibilidad | **Ocultar** |
| Formato | Temas, 10 secciones |
| Seguimiento de finalización | Sí |

## 2. Secciones

| Sección | Nombre | Descripción |
|---|---|---|
| General | Bienvenida | Enlace al capítulo 1 del libro de apoyo y foro "Dudas y comentarios" |
| 1 | Módulo 1. Tu quincena rinde | Contenido de `1_libros/M1_resumen.html` |
| 2 | Módulo 2. Tu cuenta y tu dinero | `M2_resumen.html` |
| 3 | Módulo 3. Tus deudas claras | `M3_resumen.html` |
| 4 | Módulo 4. Tandas y ahorro en grupo | `M4_resumen.html` |
| 5 | Módulo 5. Buró de Crédito sin miedo | `M5_resumen.html` |
| 6 | Módulo 6. Que no te extorsionen | `M6_resumen.html` |
| 7 | Módulo 7. Tu familia y los imprevistos | `M7_resumen.html` |
| 8 | Módulo 8. Tu futuro | `M8_resumen.html` |
| 9 | Materiales de apoyo | "Casos, prácticas, glosario y dónde pedir ayuda." |
| 10 | Evaluación y constancia | "Tu constancia de conclusión." |

Descripción del foro "Dudas y comentarios": "No compartas números de cuenta, contraseñas, códigos ni montos reales de tus deudas."

## 3. Libros de lecciones

En cada sección de módulo:

1. Crea un libro: nombre `Lecciones del Módulo N`, formato de capítulo "Nada", finalización "Ver".
2. Menú del libro > **Importar capítulo** > `1_libros/MN_libro_Moodle.zip`, tipo "Cada archivo HTML representa un capítulo".
3. Comprueba que cada lección tenga su portada primero y 3 subcapítulos sangrados.

| Módulo | Capítulos | Páginas |
|---|---|---|
| M1 | 4 | 16 |
| M2 | 3 | 12 |
| M3 | 4 | 16 |
| M4 | 2 | 8 |
| M5 | 3 | 12 |
| M6 | 4 | 16 |
| M7 | 3 | 12 |
| M8 | 3 | 12 |

## 4. Libro de apoyo

En la sección 9, crea el libro `Materiales de apoyo` con la misma configuración e importa `1_libros/Apoyo_libro_Moodle.zip` (6 capítulos). En la sección General, agrega una **URL** o etiqueta al capítulo 1 ("Bienvenida").

## 5. Glosario

En la sección 9, crea el glosario `Palabras clave del curso` e importa `3_glosario/Glosario_curso_Moodle.xml`, destino "glosario actual".

## 6. Banco de preguntas y autoevaluaciones

1. *Banco de preguntas > Importar*: formato GIFT, `4_preguntas/banco_preguntas_ttdf.gift.txt`. Se crean *Tu Turno/M1* a *M8*, con 78 preguntas.
2. En cada sección de módulo, crea el cuestionario `Autoevaluación del Módulo N`: aprobatoria 70, intentos ilimitados, calificación más alta, respuestas al azar, revisión con correcta y retroalimentación, finalización "Requiere calificación aprobatoria".
3. Agrega **todas** las preguntas de *Tu Turno/MN*, 10 por página:

| M1 | M2 | M3 | M4 | M5 | M6 | M7 | M8 |
|---|---|---|---|---|---|---|---|
| 12 | 9 | 12 | 6 | 9 | 12 | 9 | 9 |

## 7. Actividades H5P (26)

Archivos en `2_h5p/MN/`, en orden. En cada sección, **después del libro** y en orden de lección:

1. *Agregar actividad > Actividad H5P*.
2. Nombre: `MN UYY · ¿Qué harías?`.
3. Sube `MN_UYY_que_harias.h5p`.
4. Opciones: descarga no, incrustar no, derechos de autor sí.
5. Calificación: seguimiento sí, "calificación más alta". Finalización: "El estudiante debe recibir una calificación".

**Orden final de cada sección:** libro, H5P en orden, autoevaluación.

**Comprueba:** abre 3 actividades al azar con *Cambiar rol a > Estudiante*. Debes ver 3 casos, 3 opciones por caso y la calificación al terminar.

## 8. Level Up, insignias, finalización y constancia

Sigue `7_guias/guia_gamificacion.md`: secciones 2 (Level Up), 3 (8 insignias con `5_insignias/`), 4 (finalización con las 8 autoevaluaciones) y 5 (constancia con `6_certificado/certificado_fondo.png`). Si Level Up o Certificado personalizado no existen, no los instales: sáltate ese paso y repórtalo.

## 9. Canal de avisos (pregunta antes)

Este curso no tiene comunidad en Moodle; se acompaña con un **canal de WhatsApp** de avisos (ver `7_guias/comunidad_y_canales.md`). En la sección General agrega una **URL** `Canal de avisos` con el enlace que te dé la persona (si no lo tiene, escribe "[por definir]" y repórtalo). Confirma que las lecciones se ven bien en el celular: el público las toma entre turnos.

## 10. Revisión final (con rol de estudiante)

- M1 U01: portada primero, dos botones de ruta, términos en color con su significado y recuadros "Dato vigente" o "Antes de actuar, verifica".
- Una H5P por módulo abre, muestra 3 casos y registra calificación.
- Una autoevaluación muestra 3 opciones por pregunta.
- El libro de apoyo muestra "Ver la clave" en los casos integradores y las preguntas frecuentes desplegables.

## 11. Reporte para la persona

Enlace del curso; páginas por libro; H5P por módulo; preguntas por autoevaluación; insignias activas; configuración de Level Up; estado de la constancia; lo que no pudiste hacer y por qué; capturas de una portada, una H5P, una autoevaluación y la vista previa de la constancia.

El curso queda **oculto**. La persona decide cuándo mostrarlo.
