# Shared Tam route state and character definitions.

default tam_salary_tier = "standard"
default tam_work_skill = 0
default tam_confidence = 0
default huyen_trust = 0
default hoang_impression = 0
default tam_c02_party_route = ""
default tam_c02_hoang_noticed = False
default tam_c02_meaningful_contact = False


# ============================================================
# Dialogue Font / Text Style
# ============================================================
# Put fonts in:
# game/fonts/
#
# Suggested:
# - NotoSerif-Regular.ttf
# - NotoSerif-Italic.ttf
# - NotoSerif-SemiBold.ttf
#
# If the font files are missing, Ren'Py will fallback to default font.

define LWLC_DIALOGUE_FONT = "fonts/NotoSerif-Regular.ttf"
define LWLC_DIALOGUE_ITALIC_FONT = "fonts/NotoSerif-Italic.ttf"
define LWLC_NAME_FONT = "fonts/NotoSerif-Bold.ttf"

define LWLC_DIALOGUE_SIZE = 34
define LWLC_NAME_SIZE = 36

define LWLC_DIALOGUE_COLOR = "#d3c8ba"
define LWLC_DIALOGUE_MUTED_COLOR = "#acacac"
define LWLC_NARRATION_COLOR = "#afafaf"
define LWLC_THOUGHT_COLOR = "#9bd8d8"

define LWLC_DIALOGUE_OUTLINES = [ (1, "#00000099", 0, 1) ]
define LWLC_NAME_OUTLINES = [ (2, "#000000AA", 0, 1) ]


# ============================================================
# Base Dialogue Styles
# ============================================================

style say_label:
    font LWLC_NAME_FONT
    size LWLC_NAME_SIZE
    color "#FFFFFF"
    outlines LWLC_NAME_OUTLINES

style say_dialogue:
    # font LWLC_DIALOGUE_FONT
    size LWLC_DIALOGUE_SIZE
    color LWLC_DIALOGUE_COLOR
    outlines LWLC_DIALOGUE_OUTLINES
    line_spacing 4

style say_thought:
    # font LWLC_DIALOGUE_ITALIC_FONT
    size LWLC_DIALOGUE_SIZE
    color LWLC_THOUGHT_COLOR
    italic True
    outlines LWLC_DIALOGUE_OUTLINES
    line_spacing 4

style say_narration:
    # font LWLC_DIALOGUE_FONT
    size LWLC_DIALOGUE_SIZE
    color LWLC_NARRATION_COLOR
    outlines LWLC_DIALOGUE_OUTLINES
    line_spacing 4


# ============================================================
# Character Name Colors
# ============================================================
# Color direction:
# - Tâm: soft pink / gentle warmth
# - Hoàng: warm gold / approachable charisma
# - Minh: cool blue-gray / restraint, intellect
# - Yuuka: sakura rose / bright artistic warmth
# - Thiên An: elegant violet / composed ambition
# - Huyền: lively orange / playful directness
# - Quân: steel gray / strict professionalism

define COLOR_TAM = "#F3A6B8"
define COLOR_HUYEN = "#F2A65A"
define COLOR_HOANG = "#E6B35C"
define COLOR_MINH = "#7DA7C7"
define COLOR_YUUKA = "#F4A7C8"
define COLOR_THIENAN = "#B79AE8"
define COLOR_QUAN = "#9EA7B3"

define COLOR_AKIKO = "#B8C8D8"
define COLOR_TETSUYA = "#C7A97A"
define COLOR_HIROSHI = "#9DD6B5"
define COLOR_AYUMI = "#C899D6"
define COLOR_LISA = "#D7B36A"
define COLOR_TAKASHI = "#9CB0C9"
define COLOR_DUYEN = "#D9A3B3"
define COLOR_KIM = "#A7C98B"

