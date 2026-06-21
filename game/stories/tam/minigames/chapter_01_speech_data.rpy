# Tâm Route - Chapter 01 Speech Mini-game Data
# ============================================================

default tam_speech_attempts = 0
default tam_speech_order = []

init python:

    tam_speech_required_order = [
        "context",
        "coordination",
        "risk",
        "commitment",
    ]

    tam_speech_short_labels = {
        "self_only": "Tự giới thiệu",
        "context": "Hiểu bối cảnh công ty",
        "coordination": "Phối hợp liên phòng ban",
        "solo": "Làm việc độc lập",
        "risk": "Tư duy rủi ro",
        "commitment": "Thái độ làm việc",
        "salary_first": "Quan tâm mức lương",
    }

    tam_speech_items = [
        {
            "id": "self_only",
            "label": "Tự giới thiệu: tập trung kể về điểm mạnh cá nhân, thành tích học tập, khả năng quan sát và học hỏi.",
        },
        {
            "id": "context",
            "label": "Triển khai dự án là điểm nối giữa xây dựng, vật liệu, IT, pháp lý, kế toán và quản lý chất lượng.",
        },
        {
            "id": "coordination",
            "label": "Nhấn mạnh năng lực phối hợp: theo dõi tiến độ, tổng hợp thông tin, làm rõ đầu việc và giữ luồng trao đổi giữa các phòng ban.",
        },
        {
            "id": "solo",
            "label": "Khả năng làm việc độc lập: em có thể tự xử lý mọi việc mà không cần làm phiền phòng ban khác.",
        },
        {
            "id": "risk",
            "label": "Nói về tư duy rủi ro: phát hiện vướng mắc sớm, báo cáo minh bạch, không để lỗi nhỏ thành vấn đề lớn.",
        },
        {
            "id": "commitment",
            "label": "Thái độ làm việc: học nhanh, chịu khó đi hiện trường khi cần, tôn trọng quy trình và chịu trách nhiệm với phần việc của mình.",
        },
        {
            "id": "salary_first",
            "label": "Nói rằng mức lương là điều em quan tâm nhất vì em muốn được đánh giá đúng giá trị.",
        },
    ]


screen tam_speech_choice_screen(items, picked):
    modal True

    frame:
        xalign 0.5
        yalign 0.5
        xmaximum 1100
        ymaximum 900
        padding (36, 30)

        vbox:
            spacing 18

            text "Chọn ý tiếp theo cho câu trả lời của Tâm" size 34

            if picked:
                text "Đã chọn: [', '.join(tam_speech_short_labels[item_id] for item_id in picked)]" size 24
            else:
                text "Đã chọn: chưa có" size 24

            text "Các ý còn lại:" size 26

            vbox:
                spacing 12

                for item in items:
                    textbutton item["label"]:
                        action Return(item["id"])
                        xfill True

            text "Mỗi lượt chọn sẽ khóa lại ý vừa chọn." size 20
