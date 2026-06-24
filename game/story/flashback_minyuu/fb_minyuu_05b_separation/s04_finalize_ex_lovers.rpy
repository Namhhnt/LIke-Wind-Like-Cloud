# FILE: game/story/flashback_minyuu/fb_minyuu_05b_separation/s04_finalize_ex_lovers.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label fb_minyuu_05b_separation_s04_finalize_ex_lovers:
    "MVP: Finalize Minh-Yuuka as ex lovers long separated. Other Minh pairings are locked."
    $ story_set_minyuu_relation('ex_lovers_long_separated')
    menu:
        "What future remains possible?"

        "They may return to each other":
            $ story_add_ending_support('e10_minyuu_reunion')
            $ story_add('minh_yuuka_trust', 1)

        "They may meet again much later":
            $ story_add_ending_support('e11_minyuu_late_reunion')

        "They may forgive but remain single":
            $ story_add_ending_support('e18_minyuu_mutual_single')
    return
