##########################################################################
# Initialization
##########################################################################

init -209 python:

    RAMEN_GUI_PATHS = [
        'titles',
        'theme/titles',
        'theme/gui',
    ]

    RAMEN_SFX_PATHS = [
        'audio',
        'titles',
        'titles/audio',
        'theme/audio',
    ]
    
init -199 python:

    # Constant For Shared Resources
    RAMEN_THEME_PATH = ramu.fn_getdir()

    font = object()
    font.game_text = RAMEN_THEME_PATH+'/fonts/WorkSans-Regular.ttf'
    font.game_label = RAMEN_THEME_PATH+'/fonts/WorkSans-SemiBold.ttf'
    font.ui_title=RAMEN_THEME_PATH+'/fonts/WorkSans-ExtraLight.ttf'
    font.ui_label=RAMEN_THEME_PATH+'/fonts/WorkSans-Light.ttf'
    font.ui_text = RAMEN_THEME_PATH+'/fonts/Abel-Regular.ttf'
    font.ui_ico = RAMEN_THEME_PATH+'/fonts/icon/fonts/ramen-ico.ttf'
        
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

init offset = -9

style ramen_gui:
    font font.ui_text
    antialias True

style ramen_gui_label:
    font font.ui_label
    antialias True
    size 22

style ramen_gui_title:
    font font.ui_title
    antialias True
    size 48

style ramen_text:
    font font.game_text
    antialias True
    size 22

style ramen_label:
    font font.game_label
    antialias True
    size 22

style ramen_icon:
    font font.ui_ico
    antialias True
    size 32

style ramen_icon_text is ramen_icon


define config.window_show_transition = {"screens": Dissolve(.25)}
define config.window_hide_transition = {"screens": Dissolve(.25)}
