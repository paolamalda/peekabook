# Guía de actividades, puntos, insignias y constancia · Tu Regreso, Tu Dinero, Tu Futuro

Esta guía es para Moodle 3.10 con Level Up (block_xp) 3.15.2 y el complemento Certificado personalizado (mod_customcert).

El objetivo es motivar sin competir. Los puntos premian avanzar, no la calificación perfecta. Nunca se muestra el nombre de nadie en una tabla.

## 1. Qué hay en cada parte

| Actividad | Cuántas | Finalización |
|---|---|---|
| Libro por lección (con la práctica incrustada) | 24 | Ver |
| Cuestionario "Autoevaluación del Módulo N" | 1 por parte (8) | Calificación aprobatoria de 70% |

**Las autoevaluaciones:** usan el banco de 72 preguntas con tres opciones y retroalimentación, en las categorías *Tu Regreso v0.1/M1* a *M8*. Calificación aprobatoria de 70%, intentos ilimitados, respuestas en orden aleatorio y revisión con respuesta correcta y retroalimentación al terminar.

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

*Administración del curso > Insignias > Agregar una nueva insignia*. Imágenes en `5_insignias/`. Emisor: Desarrolla Talento. Vencimiento: nunca. Los nombres llevan el curso para que no se repitan en la plataforma: úsalos tal cual.

| Imagen | Insignia | Criterio (finalización de actividad, con aprobación) | Descripción |
|---|---|---|---|
| 01_papeles_en_orden.png | Papeles en orden · Tu Regreso | Autoevaluación del Módulo 1 completada (aprobada) | Tu lista de papeles en orden: constancia, CURP, acta, INE y los de tus hijos. |
| 02_cuenta_a_mi_nombre.png | Cuenta a mi nombre · Tu Regreso | Autoevaluación del Módulo 2 completada (aprobada) | Una cuenta a tu nombre para recibir apoyos y dinero, y tus tarjetas de regreso bien usadas. |
| 03_historial_desde_cero.png | Historial desde cero · Tu Regreso | Autoevaluación del Módulo 3 completada (aprobada) | Tu primer historial de crédito en México, empezando chico y sin trampas. |
| 04_nada_se_queda_alla.png | Nada se queda allá · Tu Regreso | Autoevaluación del Módulo 4 completada (aprobada) | Tu lista de lo que quedó allá: último pago, cuentas, impuestos y retiro. |
| 05_semanas_contadas.png | Semanas contadas · Tu Regreso | Autoevaluación del Módulo 5 completada (aprobada) | Tus semanas cotizadas revisadas y tu Afore localizada. |
| 06_noventa_dias.png | Noventa días · Tu Regreso | Autoevaluación del Módulo 6 completada (aprobada) | Tu presupuesto de regreso para los primeros tres meses. |
| 07_lo_que_se_hacer.png | Lo que sé hacer · Tu Regreso | Autoevaluación del Módulo 7 completada (aprobada) | Tu plan para usar lo que sabes hacer: empleo, oficio o negocio pequeño. |
| 08_plan_completo.png | Plan completo · Tu Regreso | Finalización del curso | Concluiste los 8 módulos del programa. |

Al terminar, **activa** cada insignia.

## 4. Finalización del curso

*Administración del curso > Finalización del curso*: condición de finalización de actividades con **todas** las 8 autoevaluaciones. Opcional: los 8 libros.

## 5. Constancia de conclusión (Certificado personalizado)

1. En la sección "Evaluación y constancia", agrega **Certificado personalizado** con la **plantilla estándar de la plataforma** (sin imagen de fondo): nombre "Constancia de conclusión".
2. **Restringir acceso:** una condición de "Finalización de actividad" por cada una de las 8 autoevaluaciones, "debe estar completa con calificación aprobatoria", y la **Encuesta final** enviada.
3. En la plantilla cambia solo estos datos (también están en `6_constancia/constancia.md`):

   | Campo | Texto |
   |---|---|
   | Título del curso | Tu Regreso, Tu Dinero, Tu Futuro |
   | Línea | por concluir el programa de bienestar financiero Tu Regreso, Tu Dinero, Tu Futuro |
   | Tema 1 | Papeles y cuenta |
   | Tema 2 | Crédito desde cero |
   | Tema 3 | Lo que quedó allá |
   | Tema 4 | Afore y semanas |
   | Tema 5 | Plan de regreso |

4. Revisa la **Vista previa en PDF** y activa "Verificar certificado".

Si Certificado personalizado no está instalado, la insignia **Plan completo · Tu Regreso** funciona como constancia digital.

## 6. Qué no hacer

- No dar puntos por ver páginas.
- No publicar nombres en rankings.
- No pedir datos reales para aprobar.
- No ligar insignias ni constancia a contratar servicios o productos.