define COLOR_MINH_FATHER = "#8D99A6"
define COLOR_MINH_MOTHER = "#B9A1D9"
define COLOR_TAM_FATHER = "#BFA06A"
define COLOR_TAM_MOTHER = "#D9A6A0"
define COLOR_YUUKA_FATHER = "#A9B7C8"
define COLOR_YUUKA_MOTHER = "#D8AFC8"

define COLOR_SYSTEM = "#C8C8C8"
define COLOR_UNKNOWN = "#A9A9A9"


# ============================================================
# Main Characters
# ============================================================

define tam = Character(
    "Tâm",
    image="tam",
    who_color=COLOR_TAM,
    who_font=LWLC_NAME_FONT,
    who_size=LWLC_NAME_SIZE,
    who_outlines=LWLC_NAME_OUTLINES,
    what_font=LWLC_DIALOGUE_FONT,
    what_size=LWLC_DIALOGUE_SIZE,
    what_color=LWLC_DIALOGUE_COLOR,
    what_outlines=LWLC_DIALOGUE_OUTLINES
)

define huyen = Character(
    "Huyền",
    image="huyen",
    who_color=COLOR_HUYEN,
    who_font=LWLC_NAME_FONT,
    who_size=LWLC_NAME_SIZE,
    who_outlines=LWLC_NAME_OUTLINES,
    what_font=LWLC_DIALOGUE_FONT,
    what_size=LWLC_DIALOGUE_SIZE,
    what_color=LWLC_DIALOGUE_COLOR,
    what_outlines=LWLC_DIALOGUE_OUTLINES
)

define hoang = Character(
    "Hoàng",
    image="hoang",
    who_color=COLOR_HOANG,
    who_font=LWLC_NAME_FONT,
    who_size=LWLC_NAME_SIZE,
    who_outlines=LWLC_NAME_OUTLINES,
    what_font=LWLC_DIALOGUE_FONT,
    what_size=LWLC_DIALOGUE_SIZE,
    what_color=LWLC_DIALOGUE_COLOR,
    what_outlines=LWLC_DIALOGUE_OUTLINES
)

define hoang_unknown = Character(
    _("Mysterious man"),
    image="hoang",
    who_color=COLOR_UNKNOWN,
    who_font=LWLC_NAME_FONT,
    who_size=LWLC_NAME_SIZE,
    who_outlines=LWLC_NAME_OUTLINES,
    what_font=LWLC_DIALOGUE_FONT,
    what_size=LWLC_DIALOGUE_SIZE,
    what_color=LWLC_DIALOGUE_MUTED_COLOR,
    what_outlines=LWLC_DIALOGUE_OUTLINES
)

define yuuka = Character(
    "Yuuka",
    image="yuuka",
    who_color=COLOR_YUUKA,
    who_font=LWLC_NAME_FONT,
    who_size=LWLC_NAME_SIZE,
    who_outlines=LWLC_NAME_OUTLINES,
    what_font=LWLC_DIALOGUE_FONT,
    what_size=LWLC_DIALOGUE_SIZE,
    what_color=LWLC_DIALOGUE_COLOR,
    what_outlines=LWLC_DIALOGUE_OUTLINES
)

define minh = Character(
    "Minh",
    image="minh",
    who_color=COLOR_MINH,
    who_font=LWLC_NAME_FONT,
    who_size=LWLC_NAME_SIZE,
    who_outlines=LWLC_NAME_OUTLINES,
    what_font=LWLC_DIALOGUE_FONT,
    what_size=LWLC_DIALOGUE_SIZE,
    what_color=LWLC_DIALOGUE_COLOR,
    what_outlines=LWLC_DIALOGUE_OUTLINES
)

define minh_unknown = Character(
    _("Rainy man"),
    image="minh_shadow",
    who_color=COLOR_UNKNOWN,
    who_font=LWLC_NAME_FONT,
    who_size=LWLC_NAME_SIZE,
    who_outlines=LWLC_NAME_OUTLINES,
    what_font=LWLC_DIALOGUE_FONT,
    what_size=LWLC_DIALOGUE_SIZE,
    what_color=LWLC_DIALOGUE_MUTED_COLOR,
    what_outlines=LWLC_DIALOGUE_OUTLINES
)

