init -5 python:

    LIBRARY_CATEGORIES = [
        {
            "id": "characters",
            "title": "Character Profiles",
            "subtitle": "Learn about the characters in the story.",
            "icon_text": "◇",
            "screen": "library_characters",
            "requires_unlock": False,
        },
        {
            "id": "stories",
            "title": "Original Stories",
            "subtitle": "Read side stories and original materials.",
            "icon_text": "✦",
            "screen": "library_stories",
            "requires_unlock": False,
        },
        {
            "id": "cg",
            "title": "CG Gallery",
            "subtitle": "Review memorable visual moments.",
            "icon_text": "▣",
            "screen": "library_cg",
            "requires_unlock": False,
        },
        {
            "id": "music",
            "title": "Music Room",
            "subtitle": "Listen to unlocked music tracks.",
            "icon_text": "♪",
            "screen": "library_music",
            "requires_unlock": False,
        },
        {
            "id": "minigames",
            "title": "Minigames",
            "subtitle": "Replay special minigames.",
            "icon_text": "◈",
            "screen": "library_minigames",
            "requires_unlock": False,
        },
        {
            "id": "extras",
            "title": "Extras",
            "subtitle": "Bonus content and special materials.",
            "icon_text": "✧",
            "screen": "library_extras",
            "requires_unlock": False,
        },
    ]

    LIBRARY_PROGRESS_MAP = {
        "characters": "0 / 0",
        "stories": "0 / 0",
        "cg": "0 / 0",
        "music": "0 / 0",
        "minigames": "0 / 0",
        "extras": "0 / 0",
    }

    def library_category_is_unlocked(category_id):
        return True


    def library_get_progress_text(category_id):
        if category_id == "stories" and "get_story_library_progress_text" in globals():
            return get_story_library_progress_text()
        if category_id == "extras":
            unlocked = len(persistent.unlocked_secrets) if hasattr(persistent, "unlocked_secrets") and persistent.unlocked_secrets else 0
            if unlocked:
                return "%d %s" % (unlocked, _("found"))
            return _("None found")
        if category_id == "characters":
            unlocked = get_unlocked_character_count()
            total = len(CHARACTER_PROFILES)
            return "%d / %d" % (unlocked, total)
        if category_id == "music" and "get_music_library_progress_text" in globals():
            return get_music_library_progress_text()
        return LIBRARY_PROGRESS_MAP.get(category_id, "")


    def library_get_category(category_id):
        for category in LIBRARY_CATEGORIES:
            if category["id"] == category_id:
                return category

        return None


    def ui_image_or_solid(path, color):
        if renpy.loadable(path):
            return path

        return Solid(color)


    def ui_frame_or_solid(path, color, border=24):
        if renpy.loadable(path):
            return Frame(path, border, border)

        return Solid(color)


    SECRET_DEFINITIONS = {
        "secret_prologue_seen": {
            "title": "First Dream",
            "description": "Witness the dream in the rain.",
            "icon": "★",
        },
        "secret_tam_interview": {
            "title": "New Beginning",
            "description": "Get through the first job interview.",
            "icon": "★",
        },
        "secret_first_date": {
            "title": "Sunday Date",
            "description": "Experience the Sunday date with Tâm.",
            "icon": "★",
        },
    }

    def ensure_secret_defaults():
        if not hasattr(persistent, "unlocked_secrets") or persistent.unlocked_secrets is None:
            persistent.unlocked_secrets = []
        elif not isinstance(persistent.unlocked_secrets, list):
            persistent.unlocked_secrets = list(persistent.unlocked_secrets)

    ensure_secret_defaults()

    def unlock_secret(secret_id):
        ensure_secret_defaults()
        if secret_id in persistent.unlocked_secrets:
            return False
        persistent.unlocked_secrets.append(secret_id)
        renpy.save_persistent()
        secret = SECRET_DEFINITIONS.get(secret_id)
        if secret:
            renpy.notify(_("Secret found: %s") % secret.get("title", secret_id))
        return True

    def has_unlocked_secret(secret_id):
        ensure_secret_defaults()
        return secret_id in persistent.unlocked_secrets

    def get_unlocked_secrets():
        ensure_secret_defaults()
        results = []
        for secret_id in SECRET_DEFINITIONS:
            if secret_id in persistent.unlocked_secrets:
                results.append((secret_id, SECRET_DEFINITIONS[secret_id]))
        return results

    def get_unlocked_secret_count():
        ensure_secret_defaults()
        return len(persistent.unlocked_secrets)


    CHARACTER_PROFILES = [
        {
            "id": "tam",
            "name": "Nguyễn Minh Tâm",
            "route": "tam",
            "sprite": "side tam neutral",
            "description": "A gentle but perceptive young woman whose quiet warmth becomes stronger the longer people stay near her.",
            "profile": {
                "role": "Main protagonist / Tam route lead.",
                "public_identity": (
                    "Tâm is a young office worker with a soft, feminine presence. "
                    "She is not the type to dominate a room, but she leaves a steady impression through sincerity, emotional care, and quiet observation."
                ),
                "inner_layer": (
                    "Beneath her mild surface, Tâm is more sensitive and observant than she first appears. "
                    "She notices shifts in atmosphere, reads people carefully, and often understands more than she says. "
                    "Her softness is not weakness; it is her way of staying true without forcing herself into someone else's spotlight."
                ),
                "core_traits": [
                    "gentle",
                    "observant",
                    "emotionally careful",
                    "loyal",
                    "self-doubting when compared to stronger personalities",
                    "slow to open her heart fully",
                ],
                "narrative_function": (
                    "Tâm represents ordinary warmth with emotional depth. "
                    "She balances the brighter, sharper, more overwhelming presences around her and gives Hoàng's route its grounded emotional center."
                ),
                "fixed_relationships": [
                    {"target": "thienan", "type": "younger_sister"},
                    {"target": "tam_father", "type": "daughter"},
                    {"target": "tam_mother", "type": "daughter"},
                ],
                "notes": [
                    "Do not write Tâm as plain or passive. She is quiet, not empty.",
                    "Her emotional movement should be gradual: care first, trust later, confession last.",
                    "Do not store romance status here; handle it through route progression flags.",
                ],
            },
            "relationships": [
                {"target": "thienan", "type": "younger_sister"},
                {"target": "tam_father", "type": "daughter"},
                {"target": "tam_mother", "type": "daughter"},
            ],
            "tags": ["protagonist", "route", "main"],
        },

        {
            "id": "hoang",
            "name": "Huỳnh Việt Hoàng",
            "route": "hoang",
            "sprite": "side hoang neutral",
            "description": "Minh's younger brother: warm, socially sharp, charming, and more serious beneath the easy smile than most people expect.",
            "profile": {
                "role": "Main route character / Hoàng route lead.",
                "public_identity": (
                    "Hoàng appears approachable, handsome, lively, and socially natural. "
                    "Compared with Minh, he feels younger, softer, warmer, and easier to get close to."
                ),
                "inner_layer": (
                    "Hoàng grew up under the shadow of an exceptional older brother. "
                    "He carries a quiet need to prove that he can also protect, provide, and be chosen seriously. "
                    "His humor and warmth are real, but they also hide a stubborn pride and a strong protective instinct."
                ),
                "core_traits": [
                    "charming",
                    "warm",
                    "emotionally expressive",
                    "socially intelligent",
                    "protective",
                    "occasionally impulsive",
                    "sensitive about being compared to Minh",
                ],
                "narrative_function": (
                    "Hoàng is the warmer counterweight to Minh. "
                    "His route explores growing from attraction and instinct into patience, responsibility, and earned emotional steadiness."
                ),
                "fixed_relationships": [
                    {"target": "minh", "type": "younger_brother"},
                    {"target": "minh_father", "type": "son"},
                    {"target": "minh_mother", "type": "son"},
                ],
                "notes": [
                    "Do not make Hoàng merely comic relief or a lighter copy of Minh.",
                    "He should feel easier to approach than Minh, but not weaker.",
                    "His jealousy or insecurity should pass quickly into action or self-correction, not melodrama.",
                ],
            },
            "relationships": [
                {"target": "minh", "type": "younger_brother"},
                {"target": "minh_father", "type": "son"},
                {"target": "minh_mother", "type": "son"},
            ],
            "tags": ["route", "main"],
        },

        {
            "id": "yuuka",
            "name": "Nakamura Yuuka",
            "route": "yuuka",
            "sprite": "side yuuka neutral",
            "description": "A Japanese film director whose brightness hides a lifelong hunger to be understood beyond beauty, talent, and image.",
            "profile": {
                "role": "Main route character / Yuuka route lead.",
                "public_identity": (
                    "Yuuka is a striking Japanese woman from an educated, artistic family. "
                    "She becomes a filmmaker with a refined visual sense and a public image that often makes people see her as light before they see her as a person."
                ),
                "inner_layer": (
                    "Yuuka has been looked at too much and understood too little. "
                    "She wants to be seen not as a pretty symbol, but as someone sincere, interesting, flawed, and real. "
                    "Her cheerfulness is genuine, but behind it is a quiet loneliness and a deep need for emotional recognition."
                ),
                "core_traits": [
                    "bright",
                    "playful",
                    "artistically intuitive",
                    "emotionally intense",
                    "stubborn when she loves",
                    "sensitive to shallow admiration",
                    "stronger than her fragile moments suggest",
                ],
                "narrative_function": (
                    "Yuuka carries the story's tension between image and truth. "
                    "Her arc turns attention, love, artistic identity, dependence, separation, and self-reconstruction into one long emotional line."
                ),
                "fixed_relationships": [
                    {"target": "hiroshi", "type": "older_sister"},
                    {"target": "yuuka_father", "type": "daughter"},
                    {"target": "yuuka_mother", "type": "daughter"},
                ],
                "notes": [
                    "Do not reduce Yuuka to beauty or emotional dependency.",
                    "Her artistic identity is not decoration; it is part of her selfhood.",
                    "Her dialogue may be playful, but her emotional aim is often very exact.",
                ],
            },
            "relationships": [
                {"target": "hiroshi", "type": "older_sister"},
                {"target": "yuuka_father", "type": "daughter"},
                {"target": "yuuka_mother", "type": "daughter"},
            ],
            "tags": ["route", "main"],
        },

        {
            "id": "minh",
            "name": "Huỳnh Nhật Minh",
            "route": "minh",
            "sprite": "side minh neutral",
            "description": "A brilliant, restrained man shaped by responsibility, power, and the habit of protecting others before himself.",
            "profile": {
                "role": "Main route character / Minh route lead.",
                "public_identity": (
                    "Minh appears calm, educated, intelligent, disciplined, and almost unnervingly capable. "
                    "He rarely advertises his ability, but people sense that he understands more than he says."
                ),
                "inner_layer": (
                    "Minh's composure was not born from ease. "
                    "It was shaped by early responsibility, family pressure, political entanglement, and the need to become valuable enough that no one could easily control him or use his loved ones against him."
                ),
                "hidden_identity": (
                    "Minh has layers of influence beyond his public face. "
                    "Aliases such as Alex, Liptoner, and Itsukimori should be treated as identity layers or operational traces of Minh, not separate characters unless the UI specifically needs alias entries."
                ),
                "core_traits": [
                    "strategic",
                    "disciplined",
                    "emotionally restrained",
                    "protective",
                    "over-responsible",
                    "quietly tender",
                    "dangerous when forced into a corner",
                ],
                "narrative_function": (
                    "Minh is the story's axis of restraint, responsibility, and painful love. "
                    "He often chooses the difficult solution because he sees further than others, but that same habit can make him cruel by accident."
                ),
                "fixed_relationships": [
                    {"target": "hoang", "type": "older_brother"},
                    {"target": "minh_father", "type": "son"},
                    {"target": "minh_mother", "type": "son"},
                ],
                "aliases": ["Alex", "Liptoner", "Itsukimori"],
                "notes": [
                    "Do not write Minh as emotionless. He feels deeply, then controls the visible damage.",
                    "He loves through preparation, protection, and systems more than declarations.",
                    "His greatest flaw is deciding alone what pain is necessary.",
                ],
            },
            "relationships": [
                {"target": "hoang", "type": "older_brother"},
                {"target": "minh_father", "type": "son"},
                {"target": "minh_mother", "type": "son"},
            ],
            "tags": ["route", "main"],
        },

        {
            "id": "thienan",
            "name": "Nguyễn Thiên An",
            "route": "tam",
            "sprite": "side thienan neutral",
            "description": "Tâm's elder sister: elegant, capable, and raised to carry expectation with a straight back and very little complaint.",
            "profile": {
                "role": "Major character / Thiên An route candidate.",
                "public_identity": (
                    "Thiên An is the eldest daughter of a successful business family. "
                    "She is intelligent, elegant, competitive, and used to being seen as capable before being seen as tired."
                ),
                "inner_layer": (
                    "Under her polished surface is someone who has been trained to succeed and expected to inherit. "
                    "She is proud, but not shallow; strong, but not unbreakable. "
                    "Her tenderness often appears through control, practical help, or a carefully timed question."
                ),
                "core_traits": [
                    "ambitious",
                    "composed",
                    "competitive",
                    "elegant",
                    "protective in a restrained way",
                    "emotionally guarded",
                    "burdened by expectation",
                ],
                "narrative_function": (
                    "Thiên An shows what happens when excellence becomes both armor and cage. "
                    "She contrasts Tâm's softness with a sharper, more trained form of womanhood."
                ),
                "fixed_relationships": [
                    {"target": "tam", "type": "older_sister"},
                    {"target": "tam_father", "type": "daughter"},
                    {"target": "tam_mother", "type": "daughter"},
                ],
                "notes": [
                    "Do not write Thiên An as merely cold or superior.",
                    "Her control should feel learned, not natural arrogance.",
                    "She speaks less emotionally than she feels.",
                ],
            },
            "relationships": [
                {"target": "tam", "type": "older_sister"},
                {"target": "tam_father", "type": "daughter"},
                {"target": "tam_mother", "type": "daughter"},
            ],
            "tags": ["route", "main"],
        },

        {
            "id": "huyen",
            "name": "Lê Thị Huyền",
            "route": "tam",
            "sprite": "side huyen neutral",
            "description": "Tâm's close friend: frank, socially alert, and often the person who says the thing Tâm is still trying to swallow.",
            "profile": {
                "role": "Close friend / supporting route candidate.",
                "public_identity": (
                    "Huyền is Tâm's close friend and social counterweight. "
                    "She is more outwardly direct, more willing to tease, and quicker to read a room from the practical side."
                ),
                "inner_layer": (
                    "Huyền's liveliness should not be treated as shallowness. "
                    "She often protects emotional balance by making things lighter, but she also knows when not to intrude."
                ),
                "core_traits": [
                    "direct",
                    "witty",
                    "socially perceptive",
                    "loyal",
                    "playful",
                    "pragmatic",
                ],
                "narrative_function": (
                    "Huyền keeps Tâm's scenes from becoming too inward. "
                    "She adds movement, teasing pressure, and friend-level honesty without stealing the emotional center."
                ),
                "fixed_relationships": [],
                "notes": [
                    "Use Huyền to tease, deflect, or puncture tension.",
                    "Do not let her become a noisy sidekick. Her timing matters.",
                ],
            },
            "relationships": [],
            "tags": ["route", "main", "friend"],
        },

        {
            "id": "quan",
            "name": "Trần Quốc Quân",
            "route": "tam",
            "sprite": "side quan neutral",
            "description": "A demanding senior at work whose standards are high enough to frighten people before they learn why he keeps them.",
            "profile": {
                "role": "Workplace supporting character.",
                "public_identity": (
                    "Quân is known at work as capable, strict, sharp-eyed, and difficult to impress. "
                    "He dislikes shallow performance and notices weak preparation quickly."
                ),
                "inner_layer": (
                    "Quân's strictness should come from professional seriousness, not petty cruelty. "
                    "He may be hard to please, but he respects genuine effort and competence."
                ),
                "core_traits": [
                    "strict",
                    "competent",
                    "observant",
                    "professional",
                    "dry",
                    "fair when earned",
                ],
                "narrative_function": (
                    "Quân gives the workplace arc pressure and structure. "
                    "He is useful as a standard-setter, a gatekeeper, and sometimes an unwilling source of recognition."
                ),
                "fixed_relationships": [],
                "notes": [
                    "Prioritize the current game canon: Quân as a demanding workplace senior/manager.",
                    "Avoid making him simply warm and reliable unless the scene has earned that reveal.",
                ],
            },
            "relationships": [],
            "tags": ["supporting", "workplace"],
        },

        {
            "id": "akiko",
            "name": "Kobayashi Akiko",
            "route": "yuuka",
            "sprite": "side akiko neutral",
            "description": "Yuuka's closest friend: quiet, film-obsessed, emotionally safe, and sharper than her soft manner first suggests.",
            "profile": {
                "role": "Yuuka's close friend / Japan-side supporting character.",
                "public_identity": (
                    "Akiko is small, quiet, gentle, and reserved. "
                    "At first glance she can seem timid, but when she speaks about cinema, her whole presence brightens."
                ),
                "inner_layer": (
                    "Akiko understands Yuuka without turning her into an object of admiration. "
                    "She gives Yuuka a place where she does not need to perform brightness, beauty, or perfection."
                ),
                "core_traits": [
                    "quiet",
                    "gentle",
                    "film-obsessed",
                    "emotionally perceptive",
                    "safe",
                    "subtly firm",
                ],
                "narrative_function": (
                    "Akiko is Yuuka's emotional witness. "
                    "She anchors Yuuka's Japan-side life and often reflects changes Yuuka cannot yet name."
                ),
                "fixed_relationships": [
                    {"target": "tetsuya", "type": "wife"},
                ],
                "notes": [
                    "Akiko should not be written as merely shy.",
                    "Her quietness contains judgment, taste, and emotional precision.",
                ],
            },
            "relationships": [
                {"target": "tetsuya", "type": "wife"},
            ],
            "tags": ["supporting", "friend", "japan_arc"],
        },

        {
            "id": "tetsuya",
            "name": "Fujimoto Tetsuya",
            "route": None,
            "sprite": "side tetsuya neutral",
            "description": "Akiko's husband: ordinary in the best way, attentive through small domestic gestures rather than dramatic words.",
            "profile": {
                "role": "Japan-side supporting character.",
                "public_identity": (
                    "Tetsuya is Akiko's husband and part of the quiet domestic life Yuuka returns to after separation. "
                    "He is not flashy, but his care is steady and visible in small routines."
                ),
                "inner_layer": (
                    "Tetsuya's presence matters because he turns ordinary life into something warm and inhabited. "
                    "His care for Akiko becomes a mirror that makes Yuuka notice what she has lost."
                ),
                "core_traits": [
                    "steady",
                    "domestic",
                    "attentive",
                    "low-key",
                    "kind",
                    "practical",
                ],
                "narrative_function": (
                    "Tetsuya is a mirror character. "
                    "Through his everyday care for Akiko, Yuuka is forced to recognize the shape of absence in her own life."
                ),
                "fixed_relationships": [
                    {"target": "akiko", "type": "husband"},
                ],
                "notes": [
                    "Keep him ordinary, not bland.",
                    "His best scenes should work through small domestic actions.",
                ],
            },
            "relationships": [
                {"target": "akiko", "type": "husband"},
            ],
            "tags": ["supporting", "japan_arc"],
        },

        {
            "id": "hiroshi",
            "name": "Nakamura Hiroshi",
            "route": None,
            "sprite": "side hiroshi neutral",
            "description": "Yuuka's younger brother, whose existence quietly changed Yuuka's place in the family without breaking her love for him.",
            "profile": {
                "role": "Family supporting character.",
                "public_identity": (
                    "Hiroshi is Yuuka's younger brother and the second child of the Nakamura family."
                ),
                "inner_layer": (
                    "Hiroshi is not Yuuka's enemy or rival in a simple sense. "
                    "His birth shifted Yuuka away from the emotional center of the family, creating a quiet wound without destroying sibling affection."
                ),
                "core_traits": [
                    "younger sibling",
                    "family anchor",
                    "unintentional emotional catalyst",
                ],
                "narrative_function": (
                    "Hiroshi helps explain Yuuka's old feeling of being gently displaced rather than openly abandoned."
                ),
                "fixed_relationships": [
                    {"target": "yuuka", "type": "younger_brother"},
                    {"target": "yuuka_father", "type": "son"},
                    {"target": "yuuka_mother", "type": "son"},
                ],
                "notes": [
                    "Do not make Hiroshi the cause of family cruelty.",
                    "The wound is subtle: Yuuka loves him, but her place in the family changed.",
                ],
            },
            "relationships": [
                {"target": "yuuka", "type": "younger_brother"},
                {"target": "yuuka_father", "type": "son"},
                {"target": "yuuka_mother", "type": "son"},
            ],
            "tags": ["supporting", "family", "japan_arc"],
        },

        {
            "id": "ayumi",
            "name": "Shimura Ayumi",
            "route": None,
            "sprite": "side ayumi neutral",
            "description": "A sharp, elegant rival-turned-colleague whose competence makes every room feel slightly more exacting.",
            "profile": {
                "role": "Rival / colleague / Japan-side recurring character.",
                "public_identity": (
                    "Shimura Ayumi is precise, elegant, professionally respected, and difficult to dismiss. "
                    "She has the kind of competence that enters a room before she speaks."
                ),
                "inner_layer": (
                    "Ayumi is not merely a rival. "
                    "She understands excellence, respects people who earn their place, and recognizes emotional truths without always naming them directly."
                ),
                "core_traits": [
                    "sharp",
                    "elegant",
                    "ambitious",
                    "professionally credible",
                    "composed",
                    "hard to impress",
                    "capable of respect without softness",
                ],
                "narrative_function": (
                    "Ayumi reflects the version of Yuuka who must compete, refine herself, and stand without relying on emotional shelter. "
                    "Her reappearance in Japan should evoke both rivalry and the shadow of Minh."
                ),
                "fixed_relationships": [],
                "notes": [
                    "Use confirmed surname: Shimura.",
                    "Do not write Ayumi as petty. Her pressure should come from competence.",
                    "Her relationship with Yuuka should carry rivalry, history, respect, and uncomfortable recognition.",
                ],
            },
            "relationships": [],
            "tags": ["supporting", "rival", "japan_arc", "film"],
        },

        {
            "id": "lisa",
            "name": "Lisa Bennett",
            "route": None,
            "sprite": "side lisa neutral",
            "description": "A film-school friend with a dry eye for emotional tension and a useful habit of saying what others avoid.",
            "profile": {
                "role": "Film-school supporting character.",
                "public_identity": (
                    "Lisa is part of Yuuka's film-school circle. "
                    "She is observant, casually sharp, and often reads romantic or interpersonal tension faster than the people involved."
                ),
                "inner_layer": (
                    "Lisa's teasing works because it is grounded in perception. "
                    "She may sound casual, but she usually sees the emotional angle clearly."
                ),
                "core_traits": [
                    "dry-witted",
                    "observant",
                    "casual",
                    "emotionally sharp",
                    "socially unafraid",
                ],
                "narrative_function": (
                    "Lisa helps expose subtext in the film-school arc without turning it into heavy explanation."
                ),
                "fixed_relationships": [],
                "notes": [
                    "Keep her dialogue short, modern, and lightly teasing.",
                    "She should puncture tension, not hijack it.",
                ],
            },
            "relationships": [],
            "tags": ["supporting", "film", "school_arc"],
        },

        {
            "id": "takashi",
            "name": "Kuroda Takashi",
            "route": None,
            "sprite": "side takashi neutral",
            "description": "A film-school peer drawn to experimental ideas, often drifting at the edge of the group like someone half inside his own soundtrack.",
            "profile": {
                "role": "Film-school supporting character.",
                "public_identity": (
                    "Takashi is a member of Yuuka's film-school group, associated with experimental sound and unconventional project ideas."
                ),
                "inner_layer": (
                    "Takashi works best as a texture character: present enough to shape group rhythm, but not so loud that he pulls focus from the core emotional arc."
                ),
                "core_traits": [
                    "experimental",
                    "quietly eccentric",
                    "music-aware",
                    "independent",
                    "slightly detached",
                ],
                "narrative_function": (
                    "Takashi broadens the film-school world and gives group scenes a different creative angle."
                ),
                "fixed_relationships": [],
                "notes": [
                    "Do not overuse him unless a chapter needs group-project dynamics.",
                    "He can be useful for sound, editing, or production tension.",
                ],
            },
            "relationships": [],
            "tags": ["supporting", "film", "school_arc"],
        },

        {
            "id": "duyen",
            "name": "Phạm Khánh Duyên",
            "route": None,
            "sprite": "side duyen neutral",
            "description": "A careful, sensitive figure from Minh and Thiên An's youth, marked by quiet insecurity and the need to find her own place.",
            "profile": {
                "role": "Past arc supporting character.",
                "public_identity": (
                    "Duyên belongs to Minh and Thiên An's school-years circle. "
                    "She is attentive, careful, and often more affected by comparison than she wants to admit."
                ),
                "inner_layer": (
                    "Duyên's wound is the fear of being the smaller presence beside people who seem brighter, sharper, or more necessary. "
                    "She is not weak, but she can mistake quietness for inadequacy."
                ),
                "core_traits": [
                    "sensitive",
                    "careful",
                    "insecure",
                    "loyal",
                    "detail-oriented",
                    "emotionally restrained",
                ],
                "narrative_function": (
                    "Duyên gives the youth arc a softer emotional fracture: not grand tragedy, but the pain of feeling unnecessary beside exceptional people."
                ),
                "fixed_relationships": [
                    {"target": "kim", "type": "wife"},
                ],
                "notes": [
                    "Do not write Duyên as jealous in a shallow way.",
                    "Her insecurity should feel quiet, accumulated, and believable.",
                ],
            },
            "relationships": [
                {"target": "kim", "type": "wife"},
            ],
            "tags": ["supporting", "past_arc"],
        },

        {
            "id": "kim",
            "name": "Phạm Gia Kim",
            "route": None,
            "sprite": "side kim neutral",
            "description": "A perceptive friend from Minh's youth, warm enough to mediate and patient enough to stay beside wounded people.",
            "profile": {
                "role": "Past arc supporting character.",
                "public_identity": (
                    "Kim is part of the school-years circle around Minh, Thiên An, and Duyên. "
                    "He is socially perceptive, often the one who notices when the group has started to fracture."
                ),
                "inner_layer": (
                    "Kim's warmth is active rather than decorative. "
                    "He tries to repair distance, ease insecurity, and give others room without forcing them."
                ),
                "core_traits": [
                    "perceptive",
                    "warm",
                    "patient",
                    "mediating",
                    "emotionally generous",
                    "quietly persistent",
                ],
                "narrative_function": (
                    "Kim functions as the emotional mediator of the youth arc and later as proof that patient care can become a life path, not just a temporary comfort."
                ),
                "fixed_relationships": [
                    {"target": "duyen", "type": "husband"},
                ],
                "notes": [
                    "Kim should feel kind, not naïve.",
                    "His patience should have dignity, not desperation.",
                ],
            },
            "relationships": [
                {"target": "duyen", "type": "husband"},
            ],
            "tags": ["supporting", "past_arc"],
        },

        {
            "id": "minh_father",
            "name": "Huỳnh Phi Hùng",
            "route": None,
            "sprite": "side minh_father neutral",
            "description": "Minh and Hoàng's father: a military man whose stern discipline hides practical, understated warmth.",
            "profile": {
                "role": "Family supporting character.",
                "public_identity": (
                    "Huỳnh Phi Hùng is Minh and Hoàng's father, a senior military figure with a strict, disciplined bearing."
                ),
                "inner_layer": (
                    "His warmth is not verbal or decorative. "
                    "He teaches through habits, discipline, and practical lessons, giving his sons a sense of structure and endurance."
                ),
                "core_traits": [
                    "disciplined",
                    "stern",
                    "practical",
                    "quietly warm",
                    "principled",
                    "protective",
                ],
                "narrative_function": (
                    "He forms the disciplined half of Minh and Hoàng's family foundation."
                ),
                "fixed_relationships": [
                    {"target": "minh_mother", "type": "husband"},
                    {"target": "minh", "type": "father"},
                    {"target": "hoang", "type": "father"},
                ],
                "notes": [
                    "Use confirmed name: Huỳnh Phi Hùng.",
                    "Do not make him emotionally verbose.",
                ],
            },
            "relationships": [
                {"target": "minh_mother", "type": "husband"},
                {"target": "minh", "type": "father"},
                {"target": "hoang", "type": "father"},
            ],
            "tags": ["supporting", "family"],
        },

        {
            "id": "minh_mother",
            "name": "Bùi Thị Kim Liên",
            "route": None,
            "sprite": "side minh_mother neutral",
            "description": "Minh and Hoàng's mother: a high-ranking political figure whose softness and authority are both real.",
            "profile": {
                "role": "Family / political supporting character.",
                "public_identity": (
                    "Bùi Thị Kim Liên is Minh and Hoàng's mother, a senior political figure with composure, influence, and controlled grace."
                ),
                "inner_layer": (
                    "She is decisive without losing softness. "
                    "Her love is often expressed through protection, preparation, and hard choices rather than open emotional display."
                ),
                "core_traits": [
                    "decisive",
                    "politically sharp",
                    "composed",
                    "subtly warm",
                    "protective",
                    "strategic",
                ],
                "narrative_function": (
                    "She is central to Minh's political wound and to his understanding that love, power, and sacrifice can become dangerously entangled."
                ),
                "fixed_relationships": [
                    {"target": "minh_father", "type": "wife"},
                    {"target": "minh", "type": "mother"},
                    {"target": "hoang", "type": "mother"},
                ],
                "notes": [
                    "Use confirmed name: Bùi Thị Kim Liên.",
                    "Her authority should be calm, not theatrical.",
                ],
            },
            "relationships": [
                {"target": "minh_father", "type": "wife"},
                {"target": "minh", "type": "mother"},
                {"target": "hoang", "type": "mother"},
            ],
            "tags": ["supporting", "family", "political"],
        },

        {
            "id": "tam_father",
            "name": "Nguyễn Đức Thành",
            "route": None,
            "sprite": "side tam_father neutral",
            "description": "The father of Thiên An and Tâm, representing the family's business expectations and quiet pressure.",
            "profile": {
                "role": "Family supporting character.",
                "public_identity": (
                    "Nguyễn Đức Thành is the father of Thiên An and Tâm, connected to the business-family structure that shaped Thiên An's upbringing."
                ),
                "inner_layer": (
                    "He should represent expectation more than cruelty. "
                    "His presence matters because the family standard presses differently on each daughter."
                ),
                "core_traits": [
                    "business-minded",
                    "expectant",
                    "practical",
                    "status-aware",
                    "family-oriented",
                ],
                "narrative_function": (
                    "He helps define the family pressure behind Thiên An's discipline and Tâm's quieter position."
                ),
                "fixed_relationships": [
                    {"target": "tam_mother", "type": "husband"},
                    {"target": "thienan", "type": "father"},
                    {"target": "tam", "type": "father"},
                ],
                "notes": [
                    "Name is provisional until canon says otherwise.",
                    "Avoid turning him into a simple villain.",
                ],
            },
            "relationships": [
                {"target": "tam_mother", "type": "husband"},
                {"target": "thienan", "type": "father"},
                {"target": "tam", "type": "father"},
            ],
            "tags": ["supporting", "family"],
        },

        {
            "id": "tam_mother",
            "name": "Đặng Thu Hà",
            "route": None,
            "sprite": "side tam_mother neutral",
            "description": "The mother of Thiên An and Tâm, whose concern often arrives dressed as pressure.",
            "profile": {
                "role": "Family supporting character.",
                "public_identity": (
                    "Đặng Thu Hà is the mother of Thiên An and Tâm. "
                    "She is part of the domestic pressure around marriage, family standing, and what a daughter should become."
                ),
                "inner_layer": (
                    "Her pressure should not be written as pure malice. "
                    "She can care and still wound; she can worry and still push too hard."
                ),
                "core_traits": [
                    "concerned",
                    "status-aware",
                    "pressuring",
                    "family-focused",
                    "emotionally indirect",
                ],
                "narrative_function": (
                    "She gives the Thiên An/Tâm family scenes their domestic tension and reveals how different the two sisters' burdens are."
                ),
                "fixed_relationships": [
                    {"target": "tam_father", "type": "wife"},
                    {"target": "thienan", "type": "mother"},
                    {"target": "tam", "type": "mother"},
                ],
                "notes": [
                    "Name is provisional until canon says otherwise.",
                    "Her conflict should feel domestic and believable, not cartoonish.",
                ],
            },
            "relationships": [
                {"target": "tam_father", "type": "wife"},
                {"target": "thienan", "type": "mother"},
                {"target": "tam", "type": "mother"},
            ],
            "tags": ["supporting", "family"],
        },

        {
            "id": "yuuka_father",
            "name": "Nakamura Seiji",
            "route": None,
            "sprite": "side yuuka_father neutral",
            "description": "Yuuka and Hiroshi's father, a scholar of classical Japanese literature and a pillar of the Nakamura family's refined expectations.",
            "profile": {
                "role": "Family supporting character.",
                "public_identity": (
                    "Nakamura Seiji is Yuuka and Hiroshi's father, a professor of classical Japanese literature."
                ),
                "inner_layer": (
                    "He represents the intellectual and traditional side of the Nakamura household: refined, cultivated, and quietly demanding."
                ),
                "core_traits": [
                    "scholarly",
                    "traditional",
                    "cultivated",
                    "reserved",
                    "expectant",
                ],
                "narrative_function": (
                    "He helps define the atmosphere of beauty, culture, rules, and expectation that shaped Yuuka."
                ),
                "fixed_relationships": [
                    {"target": "yuuka_mother", "type": "husband"},
                    {"target": "yuuka", "type": "father"},
                    {"target": "hiroshi", "type": "father"},
                ],
                "notes": [
                    "Name is provisional until canon says otherwise.",
                    "Do not make him cold by default; restraint is not the same as lack of love.",
                ],
            },
            "relationships": [
                {"target": "yuuka_mother", "type": "husband"},
                {"target": "yuuka", "type": "father"},
                {"target": "hiroshi", "type": "father"},
            ],
            "tags": ["supporting", "family", "japan_arc"],
        },

        {
            "id": "yuuka_mother",
            "name": "Nakamura Reiko",
            "route": None,
            "sprite": "side yuuka_mother neutral",
            "description": "Yuuka and Hiroshi's mother, an art lecturer whose elegance and standards helped shape Yuuka's sense of beauty and restraint.",
            "profile": {
                "role": "Family supporting character.",
                "public_identity": (
                    "Nakamura Reiko is Yuuka and Hiroshi's mother, an art lecturer with a refined presence and strong aesthetic sense."
                ),
                "inner_layer": (
                    "She is graceful and caring, but the care comes within a framework of manners, expectation, and cultivated self-control."
                ),
                "core_traits": [
                    "elegant",
                    "artistic",
                    "composed",
                    "standard-setting",
                    "quietly caring",
                ],
                "narrative_function": (
                    "She helps explain Yuuka's aesthetics, discipline, and discomfort with always having to be the correct version of herself."
                ),
                "fixed_relationships": [
                    {"target": "yuuka_father", "type": "wife"},
                    {"target": "yuuka", "type": "mother"},
                    {"target": "hiroshi", "type": "mother"},
                ],
                "notes": [
                    "Name is provisional until canon says otherwise.",
                    "Her warmth should exist, but filtered through family culture and form.",
                ],
            },
            "relationships": [
                {"target": "yuuka_father", "type": "wife"},
                {"target": "yuuka", "type": "mother"},
                {"target": "hiroshi", "type": "mother"},
            ],
            "tags": ["supporting", "family", "japan_arc"],
        },
    ]

    def unlock_library_character(character_id):
        if not hasattr(persistent, "unlocked_library_characters") or persistent.unlocked_library_characters is None:
            persistent.unlocked_library_characters = []
        if character_id not in persistent.unlocked_library_characters:
            persistent.unlocked_library_characters.append(character_id)


    def unlock_character_section(character_id, section_key):
        if not hasattr(persistent, "unlocked_character_sections") or persistent.unlocked_character_sections is None:
            persistent.unlocked_character_sections = []
        entry = "%s.%s" % (character_id, section_key)
        if entry not in persistent.unlocked_character_sections:
            persistent.unlocked_character_sections.append(entry)


    def is_character_unlocked(profile):
        if profile.get("route") is None:
            return True

        cid = profile["id"]
        if not hasattr(persistent, "unlocked_library_characters"):
            return False
        if not isinstance(persistent.unlocked_library_characters, list):
            return False
        return cid in persistent.unlocked_library_characters


    def is_character_section_unlocked(character_id, section_key):
        # role and public_identity are always visible when the character is unlocked
        always_visible = ["role", "public_identity"]
        if section_key in always_visible:
            return True
        entry = "%s.%s" % (character_id, section_key)
        if not hasattr(persistent, "unlocked_character_sections"):
            return False
        if not isinstance(persistent.unlocked_character_sections, list):
            return False
        return entry in persistent.unlocked_character_sections


    def get_unlocked_character_count():
        count = 0
        for profile in CHARACTER_PROFILES:
            if is_character_unlocked(profile):
                count += 1
        return count
