# Authoring Guide

## Overview

This guide covers how to write scenes and chapters for this Ren'Py visual novel: which characters and expressions exist, which backgrounds and CGs are ready, how the map and progression systems work, and how to add new assets.

---

## 1. Chapter & Scene Structure

### Folder Layout

Every chapter lives under `game/story/<route_name>/<chapter_id>/` with:
- `_chapter.rpy` — Chapter wrapper label that calls scene labels in sequence
- `sNN_<name>.rpy` — Individual scene files (s01_, s02_, etc.)

```

game/story/
├── prologue/
│   └── prologue_rain_dream/
│       ├── _chapter.rpy
│       ├── s01_rain_meeting.rpy
│       ├── s02_wake_up.rpy
│       └── s03_tell_or_hide.rpy
├── tam/
│   ├── tam_c01_interview_day/
│   │   ├── _chapter.rpy
│   │   ├── s01_tam_huyen_morning.rpy
│   │   ├── s02_interview_room.rpy
│   │   ├── s03_success_result.rpy
│   │   └── s04_celebration_dinner.rpy
│   ├── tam_c02_company_party/
│   │   └── ...
│   └── ...
├── hoang/
├── yuuka/
├── minh/ (flashback_minyuu)
├── thienan/
├── huyen/
├── work/
├── group/
├── minyuu/
└── final/
```

### Chapter Wrapper Pattern

Every chapter wrapper follows this exact pattern:

```renpy
label tam_c02_company_party:
    call tam_c02_company_party_s01_company_rumors_about_quan
    call tam_c02_company_party_s02_party_start
    call tam_c02_company_party_s03_hoang_intro
    call tam_c02_company_party_s04_first_branch
    $ story_complete_chapter('tam_c02_company_party')
    if renpy.has_label('route_map'):
        jump route_map
    return
```

Key rules:
- Scene labels are called in order via `call`, not `jump`.
- After all scenes, call `$ story_complete_chapter('<chapter_id>')` — this triggers the progression system (saves completion, applies flags, recalculates unlocks).
- Then jump back to `route_map` so the player sees the interactive map.

### Scene File Pattern

```renpy
# FILE: game/story/tam/tam_c01_interview_day/s02_interview_room.rpy
# Scene file.

label tam_c01_interview_day_s02_interview_room:
    scene bg_interview_room
    show tam neutral at center

    tam "Welcome. Please have a seat."

    menu:
        "Ask about the team":
            $ story_add('career_tam', 1)
            tam "What is the team like?"

        "Stay quiet":
            $ story_add('tam_self_clarity', 1)
            tam "..."

    hide tam
    return
```

Scene labels must be unique across the whole project. The convention is `<chapter_id>_sNN_<descriptive_name>`.

### Custom Map Context (Optional)

After completing a chapter, you can queue a map background for when the player returns to the map:

```renpy
$ queue_story_map_context(chapter_id='tam_c02_company_party')
```

This is optional — the system auto-resolves from `MAP_CONTEXT_BY_CHAPTER` or `MAP_CONTEXT_BY_SCENE` by default.

---

## 2. Characters

### Defined Speaking Characters

These characters have `define` statements in `game/story/common.rpy` and can speak dialogue:

| Variable | Display Name | Side Image Prefix | Image Tag |
|----------|-------------|-------------------|-----------|
| `tam` | Tâm | `tam_` | `tam` |
| `huyen` | Huyền | `huyen_` | `huyen` |
| `hoang` | Hoàng | `hoang_` | `hoang` |
| `hoang_unknown` | Mysterious man | `hoang_` | `hoang` |
| `quan` | Quân | `quan_` | `quan` |
| `narrator` | (none) | — | — |
| `hr` | Recruiter | — | — |
| `interviewer` | Interviewer | — | — |
| `manager` | Manager | — | — |
| `coworker` | Coworker | — | — |
| `yuuka` | Yuuka | `yuuka_` | `yuuka` |
| `minh` | Minh | `minh_` | `minh` |
| `thienan` | Thiên An | `thienan_` | `thienan` |