define thienan = Character(
    "Thiên An",
    image="thienan",
    who_color=COLOR_THIENAN,
    who_font=LWLC_NAME_FONT,
    who_size=LWLC_NAME_SIZE,
    who_outlines=LWLC_NAME_OUTLINES,
    what_font=LWLC_DIALOGUE_FONT,
    what_size=LWLC_DIALOGUE_SIZE,
    what_color=LWLC_DIALOGUE_COLOR,
    what_outlines=LWLC_DIALOGUE_OUTLINES
)

define quan = Character(
    "Quân",
    image="quan",
    who_color=COLOR_QUAN,
    who_font=LWLC_NAME_FONT,
    who_size=LWLC_NAME_SIZE,
    who_outlines=LWLC_NAME_OUTLINES,
    what_font=LWLC_DIALOGUE_FONT,
    what_size=LWLC_DIALOGUE_SIZE,
    what_color=LWLC_DIALOGUE_COLOR,
    what_outlines=LWLC_DIALOGUE_OUTLINES
)


# ============================================================
# Workplace / Generic Characters
# ============================================================

define hr = Character(
    _("Recruiter"),
    who_color="#B8B8B8",
    who_font=LWLC_NAME_FONT,
    who_size=LWLC_NAME_SIZE,
    who_outlines=LWLC_NAME_OUTLINES,
    what_font=LWLC_DIALOGUE_FONT,
    what_size=LWLC_DIALOGUE_SIZE,
    what_color=LWLC_DIALOGUE_COLOR,
    what_outlines=LWLC_DIALOGUE_OUTLINES
)

define interviewer = Character(
    _("Interviewer"),
    who_color="#B8B8B8",
    who_font=LWLC_NAME_FONT,
    who_size=LWLC_NAME_SIZE,
    who_outlines=LWLC_NAME_OUTLINES,
    what_font=LWLC_DIALOGUE_FONT,
    what_size=LWLC_DIALOGUE_SIZE,
    what_color=LWLC_DIALOGUE_COLOR,
    what_outlines=LWLC_DIALOGUE_OUTLINES
)

define manager = Character(
    _("Manager"),
    who_color="#AEB7C2",
    who_font=LWLC_NAME_FONT,
    who_size=LWLC_NAME_SIZE,
    who_outlines=LWLC_NAME_OUTLINES,
    what_font=LWLC_DIALOGUE_FONT,
    what_size=LWLC_DIALOGUE_SIZE,
    what_color=LWLC_DIALOGUE_COLOR,
    what_outlines=LWLC_DIALOGUE_OUTLINES
)

define coworker = Character(
    _("Coworker"),
    who_color="#C0B8AA",
    who_font=LWLC_NAME_FONT,
    who_size=LWLC_NAME_SIZE,
    who_outlines=LWLC_NAME_OUTLINES,
    what_font=LWLC_DIALOGUE_FONT,
    what_size=LWLC_DIALOGUE_SIZE,
    what_color=LWLC_DIALOGUE_COLOR,
    what_outlines=LWLC_DIALOGUE_OUTLINES
)


# ============================================================
# Japan Arc Characters
# ============================================================

define akiko = Character(
    "Akiko",
    image="akiko",
    who_color=COLOR_AKIKO,
    who_font=LWLC_NAME_FONT,
    who_size=LWLC_NAME_SIZE,
    who_outlines=LWLC_NAME_OUTLINES,
    what_font=LWLC_DIALOGUE_FONT,
    what_size=LWLC_DIALOGUE_SIZE,
    what_color=LWLC_DIALOGUE_COLOR,
    what_outlines=LWLC_DIALOGUE_OUTLINES
)

