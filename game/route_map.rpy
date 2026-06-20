style route_map_root_frame is empty
style route_map_panel is frame
style route_map_title is gui_text
style route_map_summary is gui_text
style route_map_route_title is gui_text
style route_map_route_status is gui_text
style route_map_chapter_button is button
style route_map_chapter_button_text is button_text
style route_map_recommended_text is gui_text
style route_map_completed_text is gui_text
style route_map_locked_text is gui_text

style route_map_panel:
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)
    xpadding 24
    ypadding 24

style route_map_title:
    size 54
    color gui.selected_color
    text_align 0.5

style route_map_summary:
    size 22
    color gui.idle_small_color
    text_align 0.5

style route_map_route_title:
    size 34
    color gui.selected_color

style route_map_route_status:
    size 22
    color gui.accent_color

style route_map_chapter_button:
    properties gui.button_properties("button")
    xfill True

style route_map_chapter_button_text:
    properties gui.text_properties("button")
    xalign 0.0

style route_map_recommended_text:
    size 20
    color gui.hover_color

style route_map_completed_text:
    size 24
    color gui.idle_small_color

style route_map_locked_text:
    size 24
    color gui.insensitive_color

screen route_map():
    modal True

    add gui.game_menu_background

    frame:
        style "route_map_root_frame"
        background Solid("#050507aa")
        xfill True
        yfill True

    viewport:
        xalign 0.5
        yalign 0.5
        xsize 1560
        ysize 860
        draggable True
        mousewheel True

        vbox:
            spacing 24

            text _("Route Map"):
                style "route_map_title"
                xalign 0.5

            text _("Phase 3 prototype: bonus chapters now branch into mutually exclusive directions."):
                style "route_map_summary"
                xalign 0.5

            if progress["recommended_next"]:
                text _("Recommended Next: [', '.join(chapter_title(chapter_id) for chapter_id in progress['recommended_next'])]"):
                    style "route_map_summary"
                    xalign 0.5

            text _("Play Order: [get_play_order_summary()]"):
                style "route_map_summary"
                xalign 0.5

            text _("Unlocked Choices: [get_unlocked_choice_summary()]"):
                style "route_map_summary"
                xalign 0.5

            text _("Eligible Endings: [get_ending_summary()]"):
                style "route_map_summary"
                xalign 0.5

            for route_id in ROUTE_ORDER:
                $ route = ROUTES[route_id]
                $ route_chapters = get_route_chapters(route_id)
                $ route_status = get_route_status_label(route_id)

                frame:
                    style "route_map_panel"

                    vbox:
                        spacing 14

                        text route["title"]:
                            style "route_map_route_title"

                        text _("Focus: [get_route_focus_summary(route_id)]"):
                            style "route_map_summary"

                        text _("Direction: [get_relationship_direction_summary(route_id)]"):
                            style "route_map_summary"

                        if route_status == "completed":
                            text _("Completed") style "route_map_route_status"
                        elif route_status == "partially_unlocked":
                            text _("In Progress") style "route_map_route_status"
                        elif route_status == "available":
                            text _("Available") style "route_map_route_status"
                        else:
                            text _("Locked") style "route_map_route_status"

                        if route_chapters:
                            for chapter_id in route_chapters:
                                $ chapter_state = get_chapter_state(chapter_id)

                                if chapter_state == "available":
                                    textbutton chapter_title(chapter_id):
                                        style "route_map_chapter_button"
                                        action Return(chapter_id)

                                    if is_recommended_chapter(chapter_id):
                                        text _("Recommended next chapter"):
                                            style "route_map_recommended_text"

                                elif chapter_state == "completed":
                                    text "[chapter_title(chapter_id)] - [_(\"Completed\")]":
                                        style "route_map_completed_text"

                                elif chapter_state == "excluded":
                                    text "[chapter_title(chapter_id)] - [_(\"Excluded\")]":
                                        style "route_map_locked_text"

                                else:
                                    text "[chapter_title(chapter_id)] - [_(\"Locked\")]":
                                        style "route_map_locked_text"
                        else:
                            text _("No chapters are configured for this route yet."):
                                style "route_map_locked_text"

            if not progress["available"] and not progress["completed"]:
                text _("No chapters are available yet."):
                    style "route_map_summary"
                    xalign 0.5

            hbox:
                xalign 0.5
                spacing 18

                textbutton _("Main Menu") action MainMenu(confirm=False)
                textbutton _("Load") action ShowMenu("load")
                textbutton _("Progress Debug") action Show("debug_progression")


