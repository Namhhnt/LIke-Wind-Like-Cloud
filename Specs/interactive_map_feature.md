# Interactive Map System — Feature & Integration Guide

**Version:** 1.0
**Last updated:** 2026-07-05
**Location:** `Specs/interactive_map_feature.md`
**Source files:** `game/map_data.rpy`, `game/map_logic_with_interactions.rpy`, `game/map_screen_with_interactions.rpy`, `game/map_hub_with_interactions.rpy`, `game/map_location_interactions.rpy`, `game/story/locations/location_private_hubs_huyen_hoang_scenes.rpy`

---

## 1. Overview

The Interactive Map is a location-based navigation and free-time management system for *Like Wind, Like Cloud*. It provides an alternative interface to the timeline-based route map for selecting and progressing story chapters, while adding a layer of simulated "life simulation" activities between main story beats.

The map serves two distinct but connected purposes:

| Mode | Purpose | Entry Point |
|------|---------|-------------|
| **Story Hub** | Proceed to the next available chapter. Shows all unlocked/available chapters pinned to their on-map locations. | `label story_hub()` — default route map entry |
| **Free-Time Hub** | Visit a location to perform downtime activities (rest, shop, visit characters, cook, work part-time). | `label location_interaction_hub(location_id)` — accessed from story hub markers |

---

## 2. Architecture

The system is divided across five core files plus one extension file, following strict separation of concerns:

```
┌─────────────────────────────────────────────────────┐
│                    ENTRY LAYER                       │
│  map_hub_with_interactions.rpy                      │
│  • label interactive_map() — main dispatch loop      │
│  • label story_hub() — autosave + entry              │
│  • Dispatches to: chapter labels, location hub,      │
│    timeline, phone                                   │
├─────────────────────────────────────────────────────┤
│                      UI LAYER                        │
│  map_screen_with_interactions.rpy                    │
│  • screen interactive_map_screen()                   │
│  • Draggable viewport, zoom, marker rendering        │
│  • Event panel, focus button, phone button           │
│  • Hover tooltip, location label buttons             │
│  • All styles (warm-themed palette)                  │
├─────────────────────────────────────────────────────┤
│                   LOGIC LAYER                        │
│  map_logic_with_interactions.rpy                     │
│  • Entry resolution (available/locked/hidden)        │
│  • build_map_entries() — combine chapters + locations│
│  • Chapter→location mapping                          │
│  • Context queue/resolve system                      │
│  • Location unlock logic                             │
├─────────────────────────────────────────────────────┤
│                   DATA LAYER                         │
│  map_data.rpy                                        │
│  • FIXED_MAP_LOCATIONS — 10 permanent locations      │
│  • MAP_ROUTE_DEFAULT_LOCATIONS — route→location      │
│  • MAP_CHAPTER_LOCATION_OVERRIDES — chapter→location  │
│  • MAP_CONTEXTS — backgrounds, titles, rules          │
│  • MAP_CONTEXT_BY_CHAPTER / MAP_CONTEXT_BY_SCENE     │
├─────────────────────────────────────────────────────┤
│              INTERACTION LAYER                       │
│  map_location_interactions.rpy                       │
│  • MAP_LOCATION_ACTIONS — per-location free-time     │
│  • Activity state (money, time_units, energy, ...)   │
│  • perform_location_action() — effects, risks, flags │
│  • Scene router — weighted-random scene selection    │
│  • Inventory & flag system                           │
├─────────────────────────────────────────────────────┤
│              EXTENSION FILE                          │
│  story/locations/location_private_hubs_huyen_hoang.. │
│  • Scene rules for Huyền's apartment & Hoàng's house │
│  • Sample pattern for adding scripted scenes         │
│    to location interactions                          │
└─────────────────────────────────────────────────────┘
```

---

## 3. Data Structures

### 3.1 Fixed Map Locations (`FIXED_MAP_LOCATIONS`)

Ten permanent named locations on the map canvas:

