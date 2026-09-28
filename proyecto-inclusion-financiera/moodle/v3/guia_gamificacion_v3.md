# Guía de actividades, puntos, insignias y constancia (versión 3)

Esta guía es para Moodle 3.10 con Level Up (block_xp) 3.15.2. Usa lo que ya tiene tu plataforma y solo pide un complemento: el certificado.

El objetivo es motivar sin competir. Los puntos premian avanzar, no la calificación perfecta. Nunca se muestra el nombre de nadie en una tabla.

## 1. Qué hay en cada módulo

| Actividad | Cuántas | Finalización |
|---|---|---|
| Libro "Lecciones del Módulo N" | 1 por módulo | Ver |
| Actividad H5P "MN UYY · ¿Qué harías?" | 1 por lección (59 en total) | Recibir calificación |
| Cuestionario "Autoevaluación del Módulo N" | 1 por módulo | Calificación aprobatoria de 70% |

**Las actividades H5P:**

- Cada una trae tres casos de la lección, con tres opciones cada uno.
- Mezclan las opciones, marcan la respuesta correcta y dejan reintentar.
- Son de tipo *Single Choice Set*. Traen incluidas sus librerías, en versiones compatibles con Moodle 3.10.
- Súbelas como **Actividad H5P** (mod_h5pactivity, parte de Moodle desde 3.9).

**Configuración de cada actividad H5P:**

- Opciones de H5P: sin botón de descarga, con botón de derechos de autor e incrustar desactivado.
- Intentos: seguimiento activado y método "Calificación más alta".
- Finalización: "El estudiante debe recibir una calificación".

**Las autoevaluaciones:**

- Usan el banco de preguntas v3: 177 preguntas con tres opciones y retroalimentación.
- Cada módulo tiene su propia categoría: *Tu Dinero v3/M1* a *M5*.
- Configuración: calificación aprobatoria de 70%, intentos ilimitados y revisión con respuesta correcta y retroalimentación al terminar.

## 2. Level Up: niveles y puntos

La versión gratuita de Level Up da puntos por **eventos**. Configura una sola regla principal, así funciona con la versión gratuita y con Level Up+.

**Reglas** (*Level Up > Reglas*):

1. **Quita o pon en 0 las reglas predeterminadas.** Así, abrir una página o ver un recurso no da puntos.
2. **Por completar cualquier actividad:** 25 puntos. Usa el evento "Se ha actualizado la finalización de un módulo del curso" (`\core\event\course_module_completion_updated`).
3. **Por participar en el foro:** 5 puntos. Usa el evento "Mensaje creado" (`\mod_forum\event\post_created`).
4. Deja activada la **protección contra trampas** que trae Level Up. Evita que el mismo evento repetido sume puntos.

Con esas reglas, completar todo el curso da unos 1,725 puntos:

| Actividades | Cuántas | Puntos |
|---|---|---|
| Actividades H5P | 59 | 1,475 |
| Libros | 5 | 125 |
| Autoevaluaciones | 5 | 125 |
| **Total** | 69 | **1,725** |

**Niveles** (*Level Up > Niveles*, 6 niveles, sin algoritmo automático):

| Nivel | Nombre | Puntos | Cuándo se alcanza, más o menos |
|---|---|---|---|
| 1 | Empiezo | 0 | Al entrar |
| 2 | Me organizo | 150 | A mitad del Módulo 1 |
| 3 | Uso mi cuenta | 450 | Durante el Módulo 2 |
| 4 | Cuido mi crédito | 800 | Durante el Módulo 3 |
| 5 | Protejo a mi familia | 1,150 | Durante el Módulo 4 |
| 6 | Construyo mi futuro | 1,500 | Durante el Módulo 5 |

**Clasificación** (*Level Up > Clasificación*):

- Anonimato activado.
- Mostrar solo a los vecinos cercanos, o desactivar la clasificación.

## 3. Insignias

Créalas en *Administración del curso > Insignias > Agregar una nueva insignia*. Las imágenes están en `5_insignias/`.

Para cada insignia:

- **Emisor:** Desarrolla Talento.
- **Vencimiento:** nunca.
- **Criterio:** "Finalización de actividad", salvo "Plan completo", que usa "Finalización del curso".

