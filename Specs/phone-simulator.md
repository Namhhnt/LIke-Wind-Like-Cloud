# Technical Implementation Document

# Phone Panel + Character Status System

## Project: Like Wind, Like Cloud — Ren’Py Visual Novel

## 1. Purpose

Implement a diegetic in-game **Phone Panel** that allows the player to access unlocked contacts, messages, emails, social posts, and public character status information.

The system should support:

* unlocked character contacts;
* one-to-one chat threads;
* group chat threads;
* mail inbox entries;
* social feed posts and comments;
* unread indicators;
* read tracking;
* optional one-time reply choices;
* story flag / score effects when reading or replying;
* public-facing character status such as job, income, inventory, public notes, and known facts.

This feature must integrate with the existing progression, story flags, relationship directions, Library character profiles, and interactive map systems without replacing them.

The Phone Panel is not a full smartphone simulator. It is a story-facing UI layer used to reveal character texture, optional subtext, side content, and small route-sensitive interactions.

---

## 2. Design Principles

### 2.1 Narrative-first

The Phone Panel should serve the story.

Use it for:

* messages that reveal emotional distance;
* unread or unsent messages;
* subtle post-chapter reactions;
* job offers and official notices;
* relationship follow-ups;
* public/private contrast between social posts and real feelings;
* small keepsakes or inventory items that carry story meaning.

Avoid meaningless filler threads.

Bad usage:

```text
Hoàng: Hi.
Tâm: Hi.
Hoàng: What are you doing?
Tâm: Nothing.
```

Good usage:

```text
Hoàng: Về đến nhà chưa?
Tâm: Rồi.
Hoàng: Tốt rồi.

[Three minutes later]

Hoàng: Lúc nãy anh nói hơi ít.
Hoàng: Không phải vì không muốn nói.
```

### 2.2 Keep hidden scores hidden

Do not expose internal route scores directly to the player.

Do not display:

```text
tam_hoang_interest = 4
hoang_tam_trust = 7
```

Display public-facing status instead:

```text
Relationship Note:
Hoàng seems more comfortable texting Tâm after the company party.
```

### 2.3 Do not duplicate the Route Map

The Phone Panel may unlock optional content, but it must not become a second chapter-selection system.

Core story navigation remains in the Route Map / Interactive Map.

### 2.4 Keep data-driven structure

Phone content must be defined in data dictionaries, not hard-coded inside screens.

Screens should render data.
Logic should resolve conditions and apply effects.
Story files should only call helper functions.

---

## 3. Proposed File Structure

Create these files:

```text
game/
├── phone_state.rpy
├── phone_logic.rpy
├── screens/
│   ├── phone_screen.rpy
│   └── phone_subscreens.rpy
└── data/
    ├── phone_contacts.rpy
    ├── phone_threads.rpy
    ├── phone_mail.rpy
    ├── phone_social.rpy
    └── character_status_data.rpy
```

Optional later:

```text
game/gui/phone/
├── frame_phone.png
├── icon_messages.png
├── icon_mail.png
├── icon_social.png
├── icon_contacts.png
└── avatars/
    ├── tam.png
    ├── hoang.png
    ├── huyen.png
    ├── minh.png
    ├── yuuka.png
    └── thienan.png
```

Do not place all implementation inside `game/screens.rpy`.
Only add a small entry point to the quick menu or navigation there if needed.

---

## 4. State Model

Create `game/phone_state.rpy`.

```renpy
# FILE: game/phone_state.rpy
# Runtime state for the in-game phone and public character status.

default phone_state = {
    "unlocked_contacts": [],
    "unlocked_threads": [],
    "read_threads": [],
    "unread_threads": [],
    "read_messages": [],
    "sent_replies": {},
    "unlocked_mails": [],
    "read_mails": [],
    "unlocked_posts": [],
    "read_posts": [],
    "liked_posts": [],
    "notification_log": [],
}

default character_status = {
    "tam": {
        "job_title": None,
        "job_level": 0,
        "salary": None,
        "income_monthly": None,
        "inventory": [],
        "known_info": [],
        "public_stats": {},
    },
    "hoang": {
        "job_title": None,
        "job_level": 0,
        "salary": None,
        "income_monthly": None,
        "inventory": [],
        "known_info": [],
        "public_stats": {},
    },
    "huyen": {
        "job_title": None,
        "job_level": 0,
        "salary": None,
        "income_monthly": None,
        "inventory": [],
        "known_info": [],
        "public_stats": {},
    },
    "minh": {
        "job_title": None,
        "job_level": 0,
        "salary": None,
        "income_monthly": None,
        "inventory": [],
        "known_info": [],
        "public_stats": {},
    },
    "yuuka": {
        "job_title": None,
        "job_level": 0,
        "salary": None,
        "income_monthly": None,
        "inventory": [],
        "known_info": [],
        "public_stats": {},
    },
    "thienan": {
        "job_title": None,
        "job_level": 0,
        "salary": None,
        "income_monthly": None,
        "inventory": [],
        "known_info": [],
        "public_stats": {},
    },
}
```

### Notes

* `phone_state` is player-progress runtime state.
* `character_status` is public-facing character state.
* Do not store route-critical hidden scores here.
* Use existing `story_state` for ending-critical values.
* Use `character_status` only for visible or semi-visible information.

---

## 5. Static Data Model

## 5.1 Contacts

Create `game/data/phone_contacts.rpy`.

