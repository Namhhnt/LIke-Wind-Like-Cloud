# Chapter 07 — `tam_c07_minh_at_company`

## Files

- `_chapter.rpy` — resolves the route snapshot and calls all scenes.
- `s01_monday_morning.rpy` — route-aware opening and company setup.
- `s02_northbridge_arrival.rpy` — Minh enters as NorthBridge adviser; dream recognition and Huyền reactions.
- `s03_working_logic.rpy` — professional interaction and player choice.
- `s04_recognition_and_huyen.rpy` — Tâm's career recognition and route-sensitive Huyền conversation.
- `s05_evening_routes.rpy` — separate endings for stable Hoàng, uncertain Hoàng, uncommitted/career, and fallback routes.

## Route resolution

1. `direction_tam_tam_hoang_commit` + `tam_self_clarity >= 60`
   - Mode: `hoang_clear`
   - Minh remains professional admiration only.

2. `direction_tam_tam_hoang_commit` or `direction_tam_tam_hoang_open`, below the clarity threshold
   - Mode: `hoang_uncertain`
   - Default work choice reproduces the canon dinner misstep and avoidance.
   - Choosing **Giữ khoảng cách** allows an early-honesty repair branch.

3. No romance commit
   - Mode: `uncommitted`
   - Tâm reacts more strongly to confirming Minh as the dream man.
   - Huyền's teasing changes for Huyền–Hoàng, Huyền–Quân, or uncommitted states.

4. Other romance commit
   - Mode: `other_commit`
   - Conservative fallback; keeps the interaction professional.

## Integration notes

- Uses only currently documented backgrounds and the 25 supported side-image expressions.
- `bg_luxury_restaurant_evening` is used as the available placeholder for the dinner/hotpot scene.
- The wrapper calls `time_start_period_after_chapter("tam_c07_minh_at_company")`; remove this line only if Chapter 07 should not open a free-time period in the current progression configuration.
