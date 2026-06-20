# The script of the game goes in this file.

define e = Character("Eileen")

label start:
    $ initialize_progression()
    jump route_map


label after_load:
    $ initialize_progression()
    $ refresh_validation_state()
    return
