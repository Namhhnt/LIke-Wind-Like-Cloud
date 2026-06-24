# FILE: game/ending_rules.rpy
# Purpose: Ending condition helpers and final resolver.

init python:
    def can_get_canon_true():
        return (
            story_state["hoang_tam_trust"] >= 5
            and story_state["minh_yuuka_relation"] in ["ex_lovers_long_separated", "still_lovers"]
            and story_state["minh_yuuka_trust"] >= 5
            and story_state["huyen_quan_trust"] >= 4
            and story_state["thienan_quang_trust"] >= 4
            and story_state["doom_score"] < 5
            and story_has_ending_support("e01_canon_true")
        )

    def can_get_tam_hoang():
        return (
            story_state["hoang_tam_trust"] >= 5
            and not story_has_direction("tam", "tam_minh_commit")
            and story_state["hoang_insecurity"] < 6
            and story_has_ending_support("e02_tam_hoang")
        )

    def can_get_tam_minh():
        return (
            story_state["minh_yuuka_relation"] == "old_close_friends"
            and not story_state["minh_romance_lock"]
            and story_state["tam_minh_drawn"] >= 4
            and story_has_direction("tam", "tam_minh_commit")
            and story_has_ending_support("e03_tam_minh")
        )

    def can_get_hoang_huyen():
        return (
            story_state["hoang_huyen_interest"] >= 4
            and story_state["huyen_hoang_interest"] >= 4
            and not story_has_direction("tam", "tam_hoang_commit")
            and story_has_ending_support("e04_hoang_huyen")
        )

    def can_get_huyen_quan():
        return (
            story_state["huyen_quan_trust"] >= 4
            and not story_has_direction("huyen", "huyen_hoang_commit")
            and story_has_ending_support("e05_huyen_quan")
        )

    def can_get_thienan_quang():
        return (
            story_state["thienan_quang_trust"] >= 4
            and story_state["family_pressure_thienan"] < 6
            and story_has_ending_support("e06_thienan_quang")
        )

    def can_get_thienan_minh():
        return (
            story_state["minh_yuuka_relation"] == "old_close_friends"
            and not story_state["minh_romance_lock"]
            and story_state["thienan_minh_residue"] >= 4
            and story_has_direction("thienan", "thienan_minh_commit")
            and story_has_ending_support("e07_thienan_minh")
        )

    def can_get_thienan_single():
        return (
            story_state["thienan_self_assertion"] >= 4
            and story_has_ending_support("e08_thienan_single")
        )

    def can_get_thienan_arranged():
        return (
            story_state["family_pressure_thienan"] >= 5
            and story_has_ending_support("e09_thienan_arranged")
        )

    def can_get_minh_single():
        return (
            story_state["minh_yuuka_relation"] in ["old_close_friends", "ex_lovers_long_separated"]
            and story_has_ending_support("e16_minh_single")
        )

    def can_get_yuuka_single():
        return (
            story_state["minh_yuuka_relation"] in ["old_close_friends", "ex_lovers_long_separated"]
            and story_has_ending_support("e17_yuuka_single")
        )

    def can_get_yuuka_career():
        return story_has_ending_support("e19_yuuka_career")

    def can_get_minyuu_friendship():
        return (
            story_state["minh_yuuka_relation"] == "old_close_friends"
            and story_state["minh_yuuka_trust"] >= 3
            and story_has_ending_support("e20_minyuu_friendship")
        )

    def can_get_tam_independent():
        return (
            story_state["tam_self_clarity"] >= 4
            and story_has_ending_support("e21_tam_independent")
        )

    def can_get_huyen_independent():
        return (
            story_state["career_huyen"] >= 3
            and story_has_ending_support("e22_huyen_independent")
        )

    def can_get_hoang_single_growth():
        return (
            story_state["hoang_self_acceptance"] >= 4
            and story_has_ending_support("e23_hoang_single_growth")
        )

    def resolve_ex_lovers_ending():
        if story_has_ending_support("e10_minyuu_reunion") and story_state["minh_yuuka_trust"] >= 5:
            return "e10_minyuu_reunion"

        if story_has_ending_support("e11_minyuu_late_reunion") and story_state["minh_yuuka_trust"] >= 3:
            return "e11_minyuu_late_reunion"

        if story_has_ending_support("e18_minyuu_mutual_single"):
            return "e18_minyuu_mutual_single"

        if story_state["minh_yuuka_unresolved"] >= 6:
            return "e24_doom"

        if can_get_minh_single():
            return "e16_minh_single"

        if can_get_yuuka_single():
            return "e17_yuuka_single"

        return None

    def resolve_still_lovers_ending():
        if story_has_ending_support("e13_minyuu_public_lovers"):
            return "e13_minyuu_public_lovers"
        if story_has_ending_support("e14_minyuu_non_marriage"):
            return "e14_minyuu_non_marriage"
        if story_has_ending_support("e15_minyuu_long_distance"):
            return "e15_minyuu_long_distance"
        return "e12_minyuu_private_lovers"

    def resolve_story_ending():
        relation = story_state["minh_yuuka_relation"]

        if story_state["doom_score"] >= 8 or story_has_ending_support("e24_doom"):
            return "e24_doom"

        if can_get_canon_true():
            return "e01_canon_true"

        if relation == "still_lovers":
            return resolve_still_lovers_ending()

        if relation == "ex_lovers_long_separated":
            resolved = resolve_ex_lovers_ending()
            if resolved:
                return resolved

        if relation == "old_close_friends":
            if can_get_tam_minh():
                return "e03_tam_minh"
            if can_get_thienan_minh():
                return "e07_thienan_minh"
            if can_get_minyuu_friendship():
                return "e20_minyuu_friendship"

        if can_get_tam_hoang():
            return "e02_tam_hoang"
        if can_get_hoang_huyen():
            return "e04_hoang_huyen"
        if can_get_huyen_quan():
            return "e05_huyen_quan"
        if can_get_thienan_quang():
            return "e06_thienan_quang"
        if can_get_yuuka_career():
            return "e19_yuuka_career"
        if can_get_tam_independent():
            return "e21_tam_independent"
        if can_get_huyen_independent():
            return "e22_huyen_independent"
        if can_get_hoang_single_growth():
            return "e23_hoang_single_growth"
        if can_get_thienan_single():
            return "e08_thienan_single"
        if can_get_thienan_arranged():
            return "e09_thienan_arranged"
        if can_get_minh_single():
            return "e16_minh_single"
        if can_get_yuuka_single():
            return "e17_yuuka_single"

        return "e24_doom"

