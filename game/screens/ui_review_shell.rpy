# Review-only entry point. Live navigation is deliberately unchanged until the
# four representative layouts have been reviewed.
init -9 python:
    UI_REVIEW_COLORS = dict(
        canvas="#241e19ee", panel="#322920f2", text="#f5e8d2",
        muted="#cdbb9e", accent="#d6b477", border="#8f7755",
    )
    UI_REVIEW_SPACING = (8, 16, 24, 32, 48)

screen ui_review_shell(title, compact=False):
    add "gui/theme/refined/rainy_library_v2.png" fit "cover"
    add Solid("#140e09a0")

    text title:
        pos (96, 40)
        font "fonts/NotoSerif-Regular.ttf"
        size (58 if compact else 64)
        color UI_REVIEW_COLORS["text"]

    textbutton _("Back"):
        pos (1512, 32)
        xysize (312, 112)
        background ui_panel("#322920f2", "#8f7755", radius=24)
        hover_background ui_panel("#57422ff5", "#d6b477", radius=24)
        text_font "fonts/NotoSerif-Regular.ttf"
        text_size (42 if compact else 32)
        text_color "#f5e8d2"
        text_xalign 0.5
        text_yalign 0.5
        action ShowMenu("ui_review_hub", compact=compact)

    fixed:
        pos (96, 176)
        xysize (1728, 820)
        transclude

    key "game_menu" action ShowMenu("ui_review_hub", compact=compact)

screen ui_review_hub(compact=False):
    tag menu
    add "gui/theme/refined/rainy_library_v2.png" fit "cover"
    add Solid("#140e09bb")
    vbox:
        align (0.5, 0.5)
        spacing 24
        for title, target in [
            (_("Preferences"), "ui_review_settings"),
            (_("Library"), "ui_review_library"),
            (_("Messages"), "ui_review_phone"),
            (_("Original Stories"), "ui_review_reader"),
        ]:
            textbutton title:
                xysize (900, 112)
                background ui_panel("#322920f2", "#8f7755", radius=24)
                hover_background ui_panel("#57422ff5", "#d6b477", radius=24)
                text_font "fonts/NotoSerif-Regular.ttf"
                text_size 42
                text_color "#f5e8d2"
                action ShowMenu(target, compact=compact)
        textbutton ("PC  /  Mobile landscape"):
            xysize (900, 112)
            text_size 42
            action ToggleScreenVariable("compact")
        textbutton _("Return"):
            xysize (900, 112)
            text_size 42
            action ShowMenu("main_menu")
    key "game_menu" action ShowMenu("main_menu")

label ui_review:
    call screen ui_review_hub
    return
