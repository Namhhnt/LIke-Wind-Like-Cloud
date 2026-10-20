# Isolated C05 visual and full chapter regression tests; excluded from builds.
init python:
    def c05_test_choice_caption(index):
        items = [item for item in renpy.get_screen("choice").scope["items"] if item.action is not None]
        return items[index % len(items)].caption

label _test_c05_catalog:
    $ _c05_catalog = ["bg_c05_breakfast","bg_c05_glasshouse","bg_c05_park","bg_c05_market_cafe","bg_c05_rain_awning","bg_c05_car_night","bg_c05_lobby_night","cg_tam_c05_tam_morning","cg_tam_c05_huyen_morning","cg_tam_c05_group_morning","cg_tam_c05_tam_pickup","cg_tam_c05_tam_breakfast","cg_tam_c05_tam_glasshouse","cg_tam_c05_tam_bench","cg_tam_c05_huyen_pickup","cg_tam_c05_huyen_breakfast","cg_tam_c05_huyen_photo","cg_tam_c05_huyen_rain","cg_tam_c05_group_meal","cg_tam_c05_group_photo","cg_tam_c05_tam_topaz","cg_tam_c05_tam_fastening","cg_tam_c05_tam_expensive","cg_tam_c05_tam_card","cg_tam_c05_huyen_printer","cg_tam_c05_huyen_album","cg_tam_c05_huyen_print","cg_tam_c05_group_envelopes","cg_tam_c05_tam_collar","cg_tam_c05_huyen_car","cg_tam_c05_group_afterward","bg_c05_market_day"]
    $ _c05_index = 0
    while _c05_index < len(_c05_catalog):
        scene expression _c05_catalog[_c05_index]
        "..."
        $ _c05_index += 1
    scene bg_tam_living_room_night
    "..."
    return

label _test_c05_entry:
    $ initialize_progression()
    "..."
    jump tam_c05_sunday_date

