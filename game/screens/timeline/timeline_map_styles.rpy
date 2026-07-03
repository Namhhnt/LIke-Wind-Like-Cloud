style timeline_title is gui_text
style timeline_subtitle is gui_text
style timeline_back_button is button
style timeline_back_button_text is button_text
style timeline_route_tab is button
style timeline_route_tab_selected is button
style timeline_route_tab_text is button_text
style timeline_route_tab_text_selected is button_text
style timeline_map_panel is frame
style timeline_scroll_hint is gui_text
style timeline_empty_state is gui_text
style timeline_node is button
style timeline_node_selected is button
style timeline_node_code is gui_text
style timeline_node_title is gui_text
style timeline_status_completed_icon is gui_text
style timeline_status_completed_text is gui_text
style timeline_status_current_icon is gui_text
style timeline_status_current_text is gui_text
style timeline_status_locked_icon is gui_text
style timeline_status_locked_text is gui_text
style timeline_badge_bonus is gui_text
style timeline_badge_pov is gui_text
style timeline_detail_panel is frame
style timeline_detail_title is gui_text
style timeline_detail_summary is gui_text
style timeline_detail_meta is gui_text
style timeline_detail_meta_locked is gui_text
style timeline_requirements_title is gui_text
style timeline_requirement_text is gui_text
style timeline_stat_text is gui_text
style timeline_play_button is button
style timeline_play_button_text is button_text
style timeline_secondary_button is button
style timeline_secondary_button_text is button_text
style timeline_legend_panel is frame
style timeline_legend_title is gui_text

style timeline_footer_text is gui_text
style timeline_footer_hint is gui_text

style timeline_title:
    size 54
    bold True
    color "#f5d7a6"
    outlines [(2, "#1a0e05", 0, 0)]

style timeline_subtitle:
    size 22
    color "#eadac4"
    outlines [(1, "#00000099", 0, 0)]

style timeline_back_button:
    background Solid("#1a1510cc")
    hover_background Solid("#3a2c1ecc")
    xysize (170, 56)
    xpadding 18
    ypadding 10

style timeline_back_button_text:
    size 22
    color "#f5e5cb"
    hover_color "#ffddaa"

style timeline_route_tab:
    background Solid("#18120ecc")
    hover_background Solid("#312419dd")
    xysize (160, 50)
    xpadding 16
    ypadding 8

style timeline_route_tab_selected:
    background Solid("#a8743bdd")
    hover_background Solid("#c98a48ee")
    xysize (160, 50)
    xpadding 16
    ypadding 8

style timeline_route_tab_text:
    size 24
    color "#d6c5ad"
    hover_color "#ffddaa"

style timeline_route_tab_text_selected:
    size 24
    bold True
    color "#ffffff"

style timeline_map_panel:
    background Solid("#111111d6")
    xpadding 0
    ypadding 0

style timeline_scroll_hint:
    size 17
    color "#cfba9b"

style timeline_empty_state:
    size 26
    color gui.idle_small_color
    text_align 0.5

style timeline_node:
    background Solid("#1b1714ee")
    hover_background Solid("#2a221cee")
    xpadding 0
    ypadding 0

style timeline_node_selected:
    background Solid("#684321ee")
    hover_background Solid("#7e5228ee")
    xpadding 0
    ypadding 0

style timeline_node_code:
    size 20
    color "#f5d7a6"
    bold True
    align (0.5, 0.5)

style timeline_node_title:
    size 20
    color "#fff8ed"

style timeline_status_completed_icon:
    size 18
    color "#9fe0b1"
    align (1.0, 1.0)

style timeline_status_completed_text:
    size 16
    color "#9fe0b1"
    align (1.0, 1.0)

style timeline_status_current_icon:
    size 18
    color "#f5d7a6"
    align (1.0, 1.0)

style timeline_status_current_text:
    size 16
    color "#f5d7a6"

style timeline_status_locked_icon:
    size 18
    color "#bda98f"
    align (1.0, 1.0)

style timeline_status_locked_text:
    size 16
    color "#bda98f"
    align (1.0, 1.0)

style timeline_badge_bonus:
    size 14
    color "#2a1600"
    background Solid("#f0cc72")
    xpadding 8
    ypadding 2

style timeline_badge_pov:
    size 14
    color "#201205"
    background Solid("#d6b0ff")
    xpadding 8
    ypadding 2

style timeline_detail_panel:
    background Solid("#110d0bf0")
    xpadding 0
    ypadding 0

style timeline_detail_title:
    size 32
    bold True
    color "#fff4e4"

style timeline_detail_summary:
    size 18
    color "#eadac4"
    line_spacing 3

style timeline_detail_meta:
    size 18
    color "#cfba9b"

style timeline_detail_meta_locked:
    size 18
    color "#d7a1a1"

style timeline_requirements_title:
    size 18
    bold True
    color "#f5d7a6"

style timeline_requirement_text:
    size 15
    color "#eadac4"

style timeline_stat_text:
    size 14
    color "#cfba9b"

style timeline_play_button:
    background Solid("#8a5d2f")
    hover_background Solid("#a8743b")
    insensitive_background Solid("#463427")
    xysize (210, 50)
    xpadding 16
    ypadding 8

style timeline_play_button_text:
    size 18
    bold True
    color "#fff9ef"
    insensitive_color "#c3b09d"

style timeline_secondary_button:
    background Solid("#251c16")
    hover_background Solid("#39281b")
    xysize (210, 48)
    xpadding 16
    ypadding 8

style timeline_secondary_button_text:
    size 18
    color "#eadac4"
    hover_color "#fff4e4"

style timeline_legend_panel:
    background Solid("#16110eea")
    xpadding 0
    ypadding 0

style timeline_legend_title:
    size 28
    bold True
    color "#f5d7a6"

style timeline_footer_text:
    size 18
    color "#cfba9b"

style timeline_footer_hint:
    size 17
    color "#bda98f"

style timeline_lane_label_frame is frame
style timeline_lane_label_text is gui_text
style timeline_time_marker_text is gui_text

style timeline_lane_label_frame:
    background Solid("#1a1510aa")
    xpadding 0
    ypadding 0

style timeline_lane_label_text:
    size 16
    bold True
    color "#f5d7a6"
    text_align 0.5

style timeline_time_marker_text:
    size 22
    bold True
    color "#fff4e4"
    outlines [(1, "#2b0611", 0, 0)]