### Side Image Expressions

Each character with `image="<name>"` in their `Character()` definition gets automatic side images from the declarations in `game/scripts/`. To display a side image, write dialogue with the matching tag:

```renpy
tam happy "I'm so excited!"
tam serious "Let me think about this."
```

#### Character — 25 expressions supported for side images:
`neutral`, `smile`, `happy`, `grinning`, `laughing`, `shy`, `embarrassed`, `flustered`, `bashful`, `teasing`, `sad`, `melancholic`, `teary`, `crying`, `hurt`, `angry`, `irritated`, `frustrated`, `disgusted`, `contemptuous`, `surprised`, `shocked`, `confused`, `bored`, `tired`

### Full-Sprite Declarations (for `show` / `scene`)

Currently only side images (`image side`) are declared. To show a character as a full sprite on screen (e.g. `show tam happy at center`), you need to add `image` declarations for the full-body sprites. See section 5 for the pattern.

---

## 3. Backgrounds

### Available Background Assets

Declared in `game/scripts/backgrounds.rpy`. Use with `scene <name>` or `show <name>`:

| Image Name | File | Description |
|-----------|------|-------------|
| `bg_tam_room_morning` | `images/assets/bg/bg_tam_room_morning.png` | Tâm's room in the morning |
| `bg_apartment_lobby_morning` | `images/assets/bg/bg_apartment_lobby_morning.png` | Apartment lobby, morning |
| `bg_company_lobby_morning` | `images/assets/bg/bg_company_lobby_morning.png` | Company lobby, morning |
| `bg_interview_waiting_room` | `images/assets/bg/bg_interview_waiting_room.png` | Interview waiting area |
| `bg_interview_room` | `images/assets/bg/bg_interview_room.png` | Interview room |
| `bg_company_lobby_noon` | `images/assets/bg/bg_company_lobby_noon.png` | Company lobby, noon |
| `bg_company_lobby_afternoon` | `images/assets/bg/bg_company_lobby_afternoon.png` | Company lobby, afternoon |
| `bg_luxury_restaurant_evening` | `images/assets/bg/bg_luxury_restaurant_evening.png` | Luxury restaurant, evening |
| `bg_company_open_office_day` | `images/assets/bg/bg_company_open_office_day.png` | Open office, daytime |
| `bg_meeting_room_day` | `images/assets/bg/bg_meeting_room_day.png` | Meeting room, daytime |
| `bg_company_year_end_party` | `images/assets/bg/bg_company_year_end_party.png` | Year-end party venue |
| `bg_company_year_end_party_late` | `images/assets/bg/bg_company_year_end_party_late.png` | Year-end party, late |

### Additional Background Files Available (not yet declared)

These PNG files exist in `game/images/assets/bg/` but don't have `image` declarations yet. To use them, add a line to `game/scripts/backgrounds.rpy`:

| File | Likely Subject |
|------|---------------|
| `bg_company_lobby_morning_empty.png` | Empty company lobby morning |
| `bg_company_2_lobby_morning.png` | Company 2 lobby morning |
| `bg_company_2_lobby_afternoon.png` | Company 2 lobby afternoon |
| `bg_company_3_lobby_afternoon.png` | Company 3 lobby afternoon |
| `bg_company_4_lobby_noon.png` | Company 4 lobby noon |
| `bg_high_class_apartment_lobby_morning.png` | High-class lobby morning |
| `bg_high_class_apartment_lobby_2_morning.png` | High-class lobby 2 morning |
| `bg_high_class_apartment_lobby_2_afternoon.png` | High-class lobby 2 afternoon |
| `bg_hotel_lobby_afternoon.png` | Hotel lobby afternoon |
| `bg_meeting_room_night.png` | Meeting room at night |

Usage in scenes:

