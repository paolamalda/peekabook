# Genera instalacion/README_INSTALAR_<X>_PARA_CLAUDE.md y instalacion/guia_gamificacion.md (español) desde curso.json.
import os, re


def ux3(readme, guia, CFG, MODS, n, tot, nm, sec_eval, cat):
    """Formato UX3: mosaicos con submosaicos, un libro por lección con la práctica incrustada, sin ranking."""
    NOMB = {m: CFG.get("nombres", {}).get(m, {}).get("titulo", t) for m, t in MODS.items()}
    def rep(a, b, s):
        assert a in s, a[:60]
        return s.replace(a, b)
    readme = rep("| Formato | **Mosaicos** (Tiles) si está instalado; si no, Temas. " + str(sec_eval) + " secciones |",
                 "| Formato | **Mosaicos** (Tiles). " + str(sec_eval) + " secciones |", readme)
    readme = re.sub(r"\*\*Formato Mosaicos \(si existe\):\*\*.*\n", """**Formato Mosaicos:**
- *Mostrar progreso en los mosaicos*: **como porcentaje**.
- **Usar submosaicos para las actividades: Sí** (cada lección se ve como un mosaico dentro de su parte).
- Un ícono por parte acorde a su tema; la sección General arriba de los mosaicos.
- Oculta el bloque *Tabla de posiciones* o *Ranking* de Level Up si aparece en la columna derecha.
""", readme)
    for i, m in enumerate(MODS, 1):
        readme = readme.replace(f"| {i} | {MODS[m]} |", f"| {i} | {NOMB[m]} |")
    filas = "\n".join(f"| {NOMB[m]} | {n[m]} | `1_libros/{m}/` |" for m in MODS)
    readme = re.sub(r"## 3\. Libros de lecciones\n.*?(?=\n## 4\.)", f"""## 3. Lecciones: un libro por lección

La estructura completa (nombres, orden, archivos y minutos) está en `estructura_moodle.json`. En cada sección, por cada lección y en orden:

1. Crea un **Libro** con el nombre de la lección **tal cual** (la pregunta, sin claves como «M1 U01»). Formato de capítulo "Nada"; estilo de navegación "Texto".
2. Menú del libro > **Importar capítulo** > el zip de la lección (`1_libros/MN/NN_MN_UYY.zip`), tipo "Cada archivo HTML representa un capítulo". Deben quedar 4 capítulos: Empieza, Lo esencial, Profundiza, Practica.
3. **Finalización:** "Ver".
4. **Restringir acceso:** la lección anterior debe estar completa (la primera de cada parte, sin restricción; la primera de la parte 2 en adelante pide la última de la parte anterior). Muestra la lección bloqueada en gris, no oculta.

| Parte | Lecciones | Carpeta |
|---|---|---|
{filas}
""", readme, flags=re.S)
    readme = re.sub(r"## 7\. Actividades H5P \(\d+\)\n.*?(?=\n## 8\.)", f"""## 7. Práctica dentro de cada lección ({tot} H5P)

La práctica **no** va como actividad aparte en la sección: va incrustada en el capítulo «Practica» de su libro.

1. *Banco de contenido* del curso > **Subir** los {tot} archivos de `2_h5p/MN/` (`MN_UYY_practica.h5p`).
2. Abre el capítulo «Practica» de cada libro en modo edición. Verás un recuadro rosa con el texto `[[H5P MN_UYY_practica.h5p]]`.
3. Borra **todo el recuadro** y en su lugar inserta el H5P con el botón **Insertar H5P** del editor, eligiendo ese archivo del banco de contenido.
4. Guarda y comprueba con *Cambiar rol a > Estudiante* que se vean las situaciones y preguntas, una por pantalla.

**Nota:** la práctica incrustada no registra calificación. El avance de cada lección se marca al verla, y la calificación del módulo sale de la autoevaluación.

**Orden final de cada sección:** las lecciones en orden y al final la autoevaluación (restringida a completar la última lección de la parte).
""", readme, flags=re.S)
    readme = rep("- M1 U01: portada primero, dos botones de ruta, términos en color con su significado y recuadros \"Dato vigente\" o \"Antes de actuar, verifica\".\n- Una H5P por módulo abre, muestra 3 casos y registra calificación.",
                 "- La portada muestra un mosaico por parte con su porcentaje; dentro de cada parte, un submosaico por lección sin claves técnicas.\n- La primera lección: capítulos Empieza, Lo esencial, Profundiza y Practica; «Cuidado con estos errores» al final de Lo esencial; la práctica incrustada funciona.\n- La segunda lección aparece bloqueada hasta ver la primera.\n- No hay ranking ni tabla de posiciones visible.", readme)
    readme = readme.replace("páginas por libro; H5P por módulo;", "libros por parte; H5P incrustadas;")
    pts = (tot + nm) * 25
    guia = re.sub(r"## 1\. Qué hay en cada módulo\n.*?(?=\n\*\*Las autoevaluaciones)", f"""## 1. Qué hay en cada parte

| Actividad | Cuántas | Finalización |
|---|---|---|
| Libro por lección (con la práctica incrustada) | {tot} | Ver |
| Cuestionario "Autoevaluación del Módulo N" | 1 por parte ({nm}) | Calificación aprobatoria de 70% |
""", guia, flags=re.S)
    guia = re.sub(r"Completar todo el curso da unos .*?\| \*\*Total\*\* \|[^\n]*\n", f"""Completar todo el curso da unos {pts:,} puntos:

| Actividades | Cuántas | Puntos |
|---|---|---|
| Lecciones | {tot} | {tot * 25:,} |
| Autoevaluaciones | {nm} | {nm * 25:,} |
| **Total** | {tot + nm} | **{pts:,}** |
""", guia, flags=re.S)
    guia = rep("**Clasificación:** anonimato activado; mostrar solo vecinos cercanos o desactivarla.",
               "**Clasificación (ranking): desactivada.** En *Level Up > Clasificación* elige no mostrarla, y quita o esconde el bloque de tabla de posiciones. Cada persona ve solo sus puntos, su nivel y sus insignias.", guia)
    return readme, guia


