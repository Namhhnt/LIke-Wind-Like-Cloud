# Desktop UI performance investigation — 2026-10-20

## Findings and fixes

1. `ensure_activity_state()` called `initialize_progression()` on every HUD read.
   In the baseline Map profile this happened 187 times across 17 interaction
   updates (11 calls/update). Each call recalculated chapter/route/ending state,
   validated metadata and scanned phone unlock conditions. Readers now bootstrap
   only when progression is not initialized. Explicit start, after-load,
   chapter-completion and map-entry refresh paths remain intact.
2. UI constructors created new panels/icons on every screen reevaluation. Icon
   render methods additionally constructed SVG transforms and medallions *inside*
   rendering, preventing child prediction and render-tree reuse. Bounded factories
   now share immutable visual definitions; icons and pins retain their children
   and expose them through `visit()`. Pure factories allow screen optimization.
   Cache bounds: 192 panel styles, 64 icon variants, 32 pin variants. Game state
   and translated text are not cached by these factories.
3. Map's scrolling location list was measured at different widths by the
   scrollbar layout and final render. Text layouts were repeatedly rebuilt:
   the intermediate profile showed 4,304 Text Layout constructions in 37 updates.
   The viewport is now explicitly 374 logical px and its content 350 logical px.
   Rows have parameterized scopes and stable entry IDs; marker ordering also
   uses stable IDs. Existing wrapping, scrolling and selection remain live.

No reduction of antialiasing, icon supersampling, background resolution, shader
quality, frame-rate preference or image-cache budget was used. Blur was inspected
but the measured hot paths were state refresh and render/layout churn, so blur
was retained. The user's staged image-optimizer changes were not modified.

## Reproducible measurements

Windows 11, RTX 2070 SUPER, GL2, 1920×1080. Installed Windows runtime reports
Ren'Py `8.5.4.26101301+nightly` despite the SDK directory name `renpy-8.3.2-sdk`.

`game/tests/ui_performance.rpy` warms each screen for 0.7 s, then profiles a
2 s interval with a 16 ms timer requesting interaction restarts. It records
wall time spent in `Interface.draw_screen` plus a cumulative cProfile report.
This stresses interaction rebuilds; it is **not** a gameplay FPS benchmark,
GPU-only timing, input-latency measurement or cold-screen loading benchmark.
The hook includes Ren'Py's render-only draw calls as well as submitted draws;
their proportions can change when caching improves. Profiler overhead is present
in both runs. Do not convert these values to presented FPS.

Matched initial baseline (`before`) and final isolated verification pass
(`verified`, after adding selection assertions):

| Screen | Median before → after (ms) | p95 before → after (ms) |
| --- | --- | --- |
| Library | 14.43 → 5.48 | 17.23 → 6.73 |
| Phone home | 11.57 → 1.74 | 14.58 → 7.36 |
| Interactive Map | 48.93 → 9.29 | 59.63 → 12.61 |

These are short diagnostic samples on this PC, not guarantees for other
hardware or every chapter. Raw JSON and top-65 cProfile reports are generated
under ignored `tests/performance/`. Several intermediate passes are retained
locally. Use the same renderer, resolution and workload when comparing runs.

```powershell
$env:LWLC_PERF_TAG = 'local'
& D:/RenPy/renpy-8.3.2-sdk/lib/py3-windows-x86_64/python.exe `
  D:/RenPy/renpy-8.3.2-sdk/renpy.py `
  D:/Projects/RenPy_Games/LikeWindLikeCloud `
  --savedir D:/Projects/RenPy_Games/LikeWindLikeCloud/tests/ui_refresh_saves `
  test ui_performance --report-detailed
```

Run this benchmark alone, not alongside screenshot tests or another game
instance. It uses an isolated savedir and never the player's actual save.
Tests and generated performance output are excluded from distribution builds.

## Regression coverage

- UI suite: English/Vietnamese × 1080p/720p, real Windows captures, 48 assertions,
  including location-list click/focus, locked travel action, active-day HUD,
  Library localization and phone back navigation.
- Performance suite: 5 assertions including factory identity reuse and an
  isolated state contract checking that repeated HUD reads do not initialize
  progression, time changes appear immediately, legacy activity state migrates,
  and fresh progression still bootstraps.
- Screenshots were visually checked for Map wrapping/scrollbar boundaries,
  panel edges and controls. Full narrative playthrough, integrated-GPU testing
  and long-session VRAM profiling remain outside this pass.