```renpy
scene bg_interview_room
show tam neutral at center
tam neutral "This is the interview room."
```

---

## 4. CG Art

Eight CGs are available. Declared in `game/scripts/cgs.rpy`.

| Image Name | File |
|-----------|------|
| `cg_yuuka_minh_market_walk` | `images/assets/cg/cg_yuuka_minh_market_walk.png` |
| `cg_yuuka_minh_choose_strawberries` | `images/assets/cg/cg_yuuka_minh_choose_strawberries.png` |
| `cg_yuuka_minh_blue_apron` | `images/assets/cg/cg_yuuka_minh_blue_apron.png` |
| `cg_yuuka_minh_bench_rest` | `images/assets/cg/cg_yuuka_minh_bench_rest.png` |
| `cg_yuuka_minh_clean_strawberry` | `images/assets/cg/cg_yuuka_minh_clean_strawberry.png` |
| `cg_yuuka_minh_hair_touch` | `images/assets/cg/cg_yuuka_minh_hair_touch.png` |
| `cg_yuuka_minh_strawberry_smile` | `images/assets/cg/cg_yuuka_minh_strawberry_smile.png` |
| `cg_yuuka_minh_finger_touch` | `images/assets/cg/cg_yuuka_minh_finger_touch.png` |

Usage:

```renpy
scene cg_yuuka_minh_market_walk
with dissolve
"Yuuka and Minh walk through the market."
```

---

## 5. How to Add New Assets

### Add a New Expression to an Existing Character

1. Place the PNG file in `game/images/characters/<character>/expressions/<character>_<expression>.png`
2. Add to the corresponding sprite file in `game/scripts/<character>_sprites.rpy`:

```renpy
image side <character> <expression> = "characters/<character>/expressions/<character>_<expression>.png"
```

Example:

```renpy
image side tam determined = "characters/tam/expressions/tam_determined.png"
```

Then use it in dialogue:

```renpy
tam determined "I've made up my mind."
```

### Add a New Background

1. Place the PNG in `game/images/assets/bg/bg_<name>.png`
2. Add a declaration to `game/scripts/backgrounds.rpy`:

```renpy
image bg_<name> = "images/assets/bg/bg_<name>.png"
```

3. Use it in scenes:

```renpy
scene bg_<name>
```

### Add a New Character (with sprites)

1. Create a folder `game/images/characters/<name>/expressions/`
2. Add expression PNGs named `<name>_<expression>.png`
3. Create `game/scripts/<name>_sprites.rpy` and declare each:

```renpy
image side <name> neutral = "characters/<name>/expressions/<name>_neutral.png"
image side <name> smile = "characters/<name>/expressions/<name>_smile.png"
...
```

4. Define the Character in `game/story/common.rpy`:

```renpy
define <name> = Character("<Display Name>", image="<name>")
```

### Add a New CG

1. Place the PNG in `game/images/assets/cg/cg_<name>.png`
2. Declare in `game/scripts/cgs.rpy`:

```renpy
image cg_<name> = "images/assets/cg/cg_<name>.png"
```

---

## 6. Interactive Map Locations

### Current Fixed Locations

Defined in `game/map_data.rpy` (`FIXED_MAP_LOCATIONS`). These appear as clickable markers on the interactive map:

| ID | Name | Coordinates | Unlocked By | Default |
|----|------|------------|-------------|---------|
| `tam_apartment` | Tâm's Apartment | (200, 218) | `completed:tam_c01_interview_day` | No |
| `huyen_apartment` | Huyền's Apartment | (580, 180) | `completed:tam_c01_interview_day` | No |
| `hoang_house` | Hoàng / Minh's House | (240, 732) | `completed:tam_c01_interview_day` | No |
| `park` | Park | (350, 432) | Always | **Yes** |
| `library` | Library | (550, 450) | `completed:tam_c01_interview_day` | No |
| `foodie_street` | Foodie Street | (720, 280) | Always | **Yes** |
| `shopping_area` | Shopping Area | (970, 210) | Always | **Yes** |
| `restaurant` | Restaurant | (250, 500) | Always | **Yes** |
| `company` | Company | (1130, 540) | `completed:tam_c01_interview_day` | No |
| `conference_hall` | Conference Hall | (1060, 410) | `completed:tam_c02_company_party` | No |
| `airport` | Airport | (1440, 170) | `completed:yuuka_c08_festival_arrival` | No |

