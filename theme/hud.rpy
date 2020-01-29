init -99 python:

    hud = ramen_object(id='hud')
    hud.set_ui(
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
            'hud': True,
        },
        icons = {
            'pocket':[ '2','W', "Pocket", 'inventory_ui'],
            'map':[ '3','M' , "Map", 'map','map' ],
            'mcphone':[ '1','P' , "Smartphone", 'phone_ui'],
        },
        bars = {
            'energy':'#ff0',
            'hygiene':'#3c3',
            'vital':'#acd',
        }
    )
    
    mc.pref = {}
    mc.pref['icons']= ['pocket','mcphone']
    
    def hud_toggle(what,sfx=True):
            
        try: hud.ui.element[what]
        except: hud.ui.element[what]=True
        
        if hud.ui.element[what]:
            hud.ui.element[what]=False
            if sfx: renpy.play(DEFAULT_SFXPATH+"/tone0.mp3")
        else:
            hud.ui.element[what]=True
            if sfx: renpy.play(DEFAULT_SFXPATH+"/tone1.mp3")
        

init -1:
    default hud_show = hud.ui.element['hud']
    default hud_disable = False
    default hud_set = 0

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

screen hud_toolbar():

    frame background hud.ui.bgcolor[hud_set] style "hud_toolbar":
        hbox:
            xfill True
            yalign 0.5
            hbox xoffset 48:
                yalign 0.5
                textbutton ("{:03d}".format(mc.score)) style "hud_score":
                    action ToggleScreen('hud_stats')
                    text_color hud.ui.fgcolor[hud_set]+"9"             
                    text_hover_color hud.ui.fgcolor[hud_set]                     
                hbox xoffset 8 yoffset 8:
                    textbutton hud.ui.sun[wo.sun] style 'hud_sunico' text_color hud.ui.fgcolor[hud_set] action Null
                    vbox xoffset 6:
                        text "Day "+ str(wo.dayplay) color hud.ui.fgcolor[hud_set]+"9"
                        text ("{:03d}".format(mc.cash)) +" $" color hud.ui.fgcolor[hud_set] size 18              
            hbox xalign 1.0 yalign 0.5:
                for m in hud.ui.icons.keys():
                    $ i = hud.ui.icons[m]
                    if m in mc.pref['icons']:
                        textbutton i[1] action ToggleScreen(i[3]) style 'hud_icon':
                            text_color hud.ui.fgcolor[hud_set]+"9" 
                            text_hover_color hud.ui.fgcolor[hud_set]
                    else:
                        textbutton i[1] action Null style 'hud_icon' text_color "#fff3"
                null width 32



screen hud_legend():
    text "this legend" ypos 100

screen hud_stats():
    frame ypos 200 xsize 300 background hud.ui.bgcolor[hud_set]:
        python:
            xmax =280
            topic = 'vital'
            barsty = style.hbar[topic]
            val = mc.stat['vital']
            max = 10
            tcolor = hud.ui.fgcolor[hud_set]
        vbox xoffset 8:
            hbox xmaximum xmax:
                xfill True
                text topic.title() style 'hud_label' color tcolor size 12 xalign 0
                text str(val)+"/"+str(max) style 'hud_text' color tcolor size 12 xalign 1.0 text_align 1.0
            null height 4
            bar range max value val style barsty xmaximum xmax ysize 12
            null height 16        

screen hud_inventory():
    text "this inventory" ypos 300
   
screen hud_init():

    zorder 190
    key "K_F5" action SetVariable('hud_set',ramu.cycle(hud_set,hud.ui.bgcolor))
    key "K_F6" action Function(hud_toggle,what='legend')
    key "K_F7" action Function(hud_toggle,what='stats')
    key "K_F8" action Function(hud_toggle,what='inventory')
    key "K_F9" action Function(hud_toggle,what='hud')
    key "shift_K_F9" action Function(ramu.toggle,what='quick_menu')
    
    if not hud_disable:
    
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
                text_color hud.ui.fgcolor[hud_set]+"6"
                text_hover_color hud.ui.fgcolor[hud_set]
            else:
                text_color "#fff9"
                text_hover_color "#fff"
    
    
label ramen_test:

    show screen hud_init

    "we"
    "text"
    "test"
    "our"
    