| ID | Name | Category | (X, Y) | Unlock condition |
|----|------|----------|--------|-----------------|
| `tam_apartment` | Tâm's Apartment | residential | (200, 218) | `tam_c01` |
| `huyen_apartment` | Huyền's Apartment | residential | (580, 180) | `tam_c01` |
| `hoang_house` | Hoàng's House | residential_villa | (240, 732) | `tam_c02` |
| `quan_apartment` | Quân's Apartment | residential | (1158, 280) | `tam_c02` |
| `park` | Park | public | (350, 432) | `tam_c01` |
| `library` | Library | public | (550, 450) | `tam_c01` |
| `foodie_street` | Foodie Street | commercial | (720, 280) | `tam_c01` |
| `shopping_area` | Shopping Area | commercial | (438, 600) | `tam_c02` |
| `restaurant` | Restaurant | commercial | (896, 590) | `tam_c01` |
| `company` | Company | office | (1158, 548) | `tam_c01` |
| `conference_hall` | Conference Hall | event | (896, 378) | `tam_c02` |
| `airport` | Airport | transport | (1546, 170) | `yuuka_c08` |

Each location has:
- **x, y** — pixel coordinates on the 1920x1080 canvas
- **category** — used for icon and thematic grouping
- **icon** — lookup key for the location marker sprite
- **default_unlocked** — whether it starts unlocked (all `False` currently)
- **unlock_conditions** — list of condition strings (see §3.4)
- **description** — flavour text shown in the hover tooltip

### 3.2 Route→Location Defaults (`MAP_ROUTE_DEFAULT_LOCATIONS`)

Maps each route ID to a default location. Used when a chapter has no specific location override.

```python
MAP_ROUTE_DEFAULT_LOCATIONS = {
    "tam": "tam_apartment",
    "hoang": "hoang_house",
    "yuuka": "airport",
    "minh": "park",
    "thienan": "library",
    "huyen": "huyen_apartment",
    "work": "company",
    "final": "conference_hall",
}
```

### 3.3 Chapter→Location Overrides (`MAP_CHAPTER_LOCATION_OVERRIDES`)

Pins a specific chapter to a specific location, overriding the route default. ~35 chapters are currently mapped (see `game/map_data.rpy:200`). If a chapter is not listed here, its route's default location is used.

### 3.4 Condition Strings

Used in `unlock_conditions`, `conditions`, and `requires` fields. Evaluated by `map_condition_is_met()`.

| Format | Meaning |
|--------|---------|
| `always` | Always true |
| `completed:CHAPTER_ID` | Chapter completed |
| `not_completed:CHAPTER_ID` | Chapter not completed |
| `flag:FLAG_ID` | Story/activity flag is set |
| `not_flag:FLAG_ID` | Story/activity flag is NOT set |
| `direction:CHARACTER:DIRECTION` | Relationship direction matches (e.g. `direction:tam:romantic`) |

---

## 4. Entry Flow — How the Map Works End-to-End

### 4.1 Normal Flow (Story Chapter → Map → Next Chapter)

```
         ┌─────────────────────────────────┐
         │        label start               │
         │  → initialize_progression()      │
         │  → jump prologue_rain_dream      │
         └────────────┬────────────────────┘
                      │
                      ▼
         ┌─────────────────────────────────┐
         │     prologue / chapter scene     │
         │  (story content plays out)       │
         │                                 │
         │  At end of chapter:              │
         │  call story_hub()                │
         └────────────┬────────────────────┘
                      │
                      ▼
         ┌─────────────────────────────────┐
         │  label story_hub()              │
         │  • autosave_progression_at_map() │
         │  • resolve_story_map_context()   │
         │  • call interactive_map(...)     │
         └────────────┬────────────────────┘
                      │
                      ▼
         ┌─────────────────────────────────┐
         │  screen interactive_map_screen() │
         │  • Shows available chapters      │
         │    pinned to map locations       │
         │  • Player clicks a chapter       │
         │  • Returns selected entry        │
         └────────────┬────────────────────┘
                      │
          ┌───────────┴──────────┐
          ▼                      ▼
  ┌─────────────────┐  ┌──────────────────────┐
  │ Chapter label    │  │ location_interaction │
  │ jump expression  │  │ _hub()               │
  │ target_label     │  │ • Free-time actions   │
  │                  │  │ • Scene router        │
  │ → play chapter   │  │ → return to map       │
  └─────────────────┘  └──────────────────────┘
```

