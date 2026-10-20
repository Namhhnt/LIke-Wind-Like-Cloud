# Isolated visual and actual-story branch acceptance checks.
label _test_c04_family:
    $ initialize_progression()
    $ tam_c04_ensure_extended_story_state()
    $ _c04_family_done = False
    call tam_c04_w14_s02_huyen_meets_anh_nhi
    call tam_c04_w17_s04_huyen_knows_the_house
    call tam_c04_w19_s04_huyen_anh_nhi_school_project
    call tam_c04_w22_s04_huyen_anh_nhi_sleepover
    $ tam_c04_lock_tam_romance("independent")
    call tam_c04_w23_s02_group_dinner_new_balance
    call tam_c04_w23_s03_huyen_hoang_friend_seed
    $ _c04_family_done = True
    "Hoàn tất kiểm tra nhánh gia đình."
    return

testsuite chapter_four_family_assets:
    parameter variant = [0, 1, 2]
    setup:
        $ _test.timeout = 120.0
        $ _test.transition_timeout = 0.1
        $ _test.screenshot_directory = "tests/screenshots/chapter_four_family_assets"
        run Language(None)
        $ renpy.set_physical_size((1280, 720) if variant == 1 else (1920, 1080))
    testcase family_choices_and_cleanup:
        run Start("_test_c04_family")
        advance until eval renpy.showing("cg_tam_c04_school_pickup")
        advance until screen "choice"
        assert eval renpy.showing("bg_c04_school_gate")
        click expression ["Để Huyền tự xoay xở", "Ghé qua mang đồ ăn", "Hỏi Ánh Nhi về Quân ở nhà"][variant]
        advance until eval renpy.showing("cg_tam_c04_spare_key")
        advance until screen "choice"
        assert eval renpy.showing("bg_c04_quan_home_day")
        click expression ["Huyền nhận chìa khóa", "Huyền chỉ nhận khi Quân đi công tác", "Huyền trả lại nhưng ghi mã khóa"][variant]
        advance until eval renpy.showing("cg_tam_c04_school_bridge")
        advance until screen "choice"
        assert eval renpy.showing("bg_company_open_office_day")
        click expression ["Huyền sửa cùng Ánh Nhi", "Tâm và Huyền chia nhau một người một nửa", "Để Quân tự về đúng giờ"][variant]
        advance until eval renpy.showing("cg_tam_c04_huyen_nhi_huyen_home")
        advance until screen "choice"
        assert eval renpy.showing("bg_c04_huyen_home_night")
        click expression ["Huyền nói vì Quân đáng tin", "Huyền nói vì Ánh Nhi", "Huyền đánh trống lảng"][variant]
        advance until eval renpy.showing("cg_tam_c04_group_dinner")
        pause 0.1
        screenshot ("group_dinner_" + str(variant) + ".png")
        advance until screen "choice"
        assert eval renpy.showing("bg_luxury_restaurant_evening")
        click "Giữ bữa tối ở đúng nghĩa nhóm bạn"
        advance until eval renpy.showing("cg_tam_c04_huyen_hoang_hall")
        advance until eval _c04_family_done
        assert eval not renpy.showing("cg_tam_c04_huyen_hoang_hall")
        assert eval story_has_flag("tam_c04_huyen_met_anh_nhi")
        run MainMenu(confirm=False)
        assert screen "main_menu"

label _test_c04_catalog:
    $ _c04_catalog_images = ['cg_tam_c04_phone_morning', 'cg_tam_c04_phone_night', 'cg_tam_c04_tam_work_day', 'cg_tam_c04_tam_work_evening', 'cg_tam_c04_tam_huyen_work', 'cg_tam_c04_team_review', 'cg_tam_c04_tam_presentation', 'cg_tam_c04_huyen_presentation', 'cg_tam_c04_huyen_quan_work', 'cg_tam_c04_hoang_lobby', 'cg_tam_c04_hoang_home', 'cg_tam_c04_hoang_restaurant', 'cg_tam_c04_quang_lobby', 'cg_tam_c04_quang_door', 'cg_tam_c04_family_table', 'cg_tam_c04_sisters_table', 'cg_tam_c04_quang_thienan_work', 'cg_tam_c04_tam_quang_cafe', 'cg_tam_c04_huyen_nhi_quan_home', 'cg_tam_c04_huyen_nhi_huyen_home', 'cg_tam_c04_huyen_hoang_office', 'cg_tam_c04_huyen_hoang_hall', 'cg_tam_c04_empty_chair', 'cg_tam_c04_spare_key', 'cg_tam_c04_school_pickup', 'cg_tam_c04_south_late_night', 'cg_tam_c04_return_luggage', 'cg_tam_c04_decision_bed', 'cg_tam_c04_hoang_hands', 'cg_tam_c04_quang_confession', 'cg_tam_c04_independent_plan', 'cg_tam_c04_school_bridge', 'cg_tam_c04_group_dinner', 'cg_tam_c04_final_review', 'cg_tam_c04_thienan_open_door', 'cg_tam_c04_sleeping_blanket', 'cg_tam_c04_hoang_final', 'cg_tam_c04_quang_final']
    $ _c04_catalog_index = 0
    while _c04_catalog_index < len(_c04_catalog_images):
        scene expression _c04_catalog_images[_c04_catalog_index]
        "Kiểm tra bố cục CG chương 4 dưới vùng hội thoại."
        $ _c04_catalog_index += 1
    scene bg_company_open_office_day
    "Hoàn tất kiểm tra hình."
    return