```renpy
# FILE: game/data/phone_contacts.rpy

define PHONE_CONTACTS = {
    "tam": {
        "id": "tam",
        "name": "Tâm",
        "display_name": "Tâm",
        "avatar": "gui/phone/avatars/tam.png",
        "profile_id": "tam",
        "unlock_conditions": ["completed:tam_c01_interview_day"],
        "tags": ["main", "friend", "work"],
        "default_status": "Available",
    },

    "hoang": {
        "id": "hoang",
        "name": "Hoàng",
        "display_name": "Hoàng",
        "avatar": "gui/phone/avatars/hoang.png",
        "profile_id": "hoang",
        "unlock_conditions": ["flag:hoang_contact_unlocked"],
        "tags": ["architect", "friend"],
        "default_status": "Usually replies late, but not carelessly.",
    },

    "huyen": {
        "id": "huyen",
        "name": "Huyền",
        "display_name": "Huyền",
        "avatar": "gui/phone/avatars/huyen.png",
        "profile_id": "huyen",
        "unlock_conditions": ["completed:tam_c01_interview_day"],
        "tags": ["friend", "work"],
        "default_status": "Online more often than she admits.",
    },
}
```

---

## 5.2 Chat Threads

Create `game/data/phone_threads.rpy`.

```renpy
# FILE: game/data/phone_threads.rpy

define PHONE_THREADS = {
    "tam_hoang_after_party_01": {
        "id": "tam_hoang_after_party_01",
        "type": "chat",
        "contact_id": "hoang",
        "title": "Hoàng",
        "unlock_conditions": ["flag:tam_c02_meaningful_contact"],
        "sort_order": 100,
        "messages": [
            {
                "id": "m01",
                "sender": "hoang",
                "text": "Về đến nhà chưa?",
                "time": "22:48",
            },
            {
                "id": "m02",
                "sender": "player",
                "text": "Rồi. Anh cũng về rồi chứ?",
                "time": "22:49",
            },
            {
                "id": "m03",
                "sender": "hoang",
                "text": "Ừ. Nhưng cà vạt vẫn chưa sống sót.",
                "time": "22:50",
            },
        ],
        "effects_on_read": {
            "flags": ["read_hoang_after_party_message"],
        },
    },

    "group_company_party_recap": {
        "id": "group_company_party_recap",
        "type": "group_chat",
        "contact_id": None,
        "title": "After Party",
        "participants": ["tam", "huyen", "hoang"],
        "unlock_conditions": ["completed:tam_c02_company_party"],
        "sort_order": 90,
        "messages": [
            {
                "id": "m01",
                "sender": "huyen",
                "text": "Tôi xin phép tuyên bố: giày cao gót là hình thức tra tấn hợp pháp.",
                "time": "23:16",
            },
            {
                "id": "m02",
                "sender": "tam",
                "text": "Cậu nói thế sau khi đứng cả tối thật à?",
                "time": "23:17",
            },
            {
                "id": "m03",
                "sender": "huyen",
                "text": "Tôi nói sau khi sống sót.",
                "time": "23:17",
            },
        ],
        "effects_on_read": {},
    },
}
```

---

## 5.3 Reply Choices

Optional for Phase 4.

```renpy
define PHONE_REPLY_CHOICES = {
    "tam_hoang_after_party_01": [
        {
            "id": "ask_if_ok",
            "text": "Anh ổn chứ?",
            "once": True,
            "effects": {
                "story_add": {"hoang_tam_trust": 1},
                "flags": ["tam_asked_hoang_if_ok_after_party"],
            },
            "response_messages": [
                {
                    "id": "r01",
                    "sender": "hoang",
                    "text": "Ổn. Chỉ là hơi không quen khi có người hỏi vậy.",
                    "time": "22:54",
                }
            ],
        },
        {
            "id": "tease_necktie",
            "text": "Em nghĩ cà vạt đó đã hy sinh anh dũng.",
            "once": True,
            "effects": {
                "story_add": {"tam_hoang_interest": 1},
                "flags": ["tam_teased_hoang_after_party"],
            },
            "response_messages": [
                {
                    "id": "r01",
                    "sender": "hoang",
                    "text": "Anh sẽ ghi nhận lòng thương tiếc muộn màng này.",
                    "time": "22:54",
                }
            ],
        },
    ],
}
```

Reply choices must be one-time by default.
Do not allow repeatable score farming.

---

## 5.4 Mail

Create `game/data/phone_mail.rpy`.

```renpy
# FILE: game/data/phone_mail.rpy

define PHONE_MAILS = {
    "company_salary_first_month": {
        "id": "company_salary_first_month",
        "from": "HR Department",
        "subject": "Salary Notification",
        "preview": "Your first monthly salary has been processed.",
        "body": "Your first monthly salary has been processed. Please check the attached payroll notice for details.",
        "unlock_conditions": ["flag:tam_huyen_first_job_offer"],
        "sort_order": 100,
        "effects_on_read": {
            "character_status": {
                "tam": {
                    "job_title": "Junior Staff",
                    "job_level": 1,
                    "income_monthly": 1200,
                },
                "huyen": {
                    "job_title": "Junior Staff",
                    "job_level": 1,
                    "income_monthly": 1200,
                },
            },
            "flags": ["read_first_salary_mail"],
        },
    },

    "company_party_invitation": {
        "id": "company_party_invitation",
        "from": "Company Affairs",
        "subject": "Company Gathering Invitation",
        "preview": "You are invited to the upcoming company gathering.",
        "body": "You are invited to the upcoming company gathering. Dress code: semi-formal.",
        "unlock_conditions": ["completed:tam_c01_interview_day"],
        "sort_order": 90,
        "effects_on_read": {},
    },
}
```

---

## 5.5 Social Posts

Create `game/data/phone_social.rpy`.

