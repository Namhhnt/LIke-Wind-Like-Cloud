init -5 python:
    PHONE_THREADS.update({
        "tam_c04_w21_hoang_food": {"id":"tam_c04_w21_hoang_food","type":"chat","contact_id":"hoang","title":"Hoàng","unlock_conditions":["flag:tam_c04_w21_started","flag:tam_c04_tam_hoang_dating"],"sort_order":1710,"messages":[
            {"id":"m01","sender":"hoang","text":"Anh để phần ăn trong tủ lạnh. Nếu qua muộn, hâm ba phút.","time":"07:11"}],"effects_on_read":{"flags":["read_tam_c04_w21_hoang_food"]}},
        "tam_c04_w21_quang_before_visit": {"id":"tam_c04_w21_quang_before_visit","type":"chat","contact_id":"quang","title":"Quang","unlock_conditions":["flag:tam_c04_w21_started","flag:tam_c04_tam_quang_confirmed"],"sort_order":1710,"messages":[
            {"id":"m01","sender":"quang","text":"Tối nay anh qua. Anh đang hỏi trước.","time":"07:13"},{"id":"m02","sender":"player","text":"Tiến bộ đấy.","time":"07:15"}],"effects_on_read":{"flags":["read_tam_c04_w21_quang_before_visit"]}},
        "tam_c04_w21_huyen_ten_days": {"id":"tam_c04_w21_huyen_ten_days","type":"chat","contact_id":"huyen","title":"Huyền","unlock_conditions":["flag:tam_c04_w21_started","flag:tam_c04_huyen_met_anh_nhi"],"sort_order":1705,"messages":[
            {"id":"m01","sender":"huyen","text":"Mười ngày. Anh ấy để lại lịch học dài hơn brief khách hàng.","time":"06:44"},{"id":"m02","sender":"player","text":"Mày vẫn nhận à?","time":"06:46"},{"id":"m03","sender":"huyen","text":"Con bé đã hỏi tao trước anh ấy.","time":"06:47"}],"effects_on_read":{"flags":["read_tam_c04_w21_huyen_ten_days"]}},
        "tam_c04_w22_hoang_ten_minutes": {"id":"tam_c04_w22_hoang_ten_minutes","type":"chat","contact_id":"hoang","title":"Hoàng","unlock_conditions":["flag:tam_c04_w22_started","flag:tam_c04_tam_hoang_dating"],"sort_order":1720,"messages":[
            {"id":"m01","sender":"hoang","text":"Tối nay gọi mười phút được không? Không cần kể chuyện hay.","time":"20:02"}],"effects_on_read":{"flags":["read_tam_c04_w22_hoang_ten_minutes"]}},
        "tam_c04_w22_anhni_question": {"id":"tam_c04_w22_anhni_question","type":"chat","contact_id":"huyen","title":"Huyền","unlock_conditions":["flag:tam_c04_w22_started","flag:tam_c04_huyen_met_anh_nhi"],"sort_order":1715,"messages":[
            {"id":"m01","sender":"huyen","text":"Ánh Nhi vừa hỏi tại sao tao vẫn giúp bố nó nếu ông ấy làm tao tức.","time":"21:12"},{"id":"m02","sender":"player","text":"Mày trả lời sao?","time":"21:14"},{"id":"m03","sender":"huyen","text":"Tao bảo trẻ con đi ngủ.","time":"21:15"}],"effects_on_read":{"flags":["read_tam_c04_w22_anhni_question"]}},
        "tam_c04_w23_group_dinner": {"id":"tam_c04_w23_group_dinner","type":"group_chat","contact_id":None,"title":"Bữa tối cuối tuần","participants":["tam","huyen","hoang"],"unlock_conditions":["flag:tam_c04_w23_started"],"sort_order":1730,"messages":[
            {"id":"m01","sender":"hoang","text":"Tối thứ Bảy. Có chỗ cho trẻ con và người không ăn hành.","time":"07:20"},{"id":"m02","sender":"huyen","text":"Anh đang nói Ánh Nhi hay tôi?","time":"07:22"},{"id":"m03","sender":"hoang","text":"Tôi chưa biết cô cũng không ăn hành.","time":"07:23"},{"id":"m04","sender":"player","text":"Giờ thì biết rồi.","time":"07:24"}],"effects_on_read":{"flags":["read_tam_c04_w23_group_dinner"]}},
        "tam_c04_w24_review": {"id":"tam_c04_w24_review","type":"chat","contact_id":"huyen","title":"Huyền","unlock_conditions":["flag:tam_c04_w24_started"],"sort_order":1740,"messages":[
            {"id":"m01","sender":"huyen","text":"Sáu tháng rồi đấy.","time":"06:35"},{"id":"m02","sender":"player","text":"Nghe dài hơn lúc sống qua.","time":"06:37"},{"id":"m03","sender":"huyen","text":"Vì mày đã dùng nửa thời gian để chọn trả lời ai trước.","time":"06:38"}],"effects_on_read":{"flags":["read_tam_c04_w24_review"]}},
    })
    PHONE_REPLY_CHOICES.update({
        "tam_c04_w21_hoang_food": [
            {"id":"will_come","text":"Em sẽ qua. Có thể hơi muộn.","once":True,"effects":{"story_add":{"hoang_tam_trust":1},"relationship_contacts":[{"pair_id":"tam_hoang","period_id":"tam_c04_w21","source":"phone"}],"flags":["tam_c04_w21_phone_keeps_hoang_contact"]},"response_messages":[{"id":"r01","sender":"hoang","text":"Anh để đèn bếp. Đi chậm thôi.","time":"07:14"}]},
            {"id":"need_alone","text":"Hôm nay em muốn ở một mình.","once":True,"effects":{"story_add":{"tam_self_clarity":1},"relationship_contacts":[{"pair_id":"tam_hoang","period_id":"tam_c04_w21","source":"phone"}],"flags":["tam_c04_w21_phone_asks_space"]},"response_messages":[{"id":"r01","sender":"hoang","text":"Được. Phần ăn để mai cũng được.","time":"07:14"}]}
        ],
        "tam_c04_w22_hoang_ten_minutes": [
            {"id":"call_ten","text":"Được. Mười phút.","once":True,"effects":{"story_add":{"hoang_tam_trust":1},"relationship_contacts":[{"pair_id":"tam_hoang","period_id":"tam_c04_w22","source":"phone"}],"flags":["tam_c04_w22_phone_ten_minute_call"]},"response_messages":[{"id":"r01","sender":"hoang","text":"Anh gọi lúc mười giờ.","time":"20:05"}]}
        ]
    })
