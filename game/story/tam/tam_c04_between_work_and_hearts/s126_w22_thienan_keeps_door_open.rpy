# FILE: game/story/tam/tam_c04_between_work_and_hearts/s126_w22_thienan_keeps_door_open.rpy

label tam_c04_w22_s03_thienan_keeps_door_open:
    if story_has_flag("tam_c04_tam_quang_confirmed"):
        return
    if not story_has_flag("tam_c04_quang_thienan_committed") and not tam_c04_quang_thienan_breakthrough_ready():
        return
    scene bg_tam_family_entry_evening
    with dissolve
    "Quang đưa Thiên An về sau một buổi làm muộn."
    thienan neutral "Anh không cần lên."
    quang "Ừ."
    scene cg_tam_c04_thienan_open_door
    with dissolve
    "Anh quay đi. Thiên An giữ cửa chưa khép."
    scene bg_tam_family_entry_evening
    with dissolve
    thienan neutral "Trà vẫn còn. Nếu anh muốn uống."
    quang "Anh muốn."
    $ story_add("thienan_quang_trust", 5)
    $ tam_c04_add_extended_score("quang_thienan_resolve", 5)
    $ tam_c04_commit_quang_thienan()
    $ story_flag("tam_c04_w22_thienan_keeps_door_open")
    return
