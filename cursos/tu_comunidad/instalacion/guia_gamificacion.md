# Guía de actividades, puntos, insignias y constancia · Tu Comunidad, Tu Dinero, Tu Futuro

Esta guía es para Moodle 3.10 con Level Up (block_xp) 3.15.2 y el complemento Certificado personalizado (mod_customcert).

El objetivo es motivar sin competir. Los puntos premian avanzar, no la calificación perfecta. Nunca se muestra el nombre de nadie en una tabla.

## 1. Qué hay en cada parte

| Actividad | Cuántas | Finalización |
|---|---|---|
| Libro por lección (con la práctica incrustada) | 14 | Ver |
| Cuestionario "Autoevaluación del Módulo N" | 1 por parte (7) | Calificación aprobatoria de 70% |

**Las autoevaluaciones:** usan el banco de 42 preguntas con tres opciones y retroalimentación, en las categorías *Tu Comunidad v0.1/M1* a *M7*. Calificación aprobatoria de 70%, intentos ilimitados, respuestas en orden aleatorio y revisión con respuesta correcta y retroalimentación al terminar.

## 2. Level Up: niveles y puntos

**Reglas** (*Level Up > Reglas*):

1. Quita o pon en 0 las reglas predeterminadas.
2. **Por completar cualquier actividad:** 25 puntos, con el evento "Se ha actualizado la finalización de un módulo del curso" (`\core\event\course_module_completion_updated`).
3. **Por participar en el foro:** 5 puntos, con el evento "Mensaje creado" (`\mod_forum\event\post_created`).
4. Deja activada la protección contra trampas.

Completar todo el curso da unos 525 puntos:

| Actividades | Cuántas | Puntos |
|---|---|---|
| Lecciones | 14 | 350 |
| Autoevaluaciones | 7 | 175 |
| **Total** | 21 | **525** |

**Niveles** (6 niveles, sin algoritmo automático):

| Nivel | Nombre | Puntos | Cuándo se alcanza, más o menos |
|---|---|---|---|
| 1 | Empiezo | 0 | Al entrar |
| 2 | Me organizo | 50 | Durante el Módulo 2 |
| 3 | Avanzo | 100 | Durante el Módulo 3 |
| 4 | Me protejo | 200 | Durante el Módulo 4 |
| 5 | Planeo | 250 | Durante el Módulo 6 |
| 6 | Lo logré | 350 | Durante el Módulo 7 |

**Clasificación (ranking): desactivada.** En *Level Up > Clasificación* elige no mostrarla, y quita o esconde el bloque de tabla de posiciones. Cada persona ve solo sus puntos, su nivel y sus insignias.

## 3. Insignias

*Administración del curso > Insignias > Agregar una nueva insignia*. Imágenes en `5_insignias/`. Emisor: Desarrolla Talento. Vencimiento: nunca. Los nombres llevan el curso para que no se repitan en la plataforma: úsalos tal cual.

| Imagen | Insignia | Criterio (finalización de actividad, con aprobación) | Descripción |
|---|---|---|---|
| 01_mi_apoyo_completo.png | Mi apoyo completo · Tu Comunidad | Autoevaluación del Módulo 1 completada (aprobada) | Tus apoyos cobrados completos, sin pagar a nadie. |
| 02_cuenta_a_mi_nombre.png | Cuenta a mi nombre · Tu Comunidad | Autoevaluación del Módulo 2 completada (aprobada) | Una cuenta a tu nombre, sobre todo si eres mujer. |
| 03_dinero_que_llega.png | Dinero que llega · Tu Comunidad | Autoevaluación del Módulo 3 completada (aprobada) | Tu dinero recibido y enviado con menos comisión y sin intermediarios. |
| 04_grupo_con_reglas.png | Grupo con reglas · Tu Comunidad | Autoevaluación del Módulo 4 completada (aprobada) | Las reglas escritas de tu grupo de ahorro. |
| 05_no_me_enganan.png | No me engañan · Tu Comunidad | Autoevaluación del Módulo 5 completada (aprobada) | Tu regla para colgar y no instalar apps de préstamo. |
| 06_mi_tierra_en_orden.png | Mi tierra en orden · Tu Comunidad | Autoevaluación del Módulo 6 completada (aprobada) | Tu lista de sucesión hecha y tus beneficiarios al día. |
| 07_familia_protegida.png | Familia protegida · Tu Comunidad | Autoevaluación del Módulo 7 completada (aprobada) | Tu plan para los gastos funerarios sin endeudar a tu familia. |
| 08_plan_completo.png | Plan completo · Tu Comunidad | Finalización del curso | Concluiste los 7 módulos del programa. |

Al terminar, **activa** cada insignia.

## 4. Finalización del curso

*Administración del curso > Finalización del curso*: condición de finalización de actividades con **todas** las 7 autoevaluaciones. Opcional: los 7 libros.

## 5. Constancia de conclusión (Certificado personalizado)

1. En la sección "Evaluación y constancia", agrega **Certificado personalizado** con la **plantilla estándar de la plataforma** (sin imagen de fondo): nombre "Constancia de conclusión".
2. **Restringir acceso:** una condición de "Finalización de actividad" por cada una de las 7 autoevaluaciones, "debe estar completa con calificación aprobatoria", y la **Encuesta final** enviada.
3. En la plantilla cambia solo estos datos (también están en `6_constancia/constancia.md`):

   | Campo | Texto |
   |---|---|
   | Título del curso | Tu Comunidad, Tu Dinero, Tu Futuro |
   | Línea | por concluir el programa de bienestar financiero Tu Comunidad, Tu Dinero, Tu Futuro |
   | Tema 1 | Apoyos sin intermediarios |
   | Tema 2 | Cuenta a mi nombre |
   | Tema 3 | Ahorro en grupo |
   | Tema 4 | Fraudes |
   | Tema 5 | Tierra y familia |

4. Revisa la **Vista previa en PDF** y activa "Verificar certificado".

Si Certificado personalizado no está instalado, la insignia **Plan completo · Tu Comunidad** funciona como constancia digital.

## 6. Qué no hacer

- No dar puntos por ver páginas.
- No publicar nombres en rankings.
- No pedir datos reales para aprobar.
- No ligar insignias ni constancia a contratar servicios o productos.
