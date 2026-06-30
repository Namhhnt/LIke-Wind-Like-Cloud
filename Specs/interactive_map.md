# Technical Implementation Document

# Interactive Map Screen for Ren’Py Visual Novel

## 1. Objective

Implement an **Interactive Map screen** for the game, allowing players to click locations on a city/world map to continue story events.

The map system must support:

* Fixed story locations such as:

  * Tâm’s Apartment
  * Huyền’s Apartment
  * Hoàng/Minh’s House
  * Park
  * Library
  * Foodie Street
  * Shopping Area
  * Restaurant
  * Company / Office District
  * Airport
  * Conference Hall / Event Building
* Temporary chapter-specific locations.
* Location unlock based on story progress.
* Temporary lock of fixed locations to force correct route pacing.
* Each chapter/label can pass a custom list of map locations and target labels.
* Clicking a location returns a target chapter/label and jumps to it.

The Interactive Map should **not replace the progression system**. It should act as an alternate UI layer for selecting available story events.

Existing progression conventions should remain valid:

* Each playable chapter has an object in `CHAPTERS`.
* Each chapter object has a matching Ren’Py label.
* Chapters can unlock other chapters through `unlocks`.
* Chapters can depend on `prerequisites`.
* Chapters should still end with `$ complete_chapter("chapter_id")`.
* Current chapter types such as `core`, `pov`, `bonus`, and `extra` should continue to work.

---

# 2. Design Principle

## 2.1 Map is an interaction layer, not the story brain

The map should answer one question:

> “Where can the player go right now?”

It should not independently decide narrative progression.

Narrative rules should still live in:

```text
game/progression_data.rpy
game/progression_logic.rpy
```

The map only resolves visible/clickable location entries and returns the next target label.

---

## 2.2 Fixed locations vs temporary locations

There are two types of locations.

### Fixed Locations

Fixed locations exist permanently on the city map.

Examples:

```text
tam_apartment
huyen_apartment
hoang_house
park
library
foodie_street
shopping_area
restaurant
company
airport
conference_hall
```

Fixed locations have stable coordinates on the map.

They may be:

* locked at the start
* unlocked by chapter progress
* visible but disabled
* temporarily locked during specific story contexts
* hidden if not yet discovered

### Temporary Locations

Temporary locations only exist for a specific chapter, route, or condition.

Examples:

```text
event_backdoor
private_corridor
festival_side_gate
temporary_hotel
hospital_room
school_reunion_room
```

Temporary locations may use custom coordinates and may disappear after the event is completed.

---

# 3. Recommended File Structure

Add these files:

```text
game/map_data.rpy
game/map_logic.rpy
game/map_screen.rpy
game/map_hub.rpy
```

Optional later:

```text
game/tl/vietnamese/map_screen.rpy
```

Suggested responsibility:

```text
map_data.rpy      Fixed map location definitions and map contexts.
map_logic.rpy     Helper functions for unlock, lock, filtering, and target resolution.
map_screen.rpy    Ren’Py screen UI.
map_hub.rpy       Wrapper label used by chapters to call the map.
```

---

# 4. Map Asset

Use a 16:9 map background image.

Recommended path:

```text
game/images/maps/city_map_01_day.png
```

For future variations:

```text
game/images/maps/city_map_01_evening.png
game/images/maps/city_map_01_night.png
game/images/maps/city_map_01_rain.png
```

The current map should not contain printed labels. All labels, buttons, hover panels, and lock markers should be UI overlays.

---

# 5. Coordinate System

Assume a 1920x1080 base resolution.

Each location uses pixel coordinates:

```python
"x": 320,
"y": 220,
```

The UI button should be anchored at the center:

```renpy
anchor (0.5, 0.5)
pos (x, y)
```

If the game later supports different resolutions, scale coordinates based on current screen size.

For now, keep the map at 1920x1080 for simplicity.

---

# 6. Fixed Location Data

Create in `game/map_data.rpy`:

