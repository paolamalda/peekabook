# Peekabook: prompts for the art

This file has prompts for an AI image generator (Midjourney, DALL·E, Ideogram, Stable Diffusion, Flux, etc.) to make:

1. Chibi characters built from layers you can swap (body, hair, eyes, clothes, shoes, accessories)
2. Pets built the same way
3. Busy "find them" scenes
4. A placement map for each scene that tells the app where chibis can and can't go

---

## 0. Read this first: how to keep the layers lined up

AI image generators don't line layers up to the exact pixel. Three rules make the system work:

1. **Lock one canvas and one pose.** Every layer uses the same canvas (for example 1024×1024), the same pose and the same anchor points. Make the base body first, then give it as a reference or init image when you generate each layer. Stable Diffusion with ControlNet, or Midjourney `--cref`/`--sref`, works best for this.
2. **Don't make one image per color.** Draw hair, skin, eyes and clothes in **flat light grey** (or with a separate grey "tint mask"). The app colors them in code (multiply or hue tint). One hair style then gives every hair color. The same goes for skin tones and eye colors. That's a few assets instead of hundreds.
3. **Split hair into back and front.** Hair behind the head (long hair, ponytails) and hair in front (bangs) are two layers, so the face sits between them.

### Layer order (bottom to top)

| z | Layer | Colored in code? |
|---|-------|------------------|
| 0 | `hair_back` | yes (hair color) |
| 1 | `body` (skin, head, neutral underwear shape) | yes (skin tone) |
| 2 | `shoes` | optional |
| 3 | `bottom` (pants, skirt, shorts) | optional |
| 4 | `top` (shirt, jacket, dress) | optional |
| 5 | `face` (eye whites, mouth, blush) | no |
| 6 | `iris` | yes (eye color) |
| 7 | `hair_front` (bangs) | yes (hair color) |
| 8 | `accessory_head` (hats, bows, glasses) | optional |
| 9 | `accessory_hand` (balloon, book, ice cream) | optional |

Hair length is just different `hair_back` and `hair_front` pieces (short, bob, shoulder, long, braids, pigtails, curly afro, buzz, etc.).

---

## 1. Master style prompt (add to every character and pet prompt)

Use the same style text word for word each time so everything looks consistent.

```
STYLE: super-cute chibi character, 2.5-head-tall proportions (head is 40% of total
height), big round head, small soft body, stubby rounded limbs, large sparkly eyes
positioned low on the face, tiny simple mouth, soft rosy blush, clean bold dark-brown
outline of even 4px weight, flat cel shading with ONE soft shadow tone, no gradients,
no texture, no noise, pastel-friendly palette, children's picture-book look,
kawaii, friendly and warm, vector-illustration style.

TECH: full body, front-facing 3/4 view, standing neutral pose, arms slightly away from
the body, feet together, centered on a 1024x1024 canvas, feet touching a baseline at
y=960px, top of head at y=80px, character is 520px wide max, transparent background,
no ground shadow, no text, no border, no watermark, isolated asset for game sprite.
```

**Negative prompt** (for Stable Diffusion, Flux and others that support it):
```
realistic, 3d render, photo, gradient, texture, background, scenery, floor, shadow on
ground, text, watermark, extra limbs, extra fingers, cropped, cut off, multiple
characters, blurry, noisy, scary, sexualized, adult proportions
```

---

## 2. Character layer prompts

Start every prompt with **[MASTER STYLE]**. When your tool allows it, add the base body image as a reference.

### 2.1 Base body (make this first; everything else matches it)
```
[MASTER STYLE] A bald, gender-neutral chibi child base body in a plain light-grey
(#D9D9D9) skin tone, wearing simple skin-tight neutral underwear shapes, no hair,
no clothes, no shoes, no face details except the head shape and ears. Clean
silhouette for a paper-doll dress-up system.
```
Make one body per pose you need (see section 2.8). Keep the skin flat grey so the app can tint it to any skin tone.

### 2.2 Face and eyes
```
[MASTER STYLE] ONLY the face features for the chibi base body: large round eyes with
white sclera and two sparkle highlights, IRIS drawn as a separate flat light-grey
(#BFBFBF) circle, small happy mouth, soft pink blush ovals. Everything else is
transparent. Positioned exactly where the face sits on the base body reference.
```
Variations: `happy smile`, `open-mouth laugh`, `surprised O mouth`, `wink`, `sleepy`, `freckles`.

### 2.3 Hair (make back and front for every style)
```
[MASTER STYLE] ONLY the HAIR for the chibi base body: {STYLE}. Draw it in flat
light-grey (#E0E0E0) with a single slightly darker grey shadow tone, bold outline.
Output TWO separate images: (1) HAIR_BACK = only the parts of the hair that are behind
the head and body, (2) HAIR_FRONT = only the bangs/fringe and strands in front of the
face. Transparent background, no head, no face, aligned to the base body reference.
```
`{STYLE}` ideas: `short messy`, `pixie cut`, `straight bob with bangs`, `shoulder-length wavy`, `long straight to the waist`, `high ponytail`, `two pigtails`, `two braids`, `space buns`, `curly afro puff`, `big curly afro`, `cornrows`, `locs`, `buzz cut`, `spiky`, `side part`, `hijab (as hair piece, tintable)`, `grey bun for grandma`, `balding with side hair for grandpa`.

