# Shared Tam route state and character definitions.

default tam_salary_tier = "standard"
default tam_work_skill = 0
default tam_confidence = 0
default huyen_trust = 0
default hoang_impression = 0
default tam_c02_party_route = ""
default tam_c02_hoang_noticed = False
default tam_c02_meaningful_contact = False

define tam = Character("Tâm", image="tam")
define huyen = Character("Huyền", image="huyen")
define hr = Character(_("Recruiter"))
define interviewer = Character(_("Interviewer"))
define manager = Character(_("Manager"))
define coworker = Character(_("Coworker"))
define quan = Character("Quân", image="quan")
define hoang_unknown = Character(_("Mysterious man"), image="hoang")
define hoang = Character("Hoàng", image="hoang")
define narrator = Character(None)

define yuuka = Character("Yuuka", image="yuuka")
define minh = Character("Minh", image="minh")
define thienan = Character("Thiên An", image="thienan")