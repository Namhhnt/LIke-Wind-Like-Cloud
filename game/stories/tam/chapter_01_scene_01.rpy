# Chapter 01, Scene 01

label tam_c01:

    scene black
    with fade

    narrator "Chapter 01"
    narrator "The First Day the Wind Changed Direction"

    scene bg_tam_room_morning
    with dissolve

    narrator "That morning, Tam woke up ten minutes before her alarm."
    narrator "Outside the window, the city was not fully awake yet. A thin wash of light lay over the crowded rooftops, quiet as if someone had just drawn back the curtain for a new day."
    narrator "On her desk was a neatly clipped stack of documents. CV. Application letter. A photocopy of her degree. A few small certificates she wasn't sure would help, but leaving them out somehow felt wrong."
    narrator "Tam looked at them for a long time."

    tam thoughtful "Project implementation department..."

    narrator "The position title did not sound too unfamiliar. But the company was different."
    narrator "A multi-sector investment company. Construction. Materials. IT. Legal. Accounting. Quality management. Even departments whose names alone made Tam feel like she needed another cup of coffee just to avoid giving up halfway."
    narrator "She was not the kind of person who feared difficult work."
    narrator "She was only a little afraid of what she still did not understand."

    play sound "audio/phone_vibrate.ogg"

    narrator "Her phone vibrated on the table."

    huyen smile "You awake yet, grandma?"
    tam dazed "I am."
    huyen pouty "Good. I'm downstairs. Come down. If you make me go into that interview alone, I'll curse you into getting assigned to accounting and doing payroll for the rest of your life."
    tam smile "You're evil."
    huyen smile "Come down already. I bought banh mi."

    narrator "Tam laughed."
    narrator "Some people only needed to appear through a single text message to make the air inside someone else's chest feel a little lighter."

    scene bg_apartment_lobby_morning
    with dissolve

    narrator "Huyen was standing in the apartment lobby, holding two banh mi in one hand and hugging a folder bag to her chest with the other as if it were a life buoy."
    huyen sad "I'm serious, my heart's pounding like it's quarter-end deadline season."
    tam smile "So you do know how to be scared?"
    huyen smile "Of course I do. I just hide it better than you."
    narrator "Tam took a sandwich from Huyen. It was still warm. The wrapper had soaked up a little oil, and the smell of pate and cilantro rose up in a way so ordinary it made life feel salvageable."

    huyen neutral "Hey, if they ask why you want to join project implementation later, what are you going to say?"
    tam thoughtful "I'm still thinking."
    huyen pouty "So you haven't figured it out yet."
    tam embarrassed "I have. I just haven't arranged it yet."
    huyen smile "Exactly. That's the same thing."

    narrator "Tam fell silent for a moment. Huyen glanced at her, her expression teasing but genuinely concerned."

    menu:
        "How should Tam respond to Huyen?"

        "Admit she's worried too, then ask Huyen to review the main points with her.":
            $ huyen_trust += 1
            $ add_unique(progress["player_flags"], "tam_huyen_shared_anxiety")
            tam sad "Yeah, I'm worried too. How about we go over it together on the way? Listen for me and tell me if anything sounds stupid."
            huyen happy "That's better. At least today I feel like your best friend instead of an NPC handing out sandwiches."

        "Act confident so Huyen worries less.":
            tam smile "It'll be fine. I think I can improvise in there."
            huyen serious "Sounds cool, sure. But I hate the word 'improvise' before an interview."
            narrator "Huyen said that, but she did not push further."

        "Tell Huyen not to make her even more stressed.":
            $ huyen_trust -= 1
            tam sad "Stop asking. I'm already trying not to freak out."
            huyen sad "Right... sorry."
            narrator "The answer dropped between them a little short. Not heavy. Just a little colder for a beat."

    scene bg_company_lobby_morning
    with fade

    narrator "The company occupied a large office building, its glass facade bright enough for Tam to see her own reflection in it."
    narrator "White blouse. Dark skirt. Hair tied neatly at the nape of her neck. An appearance just serious enough, and just young enough, that no one could be sure she was truly ready to step into a machine this large."
    narrator "At reception, Huyen leaned close to her ear."

    huyen smile "I just saw a guy walk past with a legal department badge. His face was as cold as a payment rejection notice."
    tam smile "Don't make me laugh."
    huyen happy "Laugh so you shake less. Science hasn't proven it, but I have, through personal experience."

    narrator "Tam pressed her lips together, but the corners of her mouth still lifted."

    scene bg_interview_waiting_room
    with dissolve

    narrator "The interview waiting room was quiet."
    narrator "On the wall hung photographs of construction projects, material plants, an office complex still under construction, and several internal dashboard screens showing figures Tam had not had time to understand."
    narrator "Maybe this was not a place where knowing how to type documents and send emails would be enough."
    narrator "The more she looked, the more Tam understood that the position she was applying for sat in the middle of many currents."
    narrator "Schedule. Documentation. Materials. Legal. Cost. Quality. People."
    narrator "A small link in the chain, but if it shifted, many things behind it would shift too."

    play sound "audio/door_open.ogg"

    hr "Tam, please come in."

    narrator "Tam stood up."
    narrator "Huyen, still seated beside her, lifted a small fist."
    huyen happy "Good luck. Don't betray me."
    tam smile "I'm going into an interview, not an interrogation room."
    huyen confused "What's the difference?"

    narrator "Tam laughed very softly, then stepped inside."

    scene bg_interview_room
    with dissolve

    interviewer "Hello. Please, make yourself comfortable."
    manager "We've looked through your file. This project implementation role is not just paperwork. It requires coordination with many departments. How do you understand this job?"

    narrator "The question came sooner than Tam expected."
    narrator "She placed both hands on her knees, her thumbs lightly brushing together."
    narrator "This was not the moment to ramble."
    narrator "She needed to organize her thoughts."

    jump tam_c01_speech_game
