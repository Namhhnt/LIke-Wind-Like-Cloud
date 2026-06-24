# Technical Implementation Document

## Dynamic Original Stories, Investment Points, Daily Check-in, Minigame Rewards, and API Chapter Updates

## 1. Objective

Implement a **dynamic Library / Original Stories system** for the Ren’Py visual novel project.

The system must support:

1. Local read-only story chapters loaded from `game/stories/`.
2. Downloaded / updated chapters from API.
3. Unlocking bonus, extra, side-story, after-story, and downloaded chapters using **Investment Points**.
4. Earning Investment Points through:

   * main story progression,
   * minigames,
   * daily check-in.
5. Keeping core storyline progression separate from point-based unlocks.

Core story chapters must remain progression-based. Investment Points should only unlock optional or updated content.

---

# 2. Design Principle

## 2.1 Core Chapters

Core chapters are unlocked only by story progression.

Example:

```text
Complete Chapter A
→ unlock Chapter B
→ unlock related route / POV / event
```

Core chapters must never require Investment Points.

## 2.2 Bonus / Extra / Downloaded Chapters

Optional chapters use a hybrid gate:

```text
Required story condition + Investment Points
```

Example:

```text
Yuuka After Story 03
Requires:
- completed yuuka_c10
- completed yuuka_after_002
- 5 Investment Points
```

This prevents spoilers and keeps story order clean.

---

# 3. Terminology

| Term               | Meaning                                                               |
| ------------------ | --------------------------------------------------------------------- |
| Core Chapter       | Main storyline chapter. Unlocked by progression only.                 |
| POV Chapter        | Important alternate point-of-view chapter. Usually progression-based. |
| Bonus Chapter      | Optional content with possible minor gameplay/story effects.          |
| Extra Chapter      | Optional read-only side content.                                      |
| Original Story     | Read-only prose-style chapter rendered inside the game.               |
| Downloaded Chapter | Chapter fetched from API/CDN and cached locally.                      |
| Investment Points  | Currency used to unlock optional content.                             |
| Small Chapter      | Short optional content. Cost: 1 point.                                |
| Medium Chapter     | Normal side content. Cost: 2–3 points.                                |
| Large Chapter      | Long after-story / major extra. Cost: 5 points.                       |

---

# 4. Directory Structure

Recommended structure:

```text
game/
  stories/
    manifest.json

    yuuka/
      001_return_to_tokyo.md
      002_old_boarding_house.md

    minh/
      001_childhood.txt

    tam/
      001_interview_memory.md

  downloaded_stories/
    manifest_cache.json
    yuuka_after_001.md
    yuuka_after_002.md

  scripts/
    story_library.rpy
    story_parser.rpy
    story_player.rpy
    investment_points.rpy
    daily_checkin.rpy
    vn_api_client.rpy
```

For PC builds, `downloaded_stories/` can be placed in a writable persistent directory instead of inside `game/`.

Recommended runtime cache location:

```python
renpy.config.savedir + "/downloaded_stories/"
```

---

# 5. Story File Format

The story files should use a Ren’Py-like read-only syntax.

They are **not real Ren’Py scripts**.
They are parsed as data and rendered by a generic story player.

## 5.1 Example `.md` Story File

```md
---
id: yuuka_after_001
title: A Morning in Tokyo
series: Yuuka After Story
type: extra
size: large
order: 10
cover: images/library/yuuka_tokyo.png
point_cost: 5
prerequisites:
  - yuuka_c10
tags:
  - Yuuka
  - After Story
---

scene bg_tokyo_morning
music bgm_soft_morning

narrator: Yuuka opened the window before the kettle finished boiling.

yuuka neutral: "It is colder than I thought."

pause 0.5

narrator: The cup on the table was still warm. She touched it once, then pulled her hand back.

yuuka soft: "You would have told me not to drink cold water."
```

## 5.2 Supported Commands

Initial supported command set:

```text
scene <background_id>
show <character_id> <expression> [at left|center|right]
hide <character_id>
music <bgm_id>
sfx <sfx_id>
pause <seconds>
narrator: <text>
<character_id> <expression>: <dialogue>
```

Optional later commands:

```text
cg <cg_id>
unlock_cg <cg_id>
unlock_profile <profile_id>
choice_hint <text>
```

