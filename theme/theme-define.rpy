################################################################################
## Initialization
################################################################################


# must before gui.rpy

init -10 python:

    try: THEME_PATH
    except NameError: THEME_PATH = ramu.fn_getdir()

    try: FONT_PATH
    except NameError: THEME_PATH = ramu.fn_getdir()+"/fonts"

    try: TITLES_PATH
    except NameError: TITLES_PATH = ramu.fn_getdir()+"/titles"



