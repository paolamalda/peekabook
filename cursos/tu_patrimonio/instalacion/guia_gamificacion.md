# Guía de actividades, puntos, insignias y constancia · Tu Patrimonio, Tu Tranquilidad, Tu Futuro

Esta guía es para Moodle 3.10 con Level Up (block_xp) 3.15.2 y el complemento Certificado personalizado (mod_customcert).

El objetivo es motivar sin competir. Los puntos premian avanzar, no la calificación perfecta. Nunca se muestra el nombre de nadie en una tabla.

## 1. Qué hay en cada módulo

| Actividad | Cuántas | Finalización |
|---|---|---|
| Libro "Lecciones del Módulo N" | 1 por módulo (11) | Ver |
| Actividad H5P "MN UYY · ¿Qué harías?" | 1 por lección (54) | Recibir calificación |
| Cuestionario "Autoevaluación del Módulo N" | 1 por módulo (11) | Calificación aprobatoria de 70% |

**Configuración de cada actividad H5P:** sin botón de descarga, con botón de derechos de autor e incrustar desactivado; seguimiento de intentos con "Calificación más alta"; finalización "El estudiante debe recibir una calificación".

**Las autoevaluaciones:** usan el banco de 162 preguntas con tres opciones y retroalimentación, en las categorías *Tu Patrimonio/M1* a *M11*. Calificación aprobatoria de 70%, intentos ilimitados, respuestas en orden aleatorio y revisión con respuesta correcta y retroalimentación al terminar.

## 2. Level Up: niveles y puntos

**Reglas** (*Level Up > Reglas*):

1. Quita o pon en 0 las reglas predeterminadas.
2. **Por completar cualquier actividad:** 25 puntos, con el evento "Se ha actualizado la finalización de un módulo del curso" (`\core\event\course_module_completion_updated`).
3. **Por participar en el foro:** 5 puntos, con el evento "Mensaje creado" (`\mod_forum\event\post_created`).
4. Deja activada la protección contra trampas.

Completar todo el curso da unos 1,900 puntos:

| Actividades | Cuántas | Puntos |
|---|---|---|
| Actividades H5P | 54 | 1,350 |
| Libros | 11 | 275 |
| Autoevaluaciones | 11 | 275 |
| **Total** | 76 | **1,900** |

**Niveles** (6 niveles, sin algoritmo automático):

| Nivel | Nombre | Puntos | Cuándo se alcanza, más o menos |
|---|---|---|---|
| 1 | Primer paso | 0 | Al entrar |
| 2 | Mi mapa | 200 | Durante el Módulo 2 |
| 3 | Con candado | 500 | Durante el Módulo 4 |
| 4 | Protegida | 850 | Durante el Módulo 5 |
| 5 | Con rumbo | 1,200 | Durante el Módulo 8 |
| 6 | Tranquila | 1,550 | Durante el Módulo 10 |

**Clasificación:** anonimato activado; mostrar solo vecinos cercanos o desactivarla.

## 3. Insignias

*Administración del curso > Insignias > Agregar una nueva insignia*. Imágenes en `5_insignias/`. Emisor: Desarrolla Talento. Vencimiento: nunca.

| Imagen | Insignia | Criterio (finalización de actividad, con aprobación) | Descripción |
|---|---|---|---|
| 01_mi_mapa_en_orden.png | Mi mapa en orden | Autoevaluaciones de los Módulos 1 y 2 | Sabes qué tienes, dónde está y cómo verificar cualquier institución. |
| 02_celular_con_candado.png | Celular con candado | Autoevaluación del Módulo 3 | Tu banca en el celular tiene alertas, límite de transferencias y una persona de confianza. |
| 03_nadie_me_engana.png | Nadie me engaña | Autoevaluación del Módulo 4 | Reconoces los fraudes y tienes tu plan de respuesta. |
| 04_ahorro_protegido.png | Ahorro protegido | Autoevaluaciones de los Módulos 5 y 6 | Tu ahorro está protegido y entiendes tus inversiones y a tu asesor. |
| 05_retiro_claro.png | Retiro claro | Autoevaluación del Módulo 7 | Conoces tus pensiones y calculaste tu retiro. |
| 06_salud_asegurada.png | Salud asegurada | Autoevaluaciones de los Módulos 8 y 9 | Entiendes tu seguro médico, tus retenciones y tus deducciones. |
| 07_familia_en_orden.png | Familia en orden | Autoevaluación del Módulo 10 | Tu testamento, tus beneficiarios y tus documentos están en orden. |
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

Si Certificado personalizado no está instalado, la insignia **Plan completo** funciona como constancia digital.

## 6. Qué no hacer

- No dar puntos por ver páginas.
- No publicar nombres en rankings.
- No pedir datos reales para aprobar.
- No ligar insignias ni constancia a contratar servicios o productos.
