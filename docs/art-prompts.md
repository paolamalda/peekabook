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
4. **Keep the outline separate from the color.** Export every layer as two files: `*_line.png` (only the dark outline) and `*_fill.png` (only the flat colors, no outline). The app tints the fill and puts the line on top. Showing the lines alone gives you **coloring pages** of any family's characters and scenes for free, with no extra art (this is the "Dibujos para colorear" feature).

### Layer order (bottom to top)

| z | Layer | Colored in code? |
|---|-------|------------------|
| −2 | `gear_back` (balloon basket, boat, rocket; see 2.9) | no |
| −1 | `hood_back` (inside of a hood that's up, cape) | optional |
| 0 | `hair_back` | yes (hair color) |
| 1 | `body` (skin, head, neutral underwear shape) | yes (skin tone) |
| 2 | `shoes` | optional |
| 3 | `bottom` (pants, skirt, shorts) | optional |
| 4 | `top` (shirt, jacket, dress) | optional |
| 5 | `face` (eye whites, mouth, blush) | no |
| 6 | `iris` | yes (eye color) |
| 6.5 | `hood_front` (hood rim around the face, animal ears on it) | optional |
| 7 | `hair_front` (bangs) | yes (hair color) |
| 8 | `accessory_head` (hats, bows, glasses) | optional |
| 9 | `accessory_hand` (balloon, book, ice cream) | optional |
| 10 | `gear_front` (basket rim, boat hull, helmet glass, swim ring) | no |

Hair length is just different `hair_back` and `hair_front` pieces (short, bob, shoulder, long, braids, pigtails, curly afro, buzz, etc.).

---

## 1. Master style prompt (add to every character and pet prompt)

Based on your 15 reference images. Most were **flat and clean** (the waving boy, the girl with long hair walking, the singer girl, the pigtails girl sitting, the red panda, the deer, the wolf, the animal stickers), so that is the game style. The glossy ones (the wavy bob girl, the girl with glasses, the princess) become the close-up style in 1.2.

Use the same style text word for word each time so everything looks consistent. **Don't paste the reference images' names, artists or characters into prompts.** Describe the style only (some references had watermarks or were copyrighted characters).

### 1.1 Game style (every layer, every scene sprite)
```
STYLE: super-cute chibi kid, about 2 heads tall (the head is HALF of the total
height), big round soft head with small ears, tiny rounded body, short stubby arms
and legs, small mitten-like hands and small rounded feet. HUGE glossy eyes set low on
the face: dark outline on top, a big iris that is lighter at the bottom, 2 white
sparkle dots (one big, one small). Tiny mouth: a small smile, ":3" or a small open
"D" smile showing a pink tongue. Round pink blush on both cheeks. Hair in a few big
chunky locks with pointy tips, one clean shine band of lighter color, often one
small hair sprout on top. Clean, smooth dark-brown outline (#4A3228), slightly
thicker around the outer silhouette than on inner details. FLAT colors with ONE soft
shadow tone, no gradients, no texture, no painterly shading. Warm, soft, slightly
muted pastel palette. Friendly, cheerful kawaii children's-app look, vector style.

TECH: full body, front 3/4 view, centered on a 1024x1024 canvas, feet on a baseline
at y=960px, top of head at y=80px, character 520px wide max, transparent background,
NO white sticker border, NO ground shadow, no text, no watermark, no logo, single
isolated game sprite.
```
The white sticker border and the soft oval shadow on the ground (both in several of your references) are **added by the app**, not drawn. The border can be turned on for easy levels to make friends easier to spot, and the shadow only shows on the ground (not in the sky or water).

### 1.2 Close-up style (character creator, "¡Encontrado!", medals, stories)
Same character and shapes, just more polished. Add this to the game style:
```
CLOSE-UP EXTRA: soft gentle gradients on hair and clothes, glossy highlights on hair
and eyes, a few clean eyelashes, subtle warm rim light. Same proportions, colors and
outline color as the game style.
```

### 1.3 Negative prompt
For Stable Diffusion, Flux and others that support it:
```
realistic, 3d render, photo, painterly, sketch, pencil, texture, noise, background,
scenery, floor, ground shadow, sticker border, white outline, text, letters,
watermark, logo, signature, extra limbs, extra fingers, cropped, cut off, multiple
characters, blurry, scary, sexualized, adult proportions, long legs, tall body,
famous character, princess from a movie
```

---

## 2. Character layer prompts

Start every prompt with **[MASTER STYLE]**. When your tool allows it, add the base body image as a reference.

### 2.1 Base body (make this first; everything else matches it)
```
[MASTER STYLE] A bald, gender-neutral chibi child base body, standing with arms slightly out
to the sides and away from the body, feet slightly apart, in a plain light-grey
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
Variations (all from your references): `small smile`, `open "D" smile with pink tongue` (excited, waving), `":3" cat mouth`, `happy closed eyes ^ ^` (relaxed, sitting), `surprised O mouth`, `wink`, `heart sparkles in the eyes` (for the "¡Encontrado!" moment), `freckles`.

**Tiny version:** when a character is very far away in a scene (under ~60px), the app can swap in a simpler face: dark dot eyes with one white sparkle and a small curved smile. Make this as a separate `face_tiny` layer.

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
`{GARMENT}` ideas: `t-shirt`, `graphic tee`, `gingham top`, `cropped denim or white jacket (worn open over a top)`, `black leather jacket`, `sailor-collar sweater with ribbon bow`, `oversized hoodie with front pocket`, `striped long-sleeve shirt`, `hoodie with hood down`, `overalls bib`, `puffy winter jacket`, `raincoat`, `sweater with star`, `sundress`, `tutu dress`, `football jersey`, `school uniform`, `cardigan (grandma)`, `button-up shirt with tie (dad)`.

**Hood up / animal-ear hats:** a hood with the hood up (like the panda hoodie in your references), a onesie hood or an animal-ear beanie needs two layers:
```
[MASTER STYLE] ONLY a raised hood {with round panda ears / bunny ears / cat ears / no
ears} for the chibi base body. Output TWO images: HOOD_BACK = the inside and the back
of the hood that shows behind the head and hair, HOOD_FRONT = only the rim of the hood
framing the face plus the ears on top. Flat light-grey, one shadow tone, bold outline,
transparent background, aligned to the base body reference.
```
When a hood is up, the app hides the parts of `hair_back` that would stick out past the hood. Bangs (`hair_front`) stay on top.

### 2.5 Bottoms
```
[MASTER STYLE] ONLY {BOTTOM} fitted to the chibi base body's legs and hips, flat
light-grey with one shadow tone, bold outline, transparent background, aligned to
the base body reference.
```
Ideas: `jeans`, `denim shorts with rolled hem`, `denim shorts with lace trim`, `shorts`, `pleated skirt`, `cargo pants with pockets and straps`, `leggings`, `cargo pants`, `pajama pants with moons`.

### 2.6 Shoes
```
[MASTER STYLE] ONLY a pair of {SHOES} on the chibi base body's feet, flat light-grey
with one shadow tone, bold outline, transparent background, aligned to the base body
reference.
```
Ideas: `sneakers with ankle socks`, `knee socks with loafers`, `black ankle boots with buckles`, `sneakers`, `rain boots`, `sandals`, `ballet flats`, `light-up sneakers`, `snow boots`, `slippers`.

### 2.7 Accessories
```
[MASTER STYLE] ONLY a {ITEM} placed where it would sit on the chibi base body, full
color is OK but also give a light-grey tintable version, bold outline, transparent
background, aligned to the base body reference.
```
Head: `headband`, `hair clip with a small bow`, `big ribbon bow on a ponytail`, `stud earrings`, `round glasses`, `sunglasses`, `baseball cap`, `beanie with pom-pom`, `hair bow`, `flower crown`, `headphones`, `party hat`, `crown`, `bunny-ear headband`.
Hand or body: `crossbody bag with a thin strap`, `belt`, `microphone`, `drinking glass`, `red balloon`, `ice-cream cone`, `teddy bear`, `backpack`, `book`, `umbrella`, `kite string`, `scarf`, `cape`.

> Hats cover hair. In the app, if a hat is on, hide `hair_front` or swap in a "hat-hair" version.

### 2.8 Poses (optional, but makes scenes more lively)
Make a full base-body set, and fitted layers, for a few poses: `standing, arms slightly out to the sides` (the main dress-up pose; sleeves and jackets swap cleanly), `waving, other hand on the hip`, `walking`, `singing / cheering (one arm out)`, `sitting on the ground with knees up`, `kneeling`, `peeking from behind something (only head + hands visible)`.
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

One pet style and **one shared body template** for every species. Only the ears, tail, markings and colors change. Your red panda, deer and wolf references set the look.

### 3.1 Pet style (use instead of 1.1 for pets)
```
PET STYLE: super-cute chibi animal, oversized round head (about 60% of the height),
tiny chubby body, short stubby legs with rounded paws, a lighter cream belly, chest
and muzzle, HUGE glossy dark eyes with 2 white sparkle dots, tiny nose, small "w" or
open smiling mouth, round pink blush, fluffy tufts on the chest and cheeks. Same
dark-brown outline (#4A3228) and FLAT colors with ONE soft shadow tone as the kids,
so pets and people look like they belong to the same world. 512x512 canvas,
paws on a baseline at y=480px, transparent background, no sticker border, no ground
shadow, no text, no watermark.
```

### 3.2 Base body (2 poses)
```
[PET STYLE] ONLY the base body of a cute chibi {dog / cat / bunny / hamster}, {POSE},
3/4 front view, flat light-grey (#DADADA) fur with a lighter grey (#F2F2F2) belly and
muzzle so both can be tinted separately, iris as a separate grey layer, NO ears and
NO tail (they are separate layers), aligned to the pet template.
```
`{POSE}`:
- `sitting, front paws together, back paws showing their pads` (the main pose)
- `standing on four legs, head turned toward the viewer, mouth open and happy`

**Species:** start with only `dog`, `cat`, `bunny` and `hamster`. Most other pets can reuse one of these four bodies with new ears and a tail. Add birds, fish or turtles later only if families ask for them, since they need their own bodies.

### 3.3 Pet layers
| Layer | Prompt fragment |
|-------|-----------------|
| `ears` | `ONLY {pointy / floppy / folded / long bunny / round} ears for the pet template, grey with a pink inner ear` |
| `tail` | `ONLY a {fluffy / curly / short stub / long thin / round pom-pom} tail` |
| `pattern` | `ONLY the {spots / patches / tabby stripes / tuxedo chest / socks / mask around the eyes} markings, darker grey, transparent elsewhere` |
| `accessory` | `ONLY a {collar with tag / bandana / bow / tiny sweater / harness}` |
| `gear` | `ONLY a {doggy life vest / swim ring / tiny astronaut bubble helmet / balloon tied to the collar / seat in the owner's basket}`. This lets the pet go into water, space or sky too (same rules as section 2.9) |

Colors come from code: the main fur color, the belly/muzzle color and the pattern color. A Dalmatian, a black lab, a golden retriever and a calico cat can then all share the same assets.

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
