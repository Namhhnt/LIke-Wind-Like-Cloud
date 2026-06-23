# -----------------------------------------------------------------------------
# Asset-free styles
# -----------------------------------------------------------------------------

style pd_panel_frame is default:
    background "#e7dfd1e8"
    padding (0, 0)

style pd_panel_header_bar is default:
    background "#102033"
    padding (0, 0)

style pd_panel_title is default:
    color "#f5ead9"
    size 26
    bold True
    outlines [(2, "#00000066", 0, 1)]

style pd_panel_icon is default:
    color "#f5ead9"
    size 30
    bold True
    outlines [(2, "#00000066", 0, 1)]

style pd_panel_hint_light is default:
    color "#f4efe6"
    size 17
    line_spacing 2
    outlines [(1, "#00000080", 0, 1)]

style pd_panel_hint_dark is default:
    color "#172231"
    size 17
    line_spacing 2

style pd_help_mark is default:
    color "#f5ead9"
    size 20
    bold True
    text_align 0.5
    outlines [(2, "#000000aa", 0, 0)]

style pd_panel_arrow is default:
    color "#ffe8a6"
    size 58
    bold True
    outlines [(4, "#000000aa", 0, 0), (2, "#ffe8a644", 0, 0)]

style pd_count_badge is default:
    background "#ffffffcc"
    padding (0, 0)

style pd_count_badge_light is default:
    background "#f8f0e5cc"
    padding (0, 0)

style pd_count_badge_text is default:
    color "#102033"
    size 17
    bold True

style pd_count_badge_text_dark is default:
    color "#102033"
    size 17
    bold True

style pd_card_button is button:
    background "#f3eadc"
    hover_background "#fff6e8"
    selected_background "#dce8f4"
    insensitive_background "#d8d0c3"
    padding (9, 7)
    yminimum 70

style pd_compact_card_button is pd_card_button:
    yminimum 50
    padding (8, 6)

style pd_action_button is pd_card_button:
    yminimum 70

style pd_card_icon_frame is default:
    background "#2e6270"
    padding (0, 0)

style pd_card_icon_frame_insight is default:
    background "#6f8a62"
    padding (0, 0)

style pd_card_icon_text is default:
    color "#f8f0e5"
    size 18
    bold True

style pd_card_title is default:
    color "#191817"
    size 19
    bold True
    line_spacing 1

style pd_card_title_dark is pd_card_title:
    color "#172231"

style pd_card_body is default:
    color "#2d2a27"
    size 15
    line_spacing 1

style pd_card_body_dark is pd_card_body:
    color "#1f2d24"

style pd_card_meta is default:
    color "#8a6e51"
    size 13
    italic True

style pd_card_meta_emphasis is default:
    color "#0b6d78"
    size 13
    bold True

style pd_card_grip is default:
    color "#6a625c"
    size 23
    bold True

style pd_selected_stack_frame is default:
    background "#f0e8dcc8"
    padding (8, 6)

style pd_selected_data_slot is button:
    background "#dfe8f2"
    hover_background "#edf5ff"
    selected_background "#d4e3f3"
    padding (10, 7)
    yminimum 40

style pd_selected_data_text is default:
    color "#0f1722"
    size 18

style pd_selected_data_remove is default:
    color "#233044"
    size 22

style pd_down_marker is default:
    color "#8b8277"
    size 28
    bold True

style pd_primary_button is button:
    background "#112642"
    hover_background "#17345a"
    insensitive_background "#5c6670"
    padding (12, 7)

style pd_primary_button_text is default:
    color "#fff2df"
    hover_color "#ffffff"
    insensitive_color "#c8c1b8"
    size 23
    bold True

style pd_primary_button_alt is button:
    background "#006876"
    hover_background "#087d8d"
    insensitive_background "#59676b"
    padding (12, 7)

style pd_primary_button_alt_text is pd_primary_button_text

style pd_secondary_button is button:
    background "#8b6b37"
    hover_background "#a77f3f"
    insensitive_background "#9a8f7a"
    padding (8, 6)

style pd_secondary_button_text is default:
    color "#fff2df"
    hover_color "#ffffff"
    insensitive_color "#d5cec1"
    size 18
    bold True

style pd_secondary_button_alt is button:
    background "#0d6f80"
    hover_background "#128396"
    insensitive_background "#839094"
    padding (8, 6)

style pd_secondary_button_alt_text is pd_secondary_button_text

style pd_tertiary_button is button:
    background "#2e3440"
    hover_background "#414a59"
    padding (8, 6)

style pd_tertiary_button_text is default:
    color "#fff2df"
    hover_color "#ffffff"
    size 18

style pd_tertiary_button_small is pd_tertiary_button:
    padding (6, 4)

style pd_tertiary_button_small_text is default:
    color "#fff2df"
    hover_color "#ffffff"
    size 13

style pd_inline_icon_button is button:
    background None
    hover_background "#00000018"
    padding (2, 0)

style pd_inline_icon_text is default:
    color "#4b2d23"
    hover_color "#a73725"
    size 17
    bold True

style pd_success_frame is default:
    background "#dcebd7"
    padding (10, 8)

style pd_success_icon_frame is default:
    background "#6e9368"
    padding (0, 0)

style pd_success_icon_text is default:
    color "#fff8e8"
    size 18
    bold True