```renpy
init python:

    FIXED_MAP_LOCATIONS = {
        "tam_apartment": {
            "id": "tam_apartment",
            "name": "Tâm's Apartment",
            "x": 230,
            "y": 165,
            "category": "residential",
            "icon": "apartment_high",
            "default_unlocked": True,
            "unlock_conditions": [],
            "description": "Modern upscale apartment complex.",
        },

        "huyen_apartment": {
            "id": "huyen_apartment",
            "name": "Huyền's Apartment",
            "x": 470,
            "y": 250,
            "category": "residential",
            "icon": "apartment_mid",
            "default_unlocked": True,
            "unlock_conditions": [],
            "description": "More ordinary apartment area near local food streets.",
        },

        "hoang_house": {
            "id": "hoang_house",
            "name": "Hoàng / Minh's House",
            "x": 310,
            "y": 780,
            "category": "residential_villa",
            "icon": "villa",
            "default_unlocked": False,
            "unlock_conditions": ["completed:tam_c01"],
            "description": "Detached villa district in the lower-left area.",
        },

        "park": {
            "id": "park",
            "name": "Park",
            "x": 290,
            "y": 455,
            "category": "public",
            "icon": "park",
            "default_unlocked": True,
            "unlock_conditions": [],
        },

        "library": {
            "id": "library",
            "name": "Library",
            "x": 620,
            "y": 500,
            "category": "public",
            "icon": "library",
            "default_unlocked": False,
            "unlock_conditions": ["completed:tam_c01"],
        },

        "foodie_street": {
            "id": "foodie_street",
            "name": "Foodie Street",
            "x": 760,
            "y": 300,
            "category": "commercial",
            "icon": "food",
            "default_unlocked": True,
            "unlock_conditions": [],
        },

        "shopping_area": {
            "id": "shopping_area",
            "name": "Shopping Area",
            "x": 910,
            "y": 285,
            "category": "commercial",
            "icon": "shopping",
            "default_unlocked": False,
            "unlock_conditions": ["completed:tam_c02"],
        },

        "restaurant": {
            "id": "restaurant",
            "name": "Restaurant",
            "x": 830,
            "y": 355,
            "category": "commercial",
            "icon": "restaurant",
            "default_unlocked": True,
            "unlock_conditions": [],
        },

        "company": {
            "id": "company",
            "name": "Company",
            "x": 1130,
            "y": 540,
            "category": "office",
            "icon": "office",
            "default_unlocked": False,
            "unlock_conditions": ["completed:tam_c01"],
        },

        "conference_hall": {
            "id": "conference_hall",
            "name": "Conference Hall",
            "x": 1010,
            "y": 465,
            "category": "event",
            "icon": "event",
            "default_unlocked": False,
            "unlock_conditions": ["completed:tam_c02"],
        },

        "airport": {
            "id": "airport",
            "name": "Airport",
            "x": 1530,
            "y": 170,
            "category": "transport",
            "icon": "airport",
            "default_unlocked": False,
            "unlock_conditions": ["completed:yuuka_return_notice"],
        },
    }
```

The coordinates above are starter values. They should be tuned using a debug coordinate overlay.

---

# 7. Map Context Data

A map context represents the current story situation.

Example:

```renpy
init python:

    MAP_CONTEXTS = {
        "act1_default": {
            "background": "images/maps/city_map_01_day.png",
            "title": "City Map",
            "show_locked_fixed_locations": True,
            "temporarily_locked_locations": {},
            "force_only_locations": [],
        },

        "tam_c02_evening": {
            "background": "images/maps/city_map_01_evening.png",
            "title": "Evening",
            "show_locked_fixed_locations": True,

            # These locations are visible but disabled.
            "temporarily_locked_locations": {
                "park": "Not the right time.",
                "library": "Closed for the evening.",
                "airport": "No reason to go there yet.",
            },

            # If non-empty, only these locations are clickable.
            # Others can be shown as disabled.
            "force_only_locations": [
                "company",
                "foodie_street",
                "restaurant",
            ],
        },

        "festival_finale": {
            "background": "images/maps/city_map_01_night.png",
            "title": "Festival Night",
            "show_locked_fixed_locations": False,
            "temporarily_locked_locations": {},
            "force_only_locations": [
                "conference_hall",
            ],
        },
    }
```

Use `force_only_locations` when the story needs to prevent the player from wandering into the wrong route.

This is useful for high-emotion or high-risk chapters.

Example:

