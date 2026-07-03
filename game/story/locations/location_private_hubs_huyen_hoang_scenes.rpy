# FILE: game/map/location_private_hubs_huyen_hoang_scenes.rpy
# Sample private-location scenes for Huyền and Hoàng.
# This file extends map_location_interactions.rpy without changing the hub UI.

init 0 python:

    def _loc_enable_scene_router_for_action(location_id, action_id, scene_key=None, default_scene_label=None):
        for action in MAP_LOCATION_ACTIONS.get(location_id, []) or []:
            if action.get("id") == action_id:
                action["use_scene_router"] = True
                action["scene_key"] = scene_key or action_id
                if default_scene_label:
                    action["default_scene_label"] = default_scene_label
                return True
        return False

    _loc_enable_scene_router_for_action("huyen_apartment", "huyen_visit_chat", "huyen_visit_chat")
    _loc_enable_scene_router_for_action("hoang_house", "hoang_visit_casual", "hoang_visit_casual")
    _loc_enable_scene_router_for_action("hoang_house", "hoang_design_help", "hoang_design_help")

    MAP_LOCATION_SCENE_RULES.setdefault("huyen_apartment", {})
    MAP_LOCATION_SCENE_RULES["huyen_apartment"].update({
        "huyen_visit_chat": {
            "mode": "weighted_random",
            "default_label": "loc_huyen_home_default_tea",
            "scenes": [
                {
                    "label": "loc_huyen_home_after_company_party_unique",
                    "priority": 100,
                    "weight": 1,
                    "conditions": ["completed:tam_c02_company_party"],
                    "min_scores": {"tam_hoang_interest": 1},
                    "blocked_flags": ["loc_seen_huyen_home_after_company_party_unique"],
                },
                {
                    "label": "loc_huyen_home_observant_friend",
                    "priority": 20,
                    "weight": 2,
                    "min_scores": {"tam_observation": 3},
                },
                {
                    "label": "loc_huyen_home_self_clarity_check",
                    "priority": 10,
                    "weight": 2,
                    "min_scores": {"tam_self_clarity": 2},
                },
                {
                    "label": "loc_huyen_home_default_tea",
                    "priority": 0,
                    "weight": 4,
                },
                {
                    "label": "loc_huyen_home_default_rain_window",
                    "priority": 0,
                    "weight": 3,
                },
            ],
        },
    })

    MAP_LOCATION_SCENE_RULES.setdefault("hoang_house", {})
    MAP_LOCATION_SCENE_RULES["hoang_house"].update({
        "hoang_visit_casual": {
            "mode": "weighted_random",
            "default_label": "loc_hoang_house_default_gate",
            "scenes": [
                {
                    "label": "loc_hoang_house_after_company_party_unique",
                    "priority": 100,
                    "weight": 1,
                    "conditions": ["completed:tam_c02_company_party"],
                    "min_scores": {"tam_hoang_interest": 1},
                    "blocked_flags": ["loc_seen_hoang_house_after_company_party_unique"],
                },
                {
                    "label": "loc_hoang_house_high_trust_kitchen",
                    "priority": 25,
                    "weight": 2,
                    "min_scores": {"hoang_tam_trust": 3},
                },
                {
                    "label": "loc_hoang_house_tam_interest_garden",
                    "priority": 15,
                    "weight": 2,
                    "min_scores": {"tam_hoang_interest": 2},
                },
                {
                    "label": "loc_hoang_house_default_gate",
                    "priority": 0,
                    "weight": 4,
                },
                {
                    "label": "loc_hoang_house_default_living_room",
                    "priority": 0,
                    "weight": 3,
                },
            ],
        },
        "hoang_design_help": {
            "mode": "weighted_random",
            "default_label": "loc_hoang_house_design_default",
            "scenes": [
                {
                    "label": "loc_hoang_house_design_professional_sync",
                    "priority": 30,
                    "weight": 2,
                    "min_scores": {"career_tam": 3, "hoang_professional_credit": 1},
                },
                {
                    "label": "loc_hoang_house_design_default",
                    "priority": 0,
                    "weight": 4,
                },
            ],
        },
    })


label loc_huyen_home_set_bg:
    if renpy.loadable("images/assets/bg/bg_huyen_apartment_evening.png"):
        scene expression "images/assets/bg/bg_huyen_apartment_evening.png"
    else:
        scene black
    with fade
    return


