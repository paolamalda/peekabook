# Instrucciones para Claude: instalar "Tu Dinero, Tu Familia, Tu Futuro" (Moodle 3.10)

Vas a crear el curso en español **Tu Dinero, Tu Familia, Tu Futuro** en academia.desarrollatalento.com. El sitio usa Moodle 3.10, el tema Boost, Level Up 3.15.2 y el complemento **Certificado personalizado** (mod_customcert).

Trabaja con el navegador y con la sesión de administrador que la persona abrió.

Reglas:

- Usa solo la interfaz web.
- No uses SSH.
- No instales complementos.
- No cambies la configuración del sitio.
- No toques otros cursos.
- Si algo no coincide con estas instrucciones, detente y pregunta.

## 0. Antes de empezar

1. Confirma que no existe un curso con nombre corto `TDTF-CA-ES`. Si existe, detente y pregunta.
2. Revisa en *Administración del sitio > Extensiones > Resumen de extensiones* si existen **Certificado personalizado** y **Level Up**, y si Level Up es la versión sin costo o Level Up+. Anótalo para el reporte.
3. Si el sitio todavía no tiene actividades H5P, la primera que subas instala sus librerías: súbela con la cuenta de administración. Si aparece un error de librerías, detente y reporta el mensaje exacto.

## 1. Crear el curso

*Administración del sitio > Cursos > Agregar un nuevo curso*:

| Campo | Valor |
|---|---|
| Nombre | Tu Dinero, Tu Familia, Tu Futuro (piloto California) |
| Nombre corto | TDTF-CA-ES |
| Visibilidad | **Ocultar** |
| Formato | Temas, 7 secciones |
| Seguimiento de finalización | Sí |

## 2. Secciones

| Sección | Nombre | Descripción |
|---|---|---|
| General | Bienvenida | Enlace al capítulo 1 del libro de apoyo y foro "Dudas y comentarios" |
| 1 | Módulo 1. Entiende tu dinero y organiza tu economía | Contenido de `1_libros/M1_resumen.html` |
| 2 | Módulo 2. Entiende el sistema financiero y planea tus remesas | `M2_resumen.html` |
| 3 | Módulo 3. Construye tu crédito y maneja tus deudas | `M3_resumen.html` |
| 4 | Módulo 4. Protege tu dinero, tu identidad y tu familia | `M4_resumen.html` |
| 5 | Módulo 5. Construye patrimonio y prepara tu futuro | `M5_resumen.html` |
| 6 | Materiales de apoyo | "Casos, prácticas, glosario y dónde pedir ayuda." |
| 7 | Evaluación y constancia | "Tu constancia de conclusión." |

Descripción del foro "Dudas y comentarios": "No compartas números de cuenta, SSN, ITIN, contraseñas ni tu situación migratoria."

## 3. Libros de lecciones (M1 a M5)

En cada sección de módulo:

1. Crea un libro:
   - Nombre: `Lecciones del Módulo N`.
   - Formato de capítulo: Nada.
   - Finalización: Ver.
2. Menú del libro > **Importar capítulo** > `1_libros/MN_libro_Moodle.zip`, tipo "Cada archivo HTML representa un capítulo".
3. Comprueba las páginas. En cada lección, la portada va primero y sus 3 subcapítulos sangrados debajo.

   | Módulo | Capítulos | Páginas |
   |---|---|---|
   | M1 | 14 | 56 |
   | M2 | 13 | 52 |
   | M3 | 10 | 40 |
   | M4 | 11 | 44 |
   | M5 | 11 | 44 |

4. El libro es la **primera actividad** de su sección.

## 4. Libro de apoyo

En la sección 6, crea el libro `Materiales de apoyo` con la misma configuración e importa `1_libros/Apoyo_libro_Moodle.zip` (6 capítulos).

En la sección General, agrega una **URL** o etiqueta que apunte al capítulo 1 ("Bienvenida") de este libro.

## 5. Glosario

En la sección 6, crea el glosario `Palabras clave del curso` e importa `3_glosario/Glosario_curso_Moodle.xml`, con destino "glosario actual".

