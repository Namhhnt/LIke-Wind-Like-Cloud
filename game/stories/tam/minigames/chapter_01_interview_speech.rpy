# ============================================================
# Chapter 01 interview minigame and outcomes
# ============================================================

label tam_c01_speech_game:

    $ tam_speech_attempts = 0

label tam_c01_speech_retry:

    $ tam_speech_order = []

    # Shuffle once per attempt.
    # This keeps the UI stable while the player is selecting and reordering ideas.
    $ tam_speech_pool = list(tam_speech_items)
    $ renpy.random.shuffle(tam_speech_pool)

    $ tam_speech_result = renpy.call_screen(
        "tam_speech_minigame",
        items=tam_speech_pool,
        attempt=(tam_speech_attempts + 1 if tam_speech_attempts < 3 else 3),
        can_skip=tam_speech_attempts >= 3
    )

    if tam_speech_result.get("action") == "skip":
        $ tam_salary_tier = "standard"
        $ add_unique(progress["player_flags"], "tam_interview_pass_skip_no_bonus")
        $ add_unique(progress["player_flags"], "tam_salary_standard_start")

        narrator "Tam takes a deep breath and lets go of the perfection she always tries to hold onto."
        narrator "She answers in a safer way, enough to avoid being rejected, but not enough to create any special spark."

        jump tam_c01_interview_skip

    $ tam_speech_order = list(tam_speech_result.get("picked", []))
    $ tam_speech_has_required_result = tam_speech_order_has_required(tam_speech_order)
    $ tam_speech_perfect_order = tam_speech_order_is_perfect(tam_speech_order)

    if tam_speech_has_required_result:

        if tam_speech_perfect_order:
            $ tam_salary_tier = "high"
            $ tam_work_skill += 2
            $ tam_confidence += 2
            $ add_unique(progress["player_flags"], "tam_interview_passed")
            $ add_unique(progress["player_flags"], "tam_interview_bonus_order")
            $ add_unique(progress["player_flags"], "tam_salary_high_start")
            $ add_unique(progress["player_flags"], "tam_work_skill_strong_c01")

            narrator "The points fall into exactly the right order."
            narrator "Tam begins by showing she understands the big picture, then moves into coordination skills, risk awareness, and only then closes with work attitude."
            narrator "It is not an ornate answer. But it is concise, structured, and never slips into clumsy self-promotion."

            jump tam_c01_interview_perfect

        else:
            $ tam_salary_tier = "standard"
            $ tam_work_skill += 1
            $ tam_confidence += 1
            $ add_unique(progress["player_flags"], "tam_interview_passed")
            $ add_unique(progress["player_flags"], "tam_salary_standard_start")

            narrator "All the important points are there, but the presentation order is not quite sharp."
            narrator "Even so, Tam still shows that she understands the job and takes it seriously."

            jump tam_c01_interview_pass

    else:

        $ tam_speech_attempts += 1

        if tam_speech_attempts < 3:
            narrator "The answer loses focus."
            narrator "The panel is not annoyed, but their expressions are enough for Tam to realize she has gone off course."
            narrator "Try again."

            jump tam_c01_speech_retry

        else:
            narrator "Tam has failed the ordering section 3 times."
            narrator "From this point on, she can keep retrying or skip ahead without earning any extra reward."

            jump tam_c01_speech_retry


label tam_c01_interview_perfect:

    tam serious "I think a project implementation role is more than just relaying information from one side to another."

    tam serious "In a company with multiple functions like construction, materials, IT, legal, accounting, and quality management, the implementation team needs to understand where its work sits in the full project flow."

    tam serious "If I do not understand the context, I will only pass information along. But if I do understand it, I can tell which details need clarification, which departments need updates, and which risks should be reported early."

    tam neutral "I do not have much real-world experience yet, but I can synthesize information, track details, and I am not afraid to learn the process from the ground up."

    tam smile "I want to do my part well in a way people can rely on. Not loudly, but clearly and responsibly."

    manager "Your answer is quite well structured."

    interviewer "And more practical than we expected."

    narrator "Tam feels her shoulders lighten a little."

    narrator "Not because she is certain she has won."

    narrator "Only because, for the first time that morning, she feels like she is standing in the right place."

    jump tam_c01_after_interview


label tam_c01_interview_pass:

    tam serious "I think project implementation work requires coordination skills and close attention to detail."

    tam serious "Our company has many departments involved in each project, so if information is unclear or updates come late, the overall schedule can be affected."

    tam neutral "I want to learn the process, help different teams work together better, and report issues in time when problems come up."

    manager "Good. The answer circles a bit, but the main point is solid."

    interviewer "I appreciate that you mentioned cross-department coordination."

    narrator "Tam nods."

    narrator "She knows she was not exceptional, but at least she did not drift off track."

    jump tam_c01_after_interview


label tam_c01_interview_skip:

    tam serious "I think this position requires carefulness, coordination, and a willingness to learn."

    tam sad "I do not have much experience yet, but I am ready to learn the process, support the work, and follow guidance from my supervisors."

    manager "All right."

    narrator "A safe answer."

    narrator "Not wrong. But it does not leave much behind, either."

    jump tam_c01_after_interview
