# Problem Diagnosis Minigame UI - asset-free redesign
# Drop this file into game/ and let it replace the old screen/style definitions.
# It keeps the existing gameplay functions and state keys intact.

screen problem_diagnosis_minigame():
    modal True
    zorder 120

    default action_filter = "all"

    $ case = pd_get_case()
    $ phase = pd_state.get("phase", 1)
    $ selected_data = list(pd_state.get("selected_data_ids", []))
    $ organize_cards = pd_get_available_organize_cards()
    $ selected_card = pd_state.get("selected_card_id")
    $ action_pairs = dict(pd_state.get("action_pic_pairs", {}))
    $ filtered_actions = pd_get_actions_for_filter(action_filter)

    fixed:
        xysize (1920, 1080)

        add "gui/theme/background_full.png"
        # Asset-free cinematic background. No image files required.
        add Solid("#07111b88")
        add Solid("#ffffff07") xpos 0 ypos 96 xsize 1920 ysize 2
        add Solid("#0d1a2acc") xpos 0 ypos 0 xsize 1920 ysize 96
        add Solid("#f4efe41c") xpos 0 ypos 96 xsize 1920 ysize 16
        add Solid("#00000066") xpos 0 ypos 112 xsize 1920 ysize 968

        # Soft pseudo-background blocks, only Solids.
        add Solid("#ffffff08") xpos 110 ypos 150 xsize 430 ysize 640
        add Solid("#ffffff06") xpos 685 ypos 150 xsize 450 ysize 650
        add Solid("#ffffff05") xpos 1250 ypos 146 xsize 560 ysize 650
        add Solid("#00000044") xpos 0 ypos 912 xsize 1920 ysize 168

        use problem_diagnosis_header(case, phase)

        # Main panels. Fixed positioning avoids the overflow/clipping from nested hbox + xfill.
        use pd_phase_data_panel(case, phase, selected_data)
        text "›" style "pd_panel_arrow" xpos 594 ypos 446
        use pd_phase_analyze_panel(case, phase, selected_data, organize_cards, selected_card)
        text "›" style "pd_panel_arrow" xpos 1194 ypos 446

        if phase == 1:
            use pd_phase_organize_panel(case, phase, selected_card)
        else:
            use pd_phase_solution_panel(case, phase, action_filter, filtered_actions, action_pairs)

        use problem_diagnosis_footer(case, phase)


screen pd_phase_data_panel(case, phase, selected_data):
    frame:
        style "pd_panel_frame"
        xpos 64
        ypos 132
        xsize 500
        ysize 764

        fixed:
            xfill True
            yfill True

            frame:
                style "pd_panel_header_bar"
                xpos 0
                ypos 0
                xsize 500
                ysize 66

            text "▣" style "pd_panel_icon" xpos 28 ypos 18
            text _("Data") style "pd_panel_title" xpos 74 ypos 19 xmaximum 360
            text _("Drag or click to select data.") style "pd_panel_hint_light" xpos 28 ypos 82 xmaximum 330

            frame:
                style "pd_count_badge"
                xpos 400
                ypos 76
                xsize 62
                ysize 30
                text "[len(selected_data)] / 4" style "pd_count_badge_text" xalign 0.5 yalign 0.5

            text "?" style "pd_help_mark" xpos 452 ypos 82

            viewport:
                xpos 22
                ypos 118
                xsize 456
                ysize 586
                draggable True
                mousewheel True
                scrollbars "vertical"

                vbox:
                    spacing 7
                    xsize 426

                    for card in case.get("data_cards", []):
                        $ selected = card["id"] in selected_data

                        button:
                            style "pd_card_button"
                            selected selected
                            xsize 426
                            action Function(pd_toggle_data_selection, card["id"])
                            sensitive phase == 1

                            hbox:
                                spacing 9
                                xfill True
                                yalign 0.5

                                frame:
                                    style "pd_card_icon_frame"
                                    xsize 42
                                    ysize 42
                                    text "D" style "pd_card_icon_text" xalign 0.5 yalign 0.5

                                vbox:
                                    spacing 3
                                    xsize 318
                                    yalign 0.5

                                    text _(card["title"]) style "pd_card_title" xmaximum 318
                                    text _(card["description"]) style "pd_card_body" xmaximum 318
                                    text ", ".join(card.get("tags", [])) style "pd_card_meta" xmaximum 318

                                text "⋮" style "pd_card_grip" xalign 1.0 yalign 0.5

            add Solid("#ffffff16") xpos 22 ypos 718 xsize 456 ysize 1
            text "ⓘ" style "pd_info_icon" xpos 28 ypos 732
            text _("Select multiple related facts to analyze.") style "pd_panel_hint_light" xpos 62 ypos 735 xmaximum 400