```text
During a finale / confession / breakup / crisis scene,
do not let the player freely go to Foodie Street.
This is not a buffet. Behave.
```

---

# 8. Map Entry Data Passed From Chapter

Each chapter can pass a list of map entries.

A map entry can point to either:

* a fixed location
* a temporary coordinate
* a target Ren’Py label
* a target chapter id

Recommended structure:

```python
{
    "id": "tam_c02_company_event",
    "location_id": "company",
    "title": "Go to the company party",
    "kind": "main",
    "target_chapter_id": "tam_c02_party",
    "required": True,
}
```

Or with direct label:

```python
{
    "id": "tam_c02_foodie_bonus",
    "location_id": "foodie_street",
    "title": "Meet Huyền before the party",
    "kind": "bonus",
    "target_label": "tam_c02_huyen_foodie_bonus",
    "conditions": ["completed:tam_c01"],
}
```

Temporary location:

```python
{
    "id": "festival_backdoor",
    "name": "Side Entrance",
    "x": 970,
    "y": 505,
    "kind": "temporary",
    "target_label": "festival_backdoor_scene",
    "conditions": ["flag:knows_event_backdoor"],
}
```

Rules:

```text
location_id is optional if x/y are provided.
x/y are optional if location_id is provided.
target_label or target_chapter_id is required.
```

---

# 9. Entry Types

Use `kind` to control marker style and priority.

Recommended values:

```text
main        Required story event
character   Character interaction
bonus       Optional meaningful scene
extra       Optional light scene
temporary   Chapter-only location
locked      Display-only locked marker
```

Suggested visual hierarchy:

```text
main        largest marker, highlighted
character   medium marker
bonus       smaller marker
extra       subtle marker
temporary   special marker
locked      gray / disabled marker
```

---

# 10. Map Logic

Create in `game/map_logic.rpy`.

## 10.1 Condition checking

```renpy
init python:

    def map_condition_is_met(condition):
        """
        Supports simple condition strings:
        - completed:chapter_id
        - not_completed:chapter_id
        - flag:flag_name
        - not_flag:flag_name
        - direction:character:direction
        - always
        """

        if not condition or condition == "always":
            return True

        parts = condition.split(":")

        if parts[0] == "completed":
            chapter_id = parts[1]
            return chapter_id in progress.get("completed", [])

        if parts[0] == "not_completed":
            chapter_id = parts[1]
            return chapter_id not in progress.get("completed", [])

        if parts[0] == "flag":
            flag_name = parts[1]
            return flag_name in progress.get("player_flags", [])

        if parts[0] == "not_flag":
            flag_name = parts[1]
            return flag_name not in progress.get("player_flags", [])

        if parts[0] == "direction":
            character_id = parts[1]
            direction = parts[2]
            directions = progress.get("relationship_directions", {}).get(character_id, [])
            return direction in directions

        return False


    def map_conditions_are_met(conditions):
        if not conditions:
            return True

        for condition in conditions:
            if not map_condition_is_met(condition):
                return False

        return True
```

If the current project already has a more complete condition checker, reuse that instead of duplicating logic.

---

## 10.2 Fixed location unlock check

```renpy
init python:

    def fixed_location_is_unlocked(location_id):
        loc = FIXED_MAP_LOCATIONS.get(location_id)

        if not loc:
            return False

        if loc.get("default_unlocked", False):
            return True

        return map_conditions_are_met(loc.get("unlock_conditions", []))
```

---

## 10.3 Resolve raw entry

```renpy
init python:

    def resolve_map_entry(raw_entry):
        """
        Merge a raw chapter entry with fixed location data.
        """

        entry = dict(raw_entry)

        location_id = entry.get("location_id")

        if location_id:
            fixed = FIXED_MAP_LOCATIONS.get(location_id, {})

            entry.setdefault("name", fixed.get("name", "Unknown Location"))
            entry.setdefault("x", fixed.get("x", 0))
            entry.setdefault("y", fixed.get("y", 0))
            entry.setdefault("category", fixed.get("category", "unknown"))
            entry.setdefault("icon", fixed.get("icon", "default"))
            entry.setdefault("description", fixed.get("description", ""))

        else:
            entry.setdefault("name", entry.get("title", "Temporary Location"))
            entry.setdefault("category", "temporary")
            entry.setdefault("icon", "temporary")

        entry.setdefault("kind", "extra")
        entry.setdefault("conditions", [])
        entry.setdefault("required", False)
        entry.setdefault("enabled", True)
        entry.setdefault("lock_reason", "")

        return entry
```

