# FILE: game/map/map_location_interactions.rpy
# Data-driven location hubs, free-time actions, and lightweight minigame entry points.
# Keep this file loaded together with map_data.rpy/map_logic.rpy/map_hub.rpy/map_screen.rpy.

init -2 python:

    MAP_LOCATION_ACTIONS = {
        "tam_apartment": [
            {
                "id": "tam_home_rest",
                "title": "Rest at home",
                "summary": "Recover energy and lower stress. Safe, but consumes free time.",
                "category": "Rest",
                "time_cost": 1,
                "effects": {"time_units": -1, "energy": 18, "stress": -10, "mood": 4},
                "messages": [
                    "Tâm ở nhà nghỉ một lúc. Căn phòng yên lại, và nhịp thở của cô cũng chậm xuống theo.",
                    "Tâm kéo rèm lại một nửa, để căn phòng bớt sáng. Không phải trốn đời. Chỉ là tạm nghỉ giao tiếp với nó.",
                    "Điện thoại úp xuống bàn. Mười phút không kiểm tra tin nhắn. Một chiến thắng nhỏ, nhưng vẫn là chiến thắng.",
                ],
            },
            {
                "id": "tam_home_cook_meal",
                "title": "Cook a simple meal",
                "summary": "Use groceries to cook. Saves money, improves cooking/life skills, and supports health.",
                "category": "Home",
                "time_cost": 1,
                "requires": {"inventory": {"groceries": 1}, "time_units": 1},
                "effects": {"time_units": -1, "energy": -4, "health": 5, "mood": 5, "cooking_skill": 3, "life_skill": 2},
                "inventory_effects": {"groceries": -1},
                "story_effects": {"tam_self_clarity": 1},
                "message": "Một bữa cơm đơn giản. Không hào nhoáng, nhưng đủ làm căn bếp có mùi của một ngày được chăm sóc tử tế.",
            },
            {
                "id": "tam_home_housekeeping",
                "title": "Clean and organize the room",
                "summary": "Small domestic task. Improves life skill and lowers stress if not overdone.",
                "category": "Home",
                "time_cost": 1,
                "effects": {"time_units": -1, "energy": -6, "stress": -6, "life_skill": 2, "mood": 2},
                "message": "Tâm gấp lại vài bộ đồ, kéo chiếc kẹp giấy về đúng mép hồ sơ. Một việc nhỏ, nhưng đầu óc cô nhẹ hơn.",
            },
        ],

        "foodie_street": [
            {
                "id": "foodie_snack_walk",
                "title": "Go snack-hopping",
                "summary": "Cheap joy. Lowers stress and boosts mood, but has a small stomach-risk.",
                "category": "Food",
                "money_cost": 120000,
                "time_cost": 1,
                "requires": {"money": 120000, "time_units": 1},
                "effects": {"money": -120000, "time_units": -1, "mood": 9, "stress": -5, "health": -1},
                "risk": {
                    "chance": 0.08,
                    "messages": [
                        "Có vẻ xiên cuối cùng hơi liều. Tâm thấy bụng mình phản đối khá có văn bản.",
                        "Tâm nhìn que xiên rỗng trên tay và bắt đầu nghi ngờ năng lực ra quyết định của mình.",
                    ],
                    "effects": {"health": -12, "stress": 5, "mood": -3},
                    "flags": ["minor_stomach_ache"],
                },
                "messages": [
                    "Đồ ăn vặt thì không giải quyết đời người. Nhưng trong mười lăm phút đầu, nó giả vờ khá thuyết phục.",
                    "Tâm đi qua ba quầy hàng, tự nhủ chỉ ăn một chút. Một chút sau đó cần thêm một túi giấy.",
                    {
                        "text": "Tâm mua thêm một phần cho Huyền, rồi tự nói là tiện đường thôi. Lý do nghe mỏng, nhưng túi đồ thì khá thật.",
                        "weight": 1,
                        "min_scores": {"tam_observation": 2},
                    },
                ],
            },
            {
                "id": "foodie_buy_groceries",
                "title": "Buy groceries",
                "summary": "Spend money now to cook later at home. Unlocks economical meals.",
                "category": "Errand",
                "money_cost": 220000,
                "time_cost": 1,
                "requires": {"money": 220000, "time_units": 1},
                "effects": {"money": -220000, "time_units": -1, "life_skill": 1},
                "inventory_effects": {"groceries": 2},
                "message": "Hai túi thực phẩm không nặng lắm, nhưng đủ khiến bữa tối ở nhà có lý do để tồn tại.",
            },
            {
                "id": "foodie_part_time_evening",
                "title": "Part-time: evening food stall",
                "summary": "Earn quick money, but costs energy and can hurt health/work focus if abused.",
                "category": "Part-time",
                "time_cost": 4,
                "requires": {"time_units": 4, "energy_min": 25},
                "conditions": ["completed:tam_c01_interview_day"],
                "effects": {"money": 450000, "time_units": -4, "energy": -20, "stress": 7, "mood": -1, "life_skill": 2},
                "overwork_sensitive": True,
                "message": "Ca làm thêm kết thúc khi phố đã lên đèn. Tiền trong ví dày hơn một chút. Vai thì không hào hứng như vậy.",
            },
        ],

        "shopping_area": [
            {
                "id": "shopping_office_clothes",
                "title": "Buy elegant office clothes",
                "summary": "Improves confidence, style, and professional presence.",
                "category": "Shopping",
                "money_cost": 650000,
                "time_cost": 1,
                "requires": {"money": 650000, "time_units": 1},
                "effects": {"money": -650000, "time_units": -1, "confidence": 5, "style": 4, "mood": 3},
                "story_effects": {"career_tam": 1},
                "flags": ["tam_has_elegant_office_clothes"],
                "message": "Bộ đồ không làm Tâm thành người khác. Nó chỉ khiến cô đứng thẳng hơn một chút khi bước vào văn phòng.",
            },
            {
                "id": "shopping_party_dress",
                "title": "Buy a party dress",
                "summary": "Expensive, but gives a strong confidence/style boost for social events.",
                "category": "Shopping",
                "money_cost": 1250000,
                "time_cost": 1,
                "requires": {"money": 1250000, "time_units": 1},
                "effects": {"money": -1250000, "time_units": -1, "confidence": 7, "style": 8, "mood": 4},
                "flags": ["tam_has_party_dress"],
                "message": "Chiếc váy được đặt vào túi giấy rất gọn. Tâm cầm lấy, tự dưng thấy buổi tiệc sắp tới bớt đáng sợ hơn.",
            },
            {
                "id": "shopping_buy_books",
                "title": "Buy books and work materials",
                "summary": "Costs money, improves knowledge and work skill.",
                "category": "Shopping",
                "money_cost": 280000,
                "time_cost": 1,
                "requires": {"money": 280000, "time_units": 1},
                "effects": {"money": -280000, "time_units": -1, "knowledge": 3, "work_skill": 2},
                "story_effects": {"career_tam": 1},
                "message": "Vài cuốn sách mới nằm yên trong túi. Kiến thức chưa tăng ngay, nhưng lương tâm nghề nghiệp thì có vẻ đã thức dậy.",
            },
            {
                "id": "shopping_part_time_promo",
                "title": "Part-time: promotion booth",
                "summary": "Earn money and social confidence, but drains energy.",
                "category": "Part-time",
                "time_cost": 2,
                "requires": {"time_units": 2, "energy_min": 30},
                "effects": {"money": 320000, "time_units": -2, "energy": -18, "stress": 6, "confidence": 2, "style": 1},
                "overwork_sensitive": True,
                "message": "Hai giờ đứng booth làm nụ cười của Tâm hơi cứng lại. Nhưng ví tiền thì tươi hơn. Công bằng một cách khó chịu.",
            },
        ],

        "library": [
            {
                "id": "library_read_general",
                "title": "Read quietly",
                "summary": "Increases knowledge and mood. Low cost, moderate time.",
                "category": "Study",
                "time_cost": 1,
                "requires": {"time_units": 1},
                "effects": {"time_units": -1, "knowledge": 4, "mood": 2, "energy": -4, "stress": -2},
                "message": "Một trang sách lật qua. Ngoài kia vẫn ồn. Trong này, mọi thứ biết giữ giọng nhỏ hơn.",
            },
            {
                "id": "library_study_work_skill",
                "title": "Study for work",
                "summary": "Improves work skill and career momentum, but increases stress slightly.",
                "category": "Study",
                "time_cost": 2,
                "requires": {"time_units": 2, "energy_min": 20},
                "effects": {"time_units": -2, "work_skill": 5, "knowledge": 2, "energy": -8, "stress": 4},
                "story_effects": {"career_tam": 1},
                "message": "Tâm ghi thêm vài dòng vào sổ. Chữ hơi nhỏ lại ở cuối trang, nhưng ý thì rõ hơn.",
            },
            {
                "id": "library_part_time_assistant",
                "title": "Part-time: library assistant",
                "summary": "A safer part-time job. Earns less, but also improves knowledge.",
                "category": "Part-time",
                "time_cost": 4,
                "requires": {"time_units": 4, "energy_min": 25},
                "effects": {"money": 360000, "time_units": -4, "energy": -12, "stress": 3, "knowledge": 2, "life_skill": 1},
                "overwork_sensitive": True,
                "message": "Sắp sách lên kệ không lãng mạn lắm. Nhưng ít nhất sách không bắt cô phải cười với khách hàng.",
            },
        ],

        "park": [
            {
                "id": "park_walk",
                "title": "Take a walk",
                "summary": "Low effort. Reduces stress and improves mood.",
                "category": "Rest",
                "time_cost": 1,
                "requires": {"time_units": 1},
                "effects": {"time_units": -1, "stress": -7, "mood": 5, "health": 2, "energy": -2},
                "message": "Tâm đi một vòng quanh công viên. Không có chuyện gì lớn xảy ra. Chỉ có vai cô bớt căng đi một chút.",
            },
            {
                "id": "park_jog",
                "title": "Light jogging",
                "summary": "Improves health, costs energy.",
                "category": "Health",
                "time_cost": 1,
                "requires": {"time_units": 1, "energy_min": 15},
                "effects": {"time_units": -1, "health": 5, "energy": -9, "stress": -3, "mood": 2},
                "message": "Mấy vòng chạy nhẹ khiến chân hơi mỏi. Nhưng đầu óc thì bớt mắc kẹt trong những thứ không gọi tên được.",
            },
        ],

        "company": [
            {
                "id": "company_overtime_training",
                "title": "Stay late for self-training",
                "summary": "Boosts career/work skill, but high stress and overwork risk.",
                "category": "Work",
                "time_cost": 4,
                "requires": {"time_units": 4, "energy_min": 30},
                "effects": {"time_units": -4, "energy": -18, "stress": 10, "work_skill": 4, "knowledge": 1},
                "story_effects": {"career_tam": 2},
                "overwork_sensitive": True,
                "message": "Văn phòng muộn có thứ ánh sáng hơi lạnh. Tâm lưu file lần cuối, rồi mới nhận ra vai mình đã cứng từ lúc nào.",
            },
        ],
    }


