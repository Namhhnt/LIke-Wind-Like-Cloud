label tam_c02_company_party_shopping_area_menu:
    scene bg_company_lobby_afternoon
    with dissolve

    "Shopping Area buổi tối đông vừa đủ."

    "Đèn trong các cửa hàng sáng lên thành từng ô vuông ấm, phản chiếu trên nền gạch bóng."

    "Tâm và Huyền đi cạnh nhau, không vội."

    "Lương đầu tiên trong tài khoản khiến mỗi chiếc váy treo sau lớp kính đều có vẻ biết nói hơn bình thường."

    huyen neutral "Mục tiêu hôm nay: mua đồ đi tiệc."

    tam neutral "Mục tiêu của tao: không phá sản."

    huyen teasing "Một mục tiêu thiếu tham vọng nhưng đáng tôn trọng."

    "Họ dừng trước một cửa hàng thời trang nữ."

    "Bên trái là khu váy áo công sở, màu sắc nhã, form gọn, nhìn qua đã thấy an toàn."

    "Bên phải là một chiếc váy dự tiệc được đặt riêng trên mannequin."

    "Vải rủ mềm. Đường cắt tinh tế. Không quá lộ, nhưng đủ làm người khác phải nhìn lần thứ hai."

    "Tâm nhìn giá tiền."

    "Rồi im lặng."

    huyen neutral "Đẹp."

    tam neutral "Đắt."

    huyen smile "Hai khái niệm này thường thân nhau."

    "Tâm nhìn chiếc váy thêm một chút."

    "Nếu chỉ tính tháng lương đầu tiên, cô không nên mua nó."

    "Nhưng nếu cộng cả khoản thưởng nhỏ từ vòng phỏng vấn xuất sắc..."

    if story_has_flag('tam_perfect_interview'):
        "Tâm chợt nhớ đến khoản bonus nhỏ được cộng thêm sau vòng phỏng vấn."

        "Không nhiều."

        "Nhưng vừa đủ để biến chiếc váy kia từ 'đừng mơ' thành 'có thể cân nhắc nếu tháng này sống tiết kiệm'."

        huyen teasing "Mày đang tính toán đúng không?"

        tam embarrassed "Mặt tao lộ vậy à?"

        huyen grinning "Mặt mày đang mở Excel trong đầu."

    else:
        "Tâm nhìn lại giá tiền lần nữa."

        "Không cần tính quá lâu."

        "Tháng này cô chưa đủ thoải mái để mua một thứ đẹp đến mức khiến ví tiền muốn xin nghỉ việc."

        huyen neutral "Đừng nhìn nữa. Nhìn lâu nó cũng không tự giảm giá đâu."

        tam tired "Tao biết."

    menu:
        "Tâm chọn mua gì?"

        "Váy áo công sở":
            $ story_add('career_tam', 2)
            $ story_add('tam_self_clarity', 1)
            $ story_flag('tam_c02_outfit_office_elegant')
            $ story_flag('tam_c02_bought_office_clothes')

            "Tâm bước sang khu váy áo công sở."

            "Cô chọn một chiếc váy màu nhã, dáng gọn, phần eo vừa vặn."

            "Không quá nổi bật."

            "Nhưng khi mặc thử, cô thấy vai mình thẳng hơn một chút."

            huyen neutral "Ừm."

            tam confused "Sao?"

            huyen smile "Không tệ. Nhìn như người có thể sống sót qua probation."

            tam tired "Đó là lời khen à?"

            huyen grinning "Rất cao cấp."

            "Tâm nhìn mình trong gương."

            "Chiếc váy không biến cô thành ai khác."

            "Chỉ làm cô trông giống một phiên bản đã chuẩn bị tốt hơn của chính mình."

            "Vậy là đủ."

            tam smile "Tao lấy bộ này."

            huyen happy "Quyết định sáng suốt. Ví tiền của mày vừa thở phào."

        "Váy dự tiệc sang trọng" if story_has_flag('tam_perfect_interview'):
            $ story_add('tam_hoang_interest', 3)
            $ story_add('hoang_tam_trust', 2)
            $ story_add('tam_self_clarity', 2)
            $ story_flag('tam_c02_outfit_party_elegant')
            $ story_flag('tam_c02_bought_luxury_party_dress')
            $ story_flag('tam_c02_hoang_approaches_due_to_dress')

            "Tâm đứng trước chiếc váy dự tiệc thêm vài giây."

            "Cô không phải kiểu người dễ tiêu tiền vì một khoảnh khắc bốc đồng."

            "Nhưng có những thứ không chỉ là vải vóc."

            "Chúng giống một lời nhắc nhỏ rằng cô cũng có quyền bước vào một căn phòng mà không phải co mình lại."

            tam neutral "Tao thử chiếc này."

            huyen surprised "Chiếc này á?"

            tam embarrassed "Ừ."

            huyen smile "Ồ."

            tam confused "Sao?"

            huyen teasing "Không có gì. Tao chỉ đang chứng kiến một nhân viên mới dùng tháng lương đầu tiên để tuyên chiến với ánh đèn tiệc."

            tam tired "Mày nói như phim quá."

            huyen grinning "Chiếc váy này xứng đáng có trailer."

            "Nhân viên cửa hàng kéo rèm phòng thử đồ lại."

            "Một lúc sau, Tâm bước ra."

            "Huyền đang nghịch điện thoại."

            "Cô ngẩng lên."

            "Rồi im hẳn."

            tam embarrassed "Sao?"

            huyen neutral "Đợi tao kiểm tra lại xem đây có phải bạn thân tao không."

            tam flustered "Đừng làm quá."

            huyen smile "Không. Lần này không làm quá."

            "Tâm quay sang gương."

            "Chiếc váy ôm vừa vặn, phần vai và eo được cắt rất khéo. Không phô trương, nhưng mỗi đường nét đều có chủ ý."

            "Cô vẫn là mình."

            "Chỉ là đứng thẳng hơn."

            "Và khó bị bỏ qua hơn."

            huyen neutral "Mua đi."

            tam neutral "Đắt."

            huyen smile "Nhưng không phí."

            "Tâm nhìn giá tiền thêm một lần."

            "Rồi cô thở ra."

            tam smile "Ừ. Tao lấy chiếc này."

            "Lúc nhân viên gấp chiếc váy vào hộp, Tâm nhìn dải ruy băng được kéo qua nắp giấy."

            "Một tiếng sột soạt nhỏ."

            "Nhưng nghe rất giống tiếng một cánh cửa vừa mở."

        "Váy dự tiệc sang trọng" if not story_has_flag('tam_perfect_interview'):
            $ story_add('tam_insecurity', 1)
            $ story_flag('tam_c02_luxury_dress_seen_but_unaffordable')

            "Tâm nhìn chiếc váy dự tiệc."

            "Rồi nhìn giá tiền."

            "Một phép tính rất ngắn chạy qua đầu."

            "Kết quả không đẹp bằng chiếc váy."

            tam neutral "Thôi."

            huyen neutral "Ừ."

            "Lần này Huyền không trêu."

            "Điều đó khiến Tâm hơi ngạc nhiên."

            huyen smile "Không phải hôm nay thì hôm khác."

            tam neutral "Tao biết."

            huyen neutral "Và bộ công sở bên kia cũng đẹp."

            tam smile "Ừ. Tao thử bộ đó."

            "Tâm rời mắt khỏi chiếc váy."

            "Không đến mức buồn."

            "Chỉ hơi tiếc."

            "Một chút tiếc nhỏ, đủ để cô nhớ rằng có những thứ mình chưa mua được."

            "Và cũng đủ để cô muốn sau này mua bằng cảm giác nhẹ nhàng hơn."

            jump tam_c02_company_party_shopping_area_menu_office_fallback

    return


label tam_c02_company_party_shopping_area_menu_office_fallback:
    $ story_add('career_tam', 2)
    $ story_add('tam_self_clarity', 1)
    $ story_flag('tam_c02_outfit_office_elegant')
    $ story_flag('tam_c02_bought_office_clothes')

    "Tâm chọn một chiếc váy công sở màu nhã."

    "Dáng váy gọn, đường may sạch, đủ lịch sự cho công ty và đủ mềm để không khiến cô trông như vừa bước ra từ file quy trình."

    huyen smile "Bộ này hợp."

    tam neutral "Thật à?"

    huyen teasing "Ừ. Nhìn có trách nhiệm, nhưng chưa tới mức làm người khác muốn nộp báo cáo."

    tam tired "Cảm ơn lời khen kỳ lạ của mày."

    "Tâm nhìn mình trong gương."

    "Không phải lựa chọn rực rỡ nhất."

    "Nhưng là lựa chọn cô có thể trả tiền mà không cần thở dài quá sâu."

    tam smile "Tao lấy bộ này."

    return