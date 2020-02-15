init -10 python:

    def ramen_icotable():
        renpy.call_screen('ico_table')

    def gui_propCollect(t=None):

        res={}
        gk=sorted(gui.__dict__.keys())

        if t is None:
            topic=['text','idle','selected','insensitive','muted','accent','hover']
        else:
            if not isinstance(t,list):
                topic=[str(t)]
            else:
                topic=t

        for t in topic:
            print t
            try: res[t]=gui.__dict__[t+"_properties"]()
            except:
                for k in gk:
                    if k.startswith(t+"_"):
                        try: res[t]
                        except: res[t]={}
                        res[t][k]=gui.__dict__[k]
        return res

    def start_guicollect():
        known_gui=['accent', 'bar', 'button', 'check', 'choice', 'confirm', 'dialogue', 'file', 'frame', 'game', 'history', 'hover', 'hyperlink', 'idle', 'insensitive', 'interface', 'label', 'language', 'main', 'muted', 'name', 'namebox', 'naration', 'navigation', 'notify', 'nvl', 'page', 'pref', 'quick', 'radio', 'scrollbar', 'selected', 'skip', 'slider', 'slot', 'text', 'textbox', 'title', 'unscrollable', 'vbar', 'vscrollbar', 'vslider']
        first=['text','idle','selected','insensitive','muted','accent','hover']
        second=[]
        for k in known_gui:
            if not k in first: second.append(k)

        known_gui=first + second

        return gui_propCollect(known_gui)


    gview='text'

init offset=-10

style devtheme is default
style devtheme_text is abel_font:
    color "#ccc"
style devtheme_textbutton is button
style devtheme_textbutton_text_font is abel_font

screen ico_table():

    $ Ico=ico(None)
    
    frame background "#fff" ypos 75 xpos 0 ysize config.screen_height-168:
        vpgrid  xsize config.screen_width:
            scrollbars "vertical"
            cols 4
            spacing 16
            draggable True
            mousewheel True
            
            for i in sorted(Ico.keys()):
                hbox yalign 0.5:
                    text Ico[i] style "ram_ico" color "#000"
                    null width 8
                    text i style "abel_font" color "#000" text_align 0.0 min_width 160
                    null width 32
            
screen gui_explorer():

    modal True
    layer "interface"

    python:
        try: gres
        except: gres=start_guicollect()

    frame xpos 0 ypos 0 background "#fff" xsize 280:
        padding (0,0,0,30)

        viewport:
            draggable True
            mousewheel True
            scrollbars "vertical"
            vbox:
                style_prefix 'devtheme'
                spacing 10
                for k in gres:
                    textbutton k text_color "#000" text_hover_color "#c00" action SetVariable('gview',k)


    if not gview is "":

        $ mywidth=config.screen_width-290
        $ cw=mywidth/12

        frame xpos 290 ypos 0 xsize mywidth background "#111":

            $ prop=gres[gview]

            viewport:
                draggable True
                mousewheel True
                scrollbars "vertical"

                vbox:
                    style_prefix 'devtheme'
                    spacing 10
                    for k in prop.keys():
                        hbox:
                            vbox xminimum 4*cw xmaximum  5*cw:
                                text k color "#fff" size 18 bold True
                                text repr( type(prop[k])) color "#ddd" size 16
                            vbox xsize 8*cw:
                                if k.endswith('color'):
                                    frame xsize 4*cw ysize 32 background prop[k]:
                                        python:
                                            try: cc=prop[k].hexcode
                                            except: cc=str(prop[k])
                                        text cc color "#000"
                                else:
                                    if "imagelike" in repr(type(prop[k])):
                                        vbox:
                                            for w in prop[k].__dict__:
                                                hbox:
                                                    text w +":" color "#fc3" min_width 3*cw
                                                    text repr(prop[k].__dict__[w]) +":" color "#ccc"  min_width 5*cw
                                    else:
                                        text repr(prop[k])  color "#ddd"



screen gui_info():

    python:
        va=[
            ['text', gui.text_color],
            ['idle', gui.idle_color],
            ['selected', gui.selected_color],
            ['insensitive', gui.insensitive_color],
            ['muted', gui.muted_color ],
            ['accent', gui.accent_color],
            ['hover', gui.hover_color],
            ['hover_muted', gui.hover_muted_color],
        ]

        vi=[
            ['idle', gui.interface_idle_color],
            ['selected', gui.interface_selected_color],
            ['insensitive', gui.interface_insensitive_color],
            ['muted', gui.interface_muted_color],
            ['hover', gui.interface_hover_color],
        ]

    frame xpos 10 ypos 30 background gui.interface_background.shade(.5) xsize 200 ysize 600:
        vbox yalign 0.25:
            for v in vi:
                text v[0] color v[1] min_width 180 text_align 1.0 size gui.interface_text_size font gui.interface_text_font


    frame xpos 210 ypos 0 background gui.game_menu_background xsize 480 ysize 600 padding (18,8,8,38):

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

        $ n=40

        label "text"

        for v in va:
            vbox xpos 0 ypos n:

                hbox yalign 0.5 ysize 30:
                    text v[0] size 12 color "#ccc" min_width 120  yalign 0.5
                    frame background v[1] xsize 80 ysize 30:
                        text repr(v[1].hexcode) color v[1].replace_lightness(1) size 16
            $ n += 32


    frame xpos 630+200 ypos 30 background "#0000":

        $ n=40

        label "interface"

        for v in vi:
            vbox xpos 0 ypos n:

                hbox yalign 0.5 ysize 30:
                    text v[0] size 12 color "#ccc" min_width 80  yalign 0.5
                    frame background v[1] xsize 80 ysize 30:
                        text repr(v[1].hexcode) color v[1].replace_lightness(1) size 16
            $ n += 32

    frame padding (24,24,24,24) xpos 240 ypos 480 xsize 300:
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
        $ test_items=['Test','Eval']
        for i in test_items:
            textbutton i action Null
