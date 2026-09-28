# Instrucciones para Claude: actualizar el curso que ya está en Moodle

Vas a actualizar el curso "Tu Dinero, Tu Familia, Tu Futuro" que la persona ya subió a academia.desarrollatalento.com. El sitio usa Moodle 3.10, el tema Boost y Level Up 3.15.2.

Trabaja con el navegador y con la sesión de administrador que la persona abrió.

Reglas:

- Usa solo la interfaz web.
- No uses SSH.
- No instales complementos.
- No cambies la configuración del sitio.
- No toques otros cursos.
- Si algo no coincide con estas instrucciones, detente y pregunta.

## 0. Antes de empezar

1. Pide a la persona la URL del curso.
2. Confirma que hay un respaldo reciente.
   - Si no lo hay, haz uno en *Administración del curso > Respaldo*, sin datos de usuarios, y descárgalo.
3. Revisa *Participantes* y anota cuántas personas con rol de estudiante hay.
   - Si hay estudiantes con avance, avisa antes del paso 1: reemplazar un libro borra su marca de "visto".
4. Revisa *Administración del sitio > Extensiones > Resumen de extensiones*:
   - si existe **Certificado personalizado** (mod_customcert);
   - si existe el bloque **Level Up** (block_xp);
   - si Level Up es la versión gratuita o Level Up+.
5. Anota la **estructura actual**: secciones, libros, cuántas páginas tiene cada libro, cuestionarios y categorías del banco de preguntas. Esa lista va en tu reporte.

Nota: la persona ya corrigió el orden de los capítulos (portadas `_0.html`). Los zips de este paquete ya traen esa corrección.

## 1. Reemplazar los libros de lecciones (M1 a M5)

Los libros nuevos cambian el recuadro "Actividad interactiva" de cada lección para que describa la actividad H5P "¿Qué harías?". El resto del contenido es igual.

Importar capítulos **agrega** páginas, no las reemplaza. Por eso, en cada módulo:

1. Anota el nombre, la descripción y la configuración del libro actual "Lecciones del Módulo N". Luego bórralo.
2. En la misma sección, crea un libro nuevo:
   - Nombre: `Lecciones del Módulo N`.
   - Formato de capítulo: Nada.
   - Finalización: Ver.
3. Menú del libro > **Importar capítulo** > `1_libros/MN_libro_Moodle.zip`, tipo "Cada archivo HTML representa un capítulo".
4. Comprueba las páginas. En cada lección, la portada debe ir primero y sus 3 subcapítulos sangrados debajo.

   | Módulo | Capítulos | Páginas |
   |---|---|---|
   | M1 | 14 | 56 |
   | M2 | 13 | 52 |
   | M3 | 10 | 40 |
   | M4 | 11 | 44 |
   | M5 | 11 | 44 |

5. Deja el libro como **primera actividad** de su sección.

## 2. Reemplazar el libro de apoyo

1. Borra el libro "Materiales de apoyo".
2. Créalo de nuevo con la misma configuración.
3. Importa `1_libros/Apoyo_libro_Moodle.zip`: son 6 capítulos con el diseño nuevo.

Si la sección General no tiene un enlace a la Bienvenida, agrégalo: una **URL** o una etiqueta que apunte al capítulo 1 de este libro.

## 3. Glosario

Si ya existe "Palabras clave del curso", no lo toques.

Si no existe:

1. Créalo en la sección 6.
2. Importa `3_glosario/Glosario_curso_Moodle.xml`, con destino "glosario actual".

## 4. Banco de preguntas y autoevaluaciones

1. *Administración del curso > Banco de preguntas > Importar*: formato GIFT, archivo `4_preguntas/banco_preguntas_v3_es.gift.txt`.
   - Se crean las categorías *Tu Dinero v3/M1* a *M5*, con 177 preguntas.
2. En cada sección de módulo, deja un cuestionario llamado `Autoevaluación del Módulo N`.
   - Si ya existe, quítale todas las preguntas viejas.
   - Si no existe, créalo.

   Configuración:

   - Calificación aprobatoria: 70.
   - Intentos: ilimitados.
   - Método: calificación más alta.
   - Ordenar al azar las respuestas: sí.
   - Revisión: después del intento, mostrar si fue correcta, la retroalimentación y la respuesta correcta.
   - Finalización: "Requiere calificación aprobatoria".
