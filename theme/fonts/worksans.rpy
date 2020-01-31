init -3:

    python:
        try: FONT_PATH
        except NameError: FONT_PATH = ramu.fn_getdir()

    style ramen_text:
        font FONT_PATH+'/WorkSans-Regular.ttf'
        antialias True
        size 22

    style ramen_gui:
        font FONT_PATH+'/WorkSans-Light.ttf'
        antialias True
        size 22

    style ramen_title:
        font FONT_PATH+'/WorkSans-ExtraLight.ttf'
        antialias True
        size 48

    style ramen_label:
        font FONT_PATH+'/WorkSans-SemiBold.ttf'
        antialias True
        size 22


