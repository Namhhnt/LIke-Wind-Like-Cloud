# FILE: game/story/tam/tam_c02_company_party/s01b_first_salary_and_shopping.rpy
# Scene file.
# Temporary implementation: Shopping Area click is represented by a selection menu.
# Later, map_hub / interactive_map can call tam_c02_company_party_shopping_area_menu
# when the player clicks location_id == "shopping_area" during this chapter context.
# # hint:
# if current_chapter == "tam_c02_company_party" and location_id == "shopping_area" and story_has_flag("tam_c02_shopping_area_unlocked"):
#     call tam_c02_company_party_shopping_area_menu

init -4 python:
    def tam_get_monthly_salary_amount():
        return 15000000 if story_has_flag("tam_perfect_interview") else 12000000

    def tam_get_first_paycheck_amount():
        return tam_get_monthly_salary_amount() // 2

    def tam_get_available_money():
        status = phone_get_character_status("tam")
        try:
            return int(status.get("salary") or 0)
        except Exception:
            return 0

    def tam_set_available_money(amount):
        safe_amount = max(0, int(amount or 0))
        phone_update_character_status(
            "tam",
            salary=safe_amount,
            public_stats={"current_money": safe_amount},
        )
        return safe_amount

    def tam_add_available_money(amount):
        updated_amount = tam_set_available_money(tam_get_available_money() + int(amount or 0))
        try:
            activity_add("money", int(amount or 0))
        except Exception:
            pass
        return updated_amount

    def tam_try_spend_money(amount):
        cost = max(0, int(amount or 0))
        current_amount = tam_get_available_money()
        if current_amount < cost:
            return False, current_amount

        remaining_amount = tam_set_available_money(current_amount - cost)
        try:
            activity_add("money", -cost)
        except Exception:
            pass
        return True, remaining_amount

    def tam_sync_c02_after_work_time():
        if story_has_flag("tam_c02_after_work_time_synced"):
            return

        activity_state = ensure_activity_state()
        current_points = int(activity_state.get("time_points", activity_state.get("time_units", 24)) or 0)
        if current_points > 14:
            current_points = 14

        synchronized_points = time_sync_time_keys(current_points)
        activity_state["time_points"] = synchronized_points
        activity_state["time_units"] = synchronized_points
        activity_state["work_completed_today"] = True
        story_flag("tam_c02_after_work_time_synced")

