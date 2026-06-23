# Chapter 02, Scene 01

label tam_c02:

    $ tam_c02_party_route = ""
    $ tam_c02_hoang_noticed = False
    $ tam_c02_meaningful_contact = False

    scene black
    with fade

    narrator "Chapter 02"
    narrator "The Company Gathering"

    call tam_c02_return_to_office
    call tam_c02_quan_intro
    call tam_c02_party_opening
    call tam_c02_pre_hoang_choice

    jump tam_c02_main_choice


label tam_c02_return_to_office:

    scene bg_company_open_office_day
    with dissolve

    narrator "After the year-end party, work did not slow down for anyone just because a new year had begun."
    narrator "Tam still arrived a little early, still opened her notebook before her email, and still felt a faint sense of relief every time she understood a problem before someone had to explain it twice."

    if has_player_flag("hoang_first_contact_c01"):
        narrator "But now there was also another kind of distraction."
        narrator "A name she had learned under hotel lights. A voice that had been calm without sounding distant."
        narrator "She did not think about him all day. Only at strange moments. When a room went briefly quiet. When someone laughed softly nearby. When she caught herself straightening the edge of a document for no real reason."
    elif has_player_flag("hoang_no_contact_c01"):
        narrator "What lingered with her was not a conversation, but the outline of one that never happened."
        narrator "A remembered glance. A face at the edge of a crowded room. The small irritation of wondering whether one missed moment deserved to stay in the mind this long."

    huyen smile "You look like you're trying to win a private argument with a spreadsheet."
    tam thoughtful "I'm trying to understand why this contractor note was written like a threat letter."
    huyen laugh "That's not a spreadsheet problem. That's a culture problem."

    narrator "Tam smiled despite herself and circled two lines in her notebook."
    narrator "Work still came first. It just no longer felt like the only thing moving quietly under her skin."

    return


label tam_c02_quan_intro:

    scene bg_meeting_room_day
    with dissolve

    narrator "A few days later, Tam finally met the department lead people kept warning new staff about."
    narrator "His name had reached her before he did."

    coworker "You two are joining Anh Quân's coordination team, right?"
    huyen neutral "Yes. Why does that sound like a weather bulletin?"
    coworker "Because he's good, exacting, and not emotionally committed to making anyone feel comfortable."
    tam surprised "That is a very efficient character summary."
    coworker "You'll see. If he says 'good,' celebrate quietly. If he says 'temporary,' fix it immediately. If he says nothing..." 
    huyen thoughtful "We should simply understand?"
    coworker "Exactly."

    narrator "Tam remembered that line longer than she expected to."
    narrator "Not because it frightened her."
    narrator "Only because some people could make the air straighten up before they even entered the room."

    narrator "When Quân finally did enter, he looked more ordinary than the rumors allowed."
    narrator "Plain shirt. Sleeves rolled neatly. Eyes already half on the documents in his hand."

    quan serious "I'm Quân. I don't need anyone here to prove they're intelligent by speaking too much."
    quan neutral "If you can do the work, let the result speak. If you're unclear, ask. If you're wrong, fix it. Don't hide it."
    quan serious "And don't perform competence. It photographs well, but it does nothing for a deadline."

    narrator "The room went quiet in the specific way quiet rooms do when everyone suddenly sits a little straighter."

    if "tam_work_skill_strong_c01" in progress["player_flags"]:
        narrator "Oddly enough, the advice did not feel hostile to Tam."
        narrator "It sounded like the stricter version of the conclusion she had already started reaching on her own."

    huyen thoughtful "He really does speak like an audit report."
    tam smile "At least now we know the report is real."

    return


