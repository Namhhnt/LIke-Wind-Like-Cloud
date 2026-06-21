label hoang_h01:
    # POV demo: this chapter unlocks two mutually exclusive bonus chapters.
    "Hoang's point of view arrives between Tam's second and third beats."
    "Completing it unlocks two mutually exclusive bonus chapters before the route can settle into its next shape."

    $ complete_chapter("hoang_h01")
    jump route_map


label hoang_bonus_restraint:
    # Bonus + hard exclusion demo: restraint excludes confession and unlocks a gentler direction.
    "Hoang chooses restraint and leaves several thoughts unspoken."
    "That choice closes off the confession variant and unlocks a gentler follow-up tone."

    $ complete_chapter("hoang_bonus_restraint")
    jump route_map


label hoang_bonus_confession:
    # Bonus + hard exclusion demo: confession excludes restraint and unlocks a more forceful direction.
    "Hoang speaks too directly, forcing the scene toward confession instead of restraint."
    "That choice excludes the quieter variant and unlocks a more forward follow-up path."

    $ complete_chapter("hoang_bonus_confession")
    jump route_map


label hoang_h02:
    # Soft-hide demo: hidden until one Hoang bonus chapter is completed.
    "Hoang's second chapter now depends on both his first scene and Tam's third one."
    "This closes the first two-route loop and gives route focus something meaningful to measure."

    if has_relationship_direction("hoang", "restraint"):
        "The restraint path keeps the scene quiet, careful, and almost fragile."

    if has_relationship_direction("hoang", "confession"):
        "The confession path carries more force, but also more risk of being misunderstood."

    $ complete_chapter("hoang_h02")
    jump resolve_seed_ending


label resolve_seed_ending:
    if "ending_true_convergence" in progress["ending_eligibility"]:
        jump ending_true_convergence
    elif "ending_focus_hoang" in progress["ending_eligibility"]:
        jump ending_focus_hoang
    elif "ending_shared_silence" in progress["ending_eligibility"]:
        jump ending_shared_silence
    elif "ending_restraint" in progress["ending_eligibility"]:
        jump ending_restraint
    elif "ending_confession" in progress["ending_eligibility"]:
        jump ending_confession

    jump route_map


label ending_shared_silence:
    # Emotional-state ending demo.
    $ mark_ending_seen("ending_shared_silence")
    "Ending unlocked: Shared Silence."
    "Trust outweighs distance, and the two routes finally converge without forcing the moment apart."
    jump route_map


label ending_focus_hoang:
    # Route-focus ending demo.
    $ mark_ending_seen("ending_focus_hoang")
    "Ending unlocked: Hoang Focus."
    "Because the playthrough leaned harder into Hoang's route, the resolution centers his emotional trajectory over Tam's hesitation."
    jump route_map


label ending_restraint:
    # Exclusion-sensitive ending demo.
    $ mark_ending_seen("ending_restraint")
    "Ending unlocked: Quiet Restraint."
    "Hoang keeps his feelings measured, and the route resolves through patience rather than confession."
    jump route_map


label ending_confession:
    # Exclusion-sensitive ending demo.
    $ mark_ending_seen("ending_confession")
    "Ending unlocked: Sudden Confession."
    "The confession path lands first, reshaping the route through urgency instead of caution."
    jump route_map


label ending_true_convergence:
    # True-ending demo: requires prior persistent clears.
    $ mark_ending_seen("ending_true_convergence")
    "True ending unlocked: True Convergence."
    "After seeing both Hoang directions across playthroughs, the routes can finally resolve into a calmer understanding that was impossible before."
    jump route_map
