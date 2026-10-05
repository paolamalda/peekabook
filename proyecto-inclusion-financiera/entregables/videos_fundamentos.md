# Videos de Desarrolla Talento · Fundamentos y prompts para generarlos con IA

Versión 1 · 5 de octubre de 2026 · basada en la entrevista con Paola.

Este documento es el parteaguas para los 678 videos de los 17 programas: lo que es igual en todos, cómo se escribe cada prompt y cómo se revisa cada video. Los guiones por lección están en `cursos/<programa>/videos/guiones_videos.md`.

## 1. Decisiones tomadas

| Tema | Decisión |
|---|---|
| Herramienta | Generador de video con IA (Sora, Veo, Runway, Kling u otro); falta elegir cuál. Los prompts sirven para cualquiera. |
| Estilo | **3D tipo animación**: personajes redondeados, materiales suaves, luz cálida. |
| Personajes | **Personas** en todos los programas; **animales solo en Tu Comunidad**. |
| Sonido | **Sin voz**. Música suave y efectos (monedas, teléfono, puerta). |
| Texto | Texto en pantalla **en todos los programas menos Tu Comunidad** (ahí solo el título). El texto, las ✓/✕ y los números **se agregan en edición**, nunca los genera la IA. |
| Formato | **Cuadrado 1:1** (1080 × 1080) para celular, Moodle y WhatsApp. |
| Tono | **Cálido y esperanzador, sereno y respetuoso**: situaciones reales, final donde la persona toma el control, ritmo pausado. |
| Apertura y cierre | Cortinilla de 1 a 2 s con el logo, el **personaje guía** del curso abre o cierra, y logo de Desarrolla Talento con el nombre del curso al final (2 s). |
| Revisión | Claude revisa contra el guion y la lista; prueba con personas del grupo; Paola aprueba. |
| Presupuesto | Por definir; se estima al elegir la herramienta, con un piloto. |

## 2. Lo que nunca aparece

- Marcas, logotipos, nombres de bancos, apps o tiendas reales; billetes y tarjetas genéricos.
- Violencia, amenazas o miedo explícito: fraude y extorsión se muestran con símbolos (una sombra en el teléfono, un ✕).
- Estereotipos o burlas: nadie se ve ignorante ni culpable; el problema es la situación.
- Discriminación de ningún tipo, incluida la de género, y violencia de género. Hombres y mujeres comparten tareas de la casa y decisiones de dinero.
- Lujo o aspiracional: sin autos de lujo, mansiones ni montones de dinero; metas reales.
- Texto, números o letras generados por la IA dentro de la imagen.
- Nombres prohibidos para personajes (lista en el manual de cada programa).
- La muerte explícita: se representa con una silla vacía, flores y una vela.

## 3. Cómo se ve todo (biblia de estilo)

- **Personas:** mexicanas y latinas diversas en tono de piel, edad, cuerpo y región; personas con discapacidad y adultos mayores de forma natural en todos los programas.
- **Lugares y ropa:** cotidianos (cocina, tiendita, calle, campo, oficina pequeña, transporte); ni lujo ni pobreza exagerada.
- **Paleta:** azul marino #0A3161, magenta #E4007C, rosa #FF4FA8, fondos claros #F5F7FB; dorado solo para monedas.
- **Luz y cámara:** luz cálida de día, cámara estable a la altura de los ojos, movimientos lentos (acercamiento suave, paneo corto); nada de cortes rápidos.
- **Señales fijas (en edición):** ✓ en círculo azul marino = así sí; ✕ en círculo magenta = así no; monedas doradas = dinero; candado = protegido; lupa = revisar; hojas de calendario = pasa el tiempo.
- **Texto en pantalla (en edición):** Figtree semibold, blanco sobre franja azul marino al pie, 56 px mínimo en 1080 × 1080, máximo 2 renglones; títulos en Bricolage Grotesque.
- **Música:** acústica suave (guitarra, marimba ligera), sin letra, volumen bajo; efectos breves.

## 4. Personajes fijos por programa (hoja de modelo)