---

## 10.4 Entry availability

```renpy
init python:

    def map_entry_is_available(entry, context=None):
        """
        Returns:
        - available
        - locked
        - hidden
        """

        location_id = entry.get("location_id")

        # Fixed location must be unlocked first.
        if location_id:
            if not fixed_location_is_unlocked(location_id):
                return "hidden"

        # Entry-specific conditions.
        if not map_conditions_are_met(entry.get("conditions", [])):
            return "hidden"

        if not entry.get("enabled", True):
            return "locked"

        if context:
            temp_locks = context.get("temporarily_locked_locations", {})

            if location_id in temp_locks:
                entry["lock_reason"] = temp_locks[location_id]
                return "locked"

            force_only = context.get("force_only_locations", [])

            if force_only and location_id and location_id not in force_only:
                entry["lock_reason"] = "Not available right now."
                return "locked"

        # Optional: target chapter availability.
        target_chapter_id = entry.get("target_chapter_id")

        if target_chapter_id:
            if not chapter_is_available_for_map(target_chapter_id):
                entry["lock_reason"] = "Story event is not available yet."
                return "locked"

        return "available"
```

Add wrapper for chapter availability.

```renpy
init python:

    def chapter_is_available_for_map(chapter_id):
        """
        Replace this with the existing chapter availability function
        if the project already has one.
        """

        chapter = CHAPTERS.get(chapter_id)

        if not chapter:
            return False

        prereqs = chapter.get("prerequisites", [])

        for prereq in prereqs:
            if prereq not in progress.get("completed", []):
                return False

        if chapter_id in progress.get("completed", []):
            return False

        if chapter_id in progress.get("excluded", []):
            return False

        return True
```

---

## 10.5 Build final entries for screen

```renpy
init python:

    def build_map_entries(raw_entries=None, context_id="act1_default"):
        raw_entries = raw_entries or []

        context = MAP_CONTEXTS.get(context_id, MAP_CONTEXTS["act1_default"])

        final_entries = []

        for raw_entry in raw_entries:
            entry = resolve_map_entry(raw_entry)
            state = map_entry_is_available(entry, context)

            if state == "hidden":
                continue

            entry["state"] = state
            final_entries.append(entry)

        final_entries.sort(key=lambda e: (
            0 if e.get("kind") == "main" else
            1 if e.get("kind") == "character" else
            2 if e.get("kind") == "bonus" else
            3
        ))

        return final_entries
```

---

# 11. Target Resolution

When the player clicks a map entry, the game should resolve the next label.

```renpy
init python:

    def resolve_map_target_label(entry):
        if entry.get("target_label"):
            return entry["target_label"]

        chapter_id = entry.get("target_chapter_id")

        if chapter_id:
            chapter = CHAPTERS.get(chapter_id)

            if chapter:
                return chapter.get("label")

        return None
```

---

# 12. Interactive Map Screen

Create in `game/map_screen.rpy`.

Basic implementation:

```renpy
screen interactive_map_screen(entries, context_id="act1_default", allow_back=True):

    tag menu

    $ context = MAP_CONTEXTS.get(context_id, MAP_CONTEXTS["act1_default"])
    $ bg = context.get("background", "images/maps/city_map_01_day.png")

    default hovered_entry = None

    add bg

    # Optional dark overlay for readability
    add Solid("#00000022")

    for entry in entries:

        $ state = entry.get("state", "available")
        $ is_available = state == "available"
        $ marker_size = 52 if entry.get("kind") == "main" else 42

        button:
            pos (entry["x"], entry["y"])
            anchor (0.5, 0.5)
            xysize (marker_size, marker_size)
            sensitive is_available

            hovered SetScreenVariable("hovered_entry", entry)
            unhovered SetScreenVariable("hovered_entry", None)

            if is_available:
                action Return(entry)
            else:
                action NullAction()

            background None

            if state == "available":
                add "gui/map/marker_available.png" xysize (marker_size, marker_size)
            else:
                add "gui/map/marker_locked.png" xysize (marker_size, marker_size)

    if hovered_entry:
        use map_hover_panel(hovered_entry)

    if allow_back:
        textbutton "Back":
            xalign 0.03
            yalign 0.94
            action Return(None)
```

