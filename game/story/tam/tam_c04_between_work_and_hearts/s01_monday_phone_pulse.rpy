# FILE: game/story/tam/tam_c04_between_work_and_hearts/s01_monday_phone_pulse.rpy
# Week 01 — Monday morning phone pulse.

label tam_c04_w01_s01_monday_phone_pulse:
    scene black
    with fade

    centered "{size=46}CHAPTER 04{/size}\n{size=30}Những ngày lệch nhịp{/size}"

    scene bg_tam_room_morning
    with dissolve

    $ story_flag("tam_c04_w01_started")
    $ phone_refresh_all()

    scene cg_tam_c04_phone_morning
    with dissolve
    "Sáng thứ Hai đến bằng tiếng chuông báo thức và ba thông báo xếp chồng trên màn hình."
    scene bg_tam_room_morning
    with dissolve

    "Tâm ngồi dậy, kéo chăn khỏi đầu gối rồi nhìn điện thoại thêm vài giây."

    tam tired "Mới đầu tuần thôi mà."

    "Tin đầu tiên là của Huyền."

    "Cô ấy gửi ảnh chụp một email được gửi từ sáu giờ mười hai phút sáng, kèm theo đúng một câu hỏi."

    huyen irritated "Anh Quân có ngủ không vậy?"

    "Tin thứ hai nằm dưới một thông báo công việc."

    if story_state.get("tam_hoang_interest", 0) >= 40:
        "Tên Hoàng hiện lên ở cuối danh sách. Không có lời chào dài. Chỉ là một câu hỏi về buổi sáng của cô."
    else:
        "Không có tin nào từ Hoàng. Tâm lướt qua danh sách, ngón tay dừng rất ngắn rồi tiếp tục."

    if story_state.get("thienan_quang_trust", 0) >= 35:
        "Quang cũng để lại một tin nhắn từ tối qua, hỏi Thiên An đã về nhà chưa."
        "Cách hỏi vòng qua Tâm quen thuộc đến mức cô không cần nghĩ cũng hiểu anh đang lo điều gì."

    "Tâm đặt điện thoại lên bàn, đi rửa mặt."

    "Khi quay lại, màn hình lại sáng."

    "Huyền đã gửi thêm một tin."

    huyen frustrated "Nếu hôm nay tao không đến công ty, nhớ nói với mọi người tao đã chiến đấu rất dũng cảm."

    tam teasing "Mày mới chỉ mở email thôi."

    huyen neutral "Đừng coi thường tổn thương tinh thần."

    "Tâm bật cười, nhét điện thoại vào túi."

    "Một tuần mới bắt đầu như thế. Không có gì đặc biệt. Chỉ là vài cái tên đã bắt đầu xuất hiện đúng chỗ hơn trước."

    return