label _test_c04_branches:
    $ initialize_progression()
    $ tam_c04_ensure_extended_story_state()
    $ _c04_test_stage = "started"
    "Chuẩn bị kiểm tra nhánh chương 4."
    $ story_state.update(dict(tam_hoang_interest=85, hoang_tam_trust=85, tam_quang_interest=85, quang_tam_warmth=85, quang_tam_awareness=85))
    $ story_flag("tam_c04_m04_hoang_ready")
    call tam_c04_w18_s02_tam_romance_decision
    call tam_c04_w18_s03_after_decision
    $ _c04_test_stage = "after_decision"
    "Kiểm tra ảnh quyết định đã được dọn."
    call tam_c04_w19_s02_first_week_after_choice
    $ _c04_test_stage = "after_first_week"
    "Kiểm tra ảnh tuần đầu đã được dọn."
    $ relationship_mark_contact("tam_hoang", "tam_c04_w21", source="asset_test")
    $ relationship_mark_contact("tam_hoang", "tam_c04_w22", source="asset_test")
    call tam_c04_w24_s03_tam_route_finale
    $ story_flag("tam_c04_quang_thienan_committed") if not story_has_flag("tam_c04_tam_quang_confirmed") else None
    call tam_c04_w24_s04_quang_thienan_finale
    $ _c04_test_stage = "after_thienan"
    "Kiểm tra cặp đôi đúng nhánh."
    call tam_c04_w24_s05_huyen_quan_finale
    $ _c04_test_stage = "finished"
    "Hoàn tất kiểm tra nhánh."
    return

testsuite chapter_four_assets:
    parameter variant = [0, 1]
    setup:
        $ _test.timeout = 120.0
        $ _test.transition_timeout = 0.1
        $ _test.screenshot_directory = "tests/screenshots/chapter_four_assets"
        run Language(None)
        $ renpy.set_physical_size((1920, 1080) if variant == 0 else (1280, 720))
    testcase all_cg_textbox_compositions:
        run Start("_test_c04_catalog")
        advance until eval renpy.showing("cg_tam_c04_phone_morning")
        pause 0.1
        screenshot ("cg_tam_c04_phone_morning_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c04_phone_night")
        pause 0.1
        screenshot ("cg_tam_c04_phone_night_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c04_tam_work_day")
        pause 0.1
        screenshot ("cg_tam_c04_tam_work_day_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c04_tam_work_evening")
        pause 0.1
        screenshot ("cg_tam_c04_tam_work_evening_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c04_tam_huyen_work")
        pause 0.1
        screenshot ("cg_tam_c04_tam_huyen_work_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c04_team_review")
        pause 0.1
        screenshot ("cg_tam_c04_team_review_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c04_tam_presentation")
        pause 0.1
        screenshot ("cg_tam_c04_tam_presentation_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c04_huyen_presentation")
        pause 0.1
        screenshot ("cg_tam_c04_huyen_presentation_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c04_huyen_quan_work")
        pause 0.1
        screenshot ("cg_tam_c04_huyen_quan_work_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c04_hoang_lobby")
        pause 0.1
        screenshot ("cg_tam_c04_hoang_lobby_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c04_hoang_home")
        pause 0.1
        screenshot ("cg_tam_c04_hoang_home_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c04_hoang_restaurant")
        pause 0.1
        screenshot ("cg_tam_c04_hoang_restaurant_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c04_quang_lobby")
        pause 0.1
        screenshot ("cg_tam_c04_quang_lobby_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c04_quang_door")
        pause 0.1
        screenshot ("cg_tam_c04_quang_door_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c04_family_table")
        pause 0.1
        screenshot ("cg_tam_c04_family_table_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c04_sisters_table")
        pause 0.1
        screenshot ("cg_tam_c04_sisters_table_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c04_quang_thienan_work")
        pause 0.1
        screenshot ("cg_tam_c04_quang_thienan_work_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c04_tam_quang_cafe")
        pause 0.1
        screenshot ("cg_tam_c04_tam_quang_cafe_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c04_huyen_nhi_quan_home")
        pause 0.1
        screenshot ("cg_tam_c04_huyen_nhi_quan_home_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c04_huyen_nhi_huyen_home")
        pause 0.1
        screenshot ("cg_tam_c04_huyen_nhi_huyen_home_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c04_huyen_hoang_office")
        pause 0.1
        screenshot ("cg_tam_c04_huyen_hoang_office_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c04_huyen_hoang_hall")
        pause 0.1
        screenshot ("cg_tam_c04_huyen_hoang_hall_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c04_empty_chair")
        pause 0.1
        screenshot ("cg_tam_c04_empty_chair_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c04_spare_key")
        pause 0.1
        screenshot ("cg_tam_c04_spare_key_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c04_school_pickup")
        pause 0.1
        screenshot ("cg_tam_c04_school_pickup_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c04_south_late_night")
        pause 0.1
        screenshot ("cg_tam_c04_south_late_night_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c04_return_luggage")
        pause 0.1
        screenshot ("cg_tam_c04_return_luggage_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c04_decision_bed")
        pause 0.1
        screenshot ("cg_tam_c04_decision_bed_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c04_hoang_hands")
        pause 0.1
        screenshot ("cg_tam_c04_hoang_hands_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c04_quang_confession")
        pause 0.1
        screenshot ("cg_tam_c04_quang_confession_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c04_independent_plan")
        pause 0.1
        screenshot ("cg_tam_c04_independent_plan_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c04_school_bridge")
        pause 0.1
        screenshot ("cg_tam_c04_school_bridge_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c04_group_dinner")
        pause 0.1
        screenshot ("cg_tam_c04_group_dinner_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c04_final_review")
        pause 0.1
        screenshot ("cg_tam_c04_final_review_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c04_thienan_open_door")
        pause 0.1
        screenshot ("cg_tam_c04_thienan_open_door_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c04_sleeping_blanket")
        pause 0.1
        screenshot ("cg_tam_c04_sleeping_blanket_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c04_hoang_final")
        pause 0.1
        screenshot ("cg_tam_c04_hoang_final_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c04_quang_final")
        pause 0.1
        screenshot ("cg_tam_c04_quang_final_" + str(variant) + ".png")
        advance until eval renpy.showing("bg_company_open_office_day")
        assert eval not any(renpy.showing(x) for x in _c04_catalog_images)
        run MainMenu(confirm=False)
        assert screen "main_menu"