Do not support arbitrary Python or Ren’Py code inside story files.

---

# 6. Manifest Format

## 6.1 Local Manifest

`game/stories/manifest.json`

```json
{
  "version": 1,
  "stories": [
    {
      "id": "yuuka_after_001",
      "title": "A Morning in Tokyo",
      "series": "Yuuka After Story",
      "type": "extra",
      "size": "large",
      "source": "local",
      "file": "stories/yuuka/001_return_to_tokyo.md",
      "order": 10,
      "point_cost": 5,
      "unlock_mode": "points",
      "prerequisites": ["yuuka_c10"],
      "tags": ["Yuuka", "After Story"],
      "cover": "images/library/yuuka_tokyo.png"
    }
  ]
}
```

## 6.2 Fallback Auto Scan

If `manifest.json` is missing or invalid:

1. Scan `game/stories/`.
2. Load `.txt` and `.md` files.
3. Parse frontmatter.
4. Register valid stories.
5. Skip invalid files silently and log warnings.

---

# 7. API Endpoints

Base URL should be configurable.

```python
VN_API_BASE_URL = "https://m3noa.site/api/vn"
```

## 7.1 List All Available Chapters

```text
GET https://m3noa.site/api/vn/chapters/
```

Supports pagination.

Query params:

```text
?page=1&page_size=20
```

Optional filters:

```text
?type=extra
?series=yuuka
?updated_after=2026-06-01T00:00:00Z
```

Response example:

```json
{
  "page": 1,
  "page_size": 20,
  "total": 120,
  "has_next": true,
  "next_page": 2,
  "chapters": [
    {
      "id": "yuuka_after_001",
      "title": "A Morning in Tokyo",
      "series": "Yuuka After Story",
      "type": "extra",
      "size": "large",
      "version": 1,
      "source": "remote",
      "file_url": "https://m3noa.site/media/vn/stories/yuuka_after_001.md",
      "hash": "sha256:abc123",
      "point_cost": 5,
      "unlock_mode": "points",
      "prerequisites": ["yuuka_c10"],
      "tags": ["Yuuka", "After Story"],
      "cover_url": "https://m3noa.site/media/vn/covers/yuuka_after_001.png",
      "updated_at": "2026-06-24T00:00:00Z"
    }
  ]
}
```

---

## 7.2 List New / Updated Chapters Only

```text
GET https://m3noa.site/api/vn/chapters/update
```

Recommended query params:

```text
?client_version=1.0.0
?last_sync_at=2026-06-20T00:00:00Z
?installed_ids=yuuka_after_001,minh_extra_002
```

Response:

```json
{
  "server_time": "2026-06-24T06:00:00Z",
  "has_updates": true,
  "chapters": [
    {
      "id": "yuuka_after_002",
      "title": "The Unsent Message",
      "series": "Yuuka After Story",
      "type": "extra",
      "size": "medium",
      "version": 1,
      "file_url": "https://m3noa.site/media/vn/stories/yuuka_after_002.md",
      "hash": "sha256:def456",
      "point_cost": 3,
      "unlock_mode": "points",
      "prerequisites": ["yuuka_after_001"],
      "updated_at": "2026-06-24T00:00:00Z"
    }
  ]
}
```

---

## 7.3 Status / Metadata Check

```text
GET https://m3noa.site/api/vn/status
```

This endpoint must not download chapter files.

Response:

```json
{
  "server_time": "2026-06-24T06:00:00Z",
  "api_version": 1,
  "latest_content_version": 7,
  "minimum_game_version": "1.0.0",
  "message": "New after-story chapters are available.",
  "has_updates": true,
  "maintenance": false
}
```

Use this endpoint for:

```text
- checking server availability
- checking whether new content exists
- retrieving server time for daily check-in validation
- showing update notification in Library
```

---

# 8. Local Data Model

## 8.1 Persistent Data

```renpy
default persistent.investment_points = 0
default persistent.spent_investment_points = 0

default persistent.unlocked_library_content = []
default persistent.read_library_content = []

default persistent.claimed_rewards = []

default persistent.last_daily_checkin_date = None
default persistent.last_daily_checkin_timestamp = None
default persistent.daily_checkin_streak = 0

default persistent.last_chapter_sync_at = None
default persistent.installed_remote_chapters = {}
```

Use lists instead of sets for persistent compatibility.