```renpy
# FILE: game/data/phone_social.rpy

define PHONE_SOCIAL_POSTS = {
    "huyen_party_post_01": {
        "id": "huyen_party_post_01",
        "author": "huyen",
        "content": "Có những buổi tiệc không mệt vì rượu, mà mệt vì phải cười đúng lúc.",
        "image": None,
        "unlock_conditions": ["completed:tam_c02_company_party"],
        "sort_order": 100,
        "comments": [
            {
                "author": "tam",
                "text": "Nghe nguy hiểm vậy.",
            },
            {
                "author": "huyen",
                "text": "Không. Chỉ là giày cao quá thôi.",
            },
        ],
        "effects_on_read": {
            "flags": ["read_huyen_party_post"],
        },
        "effects_on_like": {
            "flags": ["liked_huyen_party_post"],
        },
    },
}
```

---

## 5.6 Character Status Base Data

Create `game/data/character_status_data.rpy`.

```renpy
# FILE: game/data/character_status_data.rpy

define CHARACTER_STATUS_BASE = {
    "tam": {
        "id": "tam",
        "name": "Tâm",
        "profile_id": "tam",
        "public_title": "New Office Staff",
        "default_notes": [
            "Recently passed the interview.",
            "Still adjusting to the company environment.",
        ],
        "hidden_until": [],
    },

    "hoang": {
        "id": "hoang",
        "name": "Hoàng",
        "profile_id": "hoang",
        "public_title": "Architecture Designer",
        "default_notes": [
            "Polite, observant, and more guarded than he first appears.",
        ],
        "hidden_until": ["flag:hoang_contact_unlocked"],
    },
}

define STORY_ITEMS = {
    "tam_first_salary_envelope": {
        "id": "tam_first_salary_envelope",
        "name": "First Salary Envelope",
        "description": "Tâm's first salary. Still unopened for longer than necessary.",
        "type": "keepsake",
        "visible": True,
    },

    "yuuka_old_bookmark": {
        "id": "yuuka_old_bookmark",
        "name": "Folded Bookmark",
        "description": "A bookmark with one corner folded too neatly.",
        "type": "memory",
        "visible": False,
    },
}
```

---

# 6. Condition System

## 6.1 Supported condition formats

Implement a lightweight condition resolver for phone data.

Supported formats:

```text
completed:<chapter_id>
flag:<flag_name>
not_flag:<flag_name>
contact:<contact_id>
thread_read:<thread_id>
mail_read:<mail_id>
post_read:<post_id>
direction:<character>:<direction>
score_gte:<score_key>:<amount>
score_lte:<score_key>:<amount>
```

Examples:

```python
["completed:tam_c02_company_party"]
["flag:tam_c02_meaningful_contact"]
["direction:tam:tam_hoang_open"]
["score_gte:hoang_tam_trust:3"]
```

## 6.2 Implementation

Create `game/phone_logic.rpy`.

```renpy
# FILE: game/phone_logic.rpy

init python:
    def phone_list_get(key):
        return phone_state.setdefault(key, [])

    def phone_dict_get(key):
        return phone_state.setdefault(key, {})

    def phone_has_completed(chapter_id):
        try:
            return chapter_id in story_completed_chapters
        except Exception:
            return False

    def phone_has_flag(flag_name):
        try:
            return story_has_flag(flag_name)
        except Exception:
            try:
                return flag_name in story_flags
            except Exception:
                return False

    def phone_has_direction(character_id, direction):
        # Relationship directions are stored in story flags through story_add_direction.
        flag_name = "direction_%s_%s" % (character_id, direction)
        return phone_has_flag(flag_name)

    def phone_get_score(score_key):
        try:
            return story_state.get(score_key, 0)
        except Exception:
            return 0

    def phone_eval_condition(condition):
        if not condition:
            return True

        parts = condition.split(":")

        if parts[0] == "completed" and len(parts) == 2:
            return phone_has_completed(parts[1])

        if parts[0] == "flag" and len(parts) == 2:
            return phone_has_flag(parts[1])

        if parts[0] == "not_flag" and len(parts) == 2:
            return not phone_has_flag(parts[1])

        if parts[0] == "contact" and len(parts) == 2:
            return phone_has_contact(parts[1])

        if parts[0] == "thread_read" and len(parts) == 2:
            return parts[1] in phone_state.get("read_threads", [])

        if parts[0] == "mail_read" and len(parts) == 2:
            return parts[1] in phone_state.get("read_mails", [])

        if parts[0] == "post_read" and len(parts) == 2:
            return parts[1] in phone_state.get("read_posts", [])

        if parts[0] == "direction" and len(parts) == 3:
            return phone_has_direction(parts[1], parts[2])

        if parts[0] == "score_gte" and len(parts) == 3:
            return phone_get_score(parts[1]) >= int(parts[2])

        if parts[0] == "score_lte" and len(parts) == 3:
            return phone_get_score(parts[1]) <= int(parts[2])

        return False

    def phone_conditions_met(conditions):
        if not conditions:
            return True
        return all(phone_eval_condition(c) for c in conditions)
```

---

# 7. Unlock Logic

## 7.1 Contacts

```renpy
init python:
    def phone_unlock_contact(contact_id):
        if contact_id not in PHONE_CONTACTS:
            return False

        contacts = phone_list_get("unlocked_contacts")
        if contact_id not in contacts:
            contacts.append(contact_id)
            phone_add_notification("contact", contact_id)
        return True

    def phone_has_contact(contact_id):
        return contact_id in phone_state.get("unlocked_contacts", [])

    def phone_refresh_contacts():
        for contact_id, data in PHONE_CONTACTS.items():
            if phone_conditions_met(data.get("unlock_conditions", [])):
                phone_unlock_contact(contact_id)
```

## 7.2 Threads

