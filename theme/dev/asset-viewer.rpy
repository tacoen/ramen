style rai is default

style rai_nav is button:
    background "#333"
    hover_background "#666"
    size 16
style rai_nav_text is abel_font:
    size 16

style rai_tab is button:
    background "#666"
    hover_background "#999"
    selected_background "#ccc"
    size 16

style rai_tab_text is abel_font:
    color "#aaa"
    hover_color "#fff"
    selected_color "#333"
    size 16

style rai_text is abel_font:
    size 16

screen ramen_ai_menu():

    python:
        try:
            obj_id
        except BaseException:
            obj_id = None

        try:
            tab
        except BaseException:
            tab = None

    modal True
    style_prefix "rai"
    layer 'interface'
    add Solid('#123')

    key "K_ESCAPE" action Hide('ramen_ai_menu')

    vbox xpos 0 ypos 0:

        use rai_ctlheader(obj_id)

        if tab is not None:
            hbox:
                use rai_menu(tab)
                frame xsize 1 background "#999"

                if obj_id is not None:

                    frame background "#0001" padding(8, 8):

                        viewport:
                            draggable True
                            mousewheel True
                            scrollbars "vertical"

                            use rai_content(tab, obj_id)


screen rai_content(tab, obj_id):

    vbox:
        text tab
        text obj_id


screen rai_menu(tab):

    python:
        if tab in RD.keys():
            menus = RD[tab]
        if tab == 'ramen':
            menus = ['ico', 'gui', 'vars']

    frame background "#0001" padding(8, 8):

        viewport xsize 184:
            draggable True
            mousewheel True
            scrollbars "vertical"
            vbox xsize 168:
                for m in menus:
                    textbutton m style 'rai_nav' xsize 184 action SetScreenVariable('obj_id', m)
                    null height 4


screen rai_ctlheader(title=None):

    python:
        if title is None:
            title = "Ramen Asset Inspector"
        else:
            title = "Ramen Asset Inspector: " + title

        rdtabs = RD.keys()
        rdtabs.append('ramen')

    frame xpos 0 ypos 0 background "#0001" xsize config.screen_width:
        style_prefix "rai"
        padding(8, 8, 8, 0)

        vbox:
            hbox xfill True:
                text title bold True color "#fff"
                hbox xalign 1.0:
                    textbutton "close" action Hide('ramen_ai_menu') text_color "#ccc" text_hover_color "#fff" text_size 12

            hbox:
                null width 200
                for t in rdtabs:
                    textbutton t style 'rai_tab' action SetScreenVariable('tab', t)
                    null width 8

            frame ysize 1 background "#999"