testsuite chapter_five_assets:
    parameter variant = [0, 1]
    setup:
        $ _test.timeout = 120.0
        $ _test.transition_timeout = 0.1
        $ _test.screenshot_directory = "tests/screenshots/chapter_five_assets"
        run Language(None)
        $ renpy.set_physical_size((1920, 1080) if variant == 0 else (1280, 720))
    testcase image_catalog:
        run Start("_test_c05_catalog")
        advance until eval renpy.showing("bg_c05_breakfast")
        pause 0.1
        screenshot ("bg_c05_breakfast_" + str(variant) + ".png")
        advance until eval renpy.showing("bg_c05_glasshouse")
        pause 0.1
        screenshot ("bg_c05_glasshouse_" + str(variant) + ".png")
        advance until eval renpy.showing("bg_c05_park")
        pause 0.1
        screenshot ("bg_c05_park_" + str(variant) + ".png")
        advance until eval renpy.showing("bg_c05_market_cafe")
        pause 0.1
        screenshot ("bg_c05_market_cafe_" + str(variant) + ".png")
        advance until eval renpy.showing("bg_c05_rain_awning")
        pause 0.1
        screenshot ("bg_c05_rain_awning_" + str(variant) + ".png")
        advance until eval renpy.showing("bg_c05_car_night")
        pause 0.1
        screenshot ("bg_c05_car_night_" + str(variant) + ".png")
        advance until eval renpy.showing("bg_c05_lobby_night")
        pause 0.1
        screenshot ("bg_c05_lobby_night_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c05_tam_morning")
        pause 0.1
        screenshot ("cg_tam_c05_tam_morning_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c05_huyen_morning")
        pause 0.1
        screenshot ("cg_tam_c05_huyen_morning_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c05_group_morning")
        pause 0.1
        screenshot ("cg_tam_c05_group_morning_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c05_tam_pickup")
        pause 0.1
        screenshot ("cg_tam_c05_tam_pickup_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c05_tam_breakfast")
        pause 0.1
        screenshot ("cg_tam_c05_tam_breakfast_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c05_tam_glasshouse")
        pause 0.1
        screenshot ("cg_tam_c05_tam_glasshouse_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c05_tam_bench")
        pause 0.1
        screenshot ("cg_tam_c05_tam_bench_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c05_huyen_pickup")
        pause 0.1
        screenshot ("cg_tam_c05_huyen_pickup_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c05_huyen_breakfast")
        pause 0.1
        screenshot ("cg_tam_c05_huyen_breakfast_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c05_huyen_photo")
        pause 0.1
        screenshot ("cg_tam_c05_huyen_photo_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c05_huyen_rain")
        pause 0.1
        screenshot ("cg_tam_c05_huyen_rain_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c05_group_meal")
        pause 0.1
        screenshot ("cg_tam_c05_group_meal_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c05_group_photo")
        pause 0.1
        screenshot ("cg_tam_c05_group_photo_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c05_tam_topaz")
        pause 0.1
        screenshot ("cg_tam_c05_tam_topaz_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c05_tam_fastening")
        pause 0.1
        screenshot ("cg_tam_c05_tam_fastening_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c05_tam_expensive")
        pause 0.1
        screenshot ("cg_tam_c05_tam_expensive_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c05_tam_card")
        pause 0.1
        screenshot ("cg_tam_c05_tam_card_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c05_huyen_printer")
        pause 0.1
        screenshot ("cg_tam_c05_huyen_printer_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c05_huyen_album")
        pause 0.1
        screenshot ("cg_tam_c05_huyen_album_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c05_huyen_print")
        pause 0.1
        screenshot ("cg_tam_c05_huyen_print_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c05_group_envelopes")
        pause 0.1
        screenshot ("cg_tam_c05_group_envelopes_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c05_tam_collar")
        pause 0.1
        screenshot ("cg_tam_c05_tam_collar_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c05_huyen_car")
        pause 0.1
        screenshot ("cg_tam_c05_huyen_car_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c05_group_afterward")
        pause 0.1
        screenshot ("cg_tam_c05_group_afterward_" + str(variant) + ".png")
        advance until eval renpy.showing("bg_c05_market_day")
        pause 0.1
        screenshot ("bg_c05_market_day_" + str(variant) + ".png")
        advance until eval _c05_index == len(_c05_catalog)
        assert eval len(_c05_catalog) == 32
        assert eval not any(name.startswith("cg_tam_c05_") for name in renpy.get_showing_tags())
        run MainMenu(confirm=False)
        assert screen "main_menu"

