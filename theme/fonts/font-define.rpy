init -21 python:
    
    try: FONT_PATH
    except NameError: FONT_PATH = ramu.fn_getdir()
    
    font = object()

    font.game_text = FONT_PATH+'/WorkSans-Regular.ttf'
    font.game_label = FONT_PATH+'/WorkSans-SemiBold.ttf'

    font.ui_title=FONT_PATH+'/WorkSans-ExtraLight.ttf'
    font.ui_label=FONT_PATH+'/WorkSans-Light.ttf'
    font.ui_text = FONT_PATH+'/Abel-Regular.ttf'

    gui.main_menu_background = Color('#123')
    gui.game_menu_background = Color('#234')
    gui.game_menu_overlay = gui.game_menu_background.opacity(0.5)
    gui.game_menu_frame = gui.game_menu_overlay
    gui.game_menu_width = 300
    
    if renpy.loadable(THEME_PATH + "/main_menu.png"):
        gui.main_menu_background = THEME_PATH + "/main_menu.png"

    if renpy.loadable(THEME_PATH + "/game_menu.png"):
        gui.game_menu_background = THEME_PATH + "/game_menu.png"

    if renpy.loadable(THEME_PATH + "/ingame-overlay.png"):
        gui.game_menu_overlay = THEME_PATH + "/ingame-overlay.png"

    if renpy.loadable(THEME_PATH + "/menu_frame.png"):
        gui.game_menu_frame = THEME_PATH + "/menu_frame.png"

    if ramu.sfx(THEME_PATH, "audio/open-theme", False):
        config.main_menu_music = ramu.sfx(THEME_PATH, "audio/open-theme", False)

init offset = -20

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

