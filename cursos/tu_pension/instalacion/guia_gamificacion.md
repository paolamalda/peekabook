# Guía de actividades, puntos, insignias y constancia · Tu Pensión, Tu Tranquilidad, Tu Futuro

Esta guía es para Moodle 4.5 con Level Up (block_xp) y el complemento Certificado personalizado (mod_customcert).

El objetivo es motivar sin competir. Los puntos premian avanzar, no la calificación perfecta. Nunca se muestra el nombre de nadie en una tabla.

## 1. Qué hay en cada parte

| Actividad | Cuántas | Finalización |
|---|---|---|
| Libro por lección (con la práctica incrustada) | 16 | Ver |
| Cuestionario "Autoevaluación del Módulo N" | 1 por parte (8) | Calificación aprobatoria de 70% |

**Las autoevaluaciones:** usan el banco de 48 preguntas con tres opciones y retroalimentación, en las categorías *Tu Pensión v0.1/M1* a *M8*. Calificación aprobatoria de 70%, intentos ilimitados, respuestas en orden aleatorio y revisión con respuesta correcta y retroalimentación al terminar.

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
| 01_pension_que_alcanza.png | Pensión que alcanza · Tu Pensión | Autoevaluación del Módulo 1 completada (aprobada) | Tu pensión repartida en el bimestre, con lo básico primero. |
| 02_mi_nip_es_mio.png | Mi NIP es mío · Tu Pensión | Autoevaluación del Módulo 2 completada (aprobada) | Tu NIP protegido y tu forma segura de usar el cajero. |
| 03_cuelgo_y_verifico.png | Cuelgo y verifico · Tu Pensión | Autoevaluación del Módulo 3 completada (aprobada) | Tu regla para colgar y verificar ante llamadas y mensajes. |
| 04_nadie_decide_por_mi.png | Nadie decide por mí · Tu Pensión | Autoevaluación del Módulo 4 completada (aprobada) | Las señales de abuso patrimonial y a quién llamar. |
| 05_prestamo_con_cabeza.png | Préstamo con cabeza · Tu Pensión | Autoevaluación del Módulo 5 completada (aprobada) | Tu decisión informada sobre préstamos y el tope de 30%. |
| 06_apoyo_de_confianza.png | Apoyo de confianza · Tu Pensión | Autoevaluación del Módulo 6 completada (aprobada) | Tu persona de apoyo elegida y ningún poder amplio firmado sin revisar. |
| 07_todo_en_orden.png | Todo en orden · Tu Pensión | Autoevaluaciones de los módulos 7 y 8 | Tus beneficiarios revisados y tu decisión sobre el testamento. Tu guardadito para salud y tus seguros revisados. |
| 08_plan_completo.png | Plan completo · Tu Pensión | Finalización del curso | Concluiste los 8 módulos del programa. |

Al terminar, **activa** cada insignia.

## 4. Finalización del curso

*Más > Finalización del curso*: condición de finalización de actividades con **todas** las 8 autoevaluaciones. Opcional: los 8 libros.

## 5. Constancia de conclusión (Certificado personalizado)

1. En la sección "Evaluación y constancia", agrega **Certificado personalizado** con la **plantilla estándar de la plataforma** (sin imagen de fondo): nombre "Constancia de conclusión".
2. **Restringir acceso:** una condición de "Finalización de actividad" por cada una de las 8 autoevaluaciones, "debe estar completa con calificación aprobatoria", y la **Encuesta final** enviada.
3. En la plantilla cambia solo estos datos (también están en `6_constancia/constancia.md`):

   | Campo | Texto |
   |---|---|
   | Título del curso | Tu Pensión, Tu Tranquilidad, Tu Futuro |
   | Línea | por concluir el programa de bienestar financiero Tu Pensión, Tu Tranquilidad, Tu Futuro |
   | Tema 1 | Pensión y tarjeta |
   | Tema 2 | Fraudes |
   | Tema 3 | Abuso patrimonial |
   | Tema 4 | Testamento |
   | Tema 5 | Salud y seguros |

4. Revisa la **Vista previa en PDF** y activa "Verificar certificado".

Si Certificado personalizado no está instalado, la insignia **Plan completo · Tu Pensión** funciona como constancia digital.

## 6. Qué no hacer

- No dar puntos por ver páginas.
- No publicar nombres en rankings.
- No pedir datos reales para aprobar.
- No ligar insignias ni constancia a contratar servicios o productos.
