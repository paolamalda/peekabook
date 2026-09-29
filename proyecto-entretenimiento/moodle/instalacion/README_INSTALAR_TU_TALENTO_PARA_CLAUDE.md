# Instrucciones para Claude: instalar "Tu Talento, Tu Marca, Tu Futuro" (Moodle 3.10)

Vas a crear el curso nuevo **Tu Talento, Tu Marca, Tu Futuro** en academia.desarrollatalento.com. El sitio usa Moodle 3.10, el tema Boost, Level Up 3.15.2 y el complemento **Certificado personalizado** (mod_customcert), ya instalados.

Si en el sitio existen otros cursos (por ejemplo, "Tu Dinero, Tu Familia, Tu Futuro"), **no los toques.**

Trabaja con el navegador y con la sesión de administrador que la persona abrió.

Reglas:

- Usa solo la interfaz web.
- No uses SSH.
- No instales complementos.
- No cambies la configuración del sitio.
- No toques otros cursos.
- Si algo no coincide con estas instrucciones, detente y pregunta.

## 0. Antes de empezar

1. Confirma que no existe un curso con nombre corto `TTMF-MX`. Si existe, detente y pregunta.
2. Confirma que existen **Certificado personalizado** y **Level Up** en *Administración del sitio > Extensiones > Resumen de extensiones*.
3. Si el sitio todavía no tiene actividades H5P, la primera que subas instala sus librerías: súbela con la cuenta de administración. Si aparece un error de librerías, detente y reporta el mensaje exacto.

## 1. Crear el curso

| Campo | Valor |
|---|---|
| Nombre | Tu Talento, Tu Marca, Tu Futuro |
| Nombre corto | TTMF-MX |
| Visibilidad | **Ocultar** |
| Formato | Temas, 13 secciones |
| Seguimiento de finalización | Sí |

## 2. Secciones

| Sección | Nombre | Descripción |
|---|---|---|
| General | Bienvenida | Enlace al capítulo 1 del libro de apoyo y foro "Dudas y comentarios" |
| 1 | Módulo 1. Tu dinero real: ingresos variables | Contenido de `1_libros/M1_resumen.html` |
| 2 | Módulo 2. Tu carrera como negocio: régimen fiscal e impuestos | `M2_resumen.html` |
| 3 | Módulo 3. Contratos, representación y regalías | `M3_resumen.html` |
| 4 | Módulo 4. Conoce el sistema financiero mexicano | `M4_resumen.html` |
| 5 | Módulo 5. Compara y elige: instituciones y productos | `M5_resumen.html` |
| 6 | Módulo 6. El crédito es deuda | `M6_resumen.html` |
| 7 | Módulo 7. Buró y Círculo de Crédito | `M7_resumen.html` |
| 8 | Módulo 8. Sal de deudas | `M8_resumen.html` |
| 9 | Módulo 9. No caigas: fraudes y robo de identidad | `M9_resumen.html` |
| 10 | Módulo 10. Protección y prevención | `M10_resumen.html` |
| 11 | Módulo 11. Tu futuro | `M11_resumen.html` |
| 12 | Materiales de apoyo | "Casos, prácticas, glosario y dónde pedir ayuda." |
| 13 | Evaluación y constancia | "Tu constancia de conclusión." |

Descripción del foro "Dudas y comentarios": "No compartas RFC, CURP, números de cuenta, contraseñas ni montos reales."

## 3. Libros de lecciones (M1 a M11)

En cada sección de módulo:

1. Crea un libro: nombre `Lecciones del Módulo N`, formato de capítulo "Nada", finalización "Ver".
2. Menú del libro > **Importar capítulo** > `1_libros/MN_libro_Moodle.zip`, tipo "Cada archivo HTML representa un capítulo".
3. Comprueba que cada lección tenga su portada primero y 3 subcapítulos sangrados.

