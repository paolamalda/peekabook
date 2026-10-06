# Guía de actividades, puntos, insignias y constancia · Tu Autonomía, Tu Dinero, Tu Futuro

Esta guía es para Moodle 4.5 con Level Up (block_xp) y el complemento Certificado personalizado (mod_customcert).

El objetivo es motivar sin competir. Los puntos premian avanzar, no la calificación perfecta. Nunca se muestra el nombre de nadie en una tabla.

## 1. Qué hay en cada parte

| Actividad | Cuántas | Finalización |
|---|---|---|
| Libro por lección (con la práctica incrustada) | 24 | Ver |
| Cuestionario "Autoevaluación del Módulo N" | 1 por parte (8) | Calificación aprobatoria de 70% |

**Las autoevaluaciones:** usan el banco de 72 preguntas con tres opciones y retroalimentación, en las categorías *Tu Autonomía v0.1/M1* a *M8*. Calificación aprobatoria de 70%, intentos ilimitados, respuestas en orden aleatorio y revisión con respuesta correcta y retroalimentación al terminar.

## 2. Level Up: niveles y puntos

**Reglas** (*Level Up > Reglas*):

1. Quita o pon en 0 las reglas predeterminadas.
2. **Por completar cualquier actividad:** 25 puntos, con el evento "Se ha actualizado la finalización de un módulo del curso" (`\core\event\course_module_completion_updated`).
3. **Por participar en el foro:** 5 puntos, con el evento "Mensaje creado" (`\mod_forum\event\post_created`).
4. Deja activada la protección contra trampas.

Completar todo el curso da unos 800 puntos:

| Actividades | Cuántas | Puntos |
|---|---|---|
| Lecciones | 24 | 600 |
| Autoevaluaciones | 8 | 200 |
| **Total** | 32 | **800** |

**Niveles** (6 niveles, sin algoritmo automático):

| Nivel | Nombre | Puntos | Cuándo se alcanza, más o menos |
|---|---|---|---|
| 1 | Empiezo | 0 | Al entrar |
| 2 | Me organizo | 100 | Durante el Módulo 2 |
| 3 | Avanzo | 200 | Durante el Módulo 3 |
| 4 | Me protejo | 350 | Durante el Módulo 5 |
| 5 | Planeo | 450 | Durante el Módulo 7 |
| 6 | Lo logré | 550 | Durante el Módulo 8 |

**Clasificación (ranking): desactivada.** En *Level Up > Clasificación* elige no mostrarla, y quita o esconde el bloque de tabla de posiciones. Cada persona ve solo sus puntos, su nivel y sus insignias.

## 3. Insignias

*Más > Insignias > Agregar una nueva insignia*. Imágenes en `5_insignias/`. Emisor: Desarrolla Talento. Vencimiento: nunca. Los nombres llevan el curso para que no se repitan en la plataforma: úsalos tal cual.

| Imagen | Insignia | Criterio (finalización de actividad, con aprobación) | Descripción |
|---|---|---|---|
| 01_a_mi_nombre.png | A mi nombre · Tu Autonomía | Autoevaluación del Módulo 1 completada (aprobada) | Una cuenta, tus documentos y un ingreso propio a tu nombre. |
| 02_mi_trabajo_cuenta.png | Mi trabajo cuenta · Tu Autonomía | Autoevaluación del Módulo 2 completada (aprobada) | Tu presupuesto del hogar con tu trabajo de cuidados contado y acuerdos de dinero claros. |
| 03_mi_retiro.png | Mi retiro · Tu Autonomía | Autoevaluaciones de los módulos 3 y 4 | Tu Afore localizada, tus semanas revisadas y tu primera aportación voluntaria. Tu registro o el de una mujer cercana a la Pensión Mujeres Bienestar, y un plan para usarla. |
| 04_protegida.png | Protegida · Tu Autonomía | Autoevaluación del Módulo 5 completada (aprobada) | Tus seguros revisados y tu decisión sobre un seguro para ti. |
| 05_mi_dinero_es_mio.png | Mi dinero es mío · Tu Autonomía | Autoevaluación del Módulo 6 completada (aprobada) | Las señales de violencia económica y tu plan de seguridad económica. |
| 06_derechos_de_mis_hijos.png | Derechos de mis hijos · Tu Autonomía | Autoevaluación del Módulo 7 completada (aprobada) | Tus pasos para pedir, cobrar y administrar la pensión alimenticia. |
| 07_en_calma.png | En calma · Tu Autonomía | Autoevaluación del Módulo 8 completada (aprobada) | Tus tres pasos pequeños para bajar el estrés por dinero y tu plan de autonomía. |
| 08_plan_completo.png | Plan completo · Tu Autonomía | Finalización del curso | Concluiste los 8 módulos del programa. |

Al terminar, **activa** cada insignia.

## 4. Finalización del curso

*Más > Finalización del curso*: condición de finalización de actividades con **todas** las 8 autoevaluaciones. Opcional: los 8 libros.

## 5. Constancia de conclusión (Certificado personalizado)

1. En la sección "Evaluación y constancia", agrega **Certificado personalizado** con la **plantilla estándar de la plataforma** (sin imagen de fondo): nombre "Constancia de conclusión".
2. **Restringir acceso:** una condición de "Finalización de actividad" por cada una de las 8 autoevaluaciones, "debe estar completa con calificación aprobatoria", y la **Encuesta final** enviada.
3. En la plantilla cambia solo estos datos (también están en `6_constancia/constancia.md`):

   | Campo | Texto |
   |---|---|
   | Título del curso | Tu Autonomía, Tu Dinero, Tu Futuro |
   | Línea | por concluir el programa de bienestar financiero Tu Autonomía, Tu Dinero, Tu Futuro |
   | Tema 1 | Dinero a mi nombre |
   | Tema 2 | Trabajo de cuidados |
   | Tema 3 | Afore y pensión |
   | Tema 4 | Violencia económica |
   | Tema 5 | Estrés y salud |

4. Revisa la **Vista previa en PDF** y activa "Verificar certificado".

Si Certificado personalizado no está instalado, la insignia **Plan completo · Tu Autonomía** funciona como constancia digital.

## 6. Qué no hacer

- No dar puntos por ver páginas.
- No publicar nombres en rankings.
- No pedir datos reales para aprobar.
- No ligar insignias ni constancia a contratar servicios o productos.