### 4.2 The `interactive_map` Label (Entry Point)

```renpy
label interactive_map(map_entries=None, context_id="act1_default",
                      allow_back=True, allow_timeline=False,
                      title_override=None):
```

**Parameters:**
- `map_entries` — optional explicit list of entries (`None` = auto-build from progression state)
- `context_id` — which map context to use (determines background, title, rules)
- `allow_back` — whether "Back" is available (returns to previous screen)
- `allow_timeline` — whether "Timeline View" button is shown
- `title_override` — overrides the context title in the UI

**Dispatch logic (inside the loop):**
1. Build resolved entries via `build_map_entries(map_entries, context_id)`
2. Show `interactive_map_screen` — player clicks a marker
3. On selection:
   - `_action == "timeline"` → jump to `route_map_timeline`
   - `_action == "phone"` → call `phone_home` screen
   - `action_type == "location_hub"` → call `location_interaction_hub(location_id)`
   - Otherwise → resolve the target label via `resolve_map_target_label()` → `jump expression next_label`

### 4.3 Auto Context Resolution

The map context (background image, time-of-day variant) is determined by:

1. **Explicit**: caller passes `context_id`
2. **Queued**: `queue_story_map_context(context_id, chapter_id, scene_id)` sets a pending context
3. **Chapter-based**: after queue is consumed, checks `MAP_CONTEXT_BY_CHAPTER` for the last completed chapter
4. **Default**: falls back to `"act1_default"`

```renpy
# In a chapter's end: queue a specific context for the map
$ queue_story_map_context(context_id="evening_default")

# Then return to the map
call story_hub()
```

### 4.4 Autosave

On every `story_hub()` entry, the game autosaves to slot `"_progression_auto"`. This gives players a reliable save point before every map-based decision.

---

## 5. Location Interaction System (Free-Time Actions)

Accessed when the player clicks a location's hub icon (vs. clicking a specific chapter marker at that location). Each location has a set of actions defined in `MAP_LOCATION_ACTIONS`.

### 5.1 Activity State

Managed by `ensure_activity_state()` — stored in `progress["activity_state"]`:

| Stat | Default | Range | Description |
|------|---------|-------|-------------|
| `money` | 3,000,000₫ | 0–999M | Currency for purchases |
| `time_units` | 5 | 0–100 | Free actions per session |
| `energy` | 70 | 0–100 | Depletes on activity |
| `stress` | 20 | 0–100 | Accumulates, affects health |
| `mood` | 50 | 0–100 | General emotional state |
| `health` | 75 | 0–100 | Overall health |
| `confidence` | 0 | -50–100 | Social/professional confidence |
| `style` | 0 | -50–100 | Fashion/style rating |
| `knowledge` | 0 | 0–100 | General knowledge |
| `work_skill` | 0 | 0–100 | Work competence |
| `cooking_skill` | 0 | 0–100 | Cooking ability |
| `life_skill` | 0 | 0–100 | Domestic/life ability |
| `main_work_focus` | 50 | 0–100 | Career focus |
| `part_time_count_this_period` | 0 | 0–99 | Overwork counter |

Also tracks:
- **inventory** — dict of `{item_id: quantity}` (groceries, small_gift, office_clothes, party_dress, work_books)
- **flags** — list of activity/story flag strings
- **completed_actions** — list of one-time action IDs that have been used

### 5.2 Action Schema

