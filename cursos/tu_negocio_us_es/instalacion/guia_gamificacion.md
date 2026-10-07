# Guía de actividades, puntos, insignias y constancia · Tu Negocio, Tu Dinero, Tu Futuro · EE. UU.

Esta guía es para Moodle 4.5 con Level Up (block_xp) y el complemento Certificado personalizado (mod_customcert).

El objetivo es motivar sin competir. Los puntos premian avanzar, no la calificación perfecta. Nunca se muestra el nombre de nadie en una tabla.

## 1. Qué hay en cada parte

| Actividad | Cuántas | Finalización |
|---|---|---|
| Libro por lección (con la práctica incrustada) | 45 | Ver |
| Cuestionario "Autoevaluación del Módulo N" | 1 por parte (9) | Calificación aprobatoria de 70% |

**Las autoevaluaciones:** usan el banco de 135 preguntas con tres opciones y retroalimentación, en las categorías *Tu Negocio US ES v1.0/M1* a *M9*. Calificación aprobatoria de 70%, intentos ilimitados, respuestas en orden aleatorio y revisión con respuesta correcta y retroalimentación al terminar.

## 2. Level Up: niveles y puntos

**Reglas** (*Level Up > Reglas*):

1. Quita o pon en 0 las reglas predeterminadas.
2. **Por completar cualquier actividad:** 25 puntos, con el evento "Se ha actualizado la finalización de un módulo del curso" (`\core\event\course_module_completion_updated`).
3. **Por participar en el foro:** 5 puntos, con el evento "Mensaje creado" (`\mod_forum\event\post_created`).
4. Deja activada la protección contra trampas.

Completar todo el curso da unos 1,350 puntos:

| Actividades | Cuántas | Puntos |
|---|---|---|
| Lecciones | 45 | 1,125 |
| Autoevaluaciones | 9 | 225 |
| **Total** | 54 | **1,350** |

**Niveles** (6 niveles, sin algoritmo automático):

| Nivel | Nombre | Puntos | Cuándo se alcanza, más o menos |
|---|---|---|---|
| 1 | Idea | 0 | Al entrar |
| 2 | Arranque | 200 | Durante el Módulo 2 |
| 3 | En marcha | 400 | Durante el Módulo 4 |
| 4 | Formal | 650 | Durante el Módulo 5 |
| 5 | En crecimiento | 900 | Durante el Módulo 7 |
| 6 | Consolidado | 1,100 | Durante el Módulo 9 |

**Clasificación (ranking): desactivada.** En *Level Up > Clasificación* elige no mostrarla, y quita o esconde el bloque de tabla de posiciones. Cada persona ve solo sus puntos, su nivel y sus insignias.

## 3. Insignias

*Más > Insignias > Agregar una nueva insignia*. Imágenes en `5_insignias/`. Emisor: Desarrolla Talento. Vencimiento: nunca. Los nombres llevan el curso para que no se repitan en la plataforma: úsalos tal cual.

| Imagen | Insignia | Criterio (finalización de actividad, con aprobación) | Descripción |
|---|---|---|---|
| 01_dinero_separado.png | Dinero separado · Tu Negocio US ES | Autoevaluación del Módulo 1 | Separaste el dinero del negocio y de tu casa y te pagas un sueldo. |
| 02_precio_justo.png | Precio justo · Tu Negocio US ES | Autoevaluación del Módulo 2 | Conoces tus costos, tu margen y tu punto de equilibrio. |
| 03_flujo_bajo_control.png | Flujo bajo control · Tu Negocio US ES | Autoevaluaciones de los Módulos 3 y 4 | Controlas tu flujo, tu fiado y tus formas de cobro sin perder. |
| 04_negocio_formal.png | Negocio formal · Tu Negocio US ES | Autoevaluación del Módulo 5 | Tienes tu estructura, tus números, permisos e impuestos en orden. |
| 05_credito_inteligente.png | Crédito inteligente · Tu Negocio US ES | Autoevaluación del Módulo 6 | Sabes si necesitas crédito y cuánto cuesta de verdad. |
| 06_negocio_protegido.png | Negocio protegido · Tu Negocio US ES | Autoevaluación del Módulo 7 | Protegiste tu salud, tu negocio y tu marca, y te cuidas de fraudes. |
| 07_crecer_con_orden.png | Crecer con orden · Tu Negocio US ES | Autoevaluaciones de los Módulos 8 y 9 | Creces con orden y tienes tu plan de una página. |
| 08_plan_completo.png | Plan completo · Tu Negocio US ES | Finalización del curso | Concluiste los nueve módulos del programa. |

Al terminar, **activa** cada insignia.

## 4. Finalización del curso

*Más > Finalización del curso*: condición de finalización de actividades con **todas** las 9 autoevaluaciones. Opcional: los 9 libros.

## 5. Constancia de conclusión (Certificado personalizado)

1. En la sección "Evaluación y constancia", agrega **Certificado personalizado** con la **plantilla estándar de la plataforma** (sin imagen de fondo): nombre "Constancia de conclusión".
2. **Restringir acceso:** una condición de "Finalización de actividad" por cada una de las 9 autoevaluaciones, "debe estar completa con calificación aprobatoria", y la **Encuesta final** enviada.
3. En la plantilla cambia solo estos datos (también están en `6_constancia/constancia.md`):

   | Campo | Texto |
   |---|---|
   | Título del curso | Tu Negocio, Tu Dinero, Tu Futuro · EE. UU. |
   | Línea | por concluir el programa de bienestar financiero Tu Negocio, Tu Dinero, Tu Futuro · EE. UU. |
   | Tema 1 | Dinero separado |
   | Tema 2 | Precio y flujo |
   | Tema 3 | Impuestos y formalidad |
   | Tema 4 | Crédito y protección |
   | Tema 5 | Crecer y futuro |

4. Revisa la **Vista previa en PDF** y activa "Verificar certificado".

Si Certificado personalizado no está instalado, la insignia **Plan completo · Tu Negocio US ES** funciona como constancia digital.

## 6. Qué no hacer

- No dar puntos por ver páginas.
- No publicar nombres en rankings.
- No pedir datos reales para aprobar.
- No ligar insignias ni constancia a contratar servicios o productos.