### 2.4 Tops
```
[MASTER STYLE] ONLY a {GARMENT} fitted to the chibi base body, drawn in flat
light-grey (#E6E6E6) with one shadow tone and bold outline. Keep any pattern (stripes,
dots, stars) in a darker grey so it can be tinted. No body, no head, transparent
background, aligned to the base body reference.
```
`{GARMENT}` ideas: `t-shirt`, `striped long-sleeve shirt`, `hoodie with hood down`, `overalls bib`, `puffy winter jacket`, `raincoat`, `sweater with star`, `sundress`, `tutu dress`, `football jersey`, `school uniform`, `cardigan (grandma)`, `button-up shirt with tie (dad)`.

### 2.5 Bottoms
```
[MASTER STYLE] ONLY {BOTTOM} fitted to the chibi base body's legs and hips, flat
light-grey with one shadow tone, bold outline, transparent background, aligned to
the base body reference.
```
Ideas: `jeans`, `shorts`, `pleated skirt`, `leggings`, `cargo pants`, `pajama pants with moons`.

### 2.6 Shoes
```
[MASTER STYLE] ONLY a pair of {SHOES} on the chibi base body's feet, flat light-grey
with one shadow tone, bold outline, transparent background, aligned to the base body
reference.
```
Ideas: `sneakers`, `rain boots`, `sandals`, `ballet flats`, `light-up sneakers`, `snow boots`, `slippers`.

### 2.7 Accessories
```
[MASTER STYLE] ONLY a {ITEM} placed where it would sit on the chibi base body, full
color is OK but also give a light-grey tintable version, bold outline, transparent
background, aligned to the base body reference.
```
Head: `round glasses`, `sunglasses`, `baseball cap`, `beanie with pom-pom`, `hair bow`, `flower crown`, `headphones`, `party hat`, `crown`, `bunny-ear headband`.
Hand or body: `red balloon`, `ice-cream cone`, `teddy bear`, `backpack`, `book`, `umbrella`, `kite string`, `scarf`, `cape`.

> Hats cover hair. In the app, if a hat is on, hide `hair_front` or swap in a "hat-hair" version.

### 2.8 Poses (optional, but makes scenes more lively)
Make a full base-body set, and fitted layers, for a few poses: `standing`, `waving`, `walking side view`, `sitting`, `peeking from behind something (only head + hands visible)`.
The **peeking** pose is great for the hiding game. Keep the pose count small, because every pose multiplies the number of assets.

---

## 3. Pets

Same idea as the characters: a base per species, drawn in grey so it can be tinted, plus pattern and accessory layers.

```
[MASTER STYLE — replace "chibi character" with "chibi pet" and "2.5-head-tall" with
"oversized round head, tiny body"] ONLY the base body of a cute chibi {SPECIES},
sitting, facing 3/4 front, drawn in flat light-grey (#DADADA) with one shadow tone,
big sparkly eyes (iris as separate grey layer), tiny nose, bold outline, 512x512
canvas, paws on baseline y=480px, transparent background.
```
Species: `dog (floppy ears)`, `dog (pointy ears)`, `cat`, `bunny`, `hamster`, `guinea pig`, `parrot`, `turtle`, `goldfish in bowl`, `horse`, `lizard`.

Pet layers:
| Layer | Prompt fragment |
|-------|-----------------|
| `pattern` | `ONLY the {spots / patches / tabby stripes / tuxedo chest / socks} markings for the {SPECIES} base, darker grey, transparent elsewhere` |
| `ears_alt` | `ONLY {floppy / pointy / folded} ears for the {SPECIES} base` |
| `tail_alt` | `ONLY a {curly / fluffy / short stub / long} tail` |
| `accessory` | `ONLY a {collar with tag / bandana / bow / tiny sweater / harness}` |

Colors come from code: a main fur color plus a pattern color, so a Dalmatian, a black lab and a calico cat can share the same assets.

---

## 4. Scenes

The scene must be **busy but readable**. Kids need to find a 60–120px chibi, so the background should use **lower saturation and thinner outlines** than the characters. That way the characters stand out a little without being obvious.

### 4.1 Scene prompt template
```
A wide, busy, cheerful children's seek-and-find picture-book scene of {LOCATION},
high-angle 3/4 bird's-eye view like a Where's-Waldo spread, lots of small details,
objects and landmarks, NO people and NO animals (they will be added later), clear open
walkable areas (paths, grass, plazas, floors) spread across the whole image, a few
benches/steps/windows/doorways where characters could sit or peek, clean flat
vector style with thin soft outlines, slightly muted pastel colors, no text, no
signage words, 3840x2160 (16:9), consistent perspective with the horizon near the
top so far-away areas are small and near areas are large.
```
`{LOCATION}` ideas: `city park with pond and playground`, `beach boardwalk`, `school yard`, `zoo`, `farm`, `winter village with ice rink`, `birthday party in a backyard`, `supermarket`, `airport`, `museum of dinosaurs`, `space station`, `underwater reef city`, `grandma's house cutaway (dollhouse view)`, `camping forest`.

