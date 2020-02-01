init -99 python:

    # defaults

    gbuff = object()
    gbuff.disable=False
    gbuff.show=False
    gbuff.set=0
    gbuff.buff=0

    mc.pref['icons']= ['pocket','mcphone']

    # hub object

    hud = uiobj(id='hud',
        x=0,
        y=0,
        w=config.screen_width,
        h=config.screen_height/10,
        sun=['g','a','c','d','e'],
        bgcolor = [ "#0000", "#fff", "#000c", "#fffc", "#123", "#123c" ],
        fgcolor = [ "#eee", "#111", "#fff", "#000", "#eee", "#fff" ],
        element = {
            'inventory': False,
            'stats': False,
            'legend': False,
            'hud': gbuff.show,
        },
        icons = {
            'pocket':[ '2','W', "Pocket", 'inventory_ui'],
            'map':[ '3','M' , "Map", 'map','map' ],
            'mcphone':[ '1','P' , "Smartphone", 'phone_ui'],
        },
        hbar = {
            'energy':'#ff0',
            'hygiene':'#3c3',
            'vital':'#acd',
        },
        area = {
            'toolbar': [0,0,config.screen_width,config.screen_height/10],
            'stats': [48,config.screen_height/10 + 1, 224, config.screen_height/2,(8,8,8,8)]
        }
    )

    def hud_toggle(what,sfx=True):

        try: hud.ui.element[what]
        except: hud.ui.element[what]=True

        if hud.ui.element[what]:
            hud.ui.element[what]=False
            if sfx: renpy.play(DEFAULT_SFXPATH+"/tone0.mp3")
        else:
            hud.ui.element[what]=True
            if sfx: renpy.play(DEFAULT_SFXPATH+"/tone1.mp3")


init:

    default gbuff = gbuff

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

    transform pulse:
        block:
            linear 0.3 alpha 1
            pause 0.5
            linear 0.5 alpha 0.3
            pause 0.5
            repeat

    transform pulse_fine:
        block:
            linear 0.2 alpha 1
            pause 1.5
            linear 0.2 alpha 0.7
            repeat

    transform pulse_dying:
        block:
            linear 0.3 alpha 1
            pause 0.3
            linear 0.3 alpha 0.1
            repeat

screen hud_toolbar():

    frame background hud.ui.bgcolor[gbuff.set] style style['hud']['area']['toolbar']:
        hbox:
            xfill True
            yalign 0.5
            hbox xoffset 48:
                yalign 0.5
                textbutton ("{:03d}".format(mc.score)) style "hud_score":
                    action ToggleScreen('hud_stats')
                    text_color hud.ui.fgcolor[gbuff.set]+"9"
                    text_hover_color hud.ui.fgcolor[gbuff.set]
                hbox xoffset 8 yoffset 8:
                    textbutton hud.ui.sun[wo.sun] style 'hud_sunico' text_color hud.ui.fgcolor[gbuff.set] action Null
                    vbox xoffset 6:
                        text "Day "+ str(wo.dayplay) color hud.ui.fgcolor[gbuff.set]+"9"
                        text ("{:03d}".format(mc.cash)) +" $" color hud.ui.fgcolor[gbuff.set] size 18
            hbox xalign 1.0 yalign 0.5:
                for m in hud.ui.icons.keys():
                    $ i = hud.ui.icons[m]
                    if m in mc.pref['icons']:
                        textbutton i[1] action ToggleScreen(i[3]) style 'hud_icon':
                            text_color hud.ui.fgcolor[gbuff.set]+"9"
                            text_hover_color hud.ui.fgcolor[gbuff.set]
                    else:
                        textbutton i[1] action Null style 'hud_icon' text_color "#fff3"
                null width 32

screen hud_stats():

    frame background hud.ui.bgcolor[gbuff.set] style style['hud']['area']['stats'] ysize None:
        vbox:
            for topic in sorted(hud.ui.hbar.keys()):
                use hbar(topic)

screen hbar(topic):
    python:
        xmax = style['hud']['area']['stats'].xminimum - ( style['hud']['area']['stats'].left_padding + style['hud']['area']['stats'].right_padding )
        barsty = style['hud']['hbar'][topic]
        tcolor = hud.ui.fgcolor[gbuff.set]
        val = mc.stat[topic]
        max = 10

    vbox:
        hbox xminimum xmax:
            xfill True
            text topic.title() style 'hud_label' color tcolor size 12 xalign 0
            text str(val)+"/"+str(max) style 'hud_label' color tcolor size 12 xalign 1.0 text_align 1.0
        null height 2
        bar range max value val style barsty xmaximum xmax ysize 12
        null height 12

screen hud_status():

    python:
        ct={}
        ct['energy'] = ['You are very hungry.', 'Eat something.',2 ]
        ct['vital'] = ['You tired.', 'Rest a while.',4 ]
        ct['hygiene'] = ['You need a bath.', 'Keep Clean.',24 ]

        pp = False
        ctext = ''

        w = False

        for s in hud.ui.hbar.keys():

            if not w:

                if mc.stat[s] > 2 and mc.stat[s] < 5:
                    ctext = ct[s][1]
                    pp = pulse
                    w=s
                elif mc.stat[s] <= 2:
                    ctext = ct[s][0]
                    pp = pulse_dying
                    w=s
                    globals()['doom'] = wo.time + datetime.timedelta(hours=ct[s][2])

        try: tcolor = hud.ui.hbar[w]+"9"
        except: tcolor = hud.ui.fgcolor[w]+"9"

    if pp:
        hbox xpos 16 ypos 88:
            text ico('user') style "hud_sunico" size 24 at pp color tcolor
            if not hud.ui.element['stats']:
                null width 8
                text ctext color tcolor at pp

screen hud_init():

    zorder 190
    tag hud

    if not gbuff.disable:

        key "K_F5" action SetVariable('gbuff.set',ramu.cycle(gbuff.set,hud.ui.bgcolor))
        key "K_F6" action Function(hud_toggle,what='stats')
        key "K_F8" action Function(hud_toggle,what='hud')
        key "shift_K_F8" action Function(ramu.toggle,what='quick_menu')
        key "ctrl_K_F1" action Function(hud_toggle,what='legend')

        key "K_F9" action Function(hud_toggle,what='inventory')


        if hud.ui.element['hud']:
            $ hud_tic = ico('chevrons-up')
            if hud.ui.element['legend']:
                use hud_legend
            if hud.ui.element['stats']:
                use hud_stats
            if hud.ui.element['inventory']:
                use hud_inventory
            use hud_toolbar
        else:
            $ hud_tic = ico('chevrons-down')

        textbutton hud_tic xpos 16 ypos 18 action Function(hud_toggle,what='hud') style "hud_sunico":
            if hud.ui.element['hud']:
                text_color hud.ui.fgcolor[gbuff.set]+"6"
                text_hover_color hud.ui.fgcolor[gbuff.set]
            else:
                text_color "#fff9"
                text_hover_color "#fff"


        $ gbuff.show = hud.ui.element['hud']

        use hud_status()


init python:
    config.overlay_screens.append("hud_init")

screen hud_inventory():
    text "this inventory" ypos 300

screen hud_legend():
    modal True
    add (Solid("#000d"))
    add (THEME_PATH+"/gui/hud-legend.png")

