# FILE: game/achievements.rpy
# Achievement system for Like Wind, Like Cloud / Tựa Gió, Tựa Mây
#
# Design:
# - Achievements unlock by flags.
# - Runtime flags come from story_flags, progress["player_flags"], completed chapters,
#   relationship directions, and safe virtual flags.
# - Meta achievements use persistent history across playthroughs.
# - Ending achievements should be triggered by explicit final/world-state flags,
#   not by score thresholds directly.

default achievement_recent_unlocks = []

init -20 python:
    ACHIEVEMENT_SYSTEM_VERSION = 1

    # -------------------------------------------------------------------------
    # Helpers for defining achievements
    # -------------------------------------------------------------------------

    def ach(
        title,
        description,
        category="story",
        required_flags=None,
        required_any_groups=None,
        forbidden_flags=None,
        scope="run",
        hidden=False,
        points=10,
        order=1000
    ):
        """
        scope:
            "run"     = all required flags must exist in the current playthrough.
            "history" = all required flags must have been seen across all playthroughs.

        required_any_groups:
            [
                ["flag_a", "flag_b"],  # at least one flag in this group is required
                ["flag_c", "flag_d"],  # at least one flag in this group is required
            ]
        """
        return {
            "title": title,
            "description": description,
            "category": category,
            "required_flags": required_flags or [],
            "required_any_groups": required_any_groups or [],
            "forbidden_flags": forbidden_flags or [],
            "scope": scope,
            "hidden": hidden,
            "points": points,
            "order": order,
        }


    ACHIEVEMENT_CATEGORIES = {
        "story": "Story",
        "relationship": "Relationships",
        "ending": "Character Endings",
        "minyuu": "Minh / Yuuka",
        "family": "Family Crisis",
        "tier": "Final World-State",
        "meta": "Completion",
        "secret": "Secrets",
    }


    # -------------------------------------------------------------------------
    # Achievement definitions
    # -------------------------------------------------------------------------
    #
    # Naming convention for flags:
    #
    # Story milestones:
    #   ach_story_<event>
    #
    # Character ending modules:
    #   ach_end_<character>_<outcome>
    #
    # Couple / pair outcomes:
    #   ach_pair_<a>_<b>
    #
    # Crisis outcomes:
    #   ach_crisis_<outcome>
    #
    # Final world-state tiers:
    #   ach_tier_<tier>
    #
    # Meta achievements:
    #   use scope="history"
    #
    # Note:
    # Use explicit achievement flags in final labels / world-state resolver.
    # Do not rely only on ending_support, because ending_support is a nudge,
    # not always the resolved final truth.

    ACHIEVEMENTS = {

        # ---------------------------------------------------------------------
        # Story / early milestones
        # ---------------------------------------------------------------------

        "story_rain_dream": ach(
            "Rain Dream",
            "Saw the dream that begins the story.",
            "story",
            required_flags=["rain_dream_seen"],
            points=5,
            order=10
        ),

        "story_first_steps": ach(
            "First Steps",
            "Completed the opening interview-day arc.",
            "story",
            required_flags=["tam_interview_passed", "huyen_interview_passed"],
            points=10,
            order=20
        ),

        "story_first_offer": ach(
            "First Offer",
            "Tâm and Huyền received their first job offer milestone together.",
            "story",
            required_flags=["tam_huyen_first_job_offer"],
            points=10,
            order=30
        ),

        "story_huyen_bond": ach(
            "Girls Before Chaos",
            "Built a strong early bond between Tâm and Huyền.",
            "story",
            required_flags=["tam_huyen_strong_bond"],
            points=10,
            order=40
        ),

        "story_thienan_private_talk": ach(
            "A Question Asked Twice",
            "Tâm reached the private sister talk with Thiên An.",
            "story",
            required_flags=["tam_private_talk_with_thienan"],
            points=10,
            order=50
        ),

        "story_noticed_minyuu": ach(
            "A Pause Too Small",
            "Tâm noticed the quiet pause between Minh and Yuuka.",
            "story",
            required_flags=["noticed_minyuu_pause"],
            points=10,
            order=60
        ),


        # ---------------------------------------------------------------------
        # Relationship direction achievements
        # ---------------------------------------------------------------------

        "rel_tam_hoang_open": ach(
            "A Door Left Open",
            "Tâm became emotionally open to Hoàng.",
            "relationship",
            required_flags=["direction_tam_tam_hoang_open"],
            points=10,
            order=100
        ),

        "rel_tam_hoang_commit": ach(
            "Chosen Clearly",
            "Tâm committed to the Hoàng path.",
            "relationship",
            required_flags=["direction_tam_tam_hoang_commit"],
            points=15,
            order=110
        ),

        "rel_tam_minh_commit": ach(
            "Facing the Shadow",
            "Tâm committed to the Minh path.",
            "relationship",
            required_flags=["direction_tam_tam_minh_commit"],
            points=15,
            order=120
        ),

        "rel_hoang_huyen_open": ach(
            "A Different Warmth",
            "Hoàng opened emotionally toward Huyền.",
            "relationship",
            required_flags=["direction_hoang_hoang_huyen_open"],
            points=10,
            order=130
        ),

        "rel_huyen_hoang_commit": ach(
            "Not a Spare Wheel",
            "Huyền committed to the Hoàng path by her own arc.",
            "relationship",
            required_flags=["direction_huyen_huyen_hoang_commit"],
            points=15,
            order=140
        ),

        "rel_huyen_quan_commit": ach(
            "Quiet Trust",
            "Huyền committed to the Quân path.",
            "relationship",
            required_flags=["direction_huyen_huyen_quan_commit"],
            points=15,
            order=150
        ),

        "rel_thienan_minh_commit": ach(
            "Old Residue",
            "Thiên An committed to the Minh path.",
            "relationship",
            required_flags=["direction_thienan_thienan_minh_commit"],
            points=15,
            order=160
        ),

        "rel_thienan_quang_commit": ach(
            "Learning to Receive",
            "Thiên An committed to the Quang path.",
            "relationship",
            required_flags=["direction_thienan_thienan_quang_commit"],
            points=15,
            order=170
        ),


        # ---------------------------------------------------------------------
        # Tâm ending modules: 4
        # ---------------------------------------------------------------------

        "end_tam_hoang": ach(
            "Tâm — Chosen Clearly",
            "Tâm chooses Hoàng after understanding her own heart.",
            "ending",
            required_flags=["ach_end_tam_hoang"],
            points=20,
            order=200
        ),

        "end_tam_minh": ach(
            "Tâm — Old Shadow, New Choice",
            "Tâm reaches the Minh ending path.",
            "ending",
            required_flags=["ach_end_tam_minh"],
            points=20,
            order=210
        ),

        "end_tam_independent": ach(
            "Tâm — Her Own Center",
            "Tâm chooses independence instead of forcing romance.",
            "ending",
            required_flags=["ach_end_tam_independent"],
            points=20,
            order=220
        ),

        "end_tam_unresolved": ach(
            "Tâm — Half-Closed Door",
            "Tâm reaches an unresolved emotional outcome.",
            "ending",
            required_flags=["ach_end_tam_unresolved"],
            hidden=True,
            points=20,
            order=230
        ),


        # ---------------------------------------------------------------------
        # Huyền ending modules: 3
        # ---------------------------------------------------------------------

        "end_huyen_quan": ach(
            "Huyền — Quiet Trust",
            "Huyền and Quân reach a stable ending.",
            "ending",
            required_flags=["ach_end_huyen_quan"],
            points=20,
            order=300
        ),

        "end_huyen_hoang": ach(
            "Huyền — A Different Warmth",
            "Huyền and Hoàng reach their relationship ending.",
            "ending",
            required_flags=["ach_end_huyen_hoang"],
            points=20,
            order=310
        ),

        "end_huyen_independent": ach(
            "Huyền — Not Waiting Around",
            "Huyền reaches her independent ending.",
            "ending",
            required_flags=["ach_end_huyen_independent"],
            points=20,
            order=320
        ),


        # ---------------------------------------------------------------------
        # Hoàng ending modules: 3
        # ---------------------------------------------------------------------

        "end_hoang_tam": ach(
            "Hoàng — Chosen Back",
            "Hoàng and Tâm reach their relationship ending.",
            "ending",
            required_flags=["ach_end_hoang_tam"],
            points=20,
            order=400
        ),

        "end_hoang_huyen": ach(
            "Hoàng — New Rhythm",
            "Hoàng and Huyền reach their relationship ending.",
            "ending",
            required_flags=["ach_end_hoang_huyen"],
            points=20,
            order=410
        ),

        "end_hoang_single_growth": ach(
            "Hoàng — Standing Steadier",
            "Hoàng grows without needing romance to complete him.",
            "ending",
            required_flags=["ach_end_hoang_single_growth"],
            points=20,
            order=420
        ),


        # ---------------------------------------------------------------------
        # Minh ending modules: 7
        # ---------------------------------------------------------------------

        "end_minh_minyuu_reunion": ach(
            "Minh — The Door Opens Again",
            "Minh and Yuuka reunite after long separation.",
            "minyuu",
            required_flags=["ach_end_minh_minyuu_reunion"],
            points=25,
            order=500
        ),

        "end_minh_late_reunion": ach(
            "Minh — Late, Not Lost",
            "Minh reaches the late reunion outcome.",
            "minyuu",
            required_flags=["ach_end_minh_late_reunion"],
            points=25,
            order=510
        ),

        "end_minh_private_lovers": ach(
            "Minh — Private Lovers",
            "Minh and Yuuka choose a private form of love.",
            "minyuu",
            required_flags=["ach_end_minh_private_lovers"],
            points=25,
            order=520
        ),

        "end_minh_public_lovers": ach(
            "Minh — In the Frame",
            "Minh and Yuuka choose a public relationship.",
            "minyuu",
            required_flags=["ach_end_minh_public_lovers"],
            points=25,
            order=530
        ),

        "end_minh_long_distance": ach(
            "Minh — Across the Distance",
            "Minh and Yuuka remain together across distance.",
            "minyuu",
            required_flags=["ach_end_minh_long_distance"],
            points=25,
            order=540
        ),

        "end_minh_single": ach(
            "Minh — The Quiet Room",
            "Minh reaches his single ending.",
            "minyuu",
            required_flags=["ach_end_minh_single"],
            points=25,
            order=550
        ),

        "end_minh_friendship": ach(
            "Minh — What Remains",
            "Minh and Yuuka preserve the old-friends outcome.",
            "minyuu",
            required_flags=["ach_end_minh_friendship"],
            points=25,
            order=560
        ),


        # ---------------------------------------------------------------------
        # Yuuka ending modules: 5
        # ---------------------------------------------------------------------

        "end_yuuka_reunion": ach(
            "Yuuka — Back to the House",
            "Yuuka reaches the reunion outcome with Minh.",
            "minyuu",
            required_flags=["ach_end_yuuka_reunion"],
            points=25,
            order=600
        ),

        "end_yuuka_single": ach(
            "Yuuka — Alone, Not Empty",
            "Yuuka reaches her single ending.",
            "minyuu",
            required_flags=["ach_end_yuuka_single"],
            points=25,
            order=610
        ),

        "end_yuuka_career": ach(
            "Yuuka — Her Own Film",
            "Yuuka reaches her career-focused ending.",
            "minyuu",
            required_flags=["ach_end_yuuka_career"],
            points=25,
            order=620
        ),

        "end_yuuka_mutual_single": ach(
            "Yuuka — Two Separate Skies",
            "Yuuka and Minh mutually let each other go.",
            "minyuu",
            required_flags=["ach_end_yuuka_mutual_single"],
            points=25,
            order=630
        ),

        "end_yuuka_non_marriage": ach(
            "Yuuka — No Ring, Still Home",
            "Yuuka and Minh choose love without marriage.",
            "minyuu",
            required_flags=["ach_end_yuuka_non_marriage"],
            points=25,
            order=640
        ),


        # ---------------------------------------------------------------------
        # Thiên An ending modules: 4
        # ---------------------------------------------------------------------

        "end_thienan_quang": ach(
            "Thiên An — Accepted Help",
            "Thiên An and Quang reach their relationship ending.",
            "ending",
            required_flags=["ach_end_thienan_quang"],
            points=20,
            order=700
        ),

        "end_thienan_minh": ach(
            "Thiên An — The Old Flame",
            "Thiên An reaches the Minh ending path.",
            "ending",
            required_flags=["ach_end_thienan_minh"],
            points=20,
            order=710
        ),

        "end_thienan_single": ach(
            "Thiên An — Her Own Name",
            "Thiên An chooses herself.",
            "ending",
            required_flags=["ach_end_thienan_single"],
            points=20,
            order=720
        ),

        "end_thienan_arranged": ach(
            "Thiên An — The Price of Family",
            "Thiên An accepts an arranged marriage to protect her family.",
            "ending",
            required_flags=["ach_end_thienan_arranged"],
            points=20,
            order=730
        ),


        # ---------------------------------------------------------------------
        # Quân ending modules: 2
        # ---------------------------------------------------------------------

        "end_quan_huyen": ach(
            "Quân — Finally Chosen",
            "Quân reaches the Huyền ending path.",
            "ending",
            required_flags=["ach_end_quan_huyen"],
            points=20,
            order=800
        ),

        "end_quan_support": ach(
            "Quân — A Decent Distance",
            "Quân remains a supportive presence without romance.",
            "ending",
            required_flags=["ach_end_quan_support"],
            points=20,
            order=810
        ),


        # ---------------------------------------------------------------------
        # Quang ending modules: 2
        # ---------------------------------------------------------------------

        "end_quang_thienan": ach(
            "Quang — No Longer Hiding",
            "Quang reaches the Thiên An ending path.",
            "ending",
            required_flags=["ach_end_quang_thienan"],
            points=20,
            order=900
        ),

        "end_quang_support": ach(
            "Quang — Help Without Claiming",
            "Quang helps without turning care into ownership.",
            "ending",
            required_flags=["ach_end_quang_support"],
            points=20,
            order=910
        ),


        # ---------------------------------------------------------------------
        # Pair / couple achievements
        # ---------------------------------------------------------------------

        "pair_tam_hoang": ach(
            "Tâm × Hoàng — Warm Enough",
            "Tâm and Hoàng end together.",
            "relationship",
            required_flags=["ach_pair_tam_hoang"],
            points=25,
            order=1000
        ),

        "pair_tam_minh": ach(
            "Tâm × Minh — Against the Usual Weather",
            "Tâm and Minh end together.",
            "relationship",
            required_flags=["ach_pair_tam_minh"],
            hidden=True,
            points=25,
            order=1010
        ),

        "pair_hoang_huyen": ach(
            "Hoàng × Huyền — A New Route",
            "Hoàng and Huyền end together.",
            "relationship",
            required_flags=["ach_pair_hoang_huyen"],
            points=25,
            order=1020
        ),

        "pair_huyen_quan": ach(
            "Huyền × Quân — Quiet Trust",
            "Huyền and Quân end together.",
            "relationship",
            required_flags=["ach_pair_huyen_quan"],
            points=25,
            order=1030
        ),

        "pair_thienan_quang": ach(
            "Thiên An × Quang — Let Me Help",
            "Thiên An and Quang end together.",
            "relationship",
            required_flags=["ach_pair_thienan_quang"],
            points=25,
            order=1040
        ),

        "pair_thienan_minh": ach(
            "Thiên An × Minh — What Was Left There",
            "Thiên An and Minh end together.",
            "relationship",
            required_flags=["ach_pair_thienan_minh"],
            hidden=True,
            points=25,
            order=1050
        ),

        "pair_minyuu": ach(
            "Minh × Yuuka — Tựa Gió, Tựa Mây",
            "Minh and Yuuka end together.",
            "minyuu",
            required_flags=["ach_pair_minyuu"],
            points=30,
            order=1060
        ),


        # ---------------------------------------------------------------------
        # Family crisis achievements
        # ---------------------------------------------------------------------

        "crisis_started": ach(
            "Cracks in the Family Business",
            "The family business crisis began.",
            "family",
            required_flags=["family_business_crisis_started"],
            points=10,
            order=1100
        ),

        "crisis_scandal": ach(
            "A Trap With Paperwork",
            "The family business scandal was triggered.",
            "family",
            required_flags=["family_business_scandal_triggered"],
            points=10,
            order=1110
        ),

        "crisis_father_hospitalized": ach(
            "The Hallway Outside",
            "Tâm and Thiên An's father was hospitalized.",
            "family",
            required_flags=["family_father_hospitalized"],
            points=10,
            order=1120
        ),

        "crisis_minh_adviser": ach(
            "The Adviser",
            "Minh helped read the structure of the trap.",
            "family",
            required_flags=["crisis_minh_adviser"],
            points=15,
            order=1130
        ),

        "crisis_quang_financial_support": ach(
            "The Hand He Hid",
            "Quang used his family resources to support the crisis.",
            "family",
            required_flags=["crisis_quang_financial_support"],
            points=15,
            order=1140
        ),

        "crisis_hoang_legal_support": ach(
            "No Special Treatment",
            "Hoàng helped seek fair legal review.",
            "family",
            required_flags=["crisis_hoang_legal_support"],
            points=15,
            order=1150
        ),

        "crisis_best_outcome": ach(
            "Prevented the Scandal",
            "The crisis was handled before it could fully destroy the family.",
            "family",
            required_flags=["crisis_best_outcome"],
            points=30,
            order=1160
        ),

        "crisis_good_outcome": ach(
            "Scars, Not Ruins",
            "The family survived the crisis, but not without cost.",
            "family",
            required_flags=["crisis_good_outcome"],
            points=25,
            order=1170
        ),

        "crisis_partial_legal_clear": ach(
            "Cleared Her Name",
            "Thiên An avoided legal ruin, even if the business suffered.",
            "family",
            required_flags=["crisis_partial_legal_clear"],
            points=20,
            order=1180
        ),

        "crisis_partial_business_saved": ach(
            "Saved What Could Be Saved",
            "The business survived, but the damage remained.",
            "family",
            required_flags=["crisis_partial_business_saved"],
            points=20,
            order=1190
        ),

        "crisis_bad_default": ach(
            "Too Late to Stop It",
            "The family crisis reached the bad default outcome.",
            "family",
            required_flags=["crisis_bad_default"],
            hidden=True,
            points=20,
            order=1200
        ),


        # ---------------------------------------------------------------------
        # Final world-state tier achievements
        # ---------------------------------------------------------------------

        "tier_true": ach(
            "True Ending",
            "Reached the emotionally true final world-state.",
            "tier",
            required_flags=["ach_tier_true"],
            points=50,
            order=1300
        ),

        "tier_perfect": ach(
            "Perfect Ending",
            "Reached the cleanest possible final world-state.",
            "tier",
            required_flags=["ach_tier_perfect"],
            points=75,
            order=1310
        ),

        "tier_default": ach(
            "Default Ending",
            "Reached the default final world-state.",
            "tier",
            required_flags=["ach_tier_default"],
            points=25,
            order=1320
        ),

        "tier_bittersweet": ach(
            "Bittersweet Ending",
            "Reached a final world-state where people survive, but not everything returns.",
            "tier",
            required_flags=["ach_tier_bittersweet"],
            points=35,
            order=1330
        ),

        "tier_sacrifice": ach(
            "Sacrifice Ending",
            "Reached a final world-state built on sacrifice.",
            "tier",
            required_flags=["ach_tier_sacrifice"],
            points=35,
            order=1340
        ),

        "tier_doom": ach(
            "Doom Ending",
            "Reached the collapse route.",
            "tier",
            required_flags=["ach_tier_doom"],
            hidden=True,
            points=25,
            order=1350
        ),

        "tier_no_one_left_behind": ach(
            "No One Left Behind",
            "Reached a world-state where every major character found a stable place.",
            "tier",
            required_flags=["ach_tier_no_one_left_behind"],
            points=50,
            order=1360
        ),

        "tier_everyone_moves_on": ach(
            "Everyone Moves On",
            "Reached a world-state where no romance is forced and everyone continues forward.",
            "tier",
            required_flags=["ach_tier_everyone_moves_on"],
            points=50,
            order=1370
        ),


        # ---------------------------------------------------------------------
        # Meta / completion achievements
        # These use persistent achievement flag history across playthroughs.
        # ---------------------------------------------------------------------

        "meta_all_tam_endings": ach(
            "Tâm Archive Complete",
            "Unlocked all Tâm ending modules.",
            "meta",
            required_flags=[
                "ach_end_tam_hoang",
                "ach_end_tam_minh",
                "ach_end_tam_independent",
                "ach_end_tam_unresolved",
            ],
            scope="history",
            points=50,
            order=2000
        ),

        "meta_all_huyen_endings": ach(
            "Huyền Archive Complete",
            "Unlocked all Huyền ending modules.",
            "meta",
            required_flags=[
                "ach_end_huyen_quan",
                "ach_end_huyen_hoang",
                "ach_end_huyen_independent",
            ],
            scope="history",
            points=50,
            order=2010
        ),

        "meta_all_hoang_endings": ach(
            "Hoàng Archive Complete",
            "Unlocked all Hoàng ending modules.",
            "meta",
            required_flags=[
                "ach_end_hoang_tam",
                "ach_end_hoang_huyen",
                "ach_end_hoang_single_growth",
            ],
            scope="history",
            points=50,
            order=2020
        ),

        "meta_all_minh_endings": ach(
            "Minh Archive Complete",
            "Unlocked all Minh ending modules.",
            "meta",
            required_flags=[
                "ach_end_minh_minyuu_reunion",
                "ach_end_minh_late_reunion",
                "ach_end_minh_private_lovers",
                "ach_end_minh_public_lovers",
                "ach_end_minh_long_distance",
                "ach_end_minh_single",
                "ach_end_minh_friendship",
            ],
            scope="history",
            points=75,
            order=2030
        ),

        "meta_all_yuuka_endings": ach(
            "Yuuka Archive Complete",
            "Unlocked all Yuuka ending modules.",
            "meta",
            required_flags=[
                "ach_end_yuuka_reunion",
                "ach_end_yuuka_single",
                "ach_end_yuuka_career",
                "ach_end_yuuka_mutual_single",
                "ach_end_yuuka_non_marriage",
            ],
            scope="history",
            points=75,
            order=2040
        ),

        "meta_all_thienan_endings": ach(
            "Thiên An Archive Complete",
            "Unlocked all Thiên An ending modules.",
            "meta",
            required_flags=[
                "ach_end_thienan_quang",
                "ach_end_thienan_minh",
                "ach_end_thienan_single",
                "ach_end_thienan_arranged",
            ],
            scope="history",
            points=50,
            order=2050
        ),

        "meta_all_crisis_outcomes": ach(
            "Family Crisis Archive Complete",
            "Unlocked all major family crisis outcomes.",
            "meta",
            required_flags=[
                "crisis_best_outcome",
                "crisis_good_outcome",
                "crisis_partial_legal_clear",
                "crisis_partial_business_saved",
                "crisis_bad_default",
            ],
            scope="history",
            points=75,
            order=2060
        ),

        "meta_all_final_tiers": ach(
            "Final World-State Archive Complete",
            "Unlocked all major final world-state tiers.",
            "meta",
            required_flags=[
                "ach_tier_true",
                "ach_tier_perfect",
                "ach_tier_default",
                "ach_tier_bittersweet",
                "ach_tier_sacrifice",
                "ach_tier_doom",
            ],
            scope="history",
            points=100,
            order=2070
        ),

        "meta_full_archive": ach(
            "The Whole Wind, The Whole Cloud",
            "Completed the major ending archive.",
            "meta",
            required_flags=[
                "ach_end_tam_hoang",
                "ach_end_tam_minh",
                "ach_end_tam_independent",
                "ach_end_tam_unresolved",

                "ach_end_huyen_quan",
                "ach_end_huyen_hoang",
                "ach_end_huyen_independent",

                "ach_end_hoang_tam",
                "ach_end_hoang_huyen",
                "ach_end_hoang_single_growth",

                "ach_end_minh_minyuu_reunion",
                "ach_end_minh_late_reunion",
                "ach_end_minh_private_lovers",
                "ach_end_minh_public_lovers",
                "ach_end_minh_long_distance",
                "ach_end_minh_single",
                "ach_end_minh_friendship",

                "ach_end_yuuka_reunion",
                "ach_end_yuuka_single",
                "ach_end_yuuka_career",
                "ach_end_yuuka_mutual_single",
                "ach_end_yuuka_non_marriage",

                "ach_end_thienan_quang",
                "ach_end_thienan_minh",
                "ach_end_thienan_single",
                "ach_end_thienan_arranged",

                "ach_end_quan_huyen",
                "ach_end_quan_support",

                "ach_end_quang_thienan",
                "ach_end_quang_support",
            ],
            scope="history",
            hidden=True,
            points=150,
            order=9999
        ),
    }


    # -------------------------------------------------------------------------
    # Persistent state
    # -------------------------------------------------------------------------

    def achievement_normalize_persistent():
        if not hasattr(persistent, "unlocked_achievements") or persistent.unlocked_achievements is None:
            persistent.unlocked_achievements = []

        if not hasattr(persistent, "achievement_history_flags") or persistent.achievement_history_flags is None:
            persistent.achievement_history_flags = []

        if not hasattr(persistent, "achievement_system_version") or persistent.achievement_system_version is None:
            persistent.achievement_system_version = ACHIEVEMENT_SYSTEM_VERSION


    def achievement_save():
        achievement_normalize_persistent()
        renpy.save_persistent()


    # -------------------------------------------------------------------------
    # Flag collection
    # -------------------------------------------------------------------------

    def achievement_get_run_flags():
        """
        Collects current-playthrough flags.

        Sources:
        - story_flags
        - progress["player_flags"]
        - story_completed_chapters
        - progress["completed_chapters"]
        - progress["relationship_directions"]
        - story_state["ending_support"] as support:<ending_id>
        - story_state relation / lock virtual flags
        """

        flags = set()

        # Direct story flags.
        for f in getattr(store, "story_flags", []) or []:
            flags.add(str(f))

        # Progress flags, if the project still uses progress["player_flags"].
        progress = getattr(store, "progress", None)
        if isinstance(progress, dict):
            for f in progress.get("player_flags", []) or []:
                flags.add(str(f))

            for ch in progress.get("completed_chapters", []) or []:
                flags.add("chapter:" + str(ch))
                flags.add("completed:" + str(ch))

            # Relationship directions can also be stored here depending on version.
            directions = progress.get("relationship_directions", {}) or {}
            if isinstance(directions, dict):
                for character, values in directions.items():
                    if isinstance(values, (list, tuple, set)):
                        for direction in values:
                            flags.add("direction_%s_%s" % (character, direction))
                            flags.add("direction:%s:%s" % (character, direction))
                    elif values:
                        flags.add("direction_%s_%s" % (character, values))
                        flags.add("direction:%s:%s" % (character, values))

        # Completed chapters fallback.
        for ch in getattr(store, "story_completed_chapters", []) or []:
            flags.add("chapter:" + str(ch))
            flags.add("completed:" + str(ch))

        # Structured story state as virtual flags.
        ss = getattr(store, "story_state", {}) or {}
        if isinstance(ss, dict):
            for e in ss.get("ending_support", []) or []:
                flags.add("support:" + str(e))
                flags.add("ending_support:" + str(e))

            rel = ss.get("minh_yuuka_relation", None)
            if rel:
                flags.add("relation:minyuu:" + str(rel))
                flags.add("minh_yuuka_relation:" + str(rel))

            if ss.get("minh_romance_lock", False):
                flags.add("lock:minh_romance")
                flags.add("lock_minh_romance_except_yuuka")

            if ss.get("yuuka_romance_lock", False):
                flags.add("lock:yuuka_romance")
                flags.add("lock_yuuka_romance_except_minh")

        return flags


    def achievement_get_history_flags():
        achievement_normalize_persistent()
        return set([str(f) for f in persistent.achievement_history_flags or []])


    def achievement_register_seen_flags(flags=None):
        """
        Stores current run flags into persistent history.
        This is what makes completion achievements possible across playthroughs.
        """
        achievement_normalize_persistent()

        if flags is None:
            flags = achievement_get_run_flags()

        history = achievement_get_history_flags()
        changed = False

        for f in flags:
            if f not in history:
                history.add(f)
                changed = True

        if changed:
            persistent.achievement_history_flags = sorted(list(history))
            achievement_save()


    # -------------------------------------------------------------------------
    # Flag writing helpers
    # -------------------------------------------------------------------------

    def achievement_add_story_flag(flag_name, check=True):
        """
        Adds a flag to story_flags without depending on story_flag(...).
        This avoids recursion and keeps achievement flags isolated.

        Use this for achievement/world-state flags:
            achievement_add_story_flag("ach_end_tam_hoang")
        """
        flag_name = str(flag_name)

        if not hasattr(store, "story_flags") or store.story_flags is None:
            store.story_flags = []

        if flag_name not in store.story_flags:
            store.story_flags.append(flag_name)

        if check:
            achievement_check_all("flag:" + flag_name)


    def achievement_record_world_state(flags, check=True):
        """
        Adds multiple achievement/world-state flags at once.

        Use this in final labels or after ending resolution:
            $ achievement_record_world_state([
            $     "ach_tier_true",
            $     "ach_crisis_good_outcome",
            $     "ach_end_tam_hoang",
            $ ])
        """
        if flags is None:
            flags = []

        for f in flags:
            achievement_add_story_flag(f, check=False)

        if check:
            achievement_check_all("world_state")


    def achievement_record_final_ending(ending_id, extra_flags=None, check=True):
        """
        Optional helper for old single-label ending resolver.

        Example:
            $ achievement_record_final_ending("e10_minyuu_reunion", [
            $     "ach_end_minh_minyuu_reunion",
            $     "ach_end_yuuka_reunion",
            $     "ach_pair_minyuu",
            $ ])
        """
        flags = ["final:" + str(ending_id)]
        flags.extend(extra_flags or [])
        achievement_record_world_state(flags, check=check)


    # -------------------------------------------------------------------------
    # Requirement evaluation
    # -------------------------------------------------------------------------

    def achievement_requirements_met(defn, run_flags=None, history_flags=None):
        if run_flags is None:
            run_flags = achievement_get_run_flags()

        if history_flags is None:
            history_flags = achievement_get_history_flags()

        source = history_flags if defn.get("scope", "run") == "history" else run_flags

        for f in defn.get("required_flags", []) or []:
            if f not in source:
                return False

        for group in defn.get("required_any_groups", []) or []:
            if not any((f in source) for f in group):
                return False

        for f in defn.get("forbidden_flags", []) or []:
            if f in source:
                return False

        return True


    def achievement_is_unlocked(achievement_id):
        achievement_normalize_persistent()
        return str(achievement_id) in persistent.unlocked_achievements


    def achievement_unlock(achievement_id, notify=True):
        achievement_normalize_persistent()

        achievement_id = str(achievement_id)
        if achievement_id not in ACHIEVEMENTS:
            return False

        if achievement_id in persistent.unlocked_achievements:
            return False

        persistent.unlocked_achievements.append(achievement_id)
        persistent.unlocked_achievements = sorted(list(set(persistent.unlocked_achievements)))

        if not hasattr(store, "achievement_recent_unlocks") or store.achievement_recent_unlocks is None:
            store.achievement_recent_unlocks = []

        if achievement_id not in store.achievement_recent_unlocks:
            store.achievement_recent_unlocks.append(achievement_id)

        achievement_save()

        if notify:
            title = ACHIEVEMENTS[achievement_id].get("title", achievement_id)
            renpy.notify("Achievement unlocked: " + title)

        return True


    def achievement_check_all(trigger="manual", notify=True):
        """
        Check and unlock achievements.

        Recommended call sites:
        - after story_flag(...)
        - after story_add_direction(...)
        - after story_add_ending_support(...)
        - after story_complete_chapter(...)
        - after final world-state flags are recorded
        """
        achievement_normalize_persistent()

        run_flags = achievement_get_run_flags()

        # First record current flags into persistent history.
        achievement_register_seen_flags(run_flags)

        history_flags = achievement_get_history_flags()
        newly_unlocked = []

        for achievement_id, defn in ACHIEVEMENTS.items():
            if achievement_is_unlocked(achievement_id):
                continue

            if achievement_requirements_met(defn, run_flags=run_flags, history_flags=history_flags):
                if achievement_unlock(achievement_id, notify=False):
                    newly_unlocked.append(achievement_id)

        if newly_unlocked and notify:
            if len(newly_unlocked) == 1:
                title = ACHIEVEMENTS[newly_unlocked[0]].get("title", newly_unlocked[0])
                renpy.notify("Achievement unlocked: " + title)
            else:
                renpy.notify("%d achievements unlocked" % len(newly_unlocked))

        return newly_unlocked


    # -------------------------------------------------------------------------
    # Query helpers for UI/debug
    # -------------------------------------------------------------------------

    def achievement_total_points():
        achievement_normalize_persistent()
        total = 0
        for achievement_id in persistent.unlocked_achievements:
            if achievement_id in ACHIEVEMENTS:
                total += int(ACHIEVEMENTS[achievement_id].get("points", 0))
        return total


    def achievement_completion_count(include_hidden=True):
        achievement_normalize_persistent()

        total = 0
        unlocked = 0

        for achievement_id, defn in ACHIEVEMENTS.items():
            if not include_hidden and defn.get("hidden", False) and not achievement_is_unlocked(achievement_id):
                continue

            total += 1
            if achievement_is_unlocked(achievement_id):
                unlocked += 1

        return unlocked, total


    def achievement_list_by_category(category=None, include_hidden=True):
        achievement_normalize_persistent()

        rows = []

        for achievement_id, defn in ACHIEVEMENTS.items():
            is_unlocked = achievement_is_unlocked(achievement_id)
            is_hidden = defn.get("hidden", False)

            if category is not None and defn.get("category") != category:
                continue

            if is_hidden and not is_unlocked and not include_hidden:
                continue

            rows.append((achievement_id, defn))

        rows.sort(key=lambda item: item[1].get("order", 1000))
        return rows


    def achievement_reset_all():
        """
        Debug only. Do not expose in release builds.
        """
        achievement_normalize_persistent()
        persistent.unlocked_achievements = []
        persistent.achievement_history_flags = []
        achievement_save()
        renpy.notify("Achievement data reset.")