label loc_hoang_house_set_bg:
    if renpy.loadable("images/assets/bg/bg_hoang_house_day.png"):
        scene expression "images/assets/bg/bg_hoang_house_day.png"
    else:
        scene black
    with fade
    return


# -----------------------------------------------------------------------------
# HUYỀN PRIVATE HUB SCENES
# -----------------------------------------------------------------------------

label loc_huyen_home_after_company_party_unique:
    call loc_huyen_home_set_bg

    $ loc_activity_add_value("time_units", -1)
    $ loc_activity_add_value("energy", -3)
    $ loc_activity_add_value("stress", -4)
    $ loc_story_flag("loc_seen_huyen_home_after_company_party_unique")

    huyen teasing "Đến giờ này mới ghé à?"
    tam neutral "Cậu nói như tớ có lịch báo cáo mỗi ngày ấy."
    huyen smile "Không có. Nhưng sau buổi tiệc công ty thì đáng lẽ nên có."

    "Tâm đứng ở cửa thêm một nhịp. Trong tay cô là túi đồ nhỏ mua trên đường tới. Quai túi bị cô xoắn lệch đi một vòng."

    huyen neutral "Vào đi. Đứng đó làm nhân viên kiểm tra thảm cửa à?"

    menu:
        "Nói thật là mình hơi rối sau buổi tiệc":
            $ loc_story_add("tam_self_clarity", 2)
            $ loc_story_add("tam_observation", 1)
            $ loc_story_add("tam_hoang_interest", 1)
            $ loc_story_add("hoang_tam_trust", 1)
            $ loc_activity_add_value("mood", 5)

            tam shy "Tớ không biết nữa. Hôm đó... tớ cứ để ý anh Hoàng."
            huyen teasing "Ừ. Cốc nước trên tay cậu cũng để ý theo. Nó bị khuấy đến đáng thương."
            tam embarrassed "Cậu nhìn thấy à?"
            huyen smile "Tớ có mắt. Và hơi tiếc là cậu cũng có."

            "Tâm kéo gối ôm vào lòng, im một lúc. Lần này cô không phủ nhận."

        "Đánh trống lảng bằng chuyện công việc":
            $ loc_story_add("tam_observation", 2)
            $ loc_story_add("career_tam", 1)
            $ loc_activity_add_value("mood", 2)

            tam neutral "Tớ chỉ đang nghĩ về Quân thôi. Trưởng phòng ấy."
            huyen bored "Ừ. Rất thuyết phục. Cậu nghĩ về trưởng phòng bằng mặt đỏ như bị bắt gặp nhắn tin à?"
            tam flustered "Huyền."
            huyen teasing "Rồi, rồi. Bộ Tin Cậu tạm thời ngừng phát sóng."

            "Huyền rót thêm nước, nhưng đẩy cốc về phía Tâm rất nhẹ. Như thể không muốn làm câu đùa vừa rồi nặng hơn."

    return


label loc_huyen_home_observant_friend:
    call loc_huyen_home_set_bg

    $ loc_activity_add_value("time_units", -1)
    $ loc_activity_add_value("energy", -3)
    $ loc_activity_add_value("stress", -5)
    $ loc_story_add("tam_observation", 1)

    "Huyền đang gấp quần áo trên sofa. Một chiếc áo bị gấp lệch mép, và cô đã sửa nó ba lần."

    tam neutral "Cậu đang lo chuyện gì à?"
    huyen neutral "Không."
    tam smile "Cậu vừa gấp cái áo đó như đang thẩm vấn nó."

    huyen "..."
    huyen tired "Ghét thật. Cậu học thói quan sát này ở đâu thế?"
    tam teasing "Tự nhiên thôi. Tớ trưởng thành rồi."
    huyen bored "Ừ. Nghe rất đáng nghi."

    menu:
        "Ngồi xuống giúp Huyền gấp đồ":
            $ loc_story_add("tam_self_clarity", 1)
            $ loc_activity_add_value("mood", 4)
            $ loc_activity_add_value("stress", -2)

            "Tâm không hỏi thêm. Cô chỉ ngồi xuống, kéo một chiếc áo khác về phía mình."
            huyen smile "Cảm ơn."
            tam neutral "Có gì đâu. Gấp áo thôi mà."
            huyen neutral "Ừ. Gấp áo thôi."

        "Trêu nhẹ để Huyền tự nói":
            $ loc_story_add("tam_observation", 1)
            $ loc_activity_add_value("mood", 3)

            tam teasing "Nếu cái áo có tội, cậu nên cho nó luật sư."
            huyen irritated "Nó có đồng phạm. Tên là deadline."
            tam smile "À. Tội có tổ chức."

    return