```python
{
    "id": "tam_home_rest",           # unique action ID
    "title": "Rest at home",         # display name
    "summary": "Recover energy...",  # tooltip text
    "category": "Rest",              # category grouping in UI
    "time_cost": 1,                  # time units consumed
    "money_cost": 0,                 # money cost (if any)
    "requires": {                    # prerequisite checks
        "time_units": 1,
        "money": 0,
        "energy_min": 0,             # minimum energy required
        "inventory": {"item": 1},    # items required
    },
    "effects": {                     # stat changes on completion
        "time_units": -1,
        "energy": 18,
        "stress": -10,
        "mood": 4,
    },
    "inventory_effects": {           # inventory changes
        "groceries": -1,
    },
    "story_effects": {               # story score changes
        "tam_self_clarity": 1,
    },
    "flags": ["flag_id"],            # flags set on completion
    "once": True,                    # can only be done once
    "overwork_sensitive": True,      # tracked for overwork penalty
    "risk": {                        # chance-based negative outcome
        "chance": 0.08,
        "effects": {"health": -1},
        "message": "...",
        "flags": ["minor_stomach_ache"],
    },
    "message": "Custom narration...",  # shown after action
    "messages": [                      # weighted random narration pool
        {"text": "...", "weight": 1, "conditions": [...]},
        "Simple string fallback...",
    ],
}
```

### 5.3 Available Actions by Location

| Location | Actions |
|----------|---------|
| **Tâm's Apartment** | Rest at home, Cook a simple meal, Clean and organize, Journal/write |
| **Foodie Street** | Snack-hopping, buy groceries |
| **Shopping Area** | Buy office clothes, buy party dress, buy books, part-time promotion booth |
| **Library** | Read quietly |
| **Huyền's Apartment** | Visit Huyền, give small gift, invite to Foodie Street |
| **Hoàng's House** | Visit Hoàng (casual), help with design work |
| **Quân's Apartment** | Visit Quân, help sort documents |
| **Restaurant** | *(scene-router only, no free actions yet)* |
| **Park** | *(scene-router only, no free actions yet)* |
| **Company** | *(scene-router only, no free actions yet)* |
| **Conference Hall** | *(no actions yet)* |
| **Airport** | *(no actions yet)* |

### 5.4 Overwork and Health Penalties

The system has automatic safeguard mechanics:
- **Overwork**: `part_time_count_this_period` ≥ 10 triggers `main_work_focus -5`, `health -4`, `career_tam -1`
- **Critical state**: If `energy ≤ 12` or `stress ≥ 90`, `health -5` and `mood -4` are applied after every action

---

## 6. Scene Router System

Extensible scene selection for location interactions using conditions, priority, and weighted randomness.

### 6.1 Scene Rules Structure

```python
MAP_LOCATION_SCENE_RULES["huyen_apartment"]["huyen_visit_chat"] = {
    "mode": "weighted_random",        # or "first", "random"
    "default_label": "loc_huyen_home_default_tea",
    "scenes": [
        {
            "label": "loc_huyen_home_after_company_party_unique",
            "priority": 100,
            "weight": 1,
            "conditions": ["completed:tam_c02_company_party"],
            "min_scores": {"tam_hoang_interest": 1},
            "required_flags": [],
            "blocked_flags": ["loc_seen_huyen_home_after_company_party_unique"],
        },
        { "label": "loc_huyen_home_default_tea", "priority": 0, "weight": 4 },
        { "label": "loc_huyen_home_default_rain_window", "priority": 0, "weight": 3 },
    ],
}
```

**Routing modes:**
- `weighted_random` — pick from available scenes by weight (default)
- `first` — pick first available scene (by highest priority)
- `random` — pick randomly from highest-priority scenes

### 6.2 Extending with New Scene Rules

Create a new file under `game/story/locations/` and follow this pattern:

```python
init 0 python:
    from map_location_interactions import MAP_LOCATION_ACTIONS, MAP_LOCATION_SCENE_RULES

    # Enable scene router on an action (if not already enabled)
    for action in MAP_LOCATION_ACTIONS.get("restaurant", []):
        if action["id"] == "restaurant_visit":
            action["use_scene_router"] = True
            action["scene_key"] = "restaurant_visit"

    # Define scenes
    MAP_LOCATION_SCENE_RULES.setdefault("restaurant", {})
    MAP_LOCATION_SCENE_RULES["restaurant"]["restaurant_visit"] = {
        "mode": "weighted_random",
        "scenes": [
            { "label": "loc_restaurant_default", "priority": 0, "weight": 1 }
        ],
    }
```

