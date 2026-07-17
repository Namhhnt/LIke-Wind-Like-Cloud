# Library Story Authoring Guide

## Purpose

Use this guide when you want to add a **custom Library / Original Story** to the current project.

This guide is based on the **real implementation currently in the repo**, especially:

- `game/story_library.rpy`
- `game/story_parser.rpy`
- `game/story_player.rpy`
- `game/stories/manifest.json`
- `game/scripts/*_sprites.rpy`
- `game/scripts/backgrounds.rpy`

These stories are **not normal Ren'Py script chapters**. They are read-only `.md` or `.txt` files that the project parses as data and renders inside the Library story reader.

---

## What A Library Story Is

A Library story is:

- stored under `game/stories/`
- registered through `game/stories/manifest.json` (preferred)
- parsed by `game/story_parser.rpy`
- shown in the Library UI through `game/story_library.rpy` and `game/story_player.rpy`

It is meant for:

- original stories
- side stories
- extra / bonus prose content
- read-only optional content

It is **not** meant for:

- running arbitrary Python
- jumping to labels
- running normal Ren'Py control flow
- branching choice gameplay

---

## Current Workflow Summary

To add a new custom story, you usually need to do **3 things**:

1. Create a story file under `game/stories/`
2. Add an entry in `game/stories/manifest.json`
3. Make sure any referenced backgrounds / character portraits already exist as declared Ren'Py images

If you want a brand new character or brand new background, you must also add the asset file and its Ren'Py image declaration.

---

## Folder Structure

Current working pattern:

```text
game/
  stories/
    manifest.json
    tam/
      coffee_after_the_rain.md
      the_elevator_ride_home.md

  scripts/
    backgrounds.rpy
    tam_sprites.rpy
    hoang_sprites.rpy
    minh_sprites.rpy
    ...
```

Recommended pattern for new stories:

```text
game/
  stories/
    manifest.json
    <series_or_character>/
      <story_file>.md
```

Example:

```text
game/stories/yuuka/morning_in_tokyo.md
```

---

## Preferred Registration Method: Manifest

The implementation first tries to load `game/stories/manifest.json`.

Current example from the repo:

```json
{
  "version": 1,
  "stories": [
    {
      "id": "tam_original_coffee_rain",
      "title": "Coffee After the Rain",
      "series": "Tâm Notes",
      "type": "original_story",
      "size": "small",
      "source": "local",
      "file": "stories/tam/coffee_after_the_rain.md",
      "order": 1,
      "point_cost": 0,
      "unlock_mode": "free",
      "prerequisites": [],
      "tags": ["Tam", "Original Story"],
      "cover": ""
    }
  ]
}
```

### Recommended fields

| Key | Required | Notes |
|---|---|---|
| `id` | yes | Unique story id |
| `title` | yes | Display title in Library |
| `series` | recommended | Display grouping / subtitle |
| `type` | recommended | Example: `original_story`, `extra`, `bonus` |
| `size` | recommended | `small`, `medium`, `large`, `special` |
| `source` | recommended | Use `local` for authored stories |
| `file` | yes | Path relative to `game/`, usually starts with `stories/` |
| `order` | recommended | Sort order inside the series |
| `point_cost` | recommended | `0` for free stories |
| `unlock_mode` | recommended | Usually `free` or `points` |
| `prerequisites` | optional | Array of completed chapter ids |
| `tags` | optional | Flat string list |
| `cover` | optional | Currently stored, but not meaningfully used by the reader UI yet |

### Notes

- Keep `id` unique.
- Keep `file` accurate and relative to `game/`.
- If `unlock_mode` is omitted, the code infers it from `point_cost`.
- If `point_cost` is greater than `0`, the story is treated as point-unlock content.

---

## Fallback Registration

If `manifest.json` is missing or invalid, the current code can scan `game/stories/` for `.md` and `.txt` files.

That fallback exists, but **you should still use `manifest.json`** because it is clearer, easier to sort, and more explicit about unlock conditions.

---

## Story File Format