Para que la IA mantenga al mismo personaje en todos los videos, **primero se genera una imagen de referencia por personaje** (frente, perfil y cuerpo completo) y se reutiliza en cada clip (función de imagen de referencia o de imagen a video de la herramienta).

Plantilla de la hoja de modelo:

```
Character reference sheet, stylized 3D animated film style, soft rounded shapes, warm lighting,
plain light background, front view, side view and full body, neutral friendly expression.
Character: [nombre], [edad] years old, [origen: Mexican / Latino], [tono de piel], [complexión],
[cabello], [ropa cotidiana con colores de la marca: navy blue, magenta accents], [rasgo distintivo: lentes,
bastón, mochila de repartidor…]. No text, no logos.
```

Personaje guía por programa (el protagonista que abre o cierra): el que ya usa cada curso (por ejemplo Alex y Mar en Tu Dinero; Doña Juana en Tu Comunidad, como venada). Las hojas de modelo se hacen al elegir la herramienta.

## 5. Estructura de cada video (40 a 55 s)

| Parte | Seg. | Qué pasa | Quién lo pone |
|---|---|---|---|
| Cortinilla | 1–2 | Logo animado | Plantilla de edición |
| Personaje guía | 2–3 | Saluda o mira a cámara | IA (clip corto reutilizable por programa) |
| Título | 3 | Pregunta de la lección | Edición |
| La situación | 6–8 | El problema del personaje | IA |
| Lo esencial | 2 o 3 × 6–8 | Una idea por clip | IA + texto en edición |
| ✕ Cuidado | 5–6 | El error que más cuesta | IA + ✕ en edición |
| ✓ Así lo resolvió | 6–8 | La decisión del personaje | IA + ✓ en edición |
| Idea clave | 4–5 | Frase para recordar | Edición sobre el último clip |
| Cierre | 2 | Logo y nombre del curso | Plantilla de edición |

Cada escena de IA es un **clip de 5 a 8 segundos**; un video tiene 5 o 6 clips que se unen en edición.

## 6. Plantilla del prompt de cada clip

Los prompts van en **inglés** (los generadores responden mejor) y siempre con los mismos bloques:

```
[ESTILO] Stylized 3D animated film style, soft rounded shapes, warm natural lighting, gentle colors
(navy blue, magenta and soft pink accents on a light background), square 1:1 frame.
[PERSONAJE] <descripción fija copiada de su hoja de modelo>  (+ imagen de referencia)
[ESCENA] <lugar cotidiano> — <qué hace el personaje, con una sola acción clara>.
[EMOCIÓN] <emoción visible y sobria: worried, relieved, calm, confident>.
[CÁMARA] Eye-level, steady camera, slow <push-in / pan>, <5–8> seconds.
[NEGATIVO] No text, no letters, no numbers, no logos, no brand names, no violence, no luxury items,
no stereotypes, no distorted hands or faces.
```

Reglas para escribirlos:
1. **Una acción por clip** (la IA falla con varias acciones seguidas).
2. **Objetos genéricos**: «a generic bank card», «a generic ATM», «coins».
3. **Las cifras nunca van en el prompt**; se ponen en edición.
4. **Copiar igual** el bloque de estilo y el del personaje en todos los clips del programa.

## 7. Ejemplos completos

### Tu Dinero · ¿Todo el dinero que recibo es dinero que gané? (personas, con texto)