init -1 python:


    # Ensure this file can be loaded safely even if Ren'Py changes file order.
    # In the normal project, map_data.rpy defines these before this file.
    if "FIXED_MAP_LOCATIONS" not in globals():
        FIXED_MAP_LOCATIONS = {}

    # -------------------------------------------------------------------------
    # Location hub visuals and private-location expansion
    # -------------------------------------------------------------------------
    # These paths are intentionally data-only. If a file is missing, the screen
    # falls back to a dark placeholder instead of crashing.
    MAP_LOCATION_VISUALS = {
        "tam_apartment": {
            "background": "images/assets/bg/bg_tam_room_morning.png",
            "thumbnail": "images/ui/location_hubs/tam_apartment.png",
            "theme_color": "#6b4a32",
        },
        "huyen_apartment": {
            "background": "images/assets/bg/bg_huyen_apartment_evening.png",
            "thumbnail": "images/ui/location_hubs/huyen_apartment.png",
            "theme_color": "#5d4a6b",
        },
        "hoang_house": {
            "background": "images/assets/bg/bg_hoang_house_day.png",
            "thumbnail": "images/ui/location_hubs/hoang_house.png",
            "theme_color": "#47573c",
        },
        "quan_apartment": {
            "background": "images/assets/bg/bg_quan_apartment_evening.png",
            "thumbnail": "images/ui/location_hubs/quan_apartment.png",
            "theme_color": "#39465a",
        },
        "park": {
            "background": "images/assets/bg/bg_park_afternoon.png",
            "thumbnail": "images/ui/location_hubs/park.png",
            "theme_color": "#3e5f42",
        },
        "library": {
            "background": "images/assets/bg/bg_library_day.png",
            "thumbnail": "images/ui/location_hubs/library.png",
            "theme_color": "#554633",
        },
        "foodie_street": {
            "background": "images/assets/bg/bg_foodie_street_evening.png",
            "thumbnail": "images/ui/location_hubs/foodie_street.png",
            "theme_color": "#7a402a",
        },
        "shopping_area": {
            "background": "images/assets/bg/bg_shopping_area_day.png",
            "thumbnail": "images/ui/location_hubs/shopping_area.png",
            "theme_color": "#65465f",
        },
        "restaurant": {
            "background": "images/assets/bg/bg_luxury_restaurant_evening.png",
            "thumbnail": "images/ui/location_hubs/restaurant.png",
            "theme_color": "#6f4b30",
        },
        "company": {
            "background": "images/assets/bg/bg_company_open_office_day.png",
            "thumbnail": "images/ui/location_hubs/company.png",
            "theme_color": "#344b5f",
        },
        "conference_hall": {
            "background": "images/assets/bg/bg_company_year_end_party.png",
            "thumbnail": "images/ui/location_hubs/conference_hall.png",
            "theme_color": "#60405a",
        },
        "airport": {
            "background": "images/assets/bg/bg_airport_afternoon.png",
            "thumbnail": "images/ui/location_hubs/airport.png",
            "theme_color": "#40586d",
        },
    }

    MAP_ACTION_CATEGORY_THUMBNAILS = {
        "Rest": "images/ui/location_actions/category_rest.png",
        "Home": "images/ui/location_actions/category_home.png",
        "Food": "images/ui/location_actions/category_food.png",
        "Errand": "images/ui/location_actions/category_errand.png",
        "Part-time": "images/ui/location_actions/category_part_time.png",
        "Shopping": "images/ui/location_actions/category_shopping.png",
        "Study": "images/ui/location_actions/category_study.png",
        "Exercise": "images/ui/location_actions/category_exercise.png",
        "Health": "images/ui/location_actions/category_health.png",
        "Visit": "images/ui/location_actions/category_visit.png",
        "Relationship": "images/ui/location_actions/category_relationship.png",
        "Gift": "images/ui/location_actions/category_gift.png",
        "Story": "images/ui/location_actions/category_story.png",
        "Minigame": "images/ui/location_actions/category_minigame.png",
        "Work": "images/ui/location_actions/category_work.png",
    }

    MAP_ACTION_THUMBNAILS = {
        "tam_home_rest": "images/ui/location_actions/tam_home_rest.png",
        "tam_home_cook_meal": "images/ui/location_actions/tam_home_cook_meal.png",
        "tam_home_housekeeping": "images/ui/location_actions/tam_home_housekeeping.png",
        "foodie_snack_walk": "images/ui/location_actions/foodie_snack_walk.png",
        "foodie_buy_groceries": "images/ui/location_actions/foodie_buy_groceries.png",
        "shopping_office_clothes": "images/ui/location_actions/shopping_office_clothes.png",
        "shopping_party_dress": "images/ui/location_actions/shopping_party_dress.png",
        "shopping_buy_books": "images/ui/location_actions/shopping_buy_books.png",
        "shopping_buy_small_gift": "images/ui/location_actions/shopping_buy_small_gift.png",
        "huyen_visit_chat": "images/ui/location_actions/huyen_visit_chat.png",
        "huyen_give_small_gift": "images/ui/location_actions/huyen_give_small_gift.png",
        "huyen_invite_foodie_street": "images/ui/location_actions/huyen_invite_foodie_street.png",
        "hoang_visit_casual": "images/ui/location_actions/hoang_visit_casual.png",
        "hoang_design_help": "images/ui/location_actions/hoang_design_help.png",
        "minh_visit_quiet_talk": "images/ui/location_actions/minh_visit_quiet_talk.png",
        "quan_visit_consult": "images/ui/location_actions/quan_visit_consult.png",
        "quan_document_help": "images/ui/location_actions/quan_document_help.png",
    }

    MAP_ITEM_THUMBNAILS = {
        "groceries": "images/ui/items/groceries.png",
        "office_clothes": "images/ui/items/office_clothes.png",
        "party_dress": "images/ui/items/party_dress.png",
        "work_books": "images/ui/items/work_books.png",
        "small_gift": "images/ui/items/small_gift.png",
    }

    # Optional scene routing table. Extra files can extend this without touching
    # the hub UI. Shape:
    # MAP_LOCATION_SCENE_RULES[location_id][interaction_id] = {
    #     "mode": "weighted_random",  # or "first" / "random"
    #     "default_label": "label_name",
    #     "scenes": [
    #         {"label": "label_name", "priority": 100, "weight": 1,
    #          "conditions": ["completed:chapter_id"],
    #          "min_scores": {"tam_hoang_interest": 1},
    #          "required_flags": [], "blocked_flags": []},
    #     ],
    # }
    MAP_LOCATION_SCENE_RULES = globals().get("MAP_LOCATION_SCENE_RULES", {})

    # Private fixed locations can share the same location-hub system as public
    # areas. This keeps visiting characters, gifting, private events, and future
    # minigames out of the story-map renderer.
    FIXED_MAP_LOCATIONS.setdefault("quan_apartment", {
        "id": "quan_apartment",
        "name": "Quân's Apartment",
        "x": 655,
        "y": 620,
        "category": "residential_private",
        "icon": "apartment_private",
        "default_unlocked": False,
        "unlock_conditions": ["completed:tam_c02_company_party"],
        "description": "A private apartment for quieter Quân-facing visits, advice scenes, and relationship events.",
    })

    # Make the existing Hoàng house explicitly serve Minh/Hoàng private content.
    if "hoang_house" in FIXED_MAP_LOCATIONS:
        FIXED_MAP_LOCATIONS["hoang_house"]["name"] = "Minh / Hoàng's House"
        FIXED_MAP_LOCATIONS["hoang_house"].setdefault("private_hub", True)
        FIXED_MAP_LOCATIONS["hoang_house"]["description"] = "A private house for Minh, Hoàng, and the routes that orbit them."

    if "huyen_apartment" in FIXED_MAP_LOCATIONS:
        FIXED_MAP_LOCATIONS["huyen_apartment"].setdefault("private_hub", True)

    if "MAP_ROUTE_DEFAULT_LOCATIONS" in globals():
        MAP_ROUTE_DEFAULT_LOCATIONS.setdefault("quan", "quan_apartment")

    for _location_id, _visuals in MAP_LOCATION_VISUALS.items():
        if _location_id in FIXED_MAP_LOCATIONS:
            FIXED_MAP_LOCATIONS[_location_id].setdefault("hub_background", _visuals.get("background"))
            FIXED_MAP_LOCATIONS[_location_id].setdefault("hub_thumbnail", _visuals.get("thumbnail"))
            FIXED_MAP_LOCATIONS[_location_id].setdefault("theme_color", _visuals.get("theme_color"))

    MAP_LOCATION_ACTIONS.setdefault("shopping_area", []).extend([
        {
            "id": "shopping_buy_small_gift",
            "title": "Buy a small gift",
            "summary": "A modest gift for private visits. Useful for Huyền, Hoàng, Quân, or future relationship scenes.",
            "category": "Shopping",
            "item_id": "small_gift",
            "money_cost": 180000,
            "time_cost": 1,
            "requires": {"money": 180000, "time_units": 1},
            "effects": {"money": -180000, "time_units": -1, "mood": 1, "style": 1},
            "inventory_effects": {"small_gift": 1},
            "message": "Một món quà nhỏ được gói lại cẩn thận. Không đắt, nhưng ít nhất nó không giống mua cho có.",
        },
    ])

    MAP_LOCATION_ACTIONS.setdefault("huyen_apartment", []).extend([
        {
            "id": "huyen_visit_chat",
            "title": "Visit Huyền",
            "summary": "Drop by for a casual talk. Strengthens friendship and helps Tâm decompress.",
            "category": "Visit",
            "time_cost": 1,
            "requires": {"time_units": 1},
            "effects": {"time_units": -1, "mood": 5, "stress": -4, "energy": -3},
            "story_effects": {"tam_self_clarity": 1, "tam_observation": 1},
            "flags": ["visited_huyen_apartment"],
            "message": "Huyền mở cửa, nhìn Tâm một lượt rồi chỉ vào ghế. Không hỏi ngay. Có những người bạn biết đợi đúng ba giây trước khi tra khảo.",
        },
        {
            "id": "huyen_give_small_gift",
            "title": "Give Huyền a small gift",
            "summary": "Use one small gift. A gentle friendship boost, especially after stressful chapters.",
            "category": "Gift",
            "time_cost": 1,
            "requires": {"time_units": 1, "inventory": {"small_gift": 1}},
            "effects": {"time_units": -1, "mood": 4, "stress": -2},
            "inventory_effects": {"small_gift": -1},
            "story_effects": {"tam_self_clarity": 1},
            "flags": ["gifted_huyen_small_gift"],
            "message": "Huyền nhận món quà, im hai nhịp rồi cười. “Biết điều đấy.” Nghe như chê. Nhưng cô giữ nó rất cẩn thận.",
        },
        {
            "id": "huyen_invite_foodie_street",
            "title": "Invite Huyền to Foodie Street",
            "summary": "A friendship outing. More fun than efficient, as most good ideas unfortunately are.",
            "category": "Relationship",
            "money_cost": 160000,
            "time_cost": 2,
            "requires": {"money": 160000, "time_units": 2},
            "effects": {"money": -160000, "time_units": -2, "mood": 8, "stress": -5, "energy": -7},
            "story_effects": {"tam_self_clarity": 1, "tam_observation": 1},
            "risk": {
                "chance": 0.05,
                "message": "Ly trà cuối hơi ngọt quá. Không ai ngộ độc tình bạn, nhưng dạ dày thì vẫn có ý kiến.",
                "effects": {"health": -6, "mood": -1},
                "flags": ["minor_stomach_ache"],
            },
            "message": "Hai người đi qua mấy hàng quán sáng đèn. Huyền nói nhiều hơn mọi khi. Tâm thì nghe, và thấy vai mình nhẹ xuống một chút.",
        },
    ])

    MAP_LOCATION_ACTIONS.setdefault("hoang_house", []).extend([
        {
            "id": "hoang_visit_casual",
            "title": "Visit Hoàng",
            "summary": "A private visit. Increases trust and lets the relationship breathe outside public scenes.",
            "category": "Visit",
            "time_cost": 1,
            "requires": {"time_units": 1},
            "effects": {"time_units": -1, "mood": 5, "stress": -3, "energy": -4},
            "story_effects": {"tam_hoang_interest": 1, "hoang_tam_trust": 1},
            "flags": ["visited_hoang_house"],
            "message": "Hoàng ra mở cổng hơi nhanh hơn mức cần thiết. Tâm giả vờ không nhận ra. Hai người đều rất lịch sự với bí mật nhỏ của mình.",
        },
        {
            "id": "hoang_design_help",
            "title": "Help Hoàng with design notes",
            "summary": "A focused private/work interaction. Builds professional respect and relationship trust.",
            "category": "Work",
            "time_cost": 2,
            "requires": {"time_units": 2, "energy_min": 20},
            "effects": {"time_units": -2, "energy": -9, "stress": 2, "work_skill": 2, "knowledge": 1},
            "story_effects": {"hoang_tam_trust": 2, "hoang_professional_credit": 1, "career_tam": 1},
            "message": "Tâm cúi xuống bản vẽ, chỉ một đường hơi lệch. Hoàng nhìn theo, im một lúc rồi kéo ghế cho cô ngồi gần hơn.",
        },
        {
            "id": "minh_visit_quiet_talk",
            "title": "Visit Minh for a quiet talk",
            "summary": "A restrained private conversation. Only appears after Minh-facing content opens.",
            "category": "Story",
            "time_cost": 1,
            "conditions": ["completed:tam_c06_minh_returns"],
            "requires": {"time_units": 1},
            "effects": {"time_units": -1, "mood": 2, "stress": -2, "energy": -3},
            "story_effects": {"tam_minh_drawn": 1, "tam_observation": 1},
            "flags": ["visited_minh_private_talk"],
            "message": "Minh không hỏi nhiều. Anh chỉ đặt một cốc nước xuống cạnh ghế. Tâm nhìn cốc nước ấy lâu hơn câu trả lời của mình.",
        },
    ])

    MAP_LOCATION_ACTIONS.setdefault("quan_apartment", []).extend([
        {
            "id": "quan_visit_consult",
            "title": "Visit Quân for advice",
            "summary": "A practical conversation about work discipline. Useful, slightly intimidating, regrettably efficient.",
            "category": "Visit",
            "time_cost": 1,
            "requires": {"time_units": 1},
            "effects": {"time_units": -1, "work_skill": 2, "knowledge": 1, "stress": 1, "energy": -4},
            "story_effects": {"career_tam": 1, "tam_self_clarity": 1},
            "flags": ["visited_quan_apartment"],
            "message": "Quân nghe xong, gạch đúng ba dòng trong ghi chú của Tâm. Không dịu dàng lắm. Nhưng đúng. Khó chịu ở chỗ đó.",
        },
        {
            "id": "quan_document_help",
            "title": "Help Quân sort documents",
            "summary": "Small clerical work. Earns modest money and work skill, but costs energy.",
            "category": "Part-time",
            "time_cost": 2,
            "requires": {"time_units": 2, "energy_min": 25},
            "effects": {"money": 220000, "time_units": -2, "energy": -14, "stress": 5, "work_skill": 2},
            "story_effects": {"career_tam": 1},
            "overwork_sensitive": True,
            "message": "Đống giấy tờ không có ý định tự biến mất. Sau hai giờ, Tâm bắt đầu hiểu vì sao Quân ít cười.",
        },
        {
            "id": "quan_give_small_gift",
            "title": "Bring Quân a small gift",
            "summary": "Use one small gift. A low-key respect gesture; Quân will absolutely pretend it is unnecessary.",
            "category": "Gift",
            "time_cost": 1,
            "requires": {"time_units": 1, "inventory": {"small_gift": 1}},
            "effects": {"time_units": -1, "mood": 2, "stress": -1},
            "inventory_effects": {"small_gift": -1},
            "story_effects": {"huyen_quan_trust": 1},
            "flags": ["gifted_quan_small_gift"],
            "message": "Quân nhìn món quà, rồi nhìn Tâm. “Không cần đâu.” Nhưng anh vẫn đặt nó lên kệ, ngay ngắn đến mức hơi đáng nghi.",
        },
    ])

    # Give repeatable item-purchase actions a visible inventory payoff. Unique
    # outfit purchases are marked once=True so the player cannot farm confidence
    # by buying the same dress five times. Even capitalism has limits.
    for _action in MAP_LOCATION_ACTIONS.get("shopping_area", []):
        if _action.get("id") == "shopping_office_clothes":
            _action.setdefault("item_id", "office_clothes")
            _action.setdefault("inventory_effects", {"office_clothes": 1})
            _action.setdefault("once", True)
        elif _action.get("id") == "shopping_party_dress":
            _action.setdefault("item_id", "party_dress")
            _action.setdefault("inventory_effects", {"party_dress": 1})
            _action.setdefault("once", True)
        elif _action.get("id") == "shopping_buy_books":
            _action.setdefault("item_id", "work_books")
            _action.setdefault("inventory_effects", {"work_books": 1})

    def activity_completed_actions():
        state = ensure_activity_state()
        completed = state.setdefault("completed_actions", [])
        if completed is None or not isinstance(completed, list):
            completed = list(completed)
            state["completed_actions"] = completed
        return completed

    def location_visuals(location_id):
        return MAP_LOCATION_VISUALS.get(location_id, {})

    def location_hub_background(location):
        location_id = location.get("id")
        visuals = location_visuals(location_id)
        return location.get("hub_background") or visuals.get("background") or ""

    def location_hub_thumbnail(location):
        location_id = location.get("id")
        visuals = location_visuals(location_id)
        return location.get("hub_thumbnail") or visuals.get("thumbnail") or ""

    def location_hub_theme_color(location):
        location_id = location.get("id")
        visuals = location_visuals(location_id)
        return location.get("theme_color") or visuals.get("theme_color") or "#211812cc"

    def location_action_thumbnail(action):
        action_id = action.get("id", "")
        category = action.get("category", "Action")
        return (
            action.get("thumbnail")
            or MAP_ACTION_THUMBNAILS.get(action_id)
            or "images/ui/location_actions/%s.png" % action_id
            or MAP_ACTION_CATEGORY_THUMBNAILS.get(category, "")
        )

    def location_action_category_thumbnail(action):
        return MAP_ACTION_CATEGORY_THUMBNAILS.get(action.get("category", "Action"), "")

    def location_inventory_item_thumbnail(item_id):
        return MAP_ITEM_THUMBNAILS.get(item_id) or "images/ui/items/%s.png" % item_id

    def location_thumb_label(text_value, fallback="?"):
        if not text_value:
            return fallback
        cleaned = str(text_value).strip()
        if not cleaned:
            return fallback
        return cleaned[:2].upper()

    def loc_completed_chapter(chapter_id):
        if not chapter_id:
            return False

        completed_fn = globals().get("story_is_chapter_completed", None)
        if callable(completed_fn):
            try:
                return bool(completed_fn(chapter_id))
            except Exception:
                pass

        completed = globals().get("story_completed_chapters", [])
        if chapter_id in completed:
            return True

        prog = globals().get("progress", {})
        if isinstance(prog, dict):
            if chapter_id in prog.get("completed_chapters", []):
                return True
            if chapter_id in prog.get("story_completed_chapters", []):
                return True

        return False

    def loc_story_score(score_id, default=0):
        init_fn = globals().get("initialize_progression", None)
        if callable(init_fn):
            try:
                init_fn()
            except Exception:
                pass

        story_state_obj = globals().get("story_state", {})
        if isinstance(story_state_obj, dict):
            return story_state_obj.get(score_id, default)

        return default

    def loc_has_flag(flag_id):
        if not flag_id:
            return False

        flags = globals().get("story_flags", [])
        if flag_id in flags:
            return True

        prog = globals().get("progress", {})
        if isinstance(prog, dict):
            activity_state = prog.get("activity_state", {}) or {}
            if flag_id in activity_state.get("flags", []):
                return True

        return False

    def loc_conditions_are_met(conditions):
        conditions = conditions or []
        map_conditions_fn = globals().get("map_conditions_are_met", None)
        if callable(map_conditions_fn):
            try:
                return bool(map_conditions_fn(conditions))
            except Exception:
                pass

        for condition in conditions:
            if not condition:
                continue
            condition = str(condition)
            if condition.startswith("completed:"):
                if not loc_completed_chapter(condition.split(":", 1)[1]):
                    return False
            elif condition.startswith("flag:"):
                if not loc_has_flag(condition.split(":", 1)[1]):
                    return False
            elif condition.startswith("not_flag:"):
                if loc_has_flag(condition.split(":", 1)[1]):
                    return False
            else:
                if not loc_has_flag(condition):
                    return False
        return True

    def loc_rule_is_available(rule):
        if not rule:
            return False

        if isinstance(rule, str):
            return renpy.has_label(rule)

        if not loc_conditions_are_met(rule.get("conditions", [])):
            return False

        for flag_id in rule.get("required_flags", []) or []:
            if not loc_has_flag(flag_id):
                return False

        for flag_id in rule.get("blocked_flags", []) or []:
            if loc_has_flag(flag_id):
                return False

        for score_id, min_value in (rule.get("min_scores", {}) or {}).items():
            if loc_story_score(score_id, 0) < min_value:
                return False

        for score_id, max_value in (rule.get("max_scores", {}) or {}).items():
            if loc_story_score(score_id, 0) > max_value:
                return False

        inventory_requires = rule.get("inventory", {}) or rule.get("required_inventory", {}) or {}
        for item_id, required_count in inventory_requires.items():
            if activity_inventory_get(item_id) < required_count:
                return False

        label_name = rule.get("label") or rule.get("target_label")
        if label_name and not renpy.has_label(label_name):
            return False

        return True

    def loc_weighted_pick(entries):
        entries = [entry for entry in (entries or []) if entry]
        if not entries:
            return None

        total = 0.0
        weights = []
        for entry in entries:
            weight = 1.0
            if isinstance(entry, dict):
                weight = float(entry.get("weight", 1) or 0)
            weight = max(0.0, weight)
            total += weight
            weights.append(weight)

        if total <= 0:
            return entries[0]

        roll = renpy.random.random() * total
        upto = 0.0
        for entry, weight in zip(entries, weights):
            upto += weight
            if roll <= upto:
                return entry

        return entries[-1]

    def loc_pick_message(source):
        if not source:
            return ""

        entries = source.get("messages", None)
        if entries:
            available = []
            for entry in entries:
                if isinstance(entry, str):
                    available.append({"text": entry, "weight": 1})
                elif isinstance(entry, dict) and loc_rule_is_available(entry):
                    available.append(entry)

            picked = loc_weighted_pick(available)
            if isinstance(picked, str):
                return picked
            if isinstance(picked, dict):
                return picked.get("text", "") or picked.get("message", "")

        return source.get("message", "") or ""

    def loc_scene_rules_for(location_id, interaction_id):
        location_rules = MAP_LOCATION_SCENE_RULES.get(location_id, {}) or {}
        rule_set = location_rules.get(interaction_id, None)

        if rule_set is None:
            rule_set = location_rules.get("default", None)

        if rule_set is None:
            return {}

        if isinstance(rule_set, list):
            return {"mode": "weighted_random", "scenes": rule_set}

        if isinstance(rule_set, str):
            return {"mode": "first", "default_label": rule_set, "scenes": [{"label": rule_set}]}

        return rule_set

    def loc_resolve_scene_label(location_id, interaction_id, default_label=None):
        rule_set = loc_scene_rules_for(location_id, interaction_id)
        mode = (rule_set.get("mode", "weighted_random") or "weighted_random").lower()
        scenes = rule_set.get("scenes", []) or []
        fallback_label = default_label or rule_set.get("default_label")

        available = []
        for scene_rule in scenes:
            if isinstance(scene_rule, str):
                if renpy.has_label(scene_rule):
                    available.append({"label": scene_rule, "priority": 0, "weight": 1})
            elif isinstance(scene_rule, dict) and loc_rule_is_available(scene_rule):
                available.append(scene_rule)

        if available:
            highest_priority = max([int(rule.get("priority", 0) or 0) for rule in available])
            top = [rule for rule in available if int(rule.get("priority", 0) or 0) == highest_priority]

            if mode == "first":
                picked = top[0]
            elif mode == "random":
                picked = renpy.random.choice(top)
            else:
                picked = loc_weighted_pick(top)

            if isinstance(picked, dict):
                return picked.get("label") or picked.get("target_label")

        if fallback_label and renpy.has_label(fallback_label):
            return fallback_label

        return None

    def loc_activity_add_value(key, delta):
        return activity_add(key, delta)

    def loc_inventory_add(item_id, delta):
        return activity_inventory_add(item_id, delta)

    def loc_story_add(score_id, delta):
        activity_apply_story_effects({score_id: delta})

    def loc_story_flag(flag_id):
        activity_add_flag(flag_id)

    ACTIVITY_STATE_DEFAULTS = {
        "money": 3000000,
        "time_units": 5,
        "energy": 700,
        "stress": 20,
        "mood": 500,
        "health": 750,
        "confidence": 0,
        "style": 0,
        "knowledge": 0,
        "work_skill": 0,
        "cooking_skill": 0,
        "life_skill": 0,
        "main_work_focus": 50,
        "part_time_count_this_period": 0,
    }

    ACTIVITY_CLAMPS = {
        "money": (0, 999999999),
        "time_units": (0, 100),
        "energy": (0, 100),
        "stress": (0, 100),
        "mood": (0, 100),
        "health": (0, 100),
        "confidence": (-50, 100),
        "style": (-50, 100),
        "knowledge": (0, 100),
        "work_skill": (0, 100),
        "cooking_skill": (0, 100),
        "life_skill": (0, 100),
        "main_work_focus": (0, 100),
        "part_time_count_this_period": (0, 99),
    }


    def ensure_activity_state():
        initialize_progression()

        state = progress.setdefault("activity_state", {})
        if state is None or not isinstance(state, dict):
            state = {}
            progress["activity_state"] = state

        for key, default_value in ACTIVITY_STATE_DEFAULTS.items():
            state.setdefault(key, default_value)

        inventory = state.setdefault("inventory", {})
        if inventory is None or not isinstance(inventory, dict):
            inventory = {}
            state["inventory"] = inventory

        flags = state.setdefault("flags", [])
        if flags is None or not isinstance(flags, list):
            flags = list(flags)
            state["flags"] = flags

        completed_actions = state.setdefault("completed_actions", [])
        if completed_actions is None or not isinstance(completed_actions, list):
            completed_actions = list(completed_actions)
            state["completed_actions"] = completed_actions

        return state


    def activity_get(key, default=None):
        state = ensure_activity_state()
        if default is None:
            default = ACTIVITY_STATE_DEFAULTS.get(key, 0)
        return state.get(key, default)


    def activity_set(key, value):
        state = ensure_activity_state()
        low, high = ACTIVITY_CLAMPS.get(key, (-999999999, 999999999))
        if isinstance(value, (int, float)):
            value = min(max(value, low), high)
        state[key] = value
        return value


    def activity_add(key, delta):
        return activity_set(key, activity_get(key, 0) + delta)


    def activity_inventory_get(item_id):
        state = ensure_activity_state()
        return state.setdefault("inventory", {}).get(item_id, 0)


    def activity_inventory_add(item_id, delta):
        state = ensure_activity_state()
        inventory = state.setdefault("inventory", {})
        inventory[item_id] = max(0, inventory.get(item_id, 0) + delta)
        return inventory[item_id]


    def activity_add_flag(flag_id):
        state = ensure_activity_state()
        flags = state.setdefault("flags", [])
        add_unique(flags, flag_id)

        story_flag_fn = globals().get("story_flag", None)
        if callable(story_flag_fn):
            story_flag_fn(flag_id)


    def activity_apply_story_effects(story_effects):
        if not story_effects:
            return

        story_add_fn = globals().get("story_add", None)
        if not callable(story_add_fn):
            return

        for key, delta in story_effects.items():
            story_add_fn(key, delta)


    def activity_format_money(amount):
        try:
            return "{:,}₫".format(int(amount))
        except Exception:
            return "%s₫" % amount


    def activity_apply_effects(effects):
        for key, delta in (effects or {}).items():
            activity_add(key, delta)


    def activity_apply_inventory_effects(effects):
        for item_id, delta in (effects or {}).items():
            activity_inventory_add(item_id, delta)


    def activity_start_free_time_session(time_units=5, reset_part_time_counter=True):
        ensure_activity_state()
        activity_set("time_units", time_units)
        if reset_part_time_counter:
            activity_set("part_time_count_this_period", 0)


    def location_action_requirement_failure(action):
        ensure_activity_state()
        requires = action.get("requires", {}) or {}

        money_required = requires.get("money", action.get("money_cost", 0))
        if money_required and activity_get("money") < money_required:
            return "Not enough money. Need %s." % activity_format_money(money_required)

        time_required = requires.get("time_units", action.get("time_cost", 0))
        if time_required and activity_get("time_units") < time_required:
            return "Not enough free time. Need %s time unit(s)." % time_required

        energy_min = requires.get("energy_min", None)
        if energy_min is not None and activity_get("energy") < energy_min:
            return "Too tired for this. Need at least %s energy." % energy_min

        health_min = requires.get("health_min", None)
        if health_min is not None and activity_get("health") < health_min:
            return "Health is too low for this. Need at least %s health." % health_min

        inventory_requires = requires.get("inventory", {}) or {}
        for item_id, required_count in inventory_requires.items():
            if activity_inventory_get(item_id) < required_count:
                return "Missing item: %s x%s." % (item_id.replace("_", " ").title(), required_count)

        return None


    def location_action_is_visible(action):
        return map_conditions_are_met(action.get("conditions", []))


    def location_action_resolve_state(action):
        if not location_action_is_visible(action):
            return "hidden", ""

        if action.get("once") and action.get("id") in activity_completed_actions():
            return "locked", "Already completed."

        target_label = action.get("target_label")
        if target_label and not renpy.has_label(target_label):
            return "locked", "This minigame/story action is not ready yet."

        failure = location_action_requirement_failure(action)
        if failure:
            return "locked", failure

        return "available", ""


    def build_location_action_entries(location_id):
        ensure_activity_state()

        actions = []
        for raw_action in MAP_LOCATION_ACTIONS.get(location_id, []):
            action = dict(raw_action)
            action.setdefault("location_id", location_id)
            action.setdefault("category", "Action")
            action.setdefault("summary", "")
            action.setdefault("thumbnail", location_action_thumbnail(action))
            action.setdefault("category_thumbnail", location_action_category_thumbnail(action))
            state, lock_reason = location_action_resolve_state(action)
            if state == "hidden":
                continue
            action["state"] = state
            action["lock_reason"] = lock_reason
            actions.append(action)

        return actions


    def fixed_location_has_interaction_hub(location_id):
        return location_id in MAP_LOCATION_ACTIONS


    def build_context_location_hub_entries(context):
        ensure_activity_state()

        temp_locks = context.get("temporarily_locked_locations", {}) if context else {}
        force_only = context.get("force_only_locations", []) if context else []
        show_locked = context.get("show_locked_fixed_locations", False) if context else False
        entries = []

        for location_id, location in FIXED_MAP_LOCATIONS.items():
            unlocked = fixed_location_is_unlocked(location_id)
            has_actions = fixed_location_has_interaction_hub(location_id)
            visible = unlocked or location_id in temp_locks or location_id in force_only or show_locked

            if not visible:
                continue

            state = "available" if unlocked and has_actions else "locked"
            lock_reason = ""

            if not unlocked:
                lock_reason = "Location is not unlocked yet."
            elif not has_actions:
                lock_reason = "No interaction is available here yet."

            if location_id in temp_locks:
                state = "locked"
                lock_reason = temp_locks[location_id]

            if force_only and location_id not in force_only:
                state = "locked"
                lock_reason = "Not available right now."

            entries.append({
                "id": "location_hub_%s" % location_id,
                "location_id": location_id,
                "title": location.get("name", location_id),
                "name": location.get("name", location_id),
                "description": location.get("description", ""),
                "x": location.get("x", 960),
                "y": location.get("y", 540),
                "category": location.get("category", "location"),
                "icon": location.get("icon", "default"),
                "thumbnail": location_hub_thumbnail(location),
                "hub_background": location_hub_background(location),
                "theme_color": location_hub_theme_color(location),
                "kind": "location_hub",
                "action_type": "location_hub",
                "state": state,
                "enabled": state == "available",
                "lock_reason": lock_reason,
            })

        return entries


    def perform_location_action(action):
        ensure_activity_state()

        state, lock_reason = location_action_resolve_state(action)
        if state != "available":
            return {"ok": False, "message": lock_reason or "This action is not available."}

        activity_apply_effects(action.get("effects", {}))
        activity_apply_inventory_effects(action.get("inventory_effects", {}))
        activity_apply_story_effects(action.get("story_effects", {}))

        for flag_id in action.get("flags", []) or []:
            activity_add_flag(flag_id)

        if action.get("once") and action.get("id"):
            add_unique(activity_completed_actions(), action.get("id"))

        messages = []
        action_message = loc_pick_message(action)
        if action_message:
            messages.append(action_message)

        risk = action.get("risk")
        if risk and renpy.random.random() < risk.get("chance", 0.0):
            activity_apply_effects(risk.get("effects", {}))
            activity_apply_inventory_effects(risk.get("inventory_effects", {}))
            activity_apply_story_effects(risk.get("story_effects", {}))
            for flag_id in risk.get("flags", []) or []:
                activity_add_flag(flag_id)
            risk_message = loc_pick_message(risk)
            if risk_message:
                messages.append(risk_message)

        if action.get("overwork_sensitive"):
            part_time_count = activity_add("part_time_count_this_period", 1)
            if part_time_count >= 10:
                activity_add("main_work_focus", -5)
                activity_add("health", -4)
                activity_apply_story_effects({"career_tam": -1, "tam_insecurity": 1})
                messages.append("Làm thêm hơi dày rồi. Công việc chính và sức khỏe bắt đầu trả phí âm thầm.")

        if activity_get("energy") <= 12 or activity_get("stress") >= 90:
            activity_add("health", -5)
            activity_add("mood", -4)
            messages.append("Cơ thể bắt đầu phản đối. Không kịch tính, nhưng rất biết cách gửi hóa đơn.")

        return {"ok": True, "message": "\n\n".join(messages)}