### Progression-Only Unlocking

Once unlocked, locations stay visible permanently. Temporary story locks (via `temporarily_locked_locations` or `force_only_locations` in a map context) can still override visibility for specific scenes.

### Map Backgrounds (Time-of-Day Variants)

The map supports four time-of-day variants plus a special festival night:

| Context ID | Background Image | Title |
|-----------|-----------------|-------|
| `day_default` | `city_map_day.png` | City Map |
| `afternoon_default` | `city_map_afternoon.png` | City Map |
| `evening_default` | `city_map_evening.png` | City at Evening |
| `night_default` | `city_map_night.png` | City at Night |
| `festival_finale` | `city_map_night.png` | Festival Night |

### Adding a New Map Location

Add to `FIXED_MAP_LOCATIONS` in `game/map_data.rpy`:

```python
"new_location_id": {
    "id": "new_location_id",
    "name": "Display Name",
    "x": 500,
    "y": 400,
    "category": "public",       # one of: residential, residential_villa, public, commercial, office, event, transport
    "icon": "park",             # icon style
    "default_unlocked": False,  # True = always visible
    "unlock_conditions": ["completed:tam_c01_interview_day"],
    "description": "What the player sees on hover.",
}
```

### Chapter-to-Location Override

You can pin a chapter to a specific map location in `MAP_CHAPTER_LOCATION_OVERRIDES`:

```python
MAP_CHAPTER_LOCATION_OVERRIDES = {
    "tam_c01_interview_day": "company",
    "prologue_rain_dream": "park",
    ...
}
```

### Specifying a Map Background per Chapter or Scene

Add entries to the mapping dicts in `game/map_data.rpy`:

```python
MAP_CONTEXT_BY_CHAPTER = {
    "tam_c02_company_party": "evening_default",
    "yuuka_c08_festival_arrival": "afternoon_default",
    "final_c24_last_choices": "festival_finale",
}

MAP_CONTEXT_BY_SCENE = {
    "tam_c01_interview_day_s01_tam_huyen_morning": "day_default",
}
```

When the player returns to the map, `resolve_story_map_context()` will pick the chapter's mapped context (with scene overrides taking priority).

---

## 7. Unlocking Library Content

The Library screen (accessible from the main/game menu) has six categories. Each uses a different unlock mechanism. This section documents all of them.

### 7.1 Character Profiles

**Status: Implemented**

Character profiles use a **granular unlock API**. Instead of auto-unlocking all characters in a route when any chapter completes, the author explicitly unlocks the character (and specific profile sections) from within the scene/chapter script.

#### Unlocking a character

Call from any `.rpy` scene file when the character first appears or is first referenced:

```renpy
$ unlock_library_character("thienan")
```

This makes the character card visible in the Library — the name, sprite, description, and tags become accessible. Locked cards show "???" as the name and a "?" placeholder sprite.

#### Unlocking profile sections

Within a character's detail page, sections like Inner Layer, Core Traits, Narrative Function, Notes, and Relationships start **locked** (shown as `[Section Name — Locked]`). The author can unlock them gradually across the story:

```renpy
$ unlock_character_section("thienan", "inner_layer")
$ unlock_character_section("thienan", "core_traits")
$ unlock_character_section("thienan", "narrative_function")
$ unlock_character_section("thienan", "notes")
$ unlock_character_section("thienan", "relationships")
```

Section keys correspond to keys inside the profile's `"profile"` sub-dict, plus `"relationships"` for the top-level relationships list:

| Section Key | Profile Field | Description |
|---|---|---|
| `"inner_layer"` | `profile.inner_layer` | Deeper personality / emotional makeup |
| `"core_traits"` | `profile.core_traits` | List of defining personality traits |
| `"narrative_function"` | `profile.narrative_function` | The character's role in the story |
| `"hidden_identity"` | `profile.hidden_identity` | Secret layers (Minh-specific) |
| `"aliases"` | `profile.aliases` | Alternative names (Minh-specific) |
| `"notes"` | `profile.notes` | Author notes |
| `"relationships"` | top-level `relationships` | Relationship list |

The sections `"role"` and `"public_identity"` are **always visible** once the character is unlocked — they do not require a separate unlock call.

#### How it works

- Character IDs and section unlock state are tracked in `persistent.unlocked_library_characters` (list) and `persistent.unlocked_character_sections` (list of `"character_id.section_key"` strings), maintained in `game/story_library.rpy`.
- The core functions live in `game/data/library_data.rpy`:
  - `unlock_library_character(character_id)` — adds the character to the unlocked list
  - `unlock_character_section(character_id, section_key)` — adds the section entry
  - `is_character_unlocked(profile)` — checks `persistent.unlocked_library_characters`
  - `is_character_section_unlocked(character_id, section_key)` — checks unlocked sections
- Profiles with `"route": None` (supporting characters) are always unlocked regardless.
- The detail screen is at `screen library_character_detail` in `game/screens/library_subscreens.rpy`.
- 21 character profiles exist across all 8 routes plus supporting cast.

### 7.2 Side Stories (Original Stories)

**Status: Implemented**

Side stories are Markdown files in `game/stories/` registered via a `manifest.json`. They use a **three-tier unlock** system:

| Unlock Mode | Behavior |
|------------|----------|
| `"free"` | Unlocked automatically when all `prerequisites` (chapters) are completed. |
| `"points"` | Unlocked when prerequisites are met **and** the player spends investment points. |
| *(omitted)* | Defaults to `"points"` if `point_cost > 0`, otherwise `"free"`. |

**Prerequisite example — story requires a chapter to be completed:**

```json
{
    "id": "yuuka_minh_sunday_market",
    "title": "Sunday Market",
    "series": "Yuuka & Minh",
    "type": "side_story",
    "size": "medium",
    "order": 1,
    "unlock_mode": "free",
    "prerequisites": ["tam_c05_sunday_date"],
    "file": "stories/yuuka_minh_sunday_market.md"
}
```

**Point-cost example — story requires investment points:**

```json
{
    "id": "special_story",
    "title": "A Special Evening",
    "size": "medium",
    "point_cost": 3,
    "unlock_mode": "points",
    "prerequisites": ["tam_c03_thienan_family"]
}
```

Point costs are tiered:

| Size Keyword | Default Cost |
|-------------|-------------|
| `"small"` | 1 point |
| `"medium"` | 3 points |
| `"large"` | 5 points |
| `"special"` | 10 points |

You can override with an explicit `"point_cost"` value.

**To trigger unlock from code** (instead of prerequisites), call:

```renpy
$ unlock_library_content("content_id")
```

### 7.3 Music Room

**Status: Implemented (items auto-scanned from folder)**

Music tracks are **auto-detected** from `game/audio/music/` and registered into the library system. Each `.mp3` file in that folder is mapped to a chapter in `MUSIC_CHAPTER_BY_FILENAME` (defined in `game/data/library_music_data.rpy`):

```python
MUSIC_CHAPTER_BY_FILENAME = {
    "Keep Going On.mp3": "tam_c01_interview_day",
    "When Nothing Happens.mp3": "prologue_rain_dream",
    "Still Holding Hands.mp3": "tam_c05_sunday_date",
    # ...
}
```

- When the mapped chapter is completed, the track becomes freely available in the Music Room.
- Tracks have `unlock_mode: "free"` — no point cost.
- The library regenerates the item list at init time.

