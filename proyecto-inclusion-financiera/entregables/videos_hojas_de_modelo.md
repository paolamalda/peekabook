# Hojas de modelo de los personajes · videos con IA

Complemento de `videos_fundamentos.md` (punto 4). Versión 1 · 5 de octubre de 2026.

## 1. Qué es y para qué sirve

Una **hoja de modelo** es el «documento de identidad» visual de un personaje: un conjunto de imágenes de referencia que muestran cómo se ve siempre (cara, cuerpo, ropa, colores, objetos y expresiones). Los generadores de video con IA inventan detalles en cada clip; si no se les da una referencia, el mismo personaje cambia de cara, de edad o de ropa entre un video y otro. Con la hoja de modelo:

- el personaje se reconoce en los 40 a 80 videos de su curso;
- cualquier persona del equipo genera clips iguales sin adivinar;
- si cambiamos de herramienta, la identidad del personaje no se pierde.

Se hace **una vez por personaje**, antes de producir cualquier video, y se aprueba como si fuera un logotipo.

## 2. Qué lleva cada hoja (6 láminas)

| Lámina | Contenido | Para qué |
|---|---|---|
| A. Giro completo | Frente, tres cuartos, perfil y espalda, cuerpo completo, de pie y en posición neutra | Que la IA reconstruya al personaje desde cualquier ángulo |
| B. Cara de cerca | Frente y tres cuartos, a la altura de los hombros | Mantener rasgos, edad y tono de piel |
| C. Expresiones | 6 caras: tranquila, preocupada, sorprendida, aliviada, pensativa y contenta | Las emociones que piden los guiones, sin exagerar |
| D. Ropa y objetos | Ropa de diario y, si aplica, de trabajo; sus objetos fijos (celular, mochila de repartidor, bastón, morral) | Que la ropa no cambie entre clips |
| E. Escala | El personaje junto a los demás del curso y junto a una puerta | Que las alturas sean coherentes |
| F. Ficha de texto | Descripción fija en inglés, paleta con códigos de color y «nunca» del personaje | Lo que se copia en cada prompt |

## 3. Cómo se hace, paso a paso

1. **Ficha escrita.** Con el manual del curso se llena la ficha (sección 6): edad, origen, cuerpo, piel, cabello, ropa, colores, objeto distintivo, carácter y lo que nunca debe tener.
2. **Primera imagen (lámina A).** Se genera con el prompt de la sección 5 en el generador de imágenes o de video elegido. Se piden 4 variantes y se escoge una.
3. **Aprobación del rostro.** Paola aprueba la cara y el cuerpo. Desde aquí no se cambia nada sin nueva aprobación.
4. **Láminas B a E.** Se generan **usando la imagen aprobada como referencia** (función de imagen de referencia, «personaje», «elemento» o imagen a imagen, según la herramienta).
5. **Revisión de diversidad y estereotipos** con la lista de la sección 8.
6. **Guardar y nombrar** (sección 9). La ficha F se copia tal cual en el bloque [PERSONAJE] de todos los prompts del curso.
7. **Prueba de consistencia:** 3 clips cortos del personaje en escenas distintas. Si en alguno cambia la cara o la ropa, se ajusta la ficha o se agrega una referencia antes de producir.

Las funciones exactas para usar referencias cambian por herramienta y por versión; al elegirla, se documenta aquí cómo se carga la referencia en esa herramienta.

## 4. Reglas de consistencia

- **Rasgos fijos, nunca negociables:** tono de piel, forma de cara, peinado, complexión, edad aparente y un objeto distintivo.
- **Ropa de diario fija por curso**; solo cambia si el guion lo pide (por ejemplo, uniforme de trabajo), y esa variante también se aprueba.
- **Colores de la marca en la ropa** (azul marino, magenta, rosa) sin que parezca uniforme corporativo.
- **Misma descripción en inglés, palabra por palabra,** en todos los prompts del personaje.
- **Una referencia visual por clip**, siempre la lámina A aprobada (y la C si el clip pide una emoción).
- **Nada de texto, logos ni marcas** en ropa u objetos.

## 5. Prompts de las láminas

