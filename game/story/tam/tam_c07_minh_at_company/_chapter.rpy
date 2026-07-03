# FILE: game/story/tam/tam_c07_minh_at_company/_chapter.rpy
# Chapter wrapper. Calls scene labels only; no heavy story content here.

label tam_c07_minh_at_company:
    call tam_c07_minh_at_company_s01_project_briefing
    call tam_c07_minh_at_company_s02_minh_as_advisor
    call tam_c07_minh_at_company_s03_tam_minh_interaction
    call tam_c07_minh_at_company_s04_professional_or_personal_choice
    $ story_complete_chapter('tam_c07_minh_at_company')
    $ activity_start_free_time_session(40)
    if renpy.has_label('route_map'):
        jump route_map
    return