Example:

```python
persistent.unlocked_library_content = [
    "yuuka_after_001",
    "minh_extra_002"
]
```

## 8.2 Installed Remote Chapter Cache

```python
persistent.installed_remote_chapters = {
    "yuuka_after_001": {
        "id": "yuuka_after_001",
        "version": 1,
        "hash": "sha256:abc123",
        "local_file": "/path/to/downloaded_stories/yuuka_after_001.md",
        "installed_at": "2026-06-24T06:10:00Z"
    }
}
```

---

# 9. Point Economy

## 9.1 Chapter Costs

```python
CHAPTER_POINT_COSTS = {
    "small": 1,
    "medium": 3,
    "large": 5,
    "special": 10
}
```

Recommended values:

| Size    | Cost |
| ------- | ---: |
| small   |    1 |
| medium  |  2–3 |
| large   |    5 |
| special | 8–10 |

## 9.2 Story Progression Rewards

One-time only.

```python
STORY_REWARDS = {
    "core_chapter_first_clear": 2,
    "pov_chapter_first_clear": 1,
    "route_milestone": 3,
    "ending_clear": 5
}
```

## 9.3 Minigame Rewards

Minigames should support grind, but with a daily cap.

```python
MINIGAME_REWARDS = {
    "first_clear": 3,
    "rank_b_first_time": 1,
    "rank_a_first_time": 2,
    "rank_s_first_time": 3,
    "repeat_clear": 1
}
```

Recommended daily cap:

```python
MINIGAME_DAILY_POINT_CAP = 15
```

After reaching daily cap, minigames can still be played but should not grant more points.

## 9.4 Daily Check-in Reward

```python
DAILY_CHECKIN_REWARD = 5
```

This should be enough for:

```text
5 small chapters
2 medium chapters
1 large chapter
```

---

# 10. Investment Point Functions

Create `game/investment_points.rpy`.

```renpy
init python:

    INVESTMENT_POINT_LABEL = "Investment Points"

    def ensure_investment_defaults():
        if persistent.investment_points is None:
            persistent.investment_points = 0
        if persistent.spent_investment_points is None:
            persistent.spent_investment_points = 0
        if persistent.claimed_rewards is None:
            persistent.claimed_rewards = []
        if persistent.unlocked_library_content is None:
            persistent.unlocked_library_content = []

    def add_investment_points(amount, reason=None, reward_id=None):
        ensure_investment_defaults()

        if amount <= 0:
            return False

        if reward_id:
            if reward_id in persistent.claimed_rewards:
                return False
            persistent.claimed_rewards.append(reward_id)

        persistent.investment_points += amount
        renpy.save_persistent()

        return True

    def spend_investment_points(amount):
        ensure_investment_defaults()

        if amount <= 0:
            return True

        if persistent.investment_points < amount:
            return False

        persistent.investment_points -= amount
        persistent.spent_investment_points += amount
        renpy.save_persistent()

        return True

    def has_investment_points(amount):
        ensure_investment_defaults()
        return persistent.investment_points >= amount
```

---

# 11. Daily Check-in

Create `game/daily_checkin.rpy`.

## 11.1 Simple Offline Version

```renpy
init python:
    import datetime

    DAILY_CHECKIN_REWARD = 5

    def get_local_date_string():
        return datetime.date.today().isoformat()

    def claim_daily_checkin():
        ensure_investment_defaults()

        today = get_local_date_string()

        if persistent.last_daily_checkin_date == today:
            return False, "already_claimed"

        persistent.last_daily_checkin_date = today
        persistent.last_daily_checkin_timestamp = datetime.datetime.now().isoformat()

        add_investment_points(
            DAILY_CHECKIN_REWARD,
            reason="daily_checkin",
            reward_id="daily_checkin_" + today
        )

        renpy.save_persistent()
        return True, "claimed"
```

## 11.2 Anti-Clock-Abuse Basic Rule

If the local date goes backward compared to the last claim date, block claim temporarily.

```renpy
init python:

    def can_claim_daily_checkin():
        today = get_local_date_string()
        last = persistent.last_daily_checkin_date

        if not last:
            return True, "available"

        if today == last:
            return False, "already_claimed"

        if today < last:
            return False, "system_date_invalid"

        return True, "available"
```

## 11.3 Recommended UI Behavior

