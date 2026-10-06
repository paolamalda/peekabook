# Instrucciones para Claude: instalar "Tu Dinero, Tu Familia, Tu Futuro" (Moodle 4.5)

Vas a crear el curso **Tu Dinero, Tu Familia, Tu Futuro** en academia.desarrollatalento.com. El sitio usa Moodle 4.5, el tema Boost, Level Up (block_xp) y el complemento **Certificado personalizado** (mod_customcert).

Si en el sitio existen otros cursos, **no los toques.**

Trabaja con el navegador y con la sesión de administrador que la persona abrió.

Reglas:

- Usa solo la interfaz web.
- No uses SSH.
- No instales complementos.
- No cambies la configuración del sitio.
- No toques otros cursos.
- Si algo no coincide con estas instrucciones, detente y pregunta.

## En Moodle 4.5: dónde está cada cosa

El sitio usa **Moodle 4.5**. Donde estas instrucciones nombran un menú, búscalo así:

| Para | En Moodle 4.5 |
|---|---|
| Editar el curso | Interruptor **Modo de edición**, arriba a la derecha |
| Configuración, participantes, insignias, banco de preguntas, banco de contenido, finalización | Menú del curso (pestañas bajo el título): *Configuración*, *Participantes* y *Más* > *Banco de preguntas*, *Banco de contenido*, *Insignias*, *Finalización del curso* |
| Métodos de inscripción | *Participantes* > selector de arriba > *Métodos de inscripción* |
| Importar capítulos de un libro | Dentro del libro, menú de acciones (⋮ o *Más*) > *Importar capítulo* |
| Importar entradas del glosario | Dentro del glosario, selector o menú de acciones > *Importar entradas* |
| Importar preguntas de una encuesta (Retroalimentación) | Dentro de la actividad, pestaña *Preguntas* > menú > *Importar preguntas* |
| Ver como estudiante | Menú de tu usuario (arriba a la derecha) > *Cambiar rol a…* > *Estudiante* |
| Finalización de una actividad | En su configuración, sección *Condiciones de finalización* |

**Para ahorrar horas** (el curso tiene muchas piezas):

1. **Finalización predeterminada antes de crear los libros:** *Más > Finalización del curso* > selector > *Finalización de actividad predeterminada*. Para **Libro**: "Ver". Para **Cuestionario**: "Recibir una calificación aprobatoria". Así cada libro nuevo ya nace con su finalización.
2. **Edición masiva:** en modo de edición, *Edición masiva* (arriba a la derecha) permite mover, mostrar u ocultar varias actividades a la vez.
3. **Trabaja por etapas y reporta en cada una:** primero la sección General (Bienvenida, foro, «Mi meta», encuesta de inicio, «Tu punto de partida») y la Parte 1 completa. Detente, toma capturas y reporta a la persona antes de seguir con las demás partes.
4. Si una opción de estas instrucciones no existe con ese nombre en 4.5, usa la equivalente y anótala en el reporte.

**Mosaicos (Tiles) en 4.5:** si *Usar submosaicos para las actividades* o *Mostrar progreso* no aparecen en la configuración del curso, pueden estar desactivados para todo el sitio; no cambies la configuración del sitio: repórtalo.

**Level Up en 4.5:** las versiones nuevas agrupan las reglas en *Level Up > Puntos*. Si existe la regla de **finalización de actividad**, úsala con 25 puntos en lugar del evento. La *Clasificación* puede llamarse *Tabla de posiciones*.

## 0. Antes de empezar

1. Confirma que no existe un curso con nombre corto `TDTF-CA-ES`. Si existe, detente y pregunta.
2. Revisa en *Administración del sitio > Extensiones > Resumen de extensiones* si existen **Certificado personalizado** y **Level Up**. Anótalo para el reporte.
3. Si el sitio todavía no tiene actividades H5P, la primera que subas instala sus librerías: súbela con la cuenta de administración. Si aparece un error de librerías, detente y reporta el mensaje exacto.

