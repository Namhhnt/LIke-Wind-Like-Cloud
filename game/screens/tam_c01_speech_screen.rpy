# ============================================================
# Tam Route - Chapter 01 Speech Mini-game Screen
# ============================================================

transform tam_speech_portrait_pos:
    xpos 92
    ypos 154
    zoom 0.9


screen tam_speech_minigame(items, attempt=1, can_skip=False):

    modal True
    zorder 100

    default picked = []
    $ speech_variant = tam_speech_variant()
    $ max_choices = speech_variant.get("max_choices", 4)
    $ max_attempts = speech_variant.get("max_attempts", 3)

    fixed:
        xysize (1920, 1080)

        add "bg_interview_room"
        add Solid("#140e0acc")

        add "images/characters/tam/expressions/tam_serious.webp" at tam_speech_portrait_pos

        vbox:
            xpos 560
            ypos 42
            xsize 1210
            spacing 8

            text _("Tam's Speech") style "tam_speech_title" xalign 0.5
            text _("Arrange the key points for the interview answer") style "tam_speech_subtitle" xalign 0.5

        hbox:
            xpos 500
            ypos 154
            spacing 16

            frame:
                style "tam_speech_progress_badge"
                xysize (220, 64)

                text _("Selected [len(picked)] / [max_choices]") style "tam_speech_progress_text" xalign 0.5 yalign 0.5

            for i in range(max_choices):
                if i < len(picked):
                    $ chip_label = tam_speech_short_labels().get(picked[i], picked[i])

                    frame:
                        style "tam_speech_selected_chip"
                        xysize (228, 64)

                        hbox:
                            xalign 0.5
                            yalign 0.5
                            spacing 8

                            text "[i + 1]" style "tam_speech_chip_number"
                            text "[chip_label]" style "tam_speech_chip_text"
                            text "✓" style "tam_speech_chip_check"
                else:
                    frame:
                        style "tam_speech_empty_chip"
                        xysize (140, 64)

                        text "[i + 1]" style "tam_speech_empty_chip_text" xalign 0.5 yalign 0.5

        frame:
            style "tam_speech_main_panel"
            xpos 470
            ypos 250
            xysize (1290, 690)

            vbox:
                spacing 20

                hbox:
                    spacing 18
                    box_wrap True
                    xfill True

                    text _("Attempt [attempt] / [max_attempts]") style "tam_speech_panel_kicker"

                    if can_skip:
                        text _("Skip unlocked after [max_attempts] failed attempts") style "tam_speech_warning"
                    else:
                        text _("Choose all 4 points. You can reorder them before confirming") style "tam_speech_hint"

                    text _("Choose the points Tam should use in her answer. Pick all the right points to pass; get both the points and the order right for a better reward.") style "tam_speech_body"

                vpgrid:
                    cols 2
                    xfill True
                    ysize 430
                    spacing 16
                    draggable True
                    mousewheel True
                    scrollbars "vertical"

                    for item in items:
                        button:
                            style "tam_speech_choice_button"
                            selected item["id"] in picked
                            action Function(tam_speech_toggle_choice, picked, item["id"])

                            text item["label"] style "tam_speech_choice_text"

                hbox:
                    xfill True
                    spacing 18

                    text _("Tap a selected point again to remove it and adjust the order.") style "tam_speech_footer"

                    null width 20

                    textbutton _("Reset"):
                        style "tam_speech_secondary_button"
                        text_style "tam_speech_secondary_button_text"
                        action SetScreenVariable("picked", [])

                    textbutton _("Confirm"):
                        style "tam_speech_primary_button"
                        text_style "tam_speech_primary_button_text"
                        action Return({"action": "confirm", "picked": list(picked)})
                        sensitive len(picked) == 4

                    if can_skip:
                        textbutton _("Skip"):
                            style "tam_speech_skip_button"
                            text_style "tam_speech_skip_button_text"
                            action Return({"action": "skip"})


style tam_speech_title is default:
    size 42
    bold True
    color "#f7ebdd"


style tam_speech_subtitle is default:
    size 25
    color "#dcc8b1"


style tam_speech_progress_badge is frame:
    background "#3f2a1db8"
    padding (18, 10)


style tam_speech_progress_text is default:
    size 24
    bold True
    color "#fff2df"


style tam_speech_selected_chip is frame:
    background "#e7c9a680"
    padding (14, 10)


style tam_speech_empty_chip is frame:
    background "#ffffff14"
    padding (12, 10)


style tam_speech_chip_number is default:
    size 22
    bold True
    color "#4c2d18"


style tam_speech_chip_text is default:
    size 19
    color "#3b2418"


style tam_speech_chip_check is default:
    size 20
    bold True
    color "#6b8f57"


style tam_speech_empty_chip_text is default:
    size 22
    bold True
    color "#cfb59c"


style tam_speech_main_panel is frame:
    background "#211713e8"
    padding (34, 30)


style tam_speech_panel_kicker is default:
    size 23
    bold True
    color "#f6d7b0"


style tam_speech_warning is default:
    size 22
    color "#f0c7a2"


style tam_speech_hint is default:
    size 22
    color "#d7c0ab"


style tam_speech_body is default:
    size 24
    color "#f7efe8"
    line_spacing 3


style tam_speech_choice_button is button:
    background "#f3e5d114"
    hover_background "#9d765145"
    selected_background "#d7b28a99"
    selected_hover_background "#e5c4a3bb"
    xsize 590
    yminimum 138
    padding (24, 20)


style tam_speech_choice_text is button_text:
    size 22
    color "#f7f0e8"
    selected_color "#2f1d14"
    hover_color "#fff5e3"
    xmaximum 530
    line_spacing 3
    layout "subtitle"


style tam_speech_footer is default:
    size 20
    color "#bfa995"


style tam_speech_primary_button is button:
    background "#c69464"
    hover_background "#ddb083"
    insensitive_background "#634d3a"
    padding (28, 14)


style tam_speech_primary_button_text is button_text:
    size 22
    bold True
    color "#23150d"
    hover_color "#23150d"
    insensitive_color "#c7b8a9"


style tam_speech_secondary_button is button:
    background "#ffffff12"
    hover_background "#ffffff20"
    padding (26, 14)


style tam_speech_secondary_button_text is button_text:
    size 21
    color "#f1e5d8"
    hover_color "#fff5eb"


style tam_speech_skip_button is button:
    background "#4f3a2c"
    hover_background "#6a4b37"
    padding (26, 14)


style tam_speech_skip_button_text is button_text:
    size 21
    color "#f4dfcc"
    hover_color "#fff4ea"