On main menu or Library entry:

```text
Daily Check-in available
→ Show small modal
→ Player clicks Claim
→ +5 Investment Points
```

Do not auto-claim silently. Let the player feel the reward.

---

# 12. Minigame Reward System

Create generic reward function:

```renpy
init python:

    MINIGAME_DAILY_POINT_CAP = 15

    def get_minigame_daily_key():
        return "minigame_points_" + get_local_date_string()

    def get_daily_minigame_points_earned():
        key = get_minigame_daily_key()

        if not hasattr(persistent, "daily_minigame_points"):
            persistent.daily_minigame_points = {}

        return persistent.daily_minigame_points.get(key, 0)

    def add_minigame_points(amount, reward_id=None):
        ensure_investment_defaults()

        if not hasattr(persistent, "daily_minigame_points"):
            persistent.daily_minigame_points = {}

        key = get_minigame_daily_key()
        earned_today = persistent.daily_minigame_points.get(key, 0)

        remaining = MINIGAME_DAILY_POINT_CAP - earned_today

        if remaining <= 0:
            return False, "daily_cap_reached"

        final_amount = min(amount, remaining)

        if reward_id and reward_id in persistent.claimed_rewards:
            return False, "already_claimed"

        if reward_id:
            persistent.claimed_rewards.append(reward_id)

        persistent.daily_minigame_points[key] = earned_today + final_amount
        persistent.investment_points += final_amount

        renpy.save_persistent()
        return True, "claimed"
```

Example usage after minigame:

```renpy
$ result, reason = add_minigame_points(1, reward_id=None)
```

For first-time rank reward:

```renpy
$ add_minigame_points(3, reward_id="tam_speech_rank_s_first")
```

---

# 13. Library Unlock Logic

Create `game/story_library.rpy`.

```renpy
init python:

    library_items = {}

    def register_library_item(item):
        if not item or "id" not in item:
            return False

        library_items[item["id"]] = item
        return True

    def get_library_item(content_id):
        return library_items.get(content_id)

    def is_library_content_unlocked(content_id):
        ensure_investment_defaults()

        item = get_library_item(content_id)

        if not item:
            return False

        if item.get("unlock_mode") in [None, "free"]:
            return prerequisites_met(item)

        if content_id in persistent.unlocked_library_content:
            return True

        return False

    def prerequisites_met(item):
        prerequisites = item.get("prerequisites", [])

        for chapter_id in prerequisites:
            if not is_chapter_completed_for_library(chapter_id):
                return False

        return True

    def is_chapter_completed_for_library(chapter_id):
        # Integrate with existing progression system here.
        # Example:
        # return chapter_id in progress["completed_chapters"]
        try:
            return chapter_id in progress.get("completed_chapters", [])
        except Exception:
            return False

    def can_unlock_library_content(content_id):
        item = get_library_item(content_id)

        if not item:
            return False, "not_found"

        if is_library_content_unlocked(content_id):
            return True, "already_unlocked"

        if not prerequisites_met(item):
            return False, "missing_prerequisites"

        cost = item.get("point_cost", 0)

        if cost <= 0:
            return True, "free"

        if not has_investment_points(cost):
            return False, "not_enough_points"

        return True, "can_unlock"

    def unlock_library_content(content_id):
        ensure_investment_defaults()

        item = get_library_item(content_id)

        if not item:
            return False, "not_found"

        ok, reason = can_unlock_library_content(content_id)

        if not ok:
            return False, reason

        if content_id in persistent.unlocked_library_content:
            return True, "already_unlocked"

        cost = item.get("point_cost", 0)

        if cost > 0:
            if not spend_investment_points(cost):
                return False, "not_enough_points"

        persistent.unlocked_library_content.append(content_id)
        renpy.save_persistent()

        return True, "unlocked"
```

---

# 14. Story Parser

Create `game/story_parser.rpy`.

## 14.1 Parsed Event Model

Each story file becomes:

```python
{
    "id": "yuuka_after_001",
    "title": "A Morning in Tokyo",
    "events": [
        {"type": "scene", "bg": "bg_tokyo_morning"},
        {"type": "music", "id": "bgm_soft_morning"},
        {"type": "narrator", "text": "Yuuka opened the window..."},
        {
            "type": "dialogue",
            "character": "yuuka",
            "expression": "neutral",
            "text": "It is colder than I thought."
        },
        {"type": "pause", "seconds": 0.5}
    ]
}
```

