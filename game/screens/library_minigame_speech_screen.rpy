# FILE: game/screens/library_minigame_speech_screen.rpy
# Generic speech-order minigame screen for library replay.
# Used when replaying any speech_order variant from Library -> Minigames.
# This is a simplified version without character-specific art.

transform lib_speech_portrait_pos:
    xpos 92
    ypos 154
    zoom 0.9


screen lib_speech_minigame(items, variant, attempt=1, can_skip=False):

    modal True
    zorder 100

    default picked = []
    $ max_choices = variant.get("max_choices", 4)
    $ max_attempts = variant.get("max_attempts", 3)
    $ short_labels = tam_speech_short_labels_for_variant(variant)
    $ variant_title = variant.get("title", _("Speech"))

    fixed:
        xysize (1920, 1080)

        add Solid("#2a201a")
        add Solid("#140e0acc")

        vbox:
            xpos 560
            ypos 42
            xsize 1210
            spacing 8

            text variant_title style "tam_speech_title" xalign 0.5
            text _("Arrange the key points in the right order") style "tam_speech_subtitle" xalign 0.5

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
                    $ chip_label = short_labels.get(picked[i], picked[i])

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
                    xfill True

                    text _("Attempt [attempt] / [max_attempts]") style "tam_speech_panel_kicker"

                    if can_skip:
                        text _("Skip unlocked") style "tam_speech_warning"
                    else:
                        text _("Select all [max_choices] points in the right order") style "tam_speech_hint"

                    text _("Choose the points that matter and arrange them in the best order.") style "tam_speech_body"

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
                            action Function(tam_speech_toggle_choice_generic, picked, item["id"], max_choices)

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
                        sensitive len(picked) == max_choices

                    if can_skip:
                        textbutton _("Skip"):
                            style "tam_speech_skip_button"
                            text_style "tam_speech_skip_button_text"
                            action Return({"action": "skip"})
