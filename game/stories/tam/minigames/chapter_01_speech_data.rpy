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


    def tam_speech_toggle_choice(picked, item_id):
        if item_id in picked:
            picked.remove(item_id)
        elif len(picked) < 4:
            picked.append(item_id)

        renpy.restart_interaction()


    def tam_speech_order_is_perfect(order):
        return order == tam_speech_required_order


    def tam_speech_order_has_required(order):
        return all(item_id in order for item_id in tam_speech_required_order)