Story files are plain text files with:

1. optional frontmatter
2. body lines using the supported read-only syntax

Example:

```md
---
id: tam_original_coffee_rain
title: Coffee After the Rain
series: Tâm Notes
type: original_story
size: small
order: 1
point_cost: 0
unlock_mode: free
tags:
  - Tam
  - Original Story
---

scene bg bg_tam_room_morning with fade

narrator: The rain had stopped, but the city still smelled like wet pavement and old metal.

tam neutral: "Maybe that is what a new beginning looks like."
```

---

## Frontmatter Rules

The frontmatter parser in `game/story_parser.rpy` is intentionally simple.

It supports:

- `key: value`
- blank lines
- flat lists like:

```text
tags:
  - Tam
  - Original Story
```

It does **not** support:

- nested objects
- advanced YAML features
- quoted parsing rules like a full YAML parser
- complex inline structures

So keep frontmatter simple.

Good:

```md
title: Morning Again
size: small
prerequisites:
  - tam_c01_interview_day
```

Avoid:

```md
conditions:
  route:
    tam:
      chapter: 1
```

---

## Supported Story Body Commands

The parser currently recognizes these command shapes:

```text
scene <background>
show <character> <expression> [at left|center|right]
hide <character>
music <bgm_id>
sfx <sfx_id>
pause <seconds>
narrator: <text>
<character> <expression>: <dialogue>
```

### What the current reader visibly uses

Right now, the page builder/rendering path meaningfully uses:

- `scene`
- `show`
- `hide`
- `narrator:`
- dialogue lines like `tam neutral: ...`

The parser also recognizes:

- `music`
- `sfx`
- `pause`

But the current Library story player does **not** yet meaningfully play music/SFX or create timing-based page changes from those events.

So for current practical authoring, think of `music`, `sfx`, and `pause` as **accepted syntax but not yet a fully implemented playback feature**.

---

## How To Write Background Lines

### Current best practice

Use:

```text
scene bg <background_image_name>
```

Example from the current repo-compatible pattern:

```text
scene bg bg_tam_room_morning with fade
```

The parser now strips the trailing `with ...` part and resolves the background id.

### How background lookup works now

The story reader tries these forms internally:

1. exact name
2. `bg <name>`
3. `bg_<name>`

Because the project declares backgrounds like this:

```renpy
image bg_tam_room_morning = "images/assets/bg/bg_tam_room_morning.webp"
image bg_interview_room = "images/assets/bg/bg_interview_room.webp"
```

the safest format is:

```text
scene bg bg_interview_room
scene bg bg_tam_room_morning
```

### Important limitation

If you write:

```text
scene bg cafe_rain
```

but there is no declared image matching `cafe_rain`, `bg cafe_rain`, or `bg_cafe_rain`, the reader will show no background image.

---

## How To Write Character Dialogue With Portraits

### Easiest pattern

Use dialogue lines like:

```text
tam neutral: "..."
tam smile: "..."
hoang serious: "..."
```

The current parser/reader can infer the speaker portrait from dialogue lines even if you do not write an explicit `show` command first.

### Explicit portrait control

If you want to force placement or keep a portrait on screen across multiple pages, use:

```text
show tam neutral at left
narrator: The room felt colder.
tam neutral: "I should go in now."

show hoang serious at right
hoang serious: "You are late."

hide tam
```

### Current position support

Supported lane keywords:

- `left`
- `center`
- `right`

Example:

```text
show tam neutral at left
show hoang serious at right
```

If no position is given, the reader defaults to center for generic sprites, while side portraits may be staged in the left portrait lane depending on reader logic.

---

## How Portrait Resolution Works In This Repo

This project does **not** currently resolve portraits from arbitrary filenames.

It resolves against declared Ren'Py image names.

For example, `game/scripts/tam_sprites.rpy` contains:

```renpy
image side tam neutral = "characters/tam/expressions/tam_neutral.webp"
image side tam smile = "characters/tam/expressions/tam_smile.webp"
image side tam serious = "characters/tam/expressions/tam_serious.webp"
```