style pd_success_title is default:
    color "#182618"
    size 16
    bold True

style pd_placeholder_frame is default:
    background "#e8ded180"
    padding (12, 8)

style pd_placeholder_text is default:
    color "#756b5e"
    size 14
    italic True
    text_align 0.5

style pd_section_label is default:
    color "#6a4f32"
    size 16
    bold True

style pd_small_italic is default:
    color "#6c6257"
    size 14
    italic True
    text_align 0.5

style pd_info_icon is default:
    color "#f2eadf"
    size 20
    outlines [(2, "#00000080", 0, 0)]

style pd_bucket_frame_root is default:
    background "#f4e6c9e8"
    padding (0, 0)

style pd_bucket_frame_impact is default:
    background "#dff0f4e8"
    padding (0, 0)

style pd_bucket_icon_root is default:
    background "#a1803f"
    padding (0, 0)

style pd_bucket_icon_impact is default:
    background "#1c7e8d"
    padding (0, 0)

style pd_bucket_icon_text is default:
    color "#fff2df"
    size 18
    bold True

style pd_bucket_title is default:
    color "#7a4f13"
    size 22
    bold True

style pd_bucket_title_alt is default:
    color "#0f6b78"
    size 22
    bold True

style pd_bucket_counter is default:
    color "#241b12"
    size 17
    bold True

style pd_bucket_empty_text is default:
    color "#6e655b"
    size 14
    italic True
    line_spacing 2

style pd_bucket_card_root is default:
    background "#f6ecd8"
    padding (8, 6)

style pd_bucket_card_impact is default:
    background "#e7f4f8"
    padding (8, 6)

style pd_bucket_card_text is default:
    color "#1a1815"
    size 17
    line_spacing 1

style pd_inner_panel_frame is default:
    background "#f1e9dce0"
    padding (0, 0)

style pd_inner_panel_title is default:
    color "#172231"
    size 18
    bold True

style pd_filter_button is button:
    background "#ccb991"
    hover_background "#e2cfaa"
    selected_background "#142c4c"
    padding (10, 6)

style pd_filter_button_text is default:
    color "#1d1b18"
    hover_color "#000000"
    selected_color "#fff2df"
    size 14
    bold True

style pd_pair_frame is default:
    background "#e8ddce"
    padding (8, 6)

style pd_pair_title is default:
    color "#1d1b18"
    size 14
    bold True

style pd_pair_meta is default:
    color "#605243"
    size 12

style pd_pic_button is button:
    background "#e7f3f6"
    hover_background "#f1fbfd"
    selected_background "#cdebf1"
    padding (5, 4)

style pd_pic_button_text is default:
    color "#102033"
    size 14

style pd_pic_name is default:
    color "#102033"
    size 15
    bold True
    text_align 0.5

style pd_pic_role is default:
    color "#53606a"
    size 11
    text_align 0.5

style pd_back_button is button:
    background "#0e1b2ce6"
    hover_background "#172a44"
    padding (10, 6)

style pd_back_button_text is default:
    color "#fff2df"
    hover_color "#ffffff"
    size 24
    bold True

style pd_header_title is default:
    color "#fff2df"
    size 34
    bold True
    outlines [(3, "#00000088", 0, 1)]
    text_align 0.5

style pd_header_subtitle is default:
    color "#f2e5d1"
    size 21
    outlines [(2, "#00000088", 0, 1)]
    text_align 0.5

style pd_header_ornament is default:
    color "#b99d6d"
    size 14
    yalign 0.5

style pd_step_active is default:
    background "#ffd66c"
    padding (0, 0)

style pd_step_idle is default:
    background "#142236"
    padding (0, 0)

style pd_step_label is default:
    color "#d3c8b7"
    size 15

style pd_step_label_active is default:
    color "#ffd66c"
    size 15
    bold True

style pd_score_frame is default:
    background "#0e1b2ce6"
    padding (12, 8)

style pd_score_label is default:
    color "#d8cabb"
    size 16

style pd_score_value is default:
    color "#ffd66c"
    size 22
    bold True

style pd_attempts_value is default:
    color "#ff7e7e"
    size 22
    bold True

style pd_footer_frame is default:
    background "#0e1b2ce6"
    padding (0, 0)

style pd_footer_button is button:
    background "#111f32"
    hover_background "#1e3656"
    padding (8, 6)

style pd_footer_button_text is default:
    color "#fff2df"
    hover_color "#ffffff"
    size 22
    bold True

style pd_footer_meta is default:
    color "#d7ccbd"
    size 13
    line_spacing 1

style pd_avatar_frame is default:
    background "#b7b0a8"
    padding (0, 0)

style pd_avatar_text is default:
    color "#122033"
    size 40
    bold True

style pd_dialogue_name is default:
    color "#9bd2df"
    size 18
    bold True

style pd_dialogue_quote is default:
    color "#e5ddd0"
    size 18
    line_spacing 2

style pd_feedback_text is default:
    color "#c9b59d"
    size 13

style pd_notes_frame is default:
    background "#0e1b2ce6"
    padding (0, 0)

style pd_notes_button is button:
    background None
    hover_background "#ffffff12"
    padding (4, 4)

style pd_notes_button_text is default:
    color "#fff2df"
    hover_color "#ffffff"
    size 20
    bold True