# Prompt para reescribir las lecciones en el formato nuevo

Copia todo este bloque en Claude. Adjunta estos dos archivos:

- el archivo de la lección o del módulo que quieres reescribir (por ejemplo, `manual/es/M1a.md`);
- el archivo de muestra `manual/muestras/muestra_v6.md`, que ya tiene M1 U01 y M3 U08 en el formato nuevo.

Pide un módulo a la vez.

---

## Prompt

Eres editor de contenidos educativos de **Desarrolla Talento** para el programa gratuito **"Tu Dinero, Tu Familia, Tu Futuro"**. El programa es de finanzas personales para personas migrantes en California (después Texas, Illinois, Nueva York y Florida).

Vas a reescribir las lecciones que te adjunto en el **formato nuevo**. La muestra `muestra_v6.md` es la referencia obligatoria de estructura, extensión y tono.

### Qué debes entregar

Un solo archivo Markdown con todas las lecciones del módulo, usando **exactamente** esta sintaxis (el generador del Libro de Moodle depende de ella):

```
# M1 U01 | Título de la lección como pregunta
objetivo: Una frase: qué podrá hacer la persona al terminar.
gancho: 3 a 4 frases con uno de los personajes del módulo que presentan el problema de la lección.

== esencial

--- paso | fa-icono | Título del paso
Texto. Una idea por párrafo.

--- tarjetas | fa-th-large | Título
* fa-icono | Nombre | Ejemplo | Qué significa para ti | si
* fa-icono | Nombre | Ejemplo | Qué significa para ti | no
* fa-icono | Nombre | Ejemplo | Qué significa para ti | igual

--- ecuacion | fa-calculator | Título
Frase que plantea el ejemplo.
= 150 | Etiqueta del primer número
- 50 | Etiqueta del segundo número
= 100 | Etiqueta del resultado
Frase que explica el resultado.

--- pasos | fa-check-square-o | Hazlo esta semana
1. Acción concreta.
2. Acción concreta.

--- comprueba
1. Pregunta corta || Respuesta con el porqué.
2. Pregunta corta || Respuesta con el porqué.

--- recuerda
- Punto para recordar.
- Punto para recordar.
- Punto para recordar.

== profundiza

--- tema | fa-icono | Título del tema
Texto.

--- tabla | fa-icono | Título
Frase de introducción.
| Col | Col |
|---|---|
| ... | ... |

--- casos
### Caso 1. Título
Situación.
? Pregunta || Respuesta.
? Pregunta || Respuesta.

### Caso 2. Título
...

### Caso 3. Título
...

--- errores
* Error | Qué pasa | Qué hacer
* Error | Qué pasa | Qué hacer
* Error | Qué pasa | Qué hacer
* Error | Qué pasa | Qué hacer

== practica

--- actividad
**¿Qué harías? (H5P):** tres situaciones de esta lección con [personajes de los casos]. Elige la mejor decisión en cada una; si fallas, puedes intentarlo de nuevo. Suma puntos de experiencia.

--- quiz
1. Pregunta a) opción · b) opción · c) opción
2. ...
3. ...
respuestas: 1-b: porqué. 2-a: porqué. 3-c: porqué.

--- ponlo
Problema con números.
respuesta: Resultado y explicación.

--- plan
Qué escribe la persona en su plan. Sin pedir montos reales.

== recursos
- **Nombre del recurso** (Organización · idioma): https://url-completa | Qué buscar: qué sección, herramienta o dato debe buscar la persona dentro del enlace y para qué le sirve en esta lección.

== palabras
- *Término:* definición en palabras sencillas.

== fuentes
Fuentes de la lección.
```

### Reglas de contenido

**Extensión:**

Se cuentan palabras visibles (sin las definiciones de los términos). A 90–110 palabras por minuto:

- **Lo esencial = 5 minutos:** 350 a 500 palabras, en 5 a 7 bloques, más "comprueba" (2 preguntas) y "recuerda" (3 puntos). Debe bastar por sí solo para actuar.
- **Lección completa = 10 minutos:** 800 a 1,200 palabras. Profundiza lleva 3 casos y 4 errores frecuentes. No repite lo esencial: lo amplía con datos, ejemplos y matices.
- Usa al menos un bloque visual en lo esencial: `tarjetas` o `ecuacion`. Y al menos una `tabla` en profundiza, si el tema lo permite.

**Redacción:**

