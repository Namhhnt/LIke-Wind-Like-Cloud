# Chapter 01, Scene 03

label tam_c01_scene_03:

    scene bg_company_open_office_day
    with dissolve

    narrator "Tam learned how to tell the difference between an email that really needed an answer right away and one that only looked like it did."
    narrator "She learned how to read meeting minutes without falling asleep."
    narrator "She learned to note deadlines, file codes, contract numbers, contractor names, and even the half-joking remarks from her supervisors that were probably best not treated as jokes."
    narrator "The project implementation department was exactly as she had imagined during the interview."
    narrator "It sat in the middle of many things."
    narrator "And it was pulled from many directions too."

    scene bg_meeting_room_day
    with dissolve

    manager "Tam, the acceptance file for this material batch doesn't match the notes from quality management. Accounting needs confirmation before the end of the day to process temporary payment."
    manager "Check it again for me. Don't let legal call this afternoon asking why the paperwork moved ahead of the signed minutes."

    narrator "A stack of documents was set down in front of Tam."
    narrator "Not thick."
    narrator "But heavy enough to make her chest tighten."

    if "tam_work_skill_strong_c01" in progress["player_flags"]:
        narrator "Tam suddenly remembered her answer from the interview."
        narrator "Don't pass information along before you understand the context."
        narrator "Don't let a small mistake become a big problem."

    menu:
        "How should Tam handle the mismatch in the file?"

        "Cross-check the QC notes, confirm with materials, then send a short summary to accounting and legal.":
            $ tam_work_skill += 1
            $ tam_confidence += 1
            $ add_unique(progress["player_flags"], "tam_handled_project_issue_well")
            tam serious "Please let me verify it with QC and materials first. If the mismatch is in the minutes, I'll note the discrepancy clearly and send a short summary to the relevant teams."
            manager "Correct. Do that."
            narrator "No one added any praise."
            narrator "But that single word, 'correct,' was enough to make Tam feel her spine straighten."

        "Send a temporary confirmation to accounting first so the deadline is met, then supplement it later.":
            $ tam_confidence -= 1
            $ add_unique(progress["player_flags"], "tam_project_issue_rushed")
            tam embarrassed "Could I send a temporary confirmation first and complete the rest afterward?"
            manager "No. If payment paperwork moves before quality confirmation, our department will be the first one called."
            narrator "Tam fell silent."
            narrator "She wrote down that warning very carefully."

        "Wait for the manager to decide because the file involves too many teams.":
            $ tam_confidence -= 1
            tam sad "So for this part, should I wait for your decision and then follow it?"
            manager "I need you to check it before I decide."
            narrator "The sentence was not harsh."
            narrator "But Tam still felt her face warm up."

    scene bg_company_year_end_party
    with fade

    narrator "The company's Year End Party was held at a large hotel at the end of the year."
    narrator "After a few months of working, Tam looked less like the girl clutching a folder stiffly in an interview waiting room."
    narrator "She was still careful. Still prone to overthinking."
    narrator "But now she knew when to ask, when to stay quiet, and when she had to step forward and say something clearly before things tangled any further."

    if tam_salary_tier == "high":
        narrator "The stronger salary had given her more choices too."
        narrator "Tonight Tam wore an elegant dress that fit well, with small but bright accessories, not showy, yet enough to make people glance back."
        $ hoang_impression += 2
    else:
        narrator "Tam chose a simple, neat dress. Not especially striking, but right for her."
        narrator "Her beauty still lived in cleanliness, softness, and a quietness that was hard to name."

    if tam_confidence >= 2:
        narrator "The way she stood in a crowd had changed too."
        narrator "She no longer looked like someone trying to hide at the edge of the room."
        narrator "She spoke just enough, smiled just enough, and when a colleague mentioned a project snag that had only recently been resolved, Tam answered with a calmness rarely seen in a new employee."
        $ hoang_impression += 2
    elif tam_confidence >= 1:
        narrator "Tam was not truly confident in a crowd yet, but she no longer felt completely out of place."
        $ hoang_impression += 1
    else:
        narrator "Under the lights and music, Tam still felt a little small."
        narrator "She stayed beside Huyen more often, smiling lightly now and then when people spoke to her."

    if "huyen_trust_high_c01" in progress["player_flags"]:
        $ hoang_impression += 1
        huyen serious "Stand up straight. You're pretty, stop acting like you owe society an apology for it."
        tam embarrassed "Lower your voice."
        huyen serious "No. I'm fulfilling my best-friend duties."

    narrator "The company had invited a few guests from partner organizations that night."
    narrator "Tam did not pay much attention at first."
    narrator "Not until she noticed someone standing near the window area."
    narrator "A young man in a dark suit, tall and lean. His face was not exactly familiar, but not strange enough for her to name the feeling that brushed through her."
    narrator "He was talking with someone from the company's leadership team."
    narrator "His gaze was calm. His smile was just polite enough. The kind of person who could stand still in a noisy room and still make the air around him feel orderly."

    tam thoughtful "..."
    huyen confused "What is it?"
    tam embarrassed "Nothing."
    huyen smile "Nothing? You're looking at him like you're reading classified documents."
    tam embarrassed "Be quiet."

    narrator "Huyen followed Tam's line of sight and then lightly nudged her with an elbow."
    huyen smile "Ah."
    tam surprised "Ah what?"
    huyen smile "Nothing. I just discovered your side project."
    tam embarrassed "Huyen."
    huyen smile "All right, all right. I'll stop."

    if hoang_impression >= 4:
        $ add_unique(progress["player_flags"], "hoang_first_contact_c01")
        $ add_unique(progress["player_flags"], "hoang_approached_tam_first")
        $ add_unique(progress["player_flags"], "tam_year_end_strong_impression")

        narrator "Tam was about to look away."
        narrator "But at that moment, the young man looked over."
        narrator "Their eyes met."
        narrator "Not for long."
        narrator "Just long enough for Tam to realize he was truly looking at her, not past the crowd."
        narrator "Then he walked toward her."

        hoang neutral "Hello."
        tam shy "Uh... hello."
        hoang neutral "I'm Hoang. I'm here with the partner delegation tonight."
        tam neutral "I'm Tam. Project implementation."
        hoang smile "I know."

        narrator "Tam froze for a beat."
        hoang serious "I heard you earlier, when you were discussing the acceptance paperwork with the materials team. You summarize things clearly."
        tam embarrassed "Oh... I was only repeating what I understood."
        hoang serious "Making other people understand is a skill too."
        narrator "His tone did not sound like empty politeness."
        narrator "And because of that, Tam suddenly did not know where to put her hands."

        huyen smile "I'll go get more water."
        narrator "Huyen said it very quickly and vanished."
        narrator "A highly technical betrayal."

        hoang smile "Your friend is interesting."
        tam smile "She usually is."
        hoang smile "That must be exhausting."
        tam smile "I'm used to it."

        narrator "Hoang laughed softly."
        narrator "A very light laugh."
        narrator "Strangely enough, it reminded Tam of the shadowed table in the restaurant corner months earlier."
        narrator "A glass lifting into the air."
        narrator "A congratulations with no sound."
        narrator "The thought flashed through her and dissolved into the music."

        jump tam_c01_year_end_after_meeting

    elif hoang_impression >= 2:
        $ add_unique(progress["player_flags"], "tam_year_end_can_approach_hoang")

        narrator "The young man glanced over once."
        narrator "Very quickly."
        narrator "Not enough to call it an opening. But enough for Tam to know that if she walked over, it would not be too strange."

        menu:
            "Should Tam go over and start a conversation?"

            "Go over and speak to him" if "tam_year_end_can_approach_hoang" in progress["player_flags"]:
                $ add_unique(progress["player_flags"], "hoang_first_contact_c01")
                $ add_unique(progress["player_flags"], "tam_approached_hoang_first")
                $ hoang_impression += 1

                narrator "Tam took a very small breath."
                narrator "Not because she had suddenly become brave."
                narrator "Only because some moments, if you let them pass, turn into regret later."

                tam neutral "Hello. I think you're one of the guests from the partner company, right?"
                hoang neutral "Yeah. I'm Hoang."
                tam neutral "I'm Tam. Project implementation."
                hoang neutral "I heard the introductions earlier."
                tam embarrassed "Then I guess you also heard the part where I stumbled a little."
                hoang serious "I did."
                narrator "Tam looked up."
                hoang smile "But you recovered well afterward."
                narrator "The answer was so direct that Tam could not tell whether it was praise or an inspection note."
                tam smile "Do you always talk like you're inspecting paperwork?"
                narrator "Hoang paused."
                narrator "Then he laughed."
                hoang smile "Not often. Only when I meet someone from project implementation."
                narrator "Tam laughed too."
                narrator "It was a very short conversation."
                narrator "But enough for the two of them to have a name for each other."

                jump tam_c01_year_end_after_meeting

            "Don't approach him, just keep your distance and watch":
                $ add_unique(progress["player_flags"], "hoang_no_contact_c01")
                $ add_unique(progress["player_flags"], "hoang_romance_slow_start")
                narrator "In the end, Tam did not step forward."
                narrator "She only looked at him once more, then turned back to listen to Huyen speak."
                narrator "Some encounters begin with a greeting."
                narrator "Others begin with both people staying silent."

                jump tam_c01_year_end_no_contact

    else:
        $ add_unique(progress["player_flags"], "hoang_no_contact_c01")
        $ add_unique(progress["player_flags"], "hoang_romance_delayed_start")

        narrator "The young man remained in the distance."
        narrator "Tam saw him."
        narrator "And maybe he saw her too."
        narrator "But the crowd, the lights, the music, and the small lack of confidence inside Tam kept the two of them on opposite sides of the room."
        narrator "No one stepped forward."
        narrator "There was no greeting."
        narrator "Only a very faint glance, swallowed by the party before it could become anything clear."

        jump tam_c01_year_end_no_contact