---

## 7. Map Contexts (Time-of-Day / Atmosphere)

`MAP_CONTEXTS` defines visual and behavioral settings for different map states:

| Context ID | Background | Purpose |
|-----------|------------|---------|
| `act1_default` | `city_map_day.png` | Default act 1 |
| `day_default` | `city_map_day.png` | Daytime |
| `afternoon_default` | `city_map_afternoon.png` | Afternoon |
| `evening_default` | `city_map_evening.png` | Evening |
| `night_default` | `city_map_night.png` | Night |
| `festival_finale` | `city_map_night.png` | Finale (festival) |

Each context supports:
- **temporarily_locked_locations** — `{location_id: "reason string"}` — locks specific locations for this context
- **force_only_locations** — `[location_ids]` — hides all but these locations
- **show_locked_fixed_locations** — whether to show locked-but-known locations (greyed out)

---

## 8. How to Use from Story Chapters

### 8.1 Return to Map After a Chapter

At the end of any story chapter:

```renpy
# Simple: return to story hub (auto-saves, resolves context)
call story_hub()

# With a specific context (time-of-day)
$ queue_story_map_context(context_id="evening_default")
call story_hub()

# Just show the map interactively (no autosave)
call interactive_map()
```

### 8.2 Queue Context Before Returning

If a chapter ends in the evening and the map should reflect that:

```renpy
label tam_c02_company_party:
    # ... story content ...
    $ queue_story_map_context(context_id="evening_default")
    call story_hub()
    return
```

### 8.3 Open the Map with Specific Entries

For scripted moments where only specific locations should be available:

```renpy
$ custom_entries = [
    {
        "id": "special_event",
        "title": "Something Special",
        "target_label": "my_special_scene",
        "location_id": "park",
        "kind": "main",
        "description": "A unique event on the map.",
    },
]
call interactive_map(map_entries=custom_entries, context_id="night_default")
```

### 8.4 Open a Location Hub Directly

```renpy
# Jump directly into a location's free-time menu
call location_interaction_hub("tam_apartment")
```

### 8.5 Unlock a Location

```renpy
# After completing a chapter, unlock a new location
$ unlock_map_locations(["new_location_id"])
```

### 8.6 Interaction Functions from Story Code

Any Python function exposed in `map_location_interactions.rpy` can be called from story scripts:

```renpy
# Currency
$ money = activity_get("money")
$ activity_add("money", 500000)
$ activity_set("time_units", 5)

# Inventory
$ activity_inventory_add("small_gift", 1)
$ has_item = activity_inventory_get("groceries")

# Flags
$ activity_add_flag("tam_has_party_dress")

# Story scores
$ activity_apply_story_effects({"tam_self_clarity": 1})

# Start a free-time session
$ activity_start_free_time_session(time_units=5)
```

---

## 9. Adding New Locations

### Step 1: Define the location

In `map_data.rpy`, add to `FIXED_MAP_LOCATIONS`:

```python
"new_location": {
    "id": "new_location",
    "name": "New Location Name",
    "x": 700,            # canvas coordinate (1920x1080)
    "y": 400,
    "category": "public",  # residential, commercial, office, event, public, transport
    "icon": "default",
    "default_unlocked": False,
    "unlock_conditions": ["completed:tam_c01_interview_day"],
    "description": "What the hover tooltip shows.",
},
```

### Step 2: Map chapters to it (optional)

```python
MAP_CHAPTER_LOCATION_OVERRIDES["chapter_id"] = "new_location"
```

### Step 3: Add free-time actions (optional)

In `map_location_interactions.rpy`:

```python
MAP_LOCATION_ACTIONS.setdefault("new_location", []).extend([
    {
        "id": "new_location_action",
        "title": "Do Something",
        "summary": "It does something.",
        "category": "Action",
        "time_cost": 1,
        "requires": {"time_units": 1},
        "effects": {"time_units": -1, "mood": 5},
        "message": "You did something.",
    },
])
```

