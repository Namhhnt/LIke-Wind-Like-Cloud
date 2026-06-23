Rồi Sir. Đây là bản **Ren’Py script cho Chapter 2 — Buổi tiệc công ty**, viết theo cấu trúc chapter/label/unlock hiện tại của project: mỗi chapter cần metadata trong `CHAPTERS`, label trùng tên, kết bằng `complete_chapter()` rồi quay về `route_map`; các choice/flag/unlock cũng bám theo guide progression đang có. 
Giọng cảnh giữ hướng “đời thường có dư vị”: thoại ngắn, có trêu, có né, dùng chi tiết nhỏ để mở cảm xúc thay vì bắt nhân vật tự diễn giải quá sạch.  Hoàng được viết theo trục ấm, dễ gần, có duyên xã hội nhưng vẫn phòng thủ nhẹ khi bị tiếp cận. 

---

## 1. Metadata đề xuất — `game/progression_data.rpy`

```renpy
# Add / update inside CHAPTERS.

"tam_c02": {
    "id": "tam_c02",
    "route": "tam",
    "type": "core",
    "timeline_position": 20,
    "title": "Buổi tiệc công ty",
    "label": "tam_c02",
    "prerequisites": ["tam_c01"],
    # tam_c03 always opens after Chapter 2.
    # hoang_h01 is unlocked conditionally inside the chapter when interaction is sufficient.
    "unlocks": ["tam_c03"],
},

"hoang_h01": {
    "id": "hoang_h01",
    "route": "hoang",
    "type": "pov",
    "timeline_position": 21,
    "title": "First Impression",
    "label": "hoang_h01",
    "prerequisites": ["tam_c02"],
    "unlocks": [],
    # Optional: keep this hidden until Chapter 2 explicitly marks enough interaction.
    # If your progression logic supports player flag conditions, use:
    # "required_flags": ["unlock_hoang_h01"],
},
```

---

## 2. Script — `game/tam_c02_company_party.rpy`