screen pd_phase_analyze_panel(case, phase, selected_data, organize_cards, selected_card):
    frame:
        style "pd_panel_frame"
        xpos 622
        ypos 132
        xsize 540
        ysize 764

        fixed:
            xfill True
            yfill True

            frame:
                style "pd_panel_header_bar"
                xpos 0
                ypos 0
                xsize 540
                ysize 66

            text "⌕" style "pd_panel_icon" xpos 28 ypos 16
            text _("Analyze") style "pd_panel_title" xpos 82 ypos 19 xmaximum 382
            text _("Selected data (2–4 items to analyze)") style "pd_panel_hint_dark" xpos 28 ypos 82 xmaximum 380

            frame:
                style "pd_count_badge_light"
                xpos 454
                ypos 76
                xsize 56
                ysize 30
                text "[len(selected_data)] / 4" style "pd_count_badge_text_dark" xalign 0.5 yalign 0.5

            vbox:
                xpos 24
                ypos 118
                xsize 492
                spacing 7

                # Natural-height section. Do not set ysize here; it grows/shrinks with selected_data.
                frame:
                    style "pd_selected_stack_frame"
                    xsize 492

                    vbox:
                        spacing 6
                        xsize 468

                        if selected_data:
                            for card_id in selected_data:
                                button:
                                    style "pd_selected_data_slot"
                                    xsize 468
                                    action Function(pd_toggle_data_selection, card_id)
                                    sensitive phase == 1

                                    hbox:
                                        spacing 8
                                        yalign 0.5
                                        text _(pd_get_card_title(card_id)) style "pd_selected_data_text" xsize 408
                                        text "×" style "pd_selected_data_remove" xalign 1.0 yalign 0.5
                        else:
                            text _("Choose related data from the left panel first.") style "pd_placeholder_text" xalign 0.5 xmaximum 430

                text "⌄" style "pd_down_marker" xalign 0.5

                textbutton _("✦  Analyze Selected"):
                    style "pd_primary_button"
                    xsize 492
                    ysize 48
                    action Function(pd_analyze_selected)
                    sensitive phase == 1 and len(selected_data) >= 2

                text _("Combine clues to generate insights.") style "pd_small_italic" xalign 0.5 xmaximum 360

                if pd_state.get("created_insight_id"):
                    $ insight = case.get("insight_cards", {}).get(pd_state["created_insight_id"])

                    frame:
                        style "pd_success_frame"
                        xsize 492

                        hbox:
                            spacing 10
                            xfill True
                            yalign 0.5

                            frame:
                                style "pd_success_icon_frame"
                                xsize 42
                                ysize 42
                                text "!" style "pd_success_icon_text" xalign 0.5 yalign 0.5

                            vbox:
                                spacing 4
                                xsize 404
                                text _("Insight Generated") style "pd_success_title"
                                text _(insight["title"]) style "pd_card_title_dark" xmaximum 404
                                text _(insight["description"]) style "pd_card_body_dark" xmaximum 404
                else:
                    frame:
                        style "pd_placeholder_frame"
                        xsize 492

                        text _("Successful analysis recipes create insight cards here.") style "pd_placeholder_text" xalign 0.5 xmaximum 420

                text _("Available for organization") style "pd_section_label"

                viewport:
                    xsize 492
                    ysize 248
                    # yminimum 188
                    # ymaximum 248
                    yfill True
                    draggable True
                    mousewheel True
                    scrollbars "vertical"

                    vbox:
                        spacing 7
                        xsize 464
                        # yfill True

                        for card in organize_cards:
                            $ is_selected = selected_card == card["id"]
                            $ is_assigned = pd_is_card_assigned(card["id"])

                            button:
                                style "pd_compact_card_button"
                                selected is_selected
                                xsize 464
                                action Function(pd_select_organize_card, card["id"])
                                sensitive phase == 1

                                hbox:
                                    spacing 8
                                    yalign 0.5

                                    frame:
                                        style ("pd_card_icon_frame_insight" if card["type"] == "insight" else "pd_card_icon_frame")
                                        xsize 36
                                        ysize 36
                                        text ("I" if card["type"] == "insight" else "D") style "pd_card_icon_text" xalign 0.5 yalign 0.5

                                    vbox:
                                        spacing 2
                                        xsize 374
                                        text _(card["title"]) style "pd_card_title" xmaximum 374
                                        if card["type"] == "insight":
                                            text _("Insight") style "pd_card_meta_emphasis" xmaximum 374
                                        elif is_assigned:
                                            text _("Already assigned") style "pd_card_meta_emphasis" xmaximum 374
                                        else:
                                            text _(card["description"]) style "pd_card_body" xmaximum 374

                                    text "⋮" style "pd_card_grip" xalign 1.0 yalign 0.5


