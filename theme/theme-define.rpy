##########################################################################
# Initialization
##########################################################################

init -199 python:

    # For Shared Resources

    RAMEN_THEME_PATH = ramu.fn_getdir()
    DEFAULT_SFXPATH = RAMEN_THEME_PATH

init -99 python:

    # defaults

    rbc.hud_disable = False
    rbc.hud_show = False
    rbc.hud_set = 5
    rbc.hud_element = {}

    rbc.val = 0

    try:
        hud_fgcolor = hud.ui.fgcolor[rbc.hud_set]
    except BaseException:
        hud_fgcolor = "#fff"

    gui.init(1280, 720)

init -190 python:

    # must before gui.rpy

    try:
        FONT_PATH
    except NameError:
        FONT_PATH = RAMEN_THEME_PATH + "/fonts"

    try:
        THEME_PATH
    except NameError:
        THEME_PATH = RAMEN_THEME_PATH + "/titles"


define config.window_show_transition = {"screens": Dissolve(.25)}
define config.window_hide_transition = {"screens": Dissolve(.25)}
