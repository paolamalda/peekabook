# Guía de actividades, puntos, insignias y constancia · Tu Patrimonio, Tu Tranquilidad, Tu Futuro

Esta guía es para Moodle 4.5 con Level Up (block_xp) y el complemento Certificado personalizado (mod_customcert).

El objetivo es motivar sin competir. Los puntos premian avanzar, no la calificación perfecta. Nunca se muestra el nombre de nadie en una tabla.

## 1. Qué hay en cada parte

| Actividad | Cuántas | Finalización |
|---|---|---|
| Libro por lección (con la práctica incrustada) | 66 | Ver |
| Cuestionario "Autoevaluación del Módulo N" | 1 por parte (11) | Calificación aprobatoria de 70% |

**Las autoevaluaciones:** usan el banco de 198 preguntas con tres opciones y retroalimentación, en las categorías *Tu Patrimonio v1.0/M1* a *M11*. Calificación aprobatoria de 70%, intentos ilimitados, respuestas en orden aleatorio y revisión con respuesta correcta y retroalimentación al terminar.

## 2. Level Up: niveles y puntos

**Reglas** (*Level Up > Reglas*):

1. Quita o pon en 0 las reglas predeterminadas.
2. **Por completar cualquier actividad:** 25 puntos, con el evento "Se ha actualizado la finalización de un módulo del curso" (`\core\event\course_module_completion_updated`).
3. **Por participar en el foro:** 5 puntos, con el evento "Mensaje creado" (`\mod_forum\event\post_created`).
4. Deja activada la protección contra trampas.

Completar todo el curso da unos 1,925 puntos:

| Actividades | Cuántas | Puntos |
|---|---|---|
| Lecciones | 66 | 1,650 |
| Autoevaluaciones | 11 | 275 |
| **Total** | 77 | **1,925** |

**Niveles** (6 niveles, sin algoritmo automático):

| Nivel | Nombre | Puntos | Cuándo se alcanza, más o menos |
|---|---|---|---|
| 1 | Primer paso | 0 | Al entrar |
| 2 | Mi mapa | 200 | Durante el Módulo 2 |
| 3 | Con candado | 500 | Durante el Módulo 4 |
| 4 | Protegida | 850 | Durante el Módulo 5 |
| 5 | Con rumbo | 1,200 | Durante el Módulo 8 |
| 6 | Tranquila | 1,550 | Durante el Módulo 10 |

**Clasificación (ranking): desactivada.** En *Level Up > Clasificación* elige no mostrarla, y quita o esconde el bloque de tabla de posiciones. Cada persona ve solo sus puntos, su nivel y sus insignias.

## 3. Insignias

*Más > Insignias > Agregar una nueva insignia*. Imágenes en `5_insignias/`. Emisor: Desarrolla Talento. Vencimiento: nunca. Los nombres llevan el curso para que no se repitan en la plataforma: úsalos tal cual.

| Imagen | Insignia | Criterio (finalización de actividad, con aprobación) | Descripción |
|---|---|---|---|
| 01_mi_mapa_en_orden.png | Mi mapa en orden · Tu Patrimonio | Autoevaluaciones de los Módulos 1 y 2 | Sabes qué tienes, dónde está y cómo verificar cualquier institución. |
| 02_celular_con_candado.png | Celular con candado · Tu Patrimonio | Autoevaluación del Módulo 3 | Tu banca en el celular tiene alertas, límite de transferencias y una persona de confianza. |
| 03_nadie_me_engana.png | Nadie me engaña · Tu Patrimonio | Autoevaluación del Módulo 4 | Reconoces los fraudes y tienes tu plan de respuesta. |
| 04_ahorro_protegido.png | Ahorro protegido · Tu Patrimonio | Autoevaluaciones de los Módulos 5 y 6 | Tu ahorro está protegido y entiendes tus inversiones y a tu asesor. |
| 05_retiro_claro.png | Retiro claro · Tu Patrimonio | Autoevaluación del Módulo 7 | Conoces tus pensiones y calculaste tu retiro. |
| 06_salud_asegurada.png | Salud asegurada · Tu Patrimonio | Autoevaluaciones de los Módulos 8 y 9 | Entiendes tu seguro médico, tus retenciones y tus deducciones. |
| 07_familia_en_orden.png | Familia en orden · Tu Patrimonio | Autoevaluación del Módulo 10 | Tu testamento, tus beneficiarios y tus documentos están en orden. |
| 08_plan_completo.png | Plan completo · Tu Patrimonio | Finalización del curso | Concluiste los once módulos del programa. |

Al terminar, **activa** cada insignia.

## 4. Finalización del curso

*Más > Finalización del curso*: condición de finalización de actividades con **todas** las 11 autoevaluaciones. Opcional: los 11 libros.

## 5. Constancia de conclusión (Certificado personalizado)

1. En la sección "Evaluación y constancia", agrega **Certificado personalizado** con la **plantilla estándar de la plataforma** (sin imagen de fondo): nombre "Constancia de conclusión".
2. **Restringir acceso:** una condición de "Finalización de actividad" por cada una de las 11 autoevaluaciones, "debe estar completa con calificación aprobatoria", y la **Encuesta final** enviada.
3. En la plantilla cambia solo estos datos (también están en `6_constancia/constancia.md`):

   | Campo | Texto |
   |---|---|
   | Título del curso | Tu Patrimonio, Tu Tranquilidad, Tu Futuro |
   | Línea | por concluir el programa de bienestar financiero Tu Patrimonio, Tu Tranquilidad, Tu Futuro |
   | Tema 1 | Tu dinero y el sistema |
   | Tema 2 | Seguridad y fraudes |
   | Tema 3 | Ahorro e inversión |
   | Tema 4 | Retiro y salud |
   | Tema 5 | Familia y plan |

4. Revisa la **Vista previa en PDF** y activa "Verificar certificado".

Si Certificado personalizado no está instalado, la insignia **Plan completo · Tu Patrimonio** funciona como constancia digital.

## 6. Qué no hacer

- No dar puntos por ver páginas.
- No publicar nombres en rankings.
- No pedir datos reales para aprobar.
- No ligar insignias ni constancia a contratar servicios o productos.