def generar(D, CFG, lecciones):
    MODS = CFG["modulos"]; I = CFG["instalacion"]
    n = {m: len(lecciones(m)) for m in MODS}
    tot = sum(n.values()); nm = len(MODS)
    pts = (tot + 2 * nm) * 25
    sec_apoyo, sec_eval = nm + 1, nm + 2
    herr = "; y para tu negocio: costo y precio, punto de equilibrio y flujo de 8 semanas" if (CFG.get("negocio") or CFG.get("hojas_negocio")) else ""
    _H = {"quincena_turnos": "tu quincena con turnos extra", "pago_por_dia": "lo que ganas por día en cada casa", "ingreso_variable": "tus ingresos de 12 meses y tu fondo de sequía",
          "bienes": "tus bienes y quién los recibe", "envios": "el costo de cada envío", "adelantos": "adelantos a tu equipo", "semana_apps": "lo que te queda de verdad en la semana",
          "pension": "tus pensiones y tu mes", "temporada": "tu temporada: lo que ganas, envías y traes", "regreso": "tus primeros 90 días de regreso"}
    if CFG.get("hojas"): herr += "; además: " + ", ".join(_H[h] for h in CFG["hojas"] if h in _H)
    tit, corto = CFG["titulo"], I["nombre_corto"]
    cat, banco = f'{CFG["categoria"]} v{CFG["version"]}', CFG["banco"]
    filas_sec = "\n".join(f"| {i} | {t} | " + (f"Contenido de `1_libros/{m}_resumen.html`" if i == 1 else f"`{m}_resumen.html`") + " |"
                          for i, (m, t) in enumerate(MODS.items(), 1))
    filas_lib = "\n".join(f"| {m} | {n[m]} | {n[m] * 4} |" for m in MODS)
    cab_q = "| " + " | ".join(MODS) + " |\n|" + "---|" * nm + "\n| " + " | ".join(str(n[m] * 3) for m in MODS) + " |"
    otros = I.get("otros_cursos", "Si en el sitio existen otros cursos, **no los toques.**")
    extra = I.get("extra_readme", "")
    readme = f"""# Instrucciones para Claude: instalar "{tit}" (Moodle 3.10)

Vas a crear el curso **{tit}** en academia.desarrollatalento.com. El sitio usa Moodle 3.10, el tema Boost, Level Up 3.15.2 y el complemento **Certificado personalizado** (mod_customcert).

{otros}

Trabaja con el navegador y con la sesión de administrador que la persona abrió.

Reglas:

- Usa solo la interfaz web.
- No uses SSH.
- No instales complementos.
- No cambies la configuración del sitio.
- No toques otros cursos.
- Si algo no coincide con estas instrucciones, detente y pregunta.

## 0. Antes de empezar

1. Confirma que no existe un curso con nombre corto `{corto}`. Si existe, detente y pregunta.
2. Revisa en *Administración del sitio > Extensiones > Resumen de extensiones* si existen **Certificado personalizado** y **Level Up**. Anótalo para el reporte.
3. Si el sitio todavía no tiene actividades H5P, la primera que subas instala sus librerías: súbela con la cuenta de administración. Si aparece un error de librerías, detente y reporta el mensaje exacto.

## 1. Crear el curso

| Campo | Valor |
|---|---|
| Nombre | {tit} |
| Nombre corto | {corto} |
| Visibilidad | **Mostrar** |
| Formato | **Mosaicos** (Tiles) si está instalado; si no, Temas. {sec_eval} secciones |
| Seguimiento de finalización | Sí |

**Formato Mosaicos (si existe):** en la configuración del curso, *Mostrar progreso en los mosaicos*: **como porcentaje**; un ícono por módulo acorde a su tema; la sección General arriba de los mosaicos. Si Mosaicos no existe, usa Temas con "Mostrar una sección por página".

**Inscripción:** *Métodos de inscripción* > activa **Autoinscripción** con la **clave de inscripción** que te dé la persona (si no la tienes, deja "[por definir]" y repórtalo). Desactiva el acceso de invitados.

## 2. Secciones

| Sección | Nombre | Descripción |
|---|---|---|
| General | Bienvenida | Libro «Bienvenida», foro "Dudas y comentarios", encuesta de inicio, «Tu punto de partida» y «Mi meta» |
{filas_sec}
| {sec_apoyo} | Materiales de apoyo | "Casos, prácticas, glosario y dónde pedir ayuda." |
| {sec_eval} | Cierre y constancia | "Lo que lograste, tu constancia y hasta pronto." |

Descripción del foro "Dudas y comentarios": "{I['aviso_foro']}"

### Bienvenida y despedida (libros con diseño)

Son lo primero y lo último que ve la persona: no los omitas.

1. **Sección General, arriba de todo:** crea el libro `Bienvenida` (formato de capítulo "Nada", navegación "Texto") e importa `1_libros/Bienvenida_libro_Moodle.zip`, tipo "Cada archivo HTML representa un capítulo". Deben quedar 4 capítulos: Te damos la bienvenida, Cómo funciona el curso, Guía de contacto y comunidad, Antes de empezar. Finalización: "Ver".
2. Debajo, el foro **"Dudas y comentarios"** (foro general). **No crees un foro de presentaciones:** pedir que la gente se presente invita a compartir datos personales.
   Después, la tarea **"Mi meta"**: tipo *Tarea*, entrega "Texto en línea" (límite de 60 palabras), **sin calificación**, sin fecha límite, sin avisos a otros participantes; las entregas solo las ven la persona y el equipo del curso. Instrucciones: "En una frase: qué esperas del programa y qué quieres lograr. No escribas datos personales ni montos reales. Al final del curso la vuelves a abrir." Permite editar la entrega en cualquier momento. Finalización: "Enviar".
3. Debajo, la **Encuesta de inicio** (sección 8) y el cuestionario **«Tu punto de partida»**: importa `4_preguntas/diagnostica.gift.txt` (crea su propia categoría «Diagnóstica»), todas las preguntas, calificación sobre 0 (no cuenta para la calificación), **un intento**, tiempo máximo 10 minutos, revisión con respuesta correcta al terminar.
4. **Restringir acceso** de la primera lección de la Parte 1: el libro `Bienvenida` debe estar visto.
5. **Sección {sec_eval}, arriba de todo:** crea el libro `Cierre y despedida` con la misma configuración e importa `1_libros/Cierre_libro_Moodle.zip` (4 capítulos: Lo que lograste, Tu plan sigue, Encuesta final y constancia, Hasta pronto). Restringir acceso: la autoevaluación de la última parte debe estar completa. Debajo van la encuesta final y la constancia.
6. **Guía para imprimir o compartir:** `7_guias/Guia_de_contacto_y_comunidad.html`. Ábrela en el navegador > Imprimir > Guardar como PDF, y compártela en la sesión presencial o por WhatsApp.

## 3. Libros de lecciones

En cada sección de módulo:

1. Crea un libro: nombre `Lecciones del Módulo N`, formato de capítulo "Nada", finalización "Ver".
2. Menú del libro > **Importar capítulo** > `1_libros/MN_libro_Moodle.zip`, tipo "Cada archivo HTML representa un capítulo".
3. Comprueba que cada lección tenga su portada primero y 3 subcapítulos sangrados.

| Módulo | Capítulos | Páginas |
|---|---|---|
{filas_lib}

## 4. Libro de apoyo

En la sección {sec_apoyo}, crea el libro `Materiales de apoyo` con la misma configuración e importa `1_libros/Apoyo_libro_Moodle.zip` (6 capítulos).

Debajo, crea el libro **`Para ir a fondo`** con la misma configuración e importa `1_libros/Fondo_libro_Moodle.zip` ({nm + 1} capítulos: «Cómo ir a fondo» y uno por parte). Descripción: "Opcional. Para quien quiere leer las fuentes oficiales, las reglas y los documentos de cada tema." **Finalización: ninguna** (es opcional y no cuenta para terminar el curso).

En la misma sección {sec_apoyo}, agrega un recurso **Archivo** llamado `Herramientas para tus cuentas (Excel)` con el archivo de `10_herramientas/`. Mostrar: "Forzar descarga". Descripción: "Presupuesto, lista de deudas, fondo de emergencia y meta con interés compuesto{herr}. Escribe solo en las celdas rosas; el archivo es tuyo y no se comparte." Finalización: "Ver".

## 5. Glosario

En la sección {sec_apoyo}, crea el glosario `Palabras clave del curso` e importa `3_glosario/Glosario_curso_Moodle.xml`, destino "glosario actual".

## 6. Banco de preguntas y autoevaluaciones

1. *Banco de preguntas > Importar*: formato GIFT, `4_preguntas/{banco}`. Se crean *{cat}/M1* a *M{nm}*, con {tot * 3} preguntas.
2. En cada sección de módulo, crea el cuestionario `Autoevaluación del Módulo N`: aprobatoria 70, intentos ilimitados, calificación más alta, respuestas al azar, revisión con correcta y retroalimentación, finalización "Requiere calificación aprobatoria".
3. Agrega **todas** las preguntas de *{cat}/MN*, 10 por página:

{cab_q}

## 7. Actividades H5P ({tot})

Archivos en `2_h5p/MN/`, en orden. En cada sección, **después del libro** y en orden de lección:

1. *Agregar actividad > Actividad H5P*.
2. Nombre: `MN UYY · ¿Qué harías?`.
3. Sube `MN_UYY_que_harias.h5p`.
4. Opciones: descarga no, incrustar no, derechos de autor sí.
5. Calificación: seguimiento sí, "calificación más alta". Finalización: "El estudiante debe recibir una calificación".

**Orden final de cada sección:** libro, H5P en orden, autoevaluación.

**Comprueba:** abre 3 actividades al azar con *Cambiar rol a > Estudiante*. Debes ver 3 casos, 3 opciones por caso y la calificación al terminar.

## 8. Encuestas del programa

En `8_encuestas/` están las encuestas y su documento `encuestas.md`. Usa el módulo **Retroalimentación** (Feedback), modo **anónimo**, y en cada una *Plantillas > Importar preguntas* con su XML (si la importación falla, créalas a mano con `encuestas.md`):

| Actividad | Sección | Archivo | Finalización |
|---|---|---|---|
| `Encuesta de inicio` | General | `encuesta_inicio.xml` | Enviar |
| `Encuesta final` | {sec_eval} | `encuesta_final.xml` | Enviar; es requisito de la constancia |
| `Seguimiento a 30 días` | {sec_eval} | `encuesta_seguimiento.xml` | Enviar |
| `Seguimiento a 90 días` | {sec_eval} | `encuesta_seguimiento.xml` | Enviar |

Restringe los seguimientos por fecha: 30 y 90 días después de la fecha de fin de la cohorte ("[por definir]"). La encuesta final es la evidencia de resultados del programa: no la omitas.

## 9. Level Up, insignias, finalización y constancia

Sigue `7_guias/guia_gamificacion.md`: secciones 2 (Level Up), 3 (8 insignias con `5_insignias/`; cada nombre lleva el curso para que sea único en la plataforma), 4 (finalización con las {nm} autoevaluaciones) y 5 (constancia con la plantilla estándar y los datos de `6_constancia/constancia.md`). Si Level Up o Certificado personalizado no existen, no los instales: sáltate ese paso y repórtalo.
{extra}
## {11 if extra else 10}. Revisión final (con rol de estudiante)

- M1 U01: portada primero, dos botones de ruta, términos en color con su significado y recuadros "Dato vigente" o "Antes de actuar, verifica".
- Una H5P por módulo abre, muestra 3 casos y registra calificación.
- Una autoevaluación muestra 3 opciones por pregunta.
- El libro de apoyo muestra "Ver la clave" en los casos integradores y las preguntas frecuentes desplegables.

## {12 if extra else 11}. Reporte para la persona

Enlace del curso; páginas por libro; H5P por módulo; preguntas por autoevaluación; encuestas creadas; insignias activas; configuración de Level Up; estado de la constancia; lo que no pudiste hacer y por qué; capturas de la portada en mosaicos, una H5P, una autoevaluación y la vista previa de la constancia.

El curso queda **visible**, con inscripción por clave. Para la ficha del catálogo usa `tarjeta_catalogo.md`.
"""
    niveles = "\n".join(f"| {i} | {nom} | {p:,} | {cuando} |" for i, (nom, p, cuando) in enumerate(I["niveles"], 1))
    ins = "\n".join(f"| {fn}.png | {nom} · {CFG['categoria']} | {crit} | {desc} |" for (fn, tag, nom, icon), (crit, desc) in zip(CFG["insignias"], I["insignias_info"]))
    T = CFG["constancia"]; temas = "\n".join(f"   | Tema {i} | {t} |" for i, t in enumerate(T["mods"], 1))
    guia = f"""# Guía de actividades, puntos, insignias y constancia · {tit}

Esta guía es para Moodle 3.10 con Level Up (block_xp) 3.15.2 y el complemento Certificado personalizado (mod_customcert).

El objetivo es motivar sin competir. Los puntos premian avanzar, no la calificación perfecta. Nunca se muestra el nombre de nadie en una tabla.

## 1. Qué hay en cada módulo

| Actividad | Cuántas | Finalización |
|---|---|---|
| Libro "Lecciones del Módulo N" | 1 por módulo ({nm}) | Ver |
| Actividad H5P "MN UYY · ¿Qué harías?" | 1 por lección ({tot}) | Recibir calificación |
| Cuestionario "Autoevaluación del Módulo N" | 1 por módulo ({nm}) | Calificación aprobatoria de 70% |

**Configuración de cada actividad H5P:** sin botón de descarga, con botón de derechos de autor e incrustar desactivado; seguimiento de intentos con "Calificación más alta"; finalización "El estudiante debe recibir una calificación".

**Las autoevaluaciones:** usan el banco de {tot * 3} preguntas con tres opciones y retroalimentación, en las categorías *{cat}/M1* a *M{nm}*. Calificación aprobatoria de 70%, intentos ilimitados, respuestas en orden aleatorio y revisión con respuesta correcta y retroalimentación al terminar.

## 2. Level Up: niveles y puntos

**Reglas** (*Level Up > Reglas*):

1. Quita o pon en 0 las reglas predeterminadas.
2. **Por completar cualquier actividad:** 25 puntos, con el evento "Se ha actualizado la finalización de un módulo del curso" (`\\core\\event\\course_module_completion_updated`).
3. **Por participar en el foro:** 5 puntos, con el evento "Mensaje creado" (`\\mod_forum\\event\\post_created`).
4. Deja activada la protección contra trampas.

Completar todo el curso da unos {pts:,} puntos:

| Actividades | Cuántas | Puntos |
|---|---|---|
| Actividades H5P | {tot} | {tot * 25:,} |
| Libros | {nm} | {nm * 25:,} |
| Autoevaluaciones | {nm} | {nm * 25:,} |
| **Total** | {tot + 2 * nm} | **{pts:,}** |

**Niveles** (6 niveles, sin algoritmo automático):

| Nivel | Nombre | Puntos | Cuándo se alcanza, más o menos |
|---|---|---|---|
{niveles}

**Clasificación:** anonimato activado; mostrar solo vecinos cercanos o desactivarla.

## 3. Insignias

*Administración del curso > Insignias > Agregar una nueva insignia*. Imágenes en `5_insignias/`. Emisor: Desarrolla Talento. Vencimiento: nunca. Los nombres llevan el curso para que no se repitan en la plataforma: úsalos tal cual.

| Imagen | Insignia | Criterio (finalización de actividad, con aprobación) | Descripción |
|---|---|---|---|
{ins}

Al terminar, **activa** cada insignia.

## 4. Finalización del curso

*Administración del curso > Finalización del curso*: condición de finalización de actividades con **todas** las {nm} autoevaluaciones. Opcional: los {nm} libros.

## 5. Constancia de conclusión (Certificado personalizado)

1. En la sección "Evaluación y constancia", agrega **Certificado personalizado** con la **plantilla estándar de la plataforma** (sin imagen de fondo): nombre "Constancia de conclusión".
2. **Restringir acceso:** una condición de "Finalización de actividad" por cada una de las {nm} autoevaluaciones, "debe estar completa con calificación aprobatoria", y la **Encuesta final** enviada.
3. En la plantilla cambia solo estos datos (también están en `6_constancia/constancia.md`):

   | Campo | Texto |
   |---|---|
   | Título del curso | {tit} |
   | Línea | por concluir el programa de bienestar financiero {tit} |
{temas}

4. Revisa la **Vista previa en PDF** y activa "Verificar certificado".

Si Certificado personalizado no está instalado, la insignia **{CFG["insignias"][-1][2]} · {CFG["categoria"]}** funciona como constancia digital.

## 6. Qué no hacer

- No dar puntos por ver páginas.
- No publicar nombres en rankings.
- No pedir datos reales para aprobar.
- No ligar insignias ni constancia a contratar servicios o productos.
"""
    if CFG.get("ux") == 3: readme, guia = ux3(readme, guia, CFG, MODS, n, tot, nm, sec_eval, cat)
    import programas as _PG
    _bp = _PG.bloque_readme(os.path.basename(os.path.normpath(D)), False)
    if _bp: readme = re.sub(r"\n(## \d+\. (?:Revisión final|Final review))", lambda m: "\n" + _bp + m.group(1), readme, count=1)
    import iconos as _IC
    _ti = _IC.tabla(os.path.basename(os.path.normpath(D)), [v["titulo"] for v in CFG.get("nombres", {}).values()], False)
    if _ti: readme = readme.replace('- Un ícono por parte acorde a su tema; la sección General arriba de los mosaicos.', '- La sección General (Bienvenida) va arriba de los mosaicos.' + "\n\n" + '**Íconos de los mosaicos** (se eligen en modo de edición, en cada mosaico; si un nombre no aparece en el selector, usa el más parecido):' + "\n\n" + _ti + "\n")
    from moodle45 import adaptar
    readme, guia = adaptar(readme, guia, en=False)
    os.makedirs(os.path.join(D, "instalacion"), exist_ok=True)
    for f in os.listdir(os.path.join(D, "instalacion")):
        if f.startswith("README_INSTALAR_"): os.remove(os.path.join(D, "instalacion", f))
    open(os.path.join(D, "instalacion", I["readme"]), "w").write(readme)
    open(os.path.join(D, "instalacion", "guia_gamificacion.md"), "w").write(guia)
    print("README y guía de gamificación ·", tot, "lecciones ·", pts, "puntos")