label loc_huyen_home_self_clarity_check:
    call loc_huyen_home_set_bg

    $ loc_activity_add_value("time_units", -1)
    $ loc_activity_add_value("energy", -3)
    $ loc_story_add("tam_self_clarity", 1)
    $ loc_activity_add_value("stress", -3)

    huyen neutral "Dạo này cậu nói chuyện rõ hơn trước đấy."
    tam confused "Rõ hơn là sao?"
    huyen smile "Lúc muốn từ chối thì cậu từ chối. Lúc muốn hỏi thì cậu hỏi. Ít vòng vo hơn."

    "Tâm nhìn xuống cốc nước trong tay. Mặt nước rung rất nhẹ rồi yên lại."

    menu:
        "Thừa nhận mình đang cố thay đổi":
            $ loc_story_add("tam_self_clarity", 2)
            $ loc_activity_add_value("confidence", 2)

            tam neutral "Tớ không muốn cứ để người khác kéo mình đi mãi."
            huyen smile "Tốt. Nhớ kéo lại vừa phải thôi. Kéo mạnh quá ngã."
            tam smile "Cậu nói như mẹ tớ ấy."
            huyen bored "Xin lỗi. Tớ chưa đủ tuổi chịu trách nhiệm câu đó."

        "Cười cho qua":
            $ loc_story_add("tam_observation", 1)
            $ loc_activity_add_value("mood", 2)

            tam smile "Có lẽ do đi làm rồi. Người trưởng thành phải thế."
            huyen teasing "Người trưởng thành cũng không giấu bánh trong túi xách."
            tam embarrassed "Đó là đồ dự phòng."
            huyen smile "Ừ. Dự phòng lòng tự trọng tụt đường huyết."

    return


label loc_huyen_home_default_tea:
    call loc_huyen_home_set_bg

    $ loc_activity_add_value("time_units", -1)
    $ loc_activity_add_value("energy", -3)
    $ loc_activity_add_value("stress", -4)
    $ loc_activity_add_value("mood", 4)
    $ loc_story_add("tam_observation", 1)

    huyen neutral "Trà nóng hay nước lọc?"
    tam neutral "Nước lọc cũng được."
    huyen bored "Câu trả lời của người không muốn chọn."
    tam smile "Vậy trà nóng."
    huyen smile "Tốt. Vẫn cứu được."

    "Ấm nước kêu rất khẽ trong bếp. Tâm ngồi ở sofa, nhìn Huyền lấy hai chiếc cốc khác màu. Một chiếc cũ hơn, có vết mẻ nhỏ ở quai."

    menu:
        "Hỏi về chiếc cốc bị mẻ":
            $ loc_story_add("tam_observation", 1)
            $ loc_activity_add_value("mood", 2)

            tam neutral "Cốc đó bị mẻ rồi mà cậu vẫn dùng à?"
            huyen smile "Ừ. Uống vẫn được. Chỉ cần đừng chạm môi vào chỗ đó."
            tam neutral "Nghe như lời khuyên sống."
            huyen teasing "Đừng làm quá. Nó là cái cốc."

        "Im lặng uống trà":
            $ loc_activity_add_value("stress", -2)

            "Tâm nhận cốc trà bằng hai tay. Nóng vừa đủ. Không ai hỏi chuyện lớn. Có những buổi tối chỉ cần thế."

    return


label loc_huyen_home_default_rain_window:
    call loc_huyen_home_set_bg

    $ loc_activity_add_value("time_units", -1)
    $ loc_activity_add_value("energy", -2)
    $ loc_activity_add_value("stress", -5)
    $ loc_activity_add_value("mood", 3)

    "Ngoài cửa sổ, trời bắt đầu mưa. Huyền kéo rèm lại một nửa, rồi đứng nhìn hạt nước chạy xuống mặt kính."

    tam neutral "Cậu không đóng hẳn à?"
    huyen neutral "Để nghe tiếng mưa."
    tam smile "Tưởng cậu ghét ẩm."
    huyen bored "Ghét ẩm. Không ghét mưa. Hai thứ đó đừng nhập hộ khẩu chung."

    menu:
        "Ngồi lại thêm một lúc":
            $ loc_activity_add_value("mood", 3)
            $ loc_story_add("tam_self_clarity", 1)

            "Tâm ngồi xuống cạnh cô. Hai người không nói gì thêm một lúc lâu. Tiếng mưa lấp vào chỗ mà lời nói thường làm quá tay."

        "Đứng dậy phụ Huyền dọn bàn":
            $ loc_activity_add_value("life_skill", 1)
            $ loc_activity_add_value("stress", -1)

            "Tâm gom mấy chiếc đĩa nhỏ trên bàn. Huyền liếc cô, rồi im lặng kéo thùng rác lại gần hơn."

    return


