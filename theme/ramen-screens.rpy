﻿##########################################################################
# Initialization
##########################################################################

init offset = -9

##########################################################################
# Styles
##########################################################################


style bar:
    ysize gui.bar_size
    left_bar gui.insensitive_color.opacity(0.5)
    right_bar gui.selected_color

style vbar:
    xsize gui.bar_size
    top_bar gui.bar_base_color.opacity(0.6)
    bottom_bar gui.bar_thumb_color

style scrollbar:
    ysize gui.scrollbar_size
    base_bar gui.bar_base_color.opacity(0.6)
    thumb gui.bar_thumb_color

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar gui.bar_base_color.opacity(0.6)
    thumb gui.bar_thumb_color

style slider:
    ysize gui.slider_size
    base_bar gui.bar_base_color.opacity(0.6)
    thumb gui.bar_thumb_color

style vslider:
    xsize gui.slider_size
    base_bar gui.bar_base_color.opacity(0.6)
    thumb gui.bar_thumb_color

style frame:
    padding gui.frame_borders.padding
    background "#0000"

##########################################################################
# In-game screens
##########################################################################


## Say screen ############################################################
##
# The say screen is used to display dialogue to the player. It takes two
# parameters, who and what, which are the name of the speaking character and
# the text to be displayed, respectively. (The who parameter can be None if no
# name is given.)
##
# This screen must create a text displayable with id "what", as Ren'Py uses
# this to manage text display. It can also create displayables with id "who"
# and id "window" to apply style properties.
##
# https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):

    window:
    
        id "window"

        style_prefix "say"

        if renpy.get_screen("smp_ui") or rbc.onphone:
            padding (200,0,0,0)
            xalign 0.0

        if not str(who).endswith("~"):
        
            if not renpy.get_screen('choice'):
                background gui.textbox_background

        if who is None or str(who).endswith("~"):
            text what id "what" xalign 0.5
        else:


            window:
                id "namebox"
                style "namebox"
                text who id "who"
            text what id "what"

 
    # If there's a side image, display it above the text. Do not display on the
    # phone variant - there's no room.
    if not renpy.variant("small"):
    
        if not "{noside}" in what:
            if who == "thou":
                add SideImage() xalign 1.0 yalign 1.0
            else:
                add SideImage() xalign 0.0 yalign 1.0
            

# Make the namebox available for styling through the Character object.

init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default

style namebox is default
style namebox_label is say_label

style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5
    outlines[(absolute(3), gui.textbox_background, absolute(0), absolute(0))]

style say_dialogue:
    properties gui.text_properties("dialogue")
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

style say_thought is say_dialogue:
    xsize gui.dialogue_width-100
    outlines[(absolute(2), gui.textbox_background, absolute(0), absolute(0))]    
    
## Input screen ##########################################################
##
# This screen is used to display renpy.input. The prompt parameter is used to
# pass a text prompt in.
##
# This screen must create an input displayable with id "input" to accept the
# various input parameters.
##
# https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen #########################################################
##
# This screen is used to display the in-game choices presented by the menu
# statement. The one parameter, items, is a list of objects, each with caption
# and action fields.
##
# https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    if renpy.get_screen("smp_ui") or rbc.onphone:

        vbox xalign 0.65:
            for i in items:
                textbutton i.caption action i.action

    else:
    
        vbox:
            for i in items:
                textbutton i.caption action i.action


# When this is true, menu captions will be spoken by the narrator. When false,
# menu captions will be displayed as empty buttons.
define config.narrator_menu = True

style choice_vbox is vbox
style choice_button is button

style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    yalign 0.85
    yanchor 1.0

    spacing gui.choice_spacing

image choice_ = Frame(
    Composite(
        (100, 60),
        (0, 0), Solid(gui.choice_background),
        (0, 0), ramu.theme_image(THEME_PATH, "gui/outline-embose")
    ), Borders(3, 1, 1, 1), tile=False, xalign=0.5)

