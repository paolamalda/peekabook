# Instrucciones para Claude: instalar el curso en Moodle

Eres Claude y vas a cargar el curso "Tu Dinero, Tu Familia, Tu Futuro" en el Moodle de Desarrolla Talento (HostGator), usando el navegador con la sesión de administrador que la persona abrió. Trabaja solo por la interfaz web de Moodle. No uses SSH, no instales plugins, no cambies la configuración del sitio y no toques otros cursos.

## Antes de empezar

1. Pide a la persona:
   - la URL del Moodle,
   - que ya haya iniciado sesión como administrador,
   - en qué categoría crear el curso,
   - confirmación de que hay un respaldo reciente del sitio (en cPanel o en *Administración del sitio > Cursos > Respaldos*). Si no hay respaldo, detente y avisa.
2. Anota la versión de Moodle: *Administración del sitio > Notificaciones* (pie de página). Si es 5.0 o superior, el banco de preguntas funciona por "módulo de banco de preguntas"; el paso 5 cambia (ver nota ahí).
3. Revisa que H5P esté habilitado (*Administración del sitio > H5P > Administrar tipos de contenido H5P*) y que el bloque Level Up exista. Si algo falta, anótalo y sigue; no lo instales.

## Qué hay en esta carpeta

| Carpeta o archivo | Uso |
|---|---|
| `libros/es/M1.zip` … `M5.zip` | Capítulos (una lección = un capítulo) para importar en un Libro por módulo |
| `libros/es/Apoyo.zip` | Bienvenida, casos, prácticas, glosario, ayuda y referencias |
| `libros/es/M1_resumen.html` … | Texto para la descripción de cada sección |
| `libros/en/` | Lo mismo en inglés, para un segundo curso |
| `preguntas/banco_preguntas_es.gift.txt` y `_en` | 175 preguntas por idioma |
| `guias/` | Guiones H5P y guía de Level Up e insignias (ES y EN) |

## Paso 1. Crear el curso (oculto)

*Administración del sitio > Cursos > Agregar un nuevo curso*:

- Nombre completo: `Tu Dinero, Tu Familia, Tu Futuro (piloto California)`
- Nombre corto: `TDTF-CA-ES`
- Visibilidad: **Ocultar** (se hace visible hasta que la persona lo apruebe)
- Formato: Temas, **7 secciones**
- Finalización: **Habilitar seguimiento de finalización = Sí**
- Idioma forzado: Español, si el paquete de idioma está instalado; si no, dejar sin forzar.

## Paso 2. Nombrar las secciones

Activa el modo de edición y renombra:

| Sección | Nombre | Descripción |
|---|---|---|
| General | Bienvenida | "Empieza aquí." |
| 1 | Módulo 1. Entiende tu dinero y organiza tu economía | contenido de `M1_resumen.html` |
| 2 | Módulo 2. Entiende el sistema financiero y planea tus remesas | `M2_resumen.html` |
| 3 | Módulo 3. Construye tu crédito y maneja tus deudas | `M3_resumen.html` |
| 4 | Módulo 4. Protege tu dinero, tu identidad y tu familia | `M4_resumen.html` |
| 5 | Módulo 5. Construye patrimonio y prepara tu futuro | `M5_resumen.html` |
| 6 | Materiales de apoyo | "Casos, prácticas, glosario y dónde pedir ayuda." |
| 7 | Evaluación y constancia | "Encuesta final y constancia de participación." |

## Paso 3. Libros con las lecciones

En cada sección 1 a 5:

1. *Agregar actividad o recurso > Libro*.
   - Nombre: `Lecciones del Módulo N`.
   - Formato de capítulo: Números.
   - Finalización: "Ver".
2. Al abrir el libro vacío, entra al menú del libro y elige **Importar capítulo**.
   - Sube `libros/es/MN.zip`.
   - Tipo: **Cada archivo HTML representa un capítulo**.
3. Verifica el número de capítulos:

   | Módulo | Capítulos |
   |---|---|
   | M1 | 14 |
   | M2 | 13 |
   | M3 | 10 |
   | M4 | 11 |
   | M5 | 11 |

En la sección 6, crea el libro `Materiales de apoyo` con `Apoyo.zip` (6 capítulos). Mueve el capítulo "Bienvenida" a la sección General si la interfaz lo permite; si no, déjalo ahí.

**Comprueba:** abre 2 capítulos al azar. Las tablas deben verse con bordes, las listas con viñetas y los enlaces de "Para saber más" deben ser clicables.

## Paso 4. Foro de dudas

En General, agrega un **Foro** de tipo "Foro para uso general" llamado `Dudas y comentarios`. Su descripción:

> "No compartas números de cuenta, SSN, ITIN, contraseñas ni tu situación migratoria."

## Paso 5. Banco de preguntas

*Curso > Más > Banco de preguntas > Importar*: formato **GIFT**, archivo `preguntas/banco_preguntas_es.gift.txt`.

- Se crean las categorías M1 a M5 con 175 preguntas. Los nombres de las preguntas empiezan con el código de lección, por ejemplo "M1 U01 P1".
- **Moodle 5.0 o superior:** primero crea (o usa) el banco de preguntas del curso (*Más > Bancos de preguntas*) e importa ahí.

## Paso 6. Cuestionarios (uno por módulo para el piloto)

Para no llenar el curso de actividades en la primera revisión, crea **un cuestionario por módulo**. Después se podrá dividir por lección.

- Nombre: `Autoevaluación del Módulo N`.
- Calificación aprobatoria: 70%.
- Intentos: ilimitados.
- Revisión: mostrar respuesta y retroalimentación después del intento.
- Finalización: "Recibir calificación aprobatoria".
- Agrega todas las preguntas de la categoría MN.

## Paso 7. H5P (solo 3 de muestra en esta etapa)

Sigue `guias/Guiones_H5P_ES.docx` y crea estas tres en su sección, para que la persona vea cómo lucen:

- **M1 U01:** Drag and Drop.
- **M2 U08:** Single Choice Set.
- **M4 U01:** Single Choice Set.

Si el tipo de contenido no está instalado, anótalo y no lo instales.

## Paso 8. Level Up e insignias

Si el bloque Level Up existe, agrégalo al curso y configura los 6 niveles de `guias/Guia_LevelUp_Insignias_ES.docx`. Anota si es la versión gratuita o Level Up+.

**No crees insignias todavía.** La persona las aprobará después de ver el curso.

## Paso 9. Reporte final (obligatorio)

Entrega a la persona:

1. Enlace al curso y confirmación de que está **oculto**.
2. Tabla de lo que se creó, con conteos: secciones, capítulos por libro, preguntas importadas, cuestionarios, H5P.
3. Capturas de pantalla:
   - portada del curso,
   - un capítulo con tabla,
   - un cuestionario en vista previa,
   - una actividad H5P.
4. Lista de problemas encontrados y lo que no se pudo hacer, con el mensaje de error exacto.

## Reglas

- Nunca pidas ni escribas SSN, ITIN, contraseñas ni datos personales de participantes.
- No hagas visible el curso ni inscribas participantes.
- Si un paso falla dos veces, detente en ese paso, repórtalo y sigue con el siguiente si es independiente.
