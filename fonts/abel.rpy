init -99:

    python:
        try: FONT_PATH
        except NameError: FONT_PATH = ramu.fn_getdir()

            
    style abel_font:
        font FONT_PATH+'/Abel-Regular.ttf'
        antialias True