screen pd_phase_organize_panel(case, phase, selected_card):
    frame:
        style "pd_panel_frame"
        xpos 1220
        ypos 132
        xsize 636
        ysize 764

        fixed:
            xfill True
            yfill True

            frame:
                style "pd_panel_header_bar"
                xpos 0
                ypos 0
                xsize 636
                ysize 66

            text "▰" style "pd_panel_icon" xpos 28 ypos 18
            text _("Organize") style "pd_panel_title" xpos 82 ypos 19 xmaximum 430
            text _("Drag insights to the appropriate categories.") style "pd_panel_hint_light" xpos 28 ypos 82 xmaximum 470
            text "?" style "pd_help_mark" xpos 582 ypos 82

            frame:
                style "pd_bucket_frame_root"
                xpos 22
                ypos 118
                xsize 592
                ysize 268

                fixed:
                    xfill True
                    yfill True

                    hbox:
                        xpos 18
                        ypos 14
                        spacing 10
                        frame:
                            style "pd_bucket_icon_root"
                            xsize 38
                            ysize 38
                            text "R" style "pd_bucket_icon_text" xalign 0.5 yalign 0.5
                        text _("Root Cause") style "pd_bucket_title" yalign 0.5 xmaximum 370
                        text "[len(pd_state.get('root_cause_slots', []))] / 4" style "pd_bucket_counter" xalign 1.0 yalign 0.5

                    viewport:
                        xpos 18
                        ypos 64
                        xsize 556
                        ysize 144
                        draggable True
                        mousewheel True
                        scrollbars "vertical"

                        vbox:
                            spacing 7
                            xsize 530

                            for card_id in pd_state.get("root_cause_slots", []):
                                frame:
                                    style "pd_bucket_card_root"
                                    xsize 530

                                    hbox:
                                        spacing 7
                                        yalign 0.5
                                        text _(pd_get_card_title(card_id)) style "pd_bucket_card_text" xsize 468
                                        textbutton "×":
                                            style "pd_inline_icon_button"
                                            text_style "pd_inline_icon_text"
                                            action Function(pd_remove_from_slot, "root_cause_slots", card_id)
                                            sensitive phase == 1

                            if not pd_state.get("root_cause_slots"):
                                text _("Use insights and supporting evidence that explain why the problem exists.") style "pd_bucket_empty_text" xmaximum 520

                    textbutton _("Assign Selected"):
                        style "pd_secondary_button"
                        xpos 18
                        ypos 218
                        xsize 194
                        ysize 38
                        action Function(pd_assign_selected_card, "root_cause_slots")
                        sensitive phase == 1 and bool(selected_card)

            frame:
                style "pd_bucket_frame_impact"
                xpos 22
                ypos 402
                xsize 592
                ysize 268

                fixed:
                    xfill True
                    yfill True

                    hbox:
                        xpos 18
                        ypos 14
                        spacing 10
                        frame:
                            style "pd_bucket_icon_impact"
                            xsize 38
                            ysize 38
                            text "I" style "pd_bucket_icon_text" xalign 0.5 yalign 0.5
                        text _("Impact") style "pd_bucket_title_alt" yalign 0.5 xmaximum 370
                        text "[len(pd_state.get('impact_slots', []))] / 4" style "pd_bucket_counter" xalign 1.0 yalign 0.5

                    viewport:
                        xpos 18
                        ypos 64
                        xsize 556
                        ysize 144
                        draggable True
                        mousewheel True
                        scrollbars "vertical"

                        vbox:
                            spacing 7
                            xsize 530

                            for card_id in pd_state.get("impact_slots", []):
                                frame:
                                    style "pd_bucket_card_impact"
                                    xsize 530

                                    hbox:
                                        spacing 7
                                        yalign 0.5
                                        text _(pd_get_card_title(card_id)) style "pd_bucket_card_text" xsize 468
                                        textbutton "×":
                                            style "pd_inline_icon_button"
                                            text_style "pd_inline_icon_text"
                                            action Function(pd_remove_from_slot, "impact_slots", card_id)
                                            sensitive phase == 1

                            if not pd_state.get("impact_slots"):
                                text _("Place evidence that shows what the issue is already hurting.") style "pd_bucket_empty_text" xmaximum 520

                    textbutton _("Assign Selected"):
                        style "pd_secondary_button_alt"
                        xpos 18
                        ypos 218
                        xsize 194
                        ysize 38
                        action Function(pd_assign_selected_card, "impact_slots")
                        sensitive phase == 1 and bool(selected_card)

            textbutton _("→  Proceed to Solution"):
                style "pd_primary_button_alt"
                xpos 22
                ypos 690
                xsize 592
                ysize 50
                action Function(pd_submit_phase_1)