3. Agrega **todas** las preguntas de la categoría *Tu Dinero v3/MN*:

   | Módulo | Preguntas |
   |---|---|
   | M1 | 42 |
   | M2 | 39 |
   | M3 | 30 |
   | M4 | 33 |
   | M5 | 33 |

   Pon 10 preguntas por página.
4. La autoevaluación va al **final** de su sección.
5. **No borres** la categoría vieja "Tu Dinero" si algún cuestionario tiene intentos. Si no tiene intentos, puedes borrarla.

## 5. Actividades H5P (59)

Los archivos están en `2_h5p/MN/`, en orden. Cada archivo trae sus librerías.

La **primera** carga las instala en el sitio y necesita la cuenta de administrador. Si al subir la primera aparece un error de librerías, detente y reporta el mensaje exacto.

En cada sección de módulo, **después del libro** y en orden de lección:

1. *Agregar actividad > Actividad H5P*.
2. Nombre: `MN UYY · ¿Qué harías?`. Por ejemplo: `M1 U01 · ¿Qué harías?`.
3. Sube `MN_UYY_que_harias.h5p`.
4. Opciones de H5P:
   - Permitir descarga: no.
   - Botón de incrustar: no.
   - Botón de derechos de autor: sí.
5. Calificación:
   - Habilitar seguimiento de intentos: sí.
   - Método de calificación: calificación más alta.
6. Finalización: "El estudiante debe recibir una calificación".

**Comprueba:** abre 3 actividades al azar con *Cambiar rol a > Estudiante*. Debes ver 3 casos, 3 opciones por caso y la calificación al terminar.

## 6. Level Up

Sigue la sección 2 de `7_guias/guia_gamificacion_v3.md`: reglas, 6 niveles y clasificación anónima.

- Si Level Up no está en el curso, agrega el bloque.
- Si Level Up no existe en el sitio, sáltate este paso y repórtalo.

## 7. Insignias

Sigue la sección 3 de la guía y usa las 8 imágenes de `5_insignias/`.

- Crea cada insignia con su criterio.
- Actívalas al final.
- Si ya existen insignias con los mismos nombres, no las dupliques: actualiza su imagen y descripción, si no se han entregado.

## 8. Finalización del curso y constancia

1. Configura la **Finalización del curso** con las 5 autoevaluaciones (sección 4 de la guía).
2. Si **Certificado personalizado** está instalado:
   - crea "Constancia de conclusión" en la sección "Evaluación y constancia", según la sección 5 de la guía, con `6_certificado/certificado_fondo.png`;
   - revisa la vista previa en PDF y compárala con `certificado_muestra.png`.
3. Si **no** está instalado, no lo instales.
   - Deja una etiqueta en esa sección: "Al aprobar las cinco autoevaluaciones recibirás la insignia Plan completo y tu constancia de conclusión".
   - Reporta que falta el complemento.

## 9. Revisión final (con rol de estudiante)

- M1 U01:
  - la portada aparece primero, con los dos botones de ruta;
  - "Lo esencial", "Profundiza" y "Practica" van debajo de su propia lección;
  - los términos en color muestran su significado.
- "Actividad interactiva" en la página *Practica* describe "¿Qué harías?".
- La actividad H5P de M1 U01 funciona y registra la calificación.
- La autoevaluación de M1 muestra 3 opciones por pregunta y retroalimentación.
- El libro de apoyo muestra "Ver la clave" en los casos integradores.

## 10. Reporte para la persona

Incluye:

- Qué reemplazaste, con el número de páginas de cada libro.
- Cuántas actividades H5P subiste por módulo.
- Las preguntas de cada autoevaluación.
- Las insignias creadas y si están activas.
- La configuración de Level Up y si es la versión gratuita o Level Up+.
- Si la constancia quedó configurada o qué falta.
- Todo lo que no pudiste hacer, y por qué.
- Capturas de: una portada de lección, una actividad H5P, una autoevaluación y la vista previa de la constancia.