# -----------------------------------------------------------------------------
# HOÀNG PRIVATE HUB SCENES
# -----------------------------------------------------------------------------

label loc_hoang_house_after_company_party_unique:
    call loc_hoang_house_set_bg

    $ loc_activity_add_value("time_units", -1)
    $ loc_activity_add_value("energy", -4)
    $ loc_activity_add_value("stress", -3)
    $ loc_story_flag("loc_seen_hoang_house_after_company_party_unique")

    "Hoàng mở cổng trước khi Tâm kịp bấm chuông lần thứ hai. Anh nhìn cô, rồi nhìn xuống đôi giày cô đang hơi lệch mũi."

    hoang smile "Anh tưởng em sẽ không đến."
    tam neutral "Vậy sao anh mở cửa nhanh thế?"
    hoang embarrassed "...Tình cờ đi ngang qua thôi."
    tam teasing "Cổng nhà anh có tuyến đi ngang qua riêng à?"

    "Hoàng bật cười, hơi nghiêng người nhường đường. Câu trả lời không ai tin, nhưng cả hai đều đủ lịch sự để tha cho nó."

    menu:
        "Nhắc lại chuyện buổi tiệc công ty":
            $ loc_story_add("tam_hoang_interest", 2)
            $ loc_story_add("hoang_tam_trust", 2)
            $ loc_story_add("tam_self_clarity", 1)
            $ loc_activity_add_value("mood", 5)

            tam shy "Hôm đó... em hơi bất ngờ khi gặp anh ở đó."
            hoang neutral "Anh cũng vậy."
            tam neutral "Anh bất ngờ vì em chủ động bắt chuyện à?"
            hoang smile "Không. Anh bất ngờ vì mình đã đợi em bắt chuyện."

            "Tâm cúi xuống chỉnh lại quai túi. Chỉ một cái quai túi thôi mà tự nhiên rất bận."

        "Chỉ nói là tiện đường ghé qua":
            $ loc_story_add("tam_observation", 1)
            $ loc_story_add("hoang_tam_trust", 1)
            $ loc_activity_add_value("mood", 3)

            tam neutral "Em tiện đường nên ghé một chút."
            hoang teasing "Từ công ty đến đây vòng qua nửa thành phố. Tiện đường khá tham vọng."
            tam embarrassed "Anh có nhất thiết phải nhớ đường kỹ vậy không?"
            hoang smile "Anh học kiến trúc. Đổ lỗi nghề nghiệp đi."

    return


label loc_hoang_house_high_trust_kitchen:
    call loc_hoang_house_set_bg

    $ loc_activity_add_value("time_units", -1)
    $ loc_activity_add_value("energy", -4)
    $ loc_activity_add_value("stress", -4)
    $ loc_story_add("hoang_tam_trust", 1)

    "Trong bếp, Hoàng đang cắt táo. Miếng đầu tiên hơi dày. Miếng thứ hai lại mỏng quá. Anh cau mày như đang xử lý bản vẽ khó."

    tam smile "Anh đang thiết kế món táo à?"
    hoang neutral "Anh đang cố cắt đều."
    tam teasing "Táo không cần nghiệm thu đâu."
    hoang smile "Nhưng em thì có vẻ sẽ nghiệm thu."

    menu:
        "Đứng cạnh phụ anh":
            $ loc_story_add("tam_hoang_interest", 1)
            $ loc_story_add("hoang_tam_trust", 1)
            $ loc_activity_add_value("mood", 4)

            "Tâm lấy chiếc đĩa bên cạnh, đặt gần tay anh hơn. Hoàng không nhìn cô, nhưng khóe miệng cong lên rất nhẹ."
            hoang neutral "Cẩn thận dao."
            tam smile "Em biết rồi."
            hoang neutral "Anh biết là em biết. Anh vẫn nói."

        "Trêu anh thêm một câu":
            $ loc_story_add("tam_self_clarity", 1)
            $ loc_activity_add_value("mood", 3)

            tam teasing "Anh nghiêm túc với quả táo hơn nhiều người nghiêm túc với đời mình."
            hoang laughing "Cảm ơn. Anh sẽ ghi vào hồ sơ năng lực."

    return


