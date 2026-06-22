# Chapter 01, Scene 02

label tam_c01_after_interview:

    scene bg_company_lobby_noon
    with dissolve

    narrator "When Tam stepped out of the room, Huyen was already on her feet like a spring."
    huyen sad "How did it go?"
    tam dazed "No idea yet."
    huyen smile "Your face doesn't look terrible. That means they didn't reject you at the door."
    tam smile "Thank you for that deeply uplifting encouragement."
    huyen smile "You're welcome. I charge by the hour."

    narrator "The two of them sat down on a long bench in the lobby. Outside the glass wall, the noon sunlight had started falling in harsh slabs."
    huyen sad "I'm shaking."
    tam surprised "Is it your turn now?"
    huyen sad "Yeah. If I die in there, delete my search history."

    menu:
        "How should Tam encourage Huyen?"

        "Tell Huyen to stay calm and lean on her real strengths.":
            $ huyen_trust += 1
            $ add_unique(progress["player_flags"], "tam_supported_huyen_interview")
            tam serious "You don't need to act more capable than you really are. You speak naturally, pick things up fast, and you remember details well. Just use those."
            huyen smile "That sounds a little like dialogue from a youth drama, but... it actually helps."
            tam smile "Go on, then. Don't disgrace the breakfast banh mi."

        "Tease Huyen so she relaxes.":
            tam smile "It's fine. If you fail, I'll tell this story at your wedding."
            huyen laugh "You're exactly the kind of best friend who belongs on the project risk register."
            narrator "Huyen laughed. Some of the tension left her eyes."

        "Tell Huyen to handle it herself because everyone has to get through their own part.":
            $ huyen_trust -= 1
            tam neutral "I don't really know what to tell you. Handle it yourself. Everyone has to get through their own part."
            huyen sad "Yeah. I get it."
            narrator "Huyen smiled, but the smile looked thin."

    narrator "Huyen went into the interview room."
    narrator "Tam sat there alone."
    narrator "The company lobby suddenly felt much larger without Huyen talking beside her."

    scene bg_company_lobby_afternoon
    with dissolve

    narrator "The results came at the end of the afternoon."
    narrator "Both of them got in."
    narrator "Tam read the email twice. Huyen read it four times. Then they looked at each other for a few seconds and burst out laughing like two people who had just escaped a minor accident that still sent their hearts crashing down to their knees."

    huyen happy "We're celebrating tonight."
    tam surprised "With what?"
    huyen serious "Something fancy."
    tam shocked "You just got hired and you already want to go bankrupt?"
    huyen smile "No. I call it investing in morale before the company crushes us."
    narrator "Tam thought that argument was a little suspect."
    narrator "But also fairly convincing."

    if tam_salary_tier == "high":
        narrator "Tam's offer email came with a starting salary higher than she expected."
        narrator "Not a number big enough to change her life, but enough to make her stare at the screen for a few extra seconds and feel as if someone had opened a window inside her chest."

        menu:
            "How should Tam tell Huyen about the salary?"

            "Share honestly, but without making Huyen feel compared.":
                $ huyen_trust += 1
                $ add_unique(progress["player_flags"], "tam_shared_salary_with_care")
                tam happy "They offered me a little more than I expected."
                huyen surprised "Really? How much?"
                tam embarrassed "I'll tell you, but I'm not bragging, okay? I was surprised too."
                huyen laugh "You idiot. If you got a better offer, I'm happy for you. Just remember to buy me a large milk tea later."
                tam smile "So that was your real motive, huh?"
                huyen happy "Best friends know how to turn each other's happiness into beverages."

            "Hide it so Huyen won't feel bad.":
                $ huyen_trust -= 1
                $ add_unique(progress["player_flags"], "tam_hid_salary_from_huyen")
                tam sad "It's pretty normal, I guess."
                narrator "That's what Tam said. But she knew she had just hidden something from Huyen that did not really need hiding."
                narrator "That small silence stayed between them like a crooked pin."

            "Show off because she earned it.":
                $ huyen_trust -= 1
                tam happy "I got offered more. Guess my interview really was that good."
                huyen sad "Yeah. You're good, after all."
                narrator "Huyen kept smiling. But her voice lost a little of its brightness."

    else:
        narrator "Tam's starting salary landed in the standard range."
        narrator "Not high enough to make her squeal, and not low enough to disappoint her."
        narrator "Just enough. Like a door opening not too wide, but clearly open."

    if huyen_trust >= 2:
        $ add_unique(progress["player_flags"], "huyen_trust_high_c01")
        $ add_unique(progress["player_flags"], "huyen_advice_work_unlocked")
        $ add_unique(progress["player_flags"], "huyen_advice_relationship_unlocked")
        narrator "From that day on, Huyen began trusting Tam in a different way."
        narrator "Not just as the best friend you laugh with, complain with, and share meaningless after-work meals with."
        narrator "But as someone who could speak honestly, listen honestly, and hold on to the right advice at the right time for each other."

    scene bg_luxury_restaurant_evening
    with fade

    narrator "That evening, the two of them chose a restaurant slightly more luxurious than necessary."
    narrator "Warm yellow lights. White tablecloths. Glassware so clear Tam was afraid one clumsy grip might expose the awkwardness she had only just managed to hide."

    huyen neutral "Hey."
    tam neutral "What?"
    huyen happy "We're officially adults now."
    tam surprised "Just because we got hired?"
    huyen smile "Yeah. Adults are creatures who get excited when they receive the email that begins a long chain of selling their souls to spreadsheets."
    tam smile "That sounds awfully pessimistic."
    huyen smile "But I'm saying it in a fancy restaurant, so it becomes philosophy."

    narrator "Tam laughed and raised her fruit juice glass."
    tam happy "To us."
    huyen happy "To us. And to the project implementation department surviving after hiring the two of us."

    play sound "audio/glass_clink.ogg"

    narrator "The two glasses touched lightly."
    narrator "The sound of glass was very soft."
    narrator "At that very moment, from a table tucked into a shaded corner, someone else also raised a glass."
    narrator "Tam noticed it from the corner of her eye."
    narrator "A young man sitting alone. The light only reached half his shoulder, leaving his face sunk in a darkness that felt just unfamiliar enough."
    narrator "He said nothing."
    narrator "He only lifted his glass toward the two girls, like a quiet congratulations."

    huyen confused "What was that?"
    tam thoughtful "No idea."
    huyen confused "Someone you know?"
    tam neutral "No."

    narrator "Tam looked again."
    narrator "The young man in the corner had already lowered his glass. He tilted his head slightly, as if he had just been accidentally caught in something he had not meant anyone to notice."
    narrator "Then he turned back toward the window."
    narrator "The city lights shimmered behind him."
    narrator "A very small moment."
    narrator "Small enough that if Tam had not been so happy that day, she might have forgotten it immediately."

    $ add_unique(progress["player_flags"], "tam_saw_corner_man_at_dinner")
    $ add_unique(progress["player_flags"], "hoang_hidden_first_presence")

    scene black
    with fade

    narrator "Time passed."
    narrator "A new job does not make a person's life change overnight."
    narrator "It only quietly changes the rhythm of each day."

    jump tam_c01_scene_03