```renpy
init python:
    def phone_unlock_thread(thread_id, mark_unread=True):
        if thread_id not in PHONE_THREADS:
            return False

        unlocked = phone_list_get("unlocked_threads")
        unread = phone_list_get("unread_threads")

        if thread_id not in unlocked:
            unlocked.append(thread_id)
            phone_add_notification("thread", thread_id)

        if mark_unread and thread_id not in phone_state.get("read_threads", []):
            if thread_id not in unread:
                unread.append(thread_id)

        return True

    def phone_mark_thread_read(thread_id):
        unread = phone_list_get("unread_threads")
        read = phone_list_get("read_threads")

        if thread_id in unread:
            unread.remove(thread_id)

        if thread_id not in read:
            read.append(thread_id)

        data = PHONE_THREADS.get(thread_id)
        if data:
            phone_apply_effects(data.get("effects_on_read", {}))

    def phone_refresh_threads():
        for thread_id, data in PHONE_THREADS.items():
            if phone_conditions_met(data.get("unlock_conditions", [])):
                phone_unlock_thread(thread_id)
```

## 7.3 Mail

```renpy
init python:
    def phone_unlock_mail(mail_id, mark_unread=True):
        if mail_id not in PHONE_MAILS:
            return False

        unlocked = phone_list_get("unlocked_mails")

        if mail_id not in unlocked:
            unlocked.append(mail_id)
            phone_add_notification("mail", mail_id)

        return True

    def phone_mark_mail_read(mail_id):
        read = phone_list_get("read_mails")
        if mail_id not in read:
            read.append(mail_id)

        data = PHONE_MAILS.get(mail_id)
        if data:
            phone_apply_effects(data.get("effects_on_read", {}))

    def phone_refresh_mails():
        for mail_id, data in PHONE_MAILS.items():
            if phone_conditions_met(data.get("unlock_conditions", [])):
                phone_unlock_mail(mail_id)
```

## 7.4 Social Posts

```renpy
init python:
    def phone_unlock_post(post_id):
        if post_id not in PHONE_SOCIAL_POSTS:
            return False

        unlocked = phone_list_get("unlocked_posts")

        if post_id not in unlocked:
            unlocked.append(post_id)
            phone_add_notification("post", post_id)

        return True

    def phone_mark_post_read(post_id):
        read = phone_list_get("read_posts")
        if post_id not in read:
            read.append(post_id)

        data = PHONE_SOCIAL_POSTS.get(post_id)
        if data:
            phone_apply_effects(data.get("effects_on_read", {}))

    def phone_like_post(post_id):
        liked = phone_list_get("liked_posts")
        if post_id not in liked:
            liked.append(post_id)

            data = PHONE_SOCIAL_POSTS.get(post_id)
            if data:
                phone_apply_effects(data.get("effects_on_like", {}))

    def phone_refresh_posts():
        for post_id, data in PHONE_SOCIAL_POSTS.items():
            if phone_conditions_met(data.get("unlock_conditions", [])):
                phone_unlock_post(post_id)
```

## 7.5 Global Refresh

```renpy
init python:
    def phone_refresh_all():
        phone_refresh_contacts()
        phone_refresh_threads()
        phone_refresh_mails()
        phone_refresh_posts()
```

Call this:

* after chapter completion;
* after loading a save;
* after important story flags are set;
* before opening the phone screen.

---

# 8. Effect System

## 8.1 Supported effects

Effects dictionary:

```python
{
    "flags": ["flag_name"],
    "story_add": {"score_key": amount},
    "directions": {"character_id": ["direction_a", "direction_b"]},
    "character_status": {
        "character_id": {
            "job_title": "Junior Staff",
            "job_level": 1,
            "income_monthly": 1200,
        }
    },
    "inventory_add": {
        "character_id": ["item_id"]
    },
    "known_info_add": {
        "character_id": ["note_id_or_text"]
    }
}
```

## 8.2 Implementation

```renpy
init python:
    def phone_apply_effects(effects):
        if not effects:
            return

        for flag_name in effects.get("flags", []):
            try:
                story_flag(flag_name)
            except Exception:
                if flag_name not in story_flags:
                    story_flags.append(flag_name)

        for score_key, amount in effects.get("story_add", {}).items():
            try:
                story_add(score_key, amount)
            except Exception:
                story_state[score_key] = story_state.get(score_key, 0) + amount

        for character_id, directions in effects.get("directions", {}).items():
            for direction in directions:
                try:
                    story_add_direction(character_id, direction)
                except Exception:
                    fallback_flag = "direction_%s_%s" % (character_id, direction)
                    if fallback_flag not in story_flags:
                        story_flags.append(fallback_flag)

        for character_id, status_patch in effects.get("character_status", {}).items():
            phone_update_character_status(character_id, **status_patch)

        for character_id, item_ids in effects.get("inventory_add", {}).items():
            for item_id in item_ids:
                char_add_item(character_id, item_id)

        for character_id, notes in effects.get("known_info_add", {}).items():
            for note in notes:
                char_add_known_info(character_id, note)
```

---

# 9. Character Status Helpers

```renpy
init python:
    def phone_get_character_status(character_id):
        return character_status.setdefault(character_id, {
            "job_title": None,
            "job_level": 0,
            "salary": None,
            "income_monthly": None,
            "inventory": [],
            "known_info": [],
            "public_stats": {},
        })

    def phone_update_character_status(character_id, **kwargs):
        status = phone_get_character_status(character_id)

        for key, value in kwargs.items():
            if key == "public_stats":
                status.setdefault("public_stats", {}).update(value)
            elif key == "known_info":
                for note in value:
                    char_add_known_info(character_id, note)
            elif key == "inventory":
                for item_id in value:
                    char_add_item(character_id, item_id)
            else:
                status[key] = value

    def char_add_item(character_id, item_id):
        status = phone_get_character_status(character_id)
        inv = status.setdefault("inventory", [])
        if item_id not in inv:
            inv.append(item_id)

    def char_has_item(character_id, item_id):
        status = phone_get_character_status(character_id)
        return item_id in status.get("inventory", [])

    def char_add_known_info(character_id, note):
        status = phone_get_character_status(character_id)
        known = status.setdefault("known_info", [])
        if note not in known:
            known.append(note)

    def char_has_known_info(character_id, note):
        status = phone_get_character_status(character_id)
        return note in status.get("known_info", [])
```

