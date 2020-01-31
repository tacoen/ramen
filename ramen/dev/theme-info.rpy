init offset =-10

screen theme_info():

    python:
        va = [
            ['text', gui.text_color],
            ['idle', gui.idle_color],
            ['selected', gui.selected_color],
            ['insensitive', gui.insensitive_color],
            ['muted', gui.muted_color ],
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

    frame xpos 10 ypos 30 background gui.interface_bgr_color xsize 200 ysize 600:
        vbox yalign 0.25:
            for v in vi:
                text v[0] color v[1] min_width 180 text_align 1.0 size gui.interface_text_size font gui.interface_text_font


    frame xpos 210 ypos 30 background gui.game_menu_background xsize 400 ysize 600 padding (18,8,8,18):

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
                bar value Preference("text speed") xmaximum 360

    frame xpos 630 ypos 30 background "#0000":

        $ n = 40

        label "text"

        for v in va:
            vbox xpos 0 ypos n:

                hbox yalign 0.5 ysize 30:
                    text v[0] size 12 color "#000" min_width 80  yalign 0.5
                    frame background v[1] xsize 80 ysize 30:
                        text v[1] color ramu.color_Invert(v[1]) size 16
            $ n += 32


    frame xpos 630+200 ypos 30 background "#0000":

        $ n = 40

        label "interface"

        for v in vi:
            vbox xpos 0 ypos n:

                hbox yalign 0.5 ysize 30:
                    text v[0] size 12 color "#000" min_width 80  yalign 0.5
                    frame background v[1] xsize 80 ysize 30:
                        text v[1] color ramu.color_Invert(v[1]) size 16
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
        $ test_items = ['Test','Eval']
        for i in test_items:
            textbutton i action Null