## 14.2 Parser Skeleton

```renpy
init python:

    def parse_story_text(raw_text):
        metadata = {}
        body = raw_text

        if raw_text.startswith("---"):
            parts = raw_text.split("---", 2)
            if len(parts) >= 3:
                metadata_text = parts[1]
                body = parts[2]
                metadata = parse_simple_frontmatter(metadata_text)

        events = []

        for raw_line in body.splitlines():
            line = raw_line.strip()

            if not line:
                continue

            if line.startswith("#"):
                continue

            event = parse_story_line(line)

            if event:
                events.append(event)

        return {
            "metadata": metadata,
            "events": events
        }

    def parse_simple_frontmatter(text):
        data = {}
        current_list_key = None

        for raw_line in text.splitlines():
            line = raw_line.rstrip()

            if not line.strip():
                continue

            if line.startswith("  - ") and current_list_key:
                data.setdefault(current_list_key, []).append(line[4:].strip())
                continue

            if ":" in line:
                key, value = line.split(":", 1)
                key = key.strip()
                value = value.strip()

                if value == "":
                    data[key] = []
                    current_list_key = key
                else:
                    data[key] = value
                    current_list_key = None

        return data

    def parse_story_line(line):
        if line.startswith("scene "):
            return {
                "type": "scene",
                "bg": line.replace("scene ", "", 1).strip()
            }

        if line.startswith("show "):
            parts = line.split()
            event = {
                "type": "show",
                "character": parts[1] if len(parts) > 1 else None,
                "expression": parts[2] if len(parts) > 2 else "neutral",
                "position": "center"
            }

            if "at" in parts:
                at_index = parts.index("at")
                if len(parts) > at_index + 1:
                    event["position"] = parts[at_index + 1]

            return event

        if line.startswith("hide "):
            return {
                "type": "hide",
                "character": line.replace("hide ", "", 1).strip()
            }

        if line.startswith("music "):
            return {
                "type": "music",
                "id": line.replace("music ", "", 1).strip()
            }

        if line.startswith("sfx "):
            return {
                "type": "sfx",
                "id": line.replace("sfx ", "", 1).strip()
            }

        if line.startswith("pause "):
            value = line.replace("pause ", "", 1).strip()
            try:
                seconds = float(value)
            except Exception:
                seconds = 0.5

            return {
                "type": "pause",
                "seconds": seconds
            }

        if line.startswith("narrator:"):
            return {
                "type": "narrator",
                "text": line.replace("narrator:", "", 1).strip()
            }

        if ":" in line:
            speaker_part, text = line.split(":", 1)
            speaker_tokens = speaker_part.split()

            character = speaker_tokens[0]
            expression = speaker_tokens[1] if len(speaker_tokens) > 1 else "neutral"

            return {
                "type": "dialogue",
                "character": character,
                "expression": expression,
                "text": text.strip()
            }

        return {
            "type": "narrator",
            "text": line
        }
```

---

# 15. Story Player

Create `game/story_player.rpy`.

The story player should render parsed events one by one.

## 15.1 Basic Label

```renpy
label play_library_story(content_id):

    $ item = get_library_item(content_id)

    if not item:
        "This story could not be found."
        return

    if not is_library_content_unlocked(content_id):
        "This story is locked."
        return

    $ parsed_story = load_and_parse_library_story(item)

    if not parsed_story:
        "This story could not be loaded."
        return

    call screen original_story_player(parsed_story, item)

    $ mark_library_content_read(content_id)

    return
```

## 15.2 Mark as Read

```renpy
init python:

    def mark_library_content_read(content_id):
        if persistent.read_library_content is None:
            persistent.read_library_content = []

        if content_id not in persistent.read_library_content:
            persistent.read_library_content.append(content_id)

        renpy.save_persistent()
```

## 15.3 Screen Behavior

The screen should:

```text
- show title
- show current background
- show current character sprites if available
- show narrator/dialogue text
- support next/back
- support auto-read later if desired
- have no choices
- have no player interaction besides reading/navigation
```

---

# 16. API Client

Create `game/vn_api_client.rpy`.

## 16.1 Basic Config

```renpy
define VN_API_BASE_URL = "https://m3noa.site/api/vn"
```