image choice_hover_ = Frame(
    Composite(
        (100, 60),
        (0, 0), Solid(gui.hover_color),
        (0, 0), ramu.theme_image(THEME_PATH, "gui/outline-embose")
    ), Borders(2, 1, 2, 1), tile=False, xalign=0.5)

style choice_button is default:
    properties gui.button_properties("choice_button")
    background "choice_[prefix_]"

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Quick Menu screen #####################################################
##
# The quick menu is displayed in-game to provide easy access to the out-of-game
# menus.

screen quick_menu():

    # Ensure this appears on top of other screens.
    zorder 100

    if not renpy.get_screen("_console") and not rbc.hud_disable and quick_menu:

        mousearea:
            area(0, config.screen_height - 32, 1.0, 32)
            hovered Show('real_quick_menu', transition=dissolve)
            unhovered Hide('real_quick_menu', transition=dissolve)

screen real_quick_menu():

    zorder 100

    frame ysize 32 xalign 1.0 yalign 1.0 xsize config.screen_width:

        background Color(gui.interface_background).opacity(.5)

        hbox:
            style_prefix "quick"
            xalign 1.0
            yalign 1.0
            yanchor 1.0

            textbutton ico('arrow-left') action Rollback() tooltip _("Back")
            textbutton ico('stack') action ShowMenu('history') tooltip _("History")
            textbutton ico('chevrons-right') action Skip() alternate Skip(fast=True, confirm=True) tooltip _("Skip")
            textbutton ico('lightbulb') action Preference("auto-forward", "toggle") tooltip _("Auto")
            textbutton ico('save') action ShowMenu('save') tooltip _("Save")
            textbutton ico('log-down') action QuickSave() tooltip _("Q.Save")
            textbutton ico('log-up') action QuickLoad() tooltip _("Q.Load")
            textbutton ico('settings') action ShowMenu('preferences') tooltip _("Prefs")

    $ tooltip = GetTooltip()

    if tooltip:
        text "[tooltip]" size 14 color "#0009" xpos 10 ypos 694

# This code ensures that the quick_menu screen is displayed in-game, whenever
# the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is gui_text
style quick_label_text is gui_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")

##########################################################################
# Main and Game Menu Screens
##########################################################################

## Navigation screen #####################################################
##
# This screen is included in the main and game menus, and provides navigation
# to other menus, and to start the game.

transform cfl:
    on show:
        alpha 0
        pause 0.25
        linear 0.25 alpha 1

screen navigation():

    frame xpos 0 ypos 0:
        ysize config.screen_height 
        xsize gui.navigation_xsize 
        background gui.navigation_background
        at cfl

        vbox:
            style_prefix "navigation"
            xpos gui.navigation_xpos
            spacing gui.navigation_spacing
            yalign 0.5

            if main_menu:
                textbutton _("Start") action Start()

                if RAMEN_EPISODES_MENU and renpy.has_screen('ramen_episode_menu'):
                    textbutton _("Episodes") action ShowMenu('ramen_episode_menu')
                    
            else:
                textbutton _("History") action ShowMenu("history")
                textbutton _("Save") action ShowMenu("save")

            textbutton _("Load") action ShowMenu("load")
            textbutton _("Preferences") action ShowMenu("preferences")

            if _in_replay:
                textbutton _("End Replay") action EndReplay(confirm=True)
            elif not main_menu:
                textbutton _("Main Menu") action MainMenu()


            if RAMEN_DEV and renpy.has_screen('ramen_ai_menu'):
                textbutton _("Asset") action Show('ramen_ai_menu')

            if renpy.variant("pc") or (renpy.variant(
                    "web") and not renpy.variant("mobile")):

                # Help isn't necessary or relevant to mobile devices.
                textbutton _("Help") action ShowMenu("help")

            textbutton _("About") action ShowMenu("about")

            if renpy.variant("pc"):

                # The quit button is banned on iOS and unnecessary on Android and
                # Web.
                textbutton _("Quit") action Quit(confirm=not main_menu)


## Main Menu screen ######################################################
##
# Used to display the main menu when Ren'Py starts.
##
# https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    # This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    add gui.main_menu_background

    # This empty frame darkens the main menu.

