# FILE: game/timeline_map_data.rpy
# Purpose: Spoiler-safe continuous chronology timeline data.
# Notes: Route identity is preserved as node metadata; the visible map is one chronological route.

init -2 python:
    def normalize_timeline_persistent_state():
        if not hasattr(persistent, "timeline_bookmarks") or persistent.timeline_bookmarks is None:
            persistent.timeline_bookmarks = []
        elif not isinstance(persistent.timeline_bookmarks, list):
            persistent.timeline_bookmarks = list(persistent.timeline_bookmarks)

    normalize_timeline_persistent_state()

    TIMELINE_DEFAULT_ROUTE_ID = "chronology"
    TIMELINE_ROUTES = [{'id': 'chronology', 'label': 'Story Timeline'}]

    TIMELINE_MAP_BACKGROUND = "images/assets/bg/ui/bg_timeline_map_blur.webp"
    TIMELINE_FALLBACK_BACKGROUND = "gui/theme/background_full.png"
    TIMELINE_FALLBACK_THUMBNAIL = "gui/game_menu.png"
    TIMELINE_LOCKED_THUMBNAIL = None
    TIMELINE_LOCKED_TITLE = "Chương chưa mở khóa"
    TIMELINE_LOCKED_SUMMARY = "Tiếp tục câu chuyện để mở khóa thông tin của chương này."
    TIMELINE_LOCKED_REQUIREMENT = "Tiếp tục các chương đang mở để hé lộ nhánh này."
    TIMELINE_SCREEN_STATE_CACHE = {}

    def timeline_freeze_signature(value):
        if isinstance(value, dict):
            return tuple(sorted((key, timeline_freeze_signature(item)) for key, item in value.items()))
        if isinstance(value, (list, tuple, set)):
            return tuple(timeline_freeze_signature(item) for item in value)
        return value

    TIMELINE_MAP_NODES = {'chronology': [{'id': 'fb_minyuu_01_first_frame',
                     'chapter_id': 'fb_minyuu_01_first_frame',
                     'title': 'First Frame',
                     'code': 'FB01',
                     'type': 'bonus',
                     'thumbnail': 'images/assets/thumbnails/minh/fb_minyuu_01_first_frame.webp',
                     'summary': 'Minh và Yuuka gặp nhau trong bối cảnh học tập/nghề phim; respect và friction bắt đầu.',
                     'duration': 'MVP skeleton',
                     'x': 80,
                     'y': 400,
                     'w': 200,
                     'h': 200,
                     'origin_route': 'minh',
                     'lane': 'past_main',
                     'era': 'past'},
                    {'id': 'fb_minyuu_02_working_rhythm',
                     'chapter_id': 'fb_minyuu_02_working_rhythm',
                     'title': 'Working Rhythm',
                     'code': 'FB02',
                     'type': 'bonus',
                     'thumbnail': 'images/assets/thumbnails/minh/fb_minyuu_02_working_rhythm.webp',
                     'summary': 'Họ làm việc cùng nhau; thói quen, boundary và romantic score bắt đầu tách nhánh.',
                     'duration': 'MVP skeleton',
                     'x': 400,
                     'y': 400,
                     'w': 200,
                     'h': 200,
                     'origin_route': 'minh',
                     'lane': 'past_main',
                     'era': 'past'},
                    {'id': 'fb_minyuu_03_door_left_open',
                     'chapter_id': 'fb_minyuu_03_door_left_open',
                     'title': 'The Door Left Open',
                     'code': 'FB03',
                     'type': 'bonus',
                     'thumbnail': 'images/assets/thumbnails/minh/fb_minyuu_03_door_left_open.webp',
                     'summary': 'Một quyết định về khoảng cách đời sống mở đường cho bạn cũ, người yêu cũ, hoặc still lovers.',
                     'duration': 'MVP skeleton',
                     'x': 720,
                     'y': 400,
                     'w': 200,
                     'h': 200,
                     'origin_route': 'minh',
                     'lane': 'past_main',
                     'era': 'past'},
                    {'id': 'fb_minyuu_04a_old_friends',
                     'chapter_id': 'fb_minyuu_04a_old_friends',
                     'title': 'Điều chưa từng nói',
                     'code': 'FB04A',
                     'type': 'bonus',
                     'thumbnail': 'images/assets/thumbnails/minh/fb_minyuu_04a_old_friends.webp',
                     'summary': 'Chốt hướng bạn cũ thân thiết: có điều suýt nói, nhưng không bước qua.',
                     'duration': 'MVP skeleton',
                     'x': 1040,
                     'y': 160,
                     'w': 200,
                     'h': 200,
                     'origin_route': 'minh',
                     'lane': 'past_upper',
                     'era': 'past'},
                    {'id': 'fb_minyuu_04b_living_together',
                     'chapter_id': 'fb_minyuu_04b_living_together',
                     'title': 'Living Together',
                     'code': 'FB04B',
                     'type': 'bonus',
                     'thumbnail': 'images/assets/thumbnails/minh/fb_minyuu_04b_living_together.webp',
                     'summary': 'Mở hướng từng yêu: đời sống chung làm cảm xúc trở nên cụ thể.',
                     'duration': 'MVP skeleton',
                     'x': 1040,
                     'y': 400,
                     'w': 200,
                     'h': 200,
                     'origin_route': 'minh',
                     'lane': 'past_main',
                     'era': 'past'},
                    {'id': 'fb_minyuu_05b_separation',
                     'chapter_id': 'fb_minyuu_05b_separation',
                     'title': 'Chia xa',
                     'code': 'FB05B',
                     'type': 'bonus',
                     'thumbnail': 'images/assets/thumbnails/minh/fb_minyuu_05b_separation.webp',
                     'summary': 'Chốt người yêu cũ chia xa nhiều năm và lock romance của Minh khỏi route khác.',
                     'duration': 'MVP skeleton',
                     'x': 1360,
                     'y': 400,
                     'w': 200,
                     'h': 200,
                     'origin_route': 'minh',
                     'lane': 'past_main',
                     'era': 'past'},
                    {'id': 'fb_minyuu_04c_no_breakup',
                     'chapter_id': 'fb_minyuu_04c_no_breakup',
                     'title': 'No Breakup',
                     'code': 'FB04C',
                     'type': 'bonus',
                     'thumbnail': 'images/assets/thumbnails/minh/fb_minyuu_04c_no_breakup.webp',
                     'summary': 'Chốt hướng vẫn là người yêu: xa nhau vì hoàn cảnh, không có breakup thật.',
                     'duration': 'MVP skeleton',
                     'x': 1040,
                     'y': 640,
                     'w': 200,
                     'h': 200,
                     'origin_route': 'minh',
                     'lane': 'past_lower',
                     'era': 'past'},
                    {'id': 'marker_four_years_later',
                     'kind': 'time_marker',
                     'chapter_id': None,
                     'title': '4 Years\nLater',
                     'code': '4 Years\nLater',
                     'summary': 'Time gap before the playable present.',
                     'x': 1680,
                     'y': 425,
                     'w': 150,
                     'h': 150,
                     'lane': 'marker',
                     'era': 'marker'},
                    {'id': 'prologue_rain_dream',
                     'chapter_id': 'prologue_rain_dream',
                     'title': 'Giấc mơ trong mưa',
                     'code': 'Prologue',
                     'type': 'core',
                     'thumbnail': 'images/assets/thumbnails/tam/prologue_rain_dream.webp',
                     'summary': 'Tâm mơ về lần gặp trong mưa, gieo cảm giác mơ hồ về Minh nhưng chưa gọi tên.',
                     'duration': 'MVP skeleton',
                     'x': 1960,
                     'y': 400,
                     'w': 200,
                     'h': 200,
                     'origin_route': 'tam',
                     'lane': 'present_main',
                     'era': 'present'},
                    {'id': 'tam_c01_interview_day',
                     'chapter_id': 'tam_c01_interview_day',
                     'title': 'Ngày phỏng vấn',
                     'code': 'C01',
                     'type': 'core',
                     'thumbnail': 'images/assets/thumbnails/tam/tam_c01_interview_day.webp',
                     'summary': 'Tâm và Huyền đi phỏng vấn, được nhận việc, và có va chạm đầu tiên với thế giới mới.',
                     'duration': 'MVP skeleton',
                     'x': 2280,
                     'y': 400,
                     'w': 200,
                     'h': 200,
                     'origin_route': 'tam',
                     'lane': 'present_main',
                     'era': 'present'},
                    {'id': 'tam_c02_company_party',
                     'chapter_id': 'tam_c02_company_party',
                     'title': 'Buổi tiệc công ty',
                     'code': 'C02',
                     'type': 'core',
                     'thumbnail': 'images/assets/thumbnails/tam/tam_c02_company_party.webp',
                     'summary': 'Buổi tiệc công ty mở seed Tâm-Hoàng, Huyền-Hoàng, hoặc hướng chuyên nghiệp.',
                     'duration': 'MVP skeleton',
                     'x': 2600,
                     'y': 400,
                     'w': 200,
                     'h': 200,
                     'origin_route': 'tam',
                     'lane': 'present_main',
                     'era': 'present'},
                    {'id': 'tam_c03_thienan_family',
                     'chapter_id': 'tam_c03_thienan_family',
                     'title': 'Thiên An và gia đình',
                     'code': 'C03',
                     'type': 'core',
                     'thumbnail': 'images/assets/thumbnails/tam/tam_c03_thienan_family.webp',
                     'summary': 'Gia đình, áp lực của Thiên An, và trục trưởng thành của Tâm được mở rộng.',
                     'duration': 'MVP skeleton',
                     'x': 2920,
                     'y': 400,
                     'w': 200,
                     'h': 200,
                     'origin_route': 'tam',
                     'lane': 'present_main',
                     'era': 'present'},
                    {'id': 'hoang_h01_brother_house',
                     'chapter_id': 'hoang_h01_brother_house',
                     'title': 'Nhà của Minh',
                     'code': 'H01',
                     'type': 'pov',
                     'thumbnail': 'images/assets/thumbnails/hoang/hoang_h01_brother_house.webp',
                     'summary': 'Hoàng ở trong không gian của Minh, chọn quà và lộ rõ cách cậu yêu/né/cố gắng.',
                     'duration': 'MVP skeleton',
                     'x': 3240,
                     'y': 160,
                     'w': 200,
                     'h': 200,
                     'origin_route': 'hoang',
                     'lane': 'present_upper',
                     'era': 'present'},
                    {'id': 'tam_c05_sunday_date',
                     'chapter_id': 'tam_c05_sunday_date',
                     'title': 'Buổi hẹn Chủ Nhật',
                     'code': 'C05',
                     'type': 'core',
                     'thumbnail': 'images/assets/thumbnails/tam/tam_c05_sunday_date.webp',
                     'summary': 'Buổi hẹn hoặc outing nhóm kết tinh hướng Tâm-Hoàng / Hoàng-Huyền / friend group.',
                     'duration': 'MVP skeleton',
                     'x': 3560,
                     'y': 400,
                     'w': 200,
                     'h': 200,
                     'origin_route': 'tam',
                     'lane': 'present_main',
                     'era': 'present'},
                    {'id': 'tam_c06_minh_returns',
                     'chapter_id': 'tam_c06_minh_returns',
                     'title': 'Minh về nước',
                     'code': 'C06',
                     'type': 'core',
                     'thumbnail': 'images/assets/thumbnails/tam/tam_c06_minh_returns.webp',
                     'summary': 'Minh trở về Việt Nam và làm lệch nhịp các quan hệ hiện tại.',
                     'duration': 'MVP skeleton',
                     'x': 3880,
                     'y': 400,
                     'w': 200,
                     'h': 200,
                     'origin_route': 'tam',
                     'lane': 'present_main',
                     'era': 'present'},
                    {'id': 'tam_c07_minh_at_company',
                     'chapter_id': 'tam_c07_minh_at_company',
                     'title': 'Minh ở công ty',
                     'code': 'C07',
                     'type': 'core',
                     'thumbnail': 'images/assets/thumbnails/tam/tam_c07_minh_at_company.webp',
                     'summary': 'Minh bước vào không gian công việc, tạo áp lực chuyên môn và cảm xúc.',
                     'duration': 'MVP skeleton',
                     'x': 4200,
                     'y': 400,
                     'w': 200,
                     'h': 200,
                     'origin_route': 'tam',
                     'lane': 'present_main',
                     'era': 'present'},
                    {'id': 'yuuka_c08_festival_arrival',
                     'chapter_id': 'yuuka_c08_festival_arrival',
                     'title': 'Yuuka Nakamura',
                     'code': 'C08',
                     'type': 'core',
                     'thumbnail': 'images/assets/thumbnails/yuuka/yuuka_c08_festival_arrival.webp',
                     'summary': 'Yuuka xuất hiện trung tính tại Film Festival với tư cách đạo diễn, chưa xác nhận quan hệ với Minh.',
                     'duration': 'MVP skeleton',
                     'x': 4520,
                     'y': 400,
                     'w': 200,
                     'h': 200,
                     'origin_route': 'yuuka',
                     'lane': 'present_main',
                     'era': 'present'},
                    {'id': 'yuuka_c09_yuukas_work',
                     'chapter_id': 'yuuka_c09_yuukas_work',
                     'title': "Yuuka's Work",
                     'code': 'C09',
                     'type': 'core',
                     'thumbnail': 'images/assets/thumbnails/yuuka/yuuka_c09_yuukas_work.webp',
                     'summary': 'Buổi chiếu/Q&A đặt trọng tâm vào nghề nghiệp, phong cách làm phim và vị thế của Yuuka.',
                     'duration': 'MVP skeleton',
                     'x': 4840,
                     'y': 400,
                     'w': 200,
                     'h': 200,
                     'origin_route': 'yuuka',
                     'lane': 'present_main',
                     'era': 'present'},
                    {'id': 'work_c10_project_festival_overlap',
                     'chapter_id': 'work_c10_project_festival_overlap',
                     'title': 'Project & Festival',
                     'code': 'C10',
                     'type': 'core',
                     'thumbnail': 'images/assets/thumbnails/work/work_c10_project_festival_overlap.webp',
                     'summary': 'Dự án công ty giao với Film Festival; Yuuka thể hiện năng lực chuyên môn.',
                     'duration': 'MVP skeleton',
                     'x': 5160,
                     'y': 400,
                     'w': 200,
                     'h': 200,
                     'origin_route': 'work',
                     'lane': 'present_main',
                     'era': 'present'},
                    {'id': 'group_c11_social_dinner',
                     'chapter_id': 'group_c11_social_dinner',
                     'title': 'Social Dinner',
                     'code': 'C11',
                     'type': 'core',
                     'thumbnail': 'images/assets/thumbnails/work/group_c11_social_dinner.webp',
                     'summary': 'Bữa tối nhóm phản chiếu trạng thái Minh-Yuuka mà người chơi đã unlock.',
                     'duration': 'MVP skeleton',
                     'x': 5480,
                     'y': 400,
                     'w': 200,
                     'h': 200,
                     'origin_route': 'work',
                     'lane': 'present_main',
                     'era': 'present'},
                    {'id': 'work_c16_project_crisis',
                     'chapter_id': 'work_c16_project_crisis',
                     'title': 'Project Crisis',
                     'code': 'C16',
                     'type': 'core',
                     'thumbnail': 'images/assets/thumbnails/work/work_c16_project_crisis.webp',
                     'summary': 'Khủng hoảng dự án đẩy Tâm, Huyền, Quân, Hoàng và Minh vào các lựa chọn thực tế.',
                     'duration': 'MVP skeleton',
                     'x': 5800,
                     'y': 400,
                     'w': 200,
                     'h': 200,
                     'origin_route': 'work',
                     'lane': 'present_main',
                     'era': 'present'},
                    {'id': 'hoang_h05_shadow_of_minh',
                     'chapter_id': 'hoang_h05_shadow_of_minh',
                     'title': 'Cái bóng của Minh',
                     'code': 'H05',
                     'type': 'pov',
                     'thumbnail': 'images/assets/thumbnails/hoang/hoang_h05_shadow_of_minh.webp',
                     'summary': 'Hoàng đối diện insecurity hoặc sự sáng rõ tùy trạng thái Minh-Yuuka.',
                     'duration': 'MVP skeleton',
                     'x': 6120,
                     'y': 160,
                     'w': 200,
                     'h': 200,
                     'origin_route': 'hoang',
                     'lane': 'present_upper',
                     'era': 'present'},
                    {'id': 'yuuka_c18a_career_interlude',
                     'chapter_id': 'yuuka_c18a_career_interlude',
                     'title': 'Career Interlude',
                     'code': 'C18A',
                     'type': 'bonus',
                     'thumbnail': 'images/assets/thumbnails/yuuka/yuuka_c18a_career_interlude.webp',
                     'summary': 'Nhánh bạn cũ: Yuuka tiếp tục trục sự nghiệp và giữ Minh như một ảnh hưởng cũ.',
                     'duration': 'MVP skeleton',
                     'x': 6440,
                     'y': 160,
                     'w': 200,
                     'h': 200,
                     'origin_route': 'yuuka',
                     'lane': 'branch_upper',
                     'era': 'present'},
                    {'id': 'yuuka_c18b_habit_of_you',
                     'chapter_id': 'yuuka_c18b_habit_of_you',
                     'title': 'The Habit of You',
                     'code': 'C18B',
                     'type': 'bonus',
                     'thumbnail': 'images/assets/thumbnails/yuuka/yuuka_c18b_habit_of_you.webp',
                     'summary': 'Nhánh người yêu cũ: Yuuka nhận ra Minh đã ngấm vào cách cô sống và làm việc.',
                     'duration': 'MVP skeleton',
                     'x': 6440,
                     'y': 400,
                     'w': 200,
                     'h': 200,
                     'origin_route': 'yuuka',
                     'lane': 'branch_main',
                     'era': 'present'},
                    {'id': 'yuuka_c18c_long_distance_interlude',
                     'chapter_id': 'yuuka_c18c_long_distance_interlude',
                     'title': 'Long Distance',
                     'code': 'C18C',
                     'type': 'bonus',
                     'thumbnail': 'images/assets/thumbnails/yuuka/yuuka_c18c_long_distance_interlude.webp',
                     'summary': 'Nhánh vẫn là người yêu: Yuuka cân bằng sự nghiệp với một quan hệ xa nhưng chưa đứt.',
                     'duration': 'MVP skeleton',
                     'x': 6440,
                     'y': 640,
                     'w': 200,
                     'h': 200,
                     'origin_route': 'yuuka',
                     'lane': 'branch_lower',
                     'era': 'present'},
                    {'id': 'c19a_city_after_festival_old_friends',
                     'chapter_id': 'c19a_city_after_festival_old_friends',
                     'title': 'City After Festival',
                     'code': 'C19A',
                     'type': 'bonus',
                     'thumbnail': 'images/assets/thumbnails/minh/c19a_city_after_festival_old_friends.webp',
                     'summary': 'Bản bạn cũ: Minh và Yuuka đặt lại tình bạn và khoảng tiếc nhẹ.',
                     'duration': 'MVP skeleton',
                     'x': 6760,
                     'y': 160,
                     'w': 200,
                     'h': 200,
                     'origin_route': 'minh',
                     'lane': 'branch_upper',
                     'era': 'present'},
                    {'id': 'c19b_city_after_festival_ex_lovers',
                     'chapter_id': 'c19b_city_after_festival_ex_lovers',
                     'title': 'City After Festival',
                     'code': 'C19B',
                     'type': 'bonus',
                     'thumbnail': 'images/assets/thumbnails/minh/c19b_city_after_festival_ex_lovers.webp',
                     'summary': 'Bản người yêu cũ: đối thoại với quá khứ, mở reunion/late/single.',
                     'duration': 'MVP skeleton',
                     'x': 6760,
                     'y': 400,
                     'w': 200,
                     'h': 200,
                     'origin_route': 'minh',
                     'lane': 'branch_main',
                     'era': 'present'},
                    {'id': 'c19c_city_after_festival_still_lovers',
                     'chapter_id': 'c19c_city_after_festival_still_lovers',
                     'title': 'City After Festival',
                     'code': 'C19C',
                     'type': 'bonus',
                     'thumbnail': 'images/assets/thumbnails/minh/c19c_city_after_festival_still_lovers.webp',
                     'summary': 'Bản still lovers: không tái hợp, mà chọn hình dạng cho tình yêu đang tồn tại.',
                     'duration': 'MVP skeleton',
                     'x': 6760,
                     'y': 640,
                     'w': 200,
                     'h': 200,
                     'origin_route': 'minh',
                     'lane': 'branch_lower',
                     'era': 'present'},
                    {'id': 'tam_c20a_tam_minh_possible',
                     'chapter_id': 'tam_c20a_tam_minh_possible',
                     'title': 'Tâm-Minh Possible',
                     'code': 'C20A',
                     'type': 'bonus',
                     'thumbnail': 'images/assets/thumbnails/tam/tam_c20a_tam_minh_possible.webp',
                     'summary': 'Chỉ mở nếu Minh-Yuuka là bạn cũ thân thiết; Tâm kiểm tra cảm xúc với Minh.',
                     'duration': 'MVP skeleton',
                     'x': 7080,
                     'y': 160,
                     'w': 200,
                     'h': 200,
                     'origin_route': 'tam',
                     'lane': 'branch_upper',
                     'era': 'present'},
                    {'id': 'tam_c20b_admiration_vs_love',
                     'chapter_id': 'tam_c20b_admiration_vs_love',
                     'title': 'Admiration vs Love',
                     'code': 'C20B',
                     'type': 'bonus',
                     'thumbnail': 'images/assets/thumbnails/tam/tam_c20b_admiration_vs_love.webp',
                     'summary': 'Nếu Minh đã lock với Yuuka, Tâm học cách phân biệt ngưỡng mộ và tình yêu.',
                     'duration': 'MVP skeleton',
                     'x': 7080,
                     'y': 520,
                     'w': 200,
                     'h': 200,
                     'origin_route': 'tam',
                     'lane': 'branch_lower_merge',
                     'era': 'present'},
                    {'id': 'thienan_c21a_minh_possible',
                     'chapter_id': 'thienan_c21a_minh_possible',
                     'title': 'Thiên An-Minh Possible',
                     'code': 'C21A',
                     'type': 'bonus',
                     'thumbnail': 'images/assets/thumbnails/thienan/thienan_c21a_minh_possible.webp',
                     'summary': 'Chỉ mở nếu Minh-Yuuka là bạn cũ; Thiên An đối diện phần cũ với Minh.',
                     'duration': 'MVP skeleton',
                     'x': 7400,
                     'y': 160,
                     'w': 200,
                     'h': 200,
                     'origin_route': 'thienan',
                     'lane': 'branch_upper',
                     'era': 'present'},
                    {'id': 'thienan_c21b_choose_own_path',
                     'chapter_id': 'thienan_c21b_choose_own_path',
                     'title': 'Chọn hướng riêng',
                     'code': 'C21B',
                     'type': 'bonus',
                     'thumbnail': 'images/assets/thumbnails/thienan/thienan_c21b_choose_own_path.webp',
                     'summary': 'Nếu Minh đã lock với Yuuka, Thiên An chuyển trục sang Quang, gia đình, hoặc tự do.',
                     'duration': 'MVP skeleton',
                     'x': 7400,
                     'y': 520,
                     'w': 200,
                     'h': 200,
                     'origin_route': 'thienan',
                     'lane': 'branch_lower_merge',
                     'era': 'present'},
                    {'id': 'huyen_c22_quan_or_hoang',
                     'chapter_id': 'huyen_c22_quan_or_hoang',
                     'title': 'Huyền / Quân / Hoàng',
                     'code': 'C22',
                     'type': 'core',
                     'thumbnail': 'images/assets/thumbnails/huyen/huyen_c22_quan_or_hoang.webp',
                     'summary': 'Huyền chọn giữa Quân, Hoàng hoặc một hướng độc lập rõ ràng hơn.',
                     'duration': 'MVP skeleton',
                     'x': 7720,
                     'y': 400,
                     'w': 200,
                     'h': 200,
                     'origin_route': 'huyen',
                     'lane': 'present_main',
                     'era': 'present'},
                    {'id': 'minyuu_c23a_old_friends_resolution',
                     'chapter_id': 'minyuu_c23a_old_friends_resolution',
                     'title': 'Old Friends Resolution',
                     'code': 'C23A',
                     'type': 'bonus',
                     'thumbnail': 'images/assets/thumbnails/minh/minyuu_c23a_old_friends_resolution.webp',
                     'summary': 'Kết nhánh bạn cũ: friendship, Yuuka career, hoặc mở đường cho pairing Minh khác.',
                     'duration': 'MVP skeleton',
                     'x': 8040,
                     'y': 160,
                     'w': 200,
                     'h': 200,
                     'origin_route': 'minh',
                     'lane': 'final_upper',
                     'era': 'present'},
                    {'id': 'minyuu_c23b_ex_lovers_resolution',
                     'chapter_id': 'minyuu_c23b_ex_lovers_resolution',
                     'title': 'Ex Lovers Resolution',
                     'code': 'C23B',
                     'type': 'bonus',
                     'thumbnail': 'images/assets/thumbnails/minh/minyuu_c23b_ex_lovers_resolution.webp',
                     'summary': 'Kết nhánh người yêu cũ: quay lại, muộn hơn, hoặc cả hai độc thân.',
                     'duration': 'MVP skeleton',
                     'x': 8040,
                     'y': 400,
                     'w': 200,
                     'h': 200,
                     'origin_route': 'minh',
                     'lane': 'final_main',
                     'era': 'present'},
                    {'id': 'minyuu_c23c_still_lovers_resolution',
                     'chapter_id': 'minyuu_c23c_still_lovers_resolution',
                     'title': 'Still Lovers Resolution',
                     'code': 'C23C',
                     'type': 'bonus',
                     'thumbnail': 'images/assets/thumbnails/minh/minyuu_c23c_still_lovers_resolution.webp',
                     'summary': 'Kết nhánh still lovers: private/public/non-marriage/long-distance.',
                     'duration': 'MVP skeleton',
                     'x': 8040,
                     'y': 640,
                     'w': 200,
                     'h': 200,
                     'origin_route': 'minh',
                     'lane': 'final_lower',
                     'era': 'present'},
                    {'id': 'final_c24_last_choices',
                     'chapter_id': 'final_c24_last_choices',
                     'title': 'Final Choices',
                     'code': 'C24',
                     'type': 'core',
                     'thumbnail': 'images/assets/thumbnails/final/final_c24_last_choices.webp',
                     'summary': 'Các lựa chọn cuối cùng gom lại route support và dẫn sang ending resolver.',
                     'duration': 'MVP skeleton',
                     'x': 8360,
                     'y': 400,
                     'w': 200,
                     'h': 200,
                     'origin_route': 'final',
                     'lane': 'final_main',
                     'era': 'final'}]}

    TIMELINE_MAP_CONNECTIONS = {'chronology': [{'from': 'fb_minyuu_01_first_frame', 'to': 'fb_minyuu_02_working_rhythm', 'style': 'normal'},
                    {'from': 'fb_minyuu_02_working_rhythm', 'to': 'fb_minyuu_03_door_left_open', 'style': 'normal'},
                    {'from': 'fb_minyuu_03_door_left_open', 'to': 'fb_minyuu_04a_old_friends', 'style': 'branch'},
                    {'from': 'fb_minyuu_03_door_left_open', 'to': 'fb_minyuu_04b_living_together', 'style': 'branch'},
                    {'from': 'fb_minyuu_03_door_left_open', 'to': 'fb_minyuu_04c_no_breakup', 'style': 'branch'},
                    {'from': 'fb_minyuu_04b_living_together', 'to': 'fb_minyuu_05b_separation', 'style': 'normal'},
                    {'from': 'fb_minyuu_04a_old_friends', 'to': 'marker_four_years_later', 'style': 'merge'},
                    {'from': 'fb_minyuu_05b_separation', 'to': 'marker_four_years_later', 'style': 'merge'},
                    {'from': 'fb_minyuu_04c_no_breakup', 'to': 'marker_four_years_later', 'style': 'merge'},
                    {'from': 'marker_four_years_later', 'to': 'prologue_rain_dream', 'style': 'normal'},
                    {'from': 'prologue_rain_dream', 'to': 'tam_c01_interview_day', 'style': 'normal'},
                    {'from': 'tam_c01_interview_day', 'to': 'tam_c02_company_party', 'style': 'normal'},
                    {'from': 'tam_c02_company_party', 'to': 'tam_c03_thienan_family', 'style': 'normal'},
                    {'from': 'tam_c03_thienan_family', 'to': 'hoang_h01_brother_house', 'style': 'branch'},
                    {'from': 'hoang_h01_brother_house', 'to': 'tam_c05_sunday_date', 'style': 'merge'},
                    {'from': 'tam_c05_sunday_date', 'to': 'tam_c06_minh_returns', 'style': 'normal'},
                    {'from': 'tam_c06_minh_returns', 'to': 'tam_c07_minh_at_company', 'style': 'normal'},
                    {'from': 'tam_c07_minh_at_company', 'to': 'yuuka_c08_festival_arrival', 'style': 'normal'},
                    {'from': 'yuuka_c08_festival_arrival', 'to': 'yuuka_c09_yuukas_work', 'style': 'normal'},
                    {'from': 'yuuka_c09_yuukas_work', 'to': 'work_c10_project_festival_overlap', 'style': 'normal'},
                    {'from': 'work_c10_project_festival_overlap', 'to': 'group_c11_social_dinner', 'style': 'normal'},
                    {'from': 'group_c11_social_dinner', 'to': 'work_c16_project_crisis', 'style': 'normal'},
                    {'from': 'work_c16_project_crisis', 'to': 'hoang_h05_shadow_of_minh', 'style': 'branch'},
                    {'from': 'hoang_h05_shadow_of_minh', 'to': 'yuuka_c18a_career_interlude', 'style': 'branch'},
                    {'from': 'hoang_h05_shadow_of_minh', 'to': 'yuuka_c18b_habit_of_you', 'style': 'branch'},
                    {'from': 'hoang_h05_shadow_of_minh', 'to': 'yuuka_c18c_long_distance_interlude', 'style': 'branch'},
                    {'from': 'yuuka_c18a_career_interlude', 'to': 'c19a_city_after_festival_old_friends', 'style': 'normal'},
                    {'from': 'yuuka_c18b_habit_of_you', 'to': 'c19b_city_after_festival_ex_lovers', 'style': 'normal'},
                    {'from': 'yuuka_c18c_long_distance_interlude', 'to': 'c19c_city_after_festival_still_lovers', 'style': 'normal'},
                    {'from': 'c19a_city_after_festival_old_friends', 'to': 'tam_c20a_tam_minh_possible', 'style': 'normal'},
                    {'from': 'c19b_city_after_festival_ex_lovers', 'to': 'tam_c20b_admiration_vs_love', 'style': 'merge'},
                    {'from': 'c19c_city_after_festival_still_lovers', 'to': 'tam_c20b_admiration_vs_love', 'style': 'merge'},
                    {'from': 'tam_c20a_tam_minh_possible', 'to': 'thienan_c21a_minh_possible', 'style': 'normal'},
                    {'from': 'tam_c20b_admiration_vs_love', 'to': 'thienan_c21b_choose_own_path', 'style': 'normal'},
                    {'from': 'thienan_c21a_minh_possible', 'to': 'huyen_c22_quan_or_hoang', 'style': 'merge'},
                    {'from': 'thienan_c21b_choose_own_path', 'to': 'huyen_c22_quan_or_hoang', 'style': 'merge'},
                    {'from': 'huyen_c22_quan_or_hoang', 'to': 'minyuu_c23a_old_friends_resolution', 'style': 'branch'},
                    {'from': 'huyen_c22_quan_or_hoang', 'to': 'minyuu_c23b_ex_lovers_resolution', 'style': 'branch'},
                    {'from': 'huyen_c22_quan_or_hoang', 'to': 'minyuu_c23c_still_lovers_resolution', 'style': 'branch'},
                    {'from': 'minyuu_c23a_old_friends_resolution', 'to': 'final_c24_last_choices', 'style': 'merge'},
                    {'from': 'minyuu_c23b_ex_lovers_resolution', 'to': 'final_c24_last_choices', 'style': 'merge'},
                    {'from': 'minyuu_c23c_still_lovers_resolution', 'to': 'final_c24_last_choices', 'style': 'merge'}]}

    TIMELINE_LANE_LABELS = {'chronology': [{'text': 'PAST / FLASHBACK', 'x': 80, 'y': 56, 'w': 1180},
                    {'text': 'TIME SKIP', 'x': 1585, 'y': 56, 'w': 260},
                    {'text': 'GAME START', 'x': 1930, 'y': 56, 'w': 300},
                    {'text': 'PRESENT MAIN LINE', 'x': 2280, 'y': 56, 'w': 3820},
                    {'text': 'ROUTE BRANCHES', 'x': 6360, 'y': 56, 'w': 1380},
                    {'text': 'FINAL ARC', 'x': 8000, 'y': 56, 'w': 700}]}

    TIMELINE_NODE_META = {'prologue_rain_dream': {'display_title': 'Prologue - Giấc mơ trong mưa',
                             'summary': 'Tâm mơ về lần gặp trong mưa, gieo cảm giác mơ hồ về Minh nhưng chưa gọi tên.',
                             'conditions': [],
                             'stat_modifiers': []},
     'tam_c01_interview_day': {'display_title': 'C01 - Ngày phỏng vấn',
                               'summary': 'Tâm và Huyền đi phỏng vấn, được nhận việc, và có va chạm đầu tiên với thế giới mới.',
                               'conditions': [],
                               'stat_modifiers': []},
     'tam_c02_company_party': {'display_title': 'C02 - Buổi tiệc công ty',
                               'summary': 'Buổi tiệc công ty mở seed Tâm-Hoàng, Huyền-Hoàng, hoặc hướng chuyên nghiệp.',
                               'conditions': [],
                               'stat_modifiers': []},
     'tam_c03_thienan_family': {'display_title': 'C03 - Thiên An và gia đình',
                                'summary': 'Gia đình, áp lực của Thiên An, và trục trưởng thành của Tâm được mở rộng.',
                                'conditions': [],
                                'stat_modifiers': []},
     'tam_c05_sunday_date': {'display_title': 'C05 - Buổi hẹn Chủ Nhật',
                             'summary': 'Buổi hẹn hoặc outing nhóm kết tinh hướng Tâm-Hoàng / Hoàng-Huyền / friend group.',
                             'conditions': [],
                             'stat_modifiers': []},
     'tam_c06_minh_returns': {'display_title': 'C06 - Minh về nước',
                              'summary': 'Minh trở về Việt Nam và làm lệch nhịp các quan hệ hiện tại.',
                              'conditions': [],
                              'stat_modifiers': []},
     'tam_c07_minh_at_company': {'display_title': 'C07 - Minh ở công ty',
                                 'summary': 'Minh bước vào không gian công việc, tạo áp lực chuyên môn và cảm xúc.',
                                 'conditions': [],
                                 'stat_modifiers': []},
     'tam_c20a_tam_minh_possible': {'display_title': 'C20A - Tâm-Minh Possible',
                                    'summary': 'Chỉ mở nếu Minh-Yuuka là bạn cũ thân thiết; Tâm kiểm tra cảm xúc với Minh.',
                                    'conditions': ['Requires Minh-Yuuka relation: old_close_friends.'],
                                    'stat_modifiers': []},
     'tam_c20b_admiration_vs_love': {'display_title': 'C20B - Admiration vs Love',
                                     'summary': 'Nếu Minh đã lock với Yuuka, Tâm học cách phân biệt ngưỡng mộ và tình yêu.',
                                     'conditions': [],
                                     'stat_modifiers': []},
     'hoang_h01_brother_house': {'display_title': 'H01 - Nhà của Minh',
                                 'summary': 'Hoàng ở trong không gian của Minh, chọn quà và lộ rõ cách cậu yêu/né/cố gắng.',
                                 'conditions': [],
                                 'stat_modifiers': []},
     'hoang_h05_shadow_of_minh': {'display_title': 'H05 - Cái bóng của Minh',
                                  'summary': 'Hoàng đối diện insecurity hoặc sự sáng rõ tùy trạng thái Minh-Yuuka.',
                                  'conditions': [],
                                  'stat_modifiers': []},
     'yuuka_c08_festival_arrival': {'display_title': 'C08 - Yuuka Nakamura',
                                    'summary': 'Yuuka xuất hiện trung tính tại Film Festival với tư cách đạo diễn, chưa xác nhận quan hệ với '
                                               'Minh.',
                                    'conditions': ['Introduces Yuuka neutrally as director and old friend; relationship is not confirmed '
                                                   'here.'],
                                    'stat_modifiers': ['Unlocks Minh-Yuuka flashback layer.']},
     'yuuka_c09_yuukas_work': {'display_title': "C09 - Yuuka's Work",
                               'summary': 'Buổi chiếu/Q&A đặt trọng tâm vào nghề nghiệp, phong cách làm phim và vị thế của Yuuka.',
                               'conditions': [],
                               'stat_modifiers': []},
     'yuuka_c18a_career_interlude': {'display_title': 'C18A - Career Interlude',
                                     'summary': 'Nhánh bạn cũ: Yuuka tiếp tục trục sự nghiệp và giữ Minh như một ảnh hưởng cũ.',
                                     'conditions': ['Requires Minh-Yuuka relation: old_close_friends.'],
                                     'stat_modifiers': []},
     'yuuka_c18b_habit_of_you': {'display_title': 'C18B - The Habit of You',
                                 'summary': 'Nhánh người yêu cũ: Yuuka nhận ra Minh đã ngấm vào cách cô sống và làm việc.',
                                 'conditions': ['Requires or leads to Minh-Yuuka relation: ex_lovers_long_separated.'],
                                 'stat_modifiers': []},
     'yuuka_c18c_long_distance_interlude': {'display_title': 'C18C - Long Distance',
                                            'summary': 'Nhánh vẫn là người yêu: Yuuka cân bằng sự nghiệp với một quan hệ xa nhưng chưa đứt.',
                                            'conditions': ['Requires or leads to Minh-Yuuka relation: still_lovers.'],
                                            'stat_modifiers': []},
     'fb_minyuu_01_first_frame': {'display_title': 'FB01 - First Frame',
                                  'summary': 'Minh và Yuuka gặp nhau trong bối cảnh học tập/nghề phim; respect và friction bắt đầu.',
                                  'conditions': [],
                                  'stat_modifiers': []},
     'fb_minyuu_02_working_rhythm': {'display_title': 'FB02 - Working Rhythm',
                                     'summary': 'Họ làm việc cùng nhau; thói quen, boundary và romantic score bắt đầu tách nhánh.',
                                     'conditions': [],
                                     'stat_modifiers': []},
     'fb_minyuu_03_door_left_open': {'display_title': 'FB03 - The Door Left Open',
                                     'summary': 'Một quyết định về khoảng cách đời sống mở đường cho bạn cũ, người yêu cũ, hoặc still lovers.',
                                     'conditions': [],
                                     'stat_modifiers': ['Branches to old friends / ex lovers / still lovers verdict path.']},
     'fb_minyuu_04a_old_friends': {'display_title': 'FB04A - Điều chưa từng nói',
                                   'summary': 'Chốt hướng bạn cũ thân thiết: có điều suýt nói, nhưng không bước qua.',
                                   'conditions': ['Requires Minh-Yuuka relation: old_close_friends.'],
                                   'stat_modifiers': []},
     'fb_minyuu_04b_living_together': {'display_title': 'FB04B - Living Together',
                                       'summary': 'Mở hướng từng yêu: đời sống chung làm cảm xúc trở nên cụ thể.',
                                       'conditions': [],
                                       'stat_modifiers': []},
     'fb_minyuu_05b_separation': {'display_title': 'FB05B - Chia xa',
                                  'summary': 'Chốt người yêu cũ chia xa nhiều năm và lock romance của Minh khỏi route khác.',
                                  'conditions': ['Requires or leads to Minh-Yuuka relation: ex_lovers_long_separated.'],
                                  'stat_modifiers': []},
     'fb_minyuu_04c_no_breakup': {'display_title': 'FB04C - No Breakup',
                                  'summary': 'Chốt hướng vẫn là người yêu: xa nhau vì hoàn cảnh, không có breakup thật.',
                                  'conditions': ['Requires or leads to Minh-Yuuka relation: still_lovers.'],
                                  'stat_modifiers': []},
     'c19a_city_after_festival_old_friends': {'display_title': 'C19A - City After Festival',
                                              'summary': 'Bản bạn cũ: Minh và Yuuka đặt lại tình bạn và khoảng tiếc nhẹ.',
                                              'conditions': ['Requires Minh-Yuuka relation: old_close_friends.'],
                                              'stat_modifiers': []},
     'c19b_city_after_festival_ex_lovers': {'display_title': 'C19B - City After Festival',
                                            'summary': 'Bản người yêu cũ: đối thoại với quá khứ, mở reunion/late/single.',
                                            'conditions': ['Requires or leads to Minh-Yuuka relation: ex_lovers_long_separated.'],
                                            'stat_modifiers': []},
     'c19c_city_after_festival_still_lovers': {'display_title': 'C19C - City After Festival',
                                               'summary': 'Bản still lovers: không tái hợp, mà chọn hình dạng cho tình yêu đang tồn tại.',
                                               'conditions': ['Requires or leads to Minh-Yuuka relation: still_lovers.'],
                                               'stat_modifiers': []},
     'minyuu_c23a_old_friends_resolution': {'display_title': 'C23A - Old Friends Resolution',
                                            'summary': 'Kết nhánh bạn cũ: friendship, Yuuka career, hoặc mở đường cho pairing Minh khác.',
                                            'conditions': ['Requires Minh-Yuuka relation: old_close_friends.'],
                                            'stat_modifiers': []},
     'minyuu_c23b_ex_lovers_resolution': {'display_title': 'C23B - Ex Lovers Resolution',
                                          'summary': 'Kết nhánh người yêu cũ: quay lại, muộn hơn, hoặc cả hai độc thân.',
                                          'conditions': ['Requires or leads to Minh-Yuuka relation: ex_lovers_long_separated.'],
                                          'stat_modifiers': []},
     'minyuu_c23c_still_lovers_resolution': {'display_title': 'C23C - Still Lovers Resolution',
                                             'summary': 'Kết nhánh still lovers: private/public/non-marriage/long-distance.',
                                             'conditions': ['Requires or leads to Minh-Yuuka relation: still_lovers.'],
                                             'stat_modifiers': []},
     'thienan_c21a_minh_possible': {'display_title': 'C21A - Thiên An-Minh Possible',
                                    'summary': 'Chỉ mở nếu Minh-Yuuka là bạn cũ; Thiên An đối diện phần cũ với Minh.',
                                    'conditions': ['Requires Minh-Yuuka relation: old_close_friends.'],
                                    'stat_modifiers': []},
     'thienan_c21b_choose_own_path': {'display_title': 'C21B - Chọn hướng riêng',
                                      'summary': 'Nếu Minh đã lock với Yuuka, Thiên An chuyển trục sang Quang, gia đình, hoặc tự do.',
                                      'conditions': [],
                                      'stat_modifiers': []},
     'huyen_c22_quan_or_hoang': {'display_title': 'C22 - Huyền / Quân / Hoàng',
                                 'summary': 'Huyền chọn giữa Quân, Hoàng hoặc một hướng độc lập rõ ràng hơn.',
                                 'conditions': [],
                                 'stat_modifiers': []},
     'work_c10_project_festival_overlap': {'display_title': 'C10 - Project & Festival',
                                           'summary': 'Dự án công ty giao với Film Festival; Yuuka thể hiện năng lực chuyên môn.',
                                           'conditions': [],
                                           'stat_modifiers': []},
     'group_c11_social_dinner': {'display_title': 'C11 - Social Dinner',
                                 'summary': 'Bữa tối nhóm phản chiếu trạng thái Minh-Yuuka mà người chơi đã unlock.',
                                 'conditions': [],
                                 'stat_modifiers': []},
     'work_c16_project_crisis': {'display_title': 'C16 - Project Crisis',
                                 'summary': 'Khủng hoảng dự án đẩy Tâm, Huyền, Quân, Hoàng và Minh vào các lựa chọn thực tế.',
                                 'conditions': [],
                                 'stat_modifiers': []},
     'final_c24_last_choices': {'display_title': 'C24 - Final Choices',
                                'summary': 'Các lựa chọn cuối cùng gom lại route support và dẫn sang ending resolver.',
                                'conditions': [],
                                'stat_modifiers': ['Calls ending_resolver after final choice support is set.']}}


    def timeline_get_default_route_id():
        return TIMELINE_DEFAULT_ROUTE_ID

    def timeline_get_render_state_signature(route_id=None):
        route_id = timeline_normalize_route_id(route_id)
        progress_state = globals().get("progress", {})
        return (
            route_id,
            timeline_freeze_signature(progress_state.get("completed", [])),
            timeline_freeze_signature(progress_state.get("available", [])),
            timeline_freeze_signature(progress_state.get("excluded", [])),
            timeline_freeze_signature(progress_state.get("hidden", [])),
            timeline_freeze_signature(progress_state.get("temporarily_hidden", [])),
            timeline_freeze_signature(progress_state.get("route_status", {})),
            timeline_freeze_signature(progress_state.get("route_focus", {})),
            timeline_freeze_signature(progress_state.get("relationship_directions", {})),
            timeline_freeze_signature(progress_state.get("player_flags", [])),
            timeline_freeze_signature(getattr(persistent, "timeline_bookmarks", [])),
            bool(timeline_debug_reveal_spoilers()),
        )

    def timeline_build_screen_state(route_id=None, selected_node_id=None, viewport_width=1744):
        route_id = timeline_normalize_route_id(route_id)
        cache_key = (timeline_get_render_state_signature(route_id), selected_node_id, viewport_width)
        cached = TIMELINE_SCREEN_STATE_CACHE.get(cache_key)
        if cached:
            return cached

        nodes = timeline_get_nodes(route_id)
        node_lookup = {
            node.get("id"): node
            for node in nodes
            if node.get("id")
        }
        visible_nodes = [node for node in nodes if timeline_should_render_node(node, route_id)]
        visible_node_ids = {
            node.get("id")
            for node in visible_nodes
            if node.get("id")
        }
        render_offset_x = timeline_get_render_offset_x(route_id, visible_nodes=visible_nodes)
        node_render_positions = {
            node["id"]: node.get("x", 0) - render_offset_x
            for node in visible_nodes
            if node.get("id")
        }
        node_states = {
            node["id"]: timeline_get_node_state(node)
            for node in visible_nodes
            if node.get("id")
        }

        visible_connections = []
        for connection in timeline_get_connections(route_id):
            from_node = node_lookup.get(connection.get("from"))
            to_node = node_lookup.get(connection.get("to"))

            if not from_node or not to_node:
                continue

            from_node_id = from_node.get("id")
            to_node_id = to_node.get("id")
            if from_node_id not in visible_node_ids or to_node_id not in visible_node_ids:
                continue

            style_name = connection.get("style", "normal")
            line_color = "#f0cc72" if style_name in ["branch", "merge", "dashed"] else "#d7b77d"
            from_w = from_node.get("w", 200) + (0 if timeline_node_is_marker(from_node) else 44)
            from_h = from_node.get("h", 200) + (0 if timeline_node_is_marker(from_node) else 38)
            to_h = to_node.get("h", 200) + (0 if timeline_node_is_marker(to_node) else 38)
            from_x = node_render_positions.get(from_node_id, from_node.get("x", 0) - render_offset_x) + from_w
            from_y = from_node["y"] + int(from_h / 2)
            to_x = node_render_positions.get(to_node_id, to_node.get("x", 0) - render_offset_x)
            to_y = to_node["y"] + int(to_h / 2)
            mid_x = int((from_x + to_x) / 2)

            connection_model = dict(connection)
            connection_model.update({
                "from_x": from_x,
                "from_y": from_y,
                "to_x": to_x,
                "to_y": to_y,
                "mid_x": mid_x,
                "horizontal_width": max(1, to_x - from_x),
                "line_color": line_color,
                "dot_color": "#f5d7a6",
            })
            visible_connections.append(connection_model)

        visible_lane_labels = []
        for label in timeline_get_lane_labels(route_id):
            if not timeline_should_render_lane_label(route_id, label, visible_nodes=visible_nodes):
                continue

            label_model = dict(label)
            label_model["render_x"] = label.get("x", 0) - render_offset_x
            visible_lane_labels.append(label_model)

        canvas_size = timeline_get_canvas_size(
            route_id,
            visible_nodes=visible_nodes,
            node_render_positions=node_render_positions,
            render_offset_x=render_offset_x,
        )
        resolved_node = timeline_resolve_selected_node(route_id, selected_node_id)
        active_node_id = resolved_node["id"] if resolved_node else None
        selected_chapter_id = resolved_node.get("chapter_id") if resolved_node else None
        selected_node_state = timeline_get_node_state(resolved_node) if resolved_node else None
        screen_state = {
            "route_id": route_id,
            "nodes": nodes,
            "visible_nodes": visible_nodes,
            "visible_connections": visible_connections,
            "visible_lane_labels": visible_lane_labels,
            "node_lookup": node_lookup,
            "node_render_positions": node_render_positions,
            "node_states": node_states,
            "render_offset_x": render_offset_x,
            "resolved_node": resolved_node,
            "active_node_id": active_node_id,
            "selected_chapter_id": selected_chapter_id,
            "selected_node_state": selected_node_state,
            "selected_can_play": bool(
                selected_chapter_id
                and selected_node_state == "current"
                and timeline_has_runtime_chapter(selected_chapter_id)
            ),
            "canvas_size": canvas_size,
            "viewport_xinitial": timeline_get_viewport_xinitial(
                route_id,
                active_node_id,
                viewport_width,
                node=resolved_node,
                canvas_size=canvas_size,
                node_render_positions=node_render_positions,
                render_offset_x=render_offset_x,
            ),
        }

        if len(TIMELINE_SCREEN_STATE_CACHE) >= 24:
            TIMELINE_SCREEN_STATE_CACHE.clear()
        TIMELINE_SCREEN_STATE_CACHE[cache_key] = screen_state
        return screen_state

    def timeline_normalize_route_id(route_id=None):
        if route_id in TIMELINE_MAP_NODES:
            return route_id
        return TIMELINE_DEFAULT_ROUTE_ID

    def timeline_get_nodes(route_id=None):
        route_id = timeline_normalize_route_id(route_id)
        return TIMELINE_MAP_NODES.get(route_id, [])

    def timeline_get_connections(route_id=None):
        route_id = timeline_normalize_route_id(route_id)
        return TIMELINE_MAP_CONNECTIONS.get(route_id, [])

    def timeline_get_lane_labels(route_id=None):
        route_id = timeline_normalize_route_id(route_id)
        return TIMELINE_LANE_LABELS.get(route_id, [])

    def timeline_get_route_ids():
        return [route["id"] for route in TIMELINE_ROUTES]

    def timeline_find_node(route_id, node_id):
        if not node_id:
            return None
        route_id = timeline_normalize_route_id(route_id)
        for node in timeline_get_nodes(route_id):
            if node["id"] == node_id:
                return node
        return None

    def timeline_find_node_by_chapter(route_id, chapter_id):
        if not chapter_id:
            return None
        route_id = timeline_normalize_route_id(route_id)
        for node in timeline_get_nodes(route_id):
            if node.get("chapter_id") == chapter_id:
                return node
        return None

    def timeline_find_node_any_route(chapter_id):
        for route_id in timeline_get_route_ids():
            node = timeline_find_node_by_chapter(route_id, chapter_id)
            if node:
                return route_id, node
        return None, None

    def timeline_get_chapter_data(chapter_id):
        if chapter_id and "CHAPTERS" in globals() and chapter_id in CHAPTERS:
            return CHAPTERS[chapter_id]
        return None

    def timeline_node_is_marker(node):
        return bool(node and node.get("kind") == "time_marker")

    def timeline_is_completed(chapter_id):
        if not chapter_id:
            return False
        try:
            return chapter_id in progress.get("completed", [])
        except Exception:
            return False

    def timeline_is_excluded(chapter_id):
        if not chapter_id:
            return False
        try:
            return chapter_id in progress.get("excluded", [])
        except Exception:
            return False

    def timeline_is_hidden(chapter_id):
        if not chapter_id:
            return False
        try:
            return chapter_id in progress.get("hidden", [])
        except Exception:
            return False

    def timeline_is_available(chapter_id):
        if not chapter_id:
            return False
        try:
            return get_chapter_state(chapter_id) == "available"
        except Exception:
            chapter = timeline_get_chapter_data(chapter_id)
            if not chapter:
                return False
            prerequisites = chapter.get("prerequisites", [])
            prerequisites_any = chapter.get("prerequisites_any", [])
            if prerequisites and not all(timeline_is_completed(req_id) for req_id in prerequisites):
                return False
            if prerequisites_any and not any(timeline_is_completed(req_id) for req_id in prerequisites_any):
                return False
            return True

    def timeline_get_node_state(node):
        if timeline_node_is_marker(node):
            return "marker"

        chapter_id = node.get("chapter_id") if node else None
        if not chapter_id:
            return "locked"

        if timeline_is_completed(chapter_id):
            return "completed"
        if timeline_is_excluded(chapter_id):
            return "locked"
        if timeline_is_hidden(chapter_id):
            return "locked"
        if timeline_is_available(chapter_id):
            return "current"
        return "locked"

    def timeline_has_runtime_chapter(chapter_id):
        return timeline_get_chapter_data(chapter_id) is not None

    def timeline_route_has_state(route_id, state):
        return any(timeline_get_node_state(node) == state for node in timeline_get_nodes(route_id) if not timeline_node_is_marker(node))

    def timeline_get_first_route_with_state(state):
        for route in TIMELINE_ROUTES:
            route_id = route["id"]
            if timeline_route_has_state(route_id, state):
                return route_id
        return None

    def timeline_get_first_selectable_node(route_id=None):
        route_id = timeline_normalize_route_id(route_id)
        nodes = [node for node in timeline_get_nodes(route_id) if timeline_should_render_chapter_node(node)]

        for node in nodes:
            if timeline_get_node_state(node) == "current":
                return node["id"]

        for node in nodes:
            if timeline_get_node_state(node) == "completed":
                return node["id"]

        for node in nodes:
            if node.get("chapter_id") == "prologue_rain_dream":
                return node["id"]

        if nodes:
            return nodes[0]["id"]

        return None

    def timeline_resolve_selected_node(route_id, selected_node_id):
        route_id = timeline_normalize_route_id(route_id)
        node = timeline_find_node(route_id, selected_node_id)
        if node and timeline_should_render_chapter_node(node):
            return node
        return timeline_find_node(route_id, timeline_get_first_selectable_node(route_id))

    def timeline_resolve_route_selection(selected_route=None, selected_node_id=None):
        route_id = timeline_normalize_route_id(selected_route)

        selected_node = timeline_find_node(route_id, selected_node_id)
        if selected_node and timeline_should_render_chapter_node(selected_node):
            return route_id, selected_node["id"]

        if timeline_route_has_state(route_id, "current"):
            return route_id, timeline_get_first_selectable_node(route_id)

        current_route = timeline_get_first_route_with_state("current")
        if current_route:
            return current_route, timeline_get_first_selectable_node(current_route)

        first_node = timeline_get_first_selectable_node(route_id)
        if first_node:
            return route_id, first_node

        for route in TIMELINE_ROUTES:
            fallback_route = route["id"]
            fallback_node = timeline_get_first_selectable_node(fallback_route)
            if fallback_node:
                return fallback_route, fallback_node

        return route_id, None

    def timeline_debug_reveal_spoilers():
        reveal_fn = globals().get("progression_debug_reveal_spoilers", None)
        if callable(reveal_fn):
            return reveal_fn()
        try:
            normalize_timeline_persistent_state()
            return bool(getattr(persistent, "debug_reveal_spoilers", False))
        except Exception:
            return False

    def timeline_can_show_debug_reveal_toggle():
        try:
            if config.developer:
                return True
        except Exception:
            pass
        try:
            normalize_timeline_persistent_state()
            return bool(getattr(persistent, "debugging_mode", False))
        except Exception:
            return False

    def timeline_debug_reveal_button_label():
        return "Hide Spoilers" if timeline_debug_reveal_spoilers() else "Reveal Spoilers"

    def timeline_toggle_debug_reveal():
        # Called from a screen action. It must not return True/False, otherwise
        # renpy.call_screen() may treat that value as the screen result and
        # route_map_timeline will try to unpack a boolean.
        toggle_fn = globals().get("debug_toggle_spoiler_reveal", None)
        if callable(toggle_fn):
            toggle_fn()
        else:
            normalize_timeline_persistent_state()
            persistent.debug_reveal_spoilers = not bool(getattr(persistent, "debug_reveal_spoilers", False))
        try:
            renpy.restart_interaction()
        except Exception:
            pass
        return None

    def timeline_get_debug_node_line(node):
        if not node:
            return ""
        chapter_id = node.get("chapter_id") or node.get("id", "")
        origin_route = node.get("origin_route") or node.get("lane", "")
        return "Debug: %s · track=%s · source_x=%s y=%s" % (chapter_id, origin_route, node.get("x", "?"), node.get("y", "?"))

    def timeline_get_background_displayable():
        if renpy.loadable(TIMELINE_MAP_BACKGROUND):
            return TIMELINE_MAP_BACKGROUND
        return TIMELINE_FALLBACK_BACKGROUND

    def timeline_should_reveal_node(node_or_chapter_id):
        if isinstance(node_or_chapter_id, dict) and timeline_node_is_marker(node_or_chapter_id):
            return True

        chapter_id = node_or_chapter_id
        if isinstance(node_or_chapter_id, dict):
            chapter_id = node_or_chapter_id.get("chapter_id")

        if not chapter_id:
            return False

        if timeline_debug_reveal_spoilers():
            return True

        reveal_fn = globals().get("chapter_is_revealed", None)
        if callable(reveal_fn):
            return reveal_fn(chapter_id)

        try:
            return get_chapter_state(chapter_id) in ["available", "completed"]
        except Exception:
            return timeline_is_completed(chapter_id) or timeline_is_available(chapter_id)

    def timeline_should_render_chapter_node(node):
        # Player-facing timeline hides unrevealed chapters completely. This avoids
        # spoiling route structure through masked nodes. Debug reveal still shows
        # the full authored map for validation.
        if not node or timeline_node_is_marker(node):
            return False
        return timeline_should_reveal_node(node)

    def timeline_marker_has_visible_context(route_id, marker_node):
        if timeline_debug_reveal_spoilers():
            return True
        if not marker_node:
            return False

        marker_x = marker_node.get("x", 0)
        has_visible_before = False
        has_visible_after = False

        for candidate in timeline_get_nodes(route_id):
            if timeline_node_is_marker(candidate):
                continue
            if not timeline_should_render_chapter_node(candidate):
                continue
            if candidate.get("x", 0) < marker_x:
                has_visible_before = True
            if candidate.get("x", 0) > marker_x:
                has_visible_after = True

        return has_visible_before and has_visible_after

    def timeline_should_render_node(node, route_id=None):
        if timeline_node_is_marker(node):
            return timeline_marker_has_visible_context(timeline_normalize_route_id(route_id), node)
        return timeline_should_render_chapter_node(node)

    def timeline_get_visible_nodes(route_id=None, include_markers=True):
        route_id = timeline_normalize_route_id(route_id)
        visible = []
        for node in timeline_get_nodes(route_id):
            if timeline_node_is_marker(node) and not include_markers:
                continue
            if timeline_should_render_node(node, route_id):
                visible.append(node)
        return visible

    def timeline_should_render_connection(route_id, connection):
        route_id = timeline_normalize_route_id(route_id)
        from_node = timeline_find_node(route_id, connection.get("from"))
        to_node = timeline_find_node(route_id, connection.get("to"))
        return bool(from_node and to_node and timeline_should_render_node(from_node, route_id) and timeline_should_render_node(to_node, route_id))

    def timeline_get_render_offset_x(route_id=None, visible_nodes=None):
        route_id = timeline_normalize_route_id(route_id)
        visible = visible_nodes if visible_nodes is not None else timeline_get_visible_nodes(route_id)
        if not visible:
            return 0
        min_x = min(node.get("x", 0) for node in visible)
        return max(0, min_x - 80)

    def timeline_get_node_render_x(route_id, node, render_offset_x=None):
        if not node:
            return 0
        offset_x = render_offset_x if render_offset_x is not None else timeline_get_render_offset_x(route_id)
        return node.get("x", 0) - offset_x

    def timeline_get_lane_label_render_x(route_id, label, render_offset_x=None):
        offset_x = render_offset_x if render_offset_x is not None else timeline_get_render_offset_x(route_id)
        return label.get("x", 0) - offset_x

    def timeline_should_render_lane_label(route_id, label, visible_nodes=None):
        route_id = timeline_normalize_route_id(route_id)
        if timeline_debug_reveal_spoilers():
            return True

        label_x = label.get("x", 0)
        label_w = label.get("w", 300)
        label_end = label_x + label_w

        relevant_nodes = visible_nodes if visible_nodes is not None else timeline_get_visible_nodes(route_id)
        for node in relevant_nodes:
            node_x = node.get("x", 0)
            node_end = node_x + node.get("w", 200)
            if node_end >= label_x and node_x <= label_end:
                return True
        return False

    def timeline_get_safe_node_code(node):
        if timeline_node_is_marker(node):
            return node.get("code", "")
        if timeline_should_reveal_node(node):
            return node.get("code", "")
        return "???"

    def timeline_get_locked_thumbnail_displayable():
        if TIMELINE_LOCKED_THUMBNAIL and renpy.loadable(TIMELINE_LOCKED_THUMBNAIL):
            return TIMELINE_LOCKED_THUMBNAIL
        return Solid("#15110fee")

    def timeline_get_thumbnail_displayable(node):
        if timeline_node_is_marker(node):
            return Solid("#6d0f2cee")

        if not timeline_should_reveal_node(node):
            return timeline_get_locked_thumbnail_displayable()

        thumbnail = node.get("thumbnail")
        if thumbnail and renpy.loadable(thumbnail):
            return thumbnail
        return TIMELINE_FALLBACK_THUMBNAIL

    def timeline_toggle_bookmark(chapter_id):
        if not chapter_id:
            return False
        normalize_timeline_persistent_state()
        if chapter_id in persistent.timeline_bookmarks:
            persistent.timeline_bookmarks.remove(chapter_id)
            return False
        persistent.timeline_bookmarks.append(chapter_id)
        return True

    def timeline_is_bookmarked(chapter_id):
        if not chapter_id:
            return False
        normalize_timeline_persistent_state()
        return chapter_id in persistent.timeline_bookmarks

    def timeline_get_route_label(route_id):
        if route_id == TIMELINE_DEFAULT_ROUTE_ID:
            return "Story Timeline"
        for route in TIMELINE_ROUTES:
            if route["id"] == route_id:
                return route["label"]
        if "ROUTES" in globals() and route_id in ROUTES:
            return ROUTES[route_id]["title"]
        return route_id.title()

    def timeline_get_node_meta(node_or_chapter_id):
        chapter_id = node_or_chapter_id
        if isinstance(node_or_chapter_id, dict):
            chapter_id = node_or_chapter_id.get("chapter_id")
        if not chapter_id:
            return {}
        return TIMELINE_NODE_META.get(chapter_id, {})

    def timeline_get_node_display_title(node):
        if timeline_node_is_marker(node):
            return node.get("title", "")

        meta = timeline_get_node_meta(node)
        unlocked_title = meta.get("display_title") or node.get("title") or node.get("chapter_id")
        safe_title_fn = globals().get("chapter_safe_display_title", None)
        if callable(safe_title_fn):
            return safe_title_fn(node.get("chapter_id"), unlocked_title=unlocked_title, locked_title=TIMELINE_LOCKED_TITLE)
        if timeline_should_reveal_node(node):
            return unlocked_title
        return TIMELINE_LOCKED_TITLE

    def timeline_get_node_summary(node):
        if timeline_node_is_marker(node):
            return node.get("summary", "")

        meta = timeline_get_node_meta(node)
        if timeline_should_reveal_node(node):
            return meta.get("summary") or node.get("summary", "")
        chapter = timeline_get_chapter_data(node.get("chapter_id"))
        if chapter:
            return chapter.get("locked_summary") or TIMELINE_LOCKED_SUMMARY
        return TIMELINE_LOCKED_SUMMARY

    def timeline_get_node_stat_modifiers(node):
        if timeline_node_is_marker(node) or not timeline_should_reveal_node(node):
            return []
        meta = timeline_get_node_meta(node)
        return meta.get("stat_modifiers", [])

    def timeline_get_detail_title(node):
        return timeline_get_node_display_title(node)

    def timeline_get_story_relation():
        try:
            return story_state.get("minh_yuuka_relation", "unknown")
        except Exception:
            return "unknown"

    def timeline_story_relation_matches(allowed_relations):
        if not allowed_relations:
            return True
        return timeline_get_story_relation() in allowed_relations

    def timeline_get_requirement_lines(node):
        if timeline_node_is_marker(node):
            return []

        chapter_id = node.get("chapter_id")
        chapter = timeline_get_chapter_data(chapter_id)
        meta = timeline_get_node_meta(node)
        lines = []

        if not timeline_should_reveal_node(node):
            if timeline_is_excluded(chapter_id):
                return [(False, "Nhánh này hiện không khả dụng trong lượt chơi này.")]
            return [(False, TIMELINE_LOCKED_REQUIREMENT)]

        if chapter:
            prerequisites = chapter.get("prerequisites", [])
            prerequisites_any = chapter.get("prerequisites_any", [])

            if prerequisites:
                for prerequisite_id in prerequisites:
                    label = chapter_safe_display_title(prerequisite_id) if prerequisite_id in CHAPTERS else prerequisite_id
                    lines.append((timeline_is_completed(prerequisite_id), "Complete %s" % label))
            elif prerequisites_any:
                labels = []
                for prerequisite_id in prerequisites_any:
                    labels.append(chapter_safe_display_title(prerequisite_id) if prerequisite_id in CHAPTERS else prerequisite_id)
                lines.append((any(timeline_is_completed(req_id) for req_id in prerequisites_any), "Complete any: %s" % " / ".join(labels)))
            else:
                lines.append((True, "No chapter prerequisite."))

            required_directions = chapter.get("required_directions", {})
            for required_route_id, directions in required_directions.items():
                ok = any(has_relationship_direction(required_route_id, direction) for direction in directions)
                lines.append((ok, "%s route direction: %s" % (timeline_get_route_label(required_route_id), " / ".join(directions))))

            required_relations = chapter.get("required_story_relation", [])
            if required_relations:
                lines.append((timeline_story_relation_matches(required_relations), "Minh-Yuuka relation: %s" % " / ".join(required_relations)))

            blocked_relations = chapter.get("blocked_story_relation", [])
            if blocked_relations:
                lines.append((timeline_get_story_relation() not in blocked_relations, "Not blocked by relation: %s" % " / ".join(blocked_relations)))

            required_flags_all = chapter.get("required_flags_all", [])
            for flag in required_flags_all:
                lines.append((has_player_flag(flag), "Flag: %s" % flag))

            required_flags_any = chapter.get("required_flags_any", [])
            if required_flags_any:
                lines.append((any(has_player_flag(flag) for flag in required_flags_any), "Any flag: %s" % " / ".join(required_flags_any)))
        else:
            lines.append((False, "Planned chapter: runtime metadata is not implemented yet."))

        for condition in meta.get("conditions", []):
            lines.append((False, condition))

        if node.get("type") in ["bonus", "branch"]:
            lines.append((timeline_get_node_state(node) != "locked", "Branch is unlocked by prior choices/state."))

        if timeline_is_excluded(chapter_id):
            lines.append((False, "This chapter was excluded by a previous choice."))

        return lines[:6]

    def timeline_get_preview_text(node):
        if timeline_node_is_marker(node):
            return node.get("summary", "") or node.get("title", "")

        state = timeline_get_node_state(node)
        if not timeline_should_reveal_node(node):
            if timeline_is_excluded(node.get("chapter_id")):
                return "Nhánh này hiện không khả dụng trong lượt chơi này."
            return "Chương này vẫn bị khóa. Tiếp tục câu chuyện để hé lộ tên và nội dung."
        if state == "completed":
            return "%s is already complete." % timeline_get_detail_title(node)
        if state == "current":
            return "%s is ready to play." % timeline_get_detail_title(node)
        if timeline_has_runtime_chapter(node["chapter_id"]):
            return "%s is still locked." % timeline_get_detail_title(node)
        return "%s is planned but not implemented yet." % timeline_get_detail_title(node)

    def timeline_get_canvas_size(route_id=None, visible_nodes=None, node_render_positions=None, render_offset_x=None):
        route_id = timeline_normalize_route_id(route_id)
        max_x = 0
        max_y = 0
        relevant_nodes = visible_nodes if visible_nodes is not None else timeline_get_visible_nodes(route_id)
        positions = node_render_positions or {}
        for node in relevant_nodes:
            node_id = node.get("id")
            render_x = positions.get(node_id)
            if render_x is None:
                render_x = timeline_get_node_render_x(route_id, node, render_offset_x=render_offset_x)
            node_extra_w = 44 if not timeline_node_is_marker(node) else 0
            node_extra_h = 44 if not timeline_node_is_marker(node) else 0
            max_x = max(max_x, render_x + node.get("w", 200) + node_extra_w + 120)
            max_y = max(max_y, node.get("y", 0) + node.get("h", 200) + node_extra_h + 110)
        return (max(1792, max_x), max(950, max_y))

    def timeline_get_viewport_xinitial(route_id=None, selected_node_id=None, viewport_width=1744, node=None, canvas_size=None, node_render_positions=None, render_offset_x=None):
        route_id = timeline_normalize_route_id(route_id)
        canvas_w, _canvas_h = canvas_size if canvas_size is not None else timeline_get_canvas_size(route_id)
        scrollable_w = max(1, canvas_w - viewport_width)
        node = node if node is not None else timeline_resolve_selected_node(route_id, selected_node_id)
        if not node:
            return 0.0
        positions = node_render_positions or {}
        render_x = positions.get(node.get("id"))
        if render_x is None:
            render_x = timeline_get_node_render_x(route_id, node, render_offset_x=render_offset_x)
        target_x = max(0, render_x - int(viewport_width / 2) + int(node.get("w", 200) / 2))
        return max(0.0, min(1.0, float(target_x) / float(scrollable_w)))
