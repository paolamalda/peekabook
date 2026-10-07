# Guía de actividades, puntos, insignias y constancia · Tu Dinero, Tu Familia, Tu Futuro

Esta guía es para Moodle 4.5 con Level Up (block_xp) y el complemento Certificado personalizado (mod_customcert).

El objetivo es motivar sin competir. Los puntos premian avanzar, no la calificación perfecta. Nunca se muestra el nombre de nadie en una tabla.

## 1. Qué hay en cada parte

| Actividad | Cuántas | Finalización |
|---|---|---|
| Libro por lección (con la práctica incrustada) | 63 | Ver |
| Cuestionario "Autoevaluación del Módulo N" | 1 por parte (5) | Calificación aprobatoria de 70% |

**Las autoevaluaciones:** usan el banco de 189 preguntas con tres opciones y retroalimentación, en las categorías *Tu Dinero v1.0/M1* a *M5*. Calificación aprobatoria de 70%, intentos ilimitados, respuestas en orden aleatorio y revisión con respuesta correcta y retroalimentación al terminar.

## 2. Level Up: niveles y puntos

**Reglas** (*Level Up > Reglas*):

1. Quita o pon en 0 las reglas predeterminadas.
2. **Por completar cualquier actividad:** 25 puntos, con el evento "Se ha actualizado la finalización de un módulo del curso" (`\core\event\course_module_completion_updated`).
3. **Por participar en el foro:** 5 puntos, con el evento "Mensaje creado" (`\mod_forum\event\post_created`).
4. Deja activada la protección contra trampas.

Completar todo el curso da unos 1,700 puntos:

| Actividades | Cuántas | Puntos |
|---|---|---|
| Lecciones | 63 | 1,575 |
| Autoevaluaciones | 5 | 125 |
| **Total** | 68 | **1,700** |

**Niveles** (6 niveles, sin algoritmo automático):

| Nivel | Nombre | Puntos | Cuándo se alcanza, más o menos |
|---|---|---|---|
| 1 | Empiezo | 0 | Al entrar |
| 2 | Me organizo | 150 | A mitad del Módulo 1 |
| 3 | Uso mi cuenta | 450 | Durante el Módulo 2 |
| 4 | Cuido mi crédito | 800 | Durante el Módulo 3 |
| 5 | Protejo a mi familia | 1,150 | Durante el Módulo 4 |
| 6 | Construyo mi futuro | 1,500 | Durante el Módulo 5 |

**Clasificación (ranking): desactivada.** En *Level Up > Clasificación* elige no mostrarla, y quita o esconde el bloque de tabla de posiciones. Cada persona ve solo sus puntos, su nivel y sus insignias.

## 3. Insignias

*Más > Insignias > Agregar una nueva insignia*. Imágenes en `5_insignias/`. Emisor: Desarrolla Talento. Vencimiento: nunca. Los nombres llevan el curso para que no se repitan en la plataforma: úsalos tal cual.

| Imagen | Insignia | Criterio (finalización de actividad, con aprobación) | Descripción |
|---|---|---|---|
| 01_M1_mi_dinero_en_orden.png | Mi dinero en orden · Tu Dinero | Autoevaluación del Módulo 1 completada (aprobada) | Organizaste tu flujo de dinero, tu presupuesto y tus impuestos. 14 lecciones, unas 3 horas. |
| 02_M2_envio_inteligente.png | Envío inteligente · Tu Dinero | Autoevaluación del Módulo 2 | Sabes elegir cuenta, comparar remesas y proteger a tu familia de fraudes. 13 lecciones. |
| 03_M3_credito_con_rumbo.png | Crédito con rumbo · Tu Dinero | Autoevaluación del Módulo 3 | Entiendes tu reporte, comparas préstamos y tienes un plan de deudas. 10 lecciones. |
| 04_M4_familia_protegida.png | Familia protegida · Tu Dinero | Autoevaluación del Módulo 4 | Tienes un plan de protección, seguros y preparación familiar. 11 lecciones. |
| 05_M5_futuro_en_marcha.png | Futuro en marcha · Tu Dinero | Autoevaluación del Módulo 5 | Tus metas, tu retiro y tu plan de una página están escritos. 11 lecciones. |
| 06_detective_de_estafas.png | Detective de estafas · Tu Dinero | H5P de M2 U11, M4 U01 y M4 U02 completados | Reconoces las señales de fraude y verificas antes de actuar. |
| 07_comparador_experto.png | Comparador experto · Tu Dinero | H5P de M2 U08, M3 U05 y M5 U05 completados | Comparas con el costo total, no solo con el precio anunciado. |
| 08_plan_completo.png | Plan completo · Tu Dinero | Finalización del curso | Concluiste los cinco módulos del programa. |

Al terminar, **activa** cada insignia.

## 4. Finalización del curso

*Más > Finalización del curso*: condición de finalización de actividades con **todas** las 5 autoevaluaciones. Opcional: los 5 libros.

## 5. Constancia de conclusión (Certificado personalizado)

1. En la sección "Evaluación y constancia", agrega **Certificado personalizado** con la **plantilla estándar de la plataforma** (sin imagen de fondo): nombre "Constancia de conclusión".
2. **Restringir acceso:** una condición de "Finalización de actividad" por cada una de las 5 autoevaluaciones, "debe estar completa con calificación aprobatoria", y la **Encuesta final** enviada.
3. En la plantilla cambia solo estos datos (también están en `6_constancia/constancia.md`):

   | Campo | Texto |
   |---|---|
   | Título del curso | Tu Dinero, Tu Familia, Tu Futuro |
   | Línea | por concluir el programa de bienestar financiero Tu Dinero, Tu Familia, Tu Futuro |
   | Tema 1 | Mi dinero |
   | Tema 2 | Sistema y remesas |
   | Tema 3 | Crédito y deudas |
   | Tema 4 | Protección |
   | Tema 5 | Futuro y patrimonio |

4. Revisa la **Vista previa en PDF** y activa "Verificar certificado".

Si Certificado personalizado no está instalado, la insignia **Plan completo · Tu Dinero** funciona como constancia digital.

## 6. Qué no hacer

- No dar puntos por ver páginas.
- No publicar nombres en rankings.
- No pedir datos reales para aprobar.
- No ligar insignias ni constancia a contratar servicios o productos.