## 1. Crear el curso

| Campo | Valor |
|---|---|
| Nombre | Tu Dinero, Tu Familia, Tu Futuro |
| Nombre corto | TDTF-CA-ES |
| Visibilidad | **Mostrar** |
| Formato | **Mosaicos** (Tiles). 7 secciones |
| Seguimiento de finalización | Sí |

**Formato Mosaicos:**
- *Mostrar progreso en los mosaicos*: **como porcentaje**.
- **Usar submosaicos para las actividades: Sí** (cada lección se ve como un mosaico dentro de su parte).
- Un ícono por parte acorde a su tema; la sección General arriba de los mosaicos.
- Oculta el bloque *Tabla de posiciones* o *Ranking* de Level Up si aparece en la columna derecha.

**Inscripción:** *Métodos de inscripción* > activa **Autoinscripción** con la **clave de inscripción** que te dé la persona (si no la tienes, deja "[por definir]" y repórtalo). Desactiva el acceso de invitados.

## 2. Secciones

| Sección | Nombre | Descripción |
|---|---|---|
| General | Bienvenida | Libro «Bienvenida», foro "Dudas y comentarios", encuesta de inicio, «Tu punto de partida» y «Mi meta» |
| 1 | Tu dinero en orden | Contenido de `1_libros/M1_resumen.html` |
| 2 | Bancos y envíos a casa | `M2_resumen.html` |
| 3 | Crédito sin sustos | `M3_resumen.html` |
| 4 | Protege lo tuyo | `M4_resumen.html` |
| 5 | Tu futuro | `M5_resumen.html` |
| 6 | Materiales de apoyo | "Casos, prácticas, glosario y dónde pedir ayuda." |
| 7 | Cierre y constancia | "Lo que lograste, tu constancia y hasta pronto." |

Descripción del foro "Dudas y comentarios": "No compartas números de cuenta, SSN, ITIN, contraseñas ni tu situación migratoria."

### Bienvenida y despedida (libros con diseño)

Son lo primero y lo último que ve la persona: no los omitas.

1. **Sección General, arriba de todo:** crea el libro `Bienvenida` (formato de capítulo "Nada", navegación "Texto") e importa `1_libros/Bienvenida_libro_Moodle.zip`, tipo "Cada archivo HTML representa un capítulo". Deben quedar 4 capítulos: Te damos la bienvenida, Cómo funciona el curso, Guía de contacto y comunidad, Antes de empezar. Finalización: "Ver".
2. Debajo, el foro **"Dudas y comentarios"** (foro general). **No crees un foro de presentaciones:** pedir que la gente se presente invita a compartir datos personales.
   Después, la tarea **"Mi meta"**: tipo *Tarea*, entrega "Texto en línea" (límite de 60 palabras), **sin calificación**, sin fecha límite, sin avisos a otros participantes; las entregas solo las ven la persona y el equipo del curso. Instrucciones: "En una frase: qué esperas del programa y qué quieres lograr. No escribas datos personales ni montos reales. Al final del curso la vuelves a abrir." Permite editar la entrega en cualquier momento. Finalización: "Enviar".
3. Debajo, la **Encuesta de inicio** (sección 8) y el cuestionario **«Tu punto de partida»**: importa `4_preguntas/diagnostica.gift.txt` (crea su propia categoría «Diagnóstica»), todas las preguntas, calificación sobre 0 (no cuenta para la calificación), **un intento**, tiempo máximo 10 minutos, revisión con respuesta correcta al terminar.
4. **Restringir acceso** de la primera lección de la Parte 1: el libro `Bienvenida` debe estar visto.
5. **Sección 7, arriba de todo:** crea el libro `Cierre y despedida` con la misma configuración e importa `1_libros/Cierre_libro_Moodle.zip` (4 capítulos: Lo que lograste, Tu plan sigue, Encuesta final y constancia, Hasta pronto). Restringir acceso: la autoevaluación de la última parte debe estar completa. Debajo van la encuesta final y la constancia.
6. **Guía para imprimir o compartir:** `7_guias/Guia_de_contacto_y_comunidad.html`. Ábrela en el navegador > Imprimir > Guardar como PDF, y compártela en la sesión presencial o por WhatsApp.

