init -99:

    python:
        try: FONT_PATH
        except NameError: FONT_PATH = ramu.fn_getdir()

        gui_font = ramu.fn_getdir()+'/Abel-Regular.ttf'
        game_font = ramu.fn_getdir()+'/WorkSans-Regular.ttf'
        game_label_font = ramu.fn_getdir()+'/WorkSans-SemiBold.ttf'
        game_title_font = ramu.fn_getdir()+'/WorkSans-Light.ttf'

    style abel_font:
        font ramu.fn_getdir()+'/Abel-Regular.ttf'
        antialias True

    style ramen_gui:
        font ramu.fn_getdir()+'/WorkSans-Light.ttf'
        antialias True
        size 22

    style ramen_text:
        font ramu.fn_getdir()+'/WorkSans-Regular.ttf'
        antialias True
        size 22


    style ramen_title:
        font ramu.fn_getdir()+'/WorkSans-ExtraLight.ttf'
        antialias True
        size 48

    style ramen_label:
        font ramu.fn_getdir()+'/WorkSans-SemiBold.ttf'
        antialias True
        size 22


