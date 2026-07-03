# Route Map / Timeline System

## Overview

The route map/timeline is the primary navigation surface in *Tựa Gió, Tựa Mây*. It is the player's hub for selecting and launching story chapters across 8 interwoven character routes. It replaces the standard Ren'Py "save/load/return" menu as the main game-mode navigation.

Two complementary systems share the navigation surface:

- **Timeline Chapter Map** — a horizontally scrollable node-graph per route, showing each chapter as a card with title, status, and detail panel.
- **Interactive Story Map** — an alternate location-based selection UI where players click markers on a city map to enter chapters or trigger location-based interaction menus.

The game boots into the Interactive Story Map via `label start` → `prologue_rain_dream` → ... → `route_map` → `story_hub`.

---

## Architecture

```
game/
  script.rpy                         # Entry point: start → prologue → route_map
  route_map.rpy                      # Labels: route_map, route_map_timeline
  progression_data.rpy               # CHAPTERS dict, ROUTES dict, CHAPTER_ORDER
  progression_logic.rpy              # complete_chapter(), get_chapter_state(), recalculations
  ending_rules.rpy                   # can_get_* ending eligibility helpers
  map_data.rpy                       # FIXED_MAP_LOCATIONS, MAP_CONTEXTS, TEMPORARY_MAP_LOCATIONS
  map_logic_with_interactions.rpy    # Story hub entry building, condition evaluation, label resolution
  map_hub_with_interactions.rpy      # story_hub label, interactive_map label
  map_screen_with_interactions.rpy   # interactive_map_screen, markers, label buttons
  map_location_interactions.rpy      # Location hub menus (rest, cook, socialize, etc.)
  debug_progression.rpy              # Debug screen for state inspection and chapter completion
  screens/
    timeline/
      timeline_map_data.rpy          # TIMELINE_MAP_NODES, TIMELINE_CONNECTIONS, timeline_* helpers
      timeline_map_screen.rpy        # timeline_chapter_map screen
      timeline_map_styles.rpy        # All timeline styles
```

---

## 1. Progression Data Model (game/progression_data.rpy)

### ROUTES dict

8 character routes:

| Route ID | Title | Start Chapter | Default Unlocked |
|----------|-------|---------------|------------------|
| `tam` | Tâm | prologue_rain_dream | Yes |
| `hoang` | Hoàng | hoang_h01_brother_house | No |
| `yuuka` | Yuuka | yuuka_c08_festival_arrival | No |
| `minh` | Minh | fb_minyuu_01_first_frame | No |
| `thienan` | Thiên An | thienan_c21a_minh_possible | No |
| `huyen` | Huyền | huyen_c22_quan_or_hoang | No |
| `work` | Work / Group | work_c10_project_festival_overlap | No |
| `final` | Final | final_c24_last_choices | No |

### CHAPTERS dict

Every playable chapter is a key in `CHAPTERS`. Each chapter object has:

```python
CHAPTERS["tam_c01_interview_day"] = {
    "id": "tam_c01_interview_day",
    "title": "Ngày phỏng vấn",
    "route": "tam",
    "type": "core",                # core | pov | bonus | extra
    "label": "tam_c01_interview_day",  # Ren'Py label to jump to
    "status": "locked",            # locked | available
    "prerequisites": ["prologue_rain_dream"],
    "prerequisites_any": [],
    "unlocks": ["tam_c02_company_party"],
    "excludes": [],
    "exclusion_group": None,       # For mutual-exclusion chapters
    "required_story_relation": [], # e.g. ["still_lovers"]
    "required_directions": {},     # e.g. {"minyuu": ["ex_lover_seed"]}
    "flags_set": ["tam_route_started", "canon_interview_day"],
    "choice_unlocks": [],
    "emotional_effects": {},
    "character_flags_set": {},
    "relationship_directions_set": {},
    "soft_hide_until_any_completed": [],
    "timeline_position": 10,
}
```

