init -99 python:

    HUD_PATH=ramu.fn_getdir()

    def hud_toggle(what,sfx=True):

        try: hud.ui.element[what]
        except: hud.ui.element[what]=True

        if hud.ui.element[what]:
            hud.ui.element[what]=False
            if sfx: ramu.sfx(HUD_PATH,"tone0")
        else:
            hud.ui.element[what]=True
            if sfx: ramu.sfx(HUD_PATH,"tone1")

        rbc.hud_element[what]=hud.ui.element[what]

init -1:

    style hud is default

    style hud_toolbar:
        xpos hud.ui.x
        ypos hud.ui.y
        xsize hud.ui.w
        ysize hud.ui.h

    style hud_icon is icoram:
        xsize 48
        ysize 32

    style hud_icon_text is icoram:
        size 32

    style hud_sunico is icoram:
        xsize 24
        ysize 24

    style hud_sunico_text is icoram:
        size 24

    style hud_text is gui_text:
        size 18

    style hud_score is default

    style hud_score_text is abel_font:
        size 48
        hover_color "#ffd"

    style hud_label is abel_font:
        size 18

    style hud_title is abel_font:
        size 14
        yalign 0.5
        xoffset 2
        bold True

    transform pulse:
        block:
            linear 0.2 alpha 1
            pause 1
            linear 0.2 alpha 0
            pause 3
            repeat

    transform pulse_dying:
        block:
            linear 0.2 alpha 1
            pause 0.3
            linear 0.2 alpha 0.3
            pause 1
            repeat

    transform pulldown:
        on show:
            ypos -config.screen_height
            linear 0.2 ypos 80
            linear 0.3 ypos 72
        on hide:
            pause 0.5
            ypos 72
            linear 0.2 ypos 80
            linear 0.6 ypos -config.screen_height


    screen hc_debug(msg):
    
        text repr(msg) ypos 0.9 xpos 0.1

    screen hc_hbar_pos(obj, topic, val, sty, tcolor="#fff", legend=True, xy=(24,config.screen_height-200)):
    
        vbox pos xy:
            use hc_hbar(obj, topic, val, sty, tcolor, legend)
            
    screen hc_hbar(obj, topic, val, sty, tcolor="#000", legend=True):

        python:
            xmax=sty.xminimum - ( sty.left_padding + sty.right_padding )
            
            barsty=style[obj.id]['hbar'][topic]
            
            if type(barsty.thumb) is Null:
                barsty=style['hbar']
            
            try: max=mc.limit[topic][1]
            except: max=mc.limit['stat'][1]

        vbox:
            
            if legend:
                hbox xminimum xmax:
                    xfill True
                    text topic.title() style 'hud_label' color tcolor size 12 xalign 0
                    text str(val)+"/"+str(max) style 'hud_label' color tcolor size 12 xalign 1.0 text_align 1.0
                null height 3
            bar range max value val style barsty xmaximum xmax

    screen hc_tbar(element,title=''):

        python:
            xmax=style['hud']['area'][element].xminimum-2

        frame background Color(hud.ui.bgcolor[rbc.hud_set]).shade(0.5):
            xsize xmax
            xoffset -7
            yoffset -7
            hbox:
                xfill True
                text title style "hud_title" color hud.ui.fgcolor[rbc.hud_set]
                hbox yalign 0.4 xalign 1.0 ysize 18:
                    textbutton ico('close') style 'hud_sunico_text':
                        text_size 16
                        text_color hud.ui.fgcolor[rbc.hud_set]
                        text_hover_color Color(hud.ui.fgcolor[rbc.hud_set]).tint(0.2)
                        action Function(hud_toggle,what=element)
                    null width 4


        $ hc_test=True
