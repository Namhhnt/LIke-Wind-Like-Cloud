screen library_placeholder_page(category_id):

    $ category = library_get_category(category_id)
    $ category_title = _(category["title"]) if category else _("Library")
    $ category_subtitle = _(category["subtitle"]) if category else _("Explore special contents of Like Wind, Like Cloud")

    use library_menu_shell(
        page_title=category_title,
        page_subtitle=category_subtitle,
        back_action=ShowMenu("library")
    ):

        vbox:
            spacing 26

            text category_title:
                style "library_placeholder_title"

            text _("This section is now connected to the Library and ready for real content."):
                style "library_placeholder_body"

            text _("For now, this placeholder keeps the menu flow complete while profiles, galleries, music, and bonus materials are still being authored."):
                style "library_placeholder_body"

            frame:
                xsize 1160
                ysize 250
                background ui_frame_or_solid("gui/library/panel.png", "#120f0ccc", 24)

                vbox:
                    xpos 28
                    ypos 24
                    spacing 14

                    text _("Current status"):
                        style "library_placeholder_title"
                        size 30

                    text _("Unlocked progress: [library_get_progress_text(category_id)]"):
                        style "library_placeholder_body"

                    text _("Use this page as the future entry point for category-specific content and filters."):
                        style "library_placeholder_body"


screen library_characters():
    tag menu
    use library_placeholder_page("characters")


screen library_stories():
    tag menu
    use library_placeholder_page("stories")


screen library_cg():
    tag menu
    use library_placeholder_page("cg")


screen library_music():
    tag menu
    use library_placeholder_page("music")


screen library_minigames():
    tag menu
    use library_placeholder_page("minigames")


screen library_extras():
    tag menu
    use library_placeholder_page("extras")