screen pd_phase_solution_panel(case, phase, action_filter, filtered_actions, action_pairs):
    frame:
        style "pd_panel_frame"
        xpos 1220
        ypos 132
        xsize 636
        ysize 764

        fixed:
            xfill True
            yfill True

            frame:
                style "pd_panel_header_bar"
                xpos 0
                ypos 0
                xsize 636
                ysize 66

            text "✓" style "pd_panel_icon" xpos 28 ypos 18
            text _("Solution / Hành động") style "pd_panel_title" xpos 82 ypos 19 xmaximum 440
            text _("Match each action to the correct PIC / owner.") style "pd_panel_hint_light" xpos 28 ypos 82 xmaximum 500

            text _("Solution filters") style "pd_section_label" xpos 28 ypos 116

            hbox:
                xpos 28
                ypos 146
                spacing 6

                for filter_name, filter_label in (("all", _("All")), ("priority", _("Priority")), ("communication", _("Communication")), ("timeline", _("Timeline"))):
                    textbutton filter_label:
                        style "pd_filter_button"
                        selected action_filter == filter_name
                        action SetScreenVariable("action_filter", filter_name)

            frame:
                style "pd_inner_panel_frame"
                xpos 22
                ypos 190
                xsize 592
                ysize 248

                fixed:
                    xfill True
                    yfill True
                    text _("Actions") style "pd_inner_panel_title" xpos 16 ypos 12

                    viewport:
                        xpos 16
                        ypos 44
                        xsize 560
                        ysize 186
                        draggable True
                        mousewheel True
                        scrollbars "vertical"

                        vbox:
                            spacing 7
                            xsize 532

                            for action in filtered_actions:
                                $ action_selected = pd_state.get("selected_action_id") == action["id"]
                                $ has_bonus = pd_action_has_insight_bonus(action)

                                button:
                                    style "pd_action_button"
                                    selected action_selected
                                    xsize 532
                                    action Function(pd_select_action, action["id"])

                                    vbox:
                                        spacing 3
                                        xfill True
                                        text _(action["title"]) style "pd_card_title" xmaximum 500
                                        text _(action["description"]) style "pd_card_body" xmaximum 500
                                        if has_bonus:
                                            text _("Insight bonus active") style "pd_card_meta_emphasis"
                                        elif action.get("unlocked_if"):
                                            text _("Insight bonus unavailable") style "pd_card_meta"

            frame:
                style "pd_inner_panel_frame"
                xpos 22
                ypos 458
                xsize 284
                ysize 198

                fixed:
                    xfill True
                    yfill True
                    text _("Matched") style "pd_inner_panel_title" xpos 14 ypos 12

                    viewport:
                        xpos 14
                        ypos 44
                        xsize 254
                        ysize 136
                        draggable True
                        mousewheel True
                        scrollbars "vertical"

                        vbox:
                            spacing 5
                            xsize 232

                            for action_id, pic_id in action_pairs.items():
                                frame:
                                    style "pd_pair_frame"
                                    xsize 232

                                    vbox:
                                        spacing 3
                                        text _(pd_get_action_title(action_id)) style "pd_pair_title" xmaximum 210
                                        text _("Owner: [pd_get_pic_name(pic_id)]") style "pd_pair_meta" xmaximum 210
                                        textbutton _("Remove"):
                                            style "pd_tertiary_button_small"
                                            action Function(pd_clear_action_pair, action_id)

                            if not action_pairs:
                                text _("Connect each action to its owner.") style "pd_bucket_empty_text" xmaximum 210

            frame:
                style "pd_inner_panel_frame"
                xpos 330
                ypos 458
                xsize 284
                ysize 198

                fixed:
                    xfill True
                    yfill True
                    text _("PIC / Owners") style "pd_inner_panel_title" xpos 14 ypos 12

                    vpgrid:
                        xpos 14
                        ypos 44
                        xsize 254
                        ysize 136
                        cols 2
                        spacing 7
                        draggable True
                        mousewheel True
                        scrollbars "vertical"

                        for pic in case.get("pics", []):
                            button:
                                style "pd_pic_button"
                                xsize 120
                                ysize 62
                                action Function(pd_assign_selected_action, pic["id"])

                                vbox:
                                    spacing 2
                                    xalign 0.5
                                    yalign 0.5
                                    text _(pic["name"]) style "pd_pic_name" xalign 0.5 xmaximum 108
                                    text _(pic["role"]) style "pd_pic_role" xalign 0.5 xmaximum 108

            textbutton _("Submit Solution"):
                style "pd_primary_button_alt"
                xpos 22
                ypos 690
                xsize 592
                ysize 50
                action [Function(pd_submit_phase_2), Return(True)]
                sensitive bool(action_pairs)