define tetsuya = Character(
    "Tetsuya",
    image="tetsuya",
    who_color=COLOR_TETSUYA,
    who_font=LWLC_NAME_FONT,
    who_size=LWLC_NAME_SIZE,
    who_outlines=LWLC_NAME_OUTLINES,
    what_font=LWLC_DIALOGUE_FONT,
    what_size=LWLC_DIALOGUE_SIZE,
    what_color=LWLC_DIALOGUE_COLOR,
    what_outlines=LWLC_DIALOGUE_OUTLINES
)

define hiroshi = Character(
    "Hiroshi",
    image="hiroshi",
    who_color=COLOR_HIROSHI,
    who_font=LWLC_NAME_FONT,
    who_size=LWLC_NAME_SIZE,
    who_outlines=LWLC_NAME_OUTLINES,
    what_font=LWLC_DIALOGUE_FONT,
    what_size=LWLC_DIALOGUE_SIZE,
    what_color=LWLC_DIALOGUE_COLOR,
    what_outlines=LWLC_DIALOGUE_OUTLINES
)

define ayumi = Character(
    "Ayumi",
    image="ayumi",
    who_color=COLOR_AYUMI,
    who_font=LWLC_NAME_FONT,
    who_size=LWLC_NAME_SIZE,
    who_outlines=LWLC_NAME_OUTLINES,
    what_font=LWLC_DIALOGUE_FONT,
    what_size=LWLC_DIALOGUE_SIZE,
    what_color=LWLC_DIALOGUE_COLOR,
    what_outlines=LWLC_DIALOGUE_OUTLINES
)

define lisa = Character(
    "Lisa",
    image="lisa",
    who_color=COLOR_LISA,
    who_font=LWLC_NAME_FONT,
    who_size=LWLC_NAME_SIZE,
    who_outlines=LWLC_NAME_OUTLINES,
    what_font=LWLC_DIALOGUE_FONT,
    what_size=LWLC_DIALOGUE_SIZE,
    what_color=LWLC_DIALOGUE_COLOR,
    what_outlines=LWLC_DIALOGUE_OUTLINES
)

define takashi = Character(
    "Takashi",
    image="takashi",
    who_color=COLOR_TAKASHI,
    who_font=LWLC_NAME_FONT,
    who_size=LWLC_NAME_SIZE,
    who_outlines=LWLC_NAME_OUTLINES,
    what_font=LWLC_DIALOGUE_FONT,
    what_size=LWLC_DIALOGUE_SIZE,
    what_color=LWLC_DIALOGUE_COLOR,
    what_outlines=LWLC_DIALOGUE_OUTLINES
)


# ============================================================
# Past Arc Characters
# ============================================================

define duyen = Character(
    "Duyên",
    image="duyen",
    who_color=COLOR_DUYEN,
    who_font=LWLC_NAME_FONT,
    who_size=LWLC_NAME_SIZE,
    who_outlines=LWLC_NAME_OUTLINES,
    what_font=LWLC_DIALOGUE_FONT,
    what_size=LWLC_DIALOGUE_SIZE,
    what_color=LWLC_DIALOGUE_COLOR,
    what_outlines=LWLC_DIALOGUE_OUTLINES
)

define kim = Character(
    "Kim",
    image="kim",
    who_color=COLOR_KIM,
    who_font=LWLC_NAME_FONT,
    who_size=LWLC_NAME_SIZE,
    who_outlines=LWLC_NAME_OUTLINES,
    what_font=LWLC_DIALOGUE_FONT,
    what_size=LWLC_DIALOGUE_SIZE,
    what_color=LWLC_DIALOGUE_COLOR,
    what_outlines=LWLC_DIALOGUE_OUTLINES
)


# ============================================================
# Family Characters
# ============================================================

define minh_father = Character(
    "Huỳnh Phi Hùng",
    image="minh_father",
    who_color=COLOR_MINH_FATHER,
    who_font=LWLC_NAME_FONT,
    who_size=LWLC_NAME_SIZE,
    who_outlines=LWLC_NAME_OUTLINES,
    what_font=LWLC_DIALOGUE_FONT,
    what_size=LWLC_DIALOGUE_SIZE,
    what_color=LWLC_DIALOGUE_COLOR,
    what_outlines=LWLC_DIALOGUE_OUTLINES
)