```renpy
# ============================================================
# CHAPTER 2 — BUỔI TIỆC CÔNG TY
# Route: Tâm
# POV: Tâm, optional short Hoàng POV when interaction is sufficient
# ============================================================

# ------------------------------------------------------------
# Character aliases
# Remove these if already defined elsewhere.
# ------------------------------------------------------------

# define tam = Character("Tâm")
# define huyen = Character("Huyền")
# define hoang = Character("Hoàng")
# define quan = Character("Quân")
# define coworker = Character("Đồng nghiệp")
# define narrator = Character(None)

# ------------------------------------------------------------
# Chapter relationship variables
# Keep these defaults in one central variable file if preferred.
# ------------------------------------------------------------

default tam_hoang_interest = 0
default hoang_notices_tam = 0
default huyen_hoang_interest = 0

default trust_tam_hoang = 0
default intimacy_tam_hoang = 0
default hoang_tam_interest = 0
default career_tam = 0

default trust_hoang_huyen = 0

default tam_direction = ""
default hoang_direction = ""
default huyen_direction = ""

default tam_c02_party_route = ""
default tam_c02_direct_approach = False
default tam_c02_hoang_pov_unlocked = False


# ------------------------------------------------------------
# Safe helper functions
# These are defensive wrappers so the chapter does not break
# if the project has not finalized exact unlock function names.
# ------------------------------------------------------------

init python:

    def tg_add_unique(target_list, value):
        if value not in target_list:
            target_list.append(value)

    def tg_set_player_flag(flag):
        try:
            if "progress" in globals() and isinstance(progress, dict):
                if "player_flags" not in progress:
                    progress["player_flags"] = []

                if "add_unique" in globals():
                    add_unique(progress["player_flags"], flag)
                else:
                    tg_add_unique(progress["player_flags"], flag)
        except Exception:
            pass

    def tg_unlock_chapter(chapter_id):
        """
        Soft unlock helper.
        Replace this with your real unlock_chapter(chapter_id)
        if progression_logic.rpy already provides one.
        """
        try:
            if "unlock_chapter" in globals():
                unlock_chapter(chapter_id)
                return

            if "progress" in globals() and isinstance(progress, dict):
                for key in ["unlocked", "unlocked_chapters", "available_chapters"]:
                    if key in progress and isinstance(progress[key], list):
                        tg_add_unique(progress[key], chapter_id)
                        return

                progress["unlocked_chapters"] = [chapter_id]
        except Exception:
            pass

    def tg_set_direction(owner, direction_value):
        """
        Optional bridge for relationship direction tracking.
        The normal variables below are still the source used by this chapter.
        """
        try:
            if "progress" in globals() and isinstance(progress, dict):
                if "relationship_directions" not in progress:
                    progress["relationship_directions"] = {}

                if owner not in progress["relationship_directions"]:
                    progress["relationship_directions"][owner] = []

                tg_add_unique(progress["relationship_directions"][owner], direction_value)
        except Exception:
            pass


# ============================================================
# MAIN LABEL
# ============================================================

label tam_c02:

    $ tam_c02_party_route = ""
    $ tam_c02_direct_approach = False
    $ tam_c02_hoang_pov_unlocked = False

    scene black with fade

    "CHAPTER 2 — Buổi tiệc công ty"

    call tam_c02_onboarding
    call tam_c02_quan_intro
    call tam_c02_party_opening
    call tam_c02_pre_hoang_choice

    jump tam_c02_main_choice


# ============================================================
# COMMON INTRO — TÂM AND HUYỀN START WORKING
# ============================================================

label tam_c02_onboarding:

    scene black with fade

    "Ngày đầu đi làm của Tâm bắt đầu bằng một chiếc thẻ nhân viên còn mới cứng, một chồng tài liệu onboarding, và nụ cười của Huyền trông tự tin hơn thực tế khoảng ba mươi phần trăm."

    show tam neutral at left
    show huyen smile at right
    with dissolve

    huyen "Mày thấy chưa? Công ty nhìn nghiêm túc ghê."

    show tam thoughtful

    tam "Ừ. Nghiêm túc tới mức tao vừa thở mạnh cũng thấy hơi có lỗi."

    show huyen laugh

    huyen "Tốt. Ít nhất mày còn biết thở."

    show tam embarrassed

    tam "Mày động viên kiểu đó hơi tiết kiệm quá đấy."

    "Huyền cười, chỉnh lại dây đeo thẻ cho Tâm. Miếng nhựa trong hơi lệch, mắc vào mép cổ áo."

    show huyen smile

    huyen "Đứng yên."

    show tam confused

    tam "Sao?"

    huyen "Thẻ lệch. Nhân viên mới mà để thẻ lệch là nhìn giống người bị bắt đi làm."

    show tam smile

    "Tâm cúi xuống nhìn. Cái thẻ nhỏ nằm ngay ngắn lại trên ngực áo."

    tam "Cảm ơn."

    huyen "Không có gì. Mai tao thu phí."

    hide tam
    hide huyen
    with dissolve

    "Cả hai đi qua tuần đầu tiên bằng những buổi training nối nhau, những email chưa kịp đọc hết, và những cái gật đầu hơi nhanh mỗi khi có người hỏi: \"Hiểu chưa?\""

    "Tâm hiểu khoảng bảy mươi phần trăm."

    "Ba mươi phần trăm còn lại, cô ghi vào sổ."

    return


# ============================================================
# QUÂN INTRO — RUMORS
# ============================================================

label tam_c02_quan_intro:

    scene black with fade

    "Tên Quân xuất hiện trước cả con người thật của anh."

    show tam neutral at left
    show huyen neutral at right
    with dissolve

    coworker "Hai em vào team anh Quân à?"

    show huyen confused

    huyen "Vâng ạ. Có vấn đề gì không chị?"

    coworker "Không. Nếu chịu được thì tốt."

    show tam surprised
    show huyen surprised

    tam "Chị nói thế nghe hơi giống cảnh báo thiên tai."

    coworker "Không đến mức đó. Anh ấy giỏi thật. Làm việc rất chắc. Nhưng soi kỹ, ít khen, không thích ai làm màu."

    show huyen thoughtful

    huyen "Ít khen là ít thế nào ạ?"

    coworker "Nếu anh ấy nói \"được\", tức là tốt. Nếu nói \"tạm\", tức là nên sửa. Nếu im lặng..."

    show tam confused

    tam "Tức là?"

    coworker "Tức là tự hiểu."

    show huyen embarrassed

    huyen "Hay thật. Công ty mình tiết kiệm cả lời khen."

    hide tam
    hide huyen
    with dissolve

    "Tâm nhớ câu đó rất lâu."

    "Không phải vì sợ."

    "Chỉ là trong môi trường mới, có những người chưa cần xuất hiện đã khiến không khí tự biết cách thẳng lưng."

    scene black with fade

    show quan serious at center
    with dissolve

    "Quân xuất hiện vào sáng thứ Hai kế tiếp."

    "Áo sơ mi phẳng, tay áo xắn gọn, mắt nhìn màn hình nhiều hơn nhìn người."

    quan "Chào hai em. Anh là Quân, trưởng phòng."

    quan "Trong team này, anh không cần ai chứng minh mình thông minh bằng cách nói nhiều."

    show quan neutral

    quan "Làm được thì để kết quả nói. Không rõ thì hỏi. Sai thì sửa. Đừng giấu."

    "Anh dừng một nhịp, nhìn qua Tâm rồi đến Huyền."

    show quan serious

    quan "Và đừng làm màu. Màu đẹp mấy cũng không cứu được deadline."

    hide quan with dissolve

    scene black

    show huyen confused at right
    show tam thoughtful at left
    with dissolve

    huyen "Tao rút lại. Đây không phải tiết kiệm lời khen."

    tam "Ừ."

    show huyen serious

    huyen "Đây là cắt giảm ngân sách cảm xúc."

    show tam smile

    "Tâm bật cười rất khẽ. Cười xong lại cúi xuống ghi thêm một dòng vào sổ."

    "\"Không giấu.\""

    return


# ============================================================
# PARTY OPENING
# ============================================================

label tam_c02_party_opening:

    scene black with fade

    "Buổi tiệc công ty diễn ra sau giai đoạn onboarding."

    "Nói là tiệc, nhưng với Tâm, nó giống một bài kiểm tra xã giao được trang trí bằng đèn vàng, ly thủy tinh và những khay đồ ăn nhỏ đến mức phải ăn ba lần mới biết mình vừa ăn gì."

    show tam neutral at left
    show huyen happy at right
    with dissolve

    huyen "Đồ ăn đẹp ghê."

    show tam confused

    tam "Ừ. Đẹp tới mức tao không chắc mình có được phép ăn không."

    show huyen laugh

    huyen "Mày cứ ăn đi. Nếu bị phạt tao làm chứng là nó tự nhảy vào đĩa."

    show tam smile

    "Tâm cầm chiếc đĩa nhỏ. Trên đó có một miếng bánh mặn đặt hơi lệch, nước sốt kéo thành một vệt mỏng ở mép sứ."

    "Cô lấy khăn giấy lau nhẹ mép đĩa."

    show huyen surprised

    huyen "Trời. Mày đi tiệc hay đi kiểm tra vệ sinh an toàn thực phẩm?"

    show tam embarrassed

    tam "Nó lệch."

    huyen "Mày mới đi làm một tuần đã bị anh Quân nhập rồi à?"

    show tam pouty

    tam "Đừng nói gở."

    hide tam
    hide huyen
    with dissolve

    "Ở phía bên kia phòng, Quân đang nói chuyện với một người đàn ông trẻ lạ mặt."

    "Người đó mặc áo sơ mi sáng màu dưới một chiếc blazer tối giản. Dáng đứng thoải mái, không cố chiếm chỗ, nhưng lạ là vẫn khiến người khác vô thức nhìn qua."

    show huyen neutral at right
    show tam neutral at left
    with dissolve

    huyen "Ê."

    show tam confused

    tam "Gì?"

    huyen "Người đứng với anh Quân ấy. Khách à?"

    show tam thoughtful

    tam "Chắc vậy."

    coworker "À, đó là Hoàng. Thiết kế kiến trúc. Bên mình đang mời hợp tác một dự án cải tạo không gian làm việc."

    show huyen surprised

    huyen "Trẻ vậy á?"

    coworker "Trẻ nhưng có năng lực. Nghe nói quen anh Quân từ trước."

    show tam neutral

    "Tâm nhìn sang lần nữa."

    "Đúng lúc đó, Hoàng hơi nghiêng đầu cười với điều Quân vừa nói. Nụ cười rất nhẹ, không ồn, nhưng làm vẻ khó gần của Quân dịu xuống một chút."

    show tam thoughtful

    "Tâm thấy lạ."

    "Không phải vì anh nổi bật nhất phòng."

    "Mà vì anh trông như người biết cách đứng cạnh một người khó tính mà không làm không khí khó chịu hơn."

    return


# ============================================================
# SMALL DETAIL BEFORE MAIN CHOICE
# Determines hoang_notices_tam.
# ============================================================

label tam_c02_pre_hoang_choice:

    show tam neutral at left
    show huyen neutral at right
    with dissolve

    "Một nhân viên đi ngang qua, khuỷu tay khẽ chạm vào chiếc bàn cocktail gần Tâm."

    "Ly nước trên mép bàn lắc nhẹ."

    menu:
        "Tâm phản ứng thế nào?"

        "Kéo ly nước vào trong, không nói gì.":
            $ hoang_notices_tam += 1

            show tam neutral
            "Tâm đưa tay kéo chiếc ly vào sát giữa bàn."

            "Động tác rất nhỏ. Gần như không ai để ý."

            show huyen smile

            huyen "Mày cứu được một vụ tai nạn cấp độ nước cam."

            show tam smile

            tam "Tai nạn nhỏ cũng là tai nạn."

            "Ở phía bên kia phòng, Hoàng thoáng nhìn qua."

            "Ánh mắt anh dừng lại chưa tới một giây rồi quay đi."

        "Nhắc Huyền tránh ra.":
            show tam surprised

            tam "Huyền, cẩn thận."

            show huyen confused

            huyen "Hả?"

            "Chiếc ly đứng lại sau một nhịp lắc nhẹ."

            show huyen smile

            huyen "May. Váy tao chưa cần uống nước cam."

        "Không để ý, tiếp tục nghe mọi người nói chuyện.":
            "Tâm đang mải nghe một chị cùng team kể về những lần anh Quân sửa proposal."

            "Khi cô quay lại, chiếc ly đã được ai đó đẩy vào trong từ lúc nào."

    scene black with dissolve

    "Tiếng cười, tiếng chạm ly, tiếng giày di chuyển trên sàn gỗ hòa vào nhau thành một lớp âm thanh mỏng."

    "Tâm tự nhắc mình đây chỉ là một buổi tiệc công ty."

    "Không nên làm quá."

    return


# ============================================================
# MAIN CHOICE
# ============================================================

label tam_c02_main_choice:

    scene black with fade

    show tam thoughtful at left
    show huyen neutral at right
    with dissolve

    "Hoàng vừa tách khỏi nhóm của Quân."

    "Anh đứng gần khu bàn đồ uống, một tay cầm ly nước, mắt nhìn lướt qua không gian như đang tính xem nên ở lại thêm bao lâu cho đủ lịch sự."

    show huyen smile

    huyen "Mày nhìn người ta ba lần rồi đấy."

    show tam surprised

    tam "Có à?"

    huyen "Có. Lần thứ ba còn có vẻ nghiên cứu học thuật."

    show tam embarrassed

    tam "Tao chỉ tò mò thôi."

    huyen "Ừ. Tò mò cũng là một ngành khoa học."

    menu:
        "Tâm sẽ làm gì?"

        "Chủ động bắt chuyện với Hoàng.":
            $ tam_c02_direct_approach = True
            $ tam_hoang_interest += 1
            jump tam_c02_route_a

        "Không chủ động. Đứng cùng Huyền thêm một lúc.":
            if hoang_notices_tam >= 1:
                jump tam_c02_route_b
            else:
                jump tam_c02_route_c

        "Đẩy Huyền lên nói chuyện với Hoàng.":
            $ huyen_hoang_interest += 1
            jump tam_c02_route_d

        "Né xã giao, tập trung nói chuyện công việc rồi rời tiệc sớm.":
            jump tam_c02_route_c


# ============================================================
# ROUTE A — CANON SEED: TÂM BẮT CHUYỆN
# Condition: tam_hoang_interest >= 1 OR direct approach
# Effects:
# +2 trust_tam_hoang
# +1 intimacy_tam_hoang
# set tam_direction = tam_hoang_open
# unlock hoang_h01_first_impression
# ============================================================

label tam_c02_route_a:

    $ tam_c02_party_route = "A"
    $ trust_tam_hoang += 2
    $ intimacy_tam_hoang += 1
    $ tam_direction = "tam_hoang_open"
    $ tg_set_direction("tam", "tam_hoang_open")
    $ tg_set_player_flag("hoang_h01_first_impression")
    $ tg_set_player_flag("unlock_hoang_h01")
    $ tg_unlock_chapter("hoang_h01")
    $ tam_c02_hoang_pov_unlocked = True

    scene black with fade

    show tam thoughtful at left
    show huyen smile at right
    with dissolve

    huyen "Đi đi."

    show tam confused

    tam "Đi đâu?"

    huyen "Đi hỏi ngành kiến trúc có bao gồm việc đứng đẹp ở bàn nước không."

    show tam embarrassed

    tam "Mày bớt sáng tạo giùm tao."

    show huyen laugh

    huyen "Không. Đây là tài sản nghề nghiệp."

    "Tâm nhìn sang Hoàng."

    "Anh đang đặt chiếc ly xuống bàn. Ngón tay gõ nhẹ vào thành ly một lần, rồi dừng."

    "Có vẻ anh cũng không thật sự thích đứng một mình giữa tiệc."

    show tam serious

    "Tâm hít vào một hơi rất khẽ."

    hide huyen with dissolve

    show tam neutral at left
    show hoang neutral at right
    with dissolve

    tam "Xin chào. Anh là anh Hoàng đúng không ạ?"

    show hoang surprised

    hoang "À... đúng rồi."

    show hoang smile

    hoang "Còn em là nhân viên mới?"

    show tam smile

    tam "Vâng. Em là Tâm. Người đang cố ăn đồ tiệc mà không làm rơi nước sốt lên hồ sơ nhân sự."

    show hoang confused

    "Hoàng khựng một nhịp."

    show hoang smile

    hoang "Nghe có vẻ em đang thắng."

    show tam embarrassed

    tam "Tạm thời thôi ạ. Em chưa muốn chủ quan."

    show hoang neutral

    "Hoàng nhìn chiếc đĩa nhỏ trong tay cô. Mép đĩa sạch quá mức cần thiết."

    hoang "Em lau đĩa à?"

    show tam surprised

    tam "Anh thấy ạ?"

    show hoang smile

    hoang "Ừ. Khá khó để bỏ qua một người dự tiệc với tinh thần kiểm định chất lượng như vậy."

    show tam pouty

    tam "Em bắt đầu thấy câu đó không giống lời khen."

    hoang "Không hẳn."

    show hoang thoughtful

    hoang "Chỉ là... anh thấy yên tâm. Người để ý những thứ nhỏ thường ít làm hỏng việc lớn."

    show tam surprised

    "Tâm hơi ngẩn ra."

    "Câu đó được nói rất bình thường. Không có ý tán tỉnh. Cũng không cố tỏ ra sâu sắc."

    "Nhưng vì thế mà nó nghe thật hơn."

    show tam smile

    tam "Anh nói vậy trước mặt anh Quân chắc được cộng điểm."

    show hoang laugh

    hoang "Không đâu. Anh Quân sẽ hỏi tiêu chí đánh giá ở đâu ra."

    show tam happy

    tam "Đúng là nghe giống anh ấy."

    show hoang smile

    "Hoàng cười. Lần này vẻ phòng thủ ban đầu dịu xuống rõ hơn."

    hoang "Em mới vào mà đã nắm được tinh thần sinh tồn rồi."

    tam "Chưa ạ. Em vẫn đang trong giai đoạn đọc hướng dẫn sử dụng công ty."

    hoang "Có bản đó à?"

    show tam serious

    tam "Không. Nên em hơi lo."

    show hoang smile

    hoang "Vậy lời khuyên đầu tiên: nếu anh Quân nói \"được\", cứ xem như pháo hoa."

    show tam confused

    tam "Pháo hoa hơi... im lặng nhỉ."

    hoang "Đúng. Pháo hoa bản trưởng phòng."

    show tam laugh

    "Tâm bật cười."

    "Hoàng nhìn cô thêm một nhịp. Không lâu. Chỉ đủ để Tâm nhận ra rồi tự nhiên thấy mặt mình nóng lên."

    show tam embarrassed

    tam "Em cười hơi to à?"

    show hoang neutral

    hoang "Không."

    show hoang smile

    hoang "Phòng này cần người cười thật một chút."

    "Tâm cúi xuống nhìn chiếc đĩa trong tay."

    "Miếng bánh mặn đã nguội. Nhưng kỳ lạ là cô không còn thấy buổi tiệc này khó thở như lúc đầu nữa."

    jump tam_c02_after_routes


# ============================================================
# ROUTE B — HOÀNG CHỦ ĐỘNG
# Condition: hoang_notices_tam >= 1 AND Tâm không chủ động
# Effects:
# +1 trust_tam_hoang
# +1 hoang_tam_interest
# set hoang_direction = hoang_tam_open
# unlock tam_surprised_by_hoang
# ============================================================

label tam_c02_route_b:

    $ tam_c02_party_route = "B"
    $ trust_tam_hoang += 1
    $ hoang_tam_interest += 1
    $ hoang_direction = "hoang_tam_open"
    $ tg_set_direction("hoang", "hoang_tam_open")
    $ tg_set_player_flag("tam_surprised_by_hoang")
    $ tg_set_player_flag("unlock_hoang_h01")
    $ tg_unlock_chapter("hoang_h01")
    $ tam_c02_hoang_pov_unlocked = True

    scene black with fade

    show tam neutral at left
    show huyen smile at right
    with dissolve

    huyen "Mày không định qua à?"

    show tam thoughtful

    tam "Thôi. Người ta đang là khách mời, tự nhiên qua bắt chuyện cũng hơi kỳ."

    show huyen pouty

    huyen "Mày sống lịch sự tới mức làm tao mệt thay."

    show tam embarrassed

    tam "Mày có thể nghỉ."

    show huyen laugh

    "Huyền vừa định đáp lại thì ánh mắt cô dừng sau vai Tâm."

    show huyen surprised

    huyen "À. Hình như không cần nữa."

    show tam confused

    tam "Không cần gì?"

    hide huyen with dissolve

    show tam confused at left
    show hoang neutral at right
    with dissolve

    hoang "Xin lỗi, anh chen ngang được không?"

    show tam surprised

    tam "À... vâng."

    show hoang smile

    hoang "Anh là Hoàng."

    show tam neutral

    tam "Em là Tâm."

    show hoang thoughtful

    hoang "Anh thấy lúc nãy em kéo ly nước vào trong."

    show tam embarrassed

    tam "Chuyện đó... cũng không có gì đâu ạ."

    hoang "Ừ. Vì không có gì nên anh mới để ý."

    show tam confused

    "Tâm chớp mắt."

    "Hoàng nói câu đó xong cũng như nhận ra mình vừa nói hơi lạ. Anh nhìn sang chiếc bàn gần đó, rồi cười nhẹ."

    show hoang embarrassed

    hoang "Ý anh là... ở tiệc đông người, thường ai cũng để ý chuyện lớn. Ít người để ý mấy thứ sắp đổ."

    show tam smile

    tam "Em chỉ không muốn ai đó phải đi tìm khăn giấy thôi."

    show hoang smile

    hoang "Đó cũng là một lý do tốt."

    "Một khoảng im rất ngắn rơi xuống giữa hai người."

    "Không khó xử đến mức phải lảng đi. Nhưng cũng không đủ quen để đứng yên quá lâu."

    show tam thoughtful

    tam "Anh là kiến trúc sư ạ?"

    hoang "Gần vậy. Anh làm thiết kế kiến trúc và không gian."

    tam "Không gian làm việc bên em sắp được sửa lại ạ?"

    show hoang neutral

    hoang "Đang khảo sát thôi. Chưa chắc."

    show tam serious

    tam "Nếu sửa, anh có thể làm khu pantry bớt giống phòng chờ nha khoa không?"

    show hoang surprised

    "Hoàng nhìn cô."

    show tam embarrassed

    tam "Em nói hơi quá à?"

    show hoang laugh

    hoang "Không. Chính xác đến mức anh hơi đau nghề."

    show tam smile

    tam "Vậy là có hy vọng rồi."

    show hoang smile

    hoang "Có. Ít nhất là với pantry."

    "Tâm cúi xuống, dùng ngón tay giữ lại sợi dây thẻ đang xoay lệch."

    "Hoàng thấy động tác đó, nhưng không vạch trần."

    show hoang neutral

    hoang "Em mới vào công ty, chắc còn mệt."

    show tam surprised

    tam "Nhìn rõ vậy ạ?"

    show hoang smile

    hoang "Không rõ. Chỉ là anh đoán."

    tam "Anh đoán đúng."

    hoang "Vậy tối nay em cứ ăn nhiều một chút. Onboarding thường không ghi trong JD là sẽ làm người ta đói."

    show tam laugh

    "Tâm lại bật cười."

    "Lần này cô không kịp giữ nhỏ tiếng như thường ngày."

    jump tam_c02_after_routes


# ============================================================
# ROUTE C — KHÔNG GẶP GỠ ĐÁNG KỂ
# Condition: Tâm né xã giao / tập trung Huyền / rời tiệc sớm
# Effects:
# +1 career_tam
# -1 intimacy_tam_hoang
# set hoang_direction = hoang_friend_group_possible
# Hoàng and Tâm know each other, but not close.
# ============================================================

label tam_c02_route_c:

    $ tam_c02_party_route = "C"
    $ career_tam += 1
    $ intimacy_tam_hoang -= 1
    $ hoang_direction = "hoang_friend_group_possible"
    $ tg_set_direction("hoang", "hoang_friend_group_possible")
    $ tg_set_player_flag("tam_c02_no_significant_meeting")

    scene black with fade

    show tam thoughtful at left
    show huyen neutral at right
    with dissolve

    huyen "Không qua thật à?"

    show tam neutral

    tam "Thôi. Hôm nay tao muốn nhớ mặt mọi người trong team trước."

    show huyen smile

    huyen "Lý do nghe rất trưởng thành."

    tam "Mày đang chê à?"

    huyen "Không. Tao chỉ hơi bất ngờ khi bạn tao quyết định làm người lớn giữa một bàn bánh ngọt."

    show tam smile

    "Tâm mỉm cười, rồi quay lại nhóm đồng nghiệp phía sau."

    hide huyen
    hide tam
    with dissolve

    "Cô nói chuyện với hai chị trong team về quy trình review tài liệu."

    "Hỏi thêm về cách Quân thường góp ý."

    "Ghi nhớ tên vài người."

    "Có một lúc, Hoàng và Quân đi ngang qua nhóm của cô."

    show tam neutral at left
    show hoang neutral at right
    with dissolve

    quan "Đây là Tâm. Nhân viên mới của team anh."

    show tam smile

    tam "Em chào anh."

    show hoang smile

    hoang "Chào em. Anh là Hoàng."

    "Chỉ vậy."

    "Một cái gật đầu lịch sự."

    "Một nụ cười vừa đủ."

    "Rồi Quân dẫn Hoàng sang nhóm khác."

    hide hoang
    show tam thoughtful

    "Tâm nhìn theo một thoáng."

    "Cũng có thể nói chuyện thêm."

    "Nhưng điện thoại trong túi rung lên, Huyền đang nhắn hỏi cô có muốn về cùng không."

    show tam neutral

    "Tâm gõ trả lời:"

    tam "\"Có.\""

    scene black with fade

    "Buổi tiệc kết thúc với Tâm bằng một vài cái tên mới, một chút hiểu biết về văn hóa công ty, và cảm giác nhẹ nhõm vì mình chưa làm gì kỳ quặc."

    "Hoàng vẫn là người cô đã gặp."

    "Nhưng chưa phải người cô biết."

    jump tam_c02_after_routes


# ============================================================
# ROUTE D — HUYỀN TƯƠNG TÁC VỚI HOÀNG NHIỀU HƠN
# Condition: huyen_hoang_interest >= 1 OR Tâm pushes Huyền
# Effects:
# +2 trust_hoang_huyen
# +1 huyen_hoang_interest
# set huyen_direction = huyen_hoang_interest
# set tam_direction = tam_support_huyen
# ============================================================

label tam_c02_route_d:

    $ tam_c02_party_route = "D"
    $ trust_hoang_huyen += 2
    $ huyen_hoang_interest += 1
    $ huyen_direction = "huyen_hoang_interest"
    $ tam_direction = "tam_support_huyen"
    $ tg_set_direction("huyen", "huyen_hoang_interest")
    $ tg_set_direction("tam", "tam_support_huyen")
    $ tg_set_player_flag("tam_support_huyen")
    $ tg_set_player_flag("unlock_hoang_h01")
    $ tg_unlock_chapter("hoang_h01")
    $ tam_c02_hoang_pov_unlocked = True

    scene black with fade

    show tam smile at left
    show huyen confused at right
    with dissolve

    tam "Mày qua hỏi thử đi."

    show huyen surprised

    huyen "Hỏi gì?"

    tam "Hỏi ngành kiến trúc có thật sự giúp pantry bớt giống phòng chờ nha khoa không."

    show huyen pouty

    huyen "Câu đó của tao mà."

    tam "Thì tác giả nên tự chịu trách nhiệm với tác phẩm."

    show huyen embarrassed

    huyen "Mày đẩy tao hơi thẳng tay rồi đấy."

    show tam smile

    tam "Không sao. Tao đứng đây làm hậu phương đạo đức."

    show huyen confused

    huyen "Nghe càng không yên tâm."

    hide tam with dissolve

    show huyen neutral at left
    show hoang neutral at right
    with dissolve

    huyen "Xin chào. Anh là anh Hoàng đúng không ạ?"

    show hoang smile

    hoang "Ừ. Còn em là...?"

    huyen "Huyền. Nhân viên mới. Người đang có thắc mắc rất chính đáng về pantry."

    show hoang confused

    hoang "Pantry?"

    show huyen serious

    huyen "Vâng. Không gian nhỏ, ánh sáng trắng, ghế lạnh, đứng vào đó là tự nhiên nhớ lịch khám răng."

    show hoang surprised

    "Hoàng im một nhịp."

    show hoang laugh

    hoang "Mô tả đau thật."

    show huyen smile

    huyen "Em nói với tinh thần xây dựng."

    hoang "Anh tin. Rất sắc bén, nhưng có xây dựng."

    show huyen happy

    "Huyền cười, thoải mái hơn hẳn."

    show tam smile at farleft
    with dissolve

    "Tâm đứng cách đó vài bước, tay cầm ly nước, nhìn bạn mình thao thao với vẻ nghiêm túc hơi quá mức."

    "Cô thấy nhẹ nhõm."

    "Có những người sinh ra đã hợp với việc làm không khí sống lại."

    show hoang neutral

    hoang "Ý của em không sai. Không gian nghỉ mà khiến người ta thấy bị kiểm tra thì thất bại rồi."

    show huyen surprised

    huyen "Đúng. Chính là cảm giác bị kiểm tra."

    show hoang thoughtful

    hoang "Anh sẽ ghi lại."

    show huyen confused

    huyen "Thật ạ?"

    show hoang smile

    hoang "Ừ. Dù anh không chắc nên ghi là \"hiệu ứng nha khoa\" hay \"khủng hoảng pantry\"."

    show huyen laugh

    huyen "Cái sau nghe chuyên nghiệp hơn."

    show tam happy

    "Tâm không nhịn được cười."

    show hoang neutral

    "Hoàng nhìn sang cô."

    show tam embarrassed

    "Tâm lập tức nâng ly nước lên như thể mình chỉ vô tình đứng đó."

    show hoang smile

    "Hoàng không nói gì. Chỉ cười."

    "Huyền quay đầu nhìn Tâm, ánh mắt lấp lánh kiểu rất nguy hiểm."

    show huyen smile

    huyen "Bạn em là Tâm. Người đã đẩy em qua đây và giả vờ vô tội."

    show tam shocked

    tam "Huyền!"

    show hoang laugh

    hoang "Vậy anh nên cảm ơn Tâm."

    show tam embarrassed

    tam "Không cần đâu ạ. Em chỉ... hỗ trợ truyền thông nội bộ."

    show hoang smile

    hoang "Công việc đó có vẻ hợp với hai em."

    show huyen happy

    huyen "Anh nói thế là bên em có người ghi nhận rồi đó."

    "Câu chuyện tiếp tục thêm một lúc."

    "Tâm không nói nhiều."

    "Nhưng mỗi lần Huyền hơi quá đà, cô lại kéo nhẹ tay áo bạn mình."

    "Mỗi lần như vậy, Hoàng đều nhìn thấy."

    jump tam_c02_after_routes


# ============================================================
# AFTER ROUTES
# ============================================================

label tam_c02_after_routes:

    scene black with fade

    if tam_c02_party_route == "A":

        show huyen smile at right
        show tam embarrassed at left
        with dissolve

        huyen "Sao rồi?"

        tam "Sao là sao?"

        huyen "Ngành kiến trúc."

        show tam pouty

        tam "Ổn."

        show huyen laugh

        huyen "Chỉ ổn thôi à?"

        show tam thoughtful

        tam "Ừ."

        "Tâm cúi xuống nhìn chiếc thẻ nhân viên của mình."

        "Nó lại hơi lệch."

        "Cô chỉnh lại, nhưng lần này động tác chậm hơn."

    elif tam_c02_party_route == "B":

        show huyen smile at right
        show tam thoughtful at left
        with dissolve

        huyen "Người ta tự qua bắt chuyện với mày à?"

        show tam embarrassed

        tam "Ừ."

        huyen "Ồ."

        tam "Đừng \"ồ\" kiểu đó."

        show huyen laugh

        huyen "Tao đã nói gì đâu."

        tam "Chính vì mày chưa nói gì nên mới đáng sợ."

    elif tam_c02_party_route == "C":

        show huyen neutral at right
        show tam neutral at left
        with dissolve

        huyen "Về thôi?"

        tam "Ừ."

        show huyen smile

        huyen "Mai lại gặp anh Quân."

        show tam serious

        tam "Đừng nhắc trước giờ ngủ."

        show huyen laugh

        "Hai cô gái rời khỏi sảnh tiệc."

        "Ngoài hành lang, ánh đèn trắng hơn một chút. Không khí cũng dễ thở hơn."

    elif tam_c02_party_route == "D":

        show huyen happy at right
        show tam neutral at left
        with dissolve

        huyen "Anh Hoàng nói chuyện duyên phết."

        show tam smile

        tam "Ừ. Hợp với mày."

        show huyen surprised

        huyen "Khoan. Câu đó là ý gì?"

        show tam neutral

        tam "Ý là mày nói nhiều, anh ấy chịu nghe."

        show huyen pouty

        huyen "Tình bạn này bắt đầu mất cân bằng rồi."

        show tam laugh

        "Tâm cười, rồi đưa cho Huyền chiếc khăn giấy cô đã cầm sẵn từ lúc nào."

        show huyen confused

        huyen "Gì đây?"

        tam "Mày dính sốt ở tay áo."

        show huyen shocked

        huyen "Sao giờ mới nói?"

        show tam smile

        tam "Đợi mày nói xong phần pantry."

    hide tam
    hide huyen
    hide hoang
    hide quan
    with dissolve

    if tam_c02_hoang_pov_unlocked:
        call tam_c02_short_hoang_pov

    jump tam_c02_complete


# ============================================================
# OPTIONAL SHORT HOÀNG POV
# Only when A/B/D creates enough interaction.
# ============================================================

label tam_c02_short_hoang_pov:

    scene black with fade

    "Một lúc sau."

    show hoang neutral at left
    show quan serious at right
    with dissolve

    quan "Cậu thấy thế nào?"

    show hoang thoughtful

    hoang "Về văn phòng à?"

    quan "Không. Hai nhân viên mới."

    show hoang neutral

    "Hoàng nhìn về phía cửa sảnh."

    "Hai cô gái đã rời đi. Trên bàn gần đó còn lại một chiếc khăn giấy gấp đôi rất gọn."

    if tam_c02_party_route == "A":

        show hoang smile

        hoang "Tâm khá thú vị."

        show quan neutral

        quan "Thú vị?"

        hoang "Không ồn. Nhưng biết cách làm người khác trả lời nhiều hơn dự định."

        show quan serious

        quan "Đó có thể là năng lực tốt."

        show hoang embarrassed

        hoang "Anh nói câu đó nghe như đang chuẩn bị giao thêm việc cho người ta."

        quan "Nếu làm được thì tại sao không?"

        show hoang smile

        "Hoàng cười nhẹ."

        "Trong đầu anh hiện lên hình ảnh Tâm cúi xuống lau mép đĩa."

        "Một động tác nhỏ tới mức nếu không để ý thì sẽ trôi qua rất nhanh."

        "Nhưng anh đã để ý."

    elif tam_c02_party_route == "B":

        show hoang thoughtful

        hoang "Tâm để ý chi tiết."

        show quan neutral

        quan "Tôi biết."

        show hoang surprised

        hoang "Anh biết rồi à?"

        quan "Tôi tuyển người, không bốc thăm."

        show hoang smile

        hoang "Cũng đúng."

        "Hoàng nhìn chiếc ly nước trên tay."

        "Anh nhớ cách cô nói: \"Em chỉ không muốn ai đó phải đi tìm khăn giấy thôi.\""

        "Một câu rất nhỏ."

        "Nhưng có những người bộc lộ mình qua đúng những câu nhỏ như thế."

    elif tam_c02_party_route == "D":

        show hoang smile

        hoang "Huyền nói chuyện rất sống."

        show quan serious

        quan "Sống quá cũng mệt."

        show hoang laugh

        hoang "Anh đúng là không để niềm vui qua cửa dễ dàng."

        show quan neutral

        quan "Còn Tâm?"

        show hoang thoughtful

        hoang "Tâm đứng sau giữ nhịp."

        show quan serious

        quan "Nhận xét khá nhanh."

        show hoang smile

        hoang "Nghề của em mà."

        "Hoàng nhớ bàn tay Tâm kéo nhẹ tay áo Huyền mỗi lần bạn mình nói nhanh quá."

        "Không ngắt lời. Không chen vào."

        "Chỉ kéo một chút."

        "Có những người không cần đứng giữa phòng mới làm được điểm tựa."

    show quan serious

    quan "Dù sao cũng đừng làm phiền nhân viên mới của tôi."

    show hoang surprised

    hoang "Em đã làm gì đâu."

    quan "Tôi nhắc trước."

    show hoang pouty

    hoang "Anh nói như thể em là rủi ro vận hành."

    show quan neutral

    quan "Cậu là rủi ro xã giao."

    show hoang laugh

    "Hoàng bật cười."

    "Anh không phủ nhận."

    hide hoang
    hide quan
    with dissolve

    return


# ============================================================
# COMPLETE CHAPTER
# ============================================================

label tam_c02_complete:

    scene black with fade

    "Đêm đó, Tâm về nhà muộn hơn thường lệ."

    "Cô đặt chiếc thẻ nhân viên lên bàn, cạnh cuốn sổ đã ghi kín thêm vài dòng mới."

    if tam_c02_party_route == "A":

        "Dòng cuối cùng chỉ có ba chữ:"

        "\"Hoàng — dễ nói chuyện.\""

        "Tâm nhìn ba chữ ấy một lúc, rồi gấp sổ lại."

    elif tam_c02_party_route == "B":

        "Dòng cuối cùng được viết hơi lệch."

        "\"Hoàng — tự bắt chuyện.\""

        "Tâm nhìn nét chữ, bỗng thấy buồn cười vì chính mình cũng chưa hiểu tại sao phải ghi việc đó lại."

    elif tam_c02_party_route == "C":

        "Dòng cuối cùng là một ghi chú công việc."

        "\"Hỏi lại quy trình review proposal.\""

        "Cô khoanh tròn nó hai lần."

        "Buổi tiệc, với cô, kết thúc ở đó."

    elif tam_c02_party_route == "D":

        "Dòng cuối cùng có tên Huyền trước."

        "\"Huyền nói chuyện với Hoàng. Pantry.\""

        "Tâm nhìn chữ \"Pantry\" rồi bật cười một mình."

    "Ngoài cửa sổ, thành phố vẫn sáng."

    "Một ngày đi làm nữa đã qua."

    "Một mối liên hệ nào đó vừa bắt đầu — hoặc đi ngang qua rất khẽ."

    $ complete_chapter("tam_c02")
    jump route_map
```