And `game/story/common.rpy` contains:

```renpy
define tam = Character("Tâm", image="tam")
define hoang = Character("Hoàng", image="hoang")
```

### What this means for authoring

If you write:

```text
tam neutral: "..."
```

the reader tries portrait candidates in this order:

1. `side tam neutral`
2. `tam neutral`
3. `side tam`
4. `tam`

So the safest current pattern is:

- use the same character ids as the project’s Character definitions (`tam`, `hoang`, `minh`, `yuuka`, etc.)
- use expressions that actually exist in the sprite declaration files (`neutral`, `smile`, `happy`, `serious`, etc.)

---

## How To Add A New Story Using Existing Characters And Backgrounds

This is the safest workflow.

### Step 1: Create the story file

Example:

`game/stories/tam/late_evening_notes.md`

```md
---
id: tam_late_evening_notes
title: Late Evening Notes
series: Tâm Notes
type: extra
size: small
order: 3
point_cost: 0
unlock_mode: free
tags:
  - Tam
  - Extra
---

scene bg bg_interview_room with fade

narrator: The office was finally quiet.

tam thoughtful: "It is strange how silence can feel heavier than noise."
```

### Step 2: Register it in `game/stories/manifest.json`

```json
{
  "id": "tam_late_evening_notes",
  "title": "Late Evening Notes",
  "series": "Tâm Notes",
  "type": "extra",
  "size": "small",
  "source": "local",
  "file": "stories/tam/late_evening_notes.md",
  "order": 3,
  "point_cost": 0,
  "unlock_mode": "free",
  "prerequisites": [],
  "tags": ["Tam", "Extra"],
  "cover": ""
}
```

### Step 3: Make sure your referenced assets already exist

- `bg_interview_room` must exist in `game/scripts/backgrounds.rpy`
- `side tam thoughtful` must exist in `game/scripts/tam_sprites.rpy`

---

## Is It Possible To Add A New Background That Does Not Exist Yet?

Yes.

But you must do more than just reference the filename in the story.

### Required steps

1. Add the image asset file to the project
2. Declare it in a Ren'Py `.rpy` file
3. Reference the declared image name in the story file

### Example

Suppose you add a PNG here:

```text
game/images/assets/bg/bg_cafe_rain.png
```

Then add a declaration to `game/scripts/backgrounds.rpy`:

```renpy
image bg_cafe_rain = "images/assets/bg/bg_cafe_rain.png"
```

Then in the story file use:

```text
scene bg bg_cafe_rain
```

### Important note

Adding the PNG file alone is **not enough**. The story reader looks up declared image names, not raw filesystem paths.

---

## Is It Possible To Add A New Character That Does Not Exist Yet?

Yes.

But for a fully working character in the reader, you should add:

1. a `Character(...)` definition
2. one or more portrait image declarations
3. asset files for those portraits

### Step 1: Add a Character definition

Example:

```renpy
define linh = Character("Linh", image="linh")
```

Put that in an appropriate shared character-definition file.

### Step 2: Add portrait declarations

Example file:

`game/scripts/linh_sprites.rpy`

```renpy
image side linh neutral = "characters/linh/expressions/linh_neutral.png"
image side linh smile = "characters/linh/expressions/linh_smile.png"
image side linh serious = "characters/linh/expressions/linh_serious.png"
```

### Step 3: Add the actual image files

Example:

```text
game/characters/linh/expressions/linh_neutral.png
game/characters/linh/expressions/linh_smile.png
game/characters/linh/expressions/linh_serious.png
```

### Step 4: Use the character in a story file

```text
linh neutral: "I did not expect to see you here."
```

### Important limitation

If you only write this in the story file:

```text
linh neutral: "Hello."
```

but do **not** define `linh` and do **not** declare any matching images, then:

- the text may still render
- the display name may fall back to `Linh`
- but the reader will have no actual portrait image to show

---

## Expression Naming Rules

Use expression names that really exist in the sprite declaration files.

