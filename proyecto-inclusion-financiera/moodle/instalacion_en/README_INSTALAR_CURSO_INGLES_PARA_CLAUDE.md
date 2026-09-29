# Instrucciones para Claude: instalar el curso en inglés (Moodle 3.10)

Vas a crear el curso en inglés "Your Money, Your Family, Your Future" en academia.desarrollatalento.com. El sitio usa Moodle 3.10, el tema Boost, Level Up 3.15.2 y el complemento **Certificado personalizado** (mod_customcert), que ya está instalado.

Es un curso separado del curso en español (TDTF-CA-ES). Si ese curso existe, **no lo toques.**

Trabaja con el navegador y con la sesión de administrador que la persona abrió.

Reglas:

- Usa solo la interfaz web.
- No uses SSH.
- No instales complementos.
- No cambies la configuración del sitio.
- No toques otros cursos.
- Si algo no coincide con estas instrucciones, detente y pregunta.

Todo el contenido del curso va en inglés. Estas instrucciones están en español; los nombres que debes escribir en Moodle están en inglés, entre comillas o en `código`.

## 0. Antes de empezar

1. Confirma que no existe un curso con nombre corto `TDTF-CA-EN`. Si existe, detente y pregunta.
2. Confirma en *Administración del sitio > Extensiones > Resumen de extensiones* que existen **Certificado personalizado** y **Level Up**.
3. Si el sitio todavía no tiene actividades H5P, la primera que subas instala sus librerías: súbela con la cuenta de administración. Si aparece un error de librerías, detente y reporta el mensaje exacto.

## 1. Crear el curso

*Administración del sitio > Cursos > Agregar un nuevo curso*:

| Campo | Valor |
|---|---|
| Nombre | Your Money, Your Family, Your Future (California pilot) |
| Nombre corto | TDTF-CA-EN |
| Visibilidad | **Ocultar** |
| Idioma forzado | Inglés, solo si el paquete de idioma inglés está instalado; si no, déjalo sin forzar |
| Formato | Temas, 7 secciones |
| Seguimiento de finalización | Sí |

## 2. Secciones

| Sección | Nombre | Descripción |
|---|---|---|
| General | Welcome | Enlace al capítulo 1 del libro de apoyo y foro "Questions and comments" |
| 1 | Module 1. Understand your money and organize your finances | contenido de `1_books/M1_summary.html` |
| 2 | Module 2. Understand the financial system and plan your remittances | `M2_summary.html` |
| 3 | Module 3. Build your credit and manage your debts | `M3_summary.html` |
| 4 | Module 4. Protect your money, your identity and your family | `M4_summary.html` |
| 5 | Module 5. Build wealth and prepare your future | `M5_summary.html` |
| 6 | Support materials | "Cases, practice, glossary and where to get help." |
| 7 | Assessment and certificate | "Your certificate of completion." |

Descripción del foro "Questions and comments": "Don't share account numbers, SSN, ITIN, passwords or your immigration status."

## 3. Libros de lecciones (M1 a M5)

En cada sección de módulo:

1. Crea un libro:
   - Nombre: `Module N Lessons`.
   - Formato de capítulo: Nada.
   - Finalización: Ver.
2. Menú del libro > **Importar capítulo** > `1_books/MN_book_Moodle.zip`, tipo "Cada archivo HTML representa un capítulo".
3. Comprueba las páginas. En cada lección, la portada va primero y sus 3 subcapítulos sangrados debajo.

   | Módulo | Capítulos | Páginas |
   |---|---|---|
   | M1 | 14 | 56 |
   | M2 | 13 | 52 |
   | M3 | 10 | 40 |
   | M4 | 11 | 44 |
   | M5 | 11 | 44 |

## 4. Libro de apoyo

En la sección 6, crea el libro `Support materials` con la misma configuración e importa `1_books/Support_book_Moodle.zip` (6 capítulos).