### Step 4: Add scene rules (optional)

In your story location file:

```python
MAP_LOCATION_SCENE_RULES.setdefault("new_location", {})
MAP_LOCATION_SCENE_RULES["new_location"]["new_location_action"] = {
    "mode": "weighted_random",
    "scenes": [
        { "label": "loc_new_location_default", "priority": 0, "weight": 1 },
    ],
}
```

---

## 10. Adding New Free-Time Actions

```python
MAP_LOCATION_ACTIONS.setdefault("existing_location", []).extend([
    {
        "id": "unique_action_id",
        "title": "Display Name",
        "summary": "Short description shown in UI.",
        "category": "Home",  # Rest, Food, Shopping, Visit, Gift, Part-time, ...
        "time_cost": 1,
        "money_cost": 0,
        "requires": {"time_units": 1, "money": 0},
        "effects": {"time_units": -1, "energy": 10, "mood": 3},
        "inventory_effects": {},
        "story_effects": {},
        "flags": [],
        "once": False,
        "message": "Narration text...",
    },
])
```

**Effect keys** available: `time_units`, `money`, `energy`, `stress`, `mood`, `health`, `confidence`, `style`, `knowledge`, `work_skill`, `cooking_skill`, `life_skill`, `main_work_focus`.

**Story effect keys** available: any story score from `story_state.py` — `tam_self_clarity`, `tam_observation`, `tam_hoang_interest`, `career_tam`, etc.

---

## 11. Integration with Other Systems

### 11.1 Progression System

The map reads directly from the progression system's `progress` dict:
- **Available chapters**: `progress["available"]` — what the player can play next
- **Completed chapters**: `progress["completed"]` — used for unlock conditions
- **Flags**: `progress["player_flags"]` — used for condition checks
- **State auto-persisted** via `autosave_progression_at_map()`

### 11.2 Route Map (Timeline)

The timeline-based `route_map.rpy` and the interactive map coexist:
- `label route_map` defaults to `story_hub()` (opens the interactive map)
- From the interactive map, player can switch to timeline view (if `allow_timeline=True`)
- Both read from the same `progress` state — they stay in sync

### 11.3 Phone System

The map includes a phone button that opens the smartphone directly. This is a read-only integration — the phone overlays the map and returns when dismissed.

### 11.4 Minigames

Actions with `target_label` set can jump to minigame labels. The minigame runs within the context of the action, and the player returns to the map afterward.

---

## 12. UI Reference

### 12.1 Screen Layout

```
┌──────────────────────────────────────────────────────┐
│ ┌─────────────────────────────────────────────────┐  │
│ │                                                 │  │
│ │  ┌──────┐                                       │  │
│ │  │ Title│              MAP CANVAS               │  │
│ │  │      │         (viewport, draggable)         │  │
│ │  └──────┘                                       │  │
│ │                               ┌─────┐           │  │
│ │  ┌───────────────────┐        │Events│          │  │
│ │  │ Drag hint          │        │Panel │          │  │
│ │  │ [📱] [Focus Button]│        │      │          │  │
│ │  └───────────────────┘        └─────┘           │  │
│ │                                         [⚙ Timel]│  │
│ └─────────────────────────────────────────────────┘  │
│ ┌─────────────────────────────────────────────────┐  │
│ │              Bottom info area                    │  │
│ │  [selected location details / hover tooltip]      │  │
│ └─────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────┘
```

### 12.2 Marker Types

| Kind | Visual | Behavior |
|------|--------|----------|
| `main` | Core chapter (gold/highlighted) | Available to play |
| `character` | POV chapter | Available to play |
| `bonus` | Bonus/extra chapter | Available to play |
| `extra` | Generic chapter | Available to play |
| `locked` | Greyed out, no click | Shows lock reason |
| `location_hub` | Unique icon | Opens action menu |

### 12.3 Marker Offset System

When multiple entries share the same location, `MAP_MARKER_OFFSETS` spreads them visually:

