## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("Like Wind Like Cloud")


## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = True


## The version of the game.

define config.version = "4.9.0"


## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
""")


## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "LikeWindLikeCloud"


## Development and release safety ##############################################

## "auto" keeps developer tools available while running the project from the
## Ren'Py SDK, but disables them automatically in packaged distributions.

define config.developer = "auto"

## Never enable the Shift+O console independently in release builds.

define config.console = False


## Sounds and music ############################################################

## These three variables control, among other things, which mixers are shown
## to the player by default. Setting one of these to False will hide the
## appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

define config.main_menu_music = "audio/bgm.mp3"


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Between screens of the game menu.

define config.intra_transition = dissolve


## A transition that is used after a game has been loaded.

define config.after_load_transition = None


## Used when entering the main menu after the game has ended.

define config.end_game_transition = None


## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window.

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 0


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15

## ## Limit framerate for PC performance ## ## 
## Graphics stability and performance defaults.
default preferences.gl_powersave = False
default preferences.gl_framerate = 60
default preferences.gl_tearing = False

## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA%\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "LikeWindLikeCloud-1781924544"


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.
##
## Release goals:
## - Do not distribute .rpy/.rpym source files.
## - Distribute compiled .rpyc/.rpymc scripts.
## - Package runtime files into several .rpa archives.
## - Keep startup presplash assets outside archives.
## - Exclude editor files, source artwork, caches, saves, and temporary files.

init python:

    ## Archive declarations.
    ##
    ## Splitting archives keeps the distribution tidy and avoids rebuilding one
    ## single giant archive whenever only scripts or a specific asset group
    ## changes.

    build.archive("scripts", "all")
    build.archive("gui", "all")
    build.archive("images", "all")
    build.archive("audio", "all")
    build.archive("video", "all")
    build.archive("data", "all")


    ## Exclude temporary, hidden, editor, cache, save, and source-art files.
    ##
    ## build.classify uses the FIRST matching rule, so exclusions and special
    ## files must appear before the broader archive rules below.

    build.classify("**~", None)
    build.classify("**.bak", None)
    build.classify("**.tmp", None)
    build.classify("**.temp", None)
    build.classify("**.orig", None)
    build.classify("**.rej", None)
    build.classify("**.swp", None)
    build.classify("**/#**", None)
    build.classify("**/.**", None)
    build.classify("**/thumbs.db", None)
    build.classify("**/desktop.ini", None)
    build.classify("**.zip", None)

    build.classify("**.md", None)
    build.classify("Specs/**", None)
    build.classify("tools/**", None)
    build.classify("game/cache/**", None)
    build.classify("game/saves/**", None)
    build.classify("game/images/reserved/**", None)
    build.classify("game/images/characters/**_expression_**.png", None)    

    build.classify("**.psd", None)
    build.classify("**.psb", None)
    build.classify("**.kra", None)
    build.classify("**.xcf", None)
    build.classify("**.clip", None)
    build.classify("**.ase", None)
    build.classify("**.aseprite", None)
    build.classify("**.blend", None)


    ## Keep presplash files outside .rpa archives.
    ##
    ## These files can be needed before Ren'Py has fully initialized and loaded
    ## the game archives.

    build.classify("game/presplash.png", "all")
    build.classify("game/presplash.jpg", "all")
    build.classify("game/presplash_background.png", "all")
    build.classify("game/presplash_background.jpg", "all")
    build.classify("game/presplash_foreground.png", "all")
    build.classify("game/presplash_foreground.jpg", "all")

    build.classify("game/android-presplash.jpg", "all")
    build.classify("game/android-downloading.jpg", "all")


    ## Scripts.
    ##
    ## Source Ren'Py scripts are excluded. Their compiled counterparts are
    ## included in scripts.rpa.

    build.classify("game/screens/ui_review_**", None)
    build.classify("game/tl/**/ui_review.*", None)
    build.classify("game/tests/**", None)
    build.classify("tests/**", None)
    build.classify("game/**.rpy", None)
    build.classify("game/**.rpym", None)

    build.classify("game/**.rpyc", "scripts")
    build.classify("game/**.rpymc", "scripts")
    build.classify("game/**.pyc", "scripts")

    ## Keep required custom Python modules. They are hidden inside scripts.rpa,
    ## but remain Python source and can still be reverse-engineered/extracted.
    ## Do not place secrets or private keys in client-side Python files.

    build.classify("game/**.py", "scripts")


    ## GUI assets and fonts.

    build.classify("game/gui/**", "gui")
    build.classify("game/**.ttf", "gui")
    build.classify("game/**.otf", "gui")
    build.classify("game/**.woff", "gui")
    build.classify("game/**.woff2", "gui")


    ## Image assets.
    ##
    ## The directory rule covers uncommon image formats stored under images/.
    ## Extension rules also catch images stored elsewhere in game/.

    build.classify("game/images/**", "images")
    build.classify("game/**.png", "images")
    build.classify("game/**.jpg", "images")
    build.classify("game/**.jpeg", "images")
    build.classify("game/**.webp", "images")
    build.classify("game/**.avif", "images")
    build.classify("game/**.svg", "images")
    build.classify("game/**.gif", "images")


    ## Audio assets.

    build.classify("game/audio/**", "audio")
    build.classify("game/**.ogg", "audio")
    build.classify("game/**.opus", "audio")
    build.classify("game/**.mp3", "audio")
    build.classify("game/**.wav", "audio")
    build.classify("game/**.flac", "audio")
    build.classify("game/**.m4a", "audio")


    ## Video assets.

    build.classify("game/video/**", "video")
    build.classify("game/videos/**", "video")
    build.classify("game/**.webm", "video")
    build.classify("game/**.mp4", "video")
    build.classify("game/**.mkv", "video")
    build.classify("game/**.ogv", "video")


    ## Any remaining runtime file under game/ goes into data.rpa.
    ##
    ## This includes JSON, CSV, YAML, shaders, and other custom runtime data
    ## that does not match a more specific rule above.

    build.classify("game/**", "data")


    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation("*.html")
    build.documentation("*.txt")


## A Google Play license key is required to perform in-app purchases. It can be
## found in the Google Play developer console, under "Monetize" > "Monetization
## Setup" > "Licensing".

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "renpytom/test-project"
