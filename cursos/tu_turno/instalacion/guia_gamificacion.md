# Guía de actividades, puntos, insignias y constancia · Tu Turno, Tu Dinero, Tu Futuro

Esta guía es para Moodle 3.10 con Level Up (block_xp) 3.15.2 y el complemento Certificado personalizado (mod_customcert).

El objetivo es motivar sin competir. Los puntos premian avanzar, no la calificación perfecta. Nunca se muestra el nombre de nadie en una tabla.

## 1. Qué hay en cada módulo

| Actividad | Cuántas | Finalización |
|---|---|---|
| Libro "Lecciones del Módulo N" | 1 por módulo (8) | Ver |
| Actividad H5P "MN UYY · ¿Qué harías?" | 1 por lección (26) | Recibir calificación |
| Cuestionario "Autoevaluación del Módulo N" | 1 por módulo (8) | Calificación aprobatoria de 70% |

**Configuración de cada actividad H5P:** sin botón de descarga, con botón de derechos de autor e incrustar desactivado; seguimiento de intentos con "Calificación más alta"; finalización "El estudiante debe recibir una calificación".

**Las autoevaluaciones:** usan el banco de 78 preguntas con tres opciones y retroalimentación, en las categorías *Tu Turno/M1* a *M8*. Calificación aprobatoria de 70%, intentos ilimitados, respuestas en orden aleatorio y revisión con respuesta correcta y retroalimentación al terminar.

## 2. Level Up: niveles y puntos

**Reglas** (*Level Up > Reglas*):

1. Quita o pon en 0 las reglas predeterminadas.
2. **Por completar cualquier actividad:** 25 puntos, con el evento "Se ha actualizado la finalización de un módulo del curso" (`\core\event\course_module_completion_updated`).
3. **Por participar en el foro:** 5 puntos, con el evento "Mensaje creado" (`\mod_forum\event\post_created`).
4. Deja activada la protección contra trampas.

Completar todo el curso da unos 1,050 puntos:

| Actividades | Cuántas | Puntos |
|---|---|---|
| Actividades H5P | 26 | 650 |
| Libros | 8 | 200 |
| Autoevaluaciones | 8 | 200 |
| **Total** | 42 | **1,050** |

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

*Administración del curso > Insignias > Agregar una nueva insignia*. Imágenes en `5_insignias/`. Emisor: Desarrolla Talento. Vencimiento: nunca.

| Imagen | Insignia | Criterio (finalización de actividad, con aprobación) | Descripción |
|---|---|---|---|
| 01_quincena_en_orden.png | Quincena en orden | Autoevaluaciones de los Módulos 1 y 2 | Tu quincena tiene presupuesto, ahorro apartado y una cuenta sin comisiones. |
| 02_deudas_claras.png | Deudas claras | Autoevaluación del Módulo 3 | Conoces todas tus deudas, lo que cuestan y tu plan para salir. |
| 03_tanda_segura.png | Tanda segura | Autoevaluación del Módulo 4 | Sabes organizar una tanda con reglas o ahorrar por tu cuenta. |
| 04_buro_sin_miedo.png | Buró sin miedo | Autoevaluación del Módulo 5 | Revisaste tu reporte de crédito y sabes cómo mejorarlo. |
| 05_nadie_me_extorsiona.png | Nadie me extorsiona | Autoevaluación del Módulo 6 | Reconoces fraudes, apps montadeudas y extorsiones, y sabes qué hacer. |
| 06_familia_protegida.png | Familia protegida | Autoevaluación del Módulo 7 | Tienes fondo de emergencia y protección para tu familia. |
| 07_futuro_en_marcha.png | Futuro en marcha | Autoevaluación del Módulo 8 | Ahorras para tu retiro y tienes tu plan de una página. |
| 08_plan_completo.png | Plan completo | Finalización del curso | Concluiste los ocho módulos del programa. |

Al terminar, **activa** cada insignia.

## 4. Finalización del curso

*Administración del curso > Finalización del curso*: condición de finalización de actividades con **todas** las 8 autoevaluaciones. Opcional: los 8 libros.

## 5. Constancia de conclusión (Certificado personalizado)

1. En la sección "Evaluación y constancia", agrega **Certificado personalizado**: nombre "Constancia de conclusión", tamaño A4 horizontal (297 × 210 mm).
2. **Restringir acceso:** una condición de "Finalización de actividad" por cada una de las 8 autoevaluaciones, "debe estar completa con calificación aprobatoria".
3. **Editar certificado:**

   | Elemento | Posición aproximada (mm) | Formato |
   |---|---|---|
   | Imagen de fondo | Cubre la página | `6_certificado/certificado_fondo.png` |
   | Nombre del estudiante | X 0, Y 74, ancho 297, centrado | Negrita, 32 pt, color #0B1220 |
   | Fecha (finalización del curso) | X 17, Y 170, ancho 70, centrado | 12 pt, color #E4007C |
   | Código | X 210, Y 170, ancho 70, centrado | 12 pt, color #E4007C |

4. Revisa la **Vista previa en PDF** y compárala con `certificado_muestra.png`. Activa "Verificar certificado".

Si Certificado personalizado no está instalado, la insignia **Plan completo** funciona como constancia digital.

## 6. Qué no hacer

- No dar puntos por ver páginas.
- No publicar nombres en rankings.
- No pedir datos reales para aprobar.
- No ligar insignias ni constancia a contratar servicios o productos.
