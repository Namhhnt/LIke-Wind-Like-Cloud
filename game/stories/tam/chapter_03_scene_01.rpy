# Chapter 03, Scene 01

label tam_c03:
    # Direction-gated core event demo: this chapter depends on Hoang taking one bonus direction.
    "Tam can only reach this moment after Hoang's route has taken one of its two optional emotional directions."
    "That makes the route map prove a real exclusion-driven dependency instead of a simple linear chain."
    "[get_emotional_hint()]"

    if choice_is_available("notice_subtle_reaction"):
        "Because the player has seen Hoang's earlier hesitation, Tam notices a subtle reaction that would otherwise pass unseen."

    menu:
        "How should Tam respond?"

        "Ask gently" if choice_is_available("ask_gently"):
            $ add_unique(progress["player_flags"], "tam_choice_gentle")
            $ progress["emotional_state"]["trust"] += 1
            "Tam softens her words and lets the moment breathe."

        "Choose direct affection" if choice_is_available("choose_direct_affection"):
            $ add_unique(progress["player_flags"], "tam_choice_direct")
            $ progress["emotional_state"]["misunderstanding"] += 1
            "Tam pushes forward directly, even if the timing is dangerous."

        "Say nothing for now":
            $ add_unique(progress["player_flags"], "tam_choice_silence")
            "Tam decides the silence still says enough for now."

    $ complete_chapter("tam_c03")
    jump route_map
