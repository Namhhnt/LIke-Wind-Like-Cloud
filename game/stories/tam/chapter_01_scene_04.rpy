# Chapter 01, Scene 04

label tam_c01_year_end_after_meeting:

    scene bg_company_year_end_party_late
    with dissolve

    narrator "Đêm ấy, khi buổi tiệc dần trôi về cuối, Tâm đứng cạnh cửa kính nhìn xuống thành phố."

    narrator "Những dòng xe nhỏ như những vệt sáng nối nhau đi qua dưới chân tòa nhà."

    huyen neutral "Sao?"

    tam neutral "Sao gì?"

    huyen smile "Dự án phụ."

    tam embarrassed "Mày gọi người ta là dự án phụ thêm lần nữa, tao sẽ nộp mày cho phòng quản lý chất lượng."

    huyen serious "Tao chỉ đang đánh giá rủi ro."

    tam surprised "Rủi ro gì?"

    huyen serious "Rủi ro mày thích người ta trước khi kịp hiểu người ta là ai."

    narrator "Tâm quay đi."

    narrator "Má cô hơi nóng. Có lẽ vì rượu trái cây."

    narrator "Có lẽ không."

    if "huyen_trust_high_c01" in progress["player_flags"]:
        huyen serious "Nhưng nếu có gì thật, nhớ nói tao."
        huyen smile "Tao không hứa khuyên đúng. Nhưng tao hứa sẽ nghe trước khi phán xét."
        tam smile "Nghe trưởng thành ghê."
        huyen happy "Tao diễn đấy. Nhưng cũng có tâm."

    narrator "Tâm khẽ cười."

    narrator "Cô không biết cuộc gặp ngắn ngủi vừa rồi sẽ dẫn mình đến đâu."

    narrator "Cô chỉ biết, trong một ngày cuối năm đầy tiếng người và ánh đèn, có một ánh mắt đã dừng lại nơi cô lâu hơn một nhịp."

    narrator "Và đôi khi, một nhịp thôi cũng đủ làm gió đổi chiều."

    jump tam_c01_end
