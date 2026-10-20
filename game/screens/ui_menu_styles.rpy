# Core menu controls share the Library palette and cached, anti-aliased panels.
# Keep actions and labels in screens.rpy so locale mappings remain unchanged.
style ui_menu_text is default:
    font gui.interface_text_font
    color "#f5e8d2"
    size 32

style ui_menu_heading is ui_menu_text:
    color "#d6b477"
    size 36

style ui_menu_option is button:
    padding (22, 10)
    background ui_panel("#241e19ee", "#8f7755", radius=14)
    hover_background ui_panel("#51402efc", "#d6b477", radius=14)
    selected_background ui_panel("#604b31fc", "#d6b477", radius=14)
    insensitive_background ui_panel("#241e19ee", "#655644", radius=14)

style ui_menu_option_text is ui_menu_text:
    size 30
    hover_color "#fff6e7"
    selected_color "#ffe1a8"
    insensitive_color "#8f806d"

style ui_menu_slider is bar:
    ysize 44
    left_bar Fixed(Transform(ui_panel("#d6b477", "#d6b477", radius=6), ysize=12, yalign=0.5))
    right_bar Fixed(Transform(ui_panel("#241e19", "#8f7755", radius=6), ysize=12, yalign=0.5))
    thumb Transform(ui_panel("#f5e8d2", "#8f7755", radius=9), xysize=(32, 44))
    thumb_shadow None
    thumb_offset 0
    thumb_align 0.5

style ui_menu_touch_slider is ui_menu_slider:
    ysize 104
    thumb Fixed(Transform(ui_panel("#f5e8d2", "#8f7755", radius=12), xysize=(48, 48), yalign=0.5), xysize=(48, 104))

screen ui_preference_option(caption, option_action, width=560, check=False, selected_override=None):
    $ selected_state = renpy.is_selected(option_action) if selected_override is None else selected_override
    button:
        style "ui_menu_option"
        xysize (width, 104 if ui_is_compact() else 68)
        action option_action
        selected selected_state
        hbox:
            yalign 0.5
            spacing 18
            text (("\u25a0" if selected_state else "\u25a1") if check else ("\u25cf" if selected_state else "\u25cb")):
                font "DejaVuSans.ttf"
                size (40 if ui_is_compact() else 28)
                color "#d6b477"
            text caption:
                style "ui_menu_option_text"
                size (40 if ui_is_compact() else 28)
                yalign 0.5

screen ui_preference_slider(caption, preference_name, width=560):
    vbox:
        spacing 12
        xsize width
        text caption:
            style "ui_menu_text"
            size (44 if ui_is_compact() else 30)
        bar:
            id ("pref_" + preference_name.replace(" ", "_"))
            style ("ui_menu_touch_slider" if ui_is_compact() else "ui_menu_slider")
            xsize width
            value Preference(preference_name)

style pref_vbox:
    xsize 380

style pref_label:
    top_margin 8
    bottom_margin 16

style pref_label_text:
    font gui.interface_text_font
    color LIB_GOLD
    size 30

style radio_button:
    xsize 374
    yminimum 52
    padding (18, 10)
    foreground None
    background ui_panel("#3c332b55", "#c3a67644", radius=18)
    hover_background ui_panel("#96734577", "#c3a676bb", radius=18)
    selected_background ui_panel("#96734599", "#e4bf7abb", radius=18)

style check_button:
    xsize 374
    yminimum 52
    padding (18, 10)
    foreground None
    background ui_panel("#3c332b55", "#c3a67644", radius=18)
    hover_background ui_panel("#96734577", "#c3a676bb", radius=18)
    selected_background ui_panel("#96734599", "#e4bf7abb", radius=18)

style radio_button_text:
    font gui.interface_text_font
    size 26
    color LIB_TEXT
    selected_color LIB_GOLD
    hover_color "#fff4dd"
    insensitive_color LIB_DISABLED

style check_button_text:
    font gui.interface_text_font
    size 26
    color LIB_TEXT
    selected_color LIB_GOLD
    hover_color "#fff4dd"
    insensitive_color LIB_DISABLED

style slider_vbox:
    xsize 560
    spacing 12

style slider_slider:
    xsize 548
    ysize 18
    left_bar ui_panel("#b58d55", "#e8c27aaa", radius=8)
    right_bar ui_panel("#211a16cc", "#c3a67666", radius=8)
    thumb Transform(ui_panel("#f5e8d0", "#e8c27a", radius=6), xysize=(18, 18))
    thumb_shadow None
    thumb_offset 0
    thumb_align 0.5
    xmaximum 548

style slot_button:
    xsize 394
    ysize 255
    padding (15, 12)
    background ui_panel("#241e19ee", "#8f7755", radius=18)
    hover_background ui_panel("#51402efc", "#d6b477", radius=18)
    selected_background ui_panel("#604b31fc", "#d6b477", radius=18)

style page_button:
    background None
    hover_background ui_panel("#96734577", radius=16)
    selected_background ui_panel("#96734599", "#e4bf7abb", radius=16)

style page_button_text:
    font gui.interface_text_font
    size 26
    color LIB_TEXT
    selected_color LIB_GOLD
    hover_color LIB_GOLD

style page_label_text:
    size 32
    color LIB_GOLD

style slot_time_text:
    size 18
    color LIB_MUTED

style slot_name_text:
    size 16
    color LIB_TEXT
    ymaximum 24

style history_text:
    xsize 860
    min_width 860

style help_button:
    padding (18, 10)
    background ui_panel("#3c332b55", "#c3a67644", radius=18)
    hover_background ui_panel("#96734577", radius=18)
    selected_background ui_panel("#96734599", "#e4bf7abb", radius=18)
    yminimum 64

style help_button_text:
    font gui.interface_text_font
    size 26
    color LIB_TEXT
    selected_color LIB_GOLD
    hover_color LIB_GOLD

style help_text:
    font gui.interface_text_font
    color "#f5e8d2"
    size 30
    xsize 870

style help_label:
    xsize 300
    right_padding 24

style help_label_text:
    font gui.interface_text_font
    color "#d6b477"
    size 28

style ui_touch_help_button is ui_menu_option:
    yminimum 104
    xminimum 320

style ui_touch_help_button_text is ui_menu_option_text:
    size 40

style ui_touch_help_label is help_label:
    xsize 420

style ui_touch_help_label_text is help_label_text:
    size 40

style ui_touch_help_text is help_text:
    size 40
    xsize 1200

style about_text:
    font gui.interface_text_font
    color "#f5e8d2"

style about_label_text:
    font gui.interface_text_font
    color "#d6b477"

style confirm_frame:
    background ui_panel("#302923f0", "#c3a676bb", radius=32, ornate=True)
    padding (48, 36)

style confirm_prompt_text:
    font gui.interface_text_font
    color LIB_TEXT
    size 32
    xmaximum 900

style confirm_button:
    padding (32, 12)
    background ui_panel("#50473e88", "#c3a676aa", radius=22)
    hover_background ui_panel("#967345bb", "#e4bf7abb", radius=22)

style confirm_button_text:
    font gui.interface_text_font
    color LIB_TEXT
    hover_color LIB_GOLD
    size 28

