# Adapta el README de instalación y la guía de gamificación a Moodle 4.5 (el sitio se actualizó en octubre de 2026).
import re

NOTA_ES = """## En Moodle 4.5: dónde está cada cosa

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

"""

NOTA_EN = """## In Moodle 4.5: where everything is

The site runs **Moodle 4.5**. Where these instructions name a menu, look for it like this:

| To | In Moodle 4.5 |
|---|---|
| Edit the course | **Edit mode** toggle, top right |
| Settings, participants, badges, question bank, content bank, completion | Course menu (tabs under the title): *Settings*, *Participants* and *More* > *Question bank*, *Content bank*, *Badges*, *Course completion* |
| Enrolment methods | *Participants* > selector at the top > *Enrolment methods* |
| Import chapters into a book | Inside the book, actions menu (⋮ or *More*) > *Import chapter* |
| Import glossary entries | Inside the glossary, selector or actions menu > *Import entries* |
| Import questions into a survey (Feedback) | Inside the activity, *Questions* tab > menu > *Import questions* |
| View as a student | Your user menu (top right) > *Switch role to…* > *Student* |
| Activity completion | In its settings, *Completion conditions* section |

**To save hours** (the course has many pieces):

1. **Default completion before creating the books:** *More > Course completion* > selector > *Default activity completion*. For **Book**: "View". For **Quiz**: "Receive a passing grade". Every new book then starts with its completion set.
2. **Bulk edit:** in edit mode, *Bulk edit* (top right) lets you move, show or hide several activities at once.
3. **Work in stages and report at each one:** first the General section (Welcome, forum, "My goal", start survey, "Your starting point") and all of Part 1. Stop, take screenshots and report to the person before continuing with the other parts.
4. If an option in these instructions has a different name in 4.5, use the equivalent and note it in the report.

**Tiles in 4.5:** if *Use sub-tiles for activities* or *Show progress* don't appear in the course settings, they may be turned off for the whole site; don't change site settings: report it.

**Level Up in 4.5:** newer versions group the rules under *Level Up > Points*. If there is an **activity completion** rule, use it with 25 points instead of the event. *Ladder* may be called *Leaderboard*.

"""


def adaptar(readme, guia, en=False):
    if en:
        readme = readme.replace("(Moodle 3.10)", "(Moodle 4.5)").replace("Moodle 3.10, the Boost theme, Level Up 3.15.2", "Moodle 4.5, the Boost theme, Level Up (block_xp)")
        guia = guia.replace("Moodle 3.10 with Level Up (block_xp) 3.15.2", "Moodle 4.5 with Level Up (block_xp)")
        readme = readme.replace("*Course administration > ", "*More > ")
        guia = guia.replace("*Course administration > ", "*More > ")
        readme = re.sub(r"\n## 0\. ", "\n" + NOTA_EN + "## 0. ", readme, count=1)
    else:
        readme = readme.replace("(Moodle 3.10)", "(Moodle 4.5)").replace("Moodle 3.10, el tema Boost, Level Up 3.15.2", "Moodle 4.5, el tema Boost, Level Up (block_xp)")
        guia = guia.replace("Moodle 3.10 con Level Up (block_xp) 3.15.2", "Moodle 4.5 con Level Up (block_xp)")
        readme = readme.replace("*Administración del curso > ", "*Más > ")
        guia = guia.replace("*Administración del curso > ", "*Más > ")
        readme = re.sub(r"\n## 0\. ", "\n" + NOTA_ES + "## 0. ", readme, count=1)
    assert "3.10" not in readme + guia
    return readme, guia