| Módulo | Capítulos | Páginas |
|---|---|---|
| M1 | 6 | 24 |
| M2 | 5 | 20 |
| M3 | 6 | 24 |
| M4 | 4 | 16 |
| M5 | 7 | 28 |
| M6 | 6 | 24 |
| M7 | 10 | 40 |
| M8 | 5 | 20 |
| M9 | 9 | 36 |
| M10 | 6 | 24 |
| M11 | 9 | 36 |

## 4. Libro de apoyo

En la sección 12, crea el libro `Materiales de apoyo` con la misma configuración e importa `1_libros/Apoyo_libro_Moodle.zip` (6 capítulos). En la sección General, agrega una **URL** o etiqueta al capítulo 1 ("Bienvenida").

## 5. Glosario

En la sección 12, crea el glosario `Palabras clave del curso` e importa `3_glosario/Glosario_curso_Moodle.xml`, destino "glosario actual".

## 6. Banco de preguntas y autoevaluaciones

1. *Banco de preguntas > Importar*: formato GIFT, `4_preguntas/banco_preguntas_ttmf.gift.txt`. Se crean *Tu Talento/M1* a *M11*, con 219 preguntas.
2. En cada sección de módulo, crea el cuestionario `Autoevaluación del Módulo N`: aprobatoria 70, intentos ilimitados, calificación más alta, respuestas al azar, revisión con correcta y retroalimentación, finalización "Requiere calificación aprobatoria".
3. Agrega **todas** las preguntas de *Tu Talento/MN*, 10 por página:

| M1 | M2 | M3 | M4 | M5 | M6 | M7 | M8 | M9 | M10 | M11 |
|---|---|---|---|---|---|---|---|---|---|---|
| 18 | 15 | 18 | 12 | 21 | 18 | 30 | 15 | 27 | 18 | 27 |

## 7. Actividades H5P (73)

Archivos en `2_h5p/MN/`, en orden. En cada sección, **después del libro** y en orden de lección:

1. *Agregar actividad > Actividad H5P*.
2. Nombre: `MN UYY · ¿Qué harías?`.
3. Sube `MN_UYY_que_harias.h5p`.
4. Opciones: descarga no, incrustar no, derechos de autor sí.
5. Calificación: seguimiento sí, "calificación más alta". Finalización: "El estudiante debe recibir una calificación".

**Orden final de cada sección:** libro, H5P en orden, autoevaluación.

## 8. Level Up, insignias, finalización y constancia

Sigue `7_guias/guia_gamificacion_ttmf.md`: secciones 2 (Level Up), 3 (8 insignias con `5_insignias/`), 4 (finalización con las 11 autoevaluaciones) y 5 (constancia con `6_certificado/certificado_fondo.png`).

## 9. Comunidad (opcional, pregunta antes)

Pregunta a la persona si quiere que crees el curso **Comunidad Tu Talento** (`TTMF-COM`, oculto). Tiene su propia carpeta y sus instrucciones: `README_CREAR_COMUNIDAD_PARA_CLAUDE.md`. La cohorte y el canal de WhatsApp los configura la persona.

## 10. Revisión final (con rol de estudiante)

- M1 U01: portada primero, dos botones de ruta, términos en color con su significado, recuadros "Dato vigente" y "Antes de actuar, verifica".
- M7 U06: la tabla de plazos de eliminación se ve completa.
- Una H5P por módulo abre, muestra 3 casos y registra calificación.
- Una autoevaluación muestra 3 opciones por pregunta.
- El libro de apoyo muestra "Ver la clave" en los casos integradores y las preguntas frecuentes desplegables.

## 11. Reporte para la persona

Enlace del curso; páginas por libro; H5P por módulo; preguntas por autoevaluación; insignias activas; configuración de Level Up; estado de la constancia; lo que no pudiste hacer y por qué; capturas de una portada, una H5P, una autoevaluación y la vista previa de la constancia.

El curso queda **oculto**. La persona decide cuándo mostrarlo.