label loc_hoang_house_tam_interest_garden:
    call loc_hoang_house_set_bg

    $ loc_activity_add_value("time_units", -1)
    $ loc_activity_add_value("energy", -4)
    $ loc_activity_add_value("stress", -3)
    $ loc_story_add("tam_hoang_interest", 1)

    "Khu vườn sau nhà có vài luống rau nhỏ. Hoàng cúi xuống nhổ một cọng cỏ mọc lệch giữa hàng cải."

    tam neutral "Anh tự chăm hết à?"
    hoang neutral "Một phần. Bố anh thích trồng, anh thích sửa những thứ bị lệch."
    tam smile "Nghe rất kiến trúc."
    hoang smile "Nghe rất bệnh nghề nghiệp thì đúng hơn."

    menu:
        "Hỏi thêm về gia đình Hoàng":
            $ loc_story_add("hoang_tam_trust", 2)
            $ loc_story_add("tam_observation", 1)

            tam neutral "Nhà anh có vẻ... nhiều thói quen nhỏ nhỉ."
            hoang neutral "Ừ. Có những thứ không ai nói là luật, nhưng ai cũng làm theo."
            tam neutral "Ví dụ?"
            hoang smile "Không để người khác đứng một mình ngoài cổng quá lâu."

            "Tâm quay đi. Một luống rau bỗng nhiên trở nên rất đáng nhìn."

        "Phụ anh nhổ cỏ":
            $ loc_activity_add_value("life_skill", 1)
            $ loc_story_add("hoang_tam_trust", 1)

            "Tâm ngồi xuống bên cạnh. Cọng cỏ đầu tiên đứt ngang vì cô kéo hơi vội."
            hoang teasing "Nhẹ tay thôi. Nó là cỏ, không phải kẻ thù của em."
            tam embarrassed "Em đang học."

    return


label loc_hoang_house_default_gate:
    call loc_hoang_house_set_bg

    $ loc_activity_add_value("time_units", -1)
    $ loc_activity_add_value("energy", -4)
    $ loc_activity_add_value("stress", -3)
    $ loc_activity_add_value("mood", 4)
    $ loc_story_add("hoang_tam_trust", 1)

    "Tâm vừa đến cổng thì thấy Hoàng đang lau kính xe. Tay áo anh xắn lên, khăn lau vắt qua cổ tay."

    hoang smile "Em đến đúng lúc đấy."
    tam neutral "Đúng lúc gì?"
    hoang teasing "Đúng lúc anh cần một người đứng ngoài nhận xét xem xe đã sạch chưa."
    tam bored "Công việc cao quý quá."

    menu:
        "Giúp anh lau xe":
            $ loc_activity_add_value("energy", -2)
            $ loc_activity_add_value("mood", 3)
            $ loc_story_add("hoang_tam_trust", 1)

            "Tâm nhận chiếc khăn sạch. Lau được ba đường, cô phát hiện Hoàng đang nhìn mình qua bóng phản chiếu trên kính."
            tam neutral "Anh nhìn gì đấy?"
            hoang smile "Kiểm tra chất lượng."
            tam teasing "Chất lượng khăn hay người lau?"
            hoang "..."

        "Đứng nhìn và chê nhẹ":
            $ loc_activity_add_value("mood", 2)
            $ loc_story_add("tam_observation", 1)

            tam teasing "Góc kia vẫn còn vệt nước."
            hoang neutral "Em vừa đến đã soi à?"
            tam smile "Em học từ môi trường công sở."

    return


label loc_hoang_house_default_living_room:
    call loc_hoang_house_set_bg

    $ loc_activity_add_value("time_units", -1)
    $ loc_activity_add_value("energy", -3)
    $ loc_activity_add_value("stress", -3)
    $ loc_activity_add_value("mood", 3)

    "Phòng khách yên hơn Tâm tưởng. Trên bàn có một cuốn sách kiến trúc mở úp xuống, cạnh đó là cốc nước đã vơi một nửa."

    hoang neutral "Anh vừa đọc dở."
    tam neutral "Em có làm phiền không?"
    hoang smile "Có. Nhưng theo hướng chấp nhận được."
    tam bored "Cảm ơn vì lời mời rất nồng hậu."

    menu:
        "Hỏi anh đang đọc gì":
            $ loc_story_add("hoang_professional_credit", 1)
            $ loc_story_add("tam_observation", 1)
            $ loc_activity_add_value("knowledge", 1)

            tam neutral "Sách gì vậy anh?"
            hoang neutral "Về cách ánh sáng đi qua không gian hẹp."
            tam smile "Nghe như thơ nhưng có bản vẽ."
            hoang smile "Kiến trúc đôi khi giả vờ khô khan để khỏi bị bắt viết thơ."

        "Nói chuyện linh tinh một lúc":
            $ loc_story_add("hoang_tam_trust", 1)
            $ loc_activity_add_value("mood", 3)

            "Hai người nói vài chuyện không quan trọng. Thời tiết. Công ty. Một quán ăn mới mở. Chính vì không quan trọng nên Tâm lại thấy dễ thở."

    return


