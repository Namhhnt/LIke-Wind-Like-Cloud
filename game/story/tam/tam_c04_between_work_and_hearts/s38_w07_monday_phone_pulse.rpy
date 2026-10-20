# FILE: game/story/tam/tam_c04_between_work_and_hearts/s38_w07_monday_phone_pulse.rpy
# Week 07 — Monday pulse before pressure exposes small truths.

label tam_c04_w07_s01_monday_phone_pulse:
    scene bg_tam_room_morning
    with fade

    $ story_flag("tam_c04_w07_started")
    $ phone_refresh_all()

    scene cg_tam_c04_phone_morning
    with dissolve
    "Sáng thứ Hai, điện thoại Tâm có bốn thông báo đến trong vòng sáu phút."
    scene bg_tam_room_morning
    with dissolve

    if story_state.get("huyen_quan_interest", 0) >= 12:
        "Huyền gửi ảnh một comment của Quân và hỏi dấu chấm cuối câu có nghĩa gì."
    elif story_state.get("huyen_quan_trust", 0) >= 45:
        "Huyền gửi bản đã sửa trước khi Quân nhắc. Cô vẫn gọi đó là phòng thủ chủ động."

    if story_state.get("tam_hoang_interest", 0) >= 70:
        "Hoàng hỏi Tâm đã ăn sáng chưa, rồi gửi địa chỉ một quán gần công ty trước khi cô trả lời."
    elif story_state.get("tam_hoang_interest", 0) >= 50:
        "Hoàng gửi một bức ảnh bữa sáng và viết: anh không mua dư, nhưng có thể."

    if story_state.get("quang_tam_awareness", 0) >= 20:
        "Quang nhắn rằng hộp thức ăn tuần trước Tâm chưa trả. Một cái cớ khá yếu."
    elif story_state.get("quang_thienan_resolve", 0) >= 65:
        "Thiên An nhắn Quang sẽ tới công ty gia đình chiều nay. Không ai hỏi vì sao."

    "Tin cuối cùng là email từ khách hàng."

    "Tiêu đề có chữ gấp."

    "Tâm đặt điện thoại xuống, uống nốt ngụm nước đã nguội."

    return