label tam_c02_company_party_s01b_first_salary_and_shopping:
    $ tam_sync_c02_after_work_time()

    scene bg_company_open_office_day
    with fade

    $ tam_first_paycheck = tam_get_first_paycheck_amount()
    if not story_has_flag('tam_c02_first_salary_received'):
        $ story_flag('tam_c02_first_salary_received')
        $ tam_current_money = tam_add_available_money(tam_first_paycheck)
        $ career_assign_level(
            "tam",
            1,
            known_info=["Received first partial salary payment for the last two weeks of October."],
        )
        python:
            activity_state = ensure_activity_state()
            activity_state["monthly_salary"] = phone_get_character_status("tam").get("income_monthly") or activity_state.get("monthly_salary", 0)
            activity_state["player_is_employed"] = True
            activity_state["salary_cycle_day"] = 1
            activity_state["last_salary_day"] = activity_state.get("current_day", 1)
            activity_state["pending_ot_bonus"] = 0
            activity_state["pending_salary_penalty"] = 0
            activity_state["work_attendance_this_month"] = 0
            activity_state["work_absence_this_month"] = 0
            activity_state["unexcused_absence_this_month"] = 0
            activity_state["ot_days_this_month"] = 0
            activity_state.setdefault("salary_history", []).append({
                "day": activity_state.get("current_day", 1),
                "amount": tam_first_paycheck,
                "type": "partial_october_first_salary",
                "chapter": "tam_c02_company_party",
            })
        $ story_flag("tam_c02_salary_mail_sent")
        $ phone_unlock_mail("company_salary_first_month")
        $ phone_refresh_all()
    else:
        $ tam_current_money = tam_get_available_money()


    "Thứ Năm, một ngày trước buổi tiệc kỷ niệm công ty, Tâm nhận được tháng lương đầu tiên."

    "Không có tiếng pháo hoa."

    "Không có nhạc nền chiến thắng."

    "Chỉ có một thông báo ngân hàng hiện lên trên màn hình điện thoại lúc cô vừa định đứng dậy đi lấy nước."

    "Đây là khoản lương một phần vì Tâm chỉ làm việc hai tuần trong tháng Mười — nhưng vẫn đủ để cô nhận ra mình vừa có một thứ thật sự thuộc về mình."

    tam surprised "..."

    huyen neutral "Sao mặt mày nghiêm trọng thế?"

    "Tâm nhìn lại con số trong tin nhắn."

    "Một con số không lớn đến mức thay đổi đời người."

    "Nhưng đủ để khiến cô ngồi yên thêm vài giây."

    tam neutral "Lương về rồi."

    huyen surprised "Thật á?"

    "Huyền lập tức kéo ghế sang, nhanh đến mức bánh xe ghế kêu lên một tiếng nhỏ trên sàn."

    scene cg_tam_c02_first_salary
    with dissolve

    huyen happy "Cho tao xem. Không phải số tiền. Tao xem cảm xúc thôi."

    tam tired "Cảm xúc cũng cần xem màn hình à?"

    huyen grinning "Có những cảm xúc phải có sao kê mới đáng tin."

    scene bg_company_open_office_day
    with dissolve

    "Tâm tắt màn hình điện thoại, nhưng khóe môi vẫn không giấu được."

    "Tháng lương đầu tiên."

    "Cô đã từng nghĩ mình sẽ bình tĩnh hơn."

    "Nhưng hóa ra có những thứ rất đời thường vẫn đủ làm người ta thấy mình vừa bước qua một cánh cửa nhỏ."

    huyen smile "Ngày mai tiệc công ty rồi."

    tam neutral "Ừ."

    huyen teasing "Và mày định mặc bộ váy công sở an toàn như báo cáo nội bộ?"

    tam embarrassed "Tao chưa quyết."

    huyen neutral "Nghĩa là có."

    tam "..."

    huyen tired "Tâm."

    tam confused "Gì?"

    huyen neutral "Tháng lương đầu tiên không bắt buộc phải tiêu hết. Nhưng ít nhất cũng nên mua cho bản thân một thứ để nhớ."

    "Tâm nhìn xuống tay mình."

    "Ngón tay cô đặt trên cạnh điện thoại, vô thức miết nhẹ phần ốp lưng đã hơi cũ."

    tam neutral "Một thứ để nhớ..."

    huyen smile "Ừ. Không cần đắt. Chỉ cần sau này nhìn lại, mày nhớ: à, hồi đó mình bắt đầu đi làm rồi."

    "Câu đó chạm nhẹ hơn Tâm tưởng."

    "Bên ngoài cửa kính văn phòng, nắng chiều đang trượt dần khỏi những tòa nhà đối diện."

    "Một ngày làm việc sắp kết thúc."

    "Ngày mai là buổi tiệc."

    "Nếu muốn mua gì đó, tối nay là lúc hợp lý nhất."

    "Số dư dành riêng cho lần mua sắm này hiện là [activity_format_money(tam_current_money)]."

    menu:
        "Sau giờ làm, Tâm có đi mua sắm không?"

        "Đi Shopping Area với Huyền":
            $ story_flag('tam_c02_shopping_area_unlocked')
            $ story_add('tam_self_clarity', 1)

            tam neutral "Tan làm đi với tao một lát không?"

            huyen happy "Shopping?"

            tam smile "Ừ."

            huyen grinning "Cuối cùng. Công ty này đã tạo ra giá trị xã hội."

            tam tired "Mày bớt nói quá."

            huyen teasing "Không. Khoảnh khắc bạn thân nhận lương đầu và chịu đi mua đồ là sự kiện văn hóa."

            "Tâm cất điện thoại vào túi."

            "Dù chưa biết sẽ mua gì, cô bỗng thấy lòng mình nhẹ hơn một chút."

            call tam_c02_company_party_shopping_map

        "Không mua gì, để dành tiền":
            $ story_add('career_tam', 2)
            $ story_add('tam_self_clarity', 1)
            $ story_flag('tam_c02_saved_first_salary')
            $ story_add_direction('tam', 'tam_career_focus')

            "Tâm nhìn lại tin nhắn ngân hàng."

            "Rồi cô tắt màn hình."

            tam neutral "Thôi. Tao để dành đã."

            huyen confused "Không mua gì thật à?"

            tam smile "Chưa cần."

            huyen neutral "Mai đi tiệc đấy."

            tam neutral "Tao có đồ mặc rồi."

            huyen tired "Câu này nghe như mở đầu của một bi kịch thời trang."

            tam laughing "Không đến mức đó đâu."

            "Huyền nhìn cô thêm một lúc, rồi nhún vai."

            huyen smile "Được. Tiền của mày, mày quyết."

            "Tâm gật đầu."

            "Có một chút tiếc."

            "Nhưng cũng có một chút yên tâm."

            "Tháng lương đầu tiên nằm im trong tài khoản."

            "Như một cái neo nhỏ."

            "Không rực rỡ."

            "Nhưng chắc."

    return
label tam_c02_company_party_shopping_map:
    python:
        map_entries = []
        for loc_id, loc in FIXED_MAP_LOCATIONS.items():
            if fixed_location_is_unlocked(loc_id):
                map_entries.append({
                    "id": "locked_{}".format(loc_id),
                    "location_id": loc_id,
                    "title": loc.get("name", loc_id),
                    "x": loc.get("x", 960),
                    "y": loc.get("y", 540),
                    "state": "locked",
                    "kind": "location_hub",
                    "lock_reason": "Nơi này hiện không khả dụng.",
                })
        shop_loc = FIXED_MAP_LOCATIONS.get("shopping_area", {})
        map_entries.append({
            "id": "shopping_area_active",
            "location_id": "shopping_area",
            "title": shop_loc.get("name", "Shopping Area"),
            "description": "Đi mua váy dự tiệc với Huyền.",
            "x": shop_loc.get("x", 960),
            "y": shop_loc.get("y", 540),
            "state": "available",
            "kind": "temporary",
            "target_label": "tam_c02_company_party_shopping_area_menu",
        })

    call screen interactive_map_screen(map_entries, context_id="shopping_area_visit", allow_back=False, allow_timeline=False)

    $ selected = _return
    if isinstance(selected, dict) and selected.get("target_label"):
        $ target = selected["target_label"]
        if renpy.has_label(target):
            jump expression target

    jump tam_c02_company_party_shopping_area_menu
