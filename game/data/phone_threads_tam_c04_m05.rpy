init -5 python:
    PHONE_THREADS.update({
        "tam_c04_w17_hoang_sunday": {"id":"tam_c04_w17_hoang_sunday","type":"chat","contact_id":"hoang","title":"Hoàng","unlock_conditions":["flag:tam_c04_w17_started","score_gte:tam_hoang_interest:60"],"sort_order":1610,"messages":[
            {"id":"m01","sender":"hoang","text":"Chủ Nhật này anh muốn gặp em. Không có cớ nào khác.","time":"07:20"},{"id":"m02","sender":"player","text":"Anh bỏ hết đường lui rồi à?","time":"07:23"},{"id":"m03","sender":"hoang","text":"Ừ. Em vẫn có quyền nói không.","time":"07:24"}],"effects_on_read":{"flags":["read_tam_c04_w17_hoang_sunday"]}},
        "tam_c04_w17_quang_return": {"id":"tam_c04_w17_quang_return","type":"chat","contact_id":"quang","title":"Quang","unlock_conditions":["flag:tam_c04_w17_started"],"sort_order":1605,"messages":[
            {"id":"m01","sender":"quang","text":"Anh về rồi.","time":"06:18"},{"id":"m02","sender":"player","text":"Em biết. Em đang đứng ở sảnh.","time":"06:19"}],"effects_on_read":{"flags":["read_tam_c04_w17_quang_return"]}},
        "tam_c04_w18_no_more_questions": {"id":"tam_c04_w18_no_more_questions","type":"chat","contact_id":"huyen","title":"Huyền","unlock_conditions":["flag:tam_c04_w18_started"],"sort_order":1620,"messages":[
            {"id":"m01","sender":"huyen","text":"Hôm nay mày phải nói rồi đúng không?","time":"06:45"},{"id":"m02","sender":"player","text":"Ừ.","time":"06:47"},{"id":"m03","sender":"huyen","text":"Tốt. Tao không đưa lời khuyên. Mày đã trốn sau lời khuyên đủ lâu rồi.","time":"06:48"}],"effects_on_read":{"flags":["read_tam_c04_w18_no_more_questions"]}},
        "tam_c04_w19_hoang_schedule": {"id":"tam_c04_w19_hoang_schedule","type":"chat","contact_id":"hoang","title":"Hoàng","unlock_conditions":["flag:tam_c04_w19_started","flag:tam_c04_tam_hoang_dating"],"sort_order":1630,"messages":[
            {"id":"m01","sender":"hoang","text":"Anh rảnh tối thứ Ba và thứ Sáu. Em muốn giữ tối nào?","time":"07:02"}],"effects_on_read":{"flags":["read_tam_c04_w19_hoang_schedule"]}},
        "tam_c04_w19_quang_place": {"id":"tam_c04_w19_quang_place","type":"chat","contact_id":"quang","title":"Quang","unlock_conditions":["flag:tam_c04_w19_started","flag:tam_c04_tam_quang_confirmed"],"sort_order":1630,"messages":[
            {"id":"m01","sender":"quang","text":"Tối thứ Tư đi ăn nhé. Chỉ hai đứa mình.","time":"07:04"},{"id":"m02","sender":"player","text":"Anh đã phải gõ lại mấy lần?","time":"07:06"},{"id":"m03","sender":"quang","text":"Bốn.","time":"07:07"}],"effects_on_read":{"flags":["read_tam_c04_w19_quang_place"]}},
        "tam_c04_w20_huyen_key": {"id":"tam_c04_w20_huyen_key","type":"chat","contact_id":"huyen","title":"Huyền","unlock_conditions":["flag:tam_c04_w20_started","flag:tam_c04_huyen_met_anh_nhi"],"sort_order":1640,"messages":[
            {"id":"m01","sender":"huyen","text":"Tao vẫn đang giữ chìa khóa nhà anh Quân.","time":"06:39"},{"id":"m02","sender":"player","text":"Mày muốn trả à?","time":"06:41"},{"id":"m03","sender":"huyen","text":"Tao đang hỏi tại sao tao chưa trả.","time":"06:42"}],"effects_on_read":{"flags":["read_tam_c04_w20_huyen_key"]}},
    })
    PHONE_REPLY_CHOICES.update({
        "tam_c04_w17_hoang_sunday": [
            {"id":"keep_sunday","text":"Em sẽ giữ Chủ Nhật.","once":True,"effects":{"story_add":{"tam_hoang_interest":1,"hoang_tam_trust":1},"flags":["tam_c04_w17_phone_keeps_sunday"]},"response_messages":[{"id":"r01","sender":"hoang","text":"Anh sẽ gửi địa chỉ. Không cần mặc đẹp.","time":"07:26"}]},
            {"id":"need_answer","text":"Em cần nói chuyện với một người trước.","once":True,"effects":{"story_add":{"tam_self_clarity":1},"flags":["tam_c04_w17_phone_needs_answer"]},"response_messages":[{"id":"r01","sender":"hoang","text":"Anh hiểu. Nói với anh sau đó.","time":"07:26"}]}
        ],
        "tam_c04_w19_hoang_schedule": [
            {"id":"choose_friday","text":"Thứ Sáu. Nếu trễ em sẽ báo.","once":True,"effects":{"story_add":{"hoang_tam_trust":1},"relationship_contacts":[{"pair_id":"tam_hoang","period_id":"tam_c04_w19","source":"phone"}],"flags":["tam_c04_w19_phone_keeps_hoang_contact"]},"response_messages":[{"id":"r01","sender":"hoang","text":"Được. Anh giữ tối đó.","time":"07:05"}]}
        ],
        "tam_c04_w19_quang_place": [
            {"id":"accept_place","text":"Được. Chỉ hai đứa mình.","once":True,"effects":{"story_add":{"tam_quang_interest":1},"tam_c04_extended_story_add":{"quang_tam_awareness":1},"flags":["tam_c04_w19_phone_accepts_quang_outing"]},"response_messages":[{"id":"r01","sender":"quang","text":"Anh đặt bàn.","time":"07:09"}]}
        ]
    })