screen problem_diagnosis_header(case, phase):
    $ current_step = 1 if phase == 1 else 2
    $ score_value = pd_state.get("phase_1_score", 0) if phase == 1 else pd_state.get("phase_2_score", 0)
    $ attempts_left = pd_state.get("attempts_left", 0)
    $ max_attempts = case.get("max_attempts", pd_state.get("max_attempts", 3))

    fixed:
        xpos 0
        ypos 0
        xsize 1920
        ysize 96

        textbutton _("‹  Back"):
            style "pd_back_button"
            xpos 28
            ypos 20
            xsize 144
            ysize 54
            action [Function(pd_exit_current_case), Return(True)]

        vbox:
            xpos 574
            ypos 12
            xsize 760
            spacing 1

            text _(case.get("title", "Project Diagnosis")) style "pd_header_title" xalign 0.5
            hbox:
                xalign 0.5
                spacing 14
                text "──◇" style "pd_header_ornament"
                text _(case.get("subtitle_phase_1") if phase == 1 else case.get("subtitle_phase_2")) style "pd_header_subtitle"
                text "◇──" style "pd_header_ornament"

        hbox:
            xpos 1300
            ypos 24
            spacing 22

            for step in range(1, 5):
                vbox:
                    spacing 5
                    frame:
                        style ("pd_step_active" if step == current_step else "pd_step_idle")
                        xsize 24
                        ysize 24
                    text "[step]" style ("pd_step_label_active" if step == current_step else "pd_step_label") xalign 0.5

        frame:
            style "pd_score_frame"
            xpos 1590
            ypos 18
            xsize 286
            ysize 68

            hbox:
                xalign 0.5
                yalign 0.5
                spacing 28

                vbox:
                    spacing 3
                    text _("Score") style "pd_score_label"
                    text "★  [score_value]" style "pd_score_value"

                add Solid("#ffffff3a") xsize 1 ysize 42

                vbox:
                    spacing 3
                    text _("Attempts") style "pd_score_label"
                    text "♥  [attempts_left] / [max_attempts]" style "pd_attempts_value"


