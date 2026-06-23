init -2 python:
    def normalize_timeline_persistent_state():
        if not hasattr(persistent, "timeline_bookmarks") or persistent.timeline_bookmarks is None:
            persistent.timeline_bookmarks = []
        elif not isinstance(persistent.timeline_bookmarks, list):
            persistent.timeline_bookmarks = list(persistent.timeline_bookmarks)

    normalize_timeline_persistent_state()

    TIMELINE_ROUTES = [
        {"id": "tam", "label": "Tâm"},
        {"id": "hoang", "label": "Hoàng"},
        {"id": "yuuka", "label": "Yuuka"},
        {"id": "minh", "label": "Minh"},
        {"id": "thienan", "label": "Thiên An"},
    ]

    TIMELINE_MAP_BACKGROUND = "images/assets/bg/ui/bg_timeline_map_blur.webp"
    TIMELINE_FALLBACK_BACKGROUND = "gui/theme/background_full.png"
    TIMELINE_FALLBACK_THUMBNAIL = "gui/game_menu.png"

    TIMELINE_MAP_NODES = {
        "tam": [
            {
                "id": "tam_c01",
                "chapter_id": "tam_c01",
                "title": "Interview Day",
                "code": "Ch.01",
                "type": "core",
                "thumbnail": "images/assets/thumbnails/tam/tam_c01.webp",
                "summary": "Tam steps into her first interview and the route's opening tension.",
                "duration": "Approx. 20 min",
                "x": 40,
                "y": 120,
                "w": 200,
                "h": 200,
            },
            {
                "id": "tam_c02",
                "chapter_id": "tam_c02",
                "title": "First Weeks",
                "code": "Ch.02",
                "type": "core",
                "thumbnail": "images/assets/thumbnails/tam/tam_c02.webp",
                "summary": "Early work days start shaping Tam's confidence and direction.",
                "duration": "Approx. 25 min",
                "x": 320,
                "y": 120,
                "w": 200,
                "h": 200,
            },
            {
                "id": "tam_c03",
                "chapter_id": "tam_c03",
                "title": "Dinner",
                "code": "Ch.03",
                "type": "core",
                "thumbnail": "images/assets/thumbnails/tam/tam_c03.webp",
                "summary": "A quieter dinner scene reframes the route's emotional stakes.",
                "duration": "Approx. 25 min",
                "x": 600,
                "y": 120,
                "w": 200,
                "h": 200,
            },
            {
                "id": "tam_c03a",
                "chapter_id": "tam_c03a",
                "title": "The Confession",
                "code": "Ch.03A",
                "type": "pov",
                "thumbnail": "images/assets/thumbnails/tam/tam_c03a.webp",
                "summary": "A planned branch centered on Tam's emotional response.",
                "duration": "Approx. 15 min",
                "x": 930,
                "y": 0,
                "w": 200,
                "h": 200,
            },
            {
                "id": "tam_c03b",
                "chapter_id": "tam_c03b",
                "title": "Different Choice",
                "code": "Ch.03B",
                "type": "pov",
                "thumbnail": "images/assets/thumbnails/tam/tam_c03b.webp",
                "summary": "A planned branch that shifts the focus toward Hoang.",
                "duration": "Approx. 15 min",
                "x": 930,
                "y": 250,
                "w": 200,
                "h": 200,
            },
            {
                "id": "tam_c04",
                "chapter_id": "tam_c04",
                "title": "The Decision",
                "code": "Ch.04",
                "type": "core",
                "thumbnail": "images/assets/thumbnails/tam/tam_c04.webp",
                "summary": "A future decision point that pushes Tam's route forward.",
                "duration": "Approx. 30 min",
                "x": 1260,
                "y": 0,
                "w": 200,
                "h": 200,
            },
            {
                "id": "tam_c05",
                "chapter_id": "tam_c05",
                "title": "Moving Forward",
                "code": "Ch.05",
                "type": "core",
                "thumbnail": "images/assets/thumbnails/tam/tam_c05.webp",
                "summary": "The route rejoins after the branch and carries its consequences forward.",
                "duration": "Approx. 25 min",
                "x": 1590,
                "y": 250,
                "w": 200,
                "h": 200,
            },
            {
                "id": "tam_c06",
                "chapter_id": "tam_c06",
                "title": "After the Storm",
                "code": "Ch.06",
                "type": "core",
                "thumbnail": "images/assets/thumbnails/tam/tam_c06.webp",
                "summary": "A locked future chapter.",
                "duration": "Approx. 30 min",
                "x": 1910,
                "y": 250,
                "w": 200,
                "h": 200,
            },
            {
                "id": "tam_bonus_after_rain",
                "chapter_id": "tam_bonus_after_rain",
                "title": "After Rain",
                "code": "Bonus",
                "type": "bonus",
                "thumbnail": "images/assets/thumbnails/tam/tam_bonus_after_rain.webp",
                "summary": "Optional bonus epilogue content planned after the main path settles.",
                "duration": "Approx. 10 min",
                "x": 2240,
                "y": 250,
                "w": 200,
                "h": 200,
            },
        ],
        "hoang": [
            {
                "id": "hoang_h01",
                "chapter_id": "hoang_h01",
                "title": "Restraint",
                "code": "POV.01",
                "type": "pov",
                "thumbnail": "images/assets/thumbnails/hoang/hoang_h01.webp",
                "summary": "Hoang's first point-of-view chapter opens the side route.",
                "duration": "Approx. 10 min",
                "x": 80,
                "y": 120,
                "w": 200,
                "h": 200,
            },
            {
                "id": "hoang_bonus_restraint",
                "chapter_id": "hoang_bonus_restraint",
                "title": "Bonus: Restraint",
                "code": "Bonus A",
                "type": "bonus",
                "thumbnail": "images/assets/thumbnails/hoang/hoang_bonus_restraint.webp",
                "summary": "A quieter branch that excludes the confession variant.",
                "duration": "Approx. 8 min",
                "x": 420,
                "y": 0,
                "w": 200,
                "h": 200,
            },
            {
                "id": "hoang_bonus_confession",
                "chapter_id": "hoang_bonus_confession",
                "title": "Bonus: Confession",
                "code": "Bonus B",
                "type": "bonus",
                "thumbnail": "images/assets/thumbnails/hoang/hoang_bonus_confession.webp",
                "summary": "A more forceful branch that closes off restraint.",
                "duration": "Approx. 8 min",
                "x": 420,
                "y": 220,
                "w": 200,
                "h": 200,
            },
            {
                "id": "hoang_h02",
                "chapter_id": "hoang_h02",
                "title": "Convergence",
                "code": "POV.02",
                "type": "pov",
                "thumbnail": "images/assets/thumbnails/hoang/hoang_h02.webp",
                "summary": "The second Hoang chapter closes the first two-route loop.",
                "duration": "Approx. 10 min",
                "x": 760,
                "y": 120,
                "w": 200,
                "h": 200,
            },
        ],
        "yuuka": [],
        "minh": [],
    }

    TIMELINE_MAP_CONNECTIONS = {
        "tam": [
            {"from": "tam_c01", "to": "tam_c02", "style": "normal"},
            {"from": "tam_c02", "to": "tam_c03", "style": "normal"},
            {"from": "tam_c03", "to": "tam_c03a", "style": "branch"},
            {"from": "tam_c03", "to": "tam_c03b", "style": "branch"},
            {"from": "tam_c03a", "to": "tam_c04", "style": "normal"},
            {"from": "tam_c04", "to": "tam_c05", "style": "merge"},
            {"from": "tam_c03b", "to": "tam_c05", "style": "merge"},
            {"from": "tam_c05", "to": "tam_c06", "style": "normal"},
            {"from": "tam_c06", "to": "tam_bonus_after_rain", "style": "dashed"},
        ],
        "hoang": [
            {"from": "hoang_h01", "to": "hoang_bonus_restraint", "style": "branch"},
            {"from": "hoang_h01", "to": "hoang_bonus_confession", "style": "branch"},
            {"from": "hoang_bonus_restraint", "to": "hoang_h02", "style": "merge"},
            {"from": "hoang_bonus_confession", "to": "hoang_h02", "style": "merge"},
        ],
    }



    TIMELINE_MAP_NODES["minh"] = [
        {
            "id": "minh_m01",
            "chapter_id": "minh_m01",
            "title": "Minh Returns",
            "code": "M.01",
            "type": "pov",
            "thumbnail": "images/assets/thumbnails/minh/minh_m01.webp",
            "summary": "Placeholder for Minh's route unlock when he returns to Vietnam.",
            "duration": "Approx. 20 min",
            "x": 80,
            "y": 120,
            "w": 200,
            "h": 200,
        },
        {
            "id": "minh_m02",
            "chapter_id": "minh_m02",
            "title": "At the Company",
            "code": "M.02",
            "type": "pov",
            "thumbnail": "images/assets/thumbnails/minh/minh_m02.webp",
            "summary": "Placeholder for Minh's corporate-pressure route chapter.",
            "duration": "Approx. 20 min",
            "x": 400,
            "y": 120,
            "w": 200,
            "h": 200,
        },
        {
            "id": "minh_m03",
            "chapter_id": "minh_m03",
            "title": "After the Screening",
            "code": "M.03",
            "type": "pov",
            "thumbnail": "images/assets/thumbnails/minh/minh_m03.webp",
            "summary": "Placeholder for Minh's private reaction to Yuuka's re-entry.",
            "duration": "Approx. 18 min",
            "x": 720,
            "y": 120,
            "w": 200,
            "h": 200,
        },
    ]

    TIMELINE_MAP_NODES["yuuka"] = [
        {
            "id": "yuuka_y01",
            "chapter_id": "yuuka_y01",
            "title": "Film Festival",
            "code": "Y.01",
            "type": "core",
            "thumbnail": "images/assets/thumbnails/yuuka/yuuka_y01.webp",
            "summary": "Yuuka's present-day entry point at the film festival.",
            "duration": "Approx. 18 min",
            "x": 60,
            "y": 120,
            "w": 200,
            "h": 200,
        },
        {
            "id": "yuuka_flashback_01",
            "chapter_id": "yuuka_flashback_01",
            "title": "First Frame",
            "code": "FB.01",
            "type": "bonus",
            "thumbnail": "images/assets/thumbnails/yuuka/yuuka_flashback_01.webp",
            "summary": "First flashback placeholder for Minh and Yuuka's shared past.",
            "duration": "Approx. 12 min",
            "x": 360,
            "y": 120,
            "w": 200,
            "h": 200,
        },
        {
            "id": "yuuka_flashback_02",
            "chapter_id": "yuuka_flashback_02",
            "title": "Working Rhythm",
            "code": "FB.02",
            "type": "bonus",
            "thumbnail": "images/assets/thumbnails/yuuka/yuuka_flashback_02.webp",
            "summary": "A second flashback placeholder shaped by collaboration and emotional distance.",
            "duration": "Approx. 12 min",
            "x": 660,
            "y": 40,
            "w": 200,
            "h": 200,
        },
        {
            "id": "yuuka_flashback_03",
            "chapter_id": "yuuka_flashback_03",
            "title": "The Door Left Open",
            "code": "FB.03",
            "type": "bonus",
            "thumbnail": "images/assets/thumbnails/yuuka/yuuka_flashback_03.webp",
            "summary": "The final planned flashback before the relationship state lock-in.",
            "duration": "Approx. 14 min",
            "x": 660,
            "y": 240,
            "w": 200,
            "h": 200,
        },
        {
            "id": "yuuka_y02",
            "chapter_id": "yuuka_y02",
            "title": "Screening Night",
            "code": "Y.02",
            "type": "core",
            "thumbnail": "images/assets/thumbnails/yuuka/yuuka_y02.webp",
            "summary": "Placeholder for the public screening and private emotional fallout chapter.",
            "duration": "Approx. 20 min",
            "x": 960,
            "y": 120,
            "w": 200,
            "h": 200,
        },
    ]

    TIMELINE_MAP_CONNECTIONS["minh"] = [
        {"from": "minh_m01", "to": "minh_m02", "style": "normal"},
        {"from": "minh_m02", "to": "minh_m03", "style": "normal"},
    ]

    TIMELINE_MAP_CONNECTIONS["yuuka"] = [
        {"from": "yuuka_y01", "to": "yuuka_flashback_01", "style": "normal"},
        {"from": "yuuka_flashback_01", "to": "yuuka_flashback_02", "style": "branch"},
        {"from": "yuuka_flashback_01", "to": "yuuka_flashback_03", "style": "branch"},
        {"from": "yuuka_flashback_02", "to": "yuuka_y02", "style": "merge"},
        {"from": "yuuka_flashback_03", "to": "yuuka_y02", "style": "merge"},
    ]

    TIMELINE_MAP_CONNECTIONS["thienan"] = [
        # {"from": "thienan_c01", "to": "thienan_c02", "style": "normal"},
        # {"from": "thienan_c02", "to": "thienan_c03", "style": "normal"},
    ]

    TIMELINE_NODE_META = {
        "tam_c01": {
            "display_title": "C01 - Ngay phong van",
            "summary": "Tam and Huyen interview, get hired, and have their first distant encounter with Hoang.",
            "conditions": ["Always available after the rain-dream prologue."],
            "stat_modifiers": ["+career_tam or +tam_minh_drawn from the opening choice", "+huyen_tam_bond possible"],
        },
        "tam_c02": {
            "display_title": "C02 - Buoi tiec cong ty",
            "summary": "The company party seeds the main Tam-Hoang dynamic and can also reinforce Huyen-Hoang momentum.",
            "conditions": ["Unlock after C01.", "Hoang route strength depends on prior interest and social choices."],
            "stat_modifiers": ["+trust_tam_hoang / +intimacy_tam_hoang on canon seed", "+career_tam on the social-dodge branch", "+trust_hoang_huyen on Huyen-forward branch"],
        },
        "tam_c03": {
            "display_title": "C03 - Chi gai Thien An",
            "summary": "Family pressure, career advice, and Thien An's unresolved emotional life broaden Tam's world beyond romance.",
            "conditions": ["Unlock after C02."],
            "stat_modifiers": ["+trust_tam_thienan on family support", "+career_tam on project-management choice", "+family pressure and Thien An flags can be seeded"],
        },
        "tam_c03a": {
            "display_title": "Branch A - Tam mo long",
            "summary": "Placeholder branch for the version where Tam leans toward emotional openness after the early route seeds.",
            "conditions": ["Planned branch after the early Tam route fork."],
            "stat_modifiers": ["Expected trust/intimacy gains on Tam-led emotional choices"],
        },
        "tam_c03b": {
            "display_title": "Branch B - Tam lui lai",
            "summary": "Placeholder branch for a more guarded or Hoang-shifted version of the same beat.",
            "conditions": ["Planned alternate branch after the early Tam route fork."],
            "stat_modifiers": ["Expected distance / hesitation / route-shift flags"],
        },
        "tam_c04": {
            "display_title": "C05 - Buoi hen Chu Nhat",
            "summary": "Planned Sunday date chapter where Hoang actively steps forward and the relationship direction crystallizes.",
            "conditions": ["Follows Hoang's gift setup and the active romance/friend-group branch."],
            "stat_modifiers": ["+trust_tam_hoang", "+intimacy_tam_hoang", "Can set hoang_tam_commit or alternate group outcomes"],
        },
        "tam_c05": {
            "display_title": "C06 - Minh ve nuoc",
            "summary": "Minh's return disrupts the emotional balance and opens the next major route layer.",
            "conditions": ["Unlocks after the Sunday-date convergence beat."],
            "stat_modifiers": ["Unlock minh_route", "+tam_minh_drawn", "+hoang_insecurity_active", "+minh_notices_tam"],
        },
        "tam_c06": {
            "display_title": "C07 - Minh o cong ty",
            "summary": "Minh enters the work sphere directly, turning subtext into workplace pressure and route tension.",
            "conditions": ["Unlock after Minh's return.", "Tam or Minh POV depends on prior flags."],
            "stat_modifiers": ["Can increase trust_tam_hoang or tam_minh_drawn", "Can raise career_tam and Minh respect variables"],
        },
        "tam_bonus_after_rain": {
            "display_title": "C08 - Yuuka Nakamura",
            "summary": "Yuuka arrives as a neutral but high-impact presence, unlocking the Minh-Yuuka flashback structure.",
            "conditions": ["Planned after C07.", "Unlocks Yuuka route and first flashback chapters."],
            "stat_modifiers": ["Unlock yuuka_route", "Unlock first flashbacks", "Can raise Tam observer or conflict variables"],
        },
        "hoang_h01": {
            "display_title": "C04 - Hoang POV: Can nha cua anh trai",
            "summary": "Hoang alone in Minh's house, choosing a gift and revealing more about class, family, and restraint.",
            "conditions": ["Unlock after C03.", "Gift branch depends on Tam-Hoang, Huyen-Hoang, or friend-group direction."],
            "stat_modifiers": ["+intimacy_tam_hoang or +trust_hoang_huyen", "+trust_friend_group on neutral branch", "+awkwardness on confused-gift branch"],
        },
        "hoang_bonus_restraint": {
            "display_title": "Gift Branch - Restraint",
            "summary": "Prototype branch representing Hoang's quieter choice architecture and lower-confession path.",
            "conditions": ["Unlock from Hoang POV after the route starts favoring restraint."],
            "stat_modifiers": ["Supports hoang_tam_restraint or softer direction flags"],
        },
        "hoang_bonus_confession": {
            "display_title": "Gift Branch - Confession",
            "summary": "Prototype branch for Hoang stepping forward too directly and forcing the emotional tempo.",
            "conditions": ["Unlock from Hoang POV when the route shifts toward direct confession."],
            "stat_modifiers": ["Supports high-intensity Hoang momentum and corresponding risk flags"],
        },
        "hoang_h02": {
            "display_title": "Convergence Beat",
            "summary": "The Hoang route recombines after the side branch and feeds back into the broader cast timeline.",
            "conditions": ["Requires an Hoang bonus branch and Tam route progression."],
            "stat_modifiers": ["Can reinforce trust_tam_hoang, trust_hoang_huyen, or friend-group stability"],
        },
        "minh_m01": {
            "display_title": "Minh Route Unlock - Minh ve nuoc",
            "summary": "Placeholder for the first dedicated Minh-route beat opened by Chapter 6.",
            "conditions": ["Unlock after Chapter 6 / Tam C06 equivalent."],
            "stat_modifiers": ["+tam_minh_drawn", "+hoang_insecurity_active", "+minh_notices_tam"],
        },
        "minh_m02": {
            "display_title": "Minh POV - O cong ty",
            "summary": "Placeholder for the company arc where Minh observes, tests boundaries, and affects career pressure.",
            "conditions": ["Unlock after Minh returns.", "POV version depends on Tam/Minh flag state."],
            "stat_modifiers": ["+career_tam possible", "+minh_respect_tam possible", "+tam_minh_drawn or +boundary flags"],
        },
        "minh_m03": {
            "display_title": "Minh Reaction Sau Film Festival",
            "summary": "Placeholder for Minh's private reaction after Yuuka's public re-entry into the story.",
            "conditions": ["Follows Yuuka's first present-day appearance and/or screening night."],
            "stat_modifiers": ["Can alter trust_minh_yuuka, distance_minh_yuuka, and avoidance_minh"],
        },
        "yuuka_y01": {
            "display_title": "C08 - Yuuka Nakamura tai Film Festival",
            "summary": "Yuuka enters as a respected young director, with her history with Minh deliberately framed as neutral at first.",
            "conditions": ["Unlock after Chapter 8.", "Starts Yuuka route and flashback layer."],
            "stat_modifiers": ["Unlock first flashbacks", "+career_yuuka framing", "Can raise Tam conflict or observer flags"],
        },
        "yuuka_flashback_01": {
            "display_title": "FB01 - First Frame",
            "summary": "The first planned flashback for Minh and Yuuka's shared artistic and emotional history.",
            "conditions": ["Unlock after Yuuka's route opens."],
            "stat_modifiers": ["Begins trust_minh_yuuka and intimacy_minh_yuuka shaping"],
        },
        "yuuka_flashback_02": {
            "display_title": "FB02 - Working Rhythm",
            "summary": "A collaboration-driven flashback showing how habit, craft, and attraction intertwined.",
            "conditions": ["Unlock after FB01."],
            "stat_modifiers": ["Can raise intimacy_minh_yuuka or distance_minh_yuuka depending on choices"],
        },
        "yuuka_flashback_03": {
            "display_title": "FB03 - The Door Left Open",
            "summary": "The last pre-lock flashback before the Minh-Yuuka relationship state is chosen.",
            "conditions": ["Unlock after FB02 / flashback progression."],
            "stat_modifiers": ["Leads into old_friends / ex_lovers / still_lovers state selection"],
        },
        "yuuka_y02": {
            "display_title": "C09 - Buoi chieu phim",
            "summary": "Yuuka's screening night pushes the present-day route into open emotional consequence.",
            "conditions": ["Follows Yuuka's introduction and at least one flashback pass."],
            "stat_modifiers": ["Can raise career_yuuka, intimacy_minh_yuuka, distance_minh_yuuka, or yuuka_avoidance"],
        },
    }

    def timeline_get_nodes(route_id):
        return TIMELINE_MAP_NODES.get(route_id, [])

    def timeline_get_connections(route_id):
        return TIMELINE_MAP_CONNECTIONS.get(route_id, [])

    def timeline_find_node(route_id, node_id):
        for node in timeline_get_nodes(route_id):
            if node["id"] == node_id:
                return node
        return None

    def timeline_find_node_by_chapter(route_id, chapter_id):
        for node in timeline_get_nodes(route_id):
            if node.get("chapter_id") == chapter_id:
                return node
        return None

    def timeline_get_chapter_data(chapter_id):
        if "CHAPTERS" in globals() and chapter_id in CHAPTERS:
            return CHAPTERS[chapter_id]
        return None

    def timeline_is_completed(chapter_id):
        try:
            return chapter_id in progress.get("completed", [])
        except Exception:
            return False

    def timeline_is_excluded(chapter_id):
        try:
            return chapter_id in progress.get("excluded", [])
        except Exception:
            return False

    def timeline_is_available(chapter_id):
        try:
            return get_chapter_state(chapter_id) == "available"
        except Exception:
            chapter = timeline_get_chapter_data(chapter_id)
            if not chapter:
                return False
            return all(timeline_is_completed(req_id) for req_id in chapter.get("prerequisites", []))

    def timeline_get_node_state(node):
        chapter_id = node["chapter_id"]

        if timeline_is_completed(chapter_id):
            return "completed"
        if timeline_is_excluded(chapter_id):
            return "locked"
        if timeline_is_available(chapter_id):
            return "current"
        return "locked"

    def timeline_has_runtime_chapter(chapter_id):
        return timeline_get_chapter_data(chapter_id) is not None

    def timeline_get_first_selectable_node(route_id):
        nodes = timeline_get_nodes(route_id)

        for node in nodes:
            if timeline_get_node_state(node) == "current":
                return node["id"]

        for node in nodes:
            if timeline_get_node_state(node) == "completed":
                return node["id"]

        if nodes:
            return nodes[0]["id"]

        return None

    def timeline_resolve_selected_node(route_id, selected_node_id):
        return timeline_find_node(route_id, selected_node_id) or timeline_find_node(route_id, timeline_get_first_selectable_node(route_id))

    def timeline_get_background_displayable():
        if renpy.loadable(TIMELINE_MAP_BACKGROUND):
            return TIMELINE_MAP_BACKGROUND
        return TIMELINE_FALLBACK_BACKGROUND

    def timeline_get_thumbnail_displayable(node):
        thumbnail = node.get("thumbnail")
        if thumbnail and renpy.loadable(thumbnail):
            return thumbnail
        return TIMELINE_FALLBACK_THUMBNAIL

    def timeline_toggle_bookmark(chapter_id):
        normalize_timeline_persistent_state()
        if chapter_id in persistent.timeline_bookmarks:
            persistent.timeline_bookmarks.remove(chapter_id)
            return False
        persistent.timeline_bookmarks.append(chapter_id)
        return True

    def timeline_is_bookmarked(chapter_id):
        normalize_timeline_persistent_state()
        return chapter_id in persistent.timeline_bookmarks

    def timeline_get_route_label(route_id):
        for route in TIMELINE_ROUTES:
            if route["id"] == route_id:
                return route["label"]
        if route_id in ROUTES:
            return ROUTES[route_id]["title"]
        return route_id.title()

    def timeline_get_node_meta(node_or_chapter_id):
        chapter_id = node_or_chapter_id
        if isinstance(node_or_chapter_id, dict):
            chapter_id = node_or_chapter_id.get("chapter_id")
        return TIMELINE_NODE_META.get(chapter_id, {})

    def timeline_get_node_display_title(node):
        meta = timeline_get_node_meta(node)
        return meta.get("display_title") or node.get("title") or node.get("chapter_id")

    def timeline_get_node_summary(node):
        meta = timeline_get_node_meta(node)
        return meta.get("summary") or node.get("summary", "")

    def timeline_get_node_stat_modifiers(node):
        meta = timeline_get_node_meta(node)
        return meta.get("stat_modifiers", [])

    def timeline_get_detail_title(node):
        meta = timeline_get_node_meta(node)
        if meta.get("display_title"):
            return meta["display_title"]
        chapter = timeline_get_chapter_data(node["chapter_id"])
        if chapter:
            return chapter.get("title") or node["title"]
        return node["title"]

    def timeline_get_requirement_lines(node):
        chapter = timeline_get_chapter_data(node["chapter_id"])
        meta = timeline_get_node_meta(node)
        lines = []

        if chapter:
            prerequisites = chapter.get("prerequisites", [])
            if prerequisites:
                for prerequisite_id in prerequisites:
                    label = chapter_title(prerequisite_id) if prerequisite_id in CHAPTERS else prerequisite_id
                    lines.append((timeline_is_completed(prerequisite_id), "Complete %s" % label))
            else:
                lines.append((True, "No chapter prerequisite."))

            required_directions = chapter.get("required_directions", {})
            for route_id, directions in required_directions.items():
                for direction in directions:
                    lines.append((has_relationship_direction(route_id, direction), "%s route direction: %s" % (route_title(route_id), direction)))
        else:
            lines.append((False, "Planned chapter: runtime metadata is not implemented yet."))

        for condition in meta.get("conditions", []):
            lines.append((False, condition))

        if node.get("type") == "bonus":
            lines.append((timeline_get_node_state(node) != "locked", "Bonus route branch unlocked."))

        if timeline_is_excluded(node["chapter_id"]):
            lines.append((False, "This chapter was excluded by a previous choice."))

        return lines[:5]

    def timeline_get_preview_text(node):
        state = timeline_get_node_state(node)
        if state == "completed":
            return "%s is already complete." % timeline_get_detail_title(node)
        if state == "current":
            return "%s is ready to play." % timeline_get_detail_title(node)
        if timeline_has_runtime_chapter(node["chapter_id"]):
            return "%s is still locked." % timeline_get_detail_title(node)
        return "%s is planned but not implemented yet." % timeline_get_detail_title(node)