36 chapters defined across all routes, ordered by `CHAPTER_ORDER`.

### CHAPTER_ORDER

The global suggested traversal order. Not enforced — chapters are unlocked by progression logic. Used by the debug screen and timeline to present a consistent order.

### CHOICE_DEFINITIONS

Extra unlocks gated behind story flags or relationship directions. Each defines `condition`, `route`, and `display_text`. Checked via `choice_is_available()`.

---

## 2. Progression Engine (game/progression_logic.rpy)

### State model (`progress` dict)

```python
{
    "initialized": False,
    "completed": [...],       # chapter IDs
    "available": [...],       # recalculated each time
    "excluded": [...],        # by exclusion groups
    "hidden": [...],          # not shown to player
    "temporarily_hidden": [],
    "unlocked_map_locations": [...],
    "play_order": [...],
    "recommended_next": [...],
    "route_status": {route_id: "locked"|"available"|"partial"|"completed"},
    "route_focus": {route_id: count},
    "player_flags": [...],
    "character_flags": {track_id: [...]},
    "relationship_directions": {track_id: [...]},
    "emotional_state": {"trust": 0, "distance": 0, ...},
    "unlocked_choices": [...],
    "ending_eligibility": [...],
    "completed_exclusion_groups": [...],
    "validation_issues": [],
}
```

### Key functions

| Function | Purpose |
|----------|---------|
| `initialize_progression()` | Creates `progress` from `make_progress_state()` on first boot, normalizes persistent state, recalculates availability. Called from `script.rpy` at `start`, `after_load`, and `new_game_overwrite`. |
| `complete_chapter(chapter_id)` | The single completion entry point. Marks chapter done, applies flags/unlocks/exclusions/emotional effects, recalculates availability, route status, ending eligibility, recommended next. |
| `get_chapter_state(chapter_id)` | Returns `"completed"` / `"available"` / `"excluded"` / `"hidden"` / `"locked"`. |
| `recalculate_chapter_availability()` | Iterates all chapters, evaluates prerequisites (`all()` for `prerequisites`, `any()` for `prerequisites_any`), checks `required_story_relation`, `required_directions`, and `story_flag_blocked()`. |
| `recalculate_route_status()` | Sets each route to `"locked"` / `"available"` / `"partial"` / `"completed"` based on completed chapters per route. |
| `recalculate_ending_eligibility()` | Evaluates all `can_get_*` helpers from `ending_rules.rpy`. |
| `update_recommended_next()` | Picks the first few available chapters sorted by `timeline_position`, preferring the current route with highest focus. |
| `debug_unlock/complete/reset` | Testing commands: unlock any chapter, complete any chapter, reset all progress. |

### Completion flow

```
complete_chapter(chapter_id)
  → mark completed, remove from available, add to play_order
  → award investment points (if applicable)
  → increment route_focus for the chapter's route
  → apply_flags (set player_flags, character_flags)
  → apply_emotional_effects (modify emotional_state)
  → apply_relationship_directions (add entries to relationship_directions)
  → apply_choice_unlocks (add entries to unlocked_choices)
  → apply_exclusions (hide exclusion-group alternatives)
  → apply_direct_unlocks (add unlocked chapter to available)
  → refresh_unlocked_map_locations (update map)
  → recalculate_chapter_availability()
  → recalculate_route_status()
  → recalculate_ending_eligibility()
  → refresh_validation_state()
  → update_recommended_next()
```

---

## 3. Timeline Chapter Map (game/screens/timeline/)

### Data (timeline_map_data.rpy)

#### TIMELINE_MAP_NODES

Per-route dict. Each node:

