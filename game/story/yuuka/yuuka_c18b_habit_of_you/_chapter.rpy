# FILE: game/story/yuuka/yuuka_c18b_habit_of_you/_chapter.rpy
# Chapter wrapper. Calls scene labels only; no heavy story content here.

label yuuka_c18b_habit_of_you:
    call yuuka_c18b_habit_of_you_s01_after_separation_memory
    call yuuka_c18b_habit_of_you_s02_work_and_absence
    call yuuka_c18b_habit_of_you_s03_no_longer_running
    call yuuka_c18b_habit_of_you_s04_late_reunion_seed
    $ story_complete_chapter('yuuka_c18b_habit_of_you')
    if renpy.has_label('route_map'):
        jump route_map
    return