Hover panel:

```renpy
screen map_hover_panel(entry):

    frame:
        xalign 0.5
        yalign 0.92
        xmaximum 760
        padding (24, 16)

        vbox:
            spacing 6

            text entry.get("title", entry.get("name", "")) size 28

            if entry.get("state") == "locked":
                text entry.get("lock_reason", "Locked.") size 20 color "#cfcfcf"
            elif entry.get("description"):
                text entry.get("description") size 20 color "#dddddd"
```

Important:

* The map background should have no printed labels.
* The hover panel may show names/titles.
* If a completely label-free UI is desired, disable `map_hover_panel`.

---

# 13. Map Marker Assets

Recommended assets:

```text
game/gui/map/marker_available.png
game/gui/map/marker_main.png
game/gui/map/marker_character.png
game/gui/map/marker_bonus.png
game/gui/map/marker_locked.png
game/gui/map/marker_temporary.png
```

Fallback option: use textbuttons or colored circles first.

Temporary dev marker:

```renpy
textbutton "●":
    text_size 42
    text_color "#ffffff"
    text_hover_color "#ffd27a"
```

Replace with proper assets later.

---

# 14. Interactive Map Wrapper Label

Create in `game/map_hub.rpy`.

```renpy
label interactive_map(map_entries=None, context_id="act1_default", allow_back=True):

    $ resolved_entries = build_map_entries(map_entries, context_id)

    if not resolved_entries:
        "There is nowhere to go right now."
        return

    call screen interactive_map_screen(resolved_entries, context_id=context_id, allow_back=allow_back)

    $ selected_entry = _return

    if not selected_entry:
        return

    $ next_label = resolve_map_target_label(selected_entry)

    if not next_label:
        "This location has no valid story target."
        return

    jump expression next_label
```

---

# 15. Example Usage inside a Chapter

Example: Tâm chapter wants the player to choose where to go next.

```renpy
label tam_c02_map_choice:

    $ map_entries = [
        {
            "id": "tam_c02_main_company_party",
            "location_id": "company",
            "title": "Go to the company party",
            "kind": "main",
            "target_chapter_id": "tam_c02_party",
            "required": True,
        },
        {
            "id": "tam_c02_huyen_foodie_bonus",
            "location_id": "foodie_street",
            "title": "Meet Huyền before the party",
            "kind": "bonus",
            "target_label": "tam_c02_huyen_foodie_bonus",
            "conditions": ["completed:tam_c01"],
        },
        {
            "id": "tam_c02_restaurant_extra",
            "location_id": "restaurant",
            "title": "Have a quiet meal first",
            "kind": "extra",
            "target_label": "tam_c02_restaurant_extra",
        },
    ]

    call interactive_map(map_entries, context_id="tam_c02_evening", allow_back=False)
```

---

# 16. Example Target Chapter

If using `target_chapter_id`, the chapter should still follow the current chapter pattern.

```renpy
label tam_c02_party:

    "Company party scene starts here."

    # Story content...

    $ complete_chapter("tam_c02_party")

    jump story_hub
```

Recommended: introduce a generic `story_hub` label.

```renpy
label story_hub:

    # Later this can decide:
    # - jump route_map
    # - call interactive map
    # - show route selection
    # - go to next forced story chapter

    jump route_map
```

This avoids hardcoding `jump route_map` everywhere.

---

# 17. Fixed Location Unlock Example

If Hoàng/Minh’s house should unlock after Tâm meets Hoàng:

```python
"hoang_house": {
    "id": "hoang_house",
    "name": "Hoàng / Minh's House",
    "x": 310,
    "y": 780,
    "category": "residential_villa",
    "icon": "villa",
    "default_unlocked": False,
    "unlock_conditions": ["completed:tam_c02_party"],
}
```

After `tam_c02_party` is completed, the map can show Hoàng/Minh’s house.

---

# 18. Temporary Lock Example