label location_interaction_scene_router(location_id, interaction_id, default_label=None):
    $ resolved_scene_label = loc_resolve_scene_label(location_id, interaction_id, default_label)

    if resolved_scene_label and renpy.has_label(resolved_scene_label):
        call expression resolved_scene_label
    else:
        "There is nothing meaningful to do here yet."

    return


label location_interaction_hub(location_id):
    $ ensure_activity_state()
    $ location = FIXED_MAP_LOCATIONS.get(location_id, {"id": location_id, "name": location_id})
    $ location_actions = build_location_action_entries(location_id)

    if not location_actions:
        "There is nothing meaningful to do here yet."
        return "stay_on_map"

    call screen location_interaction_menu(location, location_actions)
    $ selected_action = _return

    # Back buttons / dismiss keys can return None, False, or sometimes True depending
    # on inherited screen actions. Only dict payloads are valid action selections.
    if not isinstance(selected_action, dict):
        return "stay_on_map"

    if selected_action.get("_action") == "back":
        return "stay_on_map"

    $ target_label = selected_action.get("target_label")

    if target_label and renpy.has_label(target_label):
        call expression target_label
        return "stay_on_map"

    $ scene_key = selected_action.get("scene_key") or selected_action.get("interaction_id")
    $ default_scene_label = selected_action.get("default_scene_label")
    $ use_scene_router = bool(selected_action.get("use_scene_router") or scene_key or default_scene_label)

    if use_scene_router:
        $ routed_interaction_id = scene_key or selected_action.get("id")
        $ routed_location_id = selected_action.get("location_id", location_id)
        call location_interaction_scene_router(routed_location_id, routed_interaction_id, default_scene_label)
        return "stay_on_map"

    $ action_result = perform_location_action(selected_action)
    $ action_message = action_result.get("message", "")

    if action_message:
        "[action_message]"

    return "stay_on_map"


