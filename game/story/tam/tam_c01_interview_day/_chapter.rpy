# FILE: game/story/tam/tam_c01_interview_day/_chapter.rpy
# Chapter wrapper. Calls scene labels only; no heavy story content here.

label tam_c01_interview_day:
    # Interview invitation email becomes the first email Tam receives.
    $ story_flag("tam_interview_invitation_received")
    $ phone_unlock_mail("company_interview_invitation")
    $ phone_refresh_all()

    call tam_c01_interview_day_s01_tam_huyen_morning
    $ initialize_progression()
    $ add_unique(progress["player_flags"], "opening_map_locations_unlocked")
    $ unlock_map_locations(["tam_apartment", "huyen_apartment", "company"])
    call tam_c01_interview_day_s02_interview_room
    call tam_c01_interview_day_s03_success_result
    call tam_c01_interview_day_s04_celebration_dinner
    $ story_complete_chapter('tam_c01_interview_day')
    $ story_flag("tam_c01_onboarding_mail_sent")
    $ phone_unlock_mail("company_onboarding_process")
    $ phone_refresh_all()

    $ time_start_period_after_chapter('tam_c01_interview_day')
    if renpy.has_label('route_map'):
        jump route_map
    return
