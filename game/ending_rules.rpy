# FILE: game/ending_rules.rpy
# Purpose: Ending condition helpers and final resolver.
# All numeric conditions use the 0-100 score scale from story_state.rpy.

init python:
    # ----------------------------
    # Thresholds
    # ----------------------------
    T_TAM_HOANG_INTEREST = 75
    T_TAM_MID_MINGAP = 50
    T_TAM_MINH_DRAWN = 90
    T_TAM_CLARITY_NORMAL = 50
    T_TAM_CLARITY_MINH = 75
    T_TAM_RESPECT_YUUKA_NORMAL = 25
    T_TAM_RESPECT_YUUKA_MINH = 50
    T_TAM_INSECURITY_MAX = 25
    T_TAM_OBSERVATION_NORMAL = 25
    T_TAM_OBSERVATION_MINH = 50
    T_CAREER_TAM_NORMAL = 50
    T_CAREER_TAM_MINH = 75

    T_HOANG_TAM_TRUST = 75
    T_HOANG_HUYEN_INTEREST = 75
    T_HOANG_INSECURITY_MAX = 15
    T_HOANG_SELF_ACCEPTANCE = 80
    T_HOANG_PROFESSIONAL_CREDIT = 90

    T_HUYEN_QUAN_TRUST = 75
    T_HUYEN_HOANG_INTEREST = 75
    T_CAREER_HUYEN = 50

    T_THIENAN_QUANG_TRUST = 90
    T_THIENAN_MINH_RESIDUE = 50
    T_FAMILY_PRESSURE_ARRANGED = 60
    T_THIENAN_SELF_ASSERTION = 50

    T_MINYUU_TRUST = 80
    T_MINYUU_INTIMACY = 75
    T_MINYUU_UNRESOLVED_MAX = 28
    T_MINYUU_BRANCH_SCORE = 80
    T_MINYUU_ROMANTIC = 43
    T_MINYUU_BOUNDARY_MAX = 34

    T_DOOM_HARD = 80
    T_DOOM_CANON_MAX = 49

    def score(key, default=0):
        getter = globals().get("story_get_score", None)
        if callable(getter):
            return getter(key, default)
        try:
            return int(story_state.get(key, default))
        except Exception:
            return default

    def minyuu_branch_score_ok():
        relation = story_state.get("minh_yuuka_relation")
        if relation == "old_close_friends":
            return score("old_friend_score") >= T_MINYUU_BRANCH_SCORE
        if relation == "ex_lovers_long_separated":
            return score("ex_lover_score") >= T_MINYUU_BRANCH_SCORE
        if relation == "still_lovers":
            return score("still_lover_score") >= T_MINYUU_BRANCH_SCORE
        return False

    def minyuu_shared_arc_ok():
        return (
            story_state.get("minh_yuuka_relation") in ["old_close_friends", "ex_lovers_long_separated", "still_lovers"]
            and score("minh_yuuka_trust") >= T_MINYUU_TRUST
            and score("minh_yuuka_intimacy") >= T_MINYUU_INTIMACY
            and score("minh_yuuka_unresolved") <= T_MINYUU_UNRESOLVED_MAX
            and minyuu_branch_score_ok()
            and score("romantic_score") >= T_MINYUU_ROMANTIC
            and score("boundary_score") <= T_MINYUU_BOUNDARY_MAX
        )

    def thienan_family_pressure_overrides_self():
        return (
            score("family_pressure_thienan") >= T_FAMILY_PRESSURE_ARRANGED
            and score("family_pressure_thienan") > score("thienan_self_assertion")
        )

    def thienan_is_free_from_family_arrangement():
        return not thienan_family_pressure_overrides_self()

    def hoang_growth_ok():
        return (
            score("hoang_insecurity") <= T_HOANG_INSECURITY_MAX
            and score("hoang_self_acceptance") >= T_HOANG_SELF_ACCEPTANCE
            and score("hoang_professional_credit") >= T_HOANG_PROFESSIONAL_CREDIT
        )

    # ----------------------------
    # Main couple / route endings
    # ----------------------------
    def can_get_canon_true():
        return (
            story_state.get("minh_yuuka_relation") in ["ex_lovers_long_separated", "still_lovers"]
            and minyuu_shared_arc_ok()
            and score("tam_hoang_interest") >= T_TAM_HOANG_INTEREST
            and score("hoang_tam_trust") >= T_HOANG_TAM_TRUST
            and score("huyen_quan_trust") >= T_HUYEN_QUAN_TRUST
            and score("career_huyen") >= T_CAREER_HUYEN
            and score("thienan_quang_trust") >= T_THIENAN_QUANG_TRUST
            and thienan_is_free_from_family_arrangement()
            and score("doom_score") <= T_DOOM_CANON_MAX
            and story_has_ending_support("e01_canon_true")
        )

    def can_get_tam_hoang():
        return (
            score("tam_hoang_interest") >= T_TAM_HOANG_INTEREST
            and score("tam_minh_drawn") >= T_TAM_MID_MINGAP
            and score("tam_self_clarity") >= T_TAM_CLARITY_NORMAL
            and score("tam_respect_yuuka") >= T_TAM_RESPECT_YUUKA_NORMAL
            and score("tam_insecurity") <= T_TAM_INSECURITY_MAX
            and score("tam_observation") >= T_TAM_OBSERVATION_NORMAL
            and score("career_tam") >= T_CAREER_TAM_NORMAL
            and score("hoang_tam_trust") >= T_HOANG_TAM_TRUST
            and hoang_growth_ok()
            and not story_has_direction("tam", "tam_minh_commit")
            and story_has_ending_support("e02_tam_hoang")
        )

    def can_get_tam_minh():
        return (
            story_state.get("minh_yuuka_relation") == "old_close_friends"
            and not story_state.get("minh_romance_lock", False)
            and minyuu_shared_arc_ok()
            and score("tam_hoang_interest") <= T_TAM_MID_MINGAP
            and score("hoang_tam_trust") >= T_TAM_MID_MINGAP
            and score("tam_minh_drawn") >= T_TAM_MINH_DRAWN
            and score("tam_self_clarity") >= T_TAM_CLARITY_MINH
            and score("tam_respect_yuuka") >= T_TAM_RESPECT_YUUKA_MINH
            and score("tam_insecurity") <= T_TAM_INSECURITY_MAX
            and score("tam_observation") >= T_TAM_OBSERVATION_MINH
            and score("career_tam") >= T_CAREER_TAM_MINH
            and story_has_direction("tam", "tam_minh_commit")
            and story_has_ending_support("e03_tam_minh")
        )

    def can_get_hoang_huyen():
        return (
            score("hoang_huyen_interest") >= T_HOANG_HUYEN_INTEREST
            and score("huyen_hoang_interest") >= T_HUYEN_HOANG_INTEREST
            and score("career_huyen") >= T_CAREER_HUYEN
            and hoang_growth_ok()
            and not story_has_direction("tam", "tam_hoang_commit")
            and story_has_ending_support("e04_hoang_huyen")
        )

    def can_get_huyen_quan():
        return (
            score("huyen_quan_trust") >= T_HUYEN_QUAN_TRUST
            and score("career_huyen") >= T_CAREER_HUYEN
            and not story_has_direction("huyen", "huyen_hoang_commit")
            and story_has_ending_support("e05_huyen_quan")
        )

    def can_get_thienan_quang():
        return (
            score("thienan_quang_trust") >= T_THIENAN_QUANG_TRUST
            and score("thienan_self_assertion") >= T_THIENAN_SELF_ASSERTION
            and thienan_is_free_from_family_arrangement()
            and story_has_ending_support("e06_thienan_quang")
        )

    def can_get_thienan_minh():
        return (
            story_state.get("minh_yuuka_relation") == "old_close_friends"
            and not story_state.get("minh_romance_lock", False)
            and minyuu_shared_arc_ok()
            and score("thienan_minh_residue") >= T_THIENAN_MINH_RESIDUE
            and score("thienan_self_assertion") >= T_THIENAN_SELF_ASSERTION
            and thienan_is_free_from_family_arrangement()
            and story_has_direction("thienan", "thienan_minh_commit")
            and story_has_ending_support("e07_thienan_minh")
        )

    def can_get_thienan_single():
        return (
            score("thienan_self_assertion") >= T_THIENAN_SELF_ASSERTION
            and thienan_is_free_from_family_arrangement()
            and story_has_ending_support("e08_thienan_single")
        )

    def can_get_thienan_arranged():
        return (
            thienan_family_pressure_overrides_self()
            and story_has_ending_support("e09_thienan_arranged")
        )

    # ----------------------------
    # Solo / support endings
    # ----------------------------
    def can_get_minh_single():
        return (
            story_state.get("minh_yuuka_relation") in ["old_close_friends", "ex_lovers_long_separated"]
            and story_has_ending_support("e16_minh_single")
        )

    def can_get_yuuka_single():
        return (
            story_state.get("minh_yuuka_relation") in ["old_close_friends", "ex_lovers_long_separated"]
            and story_has_ending_support("e17_yuuka_single")
        )

    def can_get_yuuka_career():
        return (
            minyuu_shared_arc_ok()
            and story_has_ending_support("e19_yuuka_career")
        )

    def can_get_minyuu_friendship():
        return (
            story_state.get("minh_yuuka_relation") == "old_close_friends"
            and minyuu_shared_arc_ok()
            and story_has_ending_support("e20_minyuu_friendship")
        )

    def can_get_tam_independent():
        return (
            score("tam_self_clarity") >= T_TAM_CLARITY_NORMAL
            and score("career_tam") >= T_CAREER_TAM_NORMAL
            and story_has_ending_support("e21_tam_independent")
        )

    def can_get_huyen_independent():
        return (
            score("career_huyen") >= T_CAREER_HUYEN
            and story_has_ending_support("e22_huyen_independent")
        )

    def can_get_hoang_single_growth():
        return (
            score("hoang_self_acceptance") >= T_HOANG_SELF_ACCEPTANCE
            and score("hoang_professional_credit") >= T_HOANG_PROFESSIONAL_CREDIT
            and story_has_ending_support("e23_hoang_single_growth")
        )

    # ----------------------------
    # Minh-Yuuka branch resolvers
    # ----------------------------
    def resolve_ex_lovers_ending():
        if not minyuu_shared_arc_ok():
            return "e24_doom"

        if story_has_ending_support("e10_minyuu_reunion"):
            return "e10_minyuu_reunion"

        if story_has_ending_support("e11_minyuu_late_reunion"):
            return "e11_minyuu_late_reunion"

        if story_has_ending_support("e18_minyuu_mutual_single"):
            return "e18_minyuu_mutual_single"

        if score("minh_yuuka_unresolved") > T_MINYUU_UNRESOLVED_MAX:
            return "e24_doom"

        if can_get_minh_single():
            return "e16_minh_single"

        if can_get_yuuka_single():
            return "e17_yuuka_single"

        return None

    def resolve_still_lovers_ending():
        if not minyuu_shared_arc_ok():
            return "e24_doom"

        if story_has_ending_support("e13_minyuu_public_lovers"):
            return "e13_minyuu_public_lovers"
        if story_has_ending_support("e14_minyuu_non_marriage"):
            return "e14_minyuu_non_marriage"
        if story_has_ending_support("e15_minyuu_long_distance"):
            return "e15_minyuu_long_distance"
        return "e12_minyuu_private_lovers"

    def resolve_story_ending():
        relation = story_state.get("minh_yuuka_relation", "unknown")

        if score("doom_score") >= T_DOOM_HARD or story_has_ending_support("e24_doom"):
            return "e24_doom"

        # Minh/Yuuka flashback phase is mandatory. Missing or failed relation resolution
        # means the story never reaches a valid final branch.
        if relation not in ["old_close_friends", "ex_lovers_long_separated", "still_lovers"]:
            return "e24_doom"

        if not minyuu_shared_arc_ok():
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

        # Thiên An's arranged marriage is checked before normal side-route endings so the
        # family-crisis pressure cannot be accidentally swallowed by a softer fallback.
        if can_get_thienan_arranged():
            return "e09_thienan_arranged"

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
        if can_get_minh_single():
            return "e16_minh_single"
        if can_get_yuuka_single():
            return "e17_yuuka_single"

        return "e24_doom"