screen location_interaction_menu(location, actions):
    tag menu
    modal True

    $ activity_state = ensure_activity_state()
    $ inventory = activity_state.get("inventory", {})
    $ hub_bg = location_hub_background(location)
    $ hub_thumb = location_hub_thumbnail(location)
    $ theme_color = location_hub_theme_color(location)
    $ hub_thumb_bg = Solid((theme_color + "dd") if theme_color.startswith("#") and len(theme_color) == 7 else "#2a2118dd")
    $ visible_inventory = [(item_id, count) for item_id, count in sorted(inventory.items()) if count > 0]

    fixed:
        xysize (1920, 1080)

        if hub_bg and renpy.loadable(hub_bg):
            add hub_bg fit "cover"
        else:
            add Solid("#0b0806")

        add Solid("#05040399")
        add Solid("#1a120766") ypos 710 ysize 370

        frame:
            xpos 96
            ypos 66
            xsize 1728
            ysize 948
            background ui_frame_or_solid("gui/library/panel.png", "#15100cf2", 28)

            vbox:
                spacing 18
                xfill True

                hbox:
                    xfill True
                    spacing 18

                    frame:
                        xysize (178, 112)
                        background hub_thumb_bg

                        if hub_thumb and renpy.loadable(hub_thumb):
                            add hub_thumb fit "cover"
                        else:
                            $ hub_label = location_thumb_label(location.get("name", "Location"), "LOC")
                            text hub_label:
                                xalign 0.5
                                yalign 0.5
                                size 34
                                bold True
                                color "#f7e6c8"

                    vbox:
                        spacing 6
                        xfill True

                        text location.get("name", "Location"):
                            style "location_hub_title"

                        text location.get("description", "Choose how to spend your free time here."):
                            style "location_hub_subtitle"

                    textbutton _("Back to Map"):
                        style "location_hub_back_button"
                        text_style "location_hub_back_button_text"
                        action Return({"_action": "back"})

                frame:
                    xfill True
                    ysize 82
                    background Solid("#211812cc")

                    hbox:
                        spacing 26
                        xalign 0.5
                        yalign 0.5

                        text ("Money: %s" % activity_format_money(activity_state.get("money", 0))) style "location_hub_status_text"
                        text ("Time: %s" % activity_state.get("time_units", 0)) style "location_hub_status_text"
                        text ("Energy: %s" % activity_state.get("energy", 0)) style "location_hub_status_text"
                        text ("Stress: %s" % activity_state.get("stress", 0)) style "location_hub_status_text"
                        text ("Mood: %s" % activity_state.get("mood", 0)) style "location_hub_status_text"
                        text ("Health: %s" % activity_state.get("health", 0)) style "location_hub_status_text"

                hbox:
                    spacing 22
                    xfill True

                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        xsize 1228
                        ysize 674

                        vbox:
                            spacing 12
                            xfill True

                            for action in actions:
                                $ state = action.get("state", "available")
                                $ enabled = state == "available"
                                $ action_button_action = Return(action) if enabled else NullAction()
                                $ thumb = action.get("thumbnail", "")
                                $ category_thumb = action.get("category_thumbnail", "")
                                $ thumb_label = location_thumb_label(action.get("category", "Action"), "ACT")

                                button:
                                    style "location_action_button"
                                    sensitive enabled
                                    action action_button_action

                                    hbox:
                                        spacing 16
                                        xfill True

                                        frame:
                                            xysize (142, 104)
                                            background Solid("#2a2118dd")

                                            if thumb and renpy.loadable(thumb):
                                                add thumb fit "cover"
                                            elif category_thumb and renpy.loadable(category_thumb):
                                                add category_thumb fit "cover"
                                            else:
                                                text thumb_label:
                                                    xalign 0.5
                                                    yalign 0.5
                                                    size 26
                                                    bold True
                                                    color ("#f7e6c8" if enabled else "#9f8f80")

                                        vbox:
                                            spacing 6
                                            xfill True

                                            hbox:
                                                spacing 10
                                                xfill True

                                                text action.get("title", "Action"):
                                                    style ("location_action_title" if enabled else "location_action_title_locked")

                                                null xfill True

                                                text action.get("category", "Action"):
                                                    style "location_action_tag"

                                            text action.get("summary", ""):
                                                style "location_action_summary"

                                            if not enabled:
                                                text action.get("lock_reason", "Locked."):
                                                    style "location_action_locked_reason"
                                            else:
                                                $ money_cost = action.get("money_cost", 0)
                                                $ time_cost = action.get("time_cost", 0)
                                                $ item_id = action.get("item_id", "")
                                                if money_cost or time_cost or item_id:
                                                    text ("Cost: %s%s%s" % ((activity_format_money(money_cost) if money_cost else ""), (" • %s time" % time_cost if time_cost else ""), (" • Item: %s" % item_id.replace("_", " ").title() if item_id else ""))):
                                                        style "location_action_cost"

                    frame:
                        xsize 430
                        ysize 674
                        background Solid("#120d09cc")

                        vbox:
                            spacing 10
                            xfill True

                            text _("Current Growth"):
                                style "location_hub_side_title"

                            text ("Confidence: %s" % activity_state.get("confidence", 0)) style "location_hub_side_text"
                            text ("Style: %s" % activity_state.get("style", 0)) style "location_hub_side_text"
                            text ("Knowledge: %s" % activity_state.get("knowledge", 0)) style "location_hub_side_text"
                            text ("Work Skill: %s" % activity_state.get("work_skill", 0)) style "location_hub_side_text"
                            text ("Cooking: %s" % activity_state.get("cooking_skill", 0)) style "location_hub_side_text"
                            text ("Life Skill: %s" % activity_state.get("life_skill", 0)) style "location_hub_side_text"
                            text ("Main Work Focus: %s" % activity_state.get("main_work_focus", 0)) style "location_hub_side_text"

                            null height 12

                            text _("Inventory"):
                                style "location_hub_side_title"

                            viewport:
                                scrollbars "vertical"
                                mousewheel True
                                draggable True
                                ysize 244

                                vbox:
                                    spacing 8
                                    xfill True

                                    if visible_inventory:
                                        for item_id, count in visible_inventory:
                                            $ item_thumb = location_inventory_item_thumbnail(item_id)
                                            hbox:
                                                spacing 8
                                                xfill True

                                                frame:
                                                    xysize (54, 54)
                                                    background Solid("#2a2118dd")

                                                    if item_thumb and renpy.loadable(item_thumb):
                                                        add item_thumb fit "cover"
                                                    else:
                                                        text location_thumb_label(item_id, "IT"):
                                                            xalign 0.5
                                                            yalign 0.5
                                                            size 16
                                                            bold True
                                                            color "#f7e6c8"

                                                text ("%s x%s" % (item_id.replace("_", " ").title(), count)):
                                                    style "location_hub_side_text"
                                                    yalign 0.5
                                    else:
                                        text _("Empty"):
                                            style "location_hub_side_text"