label route_map:
    $ initialize_progression()
    $ selected_chapter = renpy.call_screen("route_map")

    if selected_chapter:
        jump expression selected_chapter

    return


label tam_c01:
    "Tam reaches the riverside before sunrise, carrying questions she cannot ask aloud yet."
    "This first chapter exists to prove the new progression flow works end to end."

    $ complete_chapter("tam_c01")
    jump route_map


label tam_c02:
    "The second chapter opens only after the first is complete, using centralized progression data."
    "This chapter now opens Hoang's route before Tam can finish her own line, creating the first interwoven prerequisite."

    $ complete_chapter("tam_c02")
    jump route_map


label hoang_h01:
    "Hoang's point of view arrives between Tam's second and third beats."
    "Completing it unlocks two mutually exclusive bonus chapters before the route can settle into its next shape."

    $ complete_chapter("hoang_h01")
    jump route_map


label hoang_bonus_restraint:
    "Hoang chooses restraint and leaves several thoughts unspoken."
    "That choice closes off the confession variant and unlocks a gentler follow-up tone."

    $ complete_chapter("hoang_bonus_restraint")
    jump route_map


label hoang_bonus_confession:
    "Hoang speaks too directly, forcing the scene toward confession instead of restraint."
    "That choice excludes the quieter variant and unlocks a more forward follow-up path."

    $ complete_chapter("hoang_bonus_confession")
    jump route_map


label tam_c03:
    "Tam can only reach this moment after Hoang's route has taken one of its two optional emotional directions."
    "That makes the route map prove a real exclusion-driven dependency instead of a simple linear chain."
    "[get_emotional_hint()]"

    if choice_is_available("notice_subtle_reaction"):
        "Because the player has seen Hoang's earlier hesitation, Tam notices a subtle reaction that would otherwise pass unseen."

    menu:
        "How should Tam respond?"

        "Ask gently" if choice_is_available("ask_gently"):
            $ add_unique(progress["player_flags"], "tam_choice_gentle")
            $ progress["emotional_state"]["trust"] += 1
            "Tam softens her words and lets the moment breathe."

        "Choose direct affection" if choice_is_available("choose_direct_affection"):
            $ add_unique(progress["player_flags"], "tam_choice_direct")
            $ progress["emotional_state"]["misunderstanding"] += 1
            "Tam pushes forward directly, even if the timing is dangerous."

        "Say nothing for now":
            $ add_unique(progress["player_flags"], "tam_choice_silence")
            "Tam decides the silence still says enough for now."

    $ complete_chapter("tam_c03")
    jump route_map


label hoang_h02:
    "Hoang's second chapter now depends on both his first scene and Tam's third one."
    "This closes the first two-route loop and gives route focus something meaningful to measure."

    if has_relationship_direction("hoang", "restraint"):
        "The restraint path keeps the scene quiet, careful, and almost fragile."

    if has_relationship_direction("hoang", "confession"):
        "The confession path carries more force, but also more risk of being misunderstood."

    $ complete_chapter("hoang_h02")
    jump resolve_seed_ending


label resolve_seed_ending:
    if "ending_shared_silence" in progress["ending_eligibility"]:
        jump ending_shared_silence
    elif "ending_restraint" in progress["ending_eligibility"]:
        jump ending_restraint
    elif "ending_confession" in progress["ending_eligibility"]:
        jump ending_confession

    jump route_map


label ending_shared_silence:
    $ mark_ending_seen("ending_shared_silence")
    "Ending unlocked: Shared Silence."
    "Trust outweighs distance, and the two routes finally converge without forcing the moment apart."
    jump route_map


label ending_restraint:
    $ mark_ending_seen("ending_restraint")
    "Ending unlocked: Quiet Restraint."
    "Hoang keeps his feelings measured, and the route resolves through patience rather than confession."
    jump route_map


label ending_confession:
    $ mark_ending_seen("ending_confession")
    "Ending unlocked: Sudden Confession."
    "The confession path lands first, reshaping the route through urgency instead of caution."
    jump route_map
