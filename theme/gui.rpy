################################################################################
## Initialization
################################################################################

## The init offset statement causes the initialization statements in this file
## to run before init statements in any other file.

init -10 python:
    try: THEME_PATH
    except NameError: THEME_PATH = ramu.fn_getdir()


init offset = -1


## Calling gui.init resets the styles to sensible default values, and sets the
## width and height of the game.

init python:
    gui.init(1280, 720)

## ui

define gui.text_font = FONT_PATH+'/WorkSans-Regular.ttf'
define gui.text_size = 20
define gui.text_color = '#dddddd'
define gui.idle_color = "#eeeeee"
define gui.accent_color = "#C11"
define gui.hover_color = "#fc1"
define gui.selected_color = "#ACF"
define gui.insensitive_color = ramu.color_Darken(gui.idle_color)
define gui.hover_muted_color = ramu.color_Darken(gui.hover_color)
define gui.muted_color = ramu.color_Darken(gui.insensitive_color)

define gui.hyperlink_text_color = "#ACF"

define gui.bar_thumb_color = gui.selected_color
define gui.bar_base_color = ramu.color_Darken(gui.bar_thumb_color,50)

## Out-game / Interface

define gui.interface_bgr_color = "#d9d9d9"
define gui.interface_idle_color = "#666"
define gui.interface_hover_color = "#47A"
define gui.interface_selected_color = ramu.color_Darken(gui.interface_idle_color,40)
define gui.interface_insensitive_color =  ramu.color_Brighten(gui.interface_idle_color,16)
define gui.interface_muted_color = ramu.color_Brighten(gui.interface_idle_color,8)
define gui.interface_transparent = "CC"
define gui.interface_text_color = gui.interface_idle_color
define gui.interface_text_font = FONT_PATH+'/WorkSans-Light.ttf'
define gui.interface_text_size = 24

define gui.confirm_frame_background = Frame(
        Composite(
            (200,80),
            (0,0), Solid(gui.interface_bgr_color),
            (0,0), THEME_PATH + "/gui/outline-b.png"
        ), Borders(1,1,1,1), tile=False, xalign=0.5)

define gui.confirm_button_text_xalign = 0.5
define gui.confirm_button_text_size = 24

define gui.name_text_font = FONT_PATH+'/WorkSans-SemiBold.ttf'
define gui.name_text_size = 20
define gui.name_text_color = '#fff'

define gui.quick_button_text_font = FONT_ICO_RAMEN
define gui.quick_button_borders = Borders(16, 0, 16, 4)
define gui.quick_button_text_size = 16
define gui.quick_button_text_idle_color = gui.interface_idle_color
define gui.quick_button_text_selected_color = gui.interface_selected_color
define gui.quick_button_text_hover_color = gui.interface_hover_color

define gui.navigation_button_text_font = FONT_PATH+'/WorkSans-Light.ttf'
define gui.navigation_button_width = 250
define gui.navigation_button_text_size = 24
define gui.navigation_button_text_align = 1.0
define gui.navigation_button_text_hover_color = gui.interface_hover_color
define gui.navigation_button_text_color = gui.interface_idle_color
define gui.navigation_button_text_idle_color = gui.interface_idle_color
define gui.navigation_button_text_selected_color = gui.interface_selected_color
define gui.navigation_button_text_selected_font = FONT_PATH+'/WorkSans-Regular.ttf'


define gui.label_text_size = 24
define gui.label_text_color = gui.idle_color

define gui.notify_text_size = 16
define gui.title_text_size = 50

## The images used for the main and game menus.

if renpy.loadable(THEME_PATH+"/gui/main_menu.png"):
    define gui.main_menu_background = THEME_PATH+"/gui/main_menu.png"
else:
    define gui.main_menu_background = Solid(ramu.color_Darken(gui.interface_bgr_color,90)+gui.interface_transparent)

if renpy.loadable(THEME_PATH+"/gui/game_menu.png"):
    define gui.game_menu_background = THEME_PATH+"/gui/game_menu.png"
else:
    define gui.game_menu_background = Solid(ramu.color_Darken(gui.interface_bgr_color,90)+gui.interface_transparent)

if renpy.loadable(THEME_PATH+"/gui/ingame-overlay.png"):
    define gui.game_menu_overlay = THEME_PATH+"/gui/ingame-overlay.png"
else:
    define gui.game_menu_overlay = gui.game_menu_background

image radio_selected_ = Text(ico("check-square"),font=FONT_ICO_RAMEN,color=gui.idle_color,size=18,line_leading=8)
image radio_ = Text(ico("square"),font=FONT_ICO_RAMEN,color=gui.idle_color,size=18,line_leading=8)
image check_selected_ = Text(ico("toggle-right"),font=FONT_ICO_RAMEN,color=gui.idle_color,size=18,line_leading=10)
image check_ = Text(ico("toggle-left"),font=FONT_ICO_RAMEN,color=gui.muted_color,size=18,line_leading=10)


