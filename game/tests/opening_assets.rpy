# Run with an isolated --savedir; never use a player's save for this suite.
# Covers actual story transitions and all three interview outcomes, including
# the absence of a presentation CG when the player skips the presentation.
testsuite opening_assets:
    parameter variant = [0, 1, 2]

    setup:
        $ _test.timeout = 90.0
        $ _test.transition_timeout = 0.1
        $ _test.screenshot_directory = "tests/screenshots/opening_assets"
        run Language(None)
        $ renpy.set_physical_size((1280, 720) if variant == 1 else (1920, 1080))

    testcase opening_playthrough:
        run Start("start")
        advance until eval renpy.showing("bg_prologue_rain_street_night")
        pause 0.3
        screenshot ("01_rain_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_prologue_umbrella_touch")
        pause 0.3
        screenshot ("02_umbrella_" + str(variant) + ".png")
        advance until screen "choice"
        assert eval renpy.showing("black")
        click expression ["Gương mặt của người đàn ông ấy", "Tiếng mưa", "Không có gì rõ ràng"][variant]
        advance until eval renpy.showing("cg_prologue_tam_wakes")
        pause 0.3
        screenshot ("03_waking_" + str(variant) + ".png")
        advance until screen "choice"
        assert eval renpy.showing("bg_tam_room_morning")
        click expression ["Xem nó là một dấu hiệu đáng chú ý", "Gạt đi như áp lực trước phỏng vấn", "Thấy bất an nhưng không gọi tên"][variant]
        advance until screen "choice"
        click expression ["Kể cho Huyền", "Giữ lại cho riêng mình", "Nói đùa cho qua"][variant]
        advance until eval renpy.showing("cg_tam_c01_collar_coffee")
        assert eval story_chapter_done("prologue_rain_dream")
        pause 0.3
        screenshot ("04_collar_" + str(variant) + ".png")
        advance until screen "choice"
        assert eval renpy.showing("bg_tam_living_room_morning")
        click expression ["Calm Huyền down", "Review the portfolio again", "Hide her nervousness with a joke"][variant]
        advance until screen "choice"
        assert eval renpy.showing("bg_taxi_interior_day")
        click expression ["Review the portfolios one last time", "Lighten up the mood", "Review the portfolios one last time"][variant]
        advance until screen "tam_speech_minigame"
        assert eval renpy.showing("bg_interview_room")
        if eval variant == 2:
            # Fail three real submissions, then exercise the unlocked Skip UI.
            $ renpy.set_screen_variable("picked", ["self_only", "solo", "salary_first", "context"], screen="tam_speech_minigame")
            $ renpy.restart_interaction()
            click "Confirm"
            advance until screen "tam_speech_minigame"
            $ renpy.set_screen_variable("picked", ["self_only", "solo", "salary_first", "context"], screen="tam_speech_minigame")
            $ renpy.restart_interaction()
            click "Confirm"
            advance until screen "tam_speech_minigame"
            $ renpy.set_screen_variable("picked", ["self_only", "solo", "salary_first", "context"], screen="tam_speech_minigame")
            $ renpy.restart_interaction()
            click "Confirm"
            advance until screen "tam_speech_minigame"
            assert eval tam_speech_attempts == 3
            click "Skip"
            advance until "A safe answer."
            assert eval renpy.showing("bg_interview_room")
        else:
            $ renpy.set_screen_variable("picked", ["context", "coordination", "risk", "commitment"] if variant == 0 else ["coordination", "context", "risk", "commitment"], screen="tam_speech_minigame")
            $ renpy.restart_interaction()
            click "Confirm"
            advance until eval renpy.showing("cg_tam_c01_interview_portfolio")
            pause 0.3
            screenshot ("05_portfolio_" + str(variant) + ".png")
        advance until screen "choice"
        assert eval renpy.showing("bg_interview_waiting_room")
        click expression ["Be honest about the pressure", "Keep it vague to avoid worrying her", "Be honest with insight"][variant]
        advance until eval renpy.showing("cg_tam_c01_offer_hug")
        assert eval story_has_flag("tam_interview_passed") and story_has_flag("huyen_interview_passed")
        pause 0.3
        screenshot ("06_offer_hug_" + str(variant) + ".png")
        advance until screen "choice"
        assert eval renpy.showing("bg_company_lobby_noon")
        click expression ["Celebrate together", "Call Thiên An first", "Keep the joy quiet"][variant]
        advance until eval renpy.showing("cg_tam_c01_celebration_toast")
        pause 0.3
        screenshot ("07_toast_" + str(variant) + ".png")
        advance until eval renpy.showing("cg_tam_c01_hoang_window")
        pause 0.3
        screenshot ("08_hoang_" + str(variant) + ".png")
        advance until screen "choice"
        assert eval renpy.showing("bg_luxury_restaurant_evening")
        click expression ["Tâm", "Huyền", "Neither of them pays much attention"][variant]
        advance until eval renpy.showing("bg_company_lobby_afternoon")
        assert eval not renpy.showing("cg_tam_c01_hoang_window")
        advance until eval story_chapter_done("tam_c01_interview_day")
        assert eval story_chapter_done("tam_c01_interview_day")
        run MainMenu(confirm=False)
        assert screen "main_menu"
