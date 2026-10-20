# Isolated integration entrypoint, independent of player save state.
label _test_c03_assets_entry:
    $ initialize_progression()
    jump tam_c03_thienan_family

testsuite chapter_three_assets:
    parameter variant = [0, 1, 2, 3]

    setup:
        $ _test.timeout = 100.0
        $ _test.transition_timeout = 0.1
        $ _test.screenshot_directory = "tests/screenshots/chapter_three_assets"
        run Language(None)
        $ renpy.set_physical_size((1280, 720) if variant in (1, 3) else (1920, 1080))

    testcase chapter_three_playthrough:
        run Start("_test_c03_assets_entry")
        advance until eval renpy.showing("cg_tam_c03_thienan_sofa")
        pause 0.3
        screenshot ("01_sofa_" + str(variant) + ".png")
        advance until screen "choice"
        assert eval renpy.showing("bg_tam_family_living_room_evening")
        click expression ["Lấy chăn mỏng đắp cho chị", "Đóng laptop giúp chị", "Lặng lẽ để chị tự quyết định"][variant % 3]
        advance until eval renpy.showing("cg_tam_c03_quang_visit")
        pause 0.3
        screenshot ("02_visit_" + str(variant) + ".png")
        advance until screen "choice"
        assert eval renpy.showing("bg_tam_family_entry_evening")
        click expression ["Anh ấy đáng tin", "Anh ấy hiền quá", "Chị An vẫn giữ khoảng cách"][variant % 3]
        advance until eval renpy.showing("cg_tam_c03_trip_checklist")
        pause 0.3
        screenshot ("03_trip_" + str(variant) + ".png")
        advance until screen "choice"
        assert eval renpy.showing("bg_hoangminh_villa_living_room_day")
        click expression ["Họ thật sự tin nhau", "Họ chỉ là đồng nghiệp quá quen việc", "Anh Quang hiểu chị ấy hơn chị muốn thừa nhận"][variant % 3]
        advance until eval renpy.showing("cg_tam_c03_family_dinner")
        pause 0.3
        screenshot ("04_dinner_" + str(variant) + ".png")
        advance until screen "choice"
        assert eval renpy.showing("bg_tam_family_dining_room_evening")
        click expression ["Nhẹ nhàng hỏi mẹ có thể để chị nghỉ tối nay không", "Im lặng vì sợ làm không khí nặng hơn", "Đánh trống lảng sang chuyện công việc"][variant % 3]
        advance until eval renpy.showing("cg_tam_c03_sisters_balcony")
        pause 0.3
        screenshot ("05_balcony_" + str(variant) + ".png")
        advance until screen "choice"
        assert eval renpy.showing("bg_tam_family_balcony_night")
        if eval variant == 0:
            click "Chị có hạnh phúc không?"
            advance until screen "choice"
            click "Chị có hạnh phúc không?"
            advance until screen "choice"
            click "Chị từng thích ai chưa?"
            advance until screen "choice"
            click "Chị từng thích ai chưa?"
        else:
            if eval variant == 2:
                click "Chị có hạnh phúc không?"
                advance until screen "choice"
            if eval variant == 3:
                click "Chị từng thích ai chưa?"
                advance until screen "choice"
            click "Không hỏi gì, chỉ đứng cạnh chị"
        advance until eval renpy.showing("cg_tam_c03_quang_jacket")
        assert eval story_has_flag("tam_exhausted_private_sister_talk") == (variant == 0)
        assert eval story_has_flag("tam_sat_with_thienan_in_silence") == (variant != 0)
        pause 0.3
        screenshot ("06_jacket_" + str(variant) + ".png")
        advance until screen "choice"
        assert eval renpy.showing("bg_tam_family_living_room_evening")
        click expression ["Anh ấy xứng đáng có một cơ hội", "Chị An chưa từng nhìn anh ấy theo cách đó", "Có lẽ anh ấy nên dừng lại"][variant % 3]
        advance until eval renpy.showing("cg_tam_c03_quang_gifts")
        pause 0.3
        screenshot ("07_gifts_" + str(variant) + ".png")
        advance until screen "choice"
        assert eval renpy.showing("bg_hoangminh_villa_day")
        click expression ["Em sẽ giúp anh", "Em sẽ giúp chị em", "Anh nên nói với chị ấy một ngày nào đó", "Anh nên nghĩ cho mình nhiều hơn"][variant]
        advance until eval renpy.showing("cg_tam_c03_career_notebook")
        assert eval story_has_flag(["tam_support_quang", "tam_prioritizes_thienan_choice", "tam_encouraged_quang_confession", "tam_quang_interest_seed"][variant])
        pause 0.3
        screenshot ("08_notebook_" + str(variant) + ".png")
        advance until screen "choice"
        assert eval renpy.showing("bg_asset_0008")
        click expression ["Nghiêm túc ghi nhớ", "Cảm thấy mình bị so sánh với chị", "Cảm ơn chị thật lòng"][variant % 3]
        advance until eval story_chapter_done("tam_c03_thienan_family")
        assert eval story_chapter_done("tam_c03_thienan_family")
        assert eval story_has_flag("tam_c03_thienan_family_completed_seed")
        run MainMenu(confirm=False)
        assert screen "main_menu"
