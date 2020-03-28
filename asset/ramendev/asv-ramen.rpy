screen rai_ramen_ico():

    python:
        Ico = ico(None)
        c = math.floor((config.screen_width - 200) / (200 + 20))
        sp = math.floor((config.screen_width - 200) - (c * 200)) / c / 2

    vpgrid:
        scrollbars "vertical"
        cols c
        spacing sp
        draggable True
        mousewheel True

        for i in sorted(Ico.keys()):
            hbox xsize 200:
                text Ico[i] style "ramen_icon" color "#fff"
                null width 8
                text i style "ramen_gui" color "#fff" text_align 0.0 min_width 180
                null width 32

screen rai_ramen_vars():

    python:
        try:
            gres
        except BaseException:
            gres = start_guicollect()

        try:
            gview
        except BaseException:
            gview = ''

    viewport ysize config.screen_height - 70:
        draggable True
        mousewheel True
        scrollbars "vertical"

        vbox:
            style_prefix 'rai_nav'
            spacing 10
            for k in gres:
                textbutton k action SetVariable('gview', k)

    if not gview == "":

        $ mywidth = config.screen_width - 200
        $ cw = mywidth / 12

        frame xpos 208 xsize mywidth background "#111":

            $ prop = gres[gview]

            viewport:
                draggable True
                mousewheel True
                scrollbars "vertical"

                vbox:
                    style_prefix 'devtheme'
                    spacing 10
                    for k in prop.keys():
                        hbox:
                            vbox xminimum 4 * cw xmaximum  5 * cw:
                                text k color "#fff" size 18 bold True
                                text repr(type(prop[k])) color "#ddd" size 16
                            vbox xsize 8 * cw:
                                if k.endswith('color'):
                                    frame xsize 4 * cw ysize 32 background prop[k]:
                                        python:
                                            try:
                                                cc = prop[k].hexcode
                                            except BaseException:
                                                cc = str(prop[k])
                                        text cc color "#000"
                                else:
                                    if "imagelike" in repr(type(prop[k])):
                                        vbox:
                                            for w in prop[k].__dict__:
                                                hbox:
                                                    text w + ":" color "#fc3" min_width 3 * cw
                                                    text repr(prop[k].__dict__[w]) color "#ccc"  min_width 5 * cw
                                    else:
                                        text repr(prop[k])  color "#ddd"


screen rai_ramen_gui():

    python:
        va = [
            ['text', gui.text_color],
            ['idle', gui.idle_color],
            ['selected', gui.selected_color],
            ['insensitive', gui.insensitive_color],
            ['muted', gui.muted_color],
            ['accent', gui.accent_color],
            ['hover', gui.hover_color],
            ['hover_muted', gui.hover_muted_color],
        ]

        vi = [
            ['idle', gui.interface_idle_color],
            ['selected', gui.interface_selected_color],
            ['insensitive', gui.interface_insensitive_color],
            ['muted', gui.interface_muted_color],
            ['hover', gui.interface_hover_color],
        ]

        h = config.screen_height - 70

    frame xpos 0 background gui.interface_background.shade(.5) xsize 200 ysize h:
        vbox yalign 0.25:
            for v in vi:
                text v[0] color v[1] min_width 180 text_align 1.0 size gui.interface_text_size font gui.interface_text_font

    frame xpos 200 background gui.game_menu_background xsize 480 ysize h padding(18, 8, 8, 38):

        vbox:
            text "Accent" size gui.label_text_size color gui.accent_color font gui.interface_text_font
            null height 30
            text "Idle" size gui.label_text_size color gui.idle_color font gui.interface_text_font
            hbox:
                text "I'm a text you " color gui.text_color font gui.interface_text_font size 18
                text "selected, " color gui.selected_color font gui.interface_text_font size 18
                text "hover, " color gui.hover_color font gui.interface_text_font size 18
                text "or " color gui.text_color font gui.interface_text_font size 18
                text "muted," color gui.muted_color font gui.interface_text_font size 18
            hbox:
                text "but sometime " color gui.text_color font gui.interface_text_font size 18
                text "hover muted." color gui.hover_muted_color font gui.interface_text_font size 18
                text "because " color gui.text_color font gui.interface_text_font size 18
                text "idle." color gui.idle_color font gui.interface_text_font size 18

            null height 24

            vbox:
                text "Bars" size 20 color gui.idle_color font gui.interface_text_font
                bar value Preference("text speed") xmaximum 300

    frame xpos 580 ypos 30 background "#0000":

        $ n = 40

        label "text"

        for v in va:
            vbox xpos 0 ypos n:

                hbox yalign 0.5 ysize 30:
                    text v[0] size 12 color "#ccc" min_width 120  yalign 0.5
                    frame background v[1] xsize 80 ysize 30:
                        text repr(v[1].hexcode) color v[1].replace_lightness(1) size 16
            $ n += 32

    frame xpos 630 + 200 ypos 30 background "#0000":

        $ n = 40

        label "interface"

        for v in vi:
            vbox xpos 0 ypos n:

                hbox yalign 0.5 ysize 30:
                    text v[0] size 12 color "#ccc" min_width 80  yalign 0.5
                    frame background v[1] xsize 80 ysize 30:
                        text repr(v[1].hexcode) color v[1].replace_lightness(1) size 16
            $ n += 32

    frame padding(24, 24, 24, 24) xpos 240 ypos 480 xsize 300:
        background gui.confirm_frame_background
        style_prefix "confirm"
        vbox xalign .5 yalign .5 spacing 30:

            label _("Confirm?"):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 20
                textbutton _("Yes") action Null
                textbutton _("No") action Null

    vbox xoffset 200:
        style_prefix "choice"
        $ test_items = ['Test', 'Eval']
        for i in test_items:
            textbutton i action Null

screen rai_ramen_constant():

    python:
        mywidth = config.screen_width - 200
        cw = (mywidth / 2)
        dc=[]
        for d in globals():
            if d.startswith('RAMEN'):
                dc.append(d)

    viewport:
        draggable True
        mousewheel True
        scrollbars "vertical"
    
        vbox xsize mywidth:
            spacing 20
            for d in dc:
                hbox:
                    text d min_width 300 
                    text repr(globals()[d])

screen rai_ramen_component():

    python:
        mywidth = config.screen_width - 200
        cw = (mywidth / 2)
        ff = [ 'title', 'version', 'desc', 'author', 'dir' ]
    
    viewport:
        draggable True
        mousewheel True
        scrollbars "vertical"
    
        vbox xsize mywidth:
            spacing 24
            
            for c in sorted(ram._component.keys()):
                $ comp = ram._component[c]

                vbox:
                    text c.title() size 24 bold True color "#fff"
                    null height 8
                    frame ysize 1 background "#ccc"
                    null height 8
                    
                    for f in ff:
                        python:
                            try: val = str(comp[f])
                            except: val = ""
                        
                        hbox:
                            text f min_width 120 color "#ccc"
                            text val color "#ddd"

                    null height 16
            
        