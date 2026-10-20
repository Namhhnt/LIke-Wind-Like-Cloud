init -2:
    define LIB_TEXT = "#F5E8D0"
    define LIB_MUTED = "#C9B89A"
    define LIB_GOLD = "#E8C27A"
    define LIB_GOLD_DARK = "#B98A4A"
    define LIB_PANEL = "#16120FCC"
    define LIB_PANEL_SOFT = "#211A16EE"
    define LIB_PANEL_HOVER = "#33261BF2"
    define LIB_DISABLED = "#8A8173"
    define LIB_BORDER = "#C99B5F"

style library_title_text is default:
    color LIB_TEXT
    size 72
    font gui.interface_text_font
    outlines [(1, "#5A3A1A99", 0, 2)]

style library_subtitle_text is default:
    color LIB_TEXT
    size 28
    font gui.interface_text_font
    outlines [(1, "#00000055", 0, 1)]

style library_sidebar_text is button_text:
    color LIB_TEXT
    hover_color LIB_GOLD
    insensitive_color LIB_DISABLED
    size 28
    font gui.interface_text_font

style library_card_icon_text is default:
    color LIB_GOLD
    size 34
    font gui.interface_text_font
    text_align 0.0

style library_card_title is default:
    color LIB_TEXT
    size 30
    font gui.interface_text_font
    outlines [(1, "#00000066", 0, 1)]

style library_card_subtitle is default:
    color LIB_MUTED
    size 22
    line_spacing 4
    font gui.interface_text_font

style library_card_progress is default:
    color LIB_GOLD
    size 18
    font gui.interface_text_font

style library_card_arrow is default:
    color LIB_GOLD
    size 34
    font gui.interface_text_font

style library_compact_card_title is default:
    color LIB_TEXT
    size 44
    font gui.interface_text_font
    outlines [(1, "#00000088", 0, 1)]

style library_compact_card_subtitle is default:
    color LIB_MUTED
    size 34
    line_spacing 6
    font gui.interface_text_font

style library_compact_card_progress is default:
    color LIB_GOLD
    size 32
    font gui.interface_text_font

style library_compact_card_arrow is default:
    color LIB_GOLD
    size 48
    font "DejaVuSans.ttf"

style library_placeholder_title is default:
    color LIB_TEXT
    size 42
    font gui.interface_text_font

style library_placeholder_body is default:
    color LIB_MUTED
    size 24
    line_spacing 6
    font gui.interface_text_font

style library_back_button_text is button_text:
    color LIB_TEXT
    hover_color LIB_GOLD
    insensitive_color LIB_DISABLED
    size 28
    font gui.interface_text_font

style library_story_card_title is default:
    color LIB_TEXT
    size 34
    font gui.interface_text_font
    outlines [(1, "#00000066", 0, 1)]

style library_story_card_subtitle is default:
    color LIB_GOLD
    size 22
    font gui.interface_text_font

style library_story_meta is default:
    color LIB_MUTED
    size 21
    line_spacing 4
    font gui.interface_text_font

style library_story_status_text is default:
    color LIB_GOLD
    size 24
    font gui.interface_text_font

style library_story_summary_text is default:
    color LIB_TEXT
    size 22
    font gui.interface_text_font

style library_story_player_title is default:
    color LIB_TEXT
    size 30
    font gui.interface_text_font

style library_story_speaker is default:
    color LIB_GOLD
    size 24
    font gui.interface_text_font

style library_story_text is default:
    color LIB_TEXT
    size 26
    line_spacing 8
    font gui.interface_text_font

style library_story_button_button is button:
    background ui_panel("#2c2018cc", "#c3a67688", radius=16)
    hover_background ui_panel("#76583bcc", "#e1bc83dd", radius=16)
    insensitive_background ui_panel("#22191488", "#c3a67644", radius=16)
    padding (22, 8)

style library_story_button_text is button_text:
    color LIB_TEXT
    hover_color "#fff4dd"
    insensitive_color LIB_DISABLED
    size 24
    font gui.interface_text_font
