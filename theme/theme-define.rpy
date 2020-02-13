################################################################################
## Initialization
################################################################################


init -199 python:
    
    # For Shared Resources

    RAMEN_THEME_PATH = ramu.fn_getdir()
    DEFAULT_SFXPATH = RAMEN_THEME_PATH

init -10 python:

    # must before gui.rpy

    try: FONT_PATH
    except NameError: FONT_PATH = RAMEN_THEME_PATH+"/fonts"

    try: THEME_PATH
    except NameError: THEME_PATH = RAMEN_THEME_PATH+"/titles"