```python
MAP_MARKER_OFFSETS = [
    (0, 0),       # first entry — exact location
    (-44, -34),   # second entry — up-left
    (46, -28),    # third entry — up-right
    (-56, 34),    # fourth entry — down-left
    (58, 38),     # fifth entry — down-right
    (0, 62),      # sixth entry — below
]
```

---

## 13. Style Constants

All map styles are defined in `map_screen_with_interactions.rpy` under `style interactive_map_*`. Key palette:

| Token | Value | Used for |
|-------|-------|----------|
| Title | `#f5d7a6` `bold 45px` | Map title |
| Subtitle | `#e7d8c0` `21px` | Subtitle text |
| Panel title | `#f2dfbf` `30px bold` | Section headers |
| Panel body | `#ddccb5` `19px` | Description text |
| Marker (available) | Gold highlight | Active chapter |
| Marker (locked) | Dimmed, muted | Inaccessible |
| Background fallback | `#15120f` | If map image is missing |
| Overlay | `#05040355` (semi) | Dark vignette over map |

---

## 14. File Inventory

| File | Lines | Role |
|------|-------|------|
| `game/map_data.rpy` | ~256 | All data definitions |
| `game/map_logic_with_interactions.rpy` | ~440 | Core logic |
| `game/map_screen_with_interactions.rpy` | ~360 | UI screen + styles |
| `game/map_hub_with_interactions.rpy` | ~50 | Entry label + dispatch |
| `game/map_location_interactions.rpy` | ~1250 | Actions, state, scene router |
| `game/story/locations/location_private_hubs_huyen_hoang_scenes.rpy` | ~150 | Extension scenes |
| `game/script.rpy` | (partial) | `autosave_progression_at_map()` |
| `game/route_map.rpy` | (partial) | `story_hub()` as default dispatch |

---

## 15. Common Patterns

### After Chapter Completion

```renpy
# In your chapter's final label:
$ complete_chapter("tam_c03_thienan_family")
$ unlock_map_locations(["hoang_house"])

# Queue evening context and return to map
$ queue_story_map_context(context_id="evening_default")
call story_hub()
return
```

### Scripted Map Visit

```renpy
# Force player to visit a specific location before continuing
$ queue_story_map_context(context_id="day_default")
$ forced_entries = [
    {
        "id": "forced_tam_apartment",
        "location_id": "tam_apartment",
        "title": "Check on Tâm",
        "action_type": "location_hub",
        "kind": "main",
        "description": "You should see how Tâm is doing.",
    },
]
call interactive_map(map_entries=forced_entries, allow_back=False)
```

### Custom Context with Locked Locations

```python
MAP_CONTEXTS["post_storm"] = {
    "background": "images/maps/city_map_night.webp",
    "title": "After the Storm",
    "subtitle": "Some areas are still closed off.",
    "show_locked_fixed_locations": True,
    "temporarily_locked_locations": {
        "park": "The park is closed after the storm.",
        "airport": "All flights are suspended.",
    },
    "force_only_locations": [],
}
```

---

## 16. Notes & Caveats

- **No TEMPORARY_MAP_LOCATIONS exist yet** — the `temporary` entry kind is supported in code but no data uses it. To add temporary (one-time) locations, pass entries with `"category": "temporary"` directly in the `map_entries` parameter.
- **Map background images** referenced in `MAP_CONTEXTS` (`city_map_day.png`, `city_map_afternoon.png`, `city_map_evening.png`, `city_map_night.png`) may not all exist as assets on disk — the UI gracefully falls back to `city_map_day.png`, then to `background_full.png`, then to a solid colour.
- **Activity state persists** across the game session via `progress["activity_state"]`. It is saved in the autosave, so free-time progress is checkpointed.
- **New locations need at least one unlock condition** to appear. If you add a location with `default_unlocked: False` and no conditions, it will never unlock.
- **`build_story_hub_raw_entries()` only returns available chapters** from the progression system. If a chapter is already completed or hidden, it won't appear on the map.