During a serious route moment, force the player to go to Hoàng’s house.

```python
"hoang_conflict_night": {
    "background": "images/maps/city_map_01_night.png",
    "title": "Night",
    "show_locked_fixed_locations": True,
    "temporarily_locked_locations": {
        "tam_apartment": "Tâm is not ready to go home yet.",
        "foodie_street": "Not the right mood.",
        "park": "Too late to wander around.",
        "company": "Office is closed.",
        "airport": "No reason to go there.",
    },
    "force_only_locations": [
        "hoang_house",
    ],
}
```

Chapter usage:

```renpy
label hoang_conflict_map:

    $ map_entries = [
        {
            "id": "hoang_conflict_house",
            "location_id": "hoang_house",
            "title": "Go to Hoàng's house",
            "kind": "main",
            "target_label": "hoang_conflict_house_scene",
        },
        {
            "id": "hoang_conflict_park_locked",
            "location_id": "park",
            "title": "Walk around the park",
            "kind": "extra",
            "target_label": "unused",
        },
    ]

    call interactive_map(map_entries, context_id="hoang_conflict_night", allow_back=False)
```

---

# 19. Temporary Location Example

Festival finale with a temporary side corridor.

```renpy
label festival_finale_map:

    $ map_entries = [
        {
            "id": "festival_main_hall",
            "location_id": "conference_hall",
            "title": "Return to the main hall",
            "kind": "main",
            "target_label": "festival_return_main_hall",
        },
        {
            "id": "festival_private_corridor",
            "name": "Private Corridor",
            "x": 1160,
            "y": 470,
            "kind": "temporary",
            "target_label": "festival_private_corridor_scene",
            "conditions": ["flag:knows_private_corridor"],
        },
        {
            "id": "festival_service_exit",
            "name": "Service Exit",
            "x": 1080,
            "y": 520,
            "kind": "temporary",
            "target_label": "festival_service_exit_scene",
            "conditions": ["flag:security_route_known"],
        },
    ]

    call interactive_map(map_entries, context_id="festival_finale", allow_back=False)
```

---

# 20. Optional: Auto-generate Entries from CHAPTERS

Later, chapters can include map metadata directly.

Example in `CHAPTERS`:

```python
"tam_c02_party": {
    "id": "tam_c02_party",
    "route": "tam",
    "type": "core",
    "timeline_position": 20,
    "title": "Company Party",
    "label": "tam_c02_party",
    "location_id": "company",
    "map_kind": "main",
    "prerequisites": ["tam_c01"],
    "unlocks": ["tam_c03", "hoang_h01"],
}
```

Helper:

```renpy
init python:

    def build_available_chapter_map_entries(route_id=None):
        entries = []

        for chapter_id, chapter in CHAPTERS.items():

            if route_id and chapter.get("route") != route_id:
                continue

            if not chapter.get("location_id"):
                continue

            if not chapter_is_available_for_map(chapter_id):
                continue

            entries.append({
                "id": "chapter_map_" + chapter_id,
                "location_id": chapter["location_id"],
                "title": chapter.get("title", chapter_id),
                "kind": chapter.get("map_kind", chapter.get("type", "extra")),
                "target_chapter_id": chapter_id,
            })

        return entries
```

This allows the map to work like a location-based route map.

Useful for later open-ended route screens.

---

# 21. Recommended UX Rules

## 21.1 Main story must be obvious

Main events should be visually distinct.

Do not make the player guess where to continue the story.

Recommended:

```text
Main event marker: large / glowing
Bonus marker: smaller
Locked marker: gray
Temporary marker: special shape
```

---

## 21.2 Do not overload the map

A single map screen should ideally show:

```text
1–2 main events
1–3 character/bonus events
0–2 temporary events
```

Too many markers will make the game feel like a task board.

This story needs atmosphere, not a municipal service portal.

---

## 21.3 Use temporary locks for pacing

During emotionally sensitive scenes, lock irrelevant locations.

Examples:

```text
Breakup scene     → only airport / house / private location
Finale crisis     → only conference hall / corridor / exit route
Confession night  → only park / house / apartment
```

---

## 21.4 Keep fixed locations stable

Do not move fixed locations after they are introduced.

Players build spatial memory.