testsuite chapter_five_branches:
    parameter variant = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    setup:
        $ _test.timeout = 120.0
        $ _test.transition_timeout = 0.1
        $ _test.screenshot_directory = "tests/screenshots/chapter_five_branches"
        run Language(None)
        $ renpy.set_physical_size((1920, 1080) if variant % 2 == 0 else (1280, 720))
    testcase full_chapter:
        run Start("_test_c05_entry")
        $ profile = [["tam",60,"hoang_gift_tam_topaz_earrings",0],["tam",40,"hoang_gift_tam_topaz_earrings",1],["tam",20,"hoang_gift_tam_topaz_earrings",2],["tam",60,"hoang_gift_tam_topaz_earrings",1],["tam",60,"hoang_gift_tam_expensive_topaz",0],["tam",40,"hoang_gift_tam_expensive_topaz",1],["tam",20,"hoang_gift_tam_expensive_topaz",2],["tam",40,"",1],["huyen",60,"hoang_includes_first_huyen_photo",1],["huyen",40,"hoang_hides_huyen_gift_meaning",2],["huyen",20,"hoang_leaves_huyen_album_blank",0],["huyen",60,"",1],["friend_group",60,"",0],["friend_group",40,"",1],["friend_group",20,"",2]][variant]
        $ story_state["hoang_anniversary_route"] = profile[0]
        $ story_state["hoang_self_acceptance"] = profile[1]
        $ story_state["tam_insecurity"] = [10, 30, 50][variant % 3]
        $ story_state["hoang_tam_trust"] = 70
        $ story_state["tam_hoang_interest"] = 70
        $ story_flag(profile[2]) if profile[2] else None
        advance until eval renpy.showing({"tam": "cg_tam_c05_tam_morning", "huyen": "cg_tam_c05_huyen_morning", "friend_group": "cg_tam_c05_group_morning"}[profile[0]])
        pause 0.1
        screenshot ("morning_" + str(variant) + ".png")
        advance until screen "choice" or eval story_chapter_done("tam_c05_sunday_date")
        if screen "choice":
            assert eval not any(name.startswith("cg_tam_c05_") for name in renpy.get_showing_tags())
            click expression c05_test_choice_caption(profile[3])
        advance until eval renpy.showing({"tam": "cg_tam_c05_tam_pickup", "huyen": "cg_tam_c05_huyen_pickup", "friend_group": "cg_tam_c05_group_photo"}[profile[0]])
        pause 0.1
        screenshot ("outing_" + str(variant) + ".png")
        advance until screen "choice" or eval story_chapter_done("tam_c05_sunday_date")
        if screen "choice":
            assert eval not any(name.startswith("cg_tam_c05_") for name in renpy.get_showing_tags())
            click expression c05_test_choice_caption(profile[3])
        advance until screen "choice" or eval story_chapter_done("tam_c05_sunday_date")
        if screen "choice":
            assert eval not any(name.startswith("cg_tam_c05_") for name in renpy.get_showing_tags())
            click expression c05_test_choice_caption(profile[3])
        advance until screen "choice" or eval story_chapter_done("tam_c05_sunday_date")
        if screen "choice":
            assert eval not any(name.startswith("cg_tam_c05_") for name in renpy.get_showing_tags())
            click expression c05_test_choice_caption(profile[3])
        advance until screen "choice" or eval story_chapter_done("tam_c05_sunday_date")
        if screen "choice":
            assert eval not any(name.startswith("cg_tam_c05_") for name in renpy.get_showing_tags())
            click expression c05_test_choice_caption(profile[3])
        advance until screen "choice" or eval story_chapter_done("tam_c05_sunday_date")
        if screen "choice":
            assert eval not any(name.startswith("cg_tam_c05_") for name in renpy.get_showing_tags())
            click expression c05_test_choice_caption(profile[3])
        advance until screen "choice" or eval story_chapter_done("tam_c05_sunday_date")
        if screen "choice":
            assert eval not any(name.startswith("cg_tam_c05_") for name in renpy.get_showing_tags())
            click expression c05_test_choice_caption(profile[3])
        advance until screen "choice" or eval story_chapter_done("tam_c05_sunday_date")
        if screen "choice":
            assert eval not any(name.startswith("cg_tam_c05_") for name in renpy.get_showing_tags())
            click expression c05_test_choice_caption(profile[3])
        advance until eval story_chapter_done("tam_c05_sunday_date")
        assert eval story_has_flag("one_year_anniversary_outing_complete")
        assert eval story_has_flag(["tam_wears_anniversary_earrings","hoang_hesitates_but_fastens_tam_earring","tam_saves_anniversary_earrings_for_ordinary_day","hoang_fastens_tam_earring","tam_expensive_gift_repaired_together","tam_accepts_expensive_gift_uneasily","tam_refuses_gift_without_rejecting_hoang","tam_and_hoang_will_choose_gift_together","hoang_huyen_first_deliberate_photo","hoang_corrects_safe_album_with_couple_photo","huyen_fills_blank_album_after_honesty","hoang_huyen_choose_album_together","group_writes_first_impressions","group_writes_next_year_plan","group_recreates_first_photo_again"][variant])
        assert eval story_has_flag({"tam": "tam_hoang_one_year_anniversary_completed", "huyen": "hoang_huyen_one_year_anniversary_completed", "friend_group": "tam_huyen_hoang_one_year_close_friends"}[profile[0]])
        assert eval not any(name.startswith("cg_tam_c05_") for name in renpy.get_showing_tags())
        assert eval not story_has_flag("tam_wears_anniversary_earrings") or profile[0] == "tam" and profile[2] == "hoang_gift_tam_topaz_earrings"
        assert eval not story_has_flag("hoang_fastens_tam_earring") or profile[0] == "tam" and profile[2] == "hoang_gift_tam_topaz_earrings"
        screenshot ("completed_" + str(variant) + ".png")
        run MainMenu(confirm=False)
        assert screen "main_menu"