**To add a new track:**
1. Place the `.mp3` file in `game/audio/music/`.
2. Add an entry to `MUSIC_CHAPTER_BY_FILENAME` mapping it to the chapter that should unlock it.
3. If no chapter should gate it, comment it out or omit it (it won't appear in the library).

**To add a track that is always unlocked** (no chapter gate), assign it a dummy `prerequisites: []` or don't list it in `MUSIC_CHAPTER_BY_FILENAME` (it just won't appear until you add a registry entry manually).

### 7.4 CG Gallery

**Status: Not implemented (placeholder screen)**

The CG gallery currently shows a placeholder page. The CG image files exist in `game/images/assets/cg/` and are declared in `game/scripts/cgs.rpy`, but no library item data or unlock system has been wired yet.

**To implement the CG gallery**, you will need to:
1. Define CG items (similar to minigame items) with `"category": "cg"` and register them via `register_library_item()`.
2. Each CG item should have a `prerequisites` chapter and optionally a `point_cost`.
3. Replace the placeholder in `screen library_cg()` (in `game/screens/library_subscreens.rpy`) with actual CG thumbnails and display logic.

Example structure for future CG items:

```python
register_library_item({
    "id": "cg_yuuka_minh_market_walk",
    "title": _("Market Walk"),
    "category": "cg",
    "series": _("Yuuka & Minh"),
    "type": "cg",
    "size": "small",
    "point_cost": 0,
    "unlock_mode": "free",
    "prerequisites": ["yuuka_c08_festival_arrival"],
    "image": "images/assets/cg/cg_yuuka_minh_market_walk.png",
    "tags": ["cg", "yuuka", "minh"],
})
```

### 7.5 Minigame Replay

**Status: Implemented**

Minigames are registered into the library via `register_library_item()` calls in `game/data/library_minigame_data.rpy`. Each minigame variant:

- Has `"category": "minigames"`.
- Uses `"unlock_mode": "free"` with a `prerequisites` chapter — completing the chapter unlocks the minigame for replay.
- Has a `"type"` field that maps to the replay label (e.g., `"minigame_speech_order"`, `"minigame_problem_diagnosis"`).

**Currently registered minigames:**

| Library ID | Title | Prerequisite Chapter |
|-----------|-------|---------------------|
| `minigame_speech_tam_c01` | Tam's Interview Speech | `tam_c01_interview_day` |
| `minigame_speech_hoang_h01` | Hoàng's Gift Choice | `hoang_h01_brother_house` |
| `minigame_speech_yuuka_c08` | Yuuka's Director Speech | `yuuka_c08_festival_arrival` |
| `minigame_pd_scope_creep` | Project Diagnosis: Scope Creep | `work_c10_project_festival_overlap` |

**To add a new minigame replay entry:**

```python
# In game/data/library_minigame_data.rpy:
register_library_item({
    "id": "minigame_<unique_id>",
    "title": _("Display Title"),
    "category": "minigames",
    "series": _("Series Name"),
    "type": "minigame_<engine_type>",   # matches the replay label handler
    "size": "small",                     # small | medium | large | special
    "point_cost": 0,                     # 0 = free
    "unlock_mode": "free",              # free | points
    "prerequisites": ["chapter_id"],     # chapter that gates this
    "tags": ["minigame", "tag1", "tag2"],
    "cover": "",
})
```

The replay label must exist and be wired in the minigame engine.

### 7.6 Extras / Secrets

**Status: Implemented**

Secrets are lightweight unlockables defined in `SECRET_DEFINITIONS` in `game/data/library_data.rpy`. Unlock from anywhere in story code:

```renpy
$ unlock_secret("secret_prologue_seen")
```

```python
SECRET_DEFINITIONS = {
    "secret_prologue_seen": {
        "title": "First Dream",
        "description": "Witness the dream in the rain.",
        "icon": "★",
    },
}
```