---

# 10. Notification Helpers

```renpy
init python:
    def phone_add_notification(kind, target_id):
        log = phone_list_get("notification_log")
        entry = "%s:%s" % (kind, target_id)

        if entry not in log:
            log.append(entry)

    def phone_get_unread_count():
        count = 0
        count += len(phone_state.get("unread_threads", []))

        for mail_id in phone_state.get("unlocked_mails", []):
            if mail_id not in phone_state.get("read_mails", []):
                count += 1

        for post_id in phone_state.get("unlocked_posts", []):
            if post_id not in phone_state.get("read_posts", []):
                count += 1

        return count

    def phone_has_unread():
        return phone_get_unread_count() > 0
```

---

# 11. Screen Implementation

## 11.1 Main Phone Screen

Create `game/screens/phone_screen.rpy`.

```renpy
# FILE: game/screens/phone_screen.rpy

screen phone_home(default_tab="messages"):
    tag menu
    modal True
    zorder 200

    default tab = default_tab

    on "show" action Function(phone_refresh_all)

    add Solid("#00000099")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 760
        ysize 960
        padding (24, 24)

        vbox:
            spacing 16

            hbox:
                xfill True
                text "Phone" style "phone_title"
                null width 20
                text "[phone_get_unread_count()] new" style "phone_small_text" xalign 1.0

            hbox:
                spacing 8
                textbutton "Messages" action SetScreenVariable("tab", "messages") style "phone_tab_button"
                textbutton "Mail" action SetScreenVariable("tab", "mail") style "phone_tab_button"
                textbutton "Social" action SetScreenVariable("tab", "social") style "phone_tab_button"
                textbutton "Contacts" action SetScreenVariable("tab", "contacts") style "phone_tab_button"

            frame:
                xfill True
                yfill True

                if tab == "messages":
                    use phone_messages_tab
                elif tab == "mail":
                    use phone_mail_tab
                elif tab == "social":
                    use phone_social_tab
                elif tab == "contacts":
                    use phone_contacts_tab

            textbutton "Close" action Return() xalign 0.5
```

---

## 11.2 Subscreens

Create `game/screens/phone_subscreens.rpy`.

### Messages Tab

```renpy
screen phone_messages_tab():
    default selected_thread = None

    hbox:
        spacing 12

        viewport:
            xsize 250
            yfill True
            mousewheel True
            draggable True

            vbox:
                spacing 6

                for thread_id in sorted(phone_state.get("unlocked_threads", []), key=lambda tid: PHONE_THREADS.get(tid, {}).get("sort_order", 0), reverse=True):
                    $ thread = PHONE_THREADS.get(thread_id, {})
                    $ title = thread.get("title", thread_id)
                    $ unread = thread_id in phone_state.get("unread_threads", [])

                    textbutton ("● " + title if unread else title):
                        action SetScreenVariable("selected_thread", thread_id)
                        style "phone_list_button"

        frame:
            xfill True
            yfill True

            if selected_thread:
                use phone_thread_view(selected_thread)
            else:
                text "Select a conversation." style "phone_body_text"
```

### Thread View

```renpy
screen phone_thread_view(thread_id):
    $ thread = PHONE_THREADS.get(thread_id, {})

    on "show" action Function(phone_mark_thread_read, thread_id)

    vbox:
        spacing 10

        text thread.get("title", thread_id) style "phone_section_title"

        viewport:
            yfill True
            mousewheel True
            draggable True

            vbox:
                spacing 8

                for message in thread.get("messages", []):
                    use phone_message_bubble(message)

                $ reply_data = PHONE_REPLY_CHOICES.get(thread_id, []) if "PHONE_REPLY_CHOICES" in globals() else []

                for reply in reply_data:
                    $ sent = phone_reply_was_sent(thread_id, reply.get("id"))
                    if not sent:
                        textbutton reply.get("text", "..."):
                            action Function(phone_send_reply, thread_id, reply.get("id"))
                            style "phone_reply_button"
```

### Message Bubble

```renpy
screen phone_message_bubble(message):
    $ sender = message.get("sender", "")
    $ text_value = message.get("text", "")
    $ time_value = message.get("time", "")

    frame:
        xfill True
        padding (10, 8)

        vbox:
            spacing 2
            text sender style "phone_sender_text"
            text text_value style "phone_body_text"
            if time_value:
                text time_value style "phone_time_text"
```

### Mail Tab

```renpy
screen phone_mail_tab():
    default selected_mail = None

    hbox:
        spacing 12

        viewport:
            xsize 280
            yfill True
            mousewheel True
            draggable True

            vbox:
                spacing 6

                for mail_id in sorted(phone_state.get("unlocked_mails", []), key=lambda mid: PHONE_MAILS.get(mid, {}).get("sort_order", 0), reverse=True):
                    $ mail = PHONE_MAILS.get(mail_id, {})
                    $ unread = mail_id not in phone_state.get("read_mails", [])
                    $ subject = mail.get("subject", mail_id)

                    textbutton ("● " + subject if unread else subject):
                        action SetScreenVariable("selected_mail", mail_id)
                        style "phone_list_button"

        frame:
            xfill True
            yfill True

            if selected_mail:
                use phone_mail_view(selected_mail)
            else:
                text "Select an email." style "phone_body_text"
```

### Mail View