**Lámina A · giro completo**
```
Character turnaround sheet, stylized 3D animated film style, soft rounded shapes, warm natural lighting,
plain light gray background, four views side by side: front, three-quarter, side profile and back,
full body, standing in a relaxed neutral pose, same character in all views.
[FICHA DEL PERSONAJE]
No text, no letters, no logos, no brand names, no accessories other than listed.
```

**Lámina B · cara**
```
Close-up portrait sheet of the same character, stylized 3D animated film style, front and three-quarter view,
shoulders up, soft studio lighting, plain light background. [FICHA DEL PERSONAJE]
Keep exactly the same face, skin tone, hair and age as the reference image. No text, no logos.
```

**Lámina C · expresiones**
```
Expression sheet of the same character, stylized 3D animated film style, six head-and-shoulders portraits in a grid:
calm, worried, surprised, relieved, thoughtful, happy. Subtle, natural, adult expressions, not cartoonish.
[FICHA DEL PERSONAJE] Same face as the reference image. No text, no labels, no logos.
```

**Lámina D · ropa y objetos**
```
Outfit and props sheet of the same character, stylized 3D animated film style, full body in everyday clothes,
and separately the props: [OBJETOS]. Plain light background. [FICHA DEL PERSONAJE]
No text, no logos, no brand names on clothes or props.
```

**Lámina E · escala**
```
Lineup of characters standing side by side, stylized 3D animated film style, full body, front view,
plain light background, a simple door frame on the side for scale: [PERSONAJE 1], [PERSONAJE 2], [PERSONAJE 3].
Consistent proportions. No text, no logos.
```

Para **Tu Comunidad** (animales) se agrega a todas las láminas:
```
Anthropomorphic animal character standing upright, dignified and gentle, adult, not childish or cartoonish,
everyday rural Mexican clothing, no traditional costume stereotypes.
```

## 6. Ficha del personaje (plantilla)

```
Nombre:                       Curso:                      Papel: guía / secundario
Edad:                         Origen:                     Ocupación:
Cuerpo (estatura, complexión):
Piel:                         Cabello:                    Rasgos:
Ropa de diario:               Colores (códigos):
Objeto distintivo:
Carácter (3 palabras):
Nunca: (lo que no debe tener ni hacer)
Descripción en inglés para los prompts (1 a 3 líneas, fija):
```

## 7. Fichas listas (personajes guía)

### Alex · Tu Dinero / Your Money (guía, con Mar)
- 35 años, mexicano, vive en Los Ángeles; cobra por nómina y hace trabajos con su camioneta.
- Complexión media, piel morena clara, cabello negro corto, barba muy corta.
- Polo azul marino, pantalón de mezclilla, botas de trabajo; llaves de la camioneta.
- Carácter: trabajador, cuidadoso, cariñoso.
- Nunca: ropa de marca, joyas llamativas, gesto de enojo.
```
Alex, a 35-year-old Mexican man living in Los Angeles, medium build, light-brown skin, short black hair,
very short beard, kind eyes; navy blue polo shirt, blue jeans, brown work boots; holds a set of truck keys.
```

### Mar · Tu Dinero / Your Money
- 33 años, mexicana, trabaja en un restaurante y vende comida por encargo.
- Complexión media, piel morena, cabello negro largo recogido en una coleta.
- Blusa magenta de manga corta, pantalón negro, delantal azul marino cuando trabaja; celular.
- Carácter: decidida, práctica, alegre.
```
Mar, a 33-year-old Mexican woman, medium build, brown skin, long black hair in a ponytail; short-sleeved magenta blouse,
black pants, navy apron when working; holds a phone. Warm, practical, confident.
```

### Doña Juana · Tu Comunidad (venada, guía)
- Mayor, de una comunidad de la Montaña de Guerrero; cobra su pensión.
- Venada de pie, rostro amable, ojos grandes y serenos.
- Rebozo azul marino con rayas rosas delgadas, blusa clara, falda azul; morral tejido al hombro.
- Carácter: digna, prudente, cariñosa.
- Nunca: traje «típico» genérico, rasgos infantiles, gesto de miedo exagerado.
```
Doña Juana, an older anthropomorphic female deer standing upright, gentle face with large calm eyes,
dignified and adult; navy blue shawl with thin pink stripes, light blouse, long blue skirt, woven shoulder bag.
```