Secrets are stored in `persistent.unlocked_secrets` and displayed in the Extras category.

### 7.7 Investment Points Economy

**Status: Implemented**

Investment points are the currency for unlocking library content. Awarded automatically when a chapter is completed (via `complete_chapter()` → `award_investment_points_for_story_chapter()`):

```renpy
# Each chapter completion gives 1 point by default:
$ award_investment_points_for_story_chapter(chapter_id)
```

To award points manually:

```renpy
$ award_investment_points(amount, source_key="<unique_key>")
```

The `source_key` prevents the same source from awarding points twice. Use it for one-time rewards (e.g., reading a story, achieving a milestone).

### 7.8 Common Library Item Fields

Every library item (stories, music, minigames, future CG items) uses these fields:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | yes | Unique identifier |
| `title` | string | yes | Display title |
| `category` | string | yes | `"stories"`, `"music"`, `"cg"`, `"minigames"` |
| `series` | string | no | Grouping label |
| `type` | string | yes | Content type descriptor |
| `size` | string | no | `"small"`, `"medium"`, `"large"`, `"special"` (affects default point cost) |
| `point_cost` | int | no | Override default point cost (0 = free) |
| `unlock_mode` | string | no | `"free"` or `"points"` (auto-detected from `point_cost` if omitted) |
| `prerequisites` | list | no | Chapter IDs that must be completed first |
| `tags` | list | no | Metadata tags for filtering |
| `cover` | string | no | Cover image path |
| `order` | int | no | Sort order within category |

### 7.9 Persistent Variables Reference

| Variable | Type | Purpose |
|----------|------|---------|
| `persistent.investment_points` | int | Currency for unlocking content |
| `persistent.spent_investment_points` | int | Total points spent (tracking only) |
| `persistent.unlocked_library_content` | list | IDs of point-unlocked library content |
| `persistent.read_library_content` | list | IDs of stories that have been read |
| `persistent.claimed_rewards` | list | Reward source keys already claimed (prevents double-claiming) |
| `persistent.unlocked_secrets` | list | IDs of unlocked secrets/extras |
| `persistent.gallery_unlocks` | list | IDs of unlocked gallery items |
| `persistent.unlocked_chapters` | list | IDs of all chapters ever completed (by `complete_chapter()`) |

---

## 8. Story State & Scoring

### Per-Character Scores (`story_state`)

Defined in `game/story_state.rpy`. Use with `$ story_add('<key>', <amount>)`:

| Key | Tracks |
|-----|--------|
| `tam_hoang_interest` | Tâm's interest in Hoàng |
| `tam_minh_drawn` | Tâm's attraction to Minh |
| `tam_self_clarity` | Tâm's self-understanding |
| `tam_respect_yuuka` | Respect for Yuuka |
| `tam_insecurity` | Tâm's insecurity score |
| `tam_observation` | Tâm's observation skill |
| `career_tam` | Tâm's career outcome |
| `hoang_tam_trust` | Hoàng's trust in Tâm |
| `hoang_huyen_interest` | Hoàng's interest in Huyền |
| `hoang_insecurity` | Hoàng's insecurity |
| `hoang_self_acceptance` | Hoàng's self-acceptance |
| `hoang_professional_credit` | Hoàng's professional reputation |
| `huyen_quan_trust` | Huyền's trust in Quân |
| `huyen_hoang_interest` | Huyền's interest in Hoàng |
| `career_huyen` | Huyền's career outcome |
| `thienan_quang_trust` | Thiên An's trust in Quang |
| `thienan_minh_residue` | Thiên An's feelings about Minh |
| `family_pressure_thienan` | Family pressure on Thiên An |
| `thienan_self_assertion` | Thiên An's self-assertion |
| `minh_yuuka_trust` | Trust between Minh and Yuuka |
| `minh_yuuka_intimacy` | Intimacy between Minh and Yuuka |
| `minh_yuuka_unresolved` | Unresolved tension |
| `doom_score` | Bad ending risk |
| `ending_support` | List of ending nudges |