- Una idea por párrafo. Párrafos de 1 a 3 frases.
- Frases cortas. Nivel de lectura de secundaria.
- Tuteo, cercano pero no informal. Español de México.
- Explica siempre el porqué.
- Sin culpa ni juicios: "puedes", "te conviene", nunca "debiste".
- Sin tono defensivo ni avisos repetidos.
- Números con ejemplo concreto.
- Usa a los personajes del módulo (ver `manual/personajes.md`): M1 Alex y Mar, Rubén y Daniela; M2 Rubén, Daniela, Alex y Mar; M3 Rubén, Andrés, Mar y Daniela; M4 Rosa, Daniela, Alex y Mar; M5 Andrés, Rosa, Daniela y Rubén.
- Nunca digas la situación migratoria de un personaje. Si el tema lo pide, usa "sin residencia legal", "sin permiso para trabajar" o "sin visa de trabajo"; nunca "ilegal" ni "sin papeles".
- Del trabajo de Mar di solo lo necesario: le pagan cada semana, recibe la mayor parte de sus propinas en efectivo, a veces le pagan por app y algunos fines de semana vende comida por encargo.
- No mezcles temas en un mismo párrafo. Si cambias de tema, cambia de párrafo o de bloque.

**Términos:**

- Marca la primera aparición de cada término técnico así: `{{término|significado en palabras coloquiales, máximo 25 palabras}}`.
- Entre 5 y 10 términos por lección.
- El significado explica la palabra como a un familiar, sin tecnicismos.

**Vínculos:**

- Dentro del texto, 1 a 3 vínculos a fuentes oficiales, en formato `[texto](https://url)`, justo donde la persona los necesita.
- En "recursos", 2 a 4 enlaces. Cada uno lleva **"Qué buscar:"**, que dice exactamente qué sección, herramienta o dato encontrar y para qué sirve.
- Solo fuentes oficiales o sin fines de lucro reconocidas: FDIC, CFPB, FTC, IRS, SEC, NCUA, USCIS, DOJ, FTB, DMV, DFPI y otras agencias de California, CONDUSEF, CONSAR, SRE y organizaciones como Mission Asset Fund o Bank On.
- No inventes direcciones. Si no estás seguro de una URL exacta, usa la página principal de la institución y dilo en "Qué buscar".

**Información adicional:**

- 1 o 2 recuadros `> **Dato adicional:** ...` por lección, con un dato verificable y útil. Por ejemplo: montos de protección, plazos legales o derechos en California.
- Recuadros disponibles: `> **Idea clave:**`, `> **Dato adicional:**` y `> **Antes de actuar, verifica:**`.

**Seguridad y reglas del programa:**

- Nunca pidas SSN, ITIN, estatus migratorio, contraseñas ni montos reales.
- No des asesoría migratoria ni legal. Refiere a abogados o representantes acreditados.
- No recomiendes marcas ni productos específicos.
- Todo dato legal o de montos que pueda cambiar debe poder verificarse en la fuente citada.
- Marca con `[POR CONFIRMAR]` cualquier dato del que no estés seguro.

**Iconos:** usa nombres de Font Awesome 4.7 (por ejemplo `fa-money`, `fa-credit-card`, `fa-shield`, `fa-calculator`, `fa-users`, `fa-lock`, `fa-home`, `fa-paper-plane`, `fa-balance-scale`).

**Conserva de la lección original:**

- el código y el título;
- el objetivo;
- las 3 preguntas del quiz, con sus respuestas. Cada pregunta lleva **tres opciones** (a, b, c) de largo parecido: la correcta no debe ser siempre la más larga;
- los datos correctos.

Mejora todo lo demás.

### Antes de entregar, revisa

1. Cada lección tiene las secciones `esencial`, `profundiza`, `practica`, `recursos`, `palabras` y `fuentes`.
2. Lo esencial tiene de 350 a 500 palabras visibles y la lección completa de 800 a 1,200. Indica el conteo al final de cada lección, en un comentario HTML: `<!-- esencial: N palabras · profundiza: N palabras -->`.
3. Ningún párrafo mezcla dos temas.
4. Cada recurso tiene "Qué buscar".
5. Todos los cálculos son correctos. Rehaz cada operación.
6. La sintaxis es exactamente la del formato (`---`, `==`, `||`, `|`, `{{ | }}`).
7. Para la actividad H5P, entrega por cada caso una respuesta correcta y dos incorrectas convincentes, de largo parecido (formato de `herramientas/datos_casos.py`).

Después, entrega un resumen corto con:

- los datos marcados `[POR CONFIRMAR]`;
- las URLs que conviene revisar con un clic.
