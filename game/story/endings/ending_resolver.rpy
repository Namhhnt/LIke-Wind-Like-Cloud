# FILE: game/story/endings/ending_resolver.rpy
# Purpose: Jump to the selected ending label.

label ending_resolver:
    $ selected_ending = resolve_story_ending()

    if selected_ending == 'e01_canon_true':
        jump e01_canon_true
    elif selected_ending == 'e02_tam_hoang':
        jump e02_tam_hoang
    elif selected_ending == 'e03_tam_minh':
        jump e03_tam_minh
    elif selected_ending == 'e04_hoang_huyen':
        jump e04_hoang_huyen
    elif selected_ending == 'e05_huyen_quan':
        jump e05_huyen_quan
    elif selected_ending == 'e06_thienan_quang':
        jump e06_thienan_quang
    elif selected_ending == 'e07_thienan_minh':
        jump e07_thienan_minh
    elif selected_ending == 'e08_thienan_single':
        jump e08_thienan_single
    elif selected_ending == 'e09_thienan_arranged':
        jump e09_thienan_arranged
    elif selected_ending == 'e10_minyuu_reunion':
        jump e10_minyuu_reunion
    elif selected_ending == 'e11_minyuu_late_reunion':
        jump e11_minyuu_late_reunion
    elif selected_ending == 'e12_minyuu_private_lovers':
        jump e12_minyuu_private_lovers
    elif selected_ending == 'e13_minyuu_public_lovers':
        jump e13_minyuu_public_lovers
    elif selected_ending == 'e14_minyuu_non_marriage':
        jump e14_minyuu_non_marriage
    elif selected_ending == 'e15_minyuu_long_distance':
        jump e15_minyuu_long_distance
    elif selected_ending == 'e16_minh_single':
        jump e16_minh_single
    elif selected_ending == 'e17_yuuka_single':
        jump e17_yuuka_single
    elif selected_ending == 'e18_minyuu_mutual_single':
        jump e18_minyuu_mutual_single
    elif selected_ending == 'e19_yuuka_career':
        jump e19_yuuka_career
    elif selected_ending == 'e20_minyuu_friendship':
        jump e20_minyuu_friendship
    elif selected_ending == 'e21_tam_independent':
        jump e21_tam_independent
    elif selected_ending == 'e22_huyen_independent':
        jump e22_huyen_independent
    elif selected_ending == 'e23_hoang_single_growth':
        jump e23_hoang_single_growth
    else:
        jump e24_doom