**Negative prompt:** `people, humans, characters, animals, pets, crowd, text, letters, logos, watermark, photorealistic, blur, dark, scary`

### 4.2 Foreground (occlusion) layer
Things in front of characters (a bush, a fence, a table) make hiding feel real.
```
Using the exact same scene, output ONLY the foreground objects that a person could
stand behind (bushes, fences, railings, tables, low walls, tree trunks, parked
carts), perfectly aligned with the original, everything else transparent.
```
In the app, draw `scene_bg`, then the chibis, then `scene_fg`.

---

## 5. Where chibis can and can't go

Give the app a color-coded **placement map** that matches each scene pixel for pixel. You can prompt for a first draft, but **plan to fix it by hand** in Photoshop, Procreate or Photopea, because AI masks are rough.

### 5.1 Mask prompt
```
Using the exact same scene composition and perspective, produce a flat
segmentation map with NO shading, NO outlines and NO details, only solid colors:
- GREEN  #00FF00 = ground where a standing character's FEET can be placed
                   (grass, paths, floors, sand, plaza, platforms)
- BLUE   #0000FF = seat surfaces where a SITTING character can be placed
                   (benches, steps, low walls, picnic blankets)
- YELLOW #FFFF00 = spots where a PEEKING character can appear
                   (behind edges of bushes, doorways, windows, corners)
- CYAN   #00FFFF = water where only a swimming/boat pose may go
- RED    #FF0000 = FORBIDDEN: sky, walls, rooftops, tree canopies, deep water,
                   roads with traffic, fire, cliffs, the top 10% and bottom 8%
                   of the image (reserved for app UI)
- BLACK  #000000 = everything else (also forbidden)
Same size as the original, perfectly aligned.
```

### 5.2 Rules the app should follow (tell your developer, or the coding AI)
```
Placement rules for Peekabook scenes:
1. A character's FEET anchor point (bottom-center of its sprite) must land on a GREEN
   pixel (standing) or BLUE pixel (sitting pose). YELLOW only for the peeking pose.
   Pets use the same rules with their paw anchor.
2. Sample 3 points across the feet (left/center/right) — all must be valid.
3. Scale the sprite by depth: scale = lerp(minScale, maxScale, y / imageHeight)
   (e.g. 0.45 at the horizon, 1.0 at the bottom) so far-away friends look smaller.
4. The sprite's full bounding box must not overlap RED UI safe zones.
5. Keep a minimum distance between hidden targets (e.g. 150px scaled) and
   never let two targets overlap each other.
6. Difficulty: easy = targets in open GREEN, not behind foreground; hard = prefer
   YELLOW/peek spots and places partially covered by scene_fg.
7. Draw order sorted by feet Y so characters lower on screen appear in front.
```

### 5.3 Per-scene metadata file (example)
```json
{
  "id": "city_park",
  "background": "city_park_bg.png",
  "foreground": "city_park_fg.png",
  "placementMap": "city_park_mask.png",
  "size": [3840, 2160],
  "depthScale": { "horizonY": 420, "minScale": 0.45, "maxScale": 1.0 },
  "uiSafeZones": [
    { "x": 0, "y": 0, "w": 3840, "h": 216 },
    { "x": 0, "y": 1987, "w": 3840, "h": 173 }
  ],
  "fillerCrowd": 40,
  "maxTargets": 6
}
```

`fillerCrowd` = random decoy chibis made from the same layer system, so kids have to look for *their* people in a crowd. This is what makes it Where's-Waldo-like.

---

## 6. Suggested workflow

1. Make the **base body** plus **face** and lock them. Never change them afterwards.
2. Make hair (back and front), tops, bottoms, shoes and accessories using the base as a reference.
3. Clean up in a vector or raster editor: line up the pieces to the canvas, set the grey to the exact tint value, and export PNGs with transparency (or SVGs).
4. Name files like `hair_back/long_wavy.png`, `top/hoodie.png`, `pet_dog/pattern_spots.png`.
5. Make the scenes, then the foreground layer, then the placement mask. Fix the mask by hand.
6. In the app: build each friend or family member from `{bodyPose, skinColor, hairStyle, hairColor, eyeColor, top, topColor, bottom, shoes, accessories[]}`, place them using the mask rules, and fill the rest with a random crowd.

### Tip: vector art is worth it
For a dress-up system, vectors (SVG) are the most reliable format. Use the AI images as **concept art**, then trace them (by hand, or with auto-trace in Illustrator or Vectorizer.ai) into SVG parts on one shared template. Tinting then becomes a simple `fill` change, and the art stays sharp at any zoom.