## Dialogue ####################################################################
##
## These variables control how dialogue is displayed on the screen one line at a
## time.

## The height of the textbox containing dialogue.

define gui.textbox_height = config.screen_height/5 + 24
define gui.textbox_yalign = 1.0
define gui.textbox_background = "#000000"

## The placement of the speaking character's name, relative to the textbox.
## These can be a whole number of pixels from the left or top, or 0.5 to center.

define gui.name_xpos = config.screen_width /5
define gui.name_ypos = -20

define gui.name_xalign = 0.0
define gui.namebox_width = None
define gui.namebox_height = None
define gui.namebox_borders = Borders(0, 5, 5, 5)
define gui.namebox_tile = False

define gui.dialogue_xpos = gui.name_xpos + 16
define gui.dialogue_ypos = 14

## The maximum width of dialogue text, in pixels.
define gui.dialogue_width = config.screen_width - (2*gui.name_xpos)

$ print "w"
$ print config.screen_width 
$ print gui.dialogue_width

## The horizontal alignment of the dialogue text. This can be 0.0 for left-
## aligned, 0.5 for centered, and 1.0 for right-aligned.
define gui.dialogue_text_xalign = 0.0

define gui.naration_overlay = "#0003"

## Buttons #####################################################################
##
## These variables, along with the image files in gui/button, control aspects of
## how buttons are displayed.

## The width and height of a button, in pixels. If None, Ren'Py computes a size.
define gui.button_width = None
define gui.button_height = None

## The borders on each side of the button, in left, top, right, bottom order.
define gui.button_borders = Borders(4, 4, 4, 4)

## If True, the background image will be tiled. If False, the background image
## will be linearly scaled.
define gui.button_tile = False

define gui.button_text_font = gui.interface_text_font
define gui.button_text_size = gui.interface_text_size
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color
define gui.button_text_xalign = 0.0


## These variables override settings for different kinds of buttons. Please see
## the gui documentation for the kinds of buttons available, and what each is
## used for.
##
## These customizations are used by the default interface:

define gui.radio_button_borders = Borders(22, 4, 4, 4)
define gui.check_button_borders = Borders(22, 4, 4, 4)
define gui.page_button_borders = Borders(22, 4, 10, 4)


## You can also add your own customizations, by adding properly-named variables.
## For example, you can uncomment the following line to set the width of a
## navigation button.

## Choice Buttons ##############################################################
##
## Choice buttons are used in the in-game menus.

define gui.choice_bgr_color = gui.interface_bgr_color
define gui.choice_button_width = 5 * config.screen_width / 12
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(5, 10, 5, 10)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size-2
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = gui.interface_idle_color
define gui.choice_button_text_hover_color = ramu.color_Invert(gui.text_color)
define gui.choice_button_text_insensitive_color = gui.interface_insensitive_color
define gui.choice_spacing = 1


## File Slot Buttons ###########################################################
##
## A file slot button is a special kind of button. It contains a thumbnail
## image, and text describing the contents of the save slot. A save slot uses
## image files in gui/button, like the other kinds of buttons.

## The save slot button.

define gui.slot_button_width = 276
define gui.slot_button_height = 206
define gui.slot_button_borders = Borders(10, 10, 10, 10)
define gui.slot_button_text_size = 14
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

## The width and height of thumbnails used by the save slots.
define config.thumbnail_width = 256
define config.thumbnail_height = 144

## The number of columns and rows in the grid of save slots.
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2


## Positioning and Spacing #####################################################
##
## These variables control the positioning and spacing of various user interface
## elements.

## The position of the left side of the navigation buttons, relative to the left
## side of the screen.
define gui.navigation_xpos = 40

## The vertical position of the skip indicator.
define gui.skip_ypos = config.screen_height-30-(config.screen_height/5)
define gui.skip_xpos = config.screen_width-180-(config.screen_width/8)
## The vertical position of the notify screen.
define gui.notify_ypos = 45

## The spacing between menu choices.
define gui.choice_spacing = 22

## Buttons in the navigation section of the main and game menus.
define gui.navigation_spacing = 4

## Controls the amount of spacing between preferences.
define gui.pref_spacing = 10

## Controls the amount of spacing between preference buttons.
define gui.pref_button_spacing = 0

## The spacing between file page buttons.
define gui.page_spacing = 0

## The spacing between file slots.
define gui.slot_spacing = 10

## The position of the main menu text.
define gui.main_menu_text_xalign = 1.0


## Frames ######################################################################
##
## These variables control the look of frames that can contain user interface
## components when an overlay or window is not present.

## Generic frames.
define gui.frame_borders = Borders(4, 4, 4, 4)

## The frame that is used as part of the confirm screen.
define gui.confirm_frame_borders = Borders(40, 40, 40, 40)

## The frame that is used as part of the skip screen.
define gui.skip_frame_borders = Borders(16, 5, 50, 5)

## The frame that is used as part of the notify screen.
define gui.notify_frame_borders = Borders(16, 5, 40, 5)