### Beto · Tu Ruta (guía)
- 28 años, reparte en moto en Guadalajara.
- Delgado, piel morena, cabello corto ondulado.
- Chamarra azul marino, casco gris, mochila térmica de reparto sin logotipos; celular en soporte.
- Carácter: rápido, responsable, de buen humor.
```
Beto, a 28-year-old Mexican man, slim build, brown skin, short wavy black hair; navy blue jacket, gray helmet,
plain insulated delivery backpack with no logos, phone in a handlebar mount.
```

Las demás fichas se llenan con el manual de cada curso, en este orden de prioridad (piloto primero).

## 8. Lista de revisión de cada hoja

- [ ] Se ve adulto y digno; nada caricaturesco ni infantil (también los animales).
- [ ] Sin estereotipos de origen, género, edad, discapacidad o clase.
- [ ] Ropa cotidiana, sin lujo ni pobreza exagerada, sin marcas ni texto.
- [ ] Rasgos iguales en las láminas A a E.
- [ ] Manos, cara y proporciones sin deformaciones.
- [ ] Se distingue de los otros personajes del curso (silueta y color).
- [ ] Respeta los nombres permitidos (lista de nombres prohibidos del manual).

## 9. Cómo se guardan

```
cursos/<programa>/videos/personajes/
  alex_A_giro.png   alex_B_cara.png   alex_C_expresiones.png   alex_D_ropa.png
  elenco_E_escala.png
  fichas.md        (ficha F de cada personaje, con la descripción en inglés)
```

Cada hoja aprobada lleva fecha y versión en `fichas.md`. Si una hoja cambia, todos los clips nuevos usan la nueva versión y los anteriores se revisan.

## 10. Elencos y personajes guía por programa

Las versiones en inglés comparten personajes con su versión en español: son **15 elencos**.

| Programa | Personaje guía | Elenco secundario |
|---|---|---|
| Tu Dinero / Your Money | **Alex y Mar** | Rubén, Daniela, Rosa, Andrés |
| Tu Turno | **Don Chuy** | Karla, Ramiro, Beto |
| Tu Patrimonio | **Lucía** | Carmen, Elena, Maru |
| Tu Trabajo | **Doña Tere** | Chayo, Mari, Rosa |
| Tu Idea | **Emilio** | Santi, Naomi, Valeria |
| Tu Talento | **Toño** | Gael, Valeria, Renata |
| Tu Negocio (México) | **Rosa** | Don Pepe, Mariana, Toño |
| Tu Negocio EE. UU. / Your Business | **Don Ramón** | Lupita, Daniela, Javier |
| Tu Regreso | **Don Rafa** | Lupita, Memo, Chayo |
| Tu Pensión | **Doña Mago** | Don Toño, Doña Bertha, Sofía |
| Tu Costa | **Doña Chepa** | Don Mel, Julián, Yesenia |
| Tu Comunidad (animales) | **Doña Juana** (venada) | Rosa (tejona), Don Pedro (jaguar), Marta (colibrí); tlacuache y coyote |
| Tu Autonomía | **Lucía** | Leticia, Doña Rosario, Andrea |
| Tu Ruta | **Beto** | Mariana, Kevin, Don Chava |
| Tu Temporada | **Don Efrén** | Rosaura, Juan Carlos, Doña Imelda, Ramiro |

**Nombres que se repiten entre cursos** (Lucía, Rosa, Daniela, Lupita, Toño, Valeria, Beto, Ramiro, Chayo): son personajes distintos en cada curso y deben verse distintos. Se diferencian con el nombre del curso en el archivo (`tu_patrimonio_lucia_A_giro.png` y `tu_autonomia_lucia_A_giro.png`).

**Carga de trabajo:** unos 60 personajes en total. Para el piloto bastan **6 hojas**: Alex, Mar, Rubén y Daniela (Tu Dinero), y Doña Juana y el tlacuache (Tu Comunidad).