```python
{
    "id": "tam_c01_interview_day",     # unique per route
    "chapter_id": "tam_c01_interview_day",  # references CHAPTERS key
    "title": "Ngày phỏng vấn",          # display title
    "code": "C01",                      # short code badge
    "type": "core",                     # core | pov | bonus | extra
    "thumbnail": "images/assets/thumbnails/tam/tam_c01_interview_day.webp",
    "summary": "Tâm và Huyền đi phỏng vấn...",
    "duration": "MVP skeleton",
    "x": 320,                           # pixel position on timeline canvas
    "y": 120,
    "w": 200,                           # node card dimensions
    "h": 200,
}
```

Each route has its own node array. 36 nodes across all 8 routes.

#### TIMELINE_MAP_CONNECTIONS

Lines drawn between nodes. Each connection:
```python
{"from": "prologue_rain_dream", "to": "tam_c01_interview_day", "style": "solid"}
```

#### TIMELINE_MAP_NODE_META

Extended metadata per node, used in the detail panel:
```python
{
    "display_title": "C01 - Ngày phỏng vấn",
    "summary": "...",
    "conditions": [...],
    "stat_modifiers": [...],
}
```

#### Persistent state

```python
persistent.timeline_bookmarks = []  # list of chapter IDs bookmarked by player
```

#### Key helpers (all in timeline_map_data.rpy)

| Helper | Purpose |
|--------|---------|
| `timeline_get_nodes(route_id)` | Returns node list for a route |
| `timeline_get_connections(route_id)` | Returns connection list for a route |
| `timeline_find_node(route_id, node_id)` | Find a node by ID in a route |
| `timeline_find_node_any_route(chapter_id)` | Locate a chapter across all routes |
| `timeline_is_completed(chapter_id)` | Delegates to `progress["completed"]` |
| `timeline_is_available(chapter_id)` | Checks `get_chapter_state() == "available"` |
| `timeline_get_node_state(node)` | Returns `"completed"`/`"current"`/`"locked"`/`"excluded"`/`"hidden"` based on chapter state |
| `timeline_has_runtime_chapter(chapter_id)` | Checks if the Ren'Py label exists via `renpy.has_label()` |
| `timeline_get_first_selectable_node(route_id)` | First available-or-current node for a route |
| `timeline_resolve_route_selection(selected_route, selected_node)` | Picks the best route/node to display on entering the timeline. Falls back to first available route. |
| `timeline_toggle_bookmark(chapter_id)` | Adds/removes from `persistent.timeline_bookmarks` |
| `timeline_get_background_displayable()` | Tries `TIMELINE_MAP_BACKGROUND`, falls back to `TIMELINE_FALLBACK_BACKGROUND` |
| `timeline_get_node_meta(node)` | Look up `TIMELINE_MAP_NODE_META` for detail panel |
| `timeline_get_route_label(route_id)` | Route display name |

### Screen (timeline_map_screen.rpy)

`screen timeline_chapter_map(route_id, selected_node_id)`:

- **Route tabs**: `TIMELINE_ROUTES` rendered as textbuttons along the top. Selecting a route switches `selected_route` and resets `active_node_id` to the first selectable node.
- **Timeline viewport**: Horizontally scrollable, draggable container. Renders all nodes for the current route at their `(x, y)` positions. Each node is a styled button showing title, code badge, type badge (bonus, pov), and a status icon (completed checkmark, current arrow, lock icon).
- **Connections**: Lines drawn between nodes based on connections data, styled as solid or dashed arrows.
- **Detail panel**: Right-side panel (width ~400px) showing selected node's thumbnail, title, summary, type/duration, stat modifiers, prerequisites, and a "Play" button (enabled only when `timeline_get_node_state() == "current"` AND `timeline_has_runtime_chapter()`).
- **Play action**: Returns `("play", chapter_id, route_id, node_id)` → caller handles the jump.
- **Bookmark toggle**: `("bookmark", ...)`.
- **Route change**: `("change_route", ...)`.
- **Preview**: `("preview", ...)` shows summary via `renpy.notify`.

### Entry flow