Examples currently present for `tam`:

- `neutral`
- `smile`
- `happy`
- `laugh`
- `sad`
- `teary`
- `cry`
- `shy`
- `embarrassed`
- `confused`
- `surprised`
- `shocked`
- `dazed`
- `thoughtful`
- `pouty`
- `serious`

If you write:

```text
tam furious: "..."
```

but no image named `side tam furious` exists, the portrait will not appear.

---

## Unlocking And Availability Rules

The Library system supports both free and point-based stories.

### Free story

```json
"point_cost": 0,
"unlock_mode": "free"
```

### Point-unlock story

```json
"point_cost": 3,
"unlock_mode": "points"
```

### Story progression gate

Use completed chapter ids in `prerequisites`:

```json
"prerequisites": ["tam_c01_interview_day"]
```

That checks the real progression state before allowing the story to unlock or display as available.

---

## Current Reader Behavior And Limitations

These are important if you are authoring content today.

### Supported well enough now

- local `.md` / `.txt` story files
- manifest-based registration
- simple frontmatter
- backgrounds via declared image names
- speaker portraits via declared image names
- `show` / `hide`
- dialogue and narrator pages
- optional unlock gating through points and prerequisites

### Current limitations

1. Story files are **read-only content**, not executable Ren'Py.
2. Do not put labels, jumps, Python, menus, or arbitrary script logic in them.
3. `music`, `sfx`, and `pause` are parsed but are not yet fully realized as a polished playback system in the Library reader.
4. Image lookup depends on declared Ren'Py image names, not raw file paths.
5. The frontmatter parser is intentionally simple and should not be treated as full YAML.
6. Cover images are stored in metadata but the current Library screen does not yet present a rich cover-art card layout.

---

## Recommended Authoring Rules

Follow these rules to avoid problems:

1. Always add the story to `game/stories/manifest.json`
2. Keep frontmatter flat and simple
3. Use declared background ids from `game/scripts/backgrounds.rpy`
4. Use character ids already defined in character files
5. Use expression names that really exist in `game/scripts/*_sprites.rpy`
6. Prefer `scene bg <declared_background_id>`
7. Prefer dialogue lines like `tam neutral: "..."`
8. Use `show ... at left|center|right` when you want explicit portrait staging
9. Do not assume raw image filenames are enough; declare new images in `.rpy` files
10. Treat Library stories as optional read-only content, not core progression chapters

---

## Authoring Checklist

Before testing a new story, check all of these:

- [ ] Story file exists under `game/stories/`
- [ ] Manifest entry exists and file path is correct
- [ ] Story `id` is unique
- [ ] Background ids used in `scene` lines are declared in `.rpy`
- [ ] Character ids used in dialogue exist as project character definitions
- [ ] Expression names used in dialogue exist in sprite declarations
- [ ] `prerequisites` use real chapter ids
- [ ] `point_cost` and `unlock_mode` match the intended behavior
- [ ] Story contains no Ren'Py code, jumps, menus, or Python

---

## Minimal Templates

### Free story template

```md
---
id: your_story_id
title: Your Story Title
series: Your Series
type: original_story
size: small
order: 1
point_cost: 0
unlock_mode: free
tags:
  - Example
---

scene bg bg_interview_room

narrator: Opening line.

tam neutral: "Dialogue line."
```

### Point-gated story template

```md
---
id: your_locked_story_id
title: Locked Story
series: Bonus Notes
type: extra
size: medium
order: 10
point_cost: 3
unlock_mode: points
prerequisites:
  - tam_c01_interview_day
tags:
  - Bonus
---

scene bg bg_company_lobby_morning

tam serious: "This one unlocks later."
```

---

## Bottom Line

Yes, you can write custom Library stories with backgrounds and character portraits.

Yes, you can also add brand new backgrounds and characters.

But for new assets to actually appear in the reader, you must:

- add the asset file
- declare it as a Ren'Py image
- use the declared image / character id in the story file

If you only add raw files without matching declarations, the reader will not know how to display them.
