# Guía de actividades, puntos, insignias y constancia · Tu Negocio, Tu Dinero, Tu Futuro

Esta guía es para Moodle 3.10 con Level Up (block_xp) 3.15.2 y el complemento Certificado personalizado (mod_customcert).

El objetivo es motivar sin competir. Los puntos premian avanzar, no la calificación perfecta. Nunca se muestra el nombre de nadie en una tabla.

## 1. Qué hay en cada módulo

| Actividad | Cuántas | Finalización |
|---|---|---|
| Libro "Lecciones del Módulo N" | 1 por módulo (9) | Ver |
| Actividad H5P "MN UYY · ¿Qué harías?" | 1 por lección (34) | Recibir calificación |
| Cuestionario "Autoevaluación del Módulo N" | 1 por módulo (9) | Calificación aprobatoria de 70% |

**Configuración de cada actividad H5P:** sin botón de descarga, con botón de derechos de autor e incrustar desactivado; seguimiento de intentos con "Calificación más alta"; finalización "El estudiante debe recibir una calificación".

**Las autoevaluaciones:** usan el banco de 102 preguntas con tres opciones y retroalimentación, en las categorías *Tu Negocio MX/M1* a *M9*. Calificación aprobatoria de 70%, intentos ilimitados, respuestas en orden aleatorio y revisión con respuesta correcta y retroalimentación al terminar.

## 2. Level Up: niveles y puntos

**Reglas** (*Level Up > Reglas*):

1. Quita o pon en 0 las reglas predeterminadas.
2. **Por completar cualquier actividad:** 25 puntos, con el evento "Se ha actualizado la finalización de un módulo del curso" (`\core\event\course_module_completion_updated`).
3. **Por participar en el foro:** 5 puntos, con el evento "Mensaje creado" (`\mod_forum\event\post_created`).
4. Deja activada la protección contra trampas.

Completar todo el curso da unos 1,300 puntos:

| Actividades | Cuántas | Puntos |
|---|---|---|
| Actividades H5P | 34 | 850 |
| Libros | 9 | 225 |
| Autoevaluaciones | 9 | 225 |
| **Total** | 52 | **1,300** |

**Niveles** (6 niveles, sin algoritmo automático):

| Nivel | Nombre | Puntos | Cuándo se alcanza, más o menos |
|---|---|---|---|
| 1 | Idea | 0 | Al entrar |
| 2 | Arranque | 200 | Durante el Módulo 2 |
| 3 | En marcha | 400 | Durante el Módulo 4 |
| 4 | Formal | 650 | Durante el Módulo 5 |
| 5 | En crecimiento | 900 | Durante el Módulo 7 |
| 6 | Consolidado | 1,100 | Durante el Módulo 9 |

**Clasificación:** anonimato activado; mostrar solo vecinos cercanos o desactivarla.

## 3. Insignias

*Administración del curso > Insignias > Agregar una nueva insignia*. Imágenes en `5_insignias/`. Emisor: Desarrolla Talento. Vencimiento: nunca.

| Imagen | Insignia | Criterio (finalización de actividad, con aprobación) | Descripción |
|---|---|---|---|
| 01_dinero_separado.png | Dinero separado | Autoevaluación del Módulo 1 | Separaste el dinero del negocio y de tu casa y te pagas un sueldo. |
| 02_precio_justo.png | Precio justo | Autoevaluación del Módulo 2 | Conoces tus costos, tu margen y tu punto de equilibrio. |
| 03_flujo_bajo_control.png | Flujo bajo control | Autoevaluaciones de los Módulos 3 y 4 | Controlas tu flujo, tu fiado y tus formas de cobro sin perder. |
| 04_negocio_formal.png | Negocio formal | Autoevaluación del Módulo 5 | Tienes tu RFC, tu régimen, tus facturas y declaraciones en orden. |
| 05_credito_inteligente.png | Crédito inteligente | Autoevaluación del Módulo 6 | Sabes si necesitas crédito y cuánto cuesta de verdad. |
| 06_negocio_protegido.png | Negocio protegido | Autoevaluación del Módulo 7 | Protegiste tu salud, tu negocio, tu marca y te cuidas de fraudes. |
| 07_crecer_con_orden.png | Crecer con orden | Autoevaluaciones de los Módulos 8 y 9 | Creces con orden y tienes tu plan de una página. |
| 08_plan_completo.png | Plan completo | Finalización del curso | Concluiste los nueve módulos del programa. |

Al terminar, **activa** cada insignia.

## 4. Finalización del curso

*Administración del curso > Finalización del curso*: condición de finalización de actividades con **todas** las 9 autoevaluaciones. Opcional: los 9 libros.

## 5. Constancia de conclusión (Certificado personalizado)

1. En la sección "Evaluación y constancia", agrega **Certificado personalizado**: nombre "Constancia de conclusión", tamaño A4 horizontal (297 × 210 mm).
2. **Restringir acceso:** una condición de "Finalización de actividad" por cada una de las 9 autoevaluaciones, "debe estar completa con calificación aprobatoria".
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