### Flags (`progress["player_flags"]`)

Set with `$ story_flag('<flag_name>')` and check with `$ story_has_flag('<flag_name>')`.

Common flags:
- `prologue_seen`, `rain_dream_seen` — set by prologue
- `tam_route_started`, `canon_interview_day` — set by C01
- `tam_company_gathering_seen`, `quan_team_pressure_introduced` — set by C02
- `opening_map_locations_unlocked` — set after C01S01 for map unlock

### Relationship Directions (`progress["relationship_directions"]`)

Set via `$ story_add_direction('<character>', '<direction>')`.

Used as map unlock conditions: `direction:<character>:<direction>`.

### Ending Eligibility

Endings are checked in `game/ending_rules.rpy` using:
- `can_get_<ending_id>()` helpers

---

## 8. Progression Metadata

### Adding a New Chapter to the Progression System

Edit `game/progression_data.rpy` — add an entry to the `CHAPTERS` dict:

```python
"tam_cXX_descriptive_name": {
    "id": "tam_cXX_descriptive_name",
    "route": "tam",
    "type": "core",              # core | pov | bonus | extra
    "timeline_position": 50,     # position in route timeline (10=early, 90=late)
    "title": "Display Title",
    "label": "tam_cXX_descriptive_name",  # Ren'Py label name
    "prerequisites": ["tam_cYY"],          # chapters that must be completed first
    "prerequisites_any": [],               # any one of these suffices
    "unlocks": ["tam_cZZ"],               # chapters to unlock after completion
    "flags_set": ["flag_name"],            # flags added on completion
    "character_flags_set": {"character": ["flag"]},
    "relationship_directions_set": {"hoang": ["direction"]},
    "emotional_effects": {"trust": 1, "distance": -1},
    "choice_unlocks": ["choice_id"],
    "exclusion_group": None,              # mutual exclusion group
    "excludes": [],                        # chapters to exclude
    "soft_hide_until_any_completed": [],  # chapters in this list
    "required_directions": {},
    "optional_conditions": [],
}
```

You must also add the chapter ID to `CHAPTER_ORDER` in the same file (in proper position).

### Opening Sequence Flow

The opening sequence flows without map interruption:

```
label start
    → route_map → story_hub → interactive_map
        → prologue_rain_dream
            (no map — jumps directly to tam_c01_interview_day)
            → tam_c01_interview_day
                → s01 (unlocks tam_apartment, huyen_apartment, company)
                → s02, s03, s04
                → complete_chapter → route_map (first map appearance)
```

---

## 9. Minigames

Two minigames exist in `game/minigames/`:

- **Problem Diagnosis** — `game/minigames/problem_diagnosis/`
- **Speech Ordering** — `game/minigames/speech_order/` (used in tam_c01_interview_day)

Both have global runtime support in `game/minigames/`. Library replay data for the speech minigame is in `game/data/library_minigame_data.rpy`.

### Map of Key Files

| Purpose | File |
|---------|------|
| Chapter metadata | `game/progression_data.rpy` |
| Progression logic | `game/progression_logic.rpy` |
| Character scores/flags | `game/story_state.rpy` |
| Character definitions | `game/story/common.rpy` |
| Character side images | `game/scripts/*_sprites.rpy` |
| Backgrounds | `game/scripts/backgrounds.rpy` |
| CG art | `game/scripts/cgs.rpy` |
| Map data/locations | `game/map_data.rpy` |
| Map logic/rules | `game/map_logic.rpy` |
| Map screen UI | `game/map_screen.rpy` |
| Map hub label | `game/map_hub.rpy` |
| Route timeline (legacy) | `game/route_map.rpy` |
| Chapter authoring guide | `Specs/chapter_authoring_guide.md` |
| Interactive map spec | `Specs/interactive_map.md` |