| Imagen | Insignia | Criterio | Descripción |
|---|---|---|---|
| 01_M1_mi_dinero_en_orden.png | Mi dinero en orden | Autoevaluación del Módulo 1 completada (aprobada) | Organizaste tu flujo de dinero, tu presupuesto y tus impuestos. 14 lecciones, unas 3 horas. |
| 02_M2_envio_inteligente.png | Envío inteligente | Autoevaluación del Módulo 2 | Sabes elegir cuenta, comparar remesas y proteger a tu familia de fraudes. 13 lecciones. |
| 03_M3_credito_con_rumbo.png | Crédito con rumbo | Autoevaluación del Módulo 3 | Entiendes tu reporte, comparas préstamos y tienes un plan de deudas. 10 lecciones. |
| 04_M4_familia_protegida.png | Familia protegida | Autoevaluación del Módulo 4 | Tienes un plan de protección, seguros y preparación familiar. 11 lecciones. |
| 05_M5_futuro_en_marcha.png | Futuro en marcha | Autoevaluación del Módulo 5 | Tus metas, tu retiro y tu plan de una página están escritos. 11 lecciones. |
| 06_detective_de_estafas.png | Detective de estafas | H5P de M2 U11, M4 U01 y M4 U02 completados | Reconoces las señales de fraude y verificas antes de actuar. |
| 07_comparador_experto.png | Comparador experto | H5P de M2 U08, M3 U05 y M5 U05 completados | Comparas con el costo total, no solo con el precio anunciado. |
| 08_plan_completo.png | Plan completo | Finalización del curso | Concluiste los cinco módulos del programa. |

Al terminar, **activa** cada insignia (*Habilitar acceso*). Moodle no deja cambiar el criterio de una insignia que ya se entregó.

## 4. Finalización del curso

*Administración del curso > Finalización del curso*:

- **Condición:** finalización de actividades, con **todas** estas: las 5 autoevaluaciones.
- **Opcional:** agrega también los 5 libros.

## 5. Constancia de conclusión (certificado)

Moodle 3.10 no trae certificados. Hay dos caminos.

### Camino recomendado: complemento "Custom certificate" (mod_customcert)

Es gratuito y muy usado. Tiene versión para Moodle 3.10, la rama MOODLE_310_STABLE.

Instálalo **tú**, con la cuenta de administración del sitio, desde *Administración del sitio > Extensiones > Instalar complementos*. También puedes subirlo por cPanel.

Haz antes un respaldo del sitio.

1. En la sección "Evaluación y constancia", agrega la actividad **Certificado personalizado**.
   - **Nombre:** Constancia de conclusión.
   - **Tamaño:** A4 horizontal (297 × 210 mm).
2. **Restringir acceso:** agrega una condición de "Finalización de actividad" por cada una de las 5 autoevaluaciones, con la opción "debe estar completa con calificación aprobatoria".
3. **Editar certificado.** Agrega estos elementos:

   | Elemento | Posición aproximada (mm) | Formato |
   |---|---|---|
   | Imagen de fondo | Cubre la página | `6_certificado/certificado_fondo.png` |
   | Nombre del estudiante | X 0, Y 74, ancho 297, centrado | Negrita, 32 pt, color #0B1220 |
   | Fecha (fecha de finalización del curso) | X 17, Y 170, ancho 70, centrado | 12 pt, color #E4007C |
   | Código | X 210, Y 170, ancho 70, centrado | 12 pt, color #E4007C |

4. Usa **Vista previa en PDF** y ajusta las posiciones Y si algo se encima. Compara con `certificado_muestra.png`.
5. **Opcional:** activa "Verificar certificado" para que cualquiera pueda comprobar el código.

### Camino sin complemento

La insignia **Plan completo** funciona como constancia digital. Moodle la entrega por correo y la persona la puede descargar.

Si alguien necesita la constancia en papel, se hace a mano con `certificado_muestra.png` como modelo.

## 6. Qué no hacer

- No dar puntos por ver páginas.
- No publicar nombres en rankings.
- No pedir datos reales para aprobar.
- No crear insignias con criterios que dependan de montos de dinero o de contratar productos.
