init -5 python:
    PHONE_THREADS.update({
        "tam_c04_w13_hoang_fixed_evening": {"id":"tam_c04_w13_hoang_fixed_evening","type":"chat","contact_id":"hoang","title":"Hoàng","unlock_conditions":["flag:tam_c04_w13_started","score_gte:tam_hoang_interest:55"],"sort_order":1510,"messages":[
            {"id":"m01","sender":"hoang","text":"Tối thứ Tư, bảy giờ. Anh giữ bàn một tiếng.","time":"07:12"},{"id":"m02","sender":"player","text":"Anh đặt lịch thật à?","time":"07:15"},{"id":"m03","sender":"hoang","text":"Ừ. Để cả hai không phải đoán tuần này còn gặp được không.","time":"07:16"}],"effects_on_read":{"flags":["read_tam_c04_w13_hoang_fixed_evening"]}},
        "tam_c04_w13_quang_departure": {"id":"tam_c04_w13_quang_departure","type":"chat","contact_id":"quang","title":"Quang","unlock_conditions":["flag:tam_c04_w13_started"],"sort_order":1505,"messages":[
            {"id":"m01","sender":"quang","text":"Anh và chị An bay lúc sáu giờ chiều.","time":"07:03"},{"id":"m02","sender":"player","text":"Bao giờ về?","time":"07:05"},{"id":"m03","sender":"quang","text":"Chưa chốt. Anh sẽ báo.","time":"07:06"}],"effects_on_read":{"flags":["read_tam_c04_w13_quang_departure"]}},
        "tam_c04_w14_huyen_anhni": {"id":"tam_c04_w14_huyen_anhni","type":"chat","contact_id":"huyen","title":"Huyền","unlock_conditions":["flag:tam_c04_w14_started"],"sort_order":1520,"messages":[
            {"id":"m01","sender":"huyen","text":"Con bé không ăn hành. Sao bố nó không ghi điều này vào mail?","time":"06:51"},{"id":"m02","sender":"player","text":"Có thể anh ấy nghĩ mày sẽ hỏi.","time":"06:53"},{"id":"m03","sender":"huyen","text":"Tao đang hỏi tại sao anh ấy nghĩ tao sẽ hỏi.","time":"06:54"}],"effects_on_read":{"flags":["read_tam_c04_w14_huyen_anhni"]}},
        "tam_c04_w14_hoang_after_missed": {"id":"tam_c04_w14_hoang_after_missed","type":"chat","contact_id":"hoang","title":"Hoàng","unlock_conditions":["flag:tam_c04_w14_started","score_gte:tam_hoang_interest:55"],"sort_order":1525,"messages":[
            {"id":"m01","sender":"hoang","text":"Anh về trước. Em làm xong thì nghỉ đi.","time":"21:18"}],"effects_on_read":{"flags":["read_tam_c04_w14_hoang_after_missed"]}},
        "tam_c04_w15_quang_midnight": {"id":"tam_c04_w15_quang_midnight","type":"chat","contact_id":"quang","title":"Quang","unlock_conditions":["flag:tam_c04_w15_started"],"sort_order":1530,"messages":[
            {"id":"m01","sender":"quang","text":"Hôm nay ổn. Chị An chịu ăn tối.","time":"00:47"},{"id":"m02","sender":"player","text":"Còn anh?","time":"00:50"},{"id":"m03","sender":"quang","text":"Anh đang trả lời em nên chắc là ổn.","time":"00:51"}],"effects_on_read":{"flags":["read_tam_c04_w15_quang_midnight"]}},
        "tam_c04_w16_quan_thanks_huyen": {"id":"tam_c04_w16_quan_thanks_huyen","type":"chat","contact_id":"huyen","title":"Huyền","unlock_conditions":["flag:tam_c04_w16_started","flag:tam_c04_huyen_met_anh_nhi"],"sort_order":1540,"messages":[
            {"id":"m01","sender":"huyen","text":"Anh Quân vừa nhắn đúng bốn chữ: Cảm ơn cô. Tôi về.","time":"06:40"},{"id":"m02","sender":"player","text":"Mày muốn mấy chữ?","time":"06:42"},{"id":"m03","sender":"huyen","text":"Không muốn. Tao chỉ đang đếm.","time":"06:43"}],"effects_on_read":{"flags":["read_tam_c04_w16_quan_thanks_huyen"]}},
    })
    PHONE_REPLY_CHOICES.update({
        "tam_c04_w13_hoang_fixed_evening": [
            {"id":"keep_evening","text":"Em sẽ giữ tối đó.","once":True,"effects":{"story_add":{"tam_hoang_interest":1,"hoang_tam_trust":1},"flags":["tam_c04_w13_phone_keeps_hoang_evening"]},"response_messages":[{"id":"r01","sender":"hoang","text":"Được. Có thay đổi thì báo anh.","time":"07:18"}]},
            {"id":"cannot_promise","text":"Em chưa dám hứa.","once":True,"effects":{"story_add":{"tam_self_clarity":1},"flags":["tam_c04_w13_phone_uncertain_hoang"]},"response_messages":[{"id":"r01","sender":"hoang","text":"Vậy khi biết thì nói. Đừng im.","time":"07:18"}]}
        ],
        "tam_c04_w13_quang_departure": [
            {"id":"report_landing","text":"Hạ cánh thì báo em.","once":True,"effects":{"story_add":{"tam_quang_interest":1},"tam_c04_extended_story_add":{"quang_tam_warmth":1,"quang_tam_awareness":1},"flags":["tam_c04_w13_phone_asks_quang_report"]},"response_messages":[{"id":"r01","sender":"quang","text":"Ừ. Anh sẽ báo.","time":"07:08"}]},
            {"id":"care_thienan","text":"Anh để ý chị An giúp em.","once":True,"effects":{"story_add":{"thienan_quang_trust":1},"tam_c04_extended_story_add":{"quang_thienan_resolve":1},"flags":["tam_c04_w13_phone_supports_south_pair"]},"response_messages":[{"id":"r01","sender":"quang","text":"Anh biết.","time":"07:08"}]}
        ],
        "tam_c04_w15_quang_midnight": [
            {"id":"ask_quang","text":"Em hỏi anh có ổn không.","once":True,"effects":{"story_add":{"tam_quang_interest":1},"tam_c04_extended_story_add":{"quang_tam_warmth":1,"quang_tam_awareness":1},"flags":["tam_c04_w15_phone_asks_quang_himself"]},"response_messages":[{"id":"r01","sender":"quang","text":"Giờ thì ổn.","time":"00:53"}]},
            {"id":"support_thienan","text":"Ở cạnh chị ấy nhé.","once":True,"effects":{"story_add":{"thienan_quang_trust":1},"tam_c04_extended_story_add":{"quang_thienan_resolve":1},"flags":["tam_c04_w15_phone_supports_thienan"]},"response_messages":[{"id":"r01","sender":"quang","text":"Ừ.","time":"00:53"}]}
        ]
    })