```renpy
screen phone_mail_view(mail_id):
    $ mail = PHONE_MAILS.get(mail_id, {})

    on "show" action Function(phone_mark_mail_read, mail_id)

    viewport:
        mousewheel True
        draggable True

        vbox:
            spacing 10
            text mail.get("subject", mail_id) style "phone_section_title"
            text "From: [mail.get('from', 'Unknown')]" style "phone_small_text"
            null height 8
            text mail.get("body", "") style "phone_body_text"
```

### Social Tab

```renpy
screen phone_social_tab():
    viewport:
        mousewheel True
        draggable True

        vbox:
            spacing 16

            for post_id in sorted(phone_state.get("unlocked_posts", []), key=lambda pid: PHONE_SOCIAL_POSTS.get(pid, {}).get("sort_order", 0), reverse=True):
                use phone_social_post(post_id)
```

### Social Post

```renpy
screen phone_social_post(post_id):
    $ post = PHONE_SOCIAL_POSTS.get(post_id, {})

    on "show" action Function(phone_mark_post_read, post_id)

    frame:
        xfill True
        padding (12, 12)

        vbox:
            spacing 8

            text post.get("author", "Unknown") style "phone_sender_text"
            text post.get("content", "") style "phone_body_text"

            if post.get("image"):
                add post.get("image") xmaximum 420 ymaximum 240

            hbox:
                spacing 12
                textbutton "Like" action Function(phone_like_post, post_id) style "phone_small_button"

            for comment in post.get("comments", []):
                text "[comment.get('author', '')]: [comment.get('text', '')]" style "phone_comment_text"
```

### Contacts Tab

```renpy
screen phone_contacts_tab():
    default selected_contact = None

    hbox:
        spacing 12

        viewport:
            xsize 250
            yfill True
            mousewheel True
            draggable True

            vbox:
                spacing 6

                for contact_id in phone_state.get("unlocked_contacts", []):
                    $ contact = PHONE_CONTACTS.get(contact_id, {})
                    textbutton contact.get("display_name", contact_id):
                        action SetScreenVariable("selected_contact", contact_id)
                        style "phone_list_button"

        frame:
            xfill True
            yfill True

            if selected_contact:
                use phone_contact_view(selected_contact)
            else:
                text "Select a contact." style "phone_body_text"
```

### Contact View / Character Status

```renpy
screen phone_contact_view(contact_id):
    $ contact = PHONE_CONTACTS.get(contact_id, {})
    $ status = phone_get_character_status(contact_id)
    $ base = CHARACTER_STATUS_BASE.get(contact_id, {})

    viewport:
        mousewheel True
        draggable True

        vbox:
            spacing 10

            text contact.get("display_name", contact_id) style "phone_section_title"

            if contact.get("avatar"):
                add contact.get("avatar") xmaximum 120 ymaximum 120

            text base.get("public_title", "") style "phone_small_text"

            if status.get("job_title"):
                text "Job: [status.get('job_title')]" style "phone_body_text"

            if status.get("job_level"):
                text "Job Level: [status.get('job_level')]" style "phone_body_text"

            if status.get("income_monthly"):
                text "Monthly Income: [status.get('income_monthly')]" style "phone_body_text"

            if status.get("known_info"):
                text "Known Notes" style "phone_section_title"
                for note in status.get("known_info", []):
                    text "• [note]" style "phone_body_text"

            if status.get("inventory"):
                text "Inventory / Keepsakes" style "phone_section_title"
                for item_id in status.get("inventory", []):
                    $ item = STORY_ITEMS.get(item_id, {})
                    if item.get("visible", True):
                        text "• [item.get('name', item_id)] — [item.get('description', '')]" style "phone_body_text"

            if contact.get("profile_id"):
                textbutton "Open Library Profile":
                    action Function(phone_open_library_profile, contact.get("profile_id"))
                    style "phone_small_button"
```

---

# 12. Reply Logic

```renpy
init python:
    def phone_reply_was_sent(thread_id, reply_id):
        sent = phone_state.setdefault("sent_replies", {})
        return reply_id in sent.get(thread_id, [])

    def phone_send_reply(thread_id, reply_id):
        choices = PHONE_REPLY_CHOICES.get(thread_id, [])
        reply = None

        for item in choices:
            if item.get("id") == reply_id:
                reply = item
                break

        if not reply:
            return

        if reply.get("once", True) and phone_reply_was_sent(thread_id, reply_id):
            return

        sent = phone_state.setdefault("sent_replies", {})
        sent.setdefault(thread_id, []).append(reply_id)

        phone_apply_effects(reply.get("effects", {}))

        # Optional: append response messages to a runtime message list if needed.
        # For MVP, replies can simply disappear after being selected.
        renpy.restart_interaction()
```

For Phase 4, if runtime-appended messages are needed, add:

```python
phone_state["runtime_thread_messages"] = {
    "thread_id": [message_dict, message_dict]
}
```

Then merge static + runtime messages in `phone_get_thread_messages(thread_id)`.

---

# 13. Styles

Create styles in `game/screens/phone_screen.rpy` or a dedicated `game/styles/phone_styles.rpy`.

Use the existing warm beige/brown UI direction.

```renpy
style phone_title:
    size 36
    color "#f3e3c2"
    bold True

style phone_section_title:
    size 26
    color "#f3e3c2"
    bold True

style phone_body_text:
    size 22
    color "#ead8b7"

style phone_small_text:
    size 18
    color "#cdbb9b"

style phone_sender_text:
    size 18
    color "#f3e3c2"
    bold True

style phone_time_text:
    size 14
    color "#a89478"

style phone_comment_text:
    size 18
    color "#d8c4a2"

style phone_tab_button:
    background Solid("#3b2a1eaa")
    hover_background Solid("#5b422fcc")
    padding (12, 8)

style phone_list_button:
    background Solid("#241810aa")
    hover_background Solid("#4a3324cc")
    padding (10, 8)

style phone_reply_button:
    background Solid("#4c3525cc")
    hover_background Solid("#6b4b35dd")
    padding (12, 10)

style phone_small_button:
    background Solid("#3b2a1eaa")
    hover_background Solid("#5b422fcc")
    padding (8, 6)
```

