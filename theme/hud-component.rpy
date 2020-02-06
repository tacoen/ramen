init -99 python:

    def hud_toggle(what,sfx=True):

        try: hud.ui.element[what]
        except: hud.ui.element[what]=True

        if hud.ui.element[what]:
            hud.ui.element[what]=False
            if sfx: renpy.play(DEFAULT_SFXPATH+"/tone0.mp3")
        else:
            hud.ui.element[what]=True
            if sfx: renpy.play(DEFAULT_SFXPATH+"/tone1.mp3")

        bucket.hud.element[what] = hud.ui.element[what]

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


    screen hc_hbar(topic):
    
        python:
            xmax = style['hud']['area']['stats'].xminimum - ( style['hud']['area']['stats'].left_padding + style['hud']['area']['stats'].right_padding )
            barsty = style['hud']['hbar'][topic]
            tcolor = hud.ui.fgcolor[bucket.hud.set]
            val = mc.stat[topic]
            try: max = mc._limit[topic][1]
            except: max = mc._limit['stat'][1]

        vbox:
            hbox xminimum xmax:
                xfill True
                text topic.title() style 'hud_label' color tcolor size 12 xalign 0
                text str(val)+"/"+str(max) style 'hud_label' color tcolor size 12 xalign 1.0 text_align 1.0
            null height 2
            bar range max value val style barsty xmaximum xmax ysize 12

    screen hc_tbar(element,title=''):
    
        python:
            xmax = style['hud']['area'][element].xminimum-2
            
        frame background Color(hud.ui.bgcolor[bucket.hud.set]).shade(0.5):
            xsize xmax
            xoffset -7
            yoffset -7
            hbox:
                xfill True
                text title style "hud_title" color hud.ui.fgcolor[bucket.hud.set] 
                hbox yalign 0.4 xalign 1.0 ysize 18:
                    textbutton ico('close') style 'hud_sunico_text':
                        text_size 16
                        text_color hud.ui.fgcolor[bucket.hud.set]
                        text_hover_color Color(hud.ui.fgcolor[bucket.hud.set]).tint(0.2)
                        action Function(hud_toggle,what=element) 
                    null width 4
                    

        $ hc_test = True

label ramen_test:
    $ bucket.test = True
    "1"
    "lu lagi bikin inventory screen"
    "2"
    "3"
    