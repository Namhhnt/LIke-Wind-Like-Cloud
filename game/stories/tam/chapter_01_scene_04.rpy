# Chapter 01, Scene 04

label tam_c01_year_end_after_meeting:

    scene bg_company_year_end_party_late
    with dissolve

    narrator "That night, as the party drifted toward its end, Tam stood by the glass looking down at the city."

    narrator "Small streams of cars passed below the building like connected streaks of light."

    huyen neutral "Well?"

    tam neutral "Well what?"

    huyen smile "Your side project."

    tam embarrassed "Call him a side project one more time and I'll report you to quality management."

    huyen serious "I'm just assessing the risk."

    tam surprised "What risk?"

    huyen serious "The risk that you start liking him before you even know who he is."

    narrator "Tam turns away."

    narrator "Her cheeks feel a little warm. Maybe from the fruit wine."

    narrator "Maybe not."

    if "huyen_trust_high_c01" in progress["player_flags"]:
        huyen serious "But if something real happens, tell me."
        huyen smile "I can't promise the right advice. But I can promise I'll listen before I judge."
        tam smile "That sounds weirdly mature."
        huyen happy "I'm performing. But I mean it, too."

    narrator "Tam laughs softly."

    narrator "She does not know where that brief encounter will lead her."

    narrator "She only knows that, on a year-end night full of voices and light, one gaze lingered on her for a beat longer than it had to."

    narrator "And sometimes, one beat is enough to make the wind change direction."

    jump tam_c01_end