#    frame:
#       ysize config.screen_height
#       style "main_menu_frame"

    # The use statement includes another screen inside this one. The actual
    # contents of the main menu are in the navigation screen.
    
    use navigation

    if gui.show_name:

        vbox:
            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

# style main_menu_frame:
    # xsize gui.game_menu_width
    # yfill True

style main_menu_vbox:
    xalign 0.9
    yalign 0.9
    xmaximum((float(9) / 10) * config.screen_width) - 100

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)
    color "#000"

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ######################################################
##
# This lays out the basic common structure of a game menu screen. It's called
# with the screen title, and displays the background, title, and navigation.
##
# The scroll parameter can be None, or one of "viewport" or "vpgrid". When
# this screen is intended to be used with one or more children, which are
# transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
    
        python:
            page = title.lower()
                       
            if page == 'load':
                page_bgr = ramu.theme_image(THEME_PATH, "load_menu")
            else:
                page_bgr = gui.game_menu_background
            
        if page_bgr:
            add page_bgr
        else:
            add gui.game_menu_background
        

    frame:
        style "game_menu_outer_frame"

        hbox:

            # Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120
    background gui.game_menu_overlay

style game_menu_navigation_frame:
    xsize 300
    yfill True

style game_menu_content_frame:
    left_margin 20
    right_margin 20
    top_margin 10

style game_menu_viewport:
    xsize config.screen_width-300-60

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label is main_menu_frame
style game_menu_label_text is gui_title_text

style game_menu_label:
    xpos 0
    padding(320, 0, 0, 0)
    ysize 120
    xsize 280

style game_menu_label_text:
    properties gui.text_properties("title")
    yalign 0.5
    size 32

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30


## About screen ##########################################################
##
# This screen gives credit and copyright information about the game and Ren'Py.
##
# There's nothing special about this screen, and hence it also serves as an
# example of how to make a custom screen.

screen about():

    tag menu

    # This use statement includes the game_menu screen inside this one. The
    # vbox child is then included inside the viewport inside the game_menu
    # screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox ymaximum 0:

            python:
                nicename = config.name.title()

            text "[nicename!t]" size 32
            text _("Version [config.version!t]\n")
            null height 16

            # gui.about is usually set in options.rpy.
            if gui.about and not gui.about.strip() == '':
                text "[gui.about!t]\n"

            null height 16

            text "[build.name!t]" color gui.hover_muted_color
            text _("Made with {a=https://www.renpy.org/}{font="+font.ui_text+"}Ren'Py{/font}{/a} [renpy.version_only].")
            null height 8
            text "Ramen -- It's Renpy According Me {a=https://github.com/tacoen/ramen}{font="+font.ui_text+"}Modular Aproach{/font}{/a}."
            text "Work Sans is licensed under the SIL Open Font License. Copyright (c) 2014-2015 Wei Huang"
            text "Feathericons/feather is licensed under the MIT License. Copyright (c) Colebemis"
            null height 16

            text _("[renpy.license!t]")

# This is redefined in options.rpy to add text to the about screen.

style about_vbox:
    ysize 0
    
style about_label is gui_label

style about_label_text is gui_label_text:
    color gui.accent_color

style about_text is gui_text:
    color gui.text_color

style credit_text is gui_text:
    color gui.text_color

style about_text_hyperlink is gui_text

style credit_text_hyperlink is gui_text:
    size 3

style about_text is ramen_gui:
    size 18

style credit_text is ramen_gui:
    size 20