## 3. Lecciones: un libro por lección

La estructura completa (nombres, orden, archivos y minutos) está en `estructura_moodle.json`. En cada sección, por cada lección y en orden:

1. Crea un **Libro** con el nombre de la lección **tal cual** (la pregunta, sin claves como «M1 U01»). Formato de capítulo "Nada"; estilo de navegación "Texto".
2. Menú del libro > **Importar capítulo** > el zip de la lección (`1_libros/MN/NN_MN_UYY.zip`), tipo "Cada archivo HTML representa un capítulo". Deben quedar 4 capítulos: Empieza, Lo esencial, Profundiza, Practica.
3. **Finalización:** "Ver".
4. **Restringir acceso:** la lección anterior debe estar completa (la primera de cada parte, sin restricción; la primera de la parte 2 en adelante pide la última de la parte anterior). Muestra la lección bloqueada en gris, no oculta.

| Parte | Lecciones | Carpeta |
|---|---|---|
| Tu dinero en orden | 14 | `1_libros/M1/` |
| Bancos y envíos a casa | 13 | `1_libros/M2/` |
| Crédito sin sustos | 12 | `1_libros/M3/` |
| Protege lo tuyo | 12 | `1_libros/M4/` |
| Tu futuro | 12 | `1_libros/M5/` |

## 4. Libro de apoyo

En la sección 6, crea el libro `Materiales de apoyo` con la misma configuración e importa `1_libros/Apoyo_libro_Moodle.zip` (6 capítulos).

Debajo, crea el libro **`Para ir a fondo`** con la misma configuración e importa `1_libros/Fondo_libro_Moodle.zip` (6 capítulos: «Cómo ir a fondo» y uno por parte). Descripción: "Opcional. Para quien quiere leer las fuentes oficiales, las reglas y los documentos de cada tema." **Finalización: ninguna** (es opcional y no cuenta para terminar el curso).

En la misma sección 6, agrega un recurso **Archivo** llamado `Herramientas para tus cuentas (Excel)` con el archivo de `10_herramientas/`. Mostrar: "Forzar descarga". Descripción: "Presupuesto, lista de deudas, fondo de emergencia y meta con interés compuesto; además: el costo de cada envío, tus bienes y quién los recibe. Escribe solo en las celdas rosas; el archivo es tuyo y no se comparte." Finalización: "Ver".

## 5. Glosario

En la sección 6, crea el glosario `Palabras clave del curso` e importa `3_glosario/Glosario_curso_Moodle.xml`, destino "glosario actual".

## 6. Banco de preguntas y autoevaluaciones

1. *Banco de preguntas > Importar*: formato GIFT, `4_preguntas/banco_preguntas_v3_es.gift.txt`. Se crean *Tu Dinero v3.4/M1* a *M5*, con 189 preguntas.
2. En cada sección de módulo, crea el cuestionario `Autoevaluación del Módulo N`: aprobatoria 70, intentos ilimitados, calificación más alta, respuestas al azar, revisión con correcta y retroalimentación, finalización "Requiere calificación aprobatoria".
3. Agrega **todas** las preguntas de *Tu Dinero v3.4/MN*, 10 por página:

| M1 | M2 | M3 | M4 | M5 |
|---|---|---|---|---|
| 42 | 39 | 36 | 36 | 36 |

## 7. Práctica dentro de cada lección (63 H5P)

La práctica **no** va como actividad aparte en la sección: va incrustada en el capítulo «Practica» de su libro.