En la sección General, agrega una **URL** o etiqueta que apunte al capítulo 1 ("Welcome") de este libro.

## 5. Glosario

En la sección 6, crea el glosario `Course key words` e importa `3_glossary/Course_glossary_Moodle.xml`, con destino "glosario actual".

## 6. Banco de preguntas y autoevaluaciones

1. *Administración del curso > Banco de preguntas > Importar*: formato GIFT, archivo `4_questions/question_bank_v3_en.gift.txt`.
   - Se crean las categorías *Your Money v3/M1* a *M5*, con 177 preguntas.
2. En cada sección de módulo, crea el cuestionario `Module N Self-assessment`:
   - Calificación aprobatoria: 70.
   - Intentos: ilimitados.
   - Método: calificación más alta.
   - Ordenar al azar las respuestas: sí.
   - Revisión: después del intento, mostrar si fue correcta, la retroalimentación y la respuesta correcta.
   - Finalización: "Requiere calificación aprobatoria".
3. Agrega **todas** las preguntas de *Your Money v3/MN*, 10 por página:

   | Módulo | Preguntas |
   |---|---|
   | M1 | 42 |
   | M2 | 39 |
   | M3 | 30 |
   | M4 | 33 |
   | M5 | 33 |

## 7. Actividades H5P (59)

Los archivos están en `2_h5p/MN/`, en orden. En cada sección de módulo, **después del libro** y en orden de lección:

1. *Agregar actividad > Actividad H5P*.
2. Nombre: `MN UYY · What would you do?`. Por ejemplo: `M1 U01 · What would you do?`.
3. Sube `MN_UYY_what_would_you_do.h5p`.
4. Opciones de H5P: permitir descarga no; botón de incrustar no; botón de derechos de autor sí.
5. Calificación: seguimiento de intentos sí; método "calificación más alta".
6. Finalización: "El estudiante debe recibir una calificación".

**Orden final de cada sección:** libro, H5P de sus lecciones en orden, autoevaluación.

**Comprueba:** abre 3 actividades al azar con *Cambiar rol a > Estudiante*. Debes ver 3 casos en inglés, 3 opciones por caso y la calificación al terminar.

## 8. Level Up

Agrega el bloque Level Up al curso y sigue la sección 2 de `7_guides/gamification_guide_v3.md`: reglas, 6 niveles con sus nombres en inglés y clasificación anónima.

## 9. Insignias

Sigue la sección 3 de la guía con las 8 imágenes de `5_badges/`. Crea cada insignia con su nombre y descripción en inglés, y actívalas al final.

## 10. Finalización del curso y constancia

1. Configura la **Finalización del curso** con las 5 autoevaluaciones (sección 4 de la guía).
2. En la sección 7 crea el **Certificado personalizado** "Certificate of Completion" según la sección 5 de la guía, con `6_certificate/certificate_background.png`.
3. Revisa la vista previa en PDF y compárala con `certificate_sample.png`.

## 11. Revisión final (con rol de estudiante)

- M1 U01: la portada aparece primero, con los dos botones de ruta; los términos en color muestran su significado.
- La página *Practice* describe "What would you do?" y su quiz tiene 3 opciones.
- La H5P de M1 U01 funciona y registra la calificación.
- La autoevaluación de M1 muestra 3 opciones por pregunta.
- El libro de apoyo muestra "See the key" en los casos integradores.
- No aparece texto en español en el contenido, salvo los nombres propios de México (AFORE, CURP, matrícula consular) y los términos en español entre paréntesis del glosario, que son intencionales.

## 12. Reporte para la persona

Incluye el enlace del curso, el número de páginas de cada libro, las H5P subidas por módulo, las preguntas por autoevaluación, las insignias creadas, la configuración de Level Up, si la constancia quedó lista, todo lo que no pudiste hacer y por qué, y capturas de: una portada de lección, una H5P, una autoevaluación y la vista previa de la constancia.

El curso queda **oculto**. La persona decide cuándo mostrarlo.
