# FILE: game/story/tam/tam_c04_between_work_and_hearts/s110_w19_quang_thienan_no_longer_refuses.rpy

label tam_c04_w19_s03_quang_thienan_no_longer_refuses:
    if story_has_flag("tam_c04_tam_quang_confirmed"):
        return
    $ _active = tam_c04_quang_thienan_breakthrough_ready()
    if not _active:
        return
    scene bg_tam_family_living_room_evening
    with dissolve
    scene cg_tam_c04_quang_thienan_work
    with dissolve
    "Thiên An về muộn. Quang đang ngồi ở bậc thềm, bên cạnh là một hộp thức ăn còn ấm."
    scene bg_tam_family_living_room_evening
    with dissolve
    thienan tired "Anh có thể để trong bếp."
    quang "Anh muốn chờ em ăn."
    thienan neutral "Tôi không cần người canh."
    quang "Anh biết."
    "Thiên An mở cửa rồi đứng sang một bên."
    thienan neutral "Vào đi."
    $ story_add("thienan_quang_trust", 7)
    $ tam_c04_add_extended_score("quang_thienan_resolve", 7)
    $ story_flag("tam_c04_w19_thienan_invites_quang_in")
    return