## Should frame backgrounds be tiled?
define gui.frame_tile = False

## Bars, Scrollbars, and Sliders ###############################################
##
## These control the look and size of bars, scrollbars, and sliders.
##
## The default GUI only uses sliders and vertical scrollbars. All of the other
## bars are only used in creator-written screens.

## The height of horizontal bars, scrollbars, and sliders. The width of vertical
## bars, scrollbars, and sliders.
define gui.bar_size = 25
define gui.scrollbar_size = 12
define gui.slider_size = 25

## True if bar images should be tiled. False if they should be linearly scaled.
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

## Horizontal borders.
define gui.bar_borders = Borders(4, 4, 4, 4)
define gui.scrollbar_borders = Borders(4, 4, 4, 4)
define gui.slider_borders = Borders(4, 4, 4, 4)

## Vertical borders.
define gui.vbar_borders = Borders(4, 4, 4, 4)
define gui.vscrollbar_borders = Borders(4, 4, 4, 4)
define gui.vslider_borders = Borders(4, 4, 4, 4)

## What to do with unscrollable scrollbars in the gui. "hide" hides them, while
## None shows them.
define gui.unscrollable = "hide"


## History #####################################################################
##
## The history screen displays dialogue that the player has already dismissed.

## The number of blocks of dialogue history Ren'Py will keep.
define config.history_length = 250

## The height of a history screen entry, or None to make the height variable at
## the cost of performance.
define gui.history_height = 140

## The position, width, and alignment of the label giving the name of the
## speaking character.
define gui.history_name_xpos = 155
define gui.history_name_ypos = 0
define gui.history_name_width = 155
define gui.history_name_xalign = 1.0

## The position, width, and alignment of the dialogue text.
define gui.history_text_xpos = 170
define gui.history_text_ypos = 2
define gui.history_text_width = 740
define gui.history_text_xalign = 0.0


## NVL-Mode ####################################################################
##
## The NVL-mode screen displays the dialogue spoken by NVL-mode characters.

## The borders of the background of the NVL-mode background window.
define gui.nvl_borders = Borders(0, 10, 0, 20)

## The maximum number of NVL-mode entries Ren'Py will display. When more entries
## than this are to be show, the oldest entry will be removed.
define gui.nvl_list_length = 6

## The height of an NVL-mode entry. Set this to None to have the entries
## dynamically adjust height.
define gui.nvl_height = 115

## The spacing between NVL-mode entries when gui.nvl_height is None, and between
## NVL-mode entries and an NVL-mode menu.
define gui.nvl_spacing = 10

## The position, width, and alignment of the label giving the name of the
## speaking character.
define gui.nvl_name_xpos = 430
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 150
define gui.nvl_name_xalign = 1.0

## The position, width, and alignment of the dialogue text.
define gui.nvl_text_xpos = 450
define gui.nvl_text_ypos = 8
define gui.nvl_text_width = 590
define gui.nvl_text_xalign = 0.0

## The position, width, and alignment of nvl_thought text (the text said by the
## nvl_narrator character.)
define gui.nvl_thought_xpos = 240
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 780
define gui.nvl_thought_xalign = 0.0

## The position of nvl menu_buttons.
define gui.nvl_button_xpos = 450
define gui.nvl_button_xalign = 0.0

## Localization ################################################################

## This controls where a line break is permitted. The default is suitable
## for most languages. A list of available values can be found at https://
## www.renpy.org/doc/html/style_properties.html#style-property-language

define gui.language = "unicode"


################################################################################
## Mobile devices
################################################################################

init python:

    ## This increases the size of the quick buttons to make them easier to touch
    ## on tablets and phones.
    if renpy.variant("touch"):

        gui.quick_button_borders = Borders(40, 14, 40, 0)

    ## This changes the size and spacing of various GUI elements to ensure they
    ## are easily visible on phones.
    if renpy.variant("small"):

        ## Font sizes.
        gui.text_size = 30
        gui.name_text_size = 36
        gui.notify_text_size = 25
        gui.interface_text_size = 30
        gui.button_text_size = 30
        gui.label_text_size = 34

        ## Adjust the location of the textbox.
        gui.textbox_height = 240
        gui.name_xpos = 80
        gui.text_xpos = 90
        gui.text_width = 1100

        ## Change the size and spacing of various things.
        gui.slider_size = 36

        gui.choice_button_width = 1240

        gui.navigation_spacing = 20
        gui.pref_button_spacing = 10

        gui.history_height = 190
        gui.history_text_width = 690

        gui.quick_button_text_size = 20

        ## File button layout.
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2

        ## NVL-mode.
        gui.nvl_height = 170

        gui.nvl_name_width = 305
        gui.nvl_name_xpos = 325

        gui.nvl_text_width = 915
        gui.nvl_text_xpos = 345
        gui.nvl_text_ypos = 5

        gui.nvl_thought_width = 1240
        gui.nvl_thought_xpos = 20

        gui.nvl_button_width = 1240
        gui.nvl_button_xpos = 20