1. *Banco de contenido* del curso > **Subir** los 63 archivos de `2_h5p/MN/` (`MN_UYY_practica.h5p`).
2. Abre el capítulo «Practica» de cada libro en modo edición. Verás un recuadro rosa con el texto `[[H5P MN_UYY_practica.h5p]]`.
3. Borra **todo el recuadro** y en su lugar inserta el H5P con el botón **Insertar H5P** del editor, eligiendo ese archivo del banco de contenido.
4. Guarda y comprueba con *Cambiar rol a > Estudiante* que se vean las situaciones y preguntas, una por pantalla.

**Nota:** la práctica incrustada no registra calificación. El avance de cada lección se marca al verla, y la calificación del módulo sale de la autoevaluación.

**Orden final de cada sección:** las lecciones en orden y al final la autoevaluación (restringida a completar la última lección de la parte).

## 8. Encuestas del programa

En `8_encuestas/` están las encuestas y su documento `encuestas.md`. Usa el módulo **Retroalimentación** (Feedback), modo **anónimo**, y en cada una *Plantillas > Importar preguntas* con su XML (si la importación falla, créalas a mano con `encuestas.md`):

| Actividad | Sección | Archivo | Finalización |
|---|---|---|---|
| `Encuesta de inicio` | General | `encuesta_inicio.xml` | Enviar |
| `Encuesta final` | 7 | `encuesta_final.xml` | Enviar; es requisito de la constancia |
| `Seguimiento a 30 días` | 7 | `encuesta_seguimiento.xml` | Enviar |
| `Seguimiento a 90 días` | 7 | `encuesta_seguimiento.xml` | Enviar |

Restringe los seguimientos por fecha: 30 y 90 días después de la fecha de fin de la cohorte ("[por definir]"). La encuesta final es la evidencia de resultados del programa: no la omitas.

## 9. Level Up, insignias, finalización y constancia

Sigue `7_guias/guia_gamificacion.md`: secciones 2 (Level Up), 3 (8 insignias con `5_insignias/`; cada nombre lleva el curso para que sea único en la plataforma), 4 (finalización con las 5 autoevaluaciones) y 5 (constancia con la plantilla estándar y los datos de `6_constancia/constancia.md`). Si Level Up o Certificado personalizado no existen, no los instales: sáltate ese paso y repórtalo.

## Sección extra: Programas y apoyos

Esta sección va **aparte**: nada del curso depende de ella.

1. Agrega una sección **al final** del curso llamada `Programas y apoyos` (descripción: "Programas de gobierno y servicios públicos que pueden servirte. Información revisada; confírmala en el sitio oficial."). Elige un ícono de «ayuda» para su mosaico.
2. Crea el libro `Programas y apoyos` con la misma configuración e importa `1_libros/Programas_libro_Moodle.zip` (8 capítulos).
3. **Finalización: ninguna.** No lo incluyas en la finalización del curso ni en las restricciones de otras actividades, y no le des puntos.
4. **Para quitarla:** oculta la sección (ojo > Ocultar) o bórrala. El resto del curso sigue igual.
5. Si llega un paquete nuevo de este libro, reemplaza solo este libro.

## 10. Revisión final (con rol de estudiante)

- La portada muestra un mosaico por parte con su porcentaje; dentro de cada parte, un submosaico por lección sin claves técnicas.
- La primera lección: capítulos Empieza, Lo esencial, Profundiza y Practica; «Cuidado con estos errores» al final de Lo esencial; la práctica incrustada funciona.
- La segunda lección aparece bloqueada hasta ver la primera.
- No hay ranking ni tabla de posiciones visible.
- Una autoevaluación muestra 3 opciones por pregunta.
- El libro de apoyo muestra "Ver la clave" en los casos integradores y las preguntas frecuentes desplegables.

## 11. Reporte para la persona

Enlace del curso; libros por parte; H5P incrustadas; preguntas por autoevaluación; encuestas creadas; insignias activas; configuración de Level Up; estado de la constancia; lo que no pudiste hacer y por qué; capturas de la portada en mosaicos, una H5P, una autoevaluación y la vista previa de la constancia.

El curso queda **visible**, con inscripción por clave. Para la ficha del catálogo usa `tarjeta_catalogo.md`.
