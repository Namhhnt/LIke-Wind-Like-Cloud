# FILE: game/story/thienan/thienan_c21a_minh_possible/s04_route_commit_or_release.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label thienan_c21a_minh_possible_s04_route_commit_or_release:
    "MVP: Thiên An route seed is confirmed."
    menu:
        "Confirm Thiên An's direction."

        "Minh":
            $ story_add_direction('thienan', 'thienan_minh_commit')
            $ story_add_ending_support('e07_thienan_minh')

        "Quang":
            $ story_add_ending_support('e06_thienan_quang')

        "Single":
            $ story_add_ending_support('e08_thienan_single')

        "Arranged marriage":
            $ story_add_ending_support('e09_thienan_arranged')
    return