define minh_mother = Character(
    "Bùi Thị Kim Liên",
    image="minh_mother",
    who_color=COLOR_MINH_MOTHER,
    who_font=LWLC_NAME_FONT,
    who_size=LWLC_NAME_SIZE,
    who_outlines=LWLC_NAME_OUTLINES,
    what_font=LWLC_DIALOGUE_FONT,
    what_size=LWLC_DIALOGUE_SIZE,
    what_color=LWLC_DIALOGUE_COLOR,
    what_outlines=LWLC_DIALOGUE_OUTLINES
)

define tam_father = Character(
    "Nguyễn Đức Thành",
    image="tam_father",
    who_color=COLOR_TAM_FATHER,
    who_font=LWLC_NAME_FONT,
    who_size=LWLC_NAME_SIZE,
    who_outlines=LWLC_NAME_OUTLINES,
    what_font=LWLC_DIALOGUE_FONT,
    what_size=LWLC_DIALOGUE_SIZE,
    what_color=LWLC_DIALOGUE_COLOR,
    what_outlines=LWLC_DIALOGUE_OUTLINES
)

define tam_mother = Character(
    "Đặng Thu Hà",
    image="tam_mother",
    who_color=COLOR_TAM_MOTHER,
    who_font=LWLC_NAME_FONT,
    who_size=LWLC_NAME_SIZE,
    who_outlines=LWLC_NAME_OUTLINES,
    what_font=LWLC_DIALOGUE_FONT,
    what_size=LWLC_DIALOGUE_SIZE,
    what_color=LWLC_DIALOGUE_COLOR,
    what_outlines=LWLC_DIALOGUE_OUTLINES
)

define yuuka_father = Character(
    "Nakamura Seiji",
    image="yuuka_father",
    who_color=COLOR_YUUKA_FATHER,
    who_font=LWLC_NAME_FONT,
    who_size=LWLC_NAME_SIZE,
    who_outlines=LWLC_NAME_OUTLINES,
    what_font=LWLC_DIALOGUE_FONT,
    what_size=LWLC_DIALOGUE_SIZE,
    what_color=LWLC_DIALOGUE_COLOR,
    what_outlines=LWLC_DIALOGUE_OUTLINES
)

define yuuka_mother = Character(
    "Nakamura Reiko",
    image="yuuka_mother",
    who_color=COLOR_YUUKA_MOTHER,
    who_font=LWLC_NAME_FONT,
    who_size=LWLC_NAME_SIZE,
    who_outlines=LWLC_NAME_OUTLINES,
    what_font=LWLC_DIALOGUE_FONT,
    what_size=LWLC_DIALOGUE_SIZE,
    what_color=LWLC_DIALOGUE_COLOR,
    what_outlines=LWLC_DIALOGUE_OUTLINES
)


# ============================================================
# Narration / Thought / System
# ============================================================

define narrator = Character(
    None,
    # what_font=LWLC_DIALOGUE_FONT,
    what_size=LWLC_DIALOGUE_SIZE,
    what_color=LWLC_NARRATION_COLOR,
    what_outlines=LWLC_DIALOGUE_OUTLINES
)

define thought = Character(
    None,
    what_prefix="{i}",
    what_suffix="{/i}",
    what_font=LWLC_DIALOGUE_ITALIC_FONT,
    what_size=LWLC_DIALOGUE_SIZE,
    what_color=LWLC_THOUGHT_COLOR,
    what_outlines=LWLC_DIALOGUE_OUTLINES
)
define system = Character(
    None,
    # what_font=LWLC_DIALOGUE_FONT,
    what_size=30,
    what_color=COLOR_SYSTEM,
    what_outlines=LWLC_DIALOGUE_OUTLINES
)