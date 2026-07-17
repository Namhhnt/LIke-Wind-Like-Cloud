# FILE: game/story/yuuka/yuuka_c08_festival_arrival/_chapter.rpy
# Chapter wrapper. Calls scene labels only; no heavy story content here.

# Chapter-only supporting speaker.
define c08_van = Character("Vân", image="van")


label yuuka_c08_festival_arrival:
    # Career snapshot.
    $ c08_tam_job_rank = career_bonus_get_level("tam")
    $ c08_tam_leads_festival = c08_tam_job_rank >= 4

    # Tâm / Hoàng route exists when either side has actively opened,
    # pursued, or committed to the relationship.
    $ c08_tam_hoang_active = (
        story_has_direction("tam", "tam_hoang_open")
        or story_has_direction("tam", "tam_hoang_commit")
        or story_has_direction("hoang", "hoang_tam_open")
        or story_has_direction("hoang", "hoang_tam_pursue")
        or story_has_direction("hoang", "hoang_tam_commit")
    )

    # Huyền / Hoàng route used for the indirect introduction branch.
    $ c08_huyen_hoang_active = (
        story_has_direction("huyen", "huyen_hoang_open")
        or story_has_direction("huyen", "huyen_hoang_commit")
        or story_has_direction("hoang", "hoang_huyen_open")
        or story_has_direction("hoang", "hoang_huyen_commit")
    )

    $ c08_huyen_quan_active = (
        story_has_direction("huyen", "huyen_quan_open")
        or story_has_direction("huyen", "huyen_quan_commit")
    )

    $ c08_tam_minh_lean = (
        story_has_direction("tam", "tam_minh_open")
        or story_has_direction("tam", "tam_minh_commit")
        or story_state.get("tam_minh_drawn", 0) >= 50
    )

    $ c08_tam_high_clarity = story_state.get("tam_self_clarity", 0) >= 60

    # Chapter-local branch state.
    $ c08_tam_followed_hoang = False
    $ c08_tam_met_yuuka = False
    $ c08_yuuka_intro_source = ""
    $ c08_minyuu_greeting_mode = ""

    call yuuka_c08_festival_arrival_s01_festival_briefing
    call yuuka_c08_festival_arrival_s02_yuuka_as_director
    call yuuka_c08_festival_arrival_s03_hoang_introduces_yuuka
    call yuuka_c08_festival_arrival_s04_minh_neutral_pause

    $ story_flag("yuuka_c08_festival_arrival_complete")
    $ story_complete_chapter("yuuka_c08_festival_arrival")

    $ activity_start_free_time_session(40)

    if renpy.has_label("route_map"):
        jump route_map

    return