# FILE: game/story/tam/tam_c04_between_work_and_hearts/s06_w02_monday_phone_pulse.rpy
# Week 02 — Monday route-status pulse after the first free weekend.

label tam_c04_w02_s01_monday_phone_pulse:
    scene bg_tam_room_morning
    with fade

    $ story_flag("tam_c04_w02_started")
    $ phone_refresh_all()

    scene cg_tam_c04_phone_morning
    with dissolve
    "Sáng thứ Hai, điện thoại của Tâm sáng lên trước khi chuông báo thức kịp reo lần hai."
    scene bg_tam_room_morning
    with dissolve

    "Tin đầu tiên vẫn là của Huyền."

    huyen neutral "Tao đã sửa trước ba chỗ anh Quân có thể sẽ hỏi."

    tam tired "Mày đang khoe hay đang cầu cứu?"

    huyen irritated "Tao chưa quyết định."

    "Tâm chống tay ngồi dậy. Một tuần trước, Huyền còn gọi mỗi dấu khoanh đỏ là hiện trường vụ án."

    "Hôm nay cô đã tự tìm vị trí đặt băng cảnh giới."

    if story_has_flag("tam_c04_w01_first_focus_hoang") or story_state.get("tam_hoang_interest", 0) >= 50:
        "Bên dưới là tin nhắn của Hoàng."
        "Anh không hỏi cuối tuần vừa rồi vui không. Chỉ gửi một tấm ảnh hộp bánh còn nguyên và nói mình đã mua dư."
    else:
        "Khung chat với Hoàng nằm yên phía dưới. Lời mời cũ không biến mất, nhưng cũng không được nhắc lại."

    if story_has_flag("tam_c04_w01_first_focus_quang_thienan") or story_state.get("thienan_quang_trust", 0) >= 40:
        "Quang gửi một câu ngắn hơn thường lệ."
        quang "Anh đã gọi thẳng cho chị An rồi."
        "Không có câu hỏi nào gửi kèm cho Tâm."

    if story_has_flag("tam_c04_w01_first_focus_career"):
        "Thông báo cuối cùng là email xác nhận Tâm đã hoàn thành phần đầu của khóa học nội bộ."
        "Không ai gửi nó để nhắc cô. Cảm giác ấy nhỏ, nhưng sạch sẽ."

    "Tâm kéo rèm cửa. Nắng sáng lọt vào thành một vệt mỏng trên sàn."

    "Những lựa chọn tuần trước không tạo ra một con đường mới ngay lập tức."

    "Chúng chỉ làm một vài người đổi cách mở lời."

    return
