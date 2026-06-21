# ============================================================
# Tâm Route - Chapter 01 Speech Mini-game Screen
# ============================================================

screen tam_speech_choice_screen(items, picked):

    modal True
    zorder 100

    frame:
        style "tam_speech_panel"
        xalign 0.5
        yalign 0.5
        xsize 1680
        ymaximum 860

        vbox:
            spacing 18

            text "Chọn ý tiếp theo trong phần trả lời" style "tam_speech_title"

            text "Đã chọn: [len(picked)] / 4" style "tam_speech_hint"

            if picked:
                hbox:
                    spacing 10

                    for idx, item_id in enumerate(picked):
                        frame:
                            style "tam_speech_picked_slot"
                            xsize 380
                            ysize 76

                            text "[idx + 1]. [tam_speech_short_labels[item_id]]" style "tam_speech_picked_text"

            else:
                text "Chưa chọn ý nào." style "tam_speech_hint"

            null height 6

            vpgrid:
                cols 2
                xsize 1600
                ysize 560
                spacing 14
                draggable True
                mousewheel True
                scrollbars "vertical"

                for item in items:
                    textbutton item["label"]:
                        style "tam_speech_choice_button"
                        text_style "tam_speech_choice_text"
                        action Return(item["id"])

            text "Có thể dùng chuột lăn hoặc kéo để xem thêm lựa chọn." style "tam_speech_footer"


style tam_speech_panel is frame:
    background "#111111"
    padding (36, 32)


style tam_speech_title is default:
    size 36
    bold True
    color "#FFFFFF"


style tam_speech_hint is default:
    size 24
    color "#CCCCCC"


style tam_speech_footer is default:
    size 20
    color "#999999"


style tam_speech_picked_slot is frame:
    background "#2A2A2A"
    padding (12, 8)


style tam_speech_picked_text is default:
    size 19
    color "#FFFFFF"
    line_spacing 1


style tam_speech_choice_button is button:
    background "#242424"
    hover_background "#3A3328"
    insensitive_background "#181818"
    xsize 760
    yminimum 104
    padding (18, 14)


style tam_speech_choice_text is button_text:
    size 21
    color "#FFFFFF"
    hover_color "#FFDDAA"
    insensitive_color "#777777"
    xmaximum 710
    line_spacing 2
    layout "subtitle"
    outlines [(1, "#000000", 0, 0)]