## 16.2 Status Check

```renpy
init python:

    def api_get_status():
        url = VN_API_BASE_URL + "/status"

        try:
            # Use urllib for compatibility.
            import urllib.request
            import json

            with urllib.request.urlopen(url, timeout=10) as response:
                raw = response.read().decode("utf-8")
                return json.loads(raw)

        except Exception as e:
            renpy.log("API status check failed: %s" % e)
            return None
```

## 16.3 Fetch Updates

```renpy
init python:

    def api_get_chapter_updates():
        import urllib.parse
        import urllib.request
        import json

        params = {}

        if persistent.last_chapter_sync_at:
            params["last_sync_at"] = persistent.last_chapter_sync_at

        query = urllib.parse.urlencode(params)
        url = VN_API_BASE_URL + "/chapters/update"

        if query:
            url += "?" + query

        try:
            with urllib.request.urlopen(url, timeout=15) as response:
                raw = response.read().decode("utf-8")
                return json.loads(raw)

        except Exception as e:
            renpy.log("API chapter update failed: %s" % e)
            return None
```

## 16.4 Download Chapter File

```renpy
init python:

    def download_remote_chapter(chapter_meta):
        import urllib.request
        import os

        file_url = chapter_meta.get("file_url")

        if not file_url:
            return False, "missing_file_url"

        cache_dir = get_downloaded_story_cache_dir()

        if not os.path.exists(cache_dir):
            os.makedirs(cache_dir)

        local_filename = chapter_meta["id"] + ".md"
        local_path = os.path.join(cache_dir, local_filename)

        try:
            urllib.request.urlretrieve(file_url, local_path)

            expected_hash = chapter_meta.get("hash")

            if expected_hash:
                if not verify_file_hash(local_path, expected_hash):
                    try:
                        os.remove(local_path)
                    except Exception:
                        pass
                    return False, "hash_mismatch"

            register_installed_remote_chapter(chapter_meta, local_path)

            return True, local_path

        except Exception as e:
            renpy.log("Download failed: %s" % e)
            return False, "download_failed"
```

## 16.5 Hash Verification

```renpy
init python:

    def verify_file_hash(local_path, expected_hash):
        import hashlib

        if not expected_hash.startswith("sha256:"):
            return False

        expected = expected_hash.replace("sha256:", "", 1)

        h = hashlib.sha256()

        with open(local_path, "rb") as f:
            while True:
                chunk = f.read(8192)

                if not chunk:
                    break

                h.update(chunk)

        actual = h.hexdigest()

        return actual == expected
```

---

# 17. Download Cache Helpers

```renpy
init python:

    def get_downloaded_story_cache_dir():
        import os
        return os.path.join(config.savedir, "downloaded_stories")

    def register_installed_remote_chapter(chapter_meta, local_path):
        import datetime

        if persistent.installed_remote_chapters is None:
            persistent.installed_remote_chapters = {}

        chapter_id = chapter_meta["id"]

        persistent.installed_remote_chapters[chapter_id] = {
            "id": chapter_id,
            "version": chapter_meta.get("version", 1),
            "hash": chapter_meta.get("hash"),
            "local_file": local_path,
            "installed_at": datetime.datetime.utcnow().isoformat()
        }

        item = dict(chapter_meta)
        item["source"] = "downloaded"
        item["file"] = local_path

        register_library_item(item)

        renpy.save_persistent()
```

---

# 18. Sync Flow

Recommended flow:

```text
Player opens Library
→ call /status
→ if has_updates = true
→ show “New stories available”
→ player clicks Update
→ call /chapters/update
→ list updateable chapters
→ download selected/all chapters
→ verify hash
→ cache locally
→ register in Library
```

Do not download automatically on main menu unless explicitly desired.

---

# 19. Library UI Flow

## 19.1 Library Main Screen

Categories:

```text
Character Profiles
Original Stories
CG Gallery
Music Room
Minigames
Extras
```

## 19.2 Original Stories Screen

Each item card should show:

```text
Title
Series
Type / size
Read status
Unlock status
Point cost
Prerequisite status
Update/download status
```

Card states:

