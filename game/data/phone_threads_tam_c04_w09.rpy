init -5 python:
    PHONE_THREADS.update({
        "tam_c04_w09_hoang_kept_place": {"id":"tam_c04_w09_hoang_kept_place","type":"chat","contact_id":"hoang","title":"Hoàng","unlock_conditions":["flag:tam_c04_w09_started","score_gte:tam_hoang_interest:55"],"sort_order":1110,"messages":[
            {"id":"m01","sender":"hoang","text":"Thứ Sáu anh để một chỗ. Nếu em không tới, báo anh trước chiều nhé.","time":"07:08"},
            {"id":"m02","sender":"player","text":"Anh nói như đặt bàn vậy.","time":"07:10"},
            {"id":"m03","sender":"hoang","text":"Đặt chỗ thôi. Không đặt em.","time":"07:11"}],"effects_on_read":{"flags":["read_tam_c04_w09_hoang_kept_place"]}},
        "tam_c04_w09_huyen_clean_file": {"id":"tam_c04_w09_huyen_clean_file","type":"chat","contact_id":"huyen","title":"Huyền","unlock_conditions":["flag:tam_c04_w09_started"],"sort_order":1100,"messages":[
            {"id":"m01","sender":"huyen","text":"File tao gửi hôm qua không có một comment đỏ nào.","time":"06:44"},
            {"id":"m02","sender":"player","text":"Chúc mừng hay chia buồn?","time":"06:45"},
            {"id":"m03","sender":"huyen","text":"Chưa biết. Hơi thiếu cảm giác được quan tâm.","time":"06:46"}],"effects_on_read":{"flags":["read_tam_c04_w09_huyen_clean_file"]}},
        "tam_c04_w09_quang_deleted_message": {"id":"tam_c04_w09_quang_deleted_message","type":"chat","contact_id":"quang","title":"Quang","unlock_conditions":["flag:tam_c04_w09_started"],"sort_order":1105,"messages":[
            {"id":"m01","sender":"quang","text":"Tin lúc nãy anh gửi nhầm.","time":"08:02"},
            {"id":"m02","sender":"player","text":"Nhầm người hay nhầm câu?","time":"08:04"},
            {"id":"m03","sender":"quang","text":"Anh đang nghĩ.","time":"08:06"}],"effects_on_read":{"flags":["read_tam_c04_w09_quang_deleted_message"]}},
    })
    PHONE_REPLY_CHOICES.update({
        "tam_c04_w09_hoang_kept_place":[
            {"id":"confirm_place","text":"Em sẽ báo rõ. Đừng tự đoán.","once":True,"effects":{"story_add":{"tam_hoang_interest":1,"hoang_tam_trust":1},"flags":["tam_c04_w09_phone_confirms_hoang_place"]},"response_messages":[{"id":"r01","sender":"hoang","text":"Được. Anh giữ đúng phần của anh.","time":"07:13"}]},
            {"id":"ask_if_disappointed","text":"Nếu em không tới, anh có thất vọng không?","once":True,"effects":{"story_add":{"hoang_tam_trust":1,"hoang_self_acceptance":1},"flags":["tam_c04_w09_phone_asks_hoang_disappointed"]},"response_messages":[{"id":"r01","sender":"hoang","text":"Có. Nhưng thất vọng không phải lý do để ép em tới.","time":"07:13"}]},],
        "tam_c04_w09_huyen_clean_file":[
            {"id":"tell_huyen_earned_it","text":"Không bị sửa vì mày làm đúng.","once":True,"effects":{"story_add":{"career_huyen":1,"huyen_quan_trust":1},"flags":["tam_c04_w09_phone_tells_huyen_earned_it"]},"response_messages":[{"id":"r01","sender":"huyen","text":"Tao biết. Nghe vẫn lạ.","time":"06:48"}]},
            {"id":"tease_attention","text":"Thiếu mực đỏ hay thiếu người cầm bút?","once":True,"effects":{"story_add":{"huyen_quan_interest":1},"flags":["tam_c04_w09_phone_teases_huyen_attention"]},"response_messages":[{"id":"r01","sender":"huyen","text":"Block mày bây giờ.","time":"06:48"}]},],
        "tam_c04_w09_quang_deleted_message":[
            {"id":"redirect_an","text":"Gửi đúng cho chị An đi.","once":True,"effects":{"story_add":{"thienan_quang_trust":1,"quang_persistence":1},"tam_c04_extended_story_add":{"quang_thienan_resolve":1},"flags":["tam_c04_w09_phone_redirects_quang_an"]},"response_messages":[{"id":"r01","sender":"quang","text":"Ừ. Lần này anh tự nói.","time":"08:08"}]},
            {"id":"ask_first_reflex","text":"Sao phản xạ đầu tiên vẫn là tìm em?","once":True,"effects":{"story_add":{"tam_quang_interest":1},"tam_c04_extended_story_add":{"quang_tam_warmth":1,"quang_tam_awareness":2},"flags":["tam_c04_w09_phone_asks_quang_reflex"]},"response_messages":[{"id":"r01","sender":"quang","text":"Vì anh quen. Anh biết đó chưa phải câu trả lời đủ.","time":"08:08"}]},],
    })
