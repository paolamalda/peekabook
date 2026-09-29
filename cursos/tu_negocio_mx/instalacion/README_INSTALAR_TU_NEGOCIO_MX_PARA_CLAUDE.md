# Instrucciones para Claude: instalar "Tu Negocio, Tu Dinero, Tu Futuro" (Moodle 3.10)

Vas a crear el curso **Tu Negocio, Tu Dinero, Tu Futuro** en academia.desarrollatalento.com. El sitio usa Moodle 3.10, el tema Boost, Level Up 3.15.2 y el complemento **Certificado personalizado** (mod_customcert).

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

1. Confirma que no existe un curso con nombre corto `TNDF-MX`. Si existe, detente y pregunta.
2. Revisa en *Administración del sitio > Extensiones > Resumen de extensiones* si existen **Certificado personalizado** y **Level Up**. Anótalo para el reporte.
3. Si el sitio todavía no tiene actividades H5P, la primera que subas instala sus librerías: súbela con la cuenta de administración. Si aparece un error de librerías, detente y reporta el mensaje exacto.

## 1. Crear el curso

| Campo | Valor |
|---|---|
| Nombre | Tu Negocio, Tu Dinero, Tu Futuro |
| Nombre corto | TNDF-MX |
| Visibilidad | **Ocultar** |
| Formato | Temas, 11 secciones |
| Seguimiento de finalización | Sí |

## 2. Secciones

| Sección | Nombre | Descripción |
|---|---|---|
| General | Bienvenida | Enlace al capítulo 1 del libro de apoyo y foro "Dudas y comentarios" |
| 1 | Módulo 1. Tu negocio y tu casa: dinero separado | Contenido de `1_libros/M1_resumen.html` |
| 2 | Módulo 2. Costos y precio | `M2_resumen.html` |
| 3 | Módulo 3. Flujo de efectivo | `M3_resumen.html` |
| 4 | Módulo 4. Cobrar y vender sin perder | `M4_resumen.html` |
| 5 | Módulo 5. Formalízate sin miedo | `M5_resumen.html` |
| 6 | Módulo 6. Crédito para tu negocio | `M6_resumen.html` |
| 7 | Módulo 7. Protege tu negocio | `M7_resumen.html` |
| 8 | Módulo 8. Crecer con orden | `M8_resumen.html` |
| 9 | Módulo 9. Tu futuro | `M9_resumen.html` |
| 10 | Materiales de apoyo | "Casos, prácticas, glosario y dónde pedir ayuda." |
| 11 | Evaluación y constancia | "Tu constancia de conclusión." |

Descripción del foro "Dudas y comentarios": "No compartas tu RFC, contraseñas del SAT, e.firma, números de cuenta ni montos reales de tu negocio."

## 3. Libros de lecciones

En cada sección de módulo:

1. Crea un libro: nombre `Lecciones del Módulo N`, formato de capítulo "Nada", finalización "Ver".
2. Menú del libro > **Importar capítulo** > `1_libros/MN_libro_Moodle.zip`, tipo "Cada archivo HTML representa un capítulo".
3. Comprueba que cada lección tenga su portada primero y 3 subcapítulos sangrados.

| Módulo | Capítulos | Páginas |
|---|---|---|
| M1 | 4 | 16 |
| M2 | 4 | 16 |
| M3 | 3 | 12 |
| M4 | 3 | 12 |
| M5 | 5 | 20 |
| M6 | 4 | 16 |
| M7 | 5 | 20 |
| M8 | 3 | 12 |
| M9 | 3 | 12 |

## 4. Libro de apoyo

En la sección 10, crea el libro `Materiales de apoyo` con la misma configuración e importa `1_libros/Apoyo_libro_Moodle.zip` (6 capítulos). En la sección General, agrega una **URL** o etiqueta al capítulo 1 ("Bienvenida").

## 5. Glosario

En la sección 10, crea el glosario `Palabras clave del curso` e importa `3_glosario/Glosario_curso_Moodle.xml`, destino "glosario actual".

## 6. Banco de preguntas y autoevaluaciones

1. *Banco de preguntas > Importar*: formato GIFT, `4_preguntas/banco_preguntas_tndf_mx.gift.txt`. Se crean *Tu Negocio MX/M1* a *M9*, con 102 preguntas.
2. En cada sección de módulo, crea el cuestionario `Autoevaluación del Módulo N`: aprobatoria 70, intentos ilimitados, calificación más alta, respuestas al azar, revisión con correcta y retroalimentación, finalización "Requiere calificación aprobatoria".
3. Agrega **todas** las preguntas de *Tu Negocio MX/MN*, 10 por página:

| M1 | M2 | M3 | M4 | M5 | M6 | M7 | M8 | M9 |
|---|---|---|---|---|---|---|---|---|
| 12 | 12 | 9 | 9 | 15 | 12 | 15 | 9 | 9 |

## 7. Actividades H5P (34)

Archivos en `2_h5p/MN/`, en orden. En cada sección, **después del libro** y en orden de lección:

1. *Agregar actividad > Actividad H5P*.
2. Nombre: `MN UYY · ¿Qué harías?`.
3. Sube `MN_UYY_que_harias.h5p`.
4. Opciones: descarga no, incrustar no, derechos de autor sí.
5. Calificación: seguimiento sí, "calificación más alta". Finalización: "El estudiante debe recibir una calificación".

**Orden final de cada sección:** libro, H5P en orden, autoevaluación.

**Comprueba:** abre 3 actividades al azar con *Cambiar rol a > Estudiante*. Debes ver 3 casos, 3 opciones por caso y la calificación al terminar.

## 8. Level Up, insignias, finalización y constancia

Sigue `7_guias/guia_gamificacion.md`: secciones 2 (Level Up), 3 (8 insignias con `5_insignias/`), 4 (finalización con las 9 autoevaluaciones) y 5 (constancia con `6_certificado/certificado_fondo.png`). Si Level Up o Certificado personalizado no existen, no los instales: sáltate ese paso y repórtalo.

## 9. Comunidad (opcional, pregunta antes)

Pregunta a la persona si quiere que crees el curso **Comunidad Tu Negocio** (`TNDF-COM`, oculto). Tiene su propia carpeta y sus instrucciones: `README_CREAR_COMUNIDAD_PARA_CLAUDE.md`.

## 10. Revisión final (con rol de estudiante)

- M1 U01: portada primero, dos botones de ruta, términos en color con su significado y recuadros "Dato vigente" o "Antes de actuar, verifica".
- Una H5P por módulo abre, muestra 3 casos y registra calificación.
- Una autoevaluación muestra 3 opciones por pregunta.
- El libro de apoyo muestra "Ver la clave" en los casos integradores y las preguntas frecuentes desplegables.

## 11. Reporte para la persona

Enlace del curso; páginas por libro; H5P por módulo; preguntas por autoevaluación; insignias activas; configuración de Level Up; estado de la constancia; lo que no pudiste hacer y por qué; capturas de una portada, una H5P, una autoevaluación y la vista previa de la constancia.

El curso queda **oculto**. La persona decide cuándo mostrarlo.