label tam_c02_party_opening:

    scene bg_company_year_end_party
    with fade

    narrator "At the end of the month, the company held a small internal gathering after a long review meeting with several partner teams."
    narrator "It was not grand enough to be called a gala, but it was polished enough to make Tam hold her plate more carefully than necessary."

    huyen happy "The food looks expensive."
    tam neutral "That usually means there won't be enough of it."
    huyen laugh "Your optimism continues to inspire the nation."

    narrator "Tam picked up a small savory pastry and, without really thinking about it, wiped a thin line of sauce from the edge of the plate with a napkin."

    huyen surprised "Did you just quality-check party food?"
    tam embarrassed "It was crooked."
    huyen smile "You've been under Quân for two weeks and already started correcting geometry in public."

    narrator "Across the room, Quân was speaking with a man in a dark blazer whose posture was relaxed in a way that did not read as careless."
    narrator "Even before Tam saw his face clearly, something in her recognized the stillness around him."

    if has_player_flag("hoang_first_contact_c01"):
        narrator "When he turned, the recognition became immediate."
        narrator "Hoàng."
        narrator "The same careful smile. The same sense that he never needed to occupy the center of a room to be noticed inside it."
    elif has_player_flag("hoang_no_contact_c01"):
        narrator "The face was familiar even before she placed why."
        narrator "Then memory caught up: the young man from the year-end party, the one she had not crossed the room to greet."
    else:
        narrator "He looked like the kind of person who could stand beside someone severe without making the whole room feel more severe by association."

    coworker "That's Hoàng. He works in architectural and workspace design."
    coworker "He's helping with the office reconfiguration proposal. Anh Quân trusts him enough to argue honestly in front of him."

    huyen neutral "So that's already impressive."
    tam thoughtful "Yeah."

    narrator "Hoàng tipped his head slightly at something Quân said."
    narrator "The gesture was small, but it softened the edge of Quân's expression for half a second."
    narrator "Tam noticed that more than she meant to."

    return


label tam_c02_pre_hoang_choice:

    narrator "A few minutes later, someone brushed the cocktail table near Tam on the way past."
    narrator "A glass near the edge trembled once."

    menu:
        "How should Tam react?"

        "Steady the glass without saying anything.":
            $ tam_c02_hoang_noticed = True
            $ hoang_impression += 1
            narrator "Tam reached out and nudged the glass back toward the center before it could tip."
            huyen smile "You just prevented an orange-juice level disaster."
            tam smile "Small disasters are still disasters."
            narrator "Across the room, Hoàng glanced over once, then looked away."

        "Warn Huyen before it spills.":
            tam surprised "Huyen, careful."
            huyen confused "What— oh."
            huyen smile "Good. My sleeve survives another day."

        "Let someone else handle it and stay in the conversation.":
            narrator "Tam was listening to a teammate explain three different kinds of proposal revision when the glass stopped shaking on its own."
            narrator "By the time she looked back, someone had already moved it inward."

    narrator "The room settled again into low music, glassware, and the kind of laughter people use when they are still at least partly on work time."
    narrator "Tam told herself this was only a company gathering."
    narrator "It would be ridiculous to treat one conversation as if it might change the temperature of the night."

    return


label tam_c02_main_choice:

    if has_player_flag("hoang_first_contact_c01"):
        huyen smile "You're doing the thing again."
        tam confused "What thing?"
        huyen smile "Looking at him like you're checking whether last time actually happened."
    elif has_player_flag("hoang_no_contact_c01"):
        huyen smile "You're thinking about whether to fix last time, aren't you?"
        tam embarrassed "That is an annoyingly accurate sentence."
    else:
        huyen smile "You've looked over there three times already."
        tam surprised "Have I?"
        huyen laugh "The third one was practically academic research."

    menu:
        "What should Tam do?"

        "Walk over and speak to Hoàng yourself.":
            jump tam_c02_route_a

        "Stay where you are and wait a little longer.":
            if tam_c02_hoang_noticed:
                jump tam_c02_route_b
            else:
                jump tam_c02_route_c

        "Push Huyen into the conversation instead.":
            jump tam_c02_route_d

        "Keep it professional, talk work, and leave the moment alone.":
            jump tam_c02_route_c


