# FILE: game/story/final/final_c24_last_choices/_chapter.rpy
# Chapter wrapper. Calls scene labels only; no heavy story content here.

label final_c24_last_choices:
    call final_c24_last_choices_s01_tam_final_choice
    call final_c24_last_choices_s02_hoang_huyen_quan_final_choice
    call final_c24_last_choices_s03_thienan_final_choice
    call final_c24_last_choices_s04_minyuu_final_choice
    call final_c24_last_choices_s05_doom_or_canon_check
    $ story_complete_chapter('final_c24_last_choices')
    jump ending_resolver
