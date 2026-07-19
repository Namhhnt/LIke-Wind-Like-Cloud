# FILE: game/story/tam/tam_c03_thienan_family/s00_thienan_intro.rpy
# Scene file.

label tam_c03_thienan_family_s00_thienan_intro:
    scene black
    with fade

    centered "{size=46}CHAPTER 03{/size}\n{size=30}Thiên An và gia đình{/size}"

    scene bg_tam_family_living_room_evening
    with dissolve

    $ story_flag('tam_c03_thienan_family_started')
    $ unlock_library_character("tam")
    $ unlock_library_character("thienan")
    $ unlock_character_section("tam", "fixed_relationships")
    $ unlock_character_section("thienan", "role")
    $ unlock_character_section("thienan", "public_identity")

    "Tối hôm đó, Tâm về nhà muộn hơn mọi khi."

    "Đèn phòng khách vẫn sáng."

    "Trên bàn trà, laptop của Thiên An đang mở. Một bảng tính dài kín màn hình, vài ô được tô đỏ, vài dòng ghi chú bị gạch ngang rồi viết lại."

    "Thiên An ngồi tựa trên sofa, đầu nghiêng sang một bên."

    "Cô chưa ngủ hẳn. Nhưng cũng không còn tỉnh táo."

    tam neutral "Chị An?"

    thienan tired "Ừ..."

    "Thiên An mở mắt. Mất một nhịp, ánh mắt cô mới lấy lại được tiêu cự."

    tam worried "Chị ngủ ở đây à?"

    thienan neutral "Chị định xem nốt vài báo cáo."

    tam confused "Vài báo cáo?"

    "Tâm nhìn xuống bàn."

    "Một tập hồ sơ dày. Hai cây bút. Một cốc nước đã cạn. Bên cạnh là vé máy bay in vội, mép giấy hơi cong lên."

    tam surprised "Chị lại đi công tác?"

    thienan tired "Sáng mai."

    tam worried "Gấp vậy ạ?"

    thienan neutral "Chi nhánh phía Nam đang có chút việc."

    "Thiên An nói rất nhẹ."

    "Nhẹ đến mức nếu không nhìn thấy những ô đỏ trên màn hình, Tâm có lẽ đã tin đó thật sự chỉ là 'chút việc'."

    tam melancholic "Có nghiêm trọng không?"

    thienan smile "Chưa đến mức em phải cau mày như vậy."

    tam embarrassed "Em đâu có..."

    thienan teasing "Có. Cau rất rõ."

    "Tâm đưa tay chạm lên trán mình theo phản xạ."

    "Thiên An nhìn động tác ấy, khóe môi khẽ cong. Nhưng nụ cười chỉ giữ được một thoáng rồi lặng xuống."

    thienan neutral "Chị xử lý được."

    "Một câu rất giống Thiên An."

    "Gọn. Chắc. Không để chừa chỗ cho người khác lo lắng."

    menu:
        "Tâm làm gì khi thấy Thiên An mệt như vậy?"

        "Lấy chăn mỏng đắp cho chị":
            $ story_flag('tam_supports_thienan')
            $ story_add('thienan_self_assertion', 1)
            $ story_add('tam_observation', 1)
            $ unlock_character_section("tam", "core_traits")
            $ unlock_character_section("thienan", "inner_layer")

            "Tâm không hỏi thêm."

            "Cô đi vào phòng, lấy một chiếc chăn mỏng rồi quay lại đặt lên vai Thiên An."

            thienan surprised "Tâm."

            tam shy "Đừng nhìn em như vậy. Em chỉ sợ chị cảm lạnh thôi."

            "Thiên An nhìn chiếc chăn trên vai mình."

            "Rất lâu sau, cô khẽ kéo nó lại cho ngay."

            thienan smile "Ừ. Cảm ơn em."

        "Đóng laptop giúp chị":
            $ story_flag('tam_noticed_thienan_overwork')
            $ story_add('tam_observation', 2)
            $ story_add('career_tam', 1)
            $ unlock_character_section("tam", "narrative_function")
            $ unlock_character_section("thienan", "core_traits")

            "Tâm nhìn màn hình thêm một lúc, rồi đưa tay gập laptop xuống."

            thienan confused "Em làm gì đấy?"

            tam neutral "Nếu chị còn nhìn nữa thì sáng mai sẽ đau đầu."

            thienan neutral "Chị còn chưa lưu."

            tam smile "Em thấy góc màn hình có chữ autosaved."

            "Thiên An khựng lại."

            "Rồi cô bật cười rất khẽ."

            thienan tired "Quan sát cũng khá đấy."

        "Lặng lẽ để chị tự quyết định":
            $ story_add('tam_insecurity', 1)
            $ story_add('family_pressure_thienan', 1)
            $ story_flag('tam_kept_distance_from_thienan_pressure')
            $ unlock_character_section("thienan", "public_identity")

            "Tâm mím môi."

            "Cô muốn nói gì đó, nhưng cuối cùng chỉ kéo chiếc ghế nhỏ lại gần bàn trà."

            tam neutral "Vậy... chị nhớ ngủ sớm."

            thienan smile "Ừ. Chị biết rồi."

            "Thiên An nói như thể thật sự biết."

            "Nhưng tay cô lại mở laptop lên lần nữa."

    "Ngoài cửa sổ, tiếng xe đêm đi qua rất khẽ."

    "Tâm bỗng nhận ra, có những người trong nhà càng giỏi thì càng khiến người khác khó biết nên giúp họ bằng cách nào."

    return