style location_hub_title is gui_text
style location_hub_subtitle is gui_text
style location_hub_status_text is gui_text
style location_hub_back_button is button
style location_hub_back_button_text is button_text
style location_action_button is button
style location_action_title is gui_text
style location_action_title_locked is gui_text
style location_action_tag is gui_text
style location_action_summary is gui_text
style location_action_locked_reason is gui_text
style location_action_cost is gui_text
style location_hub_side_title is gui_text
style location_hub_side_text is gui_text

style location_hub_title:
    size 44
    bold True
    color "#f6d59b"
    outlines [(2, "#000000aa", 0, 0)]

style location_hub_subtitle:
    size 21
    color "#e8d8c0"
    line_spacing 3

style location_hub_status_text:
    size 20
    color "#f2dfbf"

style location_hub_back_button:
    background Solid("#251b13dd")
    hover_background Solid("#4a3422ee")
    xpadding 18
    ypadding 12

style location_hub_back_button_text:
    size 22
    color "#f7e6c8"
    hover_color "#ffddaa"

style location_action_button:
    background Solid("#211912cc")
    hover_background Solid("#3a2a1dde")
    insensitive_background Solid("#17110ccc")
    xfill True
    ypadding 14
    xpadding 18

style location_action_title:
    size 25
    bold True
    color "#f7e6c8"

style location_action_title_locked:
    size 25
    bold True
    color "#a99783"

style location_action_tag:
    size 17
    color "#d7b982"

style location_action_summary:
    size 19
    color "#dfcfb8"
    line_spacing 2

style location_action_locked_reason:
    size 18
    color "#c7a797"

style location_action_cost:
    size 18
    color "#d6c0a0"

style location_hub_side_title:
    size 24
    bold True
    color "#f2dfbf"

style location_hub_side_text:
    size 20
    color "#d7c5ac"