label tam_c02_route_a:

    $ tam_c02_party_route = "A"
    $ tam_c02_meaningful_contact = True
    $ hoang_impression += 2
    $ progress["emotional_state"]["trust"] += 2
    $ add_unique(progress["player_flags"], "tam_c02_direct_approach")
    $ add_unique(progress["player_flags"], "tam_c02_meaningful_hoang_contact")
    $ add_unique(progress["player_flags"], "player_knows_hoang_restraint")

    narrator "Tam took one quiet breath and crossed the distance before she could talk herself out of it."

    if has_player_flag("hoang_first_contact_c01"):
        hoang surprised "Tam?"
        tam neutral "So you do remember me."
        hoang smile "You say that like you expected an audit instead."
        narrator "The answer arrived so quickly that Tam relaxed before she meant to."
    else:
        tam neutral "Hi. You're Hoàng, right?"
        hoang neutral "Yeah."
        hoang smile "And you're the person trying to attend a company gathering without letting a drop of sauce land anywhere inappropriate."
        tam embarrassed "That was observable from this far away?"

    hoang smile "More than observable. Memorable."
    narrator "He glanced at the plate in her hand, then back at her face."

    if has_player_flag("hoang_no_contact_c01"):
        hoang thoughtful "We were at the year-end party too. I thought you might come over then."
        tam embarrassed "I thought about it."
        hoang neutral "Thinking about it and doing it are different departments."
        tam smile "I'm trying a transfer request tonight."
    else:
        tam smile "That sounds dangerously close to teasing."
        hoang "Only a little."

    hoang thoughtful "Quân said your team has been absorbing most of the coordination pain on this workspace review."
    tam serious "That is a polite way to describe it."
    hoang smile "I'm trying not to alarm a new employee."
    tam "Too late. I already work for Quân."

    narrator "Hoàng laughed softly."
    narrator "The laugh was light, but it stayed."

    hoang neutral "Then I'll give you the useful version. You're doing fine. People who notice small things usually keep larger problems from becoming expensive."
    narrator "The line was simple. No flourish. No attempt to make itself sound meaningful."
    narrator "Because of that, it landed more deeply than Tam wanted to admit."

    tam smile "You say things like that very casually for someone standing next to a design proposal war zone."
    hoang smile "It's a survival trait."

    narrator "By the time Huyen drifted back into view, the room no longer felt quite so airless to Tam."

    jump tam_c02_after_routes


label tam_c02_route_b:

    $ tam_c02_party_route = "B"
    $ tam_c02_meaningful_contact = True
    $ hoang_impression += 2
    $ progress["emotional_state"]["trust"] += 1
    $ add_unique(progress["player_flags"], "tam_c02_hoang_approached")
    $ add_unique(progress["player_flags"], "tam_c02_meaningful_hoang_contact")
    $ add_unique(progress["player_flags"], "player_knows_hoang_restraint")

    narrator "Tam decided not to move first."
    narrator "A moment later, Huyen's eyes shifted past her shoulder."

    huyen smile "All right. Apparently the universe hates hesitation."
    tam confused "What does that mean?"

    narrator "She turned just as Hoàng stopped beside them."

    hoang neutral "Sorry. Am I interrupting?"
    tam surprised "No. Not at all."

    if has_player_flag("hoang_first_contact_c01"):
        hoang smile "Good. It would be embarrassing if I remembered your name and still chose the wrong timing."
        tam smile "At least that would prove you remembered it."
    else:
        hoang smile "I'm Hoàng."
        tam neutral "Tam."

    hoang thoughtful "I saw you move the glass before it spilled."
    tam embarrassed "That hardly counts as an achievement."
    hoang "Maybe not. That's why it stood out. Most people only notice the dramatic version of a problem."

    narrator "For one second, Tam could not tell whether that sentence was observation, praise, or simply the natural shape of how he thought."
    narrator "Then Hoàng glanced away and smiled with what looked almost like self-consciousness."

    hoang "Sorry. That sounded stranger out loud than it did in my head."
    tam smile "A little."
    huyen laugh "Don't worry. We all work with Quân now. Strange phrasing no longer scares us."

    narrator "That made Hoàng laugh. The tightness in the conversation broke immediately after."

    tam thoughtful "So are you redesigning the office for real, or just threatening us with the possibility?"
    hoang smile "Still assessing. Though if you want to file formal complaints about the pantry, I accept those too."
    tam "Good. It currently feels like a dental waiting room with better lighting."
    hoang laugh "That's brutally specific."

    narrator "Tam laughed too, this time without lowering the sound first."

    jump tam_c02_after_routes