---

# 14. Quick Menu / Navigation Integration

Add a small phone entry point to an existing quick menu or navigation screen.

Example:

```renpy
textbutton "Phone":
    action ShowMenu("phone_home")
```

If showing unread count:

```renpy
$ unread_count = phone_get_unread_count()
textbutton ("Phone [%d]" % unread_count if unread_count else "Phone"):
    action ShowMenu("phone_home")
```

Do not over-edit `game/screens.rpy`.
If possible, add a small include-style block or call a new `phone_quick_button` screen.

```renpy
screen phone_quick_button():
    $ unread_count = phone_get_unread_count()
    textbutton ("Phone [%d]" % unread_count if unread_count else "Phone"):
        action ShowMenu("phone_home")
```

---

# 15. Story Integration Examples

## 15.1 Unlock a contact after a scene

```renpy
label tam_c02_company_party_s04_first_branch:
    # Story content...

    $ phone_unlock_contact("hoang")
    $ story_flag("hoang_contact_unlocked")

    return
```

## 15.2 Unlock a message thread

```renpy
$ phone_unlock_thread("tam_hoang_after_party_01")
```

## 15.3 Unlock mail after salary milestone

```renpy
$ phone_unlock_mail("company_salary_first_month")
$ char_add_item("tam", "tam_first_salary_envelope")
```

## 15.4 Open phone directly from scene

```renpy
$ phone_unlock_thread("tam_hoang_after_party_01")
call screen phone_home(default_tab="messages")
```

Use this sparingly.
Prefer notifications and player-driven opening unless the scene requires the phone.

## 15.5 Check if player read something

```renpy
if "tam_hoang_after_party_01" in phone_state.get("read_threads", []):
    huyen teasing "Cậu đọc tin nhắn rồi chứ gì."
else:
    huyen neutral "Điện thoại cậu im cả tối à?"
```

---

# 16. Map Integration

Phone should be accessible from the interactive map UI.

Recommended behavior:

* show a phone icon on the map;
* show unread badge if `phone_has_unread()` returns true;
* do not force the player into phone content unless a story scene explicitly calls it;
* phone content may unlock after route/chapter completion.

Example map button:

```renpy
use phone_quick_button
```

Or:

```renpy
if phone_has_unread():
    text "New phone activity" style "phone_small_text"
```

---

# 17. Library Profile Integration

The Phone Contact View may link to an existing Library character profile.

Implementation can be simple in MVP:

```renpy
init python:
    def phone_open_library_profile(profile_id):
        # MVP fallback: open library character screen if the project supports direct profile navigation.
        # If no direct API exists, open the character library list.
        renpy.call_screen("library_characters")
```

If the Library has direct profile APIs, use them instead.

Rules:

* Phone Contact View shows short public status.
* Library Profile remains the deeper profile/bio/reference screen.
* Do not duplicate full Library profile text inside the Phone.

---

# 18. Translation Requirements

Any new user-facing strings in `.rpy` screens or story files must be mirrored in translation files if the project requires localization.

Avoid creating many hard-coded source strings inside logic files.

Prefer data strings in data files for phone content.
For future localization, consider moving phone content into structured translation files or using stable IDs.

Important user-facing strings include:

* tab labels;
* button labels;
* empty-state text;
* mail subjects;
* mail body text;
* chat message text;
* social post text;
* reply choice text;
* item descriptions.

---

# 19. Backward Compatibility

Existing saves may not contain `phone_state` or `character_status`.

Add defensive initialization helpers:

```renpy
init python:
    def phone_ensure_state():
        global phone_state
        global character_status

        if phone_state is None:
            phone_state = {}

        defaults = {
            "unlocked_contacts": [],
            "unlocked_threads": [],
            "read_threads": [],
            "unread_threads": [],
            "read_messages": [],
            "sent_replies": {},
            "unlocked_mails": [],
            "read_mails": [],
            "unlocked_posts": [],
            "read_posts": [],
            "liked_posts": [],
            "notification_log": [],
        }

        for key, value in defaults.items():
            phone_state.setdefault(key, value if not isinstance(value, list) else [])

        if character_status is None:
            character_status = {}

        for character_id in ["tam", "hoang", "huyen", "minh", "yuuka", "thienan"]:
            phone_get_character_status(character_id)
```

Call:

```renpy
$ phone_ensure_state()
$ phone_refresh_all()
```

from:

* `after_load` hook if available;
* before opening `phone_home`;
* optionally after progression initialization.

---

# 20. Debug Support

Add a small debug screen or debug functions.

```renpy
init python:
    def phone_debug_unlock_all_contacts():
        for contact_id in PHONE_CONTACTS.keys():
            phone_unlock_contact(contact_id)

    def phone_debug_unlock_all_threads():
        for thread_id in PHONE_THREADS.keys():
            phone_unlock_thread(thread_id)

    def phone_debug_unlock_all_mails():
        for mail_id in PHONE_MAILS.keys():
            phone_unlock_mail(mail_id)

    def phone_debug_unlock_all_posts():
        for post_id in PHONE_SOCIAL_POSTS.keys():
            phone_unlock_post(post_id)

    def phone_debug_reset():
        phone_state.clear()
        phone_ensure_state()
```

Optional debug screen:

