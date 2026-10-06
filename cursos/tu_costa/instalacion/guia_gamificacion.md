# Guía de actividades, puntos, insignias y constancia · Tu Costa, Tu Dinero, Tu Futuro

Esta guía es para Moodle 4.5 con Level Up (block_xp) y el complemento Certificado personalizado (mod_customcert).

El objetivo es motivar sin competir. Los puntos premian avanzar, no la calificación perfecta. Nunca se muestra el nombre de nadie en una tabla.

## 1. Qué hay en cada parte

| Actividad | Cuántas | Finalización |
|---|---|---|
| Libro por lección (con la práctica incrustada) | 16 | Ver |
| Cuestionario "Autoevaluación del Módulo N" | 1 por parte (8) | Calificación aprobatoria de 70% |

**Las autoevaluaciones:** usan el banco de 48 preguntas con tres opciones y retroalimentación, en las categorías *Tu Costa v0.1/M1* a *M8*. Calificación aprobatoria de 70%, intentos ilimitados, respuestas en orden aleatorio y revisión con respuesta correcta y retroalimentación al terminar.

## 2. Level Up: niveles y puntos

**Reglas** (*Level Up > Reglas*):

1. Quita o pon en 0 las reglas predeterminadas.
2. **Por completar cualquier actividad:** 25 puntos, con el evento "Se ha actualizado la finalización de un módulo del curso" (`\core\event\course_module_completion_updated`).
3. **Por participar en el foro:** 5 puntos, con el evento "Mensaje creado" (`\mod_forum\event\post_created`).
4. Deja activada la protección contra trampas.

Completar todo el curso da unos 600 puntos:

| Actividades | Cuántas | Puntos |
|---|---|---|
| Lecciones | 16 | 400 |
| Autoevaluaciones | 8 | 200 |
| **Total** | 24 | **600** |

**Niveles** (6 niveles, sin algoritmo automático):

| Nivel | Nombre | Puntos | Cuándo se alcanza, más o menos |
|---|---|---|---|
| 1 | Empiezo | 0 | Al entrar |
| 2 | Me organizo | 50 | Durante el Módulo 2 |
| 3 | Avanzo | 150 | Durante el Módulo 3 |
| 4 | Me protejo | 200 | Durante el Módulo 5 |
| 5 | Planeo | 300 | Durante el Módulo 7 |
| 6 | Lo logré | 400 | Durante el Módulo 8 |

**Clasificación (ranking): desactivada.** En *Level Up > Clasificación* elige no mostrarla, y quita o esconde el bloque de tabla de posiciones. Cada persona ve solo sus puntos, su nivel y sus insignias.

## 3. Insignias

*Más > Insignias > Agregar una nueva insignia*. Imágenes en `5_insignias/`. Emisor: Desarrolla Talento. Vencimiento: nunca. Los nombres llevan el curso para que no se repitan en la plataforma: úsalos tal cual.

| Imagen | Insignia | Criterio (finalización de actividad, con aprobación) | Descripción |
|---|---|---|---|
| 01_listo_para_la_temporada.png | Listo para la temporada · Tu Costa | Autoevaluaciones de los módulos 1 y 2 | Tu plan de dinero para antes y después de un huracán. Tus documentos importantes protegidos y respaldados. |
| 02_ano_completo.png | Año completo · Tu Costa | Autoevaluación del Módulo 3 completada (aprobada) | Tu calendario de ingresos del año y lo que apartas en temporada buena. |
| 03_casa_protegida.png | Casa protegida · Tu Costa | Autoevaluación del Módulo 4 completada (aprobada) | Tu fondo de emergencia en marcha y tu decisión sobre el seguro de vivienda. |
| 04_credito_claro.png | Crédito claro · Tu Costa | Autoevaluación del Módulo 5 completada (aprobada) | Tu comparación del costo total de cualquier crédito o adelanto. |
| 05_trato_digno.png | Trato digno · Tu Costa | Autoevaluación del Módulo 6 completada (aprobada) | Tu forma de pedir un trato digno y de reclamar con folio. |
| 06_remesa_que_rinde.png | Remesa que rinde · Tu Costa | Autoevaluación del Módulo 7 completada (aprobada) | Tu forma de recibir remesas con menos comisión y con un plan. |
| 07_patrimonio_en_orden.png | Patrimonio en orden · Tu Costa | Autoevaluación del Módulo 8 completada (aprobada) | Tus papeles de casa y terreno en orden y tu decisión sobre la herencia. |
| 08_plan_completo.png | Plan completo · Tu Costa | Finalización del curso | Concluiste los 8 módulos del programa. |

Al terminar, **activa** cada insignia.

## 4. Finalización del curso

*Más > Finalización del curso*: condición de finalización de actividades con **todas** las 8 autoevaluaciones. Opcional: los 8 libros.

## 5. Constancia de conclusión (Certificado personalizado)

1. En la sección "Evaluación y constancia", agrega **Certificado personalizado** con la **plantilla estándar de la plataforma** (sin imagen de fondo): nombre "Constancia de conclusión".
2. **Restringir acceso:** una condición de "Finalización de actividad" por cada una de las 8 autoevaluaciones, "debe estar completa con calificación aprobatoria", y la **Encuesta final** enviada.
3. En la plantilla cambia solo estos datos (también están en `6_constancia/constancia.md`):

   | Campo | Texto |
   |---|---|
   | Título del curso | Tu Costa, Tu Dinero, Tu Futuro |
   | Línea | por concluir el programa de bienestar financiero Tu Costa, Tu Dinero, Tu Futuro |
   | Tema 1 | Plan ante huracanes |
   | Tema 2 | Ingreso de temporada |
   | Tema 3 | Crédito y costo total |
   | Tema 4 | Derechos y reclamos |
   | Tema 5 | Patrimonio |

4. Revisa la **Vista previa en PDF** y activa "Verificar certificado".

Si Certificado personalizado no está instalado, la insignia **Plan completo · Tu Costa** funciona como constancia digital.

## 6. Qué no hacer

- No dar puntos por ver páginas.
- No publicar nombres en rankings.
- No pedir datos reales para aprobar.
- No ligar insignias ni constancia a contratar servicios o productos.