screen problem_diagnosis_footer(case, phase):
    frame:
        style "pd_footer_frame"
        xpos 36
        ypos 920
        xsize 1540
        ysize 112

        fixed:
            xfill True
            yfill True

            hbox:
                xpos 22
                ypos 18
                spacing 22

                textbutton _("?  Hint"):
                    style "pd_footer_button"
                    xsize 180
                    ysize 50
                    action Function(pd_use_hint)

                textbutton _("↻  Reset"):
                    style "pd_footer_button"
                    xsize 180
                    ysize 50
                    action Function(pd_reset_current_phase)

            text _("Hints left: [pd_state.get('hints_left', 0)]") style "pd_footer_meta" xpos 62 ypos 78
            text _("Clear selections") style "pd_footer_meta" xpos 272 ypos 78

            frame:
                style "pd_avatar_frame"
                xpos 486
                ypos 6
                xsize 88
                ysize 88
                text "M" style "pd_avatar_text" xalign 0.5 yalign 0.5

            vbox:
                xpos 612
                ypos 20
                xsize 828
                spacing 5
                text _(case.get("guide_name", "Minh")) style "pd_dialogue_name"
                text _(case.get("guide_quote_phase_1") if phase == 1 else case.get("guide_quote_phase_2")) style "pd_dialogue_quote" xmaximum 810
                if pd_state.get("feedback_message", ""):
                    text _(pd_state.get("feedback_message", "")) style "pd_feedback_text" xmaximum 810

    frame:
        style "pd_notes_frame"
        xpos 1600
        ypos 936
        xsize 282
        ysize 86

        fixed:
            xfill True
            yfill True
            textbutton _("▤  Project Notes"):
                style "pd_notes_button"
                xpos 14
                ypos 12
                xsize 252
                ysize 38
                action Function(pd_show_notes)
            text _(case.get("description", "Review background")) style "pd_footer_meta" xpos 36 ypos 56 xmaximum 210


screen problem_diagnosis_debug_menu():
    tag menu

    use game_menu(_("Problem Diagnosis Debug"), scroll="viewport"):

        vbox:
            spacing 22

            text _("Launch the standalone diagnosis case from here without wiring it into a story chapter yet."):
                style "route_map_summary"

            text _("Debugging Mode must stay enabled for these tools to be useful inside the normal game flow."):
                style "route_map_summary"

            frame:
                style "route_map_panel"

                vbox:
                    spacing 12

                    text _("Demo Case"):
                        style "route_map_route_title"

                    text _("[pd_get_case('case_scope_creep_01').get('case_title', '')] — [pd_get_case('case_scope_creep_01').get('description', '')]"):
                        style "route_map_summary"

                    textbutton _("Launch Problem Diagnosis"):
                        action Function(pd_debug_launch_case, "case_scope_creep_01")

            if pd_debug_last_result:
                frame:
                    style "route_map_panel"

                    vbox:
                        spacing 10

                        text _("Latest Result"):
                            style "route_map_route_title"

                        text _("Tier: [pd_get_result_tier_label(pd_debug_last_result)]") style "route_map_summary"
                        text _("Phase 1 Score: [pd_debug_last_result.get('phase_1_score', 0)]") style "route_map_summary"
                        text _("Phase 2 Score: [pd_debug_last_result.get('phase_2_score', 0)]") style "route_map_summary"
                        text _("Total Score: [pd_debug_last_result.get('total_score', 0)]") style "route_map_summary"
                        text _("Insights: [', '.join(pd_debug_last_result.get('generated_insights', [])) if pd_debug_last_result.get('generated_insights') else 'None']") style "route_map_summary"