label tam_c02_route_c:

    $ tam_c02_party_route = "C"
    $ progress["emotional_state"]["distance"] += 1
    $ add_unique(progress["player_flags"], "tam_c02_chose_work_focus")

    narrator "In the end, Tam stayed with the safer version of the evening."
    narrator "She asked one teammate how Quân preferred revision notes to be summarized."
    narrator "She memorized two names she had kept meaning to learn."
    narrator "She listened more than she spoke and felt, for once, that restraint could be its own kind of competence."

    narrator "At one point Quân passed by with Hoàng beside him."

    quan neutral "This is Tam. One of the new people on my team."

    if has_player_flag("hoang_first_contact_c01"):
        hoang smile "We've met."
        tam smile "Only briefly."
    elif has_player_flag("hoang_no_contact_c01"):
        hoang neutral "I think I saw you at the year-end party."
        tam neutral "Yeah. I think so too."
    else:
        hoang smile "Nice to meet you."
        tam smile "You too."

    narrator "The exchange lasted only a few seconds."
    narrator "A polite nod. A name attached properly to a face. Nothing more binding than that."

    narrator "Later, when Huyen texted from three steps away to ask whether Tam wanted to leave together, the answer came easily."
    narrator "Yes."

    jump tam_c02_after_routes


label tam_c02_route_d:

    $ tam_c02_party_route = "D"
    $ tam_c02_meaningful_contact = True
    $ hoang_impression += 1
    $ huyen_trust += 1
    $ progress["emotional_state"]["trust"] += 1
    $ add_unique(progress["player_flags"], "tam_c02_supported_huyen")
    $ add_unique(progress["player_flags"], "tam_c02_meaningful_hoang_contact")
    $ add_unique(progress["player_flags"], "player_knows_hoang_restraint")

    tam smile "You should go talk to him."
    huyen surprised "About what?"
    tam "About whether architecture can save the pantry from feeling like preventive dentistry."
    huyen "That was my joke."
    tam "Then you should stand behind your art."

    narrator "Huyen gave her a scandalized look, then went anyway."

    huyen neutral "Hi. You're Hoàng, right?"
    hoang smile "Yeah. And you are?"
    huyen "Huyền. New staff member. Representative of pantry-related suffering."

    narrator "Hoàng paused just long enough for Tam to wonder whether Huyen had overcommitted."
    narrator "Then he laughed."

    hoang laugh "That is a remarkably strong opening statement."
    huyen happy "I believe in actionable feedback."
    hoang smile "Then yes, actionable feedback is welcome."

    narrator "Tam stayed a few steps away at first, listening to Huyen turn a joke into a full conversation with the confidence of someone born for exactly that kind of moment."
    narrator "Whenever Huyen's energy ran a little too far ahead of itself, Tam reached over and tugged lightly at her sleeve."
    narrator "Each time, Huyen slowed by half a breath."
    narrator "Each time, Hoàng noticed."

    huyen smile "My friend is Tâm. She's pretending she didn't engineer this whole interaction."
    tam embarrassed "Huyen."
    hoang smile "Then I should thank Tam too."
    tam "You don't have to. I was only supporting internal communications."
    hoang laugh "That sounds like a department title Quân would accidentally make real."

    narrator "The three of them kept talking for a while after that."
    narrator "Tam spoke less than Huyen did, but every time she did, Hoàng answered as if he had been listening for her part specifically."

    jump tam_c02_after_routes