```renpy
screen debug_phone():
    tag menu

    frame:
        xalign 0.5
        yalign 0.5

        vbox:
            text "Phone Debug"
            textbutton "Unlock All Contacts" action Function(phone_debug_unlock_all_contacts)
            textbutton "Unlock All Threads" action Function(phone_debug_unlock_all_threads)
            textbutton "Unlock All Mails" action Function(phone_debug_unlock_all_mails)
            textbutton "Unlock All Posts" action Function(phone_debug_unlock_all_posts)
            textbutton "Reset Phone" action Function(phone_debug_reset)
            textbutton "Close" action Return()
```

---

# 21. Implementation Phases

## Phase 1 — MVP Phone

Deliver:

* `phone_state.rpy`
* `phone_logic.rpy`
* `phone_contacts.rpy`
* `phone_threads.rpy`
* `phone_screen.rpy`
* `phone_subscreens.rpy`
* Messages tab
* Contacts tab
* Contact unlock
* Thread unlock
* Read/unread state
* Quick menu or map entry point

No reply choices yet.
No mail/social yet.

Acceptance:

* Player can open the Phone.
* Phone shows unlocked contacts.
* Phone shows unlocked message threads.
* Unread threads display with an indicator.
* Opening a thread marks it as read.
* Contact/thread unlocks persist across save/load.

---

## Phase 2 — Mail + Social

Deliver:

* `phone_mail.rpy`
* `phone_social.rpy`
* Mail tab
* Social tab
* Read tracking for mail/posts
* Like tracking for posts
* Effect application on read/like

Acceptance:

* Player can read unlocked mail.
* Player can read unlocked social posts.
* Read mail/posts do not show as unread again.
* Effects are applied only once.
* Social likes persist.

---

## Phase 3 — Character Status + Inventory

Deliver:

* `character_status_data.rpy`
* Character Status view inside Contacts
* Public job/income/status data
* Inventory/keepsake display
* Known notes display

Acceptance:

* Character public status can be updated from scenes.
* Items can be added to character inventory.
* Known notes can be added without duplication.
* Hidden story scores are not displayed directly.

---

## Phase 4 — Reply Choices

Deliver:

* `PHONE_REPLY_CHOICES`
* Reply buttons in thread view
* One-time reply selection
* Effects on reply
* Optional runtime response messages

Acceptance:

* Player can select one-time replies.
* Reply effects apply once.
* Reply cannot be spammed for repeated score gains.
* Selected replies persist across save/load.

---

## Phase 5 — Polish

Deliver:

* phone frame art;
* better message bubble alignment;
* avatar support;
* animation/dissolve;
* sound cues;
* optional phone notification pop-up;
* responsive/touch adjustments.

Acceptance:

* UI matches warm beige/brown project style.
* Phone panel works in 1920x1080.
* No major layout overflow.
* No Ren’Py warnings from missing assets or invalid screens.

---

# 22. Testing Checklist

## State / Save-load

* Start a new game.
* Unlock first contact.
* Save.
* Load.
* Confirm contact remains unlocked.
* Unlock a thread.
* Mark it read.
* Save/load.
* Confirm unread state does not return.

## Conditions

Test each condition type:

* `completed:<chapter_id>`
* `flag:<flag_name>`
* `not_flag:<flag_name>`
* `contact:<contact_id>`
* `thread_read:<thread_id>`
* `mail_read:<mail_id>`
* `post_read:<post_id>`
* `direction:<character>:<direction>`
* `score_gte:<score_key>:<amount>`
* `score_lte:<score_key>:<amount>`

## Effects

Test each effect type:

* flags;
* story scores;
* directions;
* character status patch;
* inventory add;
* known info add.

Confirm effects are not repeatedly applied when reopening the same item unless explicitly intended.

## UI

* Open Phone from quick menu.
* Open Phone from map.
* Open Phone from scene.
* Switch tabs.
* Select thread/mail/contact.
* Scroll long content.
* Close Phone and return to previous context.

## Regression

* Route Map still opens.
* Interactive Map still opens.
* Existing chapter completion still works.
* Existing Library screens still work.
* Existing save/load screens still work.
* No generated/runtime files are edited.

---

# 23. Anti-patterns

Do not:

* expose hidden route scores as visible UI;
* put phone content directly in screen code;
* mutate static `define` dictionaries at runtime;
* turn Phone into the main chapter navigator;
* create repeatable reply choices that farm points;
* edit `game/cache/`, `game/saves/`, `.rpyc`, `.rpymc`, `log.txt`, or `traceback.txt`;
* rely on generated navigation files as source of truth;
* overload `game/screens.rpy` with the full phone implementation;
* add many user-facing strings without considering translation sync.

---

# 24. Minimal First Content Set

Implement these sample entries for initial validation:

## Contacts

* `tam`
* `huyen`
* `hoang`

## Threads

* `tam_hoang_after_party_01`
* `group_company_party_recap`

## Mail

* `company_party_invitation`
* `company_salary_first_month`

## Social

* `huyen_party_post_01`

## Items

* `tam_first_salary_envelope`

This is enough to test:

* contact unlock;
* thread unlock;
* read/unread;
* mail read effects;
* social post read/like;
* character status update;
* inventory update.

---

# 25. Final Expected Outcome

After implementation, the player should be able to:

1. Open a warm-themed Phone Panel from the map or quick menu.
2. See unlocked contacts only.
3. Read unlocked chat threads.
4. Receive unread indicators.
5. Read mail and social posts.
6. View public character status.
7. See job/income/inventory/known notes when unlocked.
8. Trigger small story effects from reading or replying.
9. Continue using the existing Route Map, Interactive Map, Library, and progression systems normally.

The Phone Panel should feel like part of the story world, not a separate app glued onto the game.

Its best narrative use is not “the player checks messages.”

Its best narrative use is:

```text
The player notices who replied.
Who did not.
Who typed too much.
Who deleted something.
And who cared enough to ask a very ordinary question.
```
