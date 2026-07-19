# Background Asset Audit

Updated: 2026-07-19

## Purpose

Track which authored story scenes have been updated to use suitable existing background assets, which scenes still rely on stand-ins, and which new background assets should be created next.

## Completed Story BG Passes

### `tam_c03_thienan_family`

Updated all 8 authored scene openers from `scene black` to matching existing BGs.

Patched scenes:
- `s00_thienan_intro` → `bg_tam_family_living_room_evening`
- `s01_quang_visit_home` → `bg_tam_family_entry_evening`
- `s02_business_trip_preparation` → `bg_hoangminh_villa_living_room_day` *(temporary day stand-in)*
- `s03_family_pressure` → `bg_tam_family_dining_room_evening`
- `s04_private_sisters_talk` → `bg_tam_family_balcony_night`
- `s05_tam_observes_quang` → `bg_tam_family_living_room_evening`
- `s06_support_choice` → `bg_hoangminh_villa_day` *(temporary exterior day stand-in)*
- `s07_career_seed` → `bg_asset_0008` *(temporary bedroom/study stand-in)*

New dedicated assets still recommended for this chapter:
- `bg_tam_family_house_exterior_day`
- `bg_tam_family_house_exterior_evening`
- `bg_tam_family_house_exterior_night`
- `bg_tam_family_living_room_day`
- `bg_tam_family_dining_room_day`
- `bg_tam_family_entry_day`
- `bg_tam_family_father_study_night`
- `bg_tam_family_tam_room_night`

## Current Pass In Progress

### `tam_c05_sunday_date`

Low-risk patchable openings using existing assets:
- `s01_huyen_morning` → generic morning bedroom stand-in
- `s01_group_morning` → `bg_tam_room_morning`
- `s02_tam_date` → apartment lobby / departure stand-in
- `s02_huyen_date` → apartment lobby / departure stand-in

New assets recommended by this chapter:
- `bg_huyen_room_morning`
- `bg_apartment_lobby_night`
- `bg_city_park_morning`
- `bg_city_park_afternoon`
- `bg_city_park_bench_evening`
- `bg_breakfast_cafe_morning`
- `bg_weekend_market_day`
- `bg_rain_shelter_market_day`
- `bg_car_interior_day`

Notes:
- Existing commented placeholders in `game/scripts/backgrounds.rpy` already hint at some of these needs:
  - `bg_city_park_morning`
  - `bg_city_park_afternoon`
  - `bg_city_park_evening`
  - `bg_city_park_bench_evening`
  - `bg_foodie_street_evening`
  - `bg_street_food_stall_night`

### `tam_c06_minh_returns`

Low-risk patchable openings using existing assets:
- `s01_home_invitation` → Tam room morning stand-in
- `s01_company_rumor_begins` → company office
- `s02_home_door` → Hoàng house front door
- `s02_company_side_information` → company office
- `s03_prepare_for_partner_visit` → company office
- `s04_company_meeting_pending` → meeting room / office setup

New assets recommended by this chapter:
- `bg_tam_room_rain_morning`
- `bg_hoang_house_front_door_evening`
- `bg_hoang_house_dining_room_evening`
- `bg_hoang_house_kitchen_evening`
- `bg_apartment_lobby_night`
- `bg_city_street_rain_day`
- `bg_bus_stop_rain_memory`
- `bg_taxi_interior_rain_day`

### `tam_c07_minh_at_company`

Low-risk patchable openings using existing assets:
- `s01_monday_morning` chapter-card opener → `bg_tam_room_morning`

New assets recommended by this chapter:
- `bg_hotpot_restaurant_evening`
- `bg_company_break_area_evening`

### `yuuka_c08_festival_arrival`

Low-risk patchable openings using existing assets:
- `s01_festival_briefing` chapter-card opener → `bg_meeting_room_day`
- `s03_hoang_introduces_yuuka` chapter-card opener → `bg_airport_arrival_day`

New assets recommended by this chapter:
- `bg_festival_venue_exterior_day`
- `bg_conference_hall_lobby_day`
- `bg_festival_backstage`
- `bg_film_screening_auditorium`

### `prologue_rain_dream`

Best current action:
- Keep under review until a proper rainy street / covered storefront BG exists.

New assets recommended by this chapter:
- `bg_city_street_rain_night`
- `bg_park_shelter_rain_night`
- `bg_bus_stop_rain_night`

## Priority New Asset Pack

If only one pack is commissioned next, the best cross-chapter value is:

1. `bg_city_park_morning`
2. `bg_city_park_afternoon`
3. `bg_city_park_bench_evening`
4. `bg_breakfast_cafe_morning`
5. `bg_huyen_room_morning`
6. `bg_tam_room_rain_morning`
7. `bg_apartment_lobby_night`
8. `bg_city_street_rain_night`
9. `bg_hoang_house_dining_room_evening`
10. `bg_festival_venue_exterior_day`
