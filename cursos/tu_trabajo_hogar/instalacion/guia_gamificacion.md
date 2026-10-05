# Guía de actividades, puntos, insignias y constancia · Tu Trabajo, Tu Familia, Tu Futuro

Esta guía es para Moodle 3.10 con Level Up (block_xp) 3.15.2 y el complemento Certificado personalizado (mod_customcert).

El objetivo es motivar sin competir. Los puntos premian avanzar, no la calificación perfecta. Nunca se muestra el nombre de nadie en una tabla.

## 1. Qué hay en cada módulo

| Actividad | Cuántas | Finalización |
|---|---|---|
| Libro "Lecciones del Módulo N" | 1 por módulo (9) | Ver |
| Actividad H5P "MN UYY · ¿Qué harías?" | 1 por lección (45) | Recibir calificación |
| Cuestionario "Autoevaluación del Módulo N" | 1 por módulo (9) | Calificación aprobatoria de 70% |

**Configuración de cada actividad H5P:** sin botón de descarga, con botón de derechos de autor e incrustar desactivado; seguimiento de intentos con "Calificación más alta"; finalización "El estudiante debe recibir una calificación".

**Las autoevaluaciones:** usan el banco de 135 preguntas con tres opciones y retroalimentación, en las categorías *Tu Trabajo v1.0/M1* a *M9*. Calificación aprobatoria de 70%, intentos ilimitados, respuestas en orden aleatorio y revisión con respuesta correcta y retroalimentación al terminar.

## 2. Level Up: niveles y puntos

**Reglas** (*Level Up > Reglas*):

1. Quita o pon en 0 las reglas predeterminadas.
2. **Por completar cualquier actividad:** 25 puntos, con el evento "Se ha actualizado la finalización de un módulo del curso" (`\core\event\course_module_completion_updated`).
3. **Por participar en el foro:** 5 puntos, con el evento "Mensaje creado" (`\mod_forum\event\post_created`).
4. Deja activada la protección contra trampas.

Completar todo el curso da unos 1,575 puntos:

| Actividades | Cuántas | Puntos |
|---|---|---|
| Actividades H5P | 45 | 1,125 |
| Libros | 9 | 225 |
| Autoevaluaciones | 9 | 225 |
| **Total** | 63 | **1,575** |

**Niveles** (6 niveles, sin algoritmo automático):

| Nivel | Nombre | Puntos | Cuándo se alcanza, más o menos |
|---|---|---|---|
| 1 | Primer paso | 0 | Al entrar |
| 2 | Semana en orden | 150 | Durante el Módulo 2 |
| 3 | Mi trabajo vale | 350 | Durante el Módulo 3 |
| 4 | Sin deudas ocultas | 600 | Durante el Módulo 5 |
| 5 | Protegida | 800 | Durante el Módulo 7 |
| 6 | Con futuro | 1,000 | Durante el Módulo 9 |

**Clasificación:** anonimato activado; mostrar solo vecinos cercanos o desactivarla.

## 3. Insignias

*Administración del curso > Insignias > Agregar una nueva insignia*. Imágenes en `5_insignias/`. Emisor: Desarrolla Talento. Vencimiento: nunca. Los nombres llevan el curso para que no se repitan en la plataforma: úsalos tal cual.

| Imagen | Insignia | Criterio (finalización de actividad, con aprobación) | Descripción |
|---|---|---|---|
| 01_semana_en_orden.png | Semana en orden · Tu Trabajo | Autoevaluaciones de los Módulos 1 y 2 | Sabes cuánto te entra, cuánto vale tu trabajo y tu ahorro va primero. |
| 02_ahorro_seguro.png | Ahorro seguro · Tu Trabajo | Autoevaluación del Módulo 3 | Tu tanda tiene reglas y tienes un fondo para emergencias. |
| 03_familia_sin_deudas.png | Familia sin deudas · Tu Trabajo | Autoevaluaciones de los Módulos 4 y 5 | Ayudas a tu familia con reglas y tienes plan para tus deudas. |
| 04_protegida.png | Protegida · Tu Trabajo | Autoevaluación del Módulo 6 | Revisaste tu protección de salud y tu prevención. |
| 05_nadie_me_engana.png | Nadie me engaña · Tu Trabajo | Autoevaluación del Módulo 7 | Reconoces fraudes y montadeudas y sabes qué hacer. |
| 06_futuro_claro.png | Futuro claro · Tu Trabajo | Autoevaluación del Módulo 8 | Conoces tu pensión, tu Afore y los apoyos de tu familia. |
| 07_mujer_que_crece.png | Mujer que crece · Tu Trabajo | Autoevaluación del Módulo 9 | Tienes una idea para ganar más y tu plan de una página. |
| 08_plan_completo.png | Plan completo · Tu Trabajo | Finalización del curso | Concluiste los nueve módulos del programa. |

Al terminar, **activa** cada insignia.

## 4. Finalización del curso

*Administración del curso > Finalización del curso*: condición de finalización de actividades con **todas** las 9 autoevaluaciones. Opcional: los 9 libros.

## 5. Constancia de conclusión (Certificado personalizado)

1. En la sección "Evaluación y constancia", agrega **Certificado personalizado** con la **plantilla estándar de la plataforma** (sin imagen de fondo): nombre "Constancia de conclusión".
2. **Restringir acceso:** una condición de "Finalización de actividad" por cada una de las 9 autoevaluaciones, "debe estar completa con calificación aprobatoria", y la **Encuesta final** enviada.
3. En la plantilla cambia solo estos datos (también están en `6_constancia/constancia.md`):

   | Campo | Texto |
   |---|---|
   | Título del curso | Tu Trabajo, Tu Familia, Tu Futuro |
   | Línea | por concluir el programa de bienestar financiero Tu Trabajo, Tu Familia, Tu Futuro |
   | Tema 1 | Ingreso y derechos |
   | Tema 2 | Tandas y ahorro |
   | Tema 3 | Familia y deudas |
   | Tema 4 | Salud y fraudes |
   | Tema 5 | Vejez y crecer |

4. Revisa la **Vista previa en PDF** y activa "Verificar certificado".

Si Certificado personalizado no está instalado, la insignia **Plan completo · Tu Trabajo** funciona como constancia digital.

## 6. Qué no hacer

- No dar puntos por ver páginas.
- No publicar nombres en rankings.
- No pedir datos reales para aprobar.
- No ligar insignias ni constancia a contratar servicios o productos.
