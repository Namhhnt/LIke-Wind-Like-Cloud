# Isolated entrypoint for the integration suite; never uses player saves.
label _test_c02_assets_entry:
    $ initialize_progression()
    jump tam_c02_company_party

testsuite chapter_two_assets:
    parameter variant = [0, 1, 2, 3, 4]

    setup:
        $ _test.timeout = 100.0
        $ _test.transition_timeout = 0.1
        $ _test.screenshot_directory = "tests/screenshots/chapter_two_assets"
        run Language(None)
        $ renpy.set_physical_size((1280, 720) if variant in (1, 3) else (1920, 1080))

    testcase chapter_two_playthrough:
        run Start("_test_c02_assets_entry")
        advance until eval renpy.showing("cg_tam_c02_onboarding")
        pause 0.3
        screenshot ("01_onboarding_" + str(variant) + ".png")
        advance until screen "choice"
        assert eval renpy.showing("bg_company_open_office_day")
        if eval variant == 0:
            $ story_flag("tam_perfect_interview")
        $ tam_set_available_money(0)
        click expression ["Chuẩn bị nghiêm túc", "Đi chậm lại cùng Huyền", "Thấy hơi bị ngợp"][variant % 3]
        advance until screen "choice"
        assert eval renpy.showing("bg_company_lobby_noon")
        click expression ["Ghi nhớ tiêu chuẩn của Quân", "Để Huyền đùa cho nhẹ bớt", "Bị áp lực hơn"][variant % 3]
        advance until eval renpy.showing("cg_tam_c02_quan_document")
        pause 0.3
        screenshot ("02_quan_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c02_first_salary")
        assert eval tam_get_available_money() == (7500000 if variant == 0 else 6000000)
        pause 0.3
        screenshot ("03_salary_" + str(variant) + ".png")
        advance until screen "choice"
        assert eval renpy.showing("bg_company_open_office_day")
        if eval variant == 2:
            click "Không mua gì, để dành tiền"
        else:
            click "Đi Shopping Area với Huyền"
            advance until screen "interactive_map_screen"
            click id "map_location_shopping_area_active"
            click id "map_go_to_location"
            advance until eval renpy.showing("cg_tam_c02_shopping")
            pause 0.3
            screenshot ("04_shopping_" + str(variant) + ".png")
            advance until screen "choice"
            assert eval renpy.showing("bg_tam_c02_boutique_evening")
            if eval variant == 4:
                $ tam_set_available_money(0)
                # Office purchase loops back without applying outfit flags.
                click "Váy áo công sở"
                advance until eval renpy.showing("cg_tam_c02_shopping")
                advance until screen "choice"
                assert eval not story_has_flag("tam_c02_outfit_office_elegant")
            if eval variant == 1:
                click "Váy áo công sở"
            else:
                click "Váy dự tiệc sang trọng"
        advance until eval renpy.showing(["cg_tam_c02_party_premium_dress", "cg_tam_c02_party_office", "cg_tam_c02_party_default", "cg_tam_c02_party_office", "cg_tam_c02_party_default"][variant])
        assert eval story_has_flag("tam_c02_outfit_party_elegant") == (variant == 0)
        assert eval story_has_flag("tam_c02_outfit_office_elegant") == (variant in (1, 3))
        assert eval (not story_has_flag("tam_c02_outfit_party_elegant") and not story_has_flag("tam_c02_outfit_office_elegant")) == (variant in (2, 4))
        assert eval variant not in (3, 4) or story_has_flag("tam_c02_luxury_dress_seen_but_unaffordable")
        assert eval variant != 4 or story_has_flag("tam_c02_saved_first_salary")
        pause 0.3
        screenshot ("05_outfit_" + str(variant) + ".png")
        advance until screen "choice"
        assert eval renpy.showing("bg_company_year_end_party")
        click expression ["Ở gần Huyền", "Đứng gần bàn dự án", "Đứng ở góc yên tĩnh hơn"][variant % 3]
        advance until eval renpy.showing("cg_tam_c02_hoang_model")
        pause 0.3
        screenshot ("06_hoang_" + str(variant) + ".png")
        if eval variant != 0:
            advance until screen "choice"
            assert eval renpy.showing("bg_company_year_end_party")
            click expression ["Tâm chủ động bắt chuyện với Hoàng", "Hoàng bắt chuyện với Tâm trước", "Huyền nói chuyện với Hoàng trước", "Không có cuộc trò chuyện đáng kể"][variant - 1]
        advance until eval renpy.showing(["cg_tam_c02_party_end_premium", "cg_tam_c02_party_end_office", "cg_tam_c02_party_end_default", "cg_tam_c02_party_end_office", "cg_tam_c02_party_end_default"][variant])
        pause 0.3
        screenshot ("07_party_end_" + str(variant) + ".png")
        advance until screen "choice"
        assert eval renpy.showing("bg_company_year_end_party_late")
        click expression ["Trao đổi liên hệ với Hoàng", "Để Huyền tiếp tục trêu Hoàng", "Về sớm để nghỉ cho ngày mai"][variant % 3]
        advance until eval story_chapter_done("tam_c02_company_party")
        assert eval story_chapter_done("tam_c02_company_party")
        run MainMenu(confirm=False)
        assert screen "main_menu"
