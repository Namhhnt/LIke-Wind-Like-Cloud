# Production menu consistency rollout

The review samples are no longer the only implementation. Production screens now
share the Library's café background, ivory/serif typography, rounded brown panels,
gold focus/selection states, and cached panel/icon factories.

## Applied surfaces

- Main menu, language selection, start prompt, and shared game-menu navigation.
- Preferences (desktop columns; compact tabs), save/load, history, help, about,
  and confirmation dialogs.
- Library home (even three-column desktop grid; scrollable two-column compact
  grid), profiles, story/music/minigame cards, extras, and unlock confirmation.
- Phone home and app surfaces, with a wide compact-landscape shell and real
  messaging/read/reply actions retained.
- Side-story reader: desktop 16:9 stage; compact fullscreen artwork with
  a taller scrollable dialogue overlay, narrow chevron paging controls at its
  left/right edges, and icon back/hide/show controls.
- Timeline panels and compact action/navigation controls. Graph/progression
  logic and node geometry are unchanged.

`ui_is_compact()` uses touch/small variants or a physical window width <=1000.
It does not force a fixed resolution or change image quality. Mobile controls
use familiar icons where appropriate; categories and settings keep descriptive
labels. Icon controls retain accessible labels and large hit areas.

## Verification

`game/tests/ui_consistency_live.rpy` covers production screens in default English
and Vietnamese at 1920x1080 and 800x450, with screenshots under
`tests/screenshots/ui_consistency_live`. The suite exercises reader paging and
visibility, compact settings tabs, phone navigation, and confirmation dismissal.
Run using the Windows SDK with an isolated `--savedir`.

Windows compact-window testing is not physical touch-device testing. Portrait,
OS safe-area insets and wide-aspect device behavior still require device QA.
No claim of an FPS increase is made by this menu rollout. Cached panels/icons
and previous progression optimizations are retained; no per-frame blur or
new polling timers were introduced.

Verified on Windows / RTX 2070 SUPER / GL2:

- Production UI: 108 assertions passed (four locale/viewport combinations).
- Existing main-screen regression suite: 48 assertions passed.
- Formatted Vietnamese labels: 3 assertions passed.
- Cache/state/render smoke suite: 5 assertions passed.
- Short profiled draw-screen medians: Library 4.99ms, Phone 5.81ms,
  Map 7.87ms; p95 6.74/8.56/9.60ms respectively. These are not FPS or
  input-latency measurements, and are not a matched before/after comparison.
  Phone's new measured median exceeds the older recorded 1.74ms sample;
  this rollout does not claim a phone-rendering speedup.