| Clip | Prompt (bloques [ESTILO] y [NEGATIVO] iguales a la plantilla) | Texto en edición |
|---|---|---|
| Situación | [PERSONAJE] Alex, 34, Latino man, medium-brown skin, short dark hair, navy work polo. [ESCENA] Small kitchen on a Friday evening; Alex looks at a phone showing a banking screen with no readable text and smiles, surprised. [EMOCIÓN] Pleasantly surprised. [CÁMARA] Slow push-in, 6 s. | «Alex ve más dinero que nunca en su cuenta.» |
| Idea 1 | [ESCENA] Four large floating cards appear one by one beside Alex: a paycheck envelope, a hand lending coins, two arrows between two piggy banks, a store bag with a return arrow. [EMOCIÓN] Curious. [CÁMARA] Static, 7 s. | «No todo lo que entra es ingreso.» |
| Idea 2 | [ESCENA] On a kitchen table, a pile of gold coins; a hand removes a third of the pile and sets it aside on a small note. [EMOCIÓN] Thoughtful. [CÁMARA] Top-down, slow, 6 s. | «Lo que tienes − lo que debes = lo que es tuyo.» |
| ✕ Cuidado | [ESCENA] Alex and Mar in a store pointing at a refrigerator; behind them a calendar page turns and their wallet looks thinner. [EMOCIÓN] Worried. [CÁMARA] Slow pan, 6 s. | ✕ «Contar un adelanto como salario.» |
| ✓ Resolvió | [ESCENA] Alex at the table writes in a notebook next to the phone, sets aside a stack of coins labeled with a small blank tag, and nods to Mar. [EMOCIÓN] Calm, confident. [CÁMARA] Slow push-in, 7 s. | ✓ «Anota el préstamo y cuándo lo pagas.» |

Idea clave en edición: «Un préstamo te da dinero para hoy, pero no te hace más rico.»

### Tu Comunidad · Tu apoyo es tuyo, completo (animales, sin texto)

```
[PERSONAJE] Doña Juana: an older female deer standing upright, gentle face, wearing a navy shawl with
thin pink stripes and a woven shoulder bag; stylized, dignified, not childish.
```

| Clip | [ESCENA] y [CÁMARA] |
|---|---|
| Situación | A small adobe house with a magenta roof in the mountains; Doña Juana holds a generic bank card and a neat stack of gold coins appears beside her. Static, 6 s. |
| ✕ | Next to a generic ATM, a smiling opossum in a hat takes half of Doña Juana's coins; she looks sad. Slow push-in, 6 s. |
| Así sí (grupo) | Four animal neighbors beside a pickup truck; each drops one small coin into a glass jar. Slow pan, 7 s. |
| ✓ | Doña Juana at the ATM puts all her coins into her shoulder bag and smiles; her neighbors wait behind her. Static, 6 s. |

En edición: título, ✕ y ✓; sin más texto.

## 8. Edición (plantilla única)

1. Proyecto 1080 × 1080, 30 fps.
2. Cortinilla (1–2 s) → clip del personaje guía → título → clips de la lección → idea clave → cierre con logo y nombre del curso.
3. Franja de texto al pie, señales ✓/✕ y monedas con números como capas de la plantilla.
4. Música suave a −20 dB; efectos breves.
5. Exportar MP4 H.264, menos de 2 MB por cada 45 s si es posible; nombre `PROGRAMA_M1_U01.mp4`.

## 9. Lista de revisión (Claude, antes de que Paola lo vea)

- [ ] Coincide con el guion: misma situación, ideas, error y solución.
- [ ] Texto sin errores y legible en celular (2 renglones máximo); en Tu Comunidad, solo título.
- [ ] Sin texto, letras ni números generados por la IA dentro de la imagen.
- [ ] Mismo personaje que en los demás videos del programa.
- [ ] Sin marcas, violencia, estereotipos, discriminación ni lujo.
- [ ] Manos, caras y objetos sin deformaciones visibles.
- [ ] Duración 40 a 55 s; formato 1:1; peso razonable.
- [ ] Final esperanzador: la persona toma el control.

Después: prueba con 3 a 5 personas del grupo (¿qué entendiste?) y aprobación de Paola.

## 10. Plan sugerido

1. **Elegir herramienta** probando el mismo clip en 2 o 3 generadores (calidad, consistencia del personaje y costo).
2. **Hojas de modelo** de los personajes guía de Tu Dinero y Tu Comunidad.
3. **Piloto:** 5 videos de Tu Dinero y 3 de Tu Comunidad; medir tiempo y costo por video.
4. Con ese costo, decidir el ritmo para los 678.
5. Agregar a cada guion los prompts por clip con esta plantilla (lo puede hacer el generador de guiones).