label loc_hoang_house_design_default:
    call loc_hoang_house_set_bg

    $ loc_activity_add_value("time_units", -2)
    $ loc_activity_add_value("energy", -9)
    $ loc_activity_add_value("stress", 2)
    $ loc_story_add("hoang_tam_trust", 1)
    $ loc_story_add("hoang_professional_credit", 1)
    $ loc_story_add("career_tam", 1)

    "Bản vẽ trải trên bàn. Tâm cúi xuống, lấy bút chì đánh dấu một điểm ở mép phải."

    tam neutral "Chỗ này nếu người dùng đi từ cửa vào thì hơi khuất."
    hoang neutral "Ừ. Anh cũng thấy nó chưa ổn."
    tam neutral "Không phải chưa ổn. Chỉ là nó đang tự tin sai chỗ."
    hoang smile "Câu đó nghe giống Quân. Nhưng dễ nghe hơn."

    menu:
        "Phân tích tiếp theo góc nhìn người dùng":
            $ loc_activity_add_value("work_skill", 2)
            $ loc_story_add("career_tam", 1)
            $ loc_story_add("hoang_tam_trust", 1)

            tam neutral "Nếu là em, em sẽ muốn lối này mở hơn một chút. Không cần rộng, chỉ cần đừng làm người ta ngập ngừng."
            hoang neutral "Ngập ngừng cũng là dữ liệu à?"
            tam smile "Trong UI thì có. Trong đời chắc cũng thế."

        "Dừng lại trước khi quá mệt":
            $ loc_activity_add_value("stress", -2)
            $ loc_story_add("tam_self_clarity", 1)

            tam tired "Em nghĩ hôm nay đến đây thôi. Nếu nhìn thêm, em sẽ bắt đầu ghét cái bàn."
            hoang smile "Anh sẽ bảo cái bàn tự kiểm điểm."

    return


label loc_hoang_house_design_professional_sync:
    call loc_hoang_house_set_bg

    $ loc_activity_add_value("time_units", -2)
    $ loc_activity_add_value("energy", -8)
    $ loc_activity_add_value("stress", 1)
    $ loc_activity_add_value("work_skill", 2)
    $ loc_story_add("career_tam", 2)
    $ loc_story_add("hoang_professional_credit", 1)
    $ loc_story_add("hoang_tam_trust", 1)

    "Hai người gần như không cần giải thích dài. Hoàng kéo bản vẽ sang trái, Tâm đã đặt ngón tay vào đúng khoảng trống anh đang nhìn."

    hoang neutral "Em cũng thấy chỗ này à?"
    tam neutral "Ừ. Nó đẹp, nhưng hơi ích kỷ."
    hoang smile "Ích kỷ?"
    tam neutral "Nó muốn được nhìn trước khi nó chịu phục vụ người dùng."

    "Hoàng im vài giây, rồi gạch một đường rất nhẹ lên bản vẽ."

    hoang smile "Anh mượn câu đó được không?"
    tam teasing "Tính phí theo chữ."
    hoang teasing "Vậy anh trả bằng trà nhé."

    menu:
        "Nhận lời uống trà":
            $ loc_activity_add_value("mood", 4)
            $ loc_story_add("tam_hoang_interest", 1)

            tam smile "Trà thì được. Nhưng lần sau anh vẫn tính phí tư vấn đi."
            hoang smile "Anh sẽ ghi nợ."

        "Giữ nhịp chuyên nghiệp":
            $ loc_story_add("career_tam", 1)
            $ loc_story_add("tam_self_clarity", 1)

            tam neutral "Để xong phần này trước đã. Trà để sau."
            hoang neutral "Rõ. Chuyên gia khó tính."
            tam smile "Đang học từ trưởng phòng."

    return