| State                 | UI                                   |
| --------------------- | ------------------------------------ |
| Available / Free      | “Read”                               |
| Locked by story       | “Locked” + missing prerequisite hint |
| Locked by points      | “Unlock — 5 Points”                  |
| Not enough points     | “Need 5 Points”                      |
| Remote not downloaded | “Download”                           |
| Downloaded but locked | “Unlock”                             |
| Read                  | “Read Again”                         |

## 19.3 Unlock Confirmation

Before spending points:

```text
Unlock “A Morning in Tokyo”?
Cost: 5 Investment Points
Current balance: 12
Remaining: 7
```

Buttons:

```text
Unlock
Cancel
```

---

# 20. Integration Rules with Existing Progression

Core progression system remains authoritative for core story chapters.

Library content should only read from progression state:

```python
progress["completed_chapters"]
progress["player_flags"]
progress["relationship_directions"]
```

Library content should not directly mutate core progression unless explicitly marked as a bonus chapter with gameplay effects.

For pure Original Stories:

```python
"is_read_only": True
```

Read-only content can safely unlock:

```text
- read status
- CG entry
- profile note
- gallery note
```

But should not:

```text
- complete core chapter
- alter route progression
- alter ending state
```

---

# 21. Safety Rules

## 21.1 Never Execute Remote Script

Remote or local `.md/.txt` must never run as Python or Ren’Py script.

Allowed:

```text
parse → event list → render
```

Forbidden:

```text
eval
exec
renpy.call dynamically from downloaded script
running arbitrary Python
```

## 21.2 Hash Remote Files

Every remote chapter should include:

```json
"hash": "sha256:..."
```

The client must verify the downloaded file before registering it.

## 21.3 Keep Parser Strict

Unknown commands should be ignored or logged, not executed.

```python
renpy.log("Unknown story command: " + line)
```

---

# 22. Suggested Implementation Phases

## Phase 1 — Local Library

Implement:

```text
- local manifest loader
- fallback story scanner
- story parser
- story player
- Library Original Stories screen
```

## Phase 2 — Point Unlock

Implement:

```text
- Investment Points
- unlock logic
- point cost display
- spending confirmation
- story progression one-time rewards
```

## Phase 3 — Minigame Rewards

Implement:

```text
- minigame reward helper
- daily minigame cap
- first-clear rewards
- rank-based one-time rewards
```

## Phase 4 — Daily Check-in

Implement:

```text
- daily +5 points
- claim modal
- already-claimed state
- basic anti-clock-abuse rule
```

## Phase 5 — API Updates

Implement:

```text
- /status
- /chapters/update
- download/cache
- hash verification
- remote manifest registration
```

## Phase 6 — Polish

Implement:

```text
- update notification badge
- read/unread markers
- filter by character / series / type
- search
- downloadable content batch update
```

---

# 23. Acceptance Criteria

The feature is considered complete when:

```text
1. Game can scan local stories from game/stories/.
2. Game can parse .txt/.md story files into read-only story events.
3. Game can display Original Stories inside the Library.
4. Core chapters remain progression-unlocked only.
5. Optional Library content can require Investment Points.
6. Player can earn points from story rewards.
7. Player can earn grindable minigame points with daily cap.
8. Player can claim +5 daily check-in points once per day.
9. Game can call /status without downloading content.
10. Game can call /chapters/update and list new chapters.
11. Game can download chapter files, verify hash, cache locally, and register them.
12. Locked content correctly shows missing prerequisites or missing points.
13. Unlocking content spends points and persists after restart.
14. Read status persists after restart.
15. Invalid story files do not crash the game.
```

---

# 24. Recommended Constants

```renpy
define VN_API_BASE_URL = "https://m3noa.site/api/vn"

define DAILY_CHECKIN_REWARD = 5
define MINIGAME_DAILY_POINT_CAP = 15

define SMALL_CHAPTER_COST = 1
define MEDIUM_CHAPTER_COST = 3
define LARGE_CHAPTER_COST = 5
define SPECIAL_CHAPTER_COST = 10
```

---

# 25. Final Notes for Agent

Implement this as a **data-driven content system**, not as dynamic Ren’Py code execution.

The clean architecture is:

```text
Local files / API metadata
→ manifest registry
→ parser
→ library item model
→ unlock checker
→ read-only story player
```

Keep main route progression separate:

```text
Core story = progression system
Library stories = optional content system
```

This avoids breaking the main game flow while allowing long-term chapter updates after release.
