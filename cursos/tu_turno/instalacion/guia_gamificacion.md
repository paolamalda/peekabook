# Guía de actividades, puntos, insignias y constancia · Tu Turno, Tu Dinero, Tu Futuro

Esta guía es para Moodle 3.10 con Level Up (block_xp) 3.15.2 y el complemento Certificado personalizado (mod_customcert).

El objetivo es motivar sin competir. Los puntos premian avanzar, no la calificación perfecta. Nunca se muestra el nombre de nadie en una tabla.

## 1. Qué hay en cada módulo

| Actividad | Cuántas | Finalización |
|---|---|---|
| Libro "Lecciones del Módulo N" | 1 por módulo (8) | Ver |
| Actividad H5P "MN UYY · ¿Qué harías?" | 1 por lección (37) | Recibir calificación |
| Cuestionario "Autoevaluación del Módulo N" | 1 por módulo (8) | Calificación aprobatoria de 70% |

**Configuración de cada actividad H5P:** sin botón de descarga, con botón de derechos de autor e incrustar desactivado; seguimiento de intentos con "Calificación más alta"; finalización "El estudiante debe recibir una calificación".

**Las autoevaluaciones:** usan el banco de 111 preguntas con tres opciones y retroalimentación, en las categorías *Tu Turno v1.2/M1* a *M8*. Calificación aprobatoria de 70%, intentos ilimitados, respuestas en orden aleatorio y revisión con respuesta correcta y retroalimentación al terminar.

## 2. Level Up: niveles y puntos

**Reglas** (*Level Up > Reglas*):

1. Quita o pon en 0 las reglas predeterminadas.
2. **Por completar cualquier actividad:** 25 puntos, con el evento "Se ha actualizado la finalización de un módulo del curso" (`\core\event\course_module_completion_updated`).
3. **Por participar en el foro:** 5 puntos, con el evento "Mensaje creado" (`\mod_forum\event\post_created`).
4. Deja activada la protección contra trampas.

Completar todo el curso da unos 1,325 puntos:

| Actividades | Cuántas | Puntos |
|---|---|---|
| Actividades H5P | 37 | 925 |
| Libros | 8 | 200 |
| Autoevaluaciones | 8 | 200 |
| **Total** | 53 | **1,325** |

**Niveles** (6 niveles, sin algoritmo automático):

| Nivel | Nombre | Puntos | Cuándo se alcanza, más o menos |
|---|---|---|---|
| 1 | Primer turno | 0 | Al entrar |
| 2 | Quincena en orden | 150 | Durante el Módulo 2 |
| 3 | Sin deudas ocultas | 350 | Durante el Módulo 3 |
| 4 | Alerta | 550 | Durante el Módulo 5 |
| 5 | Protegido | 750 | Durante el Módulo 7 |
| 6 | Con futuro | 900 | Durante el Módulo 8 |

**Clasificación:** anonimato activado; mostrar solo vecinos cercanos o desactivarla.

## 3. Insignias

*Administración del curso > Insignias > Agregar una nueva insignia*. Imágenes en `5_insignias/`. Emisor: Desarrolla Talento. Vencimiento: nunca. Los nombres llevan el curso para que no se repitan en la plataforma: úsalos tal cual.

| Imagen | Insignia | Criterio (finalización de actividad, con aprobación) | Descripción |
|---|---|---|---|
| 01_quincena_en_orden.png | Quincena en orden · Tu Turno | Autoevaluaciones de los Módulos 1 y 2 | Tu quincena tiene presupuesto, ahorro apartado y una cuenta sin comisiones. |
| 02_deudas_claras.png | Deudas claras · Tu Turno | Autoevaluación del Módulo 3 | Conoces todas tus deudas, lo que cuestan y tu plan para salir. |
| 03_tanda_segura.png | Tanda segura · Tu Turno | Autoevaluación del Módulo 4 | Sabes organizar una tanda con reglas o ahorrar por tu cuenta. |
| 04_buro_sin_miedo.png | Buró sin miedo · Tu Turno | Autoevaluación del Módulo 5 | Revisaste tu reporte de crédito y sabes cómo mejorarlo. |
| 05_nadie_me_extorsiona.png | Nadie me extorsiona · Tu Turno | Autoevaluación del Módulo 6 | Reconoces fraudes, apps montadeudas y extorsiones, y sabes qué hacer. |
| 06_familia_protegida.png | Familia protegida · Tu Turno | Autoevaluación del Módulo 7 | Tienes fondo de emergencia y protección para tu familia. |
| 07_futuro_en_marcha.png | Futuro en marcha · Tu Turno | Autoevaluación del Módulo 8 | Ahorras para tu retiro y tienes tu plan de una página. |
| 08_plan_completo.png | Plan completo · Tu Turno | Finalización del curso | Concluiste los ocho módulos del programa. |

Al terminar, **activa** cada insignia.

## 4. Finalización del curso

*Administración del curso > Finalización del curso*: condición de finalización de actividades con **todas** las 8 autoevaluaciones. Opcional: los 8 libros.

## 5. Constancia de conclusión (Certificado personalizado)

1. En la sección "Evaluación y constancia", agrega **Certificado personalizado** con la **plantilla estándar de la plataforma** (sin imagen de fondo): nombre "Constancia de conclusión".
2. **Restringir acceso:** una condición de "Finalización de actividad" por cada una de las 8 autoevaluaciones, "debe estar completa con calificación aprobatoria", y la **Encuesta final** enviada.
3. En la plantilla cambia solo estos datos (también están en `6_constancia/constancia.md`):

   | Campo | Texto |
   |---|---|
   | Título del curso | Tu Turno, Tu Dinero, Tu Futuro |
   | Línea | por concluir el programa de bienestar financiero Tu Turno, Tu Dinero, Tu Futuro |
   | Tema 1 | Quincena y cuenta |
   | Tema 2 | Deudas y tandas |
   | Tema 3 | Buró y fraudes |
   | Tema 4 | Familia |
   | Tema 5 | Futuro |

4. Revisa la **Vista previa en PDF** y activa "Verificar certificado".

Si Certificado personalizado no está instalado, la insignia **Plan completo · Tu Turno** funciona como constancia digital.

## 6. Qué no hacer

- No dar puntos por ver páginas.
- No publicar nombres en rankings.
- No pedir datos reales para aprobar.
- No ligar insignias ni constancia a contratar servicios o productos.