---

## 3. Tóm tắt branch effects

| Route                         | Điều kiện                                          | Kết quả                                                                                                                                              |
| ----------------------------- | -------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| A — Canon Seed                | Tâm chủ động hoặc `tam_hoang_interest >= 1`        | `trust_tam_hoang +2`, `intimacy_tam_hoang +1`, `tam_direction = tam_hoang_open`, unlock `hoang_h01`                                                  |
| B — Hoàng chủ động            | `hoang_notices_tam >= 1` và Tâm không chủ động     | `trust_tam_hoang +1`, `hoang_tam_interest +1`, `hoang_direction = hoang_tam_open`, unlock `hoang_h01`                                                |
| C — Không gặp đáng kể         | Tâm né xã giao / tập trung công việc / rời sớm     | `career_tam +1`, `intimacy_tam_hoang -1`, `hoang_direction = hoang_friend_group_possible`                                                            |
| D — Huyền tương tác nhiều hơn | Tâm đẩy Huyền lên hoặc `huyen_hoang_interest >= 1` | `trust_hoang_huyen +2`, `huyen_hoang_interest +1`, `huyen_direction = huyen_hoang_interest`, `tam_direction = tam_support_huyen`, unlock `hoang_h01` |

Gọn nhưng đủ xài. Phần đáng giữ nhất là chi tiết **ly nước ở mép bàn**: nó làm điều kiện `hoang_notices_tam` tự nhiên hơn, không biến “Hoàng chú ý Tâm” thành kiểu nam chính tự dưng scan nữ chính bằng radar tình yêu rẻ tiền. Ừ, ta không làm trò đó.