```
label route_map
  if explicitly targeting a route/node:
    call route_map_timeline(selected_route, selected_node)
  else:
    resolve story map context → call story_hub(context_id)

label route_map_timeline
  initialize_progression()
  resolve route selection
  loop: call_screen "timeline_chapter_map"
    on "play": break and jump to chapter label
    on "bookmark": toggle bookmark and continue
    on "change_route": reselect and continue
    on "preview": notify summary and continue
    on exit/cancel: return
```

---

## 4. Interactive Story Map (game/map_*.rpy)

### Data (map_data.rpy)

#### FIXED_MAP_LOCATIONS

10 persistent location markers on the map canvas:

| ID | Name | Coordinates | Unlock Condition |
|----|------|------------|------------------|
| `tam_apartment` | Tâm's Apartment | (200, 218) | completed:tam_c01_interview_day |
| `huyen_apartment` | Huyền's Apartment | (580, 180) | completed:tam_c01_interview_day |
| `hoang_house` | Hoàng's House | (240, 732) | completed:tam_c02_company_party |
| `park` | Park | (350, 432) | completed:tam_c01_interview_day |
| `library` | Library | (550, 450) | completed:tam_c01_interview_day |
| `foodie_street` | Foodie Street | (720, 280) | completed:tam_c01_interview_day |
| `shopping_area` | Shopping Area | (900, 200) | completed:tam_c01_interview_day |
| `restaurant` | Restaurant | (880, 460) | completed:tam_c02_company_party |
| `company` | Company | (1080, 380) | completed:tam_c02_company_party |
| `airport` | Airport | (1250, 180) | completed:tam_c06_minh_returns |

Each location has:
- `x`, `y` coordinates (1920x1080 canvas)
- `category`: residential, public, commercial, transport
- `icon`: semantic type
- `default_unlocked`: bool
- `unlock_conditions`: list of condition strings
- `description`: flavor text

#### MAP_CONTEXTS

Story contexts grouping related chapters by act/chapter range:
```python
MAP_CONTEXTS["act1_default"] = {
    "title": "Chapter 1 - Act 1",
    "context_chapters": ["prologue_rain_dream", "tam_c01_interview_day", ...],
}
```

#### TEMPORARY_MAP_LOCATIONS

One-off event locations with custom coordinates, shown only when their unlock conditions are met. Disappear after use.

### Logic (map_logic_with_interactions.rpy)

| Function | Purpose |
|----------|---------|
| `map_condition_is_met(condition)` | Evaluates single condition string e.g. `"completed:tam_c01"`, `"flag:opening_unlocked"`, `"direction:tam:tam_minh_commit"` |
| `map_conditions_are_met(conditions)` | ANDs a list of conditions |
| `fixed_location_is_unlocked(location_id)` | Checks default, persistent unlocked set, or conditions |
| `refresh_unlocked_map_locations()` | Re-evaluates all location unlock conditions after chapter completion |
| `build_story_hub_raw_entries()` | Assembles all entries for the current story context by matching chapters to their locations |
| `build_map_entries(raw_entries, context_id)` | Resolves entries into the final list passed to the screen, adding temporary locations and hub markers |
| `resolve_map_target_label(entry)` | Returns the Ren'Py label to jump to for a given map entry |
| `resolve_story_map_context()` | Returns the best context_id for the player's current progress state |

### Screen (map_screen_with_interactions.rpy)

`screen interactive_map_screen(entries, context_id, allow_back, allow_timeline, title_override)`:

- **Full-screen map**: Background image, overlaid with location markers and label buttons.
- **Location markers**: Clickable icons at fixed coordinates. Only unlocked locations are rendered or interactive.
- **Label buttons**: Text labels next to markers showing location name. Clicking returns the entry dict to the caller.
- **Zoom**: Viewport with draggable/scrollable canvas.
- **Legend panel**: Lists all visible locations with clickable list items.
- **Bottom bar**: Back button, Timeline button (jumps to `route_map_timeline`), context title.

