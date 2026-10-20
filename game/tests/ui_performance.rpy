# Opt-in Windows benchmark. Uses the same isolated savedir as ui_refresh.
# Forces interaction updates, like repeated hovering, rather than measuring idle FPS.
init python:
    def ui_perf_state_contract():
        # Readers must not recalculate progression, but a fresh/legacy save
        # must still bootstrap and time mutations must remain visible at once.
        import copy
        original_progress = store.progress
        original_initializer = store.initialize_progression
        calls = []
        def counted_initialize():
            calls.append(True)
            return original_initializer()
        try:
            store.progress = copy.deepcopy(original_progress)
            store.initialize_progression = counted_initialize
            for unused in range(20):
                time_get_clock_header_line()
                time_get_points_header_line()
                time_get_main_today_summary()
            readers_are_cheap = len(calls) == 0
            activity_set("time_points", 12)
            mutations_are_live = activity_get("time_units") == 12 and time_get_current_hour_24() == 18
            store.progress["activity_state"] = None
            legacy_state = ensure_activity_state()
            migration_works = isinstance(legacy_state.get("inventory"), dict) and "time_points" in legacy_state
            store.progress = make_progress_state()
            ensure_activity_state()
            bootstrap_works = store.progress["initialized"] and len(calls) == 1
            return readers_are_cheap and mutations_are_live and migration_works and bootstrap_works
        finally:
            store.initialize_progression = original_initializer
            store.progress = original_progress

    def ui_perf_begin(name):
        import cProfile
        import time
        store._ui_perf_name = name
        store._ui_perf_frames = []
        store._ui_perf_draw = renpy.display.interface.draw_screen
        def measured_draw(*args, **kwargs):
            start = time.perf_counter()
            try:
                return store._ui_perf_draw(*args, **kwargs)
            finally:
                store._ui_perf_frames.append((time.perf_counter() - start) * 1000)
        renpy.display.interface.draw_screen = measured_draw
        store._ui_perf_profile = cProfile.Profile()
        store._ui_perf_profile.enable()

    def ui_perf_end():
        import json
        import os
        import pstats
        store._ui_perf_profile.disable()
        renpy.display.interface.draw_screen = store._ui_perf_draw
        tag = os.environ.get("LWLC_PERF_TAG", "local")
        directory = os.path.join(config.basedir, "tests", "performance")
        os.makedirs(directory, exist_ok=True)
        frames = sorted(store._ui_perf_frames)
        result = {"screen": store._ui_perf_name, "frames": len(frames),
            "draw_median_ms": frames[len(frames)//2] if frames else None,
            "draw_p95_ms": frames[min(len(frames)-1, int(len(frames)*.95))] if frames else None,
            "renderer": str(renpy.get_renderer_info())}
        stem = os.path.join(directory, tag + "_" + store._ui_perf_name)
        with open(stem + ".json", "w", encoding="utf-8") as output:
            json.dump(result, output, indent=2)
        with open(stem + ".txt", "w", encoding="utf-8") as output:
            pstats.Stats(store._ui_perf_profile, stream=output).sort_stats("cumulative").print_stats(65)

screen ui_perf_tick():
    timer 0.016 repeat True action Function(renpy.restart_interaction)

testsuite ui_performance:
    setup:
        $ renpy.set_physical_size((1920, 1080))
        $ initialize_progression()
        $ phone_ensure_state()

    testcase interaction_cost:
        run ShowMenu("library")
        pause 0.7
        run Show("ui_perf_tick")
        $ ui_perf_begin("library")
        pause 2.0
        $ ui_perf_end()
        run Hide("ui_perf_tick")
        run ShowMenu("phone_home")
        pause 0.7
        run Show("ui_perf_tick")
        $ ui_perf_begin("phone")
        pause 2.0
        $ ui_perf_end()
        run Hide("ui_perf_tick")
        $ ui_perf_entries = build_map_entries(context_id="act1_default")
        run ShowMenu("interactive_map_screen", entries=ui_perf_entries, allow_timeline=True)
        pause 0.7
        run Show("ui_perf_tick")
        $ ui_perf_begin("map")
        pause 2.0
        $ ui_perf_end()
        run Hide("ui_perf_tick")
        assert eval len(_ui_perf_frames) > 10

    testcase state_contract:
        assert eval ui_perf_state_contract()
        assert eval ui_panel() is ui_panel()
        assert eval ui_icon("stories") is ui_icon("stories")
        assert eval ui_map_pin(kind="home") is ui_map_pin(kind="home")
