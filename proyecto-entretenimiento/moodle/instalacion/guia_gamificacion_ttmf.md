# Guía de actividades, puntos, insignias y constancia · Tu Talento, Tu Marca, Tu Futuro

Esta guía es para Moodle 3.10 con Level Up (block_xp) 3.15.2 y el complemento Certificado personalizado (mod_customcert), que ya están instalados en el sitio.

El objetivo es motivar sin competir. Los puntos premian avanzar, no la calificación perfecta. Nunca se muestra el nombre de nadie en una tabla.

## 1. Qué hay en cada módulo

| Actividad | Cuántas | Finalización |
|---|---|---|
| Libro "Lecciones del Módulo N" | 1 por módulo (11) | Ver |
| Actividad H5P "MN UYY · ¿Qué harías?" | 1 por lección (73) | Recibir calificación |
| Cuestionario "Autoevaluación del Módulo N" | 1 por módulo (11) | Calificación aprobatoria de 70% |

**Configuración de cada actividad H5P:**

- Opciones de H5P: sin botón de descarga, con botón de derechos de autor e incrustar desactivado.
- Intentos: seguimiento activado y método "Calificación más alta".
- Finalización: "El estudiante debe recibir una calificación".

**Las autoevaluaciones:** usan el banco de 219 preguntas con tres opciones y retroalimentación, en las categorías *Tu Talento/M1* a *M11*. Calificación aprobatoria de 70%, intentos ilimitados, respuestas en orden aleatorio y revisión con respuesta correcta y retroalimentación al terminar.

## 2. Level Up: niveles y puntos

**Reglas** (*Level Up > Reglas*):

1. Quita o pon en 0 las reglas predeterminadas.
2. **Por completar cualquier actividad:** 25 puntos, con el evento "Se ha actualizado la finalización de un módulo del curso" (`\core\event\course_module_completion_updated`).
3. **Por participar en el foro:** 5 puntos, con el evento "Mensaje creado" (`\mod_forum\event\post_created`).
4. Deja activada la protección contra trampas.

Completar todo el curso da unos 2,375 puntos:

| Actividades | Cuántas | Puntos |
|---|---|---|
| Actividades H5P | 73 | 1,825 |
| Libros | 11 | 275 |
| Autoevaluaciones | 11 | 275 |
| **Total** | 95 | **2,375** |

**Niveles** (6 niveles, sin algoritmo automático):

| Nivel | Nombre | Puntos | Cuándo se alcanza, más o menos |
|---|---|---|---|
| 1 | Casting | 0 | Al entrar |
| 2 | Ensayo | 250 | Durante el Módulo 2 |
| 3 | Llamado | 700 | Durante el Módulo 5 |
| 4 | Estreno | 1,200 | Durante el Módulo 7 |
| 5 | Temporada | 1,700 | Durante el Módulo 9 |
| 6 | Trayectoria | 2,150 | Durante el Módulo 11 |

**Clasificación:** anonimato activado; mostrar solo vecinos cercanos o desactivarla.

## 3. Insignias

*Administración del curso > Insignias > Agregar una nueva insignia*. Imágenes en `5_insignias/`. Emisor: Desarrolla Talento. Vencimiento: nunca.

| Imagen | Insignia | Criterio (finalización de actividad, con aprobación) | Descripción |
|---|---|---|---|
| 01_dinero_real.png | Dinero real | Autoevaluación del Módulo 1 | Calculas tu ganancia real, te pagas un sueldo fijo y tienes meta de fondo de sequía. |
| 02_carrera_en_regla.png | Carrera en regla | Autoevaluaciones de los Módulos 2 y 3 | Conoces tu régimen fiscal, tus contratos y a quién acudir por tus regalías. |
| 03_se_elegir.png | Sé elegir | Autoevaluaciones de los Módulos 4 y 5 | Distingues instituciones, las verificas y comparas productos antes de contratar. |
| 04_credito_bajo_control.png | Crédito bajo control | Autoevaluaciones de los Módulos 6, 7 y 8 | Sabes que el crédito es deuda, revisas tu Buró y Círculo y tienes plan de salida. |
| 05_nadie_me_engana.png | Nadie me engaña | Autoevaluación del Módulo 9 | Reconoces fraudes, proteges tu identidad y sabes cómo responder. |
| 06_proteccion_activa.png | Protección activa | Autoevaluación del Módulo 10 | Tienes plan de salud, IMSS, seguros, marca y documentos para tu familia. |
| 07_futuro_en_escena.png | Futuro en escena | Autoevaluación del Módulo 11 | Tu retiro, tu carrera larga y tu plan de una página están escritos. |
| 08_plan_completo.png | Plan completo | Finalización del curso | Concluiste los once módulos del programa. |

Al terminar, **activa** cada insignia.

## 4. Finalización del curso

*Administración del curso > Finalización del curso*: condición de finalización de actividades con **todas** las 11 autoevaluaciones. Opcional: los 11 libros.

## 5. Constancia de conclusión (Certificado personalizado)

1. En la sección "Evaluación y constancia", agrega **Certificado personalizado**: nombre "Constancia de conclusión", tamaño A4 horizontal (297 × 210 mm).
2. **Restringir acceso:** una condición de "Finalización de actividad" por cada una de las 11 autoevaluaciones, "debe estar completa con calificación aprobatoria".
3. **Editar certificado:**

   | Elemento | Posición aproximada (mm) | Formato |
   |---|---|---|
   | Imagen de fondo | Cubre la página | `6_certificado/certificado_fondo.png` |
   | Nombre del estudiante | X 0, Y 74, ancho 297, centrado | Negrita, 32 pt, color #0B1220 |
   | Fecha (finalización del curso) | X 17, Y 170, ancho 70, centrado | 12 pt, color #E4007C |
   | Código | X 210, Y 170, ancho 70, centrado | 12 pt, color #E4007C |

4. Revisa la **Vista previa en PDF** y compárala con `certificado_muestra.png`. Activa "Verificar certificado".

## 6. Qué no hacer

- No dar puntos por ver páginas.
- No publicar nombres en rankings.
- No pedir datos reales para aprobar.
- No ligar insignias ni constancia a contratar servicios o productos, incluidos los que se anuncian en los canales de la comunidad.