## 6. Banco de preguntas y autoevaluaciones

1. *Administración del curso > Banco de preguntas > Importar*: formato GIFT, archivo `4_preguntas/banco_preguntas_v3_es.gift.txt`.
   - Se crean las categorías *Tu Dinero v3/M1* a *M5*, con 177 preguntas.
2. En cada sección de módulo, crea el cuestionario `Autoevaluación del Módulo N`:
   - Calificación aprobatoria: 70.
   - Intentos: ilimitados.
   - Método: calificación más alta.
   - Ordenar al azar las respuestas: sí.
   - Revisión: después del intento, mostrar si fue correcta, la retroalimentación y la respuesta correcta.
   - Finalización: "Requiere calificación aprobatoria".
3. Agrega **todas** las preguntas de *Tu Dinero v3/MN*, 10 por página:

   | Módulo | Preguntas |
   |---|---|
   | M1 | 42 |
   | M2 | 39 |
   | M3 | 30 |
   | M4 | 33 |
   | M5 | 33 |

## 7. Actividades H5P (59)

Los archivos están en `2_h5p/MN/`, en orden. Cada archivo trae sus librerías. En cada sección de módulo, **después del libro** y en orden de lección:

1. *Agregar actividad > Actividad H5P*.
2. Nombre: `MN UYY · ¿Qué harías?`. Por ejemplo: `M1 U01 · ¿Qué harías?`.
3. Sube `MN_UYY_que_harias.h5p`.
4. Opciones de H5P: permitir descarga no; botón de incrustar no; botón de derechos de autor sí.
5. Calificación: seguimiento de intentos sí; método "calificación más alta".
6. Finalización: "El estudiante debe recibir una calificación".

**Orden final de cada sección:** libro, H5P de sus lecciones en orden, autoevaluación.

**Comprueba:** abre 3 actividades al azar con *Cambiar rol a > Estudiante*. Debes ver 3 casos, 3 opciones por caso y la calificación al terminar.

## 8. Level Up

Agrega el bloque Level Up al curso y sigue la sección 2 de `7_guias/guia_gamificacion_v3.md`: reglas, 6 niveles y clasificación anónima. Si Level Up no existe en el sitio, sáltate este paso y repórtalo.

## 9. Insignias

Sigue la sección 3 de la guía con las 8 imágenes de `5_insignias/`. Crea cada insignia con su criterio y actívalas al final.

## 10. Finalización del curso y constancia

1. Configura la **Finalización del curso** con las 5 autoevaluaciones (sección 4 de la guía).
2. Si **Certificado personalizado** está instalado, crea en la sección 7 la "Constancia de conclusión" según la sección 5 de la guía, con `6_certificado/certificado_fondo.png`. Revisa la vista previa en PDF y compárala con `certificado_muestra.png`.
3. Si **no** está instalado, no lo instales. Deja en la sección 7 la etiqueta: "Al aprobar las cinco autoevaluaciones recibirás la insignia Plan completo y tu constancia de conclusión", y repórtalo.

## 11. Revisión final (con rol de estudiante)

- M1 U01: la portada aparece primero, con los dos botones de ruta; "Lo esencial", "Profundiza" y "Practica" van debajo de su lección; los términos en color muestran su significado.
- La página *Practica* describe "¿Qué harías?" y su quiz tiene 3 opciones.
- La H5P de M1 U01 funciona y registra la calificación.
- La autoevaluación de M1 muestra 3 opciones por pregunta.
- El libro de apoyo muestra "Ver la clave" en los casos integradores.

## 12. Reporte para la persona

Incluye el enlace del curso, el número de páginas de cada libro, las H5P subidas por módulo, las preguntas por autoevaluación, las insignias creadas, la configuración de Level Up (sin costo o Level Up+), si la constancia quedó lista, todo lo que no pudiste hacer y por qué, y capturas de: una portada de lección, una H5P, una autoevaluación y la vista previa de la constancia.

El curso queda **oculto**. La persona decide cuándo mostrarlo.
