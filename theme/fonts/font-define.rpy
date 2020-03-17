init -21 python:
    
    try: FONT_PATH
    except NameError: FONT_PATH = ramu.fn_getdir()
    
    font = object()

    font.game_text = FONT_PATH+'/WorkSans-Regular.ttf'
    font.game_label = FONT_PATH+'/WorkSans-SemiBold.ttf'

    font.ui_title=FONT_PATH+'/WorkSans-ExtraLight.ttf'
    font.ui_label=FONT_PATH+'/WorkSans-Light.ttf'
    font.ui_text = FONT_PATH+'/Abel-Regular.ttf'

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

