init -1 python:
    story_reader_cache = {}

    def parse_story_text(raw_text):
        metadata = {}
        body = raw_text or ""

        if body.startswith("---"):
            parts = body.split("---", 2)
            if len(parts) >= 3:
                metadata = parse_simple_frontmatter(parts[1])
                body = parts[2]

        events = []
        for raw_line in body.splitlines():
            line = raw_line.strip()
            if not line or line.startswith("#"):
                continue

            event = parse_story_line(line)
            if event:
                events.append(event)

        return {
            "metadata": metadata,
            "events": events,
        }

    def parse_simple_frontmatter(text):
        data = {}
        current_list_key = None

        for raw_line in text.splitlines():
            line = raw_line.rstrip()
            stripped = line.strip()
            if not stripped:
                continue

            if stripped.startswith("- ") and current_list_key:
                data.setdefault(current_list_key, []).append(stripped[2:].strip())
                continue

            if ":" not in line:
                continue

            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()

            if not value:
                data[key] = []
                current_list_key = key
            else:
                data[key] = value
                current_list_key = None

        return data

    def parse_story_line(line):
        if line.startswith("scene "):
            scene_body = line.replace("scene ", "", 1).strip()
            scene_body = scene_body.split(" with ", 1)[0].strip()

            if scene_body.startswith("bg "):
                bg_id = scene_body[3:].strip()
            else:
                bg_id = scene_body

            return {"type": "scene", "bg": bg_id}

        if line.startswith("show "):
            parts = line.split()
            event = {
                "type": "show",
                "character": parts[1] if len(parts) > 1 else None,
                "expression": parts[2] if len(parts) > 2 else "neutral",
                "position": "center",
            }
            if "at" in parts:
                at_index = parts.index("at")
                if len(parts) > at_index + 1:
                    event["position"] = parts[at_index + 1]
            return event

        if line.startswith("hide "):
            return {"type": "hide", "character": line.replace("hide ", "", 1).strip()}

        if line.startswith("music "):
            return {"type": "music", "id": line.replace("music ", "", 1).strip()}

        if line.startswith("sfx "):
            return {"type": "sfx", "id": line.replace("sfx ", "", 1).strip()}

        if line.startswith("pause "):
            value = line.replace("pause ", "", 1).strip()
            try:
                seconds = float(value)
            except Exception:
                seconds = 0.5
            return {"type": "pause", "seconds": seconds}

        if line.startswith("narrator:"):
            return {"type": "narrator", "text": line.replace("narrator:", "", 1).strip()}

        if ":" in line:
            speaker_part, text = line.split(":", 1)
            speaker_tokens = speaker_part.split()
            character = speaker_tokens[0]
            expression = speaker_tokens[1] if len(speaker_tokens) > 1 else "neutral"
            return {
                "type": "dialogue",
                "character": character,
                "expression": expression,
                "text": text.strip(),
            }

        return {"type": "narrator", "text": line}

    def story_image_tuple(image_name):
        if isinstance(image_name, tuple):
            return image_name
        return tuple(part for part in str(image_name or "").split() if part)

    def story_has_image(image_name):
        image_tuple = story_image_tuple(image_name)
        if not image_tuple:
            return False
        try:
            return renpy.has_image(image_tuple)
        except Exception:
            return False

    def story_image_name(image_name):
        image_tuple = story_image_tuple(image_name)
        if not image_tuple:
            return None
        return " ".join(image_tuple)

    def story_background_display_name(background_id):
        normalized = (background_id or "").strip()
        if not normalized:
            return None

        candidates = [
            normalized,
            "bg %s" % normalized,
            "bg_%s" % normalized,
        ]

        for candidate in candidates:
            if story_has_image(candidate):
                return story_image_name(candidate)

        return None

    def story_character_name(character_id):
        character_object = globals().get(character_id, None)
        if character_object is not None:
            name = getattr(character_object, "name", None)
            if name:
                return name
        return character_id.replace("_", " ").title()

    def story_sprite_entry(character, expression, position):
        display_name = None
        normalized_expression = expression or "neutral"
        candidates = [
            "side %s %s" % (character, normalized_expression),
            "%s %s" % (character, normalized_expression),
            "side %s" % character,
            character,
        ]

        for candidate in candidates:
            if story_has_image(candidate):
                display_name = story_image_name(candidate)
                break

        return {
            "character": character,
            "expression": expression or "neutral",
            "position": position or "center",
            "display_name": display_name,
        }

    def snapshot_story_sprites(sprite_state):
        return [dict(sprite) for sprite in sprite_state]

    def upsert_story_sprite(sprite_state, character, expression=None, position=None):
        existing_sprite = None
        remaining_sprites = []

        for sprite in sprite_state:
            if sprite.get("character") == character and existing_sprite is None:
                existing_sprite = sprite
            else:
                remaining_sprites.append(sprite)

        resolved_expression = expression or (existing_sprite.get("expression") if existing_sprite else "neutral")
        resolved_position = position or (existing_sprite.get("position") if existing_sprite else "center")

        remaining_sprites.append(story_sprite_entry(character, resolved_expression, resolved_position))
        return remaining_sprites

    def build_story_reader_pages(parsed_story):
        pages = []
        current_background = None
        sprite_state = []

        for event in parsed_story.get("events", []):
            event_type = event.get("type")

            if event_type == "scene":
                current_background = event.get("bg")
                continue

            if event_type == "show":
                character = event.get("character")
                sprite_state = upsert_story_sprite(sprite_state, character, event.get("expression"), event.get("position"))
                continue

            if event_type == "hide":
                character = event.get("character")
                sprite_state = [sprite for sprite in sprite_state if sprite.get("character") != character]
                continue

            if event_type not in ["narrator", "dialogue"]:
                continue

            if event_type == "dialogue":
                sprite_state = upsert_story_sprite(
                    sprite_state,
                    event.get("character"),
                    event.get("expression"),
                    None,
                )

            background_display = story_background_display_name(current_background)
            pages.append({
                "background_display": background_display,
                "sprites": snapshot_story_sprites(sprite_state),
                "speaker": None if event_type == "narrator" else story_character_name(event.get("character", "")),
                "text": event.get("text", ""),
            })

        return pages

    def load_and_parse_library_story(item):
        if not item:
            return None

        content_id = item.get("id")
        if content_id in story_reader_cache:
            return story_reader_cache[content_id]

        raw_text = story_library_read_text(item.get("file", ""))
        if raw_text is None:
            return None

        parsed_story = parse_story_text(raw_text)
        parsed_story["metadata"] = dict(parsed_story.get("metadata", {}), **{
            "id": item.get("id"),
            "title": item.get("title"),
            "series": item.get("series"),
            "type": item.get("type"),
            "size": item.get("size"),
        })
        parsed_story["pages"] = build_story_reader_pages(parsed_story)
        story_reader_cache[content_id] = parsed_story
        return parsed_story
