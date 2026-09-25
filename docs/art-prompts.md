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
| −1 | `gear_back` (balloon basket, boat, rocket; see 2.9) | no |
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
| 10 | `gear_front` (basket rim, boat hull, helmet glass, swim ring) | no |

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

Poses for the sky, water and space (only needed if you use those zones, see section 5):
- `floating` — legs dangling, arms up or holding something above the head (for balloons, kites, umbrellas, jetpacks, space)
- `swimming` — only the chest and head above a flat waterline; the bottom of the canvas is cut straight across at the waterline
- `seated in vehicle` — the same as `sitting`, but hidden from the waist down (boats, balloon baskets, rockets, cars)

### 2.9 Gear that lets chibis go into the sky, water or space
Gear is what allows a character into a zone other than the ground. Each piece is a layer. Big pieces are split into **back** and **front** so the chibi sits *inside* them.

```
[MASTER STYLE] ONLY a {GEAR} sized for the chibi base body in the {POSE} pose, flat
colors with one shadow tone, bold outline, transparent background, aligned to the
base body reference. If the character sits inside it, output TWO images:
GEAR_BACK (parts behind the body) and GEAR_FRONT (parts in front of the body, e.g.
the basket rim, the boat hull, the helmet glass).
```

| Gear | Pose | Lets them into | Layers |
|------|------|----------------|--------|
| bunch of balloons | floating | sky | back |
| hot-air balloon basket | seated in vehicle | sky | back + front |
| kite held with both hands | floating | sky | back |
| umbrella (Mary-Poppins style) | floating | sky | back |
| witch broom | seated in vehicle | sky | back + front |
| paper airplane / small plane | seated in vehicle | sky | back + front |
| superhero cape (flying) | floating | sky | back |
| swim ring / floaties | swimming | water surface | front |
| little rowboat / sailboat | seated in vehicle | water surface | back + front |
| surfboard | standing | water surface | front |
| snorkel mask + flippers | floating | underwater | front |
| mini submarine | seated in vehicle | underwater | back + front |
| astronaut suit + bubble helmet | floating | space | back + front (glass is semi-transparent) |
| small rocket / jetpack | floating or seated in vehicle | space and sky | back + front |

Tie gear to the season looks and costumes the kids trade medals for (for example, Astronauta = astronaut suit, so that character can float in space).

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
| `gear` | `ONLY a {doggy life vest / swim ring / tiny astronaut bubble helmet / balloon tied to the collar / seat in the owner's basket}` — lets the pet go into water, space or sky too (same rules as section 2.9) |

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

Scenes with a lot of sky, water or space need **open areas there too** (not just ground). Add this to the prompt for those scenes:
```
Leave generous open {sky / water surface / underwater / outer space} areas with only a
few small clouds, stars, bubbles or waves, so floating, flying or swimming characters can
be placed there later.
```
More ideas: `floating cloud kingdom with sky islands`, `outer space with planets, moon base and asteroids`, `lake with boats and a pier`, `hot-air balloon festival over a valley`, `pirate ships at sea`, `rooftops of a city at sunset (for flying characters)`.

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
- MAGENTA #FF00FF = open AIR: sky or outer space (only for characters with
                   flying/floating gear)
- CYAN   #00FFFF = WATER SURFACE: lakes, sea, pools (swimming or boat gear)
- NAVY   #000080 = UNDERWATER: open water below the surface (diving gear or
                   submarine)
- RED    #FF0000 = ALWAYS FORBIDDEN: solid walls, rooftops, tree canopies,
                   buildings' faces, roads with traffic, fire, cliffs, big
                   landmarks that must stay visible, the top 10% and bottom 8%
                   of the image (reserved for app UI)
- BLACK  #000000 = everything else (also forbidden)
Same size as the original, perfectly aligned.
```

Sky, water and space **aren't forbidden by default**. Each is its own zone, and the scene decides who can go there (see 5.2 and 5.3). A park can have a small patch of sky for balloons. In a space scene, almost everything is air.

### 5.2 Rules the app should follow (tell your developer, or the coding AI)
```
Placement rules for Peekabook scenes:
1. Each zone color needs a matching POSE and, outside the ground zones, matching GEAR:
     GREEN   → standing/waving/walking, anchor = feet
     BLUE    → sitting, anchor = feet
     YELLOW  → peeking, anchor = feet
     MAGENTA → floating or seated-in-vehicle + sky or space gear, anchor = body center
     CYAN    → swimming or boat, anchor = waterline point
     NAVY    → floating + underwater gear, anchor = body center
   Pets follow the same rules with their paw/center anchor.
2. Every scene has a zoneRules table (see 5.3) saying which zones are open and
   which gear each one accepts. A zone that is not listed, or RED/BLACK, is never used.
3. Scene default gear: a scene can give gear to everyone automatically (space
   scene → astronaut suit; underwater scene → snorkel; cloud kingdom → balloons).
   Otherwise, only characters whose outfit already includes the gear can go into
   that zone (e.g. a kid wearing the Astronauta costume they won with medals).
4. For foot-anchored zones, sample 3 points across the feet (left/center/right).
   For AIR/UNDERWATER, sample the 4 corners of the body's box plus its center.
   All samples must be the same valid zone.
5. Scale by depth: scale = lerp(minScale, maxScale, y / imageHeight). In AIR,
   use the scale of the ground directly below if there is one, else the scene's
   airScale (space scenes usually have no depth, so use one fixed scale).
6. The sprite's full bounding box must not overlap RED UI safe zones.
7. Keep a minimum distance between hidden targets (e.g. 150px scaled) and never
   let two targets overlap each other.
8. Spread targets out: don't put every target in the air or every target in the
   water. Respect the scene's maxPerZone.
9. Difficulty: easy = targets in open GREEN or open AIR, not behind foreground;
   hard = YELLOW/peek spots, spots partly covered by scene_fg, and among many
   decoys wearing the same gear.
10. Draw order is sorted by anchor Y, so characters lower on screen appear in front.
    Draw the gear layers in this order: GEAR_BACK → character → GEAR_FRONT.
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
  "zoneRules": {
    "ground":     { "open": true },
    "seat":       { "open": true },
    "peek":       { "open": true },
    "air":        { "open": true,  "gear": ["balloons", "kite", "umbrella", "cape"], "maxPerZone": 1 },
    "water":      { "open": true,  "gear": ["swim_ring", "rowboat"], "maxPerZone": 2 },
    "underwater": { "open": false }
  },
  "sceneDefaultGear": null,
  "fillerCrowd": 40,
  "maxTargets": 6
}
```

The same file for a **space** scene. Everyone floats in astronaut suits, and there's no depth:
```json
{
  "id": "outer_space",
  "size": [3840, 2160],
  "depthScale": null,
  "airScale": 0.8,
  "zoneRules": {
    "ground": { "open": true },
    "air":    { "open": true, "gear": ["astronaut_suit", "rocket", "jetpack"], "maxPerZone": 6 }
  },
  "sceneDefaultGear": { "air": "astronaut_suit" },
  "fillerCrowd": 30,
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