testsuite chapter_four_asset_branches:
    parameter variant = [0, 1, 2]
    setup:
        $ _test.timeout = 120.0
        $ _test.transition_timeout = 0.1
        $ _test.screenshot_directory = "tests/screenshots/chapter_four_asset_branches"
        run Language(None)
        $ renpy.set_physical_size((1280, 720) if variant == 1 else (1920, 1080))
    testcase actual_story_branch_cleanup:
        run Start("_test_c04_branches")
        advance until eval renpy.showing("cg_tam_c04_decision_bed")
        assert eval not renpy.showing("cg_tam_c04_hoang_hands") and not renpy.showing("cg_tam_c04_quang_confession")
        advance until screen "choice"
        assert eval renpy.showing("bg_tam_room_morning")
        click expression ["Chọn Hoàng — thử bước vào một mối quan hệ nghiêm túc", "Chọn Quang — làm rõ tình cảm giữa hai người", "Chọn độc lập — không bước vào tình cảm khi chưa thật sự muốn"][variant]
        advance until eval renpy.showing(["cg_tam_c04_hoang_hands", "cg_tam_c04_quang_confession", "cg_tam_c04_independent_plan"][variant])
        pause 0.1
        screenshot ("decision_" + str(variant) + ".png")
        advance until eval _c04_test_stage == "after_decision"
        assert eval not any(name.startswith("cg_tam_c04_") for name in renpy.get_showing_tags())
        advance until eval renpy.showing(["cg_tam_c04_hoang_lobby", "cg_tam_c04_tam_quang_cafe", "cg_tam_c04_tam_work_day"][variant])
        if eval variant == 0:
            advance until screen "choice"
            assert eval not renpy.showing("cg_tam_c04_hoang_lobby")
            click "Báo trước lịch bận và giữ một bữa tối muộn"
        advance until eval _c04_test_stage == "after_first_week"
        assert eval not any(name.startswith("cg_tam_c04_") for name in renpy.get_showing_tags())
        advance until eval renpy.showing(["cg_tam_c04_hoang_final", "cg_tam_c04_quang_final", "cg_tam_c04_independent_plan"][variant])
        advance until eval _c04_test_stage == "after_thienan"
        assert eval not renpy.showing("cg_tam_c04_quang_thienan_work")
        assert eval story_has_flag("tam_c04_final_quang_thienan_accepted_closeness") == (variant != 1)
        advance until eval renpy.showing("cg_tam_c04_sleeping_blanket")
        pause 0.1
        screenshot ("blanket_" + str(variant) + ".png")
        advance until eval _c04_test_stage == "finished"
        assert eval renpy.showing("bg_c04_quan_home_night")
        assert eval not renpy.showing("cg_tam_c04_sleeping_blanket")
        run MainMenu(confirm=False)
        assert screen "main_menu"
