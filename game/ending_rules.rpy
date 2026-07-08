# FILE: game/ending_rules.rpy
# Purpose: Ending condition helpers, final resolver, and achievement/world-state finalization.
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


    # ----------------------------
    # Safe state helpers
    # ----------------------------
    def score(key, default=0):
        getter = globals().get("story_get_score", None)
        if callable(getter):
            return getter(key, default)

        try:
            return int(story_state.get(key, default))
        except Exception:
            return default


    def ending_story_flags():
        try:
            return list(story_flags or [])
        except Exception:
            return []


    def ending_progress():
        try:
            if isinstance(progress, dict):
                return progress
        except Exception:
            pass
        return {}


    def ending_has_flag(flag_name):
        flag_name = str(flag_name)

        if flag_name in ending_story_flags():
            return True

        p = ending_progress()

        if flag_name in (p.get("player_flags", []) or []):
            return True

        # Completed chapter aliases.
        if flag_name.startswith("chapter:"):
            chapter_id = flag_name.split("chapter:", 1)[1]
            if chapter_id in (p.get("completed_chapters", []) or []):
                return True
            try:
                if chapter_id in (story_completed_chapters or []):
                    return True
            except Exception:
                pass

        if flag_name.startswith("completed:"):
            chapter_id = flag_name.split("completed:", 1)[1]
            if chapter_id in (p.get("completed_chapters", []) or []):
                return True
            try:
                if chapter_id in (story_completed_chapters or []):
                    return True
            except Exception:
                pass

        return False


    def ending_has_support(ending_id):
        """
        Safe wrapper around story_has_ending_support(...).
        Also accepts direct flags with the same name for future flexibility.
        """
        ending_id = str(ending_id)

        fn = globals().get("story_has_ending_support", None)
        if callable(fn):
            try:
                if fn(ending_id):
                    return True
            except Exception:
                pass

        try:
            if ending_id in (story_state.get("ending_support", []) or []):
                return True
        except Exception:
            pass

        return ending_has_flag(ending_id)


    def ending_has_direction(character, direction):
        """
        Safe wrapper around story_has_direction(...).
        Falls back to common direction flag formats.
        """
        character = str(character)
        direction = str(direction)

        fn = globals().get("story_has_direction", None)
        if callable(fn):
            try:
                if fn(character, direction):
                    return True
            except Exception:
                pass

        return (
            ending_has_flag("direction_%s_%s" % (character, direction))
            or ending_has_flag("direction:%s:%s" % (character, direction))
        )


    def ending_has_marker(*names):
        """
        Checks either story flags or ending_support.

        Useful for final/world-state markers:
            crisis_best_outcome
            ach_tier_perfect
            e_quan_support
        """
        for name in names:
            if ending_has_flag(name) or ending_has_support(name):
                return True
        return False


    # ----------------------------
    # Core MinYuu helpers
    # ----------------------------
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
            and ending_has_support("e01_canon_true")
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
            and not ending_has_direction("tam", "tam_minh_commit")
            and ending_has_support("e02_tam_hoang")
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
            and ending_has_direction("tam", "tam_minh_commit")
            and ending_has_support("e03_tam_minh")
        )


    def can_get_hoang_huyen():
        return (
            score("hoang_huyen_interest") >= T_HOANG_HUYEN_INTEREST
            and score("huyen_hoang_interest") >= T_HUYEN_HOANG_INTEREST
            and score("career_huyen") >= T_CAREER_HUYEN
            and hoang_growth_ok()
            and not ending_has_direction("tam", "tam_hoang_commit")
            and ending_has_support("e04_hoang_huyen")
        )


    def can_get_huyen_quan():
        return (
            score("huyen_quan_trust") >= T_HUYEN_QUAN_TRUST
            and score("career_huyen") >= T_CAREER_HUYEN
            and not ending_has_direction("huyen", "huyen_hoang_commit")
            and ending_has_support("e05_huyen_quan")
        )


    def can_get_thienan_quang():
        return (
            score("thienan_quang_trust") >= T_THIENAN_QUANG_TRUST
            and score("thienan_self_assertion") >= T_THIENAN_SELF_ASSERTION
            and thienan_is_free_from_family_arrangement()
            and ending_has_support("e06_thienan_quang")
        )


    def can_get_thienan_minh():
        return (
            story_state.get("minh_yuuka_relation") == "old_close_friends"
            and not story_state.get("minh_romance_lock", False)
            and minyuu_shared_arc_ok()
            and score("thienan_minh_residue") >= T_THIENAN_MINH_RESIDUE
            and score("thienan_self_assertion") >= T_THIENAN_SELF_ASSERTION
            and thienan_is_free_from_family_arrangement()
            and ending_has_direction("thienan", "thienan_minh_commit")
            and ending_has_support("e07_thienan_minh")
        )


    def can_get_thienan_single():
        return (
            score("thienan_self_assertion") >= T_THIENAN_SELF_ASSERTION
            and thienan_is_free_from_family_arrangement()
            and ending_has_support("e08_thienan_single")
        )


    def can_get_thienan_arranged():
        return (
            thienan_family_pressure_overrides_self()
            and ending_has_support("e09_thienan_arranged")
        )


    # ----------------------------
    # Solo / support endings
    # ----------------------------
    def can_get_minh_single():
        return (
            story_state.get("minh_yuuka_relation") in ["old_close_friends", "ex_lovers_long_separated"]
            and ending_has_support("e16_minh_single")
        )


    def can_get_yuuka_single():
        return (
            story_state.get("minh_yuuka_relation") in ["old_close_friends", "ex_lovers_long_separated"]
            and ending_has_support("e17_yuuka_single")
        )


    def can_get_yuuka_career():
        return (
            minyuu_shared_arc_ok()
            and ending_has_support("e19_yuuka_career")
        )


    def can_get_minyuu_friendship():
        return (
            story_state.get("minh_yuuka_relation") == "old_close_friends"
            and minyuu_shared_arc_ok()
            and ending_has_support("e20_minyuu_friendship")
        )


    def can_get_tam_independent():
        return (
            score("tam_self_clarity") >= T_TAM_CLARITY_NORMAL
            and score("career_tam") >= T_CAREER_TAM_NORMAL
            and ending_has_support("e21_tam_independent")
        )


    def can_get_huyen_independent():
        return (
            score("career_huyen") >= T_CAREER_HUYEN
            and ending_has_support("e22_huyen_independent")
        )


    def can_get_hoang_single_growth():
        return (
            score("hoang_self_acceptance") >= T_HOANG_SELF_ACCEPTANCE
            and score("hoang_professional_credit") >= T_HOANG_PROFESSIONAL_CREDIT
            and ending_has_support("e23_hoang_single_growth")
        )


    def can_get_quan_support():
        return ending_has_marker(
            "e25_quan_support",
            "e_quan_support",
            "quan_support",
            "ach_end_quan_support"
        )


    def can_get_quang_support():
        return ending_has_marker(
            "e26_quang_support",
            "e_quang_support",
            "quang_support",
            "ach_end_quang_support"
        )


    # ----------------------------
    # Family crisis outcome resolver
    # ----------------------------
    def resolve_family_crisis_flags(final_ending_id=None):
        """
        Returns crisis achievement/world-state flags.

        Important:
        Achievement definitions use crisis_* flags directly:
            crisis_best_outcome
            crisis_good_outcome
            crisis_partial_legal_clear
            crisis_partial_business_saved
            crisis_bad_default

        Do NOT use ach_crisis_* unless you also add those to achievements.rpy.
        """
        if ending_has_marker("crisis_best_outcome"):
            return ["crisis_best_outcome"]

        if ending_has_marker("crisis_good_outcome"):
            return ["crisis_good_outcome"]

        if ending_has_marker("crisis_partial_legal_clear"):
            return ["crisis_partial_legal_clear"]

        if ending_has_marker("crisis_partial_business_saved"):
            return ["crisis_partial_business_saved"]

        if ending_has_marker("crisis_bad_default"):
            return ["crisis_bad_default"]

        # Sensible defaults by ending type.
        if final_ending_id == "e01_canon_true":
            return ["crisis_good_outcome"]

        if final_ending_id == "e09_thienan_arranged":
            return ["crisis_partial_business_saved"]

        return []


    # ----------------------------
    # Minh-Yuuka branch resolvers
    # ----------------------------
    def resolve_ex_lovers_ending():
        if not minyuu_shared_arc_ok():
            return "e24_doom"

        if ending_has_support("e10_minyuu_reunion"):
            return "e10_minyuu_reunion"

        if ending_has_support("e11_minyuu_late_reunion"):
            return "e11_minyuu_late_reunion"

        if ending_has_support("e18_minyuu_mutual_single"):
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

        if ending_has_support("e13_minyuu_public_lovers"):
            return "e13_minyuu_public_lovers"

        if ending_has_support("e14_minyuu_non_marriage"):
            return "e14_minyuu_non_marriage"

        if ending_has_support("e15_minyuu_long_distance"):
            return "e15_minyuu_long_distance"

        return "e12_minyuu_private_lovers"


    def resolve_minyuu_axis_ending(final_ending_id=None):
        """
        Resolves the MinYuu axis independently from the headline ending.

        Example:
        Headline ending may be e02_tam_hoang, but the MinYuu axis may still be
        e20_minyuu_friendship or e10_minyuu_reunion.
        """
        if final_ending_id in [
            "e10_minyuu_reunion",
            "e11_minyuu_late_reunion",
            "e12_minyuu_private_lovers",
            "e13_minyuu_public_lovers",
            "e14_minyuu_non_marriage",
            "e15_minyuu_long_distance",
            "e16_minh_single",
            "e17_yuuka_single",
            "e18_minyuu_mutual_single",
            "e19_yuuka_career",
            "e20_minyuu_friendship",
        ]:
            return final_ending_id

        if final_ending_id == "e01_canon_true":
            return "e10_minyuu_reunion"

        relation = story_state.get("minh_yuuka_relation", "unknown")

        if relation == "still_lovers":
            return resolve_still_lovers_ending()

        if relation == "ex_lovers_long_separated":
            return resolve_ex_lovers_ending()

        if relation == "old_close_friends":
            if can_get_minyuu_friendship():
                return "e20_minyuu_friendship"
            if can_get_minh_single():
                return "e16_minh_single"
            if can_get_yuuka_single():
                return "e17_yuuka_single"

        return None


    # ----------------------------
    # Headline ending resolver
    # ----------------------------
    def resolve_story_ending():
        """
        Pure resolver.
        Returns a headline ending id.
        Does NOT unlock achievements.
        """
        relation = story_state.get("minh_yuuka_relation", "unknown")

        if score("doom_score") >= T_DOOM_HARD or ending_has_support("e24_doom"):
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


    # ----------------------------
    # Achievement / world-state flag builder
    # ----------------------------
    def _ending_add_flag(flags, flag_name):
        if flag_name and flag_name not in flags:
            flags.append(flag_name)


    def _ending_add_flags(flags, flag_names):
        for f in flag_names or []:
            _ending_add_flag(flags, f)


    def add_minyuu_achievement_flags(flags, minyuu_ending_id):
        if minyuu_ending_id == "e10_minyuu_reunion":
            _ending_add_flags(flags, [
                "ach_end_minh_minyuu_reunion",
                "ach_end_yuuka_reunion",
                "ach_pair_minyuu",
            ])

        elif minyuu_ending_id == "e11_minyuu_late_reunion":
            _ending_add_flags(flags, [
                "ach_end_minh_late_reunion",
                "ach_end_yuuka_reunion",
                "ach_pair_minyuu",
            ])

        elif minyuu_ending_id == "e12_minyuu_private_lovers":
            _ending_add_flags(flags, [
                "ach_end_minh_private_lovers",
                "ach_end_yuuka_reunion",
                "ach_pair_minyuu",
            ])

        elif minyuu_ending_id == "e13_minyuu_public_lovers":
            _ending_add_flags(flags, [
                "ach_end_minh_public_lovers",
                "ach_end_yuuka_reunion",
                "ach_pair_minyuu",
            ])

        elif minyuu_ending_id == "e14_minyuu_non_marriage":
            _ending_add_flags(flags, [
                "ach_end_yuuka_non_marriage",
                "ach_pair_minyuu",
            ])

        elif minyuu_ending_id == "e15_minyuu_long_distance":
            _ending_add_flags(flags, [
                "ach_end_minh_long_distance",
                "ach_pair_minyuu",
            ])

        elif minyuu_ending_id == "e16_minh_single":
            _ending_add_flags(flags, [
                "ach_end_minh_single",
            ])

        elif minyuu_ending_id == "e17_yuuka_single":
            _ending_add_flags(flags, [
                "ach_end_yuuka_single",
            ])

        elif minyuu_ending_id == "e18_minyuu_mutual_single":
            _ending_add_flags(flags, [
                "ach_end_yuuka_mutual_single",
            ])

        elif minyuu_ending_id == "e19_yuuka_career":
            _ending_add_flags(flags, [
                "ach_end_yuuka_career",
            ])

        elif minyuu_ending_id == "e20_minyuu_friendship":
            _ending_add_flags(flags, [
                "ach_end_minh_friendship",
            ])


    def build_ending_achievement_flags(final_ending_id):
        """
        Builds final world-state achievement flags.

        This function intentionally creates a bundle:
        - headline ending flag
        - MinYuu axis
        - Tâm / Hoàng / Huyền / Quân axis
        - Thiên An / Quang axis
        - family crisis axis
        - final tier flags

        It does NOT write anything by itself.
        """
        flags = []

        _ending_add_flag(flags, "final:" + str(final_ending_id))

        # Doom is terminal. Keep it clean.
        if final_ending_id == "e24_doom":
            _ending_add_flag(flags, "ach_tier_doom")
            return flags

        # ----------------------------
        # MinYuu axis
        # ----------------------------
        minyuu_axis = resolve_minyuu_axis_ending(final_ending_id)
        add_minyuu_achievement_flags(flags, minyuu_axis)

        # Canon true implies the intended main relationship bundle even if the
        # side-route ending_support flags are not individually present.
        canon_bundle = final_ending_id == "e01_canon_true"

        # ----------------------------
        # Tâm / Hoàng / Huyền / Quân axis
        # ----------------------------
        tam_with_hoang = False
        hoang_with_huyen = False
        huyen_with_quan = False

        if canon_bundle or final_ending_id == "e02_tam_hoang" or can_get_tam_hoang():
            tam_with_hoang = True
            _ending_add_flags(flags, [
                "ach_end_tam_hoang",
                "ach_end_hoang_tam",
                "ach_pair_tam_hoang",
            ])

        elif final_ending_id == "e03_tam_minh" or can_get_tam_minh():
            _ending_add_flags(flags, [
                "ach_end_tam_minh",
                "ach_pair_tam_minh",
            ])

        elif final_ending_id == "e21_tam_independent" or can_get_tam_independent():
            _ending_add_flag(flags, "ach_end_tam_independent")

        elif ending_has_marker("ach_end_tam_unresolved", "e_tam_unresolved", "tam_unresolved"):
            _ending_add_flag(flags, "ach_end_tam_unresolved")


        if not tam_with_hoang and (final_ending_id == "e04_hoang_huyen" or can_get_hoang_huyen()):
            hoang_with_huyen = True
            _ending_add_flags(flags, [
                "ach_end_hoang_huyen",
                "ach_end_huyen_hoang",
                "ach_pair_hoang_huyen",
            ])

        elif not tam_with_hoang and (final_ending_id == "e23_hoang_single_growth" or can_get_hoang_single_growth()):
            _ending_add_flag(flags, "ach_end_hoang_single_growth")


        if not hoang_with_huyen and (canon_bundle or final_ending_id == "e05_huyen_quan" or can_get_huyen_quan()):
            huyen_with_quan = True
            _ending_add_flags(flags, [
                "ach_end_huyen_quan",
                "ach_end_quan_huyen",
                "ach_pair_huyen_quan",
            ])

        elif not hoang_with_huyen and (final_ending_id == "e22_huyen_independent" or can_get_huyen_independent()):
            _ending_add_flag(flags, "ach_end_huyen_independent")


        if not huyen_with_quan and can_get_quan_support():
            _ending_add_flag(flags, "ach_end_quan_support")


        # ----------------------------
        # Thiên An / Quang axis
        # ----------------------------
        thienan_with_quang = False

        if final_ending_id == "e09_thienan_arranged" or can_get_thienan_arranged():
            _ending_add_flag(flags, "ach_end_thienan_arranged")

            if can_get_quang_support():
                _ending_add_flag(flags, "ach_end_quang_support")

        elif canon_bundle or final_ending_id == "e06_thienan_quang" or can_get_thienan_quang():
            thienan_with_quang = True
            _ending_add_flags(flags, [
                "ach_end_thienan_quang",
                "ach_end_quang_thienan",
                "ach_pair_thienan_quang",
            ])

        elif final_ending_id == "e07_thienan_minh" or can_get_thienan_minh():
            _ending_add_flags(flags, [
                "ach_end_thienan_minh",
                "ach_pair_thienan_minh",
            ])

            if can_get_quang_support():
                _ending_add_flag(flags, "ach_end_quang_support")

        elif final_ending_id == "e08_thienan_single" or can_get_thienan_single():
            _ending_add_flag(flags, "ach_end_thienan_single")

            if can_get_quang_support():
                _ending_add_flag(flags, "ach_end_quang_support")

        elif can_get_quang_support():
            _ending_add_flag(flags, "ach_end_quang_support")


        # ----------------------------
        # Family crisis axis
        # ----------------------------
        crisis_flags = resolve_family_crisis_flags(final_ending_id)
        _ending_add_flags(flags, crisis_flags)

        crisis_best = "crisis_best_outcome" in flags
        crisis_good = "crisis_good_outcome" in flags
        crisis_partial = (
            "crisis_partial_legal_clear" in flags
            or "crisis_partial_business_saved" in flags
        )
        crisis_bad = "crisis_bad_default" in flags

        # ----------------------------
        # Final world-state tier
        # ----------------------------
        if final_ending_id == "e01_canon_true":
            _ending_add_flag(flags, "ach_tier_true")

        if final_ending_id == "e09_thienan_arranged":
            _ending_add_flag(flags, "ach_tier_sacrifice")

        if crisis_partial or final_ending_id in [
            "e11_minyuu_late_reunion",
            "e15_minyuu_long_distance",
            "e16_minh_single",
            "e17_yuuka_single",
            "e18_minyuu_mutual_single",
            "e08_thienan_single",
            "e21_tam_independent",
            "e22_huyen_independent",
            "e23_hoang_single_growth",
        ]:
            _ending_add_flag(flags, "ach_tier_bittersweet")

        if crisis_bad:
            _ending_add_flag(flags, "ach_tier_default")

        # Explicit override markers for future use.
        if ending_has_marker("ach_tier_default", "tier_default", "e_tier_default"):
            _ending_add_flag(flags, "ach_tier_default")

        if ending_has_marker("ach_tier_bittersweet", "tier_bittersweet", "e_tier_bittersweet"):
            _ending_add_flag(flags, "ach_tier_bittersweet")

        if ending_has_marker("ach_tier_sacrifice", "tier_sacrifice", "e_tier_sacrifice"):
            _ending_add_flag(flags, "ach_tier_sacrifice")

        if ending_has_marker("ach_tier_true", "tier_true", "e_tier_true"):
            _ending_add_flag(flags, "ach_tier_true")

        # Perfect ending:
        # cleanest possible world-state, not merely canon.
        if (
            ending_has_marker("ach_tier_perfect", "tier_perfect", "e_tier_perfect")
            or (
                "ach_tier_true" in flags
                and crisis_best
                and "ach_pair_minyuu" in flags
                and "ach_pair_tam_hoang" in flags
                and "ach_pair_huyen_quan" in flags
                and "ach_pair_thienan_quang" in flags
            )
        ):
            _ending_add_flag(flags, "ach_tier_perfect")
            _ending_add_flag(flags, "ach_tier_no_one_left_behind")

        # No One Left Behind:
        # stable ending for every major axis.
        elif (
            ending_has_marker("ach_tier_no_one_left_behind", "tier_no_one_left_behind")
            or (
                "ach_pair_minyuu" in flags
                and (
                    "ach_pair_tam_hoang" in flags
                    or "ach_end_tam_independent" in flags
                )
                and (
                    "ach_pair_huyen_quan" in flags
                    or "ach_pair_hoang_huyen" in flags
                    or "ach_end_huyen_independent" in flags
                )
                and (
                    "ach_pair_thienan_quang" in flags
                    or "ach_end_thienan_single" in flags
                )
                and not crisis_bad
            )
        ):
            _ending_add_flag(flags, "ach_tier_no_one_left_behind")

        if ending_has_marker("ach_tier_everyone_moves_on", "tier_everyone_moves_on"):
            _ending_add_flag(flags, "ach_tier_everyone_moves_on")

        return flags


    def record_ending_achievement_flags(final_ending_id):
        """
        Writes final world-state flags and triggers achievements.

        Requires achievements.rpy if available.
        Falls back to appending flags to story_flags if achievement system is not loaded.
        """
        flags = build_ending_achievement_flags(final_ending_id)

        recorder = globals().get("achievement_record_world_state", None)
        if callable(recorder):
            recorder(flags, check=True)
            return flags

        # Fallback: write flags directly into story_flags.
        try:
            for f in flags:
                if f not in story_flags:
                    story_flags.append(f)
        except Exception:
            pass

        checker = globals().get("achievement_check_all", None)
        if callable(checker):
            try:
                checker("finalize_story_ending", notify=True)
            except Exception:
                pass

        return flags


    def finalize_story_ending():
        """
        Final resolver for actual ending playback.

        Use this at the final decision point instead of resolve_story_ending()
        when you want achievements to unlock.
        """
        final_ending_id = resolve_story_ending()
        record_ending_achievement_flags(final_ending_id)
        return final_ending_id