If Tâm’s apartment is top-left once, it should remain top-left forever.

---

# 22. Debug Coordinate Overlay

Create a debug screen to tune positions.

```renpy
screen map_debug_grid():

    add "images/maps/city_map_01_day.png"

    for x in range(0, 1921, 100):
        add Solid("#ffffff33"):
            xpos x
            ypos 0
            xysize (1, 1080)

        text str(x):
            xpos x + 4
            ypos 4
            size 16

    for y in range(0, 1081, 100):
        add Solid("#ffffff33"):
            xpos 0
            ypos y
            xysize (1920, 1)

        text str(y):
            xpos 4
            ypos y + 4
            size 16

    for loc_id, loc in FIXED_MAP_LOCATIONS.items():
        text "●":
            xpos loc["x"]
            ypos loc["y"]
            anchor (0.5, 0.5)
            size 36
            color "#ffdd66"

        text loc_id:
            xpos loc["x"] + 16
            ypos loc["y"] - 10
            size 18
            color "#ffffff"
```

Add debug label:

```renpy
label debug_map_grid:
    call screen map_debug_grid
    return
```

Use this to adjust fixed coordinates.

---

# 23. Save / Persistence Notes

Fixed location unlocks can be derived from completed chapters, so they do not need separate persistent storage unless needed.

Recommended:

```text
Use completed chapters and flags as source of truth.
Avoid storing duplicate unlocked location state unless necessary.
```

Only store explicit map state if:

* a location can be manually discovered outside chapter completion
* a temporary location becomes permanently known
* a location has custom visited/unvisited state

Example:

```renpy
default discovered_locations = []
default visited_locations = []
```

Helper:

```renpy
init python:

    def discover_location(location_id):
        add_unique(discovered_locations, location_id)

    def mark_location_visited(location_id):
        add_unique(visited_locations, location_id)
```

---

# 24. Error Handling

The system should fail softly.

If a map entry has no target:

```renpy
"This location has no valid story target."
```

If a chapter id does not exist:

```renpy
"Invalid chapter target."
```

If a location id does not exist:

```renpy
"Unknown map location."
```

For production, replace these with `renpy.notify()` or debug logs.

---

# 25. Implementation Checklist

## Data

* [ ] Add `game/map_data.rpy`
* [ ] Define `FIXED_MAP_LOCATIONS`
* [ ] Define `MAP_CONTEXTS`
* [ ] Add initial coordinates for all fixed locations
* [ ] Add map background asset

## Logic

* [ ] Add `game/map_logic.rpy`
* [ ] Implement `map_condition_is_met()`
* [ ] Implement `fixed_location_is_unlocked()`
* [ ] Implement `resolve_map_entry()`
* [ ] Implement `map_entry_is_available()`
* [ ] Implement `build_map_entries()`
* [ ] Implement `resolve_map_target_label()`

## UI

* [ ] Add `game/map_screen.rpy`
* [ ] Implement `interactive_map_screen`
* [ ] Implement hover panel
* [ ] Add marker assets or temporary text markers
* [ ] Add locked marker behavior

## Flow

* [ ] Add `game/map_hub.rpy`
* [ ] Implement `label interactive_map(...)`
* [ ] Add example chapter call
* [ ] Test jump to direct `target_label`
* [ ] Test jump to `target_chapter_id`
* [ ] Test returning after `complete_chapter()`

## Debug

* [ ] Add `screen map_debug_grid`
* [ ] Tune coordinates
* [ ] Test fixed location unlock
* [ ] Test temporary location
* [ ] Test temporary lock
* [ ] Test force-only route behavior
* [ ] Run Ren’Py lint

---

# 26. Final Architecture Summary

```text
CHAPTERS / progression_data
        ↓
chapter label creates map_entries
        ↓
call interactive_map(map_entries, context_id)
        ↓
build_map_entries()
        ↓
interactive_map_screen
        ↓
player clicks location
        ↓
resolve target_label / target_chapter_id
        ↓
jump target label
        ↓
target label plays story
        ↓
complete_chapter()
        ↓
story_hub / route_map / next map
```

The map should feel like the player is choosing where to go.

The code should still behave like the story is choosing what is allowed.

That is the correct balance.