## Load and Save screens #################################################
##
# These screens are responsible for letting the player save the game and load
# it again. Since they share nearly everything in common, both are implemented
# in terms of a third screen, file_slots.
##
# https://www.renpy.org/doc/html/screen_special.html#save https://
# www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu
 
    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            # This ensures the input will get the enter event before any of the
            # buttons do.
            order_reverse True

            # The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            # The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:

                        action FileAction(slot)

                        has vbox
                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            # Buttons to access other pages.

            hbox:

                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                # range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 50
    ypadding 3

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Preferences screen ####################################################
##
# The preferences screen allows the player to configure the game to better suit
# themselves.
##
# https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "radio"
                    label _("Rollback Side")
                    textbutton _("Disable") action Preference("rollback side", "disable")
                    textbutton _("Left") action Preference("rollback side", "left")
                    textbutton _("Right") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                # Additional vboxes of type "radio_pref" or "check_pref" can be
                # added here, to add additional creator-defined preferences.

            null height(4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)

                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"

style smaller_label_text is gui_label_text:
    size 20

style pref_label is gui_text
style pref_label_text is smaller_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 225

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "radio_[prefix_]"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "check_[prefix_]"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 350

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize (style['game_menu_viewport'].xminimum / 2) - (4 * gui.pref_spacing)
    #xsize 450


## History screen ########################################################
##
# This is a screen that displays the dialogue history to the player. While
# there isn't anything special about this screen, it does have to access the
# dialogue history stored in _history_list.
##
# https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    # Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                # This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        # Take the color of the who text from the Character, if
                        # set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


# This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = set()


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen ###########################################################
##
# A screen that gives information about key and mouse bindings. It uses other
# screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
# help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 15

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 8

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 250
    right_padding 20

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0


##########################################################################
# Additional screens
##########################################################################
## Confirm screen ########################################################
##
# The confirm screen is called when Ren'Py wants to ask the player a yes or no
# question.
##
# https://www.renpy.org/doc/html/screen_special.html#confirm


screen confirm(message, yes_action, no_action):

    # Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200
    layer "interface"
    style_prefix "confirm"

    add gui.game_menu_overlay

    frame:
        padding(64, 64, 64, 32)

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    # Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background gui.confirm_frame_background
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    properties gui.text_properties("confirm_prompt")
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")
    background gui.interface_hover_color.shade(0.5)
    padding(32, 16, 32, 16)

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")

## Skip indicator screen #################################################
##
# The skip_indicator screen is displayed to indicate that skipping is in
# progress.
##
# https://www.renpy.org/doc/html/screen_special.html#skip-indicator


# Will use hud Color

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 1
            text "+" style "skip_triangle"
            text _("Skipping")
            null width 6
            text "^" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "^" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "^" at delayed_blink(0.4, 1.0) style "skip_triangle"


# This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause(cycle - .4)
        repeat

style skip_triangle is icoram:
    line_leading 5
    size 14
    kerning - 10
#    outlines [ (absolute(1), gui.textbox_background, absolute(0), absolute(0)) ]
    color hud_fgcolor
#    color "#000"

style skip_frame is empty:
    ypos gui.skip_ypos
    xpos gui.skip_xpos
    xsize 180
    padding gui.skip_frame_borders.padding

style skip_text is ramen_gui:
    size gui.notify_text_size
    outlines[(absolute(1), gui.textbox_background, absolute(0), absolute(0))]
 #   color hud_fgcolor

## Notify screen #########################################################
##
# The notify screen is used to show the player a message. (For example, when
# the game is quicksaved or a screenshot has been taken.)
##
# https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 102
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')

transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0

style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos
    xpos gui.notify_xpos
    background gui.notify_frame_background
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ############################################################
##
# This screen is used for NVL-mode dialogue and menus.
##
# https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        # Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        # Displays the menu, if given. The menu may be displayed incorrectly if
        # config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


# This controls the maximum number of NVL-mode entries that can be displayed at
# once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")


##########################################################################
# Mobile Variants
##########################################################################

style pref_vbox:
    variant "medium"
    xsize 450

# Since a mouse may not be present, we replace the quick menu with a version
# that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 340

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 400

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 600

# console

style _console is _default:
    background "#111E"

style _console_text is ramen_gui:
    size 16
    color "#ccc"

style _console_command_text is _console_text:
    color "#fff"

style _console_input is _console_text:
    background "#0061"

style _console_input_text is _console_text:
    color "#ddd"

style _console_error_text is _console_text:
    color "#E66"