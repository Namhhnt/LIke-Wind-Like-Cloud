# Shared production controls. Icons save space, not touch-target area.
screen library_media_action(label, icon, action):
    if ui_is_compact():
        button:
            xysize (112, 104)
            padding (18, 14)
            background ui_panel("#4b392bf2", "#b79868", radius=20)
            hover_background ui_panel("#76583bf2", "#e1bc83", radius=20)
            action action
            alt label
            tooltip label
            add ui_icon(icon, medallion=False) xysize (72, 72) align (0.5, 0.5)
    else:
        textbutton label:
            style_prefix "library_story_button"
            action action