### Hub flow (map_hub_with_interactions.rpy)

```
label story_hub(context_id, allow_back):
  → initialize_progression()
  → autosave at map
  → call interactive_map(context_id)

label interactive_map(map_entries, context_id, ...):
  loop:
    build_map_entries()
    if no entries: show empty state; optionally jump to timeline
    call_screen interactive_map_screen()
    handle result:
      if "timeline" action → jump route_map_timeline
      if "location_hub" → call location_interaction_hub(location_id)
      if chapter entry → resolve_map_target_label() → jump to label
      if cancelled/back → return
```

### Location Interactions (map_location_interactions.rpy)

When clicking a fixed location, `location_interaction_hub()` presents contextual actions:

```python
MAP_LOCATION_ACTIONS = {
    "tam_apartment": [
        {"id": "tam_home_rest", "title": "Rest at home", "effects": {...}, ...},
        {"id": "tam_home_cook_meal", ...},
        {"id": "tam_home_housekeeping", ...},
    ],
    "foodie_street": [
        {"id": "foodie_snack_walk", ...},
    ],
    ...
}
```

Each action has:
- `time_cost`, `money_cost`, `requires` (inventory, flags)
- `effects` (modifies energy, stress, mood, skills, story_state)
- `risk` (failure chance)
- `story_effects` (modifies `story_state` variables)
- `messages` (narrative feedback)

---

## 5. Routes vs. Timeline vs. Map — When Each Is Used

| Context | Where goes | What shows |
|---------|-----------|------------|
| **First play** | `label start` → prologue → ... completes chapter | After completion, returns to `route_map` → `story_hub` (Interactive Map) |
| **From Interactive Map** | "View Timeline" button | Jumps to `route_map_timeline` (Timeline Chapter Map) |
| **From Timeline** | "Back" or "Play" | Back → Main Menu. Play → jumps to chapter label. |
| **From debug** | "Open Route Map" button | `Jump("route_map")` → auto-resolves to story hub |
| **From chapter end** | `call route_map` or `jump route_map` | Returns to the story hub or timeline |

---

## 6. Ending Resolution

After completing `final_c24_last_choices`, the chapter calls `ending_resolver` which evaluates the 24 `can_get_*` helpers from `ending_rules.rpy`. These check:

- Relationship scores (`story_state["hoang_tam_trust"] >= 5`)
- Relationship directions (`not story_has_direction("tam", "tam_hoang_commit")`)
- `minh_yuuka_relation` value
- Doom score threshold
- Ending support flags (`story_has_ending_support("e01_canon_true")`)

The resolver picks the first eligible ending and jumps to its label.

---

## 7. Debug screen

`screen debug_progression` (accessed via shift+O → "Progress Debug") exposes:

- Current completion, availability, exclusion state
- Per-route focus and direction summary
- Eligible endings list
- Validation and acceptance status
- Quick-complete buttons for any chapter
- Reset progress button

---

## 8. Design invariants

1. **Timeline does not own story data.** It reads from `CHAPTERS`/`progress` and renders a node graph. Story data lives in `progression_data.rpy`.
2. **Map does not own progression logic.** It reads from `progress` and renders clickable locations. Unlock conditions evaluate against the same system.
3. **`complete_chapter()` is the single completion entry point.** Every chapter label must call it at the end. No side-channel completion.
4. **Autosave triggers at map entry.** The game saves to a dedicated autosave slot (`"_progression_auto"`) before showing the map, so quitting mid-chapter is safe.
5. **Debug commands are additive only.** `debug_complete` and `debug_unlock` add to progress state, used for testing without breaking playthrough integrity.
6. **All 8 routes and 36 chapters are defined in metadata.** Regardless of authored content depth, the timeline/map surfaces know about every chapter. Missing labels fall back to a "Missing label" notification.
