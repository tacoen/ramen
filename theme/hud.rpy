init -98 python:

    # defaults
    bucket.hud = {}
    bucket.hud.disable=False
    bucket.hud.show = False
    bucket.hud.set=0
    bucket.hud.element = {}

    bucket.buff=0

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
        winbgcolor = [ '#333', '#ddd', '#333', '#ddd', '#333', '#333' ],
        element = {
            'hud': bucket.hud.show,
            'inventory': False,
            'stats': False,
            'legend': False,
            'map':False,
        },
        icons = {
            'pocket':[ '2','wallet', "Pocket", Function(hud_toggle,what='inventory') ],
            'map':[ '3','map-o' , "Map", 'map', Function(hud_toggle,what='map') ],
            'mcphone':[ '1','mobile' , "Smartphone", ToggleScreen('phone_ui') ],
        },
        hbar = {
            'energy':'#f91',
            'hygiene':'#2B2',
            'vital':'#959',
        },
        area = {
            'toolbar': [0,0,config.screen_width,config.screen_height/10],
            'stats': [16,config.screen_height/10 + 4, 224, None,(8,8,8,20)],
            'inventory': [
                config.screen_width/2, 
                config.screen_height/10 + 4,
                config.screen_width/2-16, 
                config.screen_height-(config.screen_height/10+4)-48, 
                (8,8,8,32)
            ]
        }
    )

    # why?
    
    for e in hud.ui.element.keys():
        bucket.hud.element[e] = hud.ui.element[e]

    for e in hud.ui.element.keys():
        hud.ui.element[e] = bucket.hud.element[e]

screen hud_toolbar():

    frame at pulldown background hud.ui.bgcolor[bucket.hud.set] style style['hud']['area']['toolbar']:
        hbox:
            xfill True
            yalign 0.5
            hbox xoffset 48:
                yalign 0.5
                textbutton ("{:03d}".format(mc.score)) style "hud_score":
                    action Function(hud_toggle,what='stats')
                    text_color hud.ui.fgcolor[bucket.hud.set]+"9"
                    text_hover_color hud.ui.fgcolor[bucket.hud.set]
                hbox xoffset 8 yoffset 8:
                    textbutton hud.ui.sun[wo.sun] style 'hud_sunico' text_color hud.ui.fgcolor[bucket.hud.set] action Null
                    vbox xoffset 6:
                        text "Day "+ str(wo.dayplay) color hud.ui.fgcolor[bucket.hud.set]+"9"
                        text ("{:03d}".format(mc.cash)) +" $" color hud.ui.fgcolor[bucket.hud.set] size 18
            hbox xalign 1.0 yalign 0.5:
                for m in hud.ui.icons.keys():
                    $ i = hud.ui.icons[m]
                    if m in mc.pref['icons']:
                        textbutton ico(i[1]) action i[3] style 'hud_icon':
                            text_color hud.ui.fgcolor[bucket.hud.set]+"9"
                            text_hover_color hud.ui.fgcolor[bucket.hud.set]
                    else:
                        textbutton ico(i[1]) action Null style 'hud_icon' text_color "#fff3"
                null width 32

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
        hbox xpos 32 ypos config.screen_height-gui.textbox_height-32:
            text ico('user') style "hud_sunico" size 24 at pp color tcolor
            if not hud.ui.element['stats']:
                null width 8
                text ctext color tcolor at pp

screen hud_init():

    zorder 190
    tag hud

#    $ renpy.watch(last_label)

    if not bucket.hud.disable:

        key "K_F5" action SetVariable('bucket.hud.set',ramu.cycle(bucket.hud.set,hud.ui.bgcolor))
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
            python:
                hud_tic = ico('chevrons-down')

        textbutton hud_tic xpos 16 ypos 18 action Function(hud_toggle,what='hud') style "hud_sunico":
            if hud.ui.element['hud']:
                text_color hud.ui.fgcolor[bucket.hud.set]+"6"
                text_hover_color hud.ui.fgcolor[bucket.hud.set]
            else:
                text_color "#fff9"
                text_hover_color "#fff"

        use hud_status()

screen hud_stats():

    frame background hud.ui.bgcolor[bucket.hud.set] style style['hud']['area']['stats']:
        vbox:
            use hc_tbar('stats','Stats')
            vbox:
                box_wrap_spacing 8
                spacing 12
                for topic in sorted(hud.ui.hbar.keys()):
                    use hc_hbar(topic)
                

screen hud_inventory():

    modal True
    
    python:
        inv = mc._inventory['pocket']
        iconsize = (100,100)
        w = style['hud']['area']['inventory'].xminimum
        h = style['hud']['area']['inventory'].yminimum
        tc = int(round(w / iconsize[0]))
        tr = int(round(h / iconsize[1]))+2
        
        safebgr = ramu.safecolor_for_bgr(hud.ui.bgcolor[bucket.hud.set],'#000000')
        
    frame background safebgr style style['hud']['area']['inventory']:
        vbox:
            use hc_tbar('inventory','Inventory')

            hbox ysize 32 yalign 0.5:
                text ico('wallet') style 'hud_icon_text' color hud.ui.fgcolor[bucket.hud.set]
                null width 8
                text ("{:03d}".format(mc.cash)) +" $" yalign 0.5 line_leading 2 color hud.ui.fgcolor[bucket.hud.set] size 24
            null height 16
            vpgrid:
                cols tc
                rows tr
                spacing 5
                for i in inv.keys():
                    $ item = inv[i]
                    $ icon = im.Scale(item.icon(),iconsize[0],iconsize[1]) 
                    imagebutton:
                        idle icon
                        hover im.MatrixColor(icon,im.matrix.brightness(0.5))
                        action Null
                


screen hud_legend():
    modal True
    add (Solid("#000d"))
    add (THEME_PATH+"/gui/hud-legend.png")



init python:
    config.overlay_screens.append("hud_init")