label tam_c02_after_routes:

    scene bg_company_year_end_party_late
    with dissolve

    if tam_c02_party_route == "A":
        huyen smile "Well?"
        tam embarrassed "Well what?"
        huyen smile "Architecture."
        tam pouty "You're impossible."
        narrator "Tam looked down at her employee badge. It had shifted slightly off-center again."
        narrator "She straightened it, but more slowly than usual."

    elif tam_c02_party_route == "B":
        huyen smile "So he came over on his own."
        tam embarrassed "Yes."
        huyen laugh "I am being very normal about this."
        tam "That's exactly why I don't trust your face right now."

    elif tam_c02_party_route == "C":
        huyen neutral "Ready to go?"
        tam neutral "Yeah."
        huyen smile "Tomorrow is still Quân."
        tam serious "Please don't say that before bedtime."
        narrator "They left the gathering together, stepping into a corridor where the light was colder and the air easier to breathe."

    elif tam_c02_party_route == "D":
        huyen happy "He's easy to talk to."
        tam smile "He is."
        huyen surprised "That answer sounded suspiciously calm."
        tam neutral "I'm being generous and letting you enjoy your pantry diplomacy victory."
        narrator "Huyen looked delighted with herself. Tam, despite every effort, looked a little too pleased for that excuse to be fully convincing."

    if tam_c02_meaningful_contact:
        call tam_c02_short_hoang_pov

    jump tam_c02_complete


label tam_c02_short_hoang_pov:

    scene black
    with fade

    narrator "A little later."

    scene bg_meeting_room_day
    with dissolve

    quan serious "What do you think?"
    hoang thoughtful "About the office layout?"
    quan "No. About the new staff."

    narrator "Hoàng looked back toward the hall as if the answer might still be there, somewhere between the emptied glasses and the half-cleared plates."

    if tam_c02_party_route == "A":
        hoang smile "Tam is interesting."
        quan neutral "Interesting?"
        hoang "Quiet. But she makes people answer more honestly than they meant to."
        narrator "What stayed with him was not the joke about the sauce, or even the laugh after."
        narrator "It was the way she seemed to notice things before deciding whether to speak."

    elif tam_c02_party_route == "B":
        hoang neutral "She notices details."
        quan serious "I know. I hired her."
        narrator "Hoàng smiled at that, but he still remembered the small movement of her hand guiding the glass back from the edge before anyone else reacted."
        narrator "Some people revealed themselves most clearly through the smallest interventions."

    elif tam_c02_party_route == "D":
        hoang smile "Huyền carries the conversation. Tâm keeps the rhythm from breaking."
        quan neutral "Fast assessment."
        hoang "Occupational hazard."
        narrator "He remembered the light tug at Huyen's sleeve, subtle enough to be nearly invisible."
        narrator "Not everyone needed to stand at the center of a room to keep it balanced."

    quan serious "Either way, don't make life difficult for my new people."
    hoang laugh "You say that as if I'm an operational risk."
    quan neutral "You're a social risk. That's adjacent enough."

    narrator "Hoàng laughed and did not deny it."

    return


label tam_c02_complete:

    scene black
    with fade

    narrator "Tam got home later than usual that night."
    narrator "She placed her employee badge on the desk beside her notebook, opened to a clean page that would not stay clean for long."

    if tam_c02_party_route == "A":
        narrator "The last line she wrote was short:"
        narrator "'Hoàng — easier to talk to than expected.'"
    elif tam_c02_party_route == "B":
        narrator "The final note was slightly crooked."
        narrator "'Hoàng came over first.'"
    elif tam_c02_party_route == "C":
        narrator "The last line was entirely practical."
        narrator "'Ask again about proposal review flow.'"
    elif tam_c02_party_route == "D":
        narrator "She wrote Huyen's name first."
        narrator "'Huyen, Hoàng, pantry diplomacy.'"

    narrator "Outside the window, the city was still bright."
    narrator "Another workday had passed."
    narrator "Something small had either begun tonight, or moved one quiet step closer to beginning."

    $ complete_chapter("tam_c02")
    jump route_map
