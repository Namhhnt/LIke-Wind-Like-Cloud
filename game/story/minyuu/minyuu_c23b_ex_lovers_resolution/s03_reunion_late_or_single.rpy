# FILE: game/story/minyuu/minyuu_c23b_ex_lovers_resolution/s03_reunion_late_or_single.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label minyuu_c23b_ex_lovers_resolution_s03_reunion_late_or_single:
    "MVP: Ex-lovers final resolution seed."
    menu:
        "Final Minh-Yuuka ex-lovers direction:"

        "Reunion":
            $ story_add_ending_support('e10_minyuu_reunion')
            $ story_add('minh_yuuka_trust', 2)

        "Late reunion":
            $ story_add_ending_support('e11_minyuu_late_reunion')

        "Mutual single":
            $ story_add_ending_support('e18_minyuu_mutual_single')

        "Unresolved doom":
            $ story_add_ending_support('e24_doom')
    return
