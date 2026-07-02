# FILE: game/story/tam/tam_c02_company_party/_chapter.rpy
# Chapter wrapper. Calls scene labels only; no heavy story content here.

label tam_c02_company_party:
    call tam_c02_company_party_s00_onboarding
    call tam_c02_company_party_s01_company_rumors_about_quan
    call tam_c02_company_party_s01b_first_salary_and_shopping
    call tam_c02_company_party_s02_party_start
    call tam_c02_company_party_s03_hoang_intro
    call tam_c02_company_party_s04_first_branch

    $ story_complete_chapter('tam_c02_company_party')

    if renpy.has_label('route_map'):
        jump route_map

    return