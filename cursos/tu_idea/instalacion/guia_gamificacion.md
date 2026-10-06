# Guía de actividades, puntos, insignias y constancia · Tu Idea, Tu Dinero, Tu Futuro

Esta guía es para Moodle 4.5 con Level Up (block_xp) y el complemento Certificado personalizado (mod_customcert).

El objetivo es motivar sin competir. Los puntos premian avanzar, no la calificación perfecta. Nunca se muestra el nombre de nadie en una tabla.

## 1. Qué hay en cada módulo

| Actividad | Cuántas | Finalización |
|---|---|---|
| Libro "Lecciones del Módulo N" | 1 por módulo (9) | Ver |
| Actividad H5P "MN UYY · ¿Qué harías?" | 1 por lección (37) | Recibir calificación |
| Cuestionario "Autoevaluación del Módulo N" | 1 por módulo (9) | Calificación aprobatoria de 70% |

**Configuración de cada actividad H5P:** sin botón de descarga, con botón de derechos de autor e incrustar desactivado; seguimiento de intentos con "Calificación más alta"; finalización "El estudiante debe recibir una calificación".

**Las autoevaluaciones:** usan el banco de 111 preguntas con tres opciones y retroalimentación, en las categorías *Tu Idea v1.0/M1* a *M9*. Calificación aprobatoria de 70%, intentos ilimitados, respuestas en orden aleatorio y revisión con respuesta correcta y retroalimentación al terminar.

## 2. Level Up: niveles y puntos

**Reglas** (*Level Up > Reglas*):

1. Quita o pon en 0 las reglas predeterminadas.
2. **Por completar cualquier actividad:** 25 puntos, con el evento "Se ha actualizado la finalización de un módulo del curso" (`\core\event\course_module_completion_updated`).
3. **Por participar en el foro:** 5 puntos, con el evento "Mensaje creado" (`\mod_forum\event\post_created`).
4. Deja activada la protección contra trampas.

Completar todo el curso da unos 1,375 puntos:

| Actividades | Cuántas | Puntos |
|---|---|---|
| Actividades H5P | 37 | 925 |
| Libros | 9 | 225 |
| Autoevaluaciones | 9 | 225 |
| **Total** | 55 | **1,375** |

**Niveles** (6 niveles, sin algoritmo automático):

| Nivel | Nombre | Puntos | Cuándo se alcanza, más o menos |
|---|---|---|---|
| 1 | Primer paso | 0 | Al entrar |
| 2 | Con idea | 150 | Durante el Módulo 2 |
| 3 | Primera venta | 350 | Durante el Módulo 4 |
| 4 | En crecimiento | 600 | Durante el Módulo 5 |
| 5 | Con cabeza | 800 | Durante el Módulo 7 |
| 6 | Con futuro | 1,000 | Durante el Módulo 9 |

**Clasificación:** anonimato activado; mostrar solo vecinos cercanos o desactivarla.

## 3. Insignias

*Más > Insignias > Agregar una nueva insignia*. Imágenes en `5_insignias/`. Emisor: Desarrolla Talento. Vencimiento: nunca. Los nombres llevan el curso para que no se repitan en la plataforma: úsalos tal cual.

| Imagen | Insignia | Criterio (finalización de actividad, con aprobación) | Descripción |
|---|---|---|---|
| 01_mente_que_crea.png | Mente que crea · Tu Idea | Autoevaluaciones de los Módulos 1 y 2 | Piensas en crear, tienes presupuesto y usas el dinero digital con seguridad. |
| 02_primera_venta.png | Primera venta · Tu Idea | Autoevaluación del Módulo 3 | Probaste una idea con costo, precio y ganancia. |
| 03_negocio_en_marcha.png | Negocio en marcha · Tu Idea | Autoevaluación del Módulo 4 | Sabes reinvertir, trabajar con socios y cuidar tu marca. |
| 04_dinero_que_trabaja.png | Dinero que trabaja · Tu Idea | Autoevaluación del Módulo 5 | Tu dinero trabaja y distingues invertir de apostar. |
| 05_credito_con_cabeza.png | Crédito con cabeza · Tu Idea | Autoevaluación del Módulo 6 | Sabes cuánto cuesta un crédito y cómo cuidar tu historial. |
| 06_nadie_me_engana.png | Nadie me engaña · Tu Idea | Autoevaluación del Módulo 7 | Tienes tu seguro de estudiante y reconoces fraudes y cuentas mula. |
| 07_entiendo_el_sistema.png | Entiendo el sistema · Tu Idea | Autoevaluación del Módulo 8 | Entiendes el sistema, los impuestos, la economía y los papeles de tu familia. |
| 08_plan_completo.png | Plan completo · Tu Idea | Finalización del curso | Concluiste los nueve módulos del programa. |

Al terminar, **activa** cada insignia.

## 4. Finalización del curso

*Más > Finalización del curso*: condición de finalización de actividades con **todas** las 9 autoevaluaciones. Opcional: los 9 libros.

## 5. Constancia de conclusión (Certificado personalizado)

1. En la sección "Evaluación y constancia", agrega **Certificado personalizado** con la **plantilla estándar de la plataforma** (sin imagen de fondo): nombre "Constancia de conclusión".
2. **Restringir acceso:** una condición de "Finalización de actividad" por cada una de las 9 autoevaluaciones, "debe estar completa con calificación aprobatoria", y la **Encuesta final** enviada.
3. En la plantilla cambia solo estos datos (también están en `6_constancia/constancia.md`):

   | Campo | Texto |
   |---|---|
   | Título del curso | Tu Idea, Tu Dinero, Tu Futuro |
   | Línea | por concluir el programa de bienestar financiero Tu Idea, Tu Dinero, Tu Futuro |
   | Tema 1 | Mente y dinero digital |
   | Tema 2 | Crear y crecer |
   | Tema 3 | Invertir y crédito |
   | Tema 4 | Riesgos y sistema |
   | Tema 5 | Futuro y plan |

4. Revisa la **Vista previa en PDF** y activa "Verificar certificado".

Si Certificado personalizado no está instalado, la insignia **Plan completo · Tu Idea** funciona como constancia digital.

## 6. Qué no hacer

- No dar puntos por ver páginas.
- No publicar nombres en rankings.
- No pedir datos reales para aprobar.
- No ligar insignias ni constancia a contratar servicios o productos.
