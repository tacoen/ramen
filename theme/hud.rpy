init -203 python:

    class uiobj(ramen_object):

        def load(self,id=None,**kwargs):
            self.__dict__['param'] = {}
            self.__dict__['ui'] = rn_obj(0)
            self.set(**kwargs)
            
        def set(self,**kwargs):
        
            for k in kwargs:
                instyle = self.makestyle(k,kwargs[k])
                setattr(self.__dict__['ui'],k,kwargs[k])

        def makestyle(self, key, val):

            try: style[self.id]
            except: style[self.id] = Style(style.default)
            
            ins = False
        
            def makestyle_hbar(key,val):
            
                for t in val.keys():
                    try: bcolor = val[t]
                    except: bcolor = ramen.random_colour(128,255) 
                
                    style[self.id][key][t].thumb = bcolor 
                    style[self.id][key][t].right_bar=bcolor+"5"
                    style[self.id][key][t].left_bar=bcolor+"D"
                    style[self.id][key][t].ysize = 16                    

            def makestyle_area(key,val):
                for t in val.keys():
                
                    try: style[self.id][key][t].xpos = val[t][0]
                    except: style[self.id][key][t].xpos = 0
                    try: style[self.id][key][t].ypos = val[t][1]
                    except: style[self.id][key][t].ypos = 0
                    try: style[self.id][key][t].xsize = val[t][2]
                    except: style[self.id][key][t].xsize = config.screen_width
                    try: style[self.id][key][t].ysize = val[t][3]
                    except: style[self.id][key][t].ysize = config.screen_height
                    try: style[self.id][key][t].padding = val[t][4]
                    except: style[self.id][key][t].padding = (0,0,0,0)
                
            if key=='hbar': ins = makestyle_hbar(key,val)
            if key=='area': ins = makestyle_area(key,val)
                
init -99 python:

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
            'hud': True,
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
    
    mc.pref['icons']= ['pocket','mcphone']
    mc.pref['set'] = 0
    
    def hud_toggle(what,sfx=True):
            
        try: hud.ui.element[what]
        except: hud.ui.element[what]=True
        
        if hud.ui.element[what]:
            hud.ui.element[what]=False
            if sfx: renpy.play(DEFAULT_SFXPATH+"/tone0.mp3")
        else:
            hud.ui.element[what]=True
            if sfx: renpy.play(DEFAULT_SFXPATH+"/tone1.mp3")

    def hudset(val):
        print "masuk"
        mc.pref['set'] = val
        globals()['hud_set'] = mc.pref['set']

init:

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

    frame background hud.ui.bgcolor[hud_set] style style['hud']['area']['toolbar']:
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

    frame background hud.ui.bgcolor[hud_set] style style['hud']['area']['stats'] ysize None:
        vbox:
            for topic in sorted(hud.ui.hbar.keys()):
                use hbar(topic)

screen hbar(topic):
    python:
        xmax = style['hud']['area']['stats'].xminimum - ( style['hud']['area']['stats'].left_padding + style['hud']['area']['stats'].right_padding )
        barsty = style['hud']['hbar'][topic]
        tcolor = hud.ui.fgcolor[hud_set]
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
                
screen hud_inventory():
    text "this inventory" ypos 300
   
screen hud_init():

    zorder 190
    key "K_F5" action SetVariable('hud_set',ramu.cycle(hud_set,hud.ui.bgcolor))
    key "K_F5" action Function(hudset,val=ramu.cycle(hud_set,hud.ui.bgcolor))
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

        # game counter:
        
        use hud_status()
    
        text str(hud_set)
        
        python:
            print hud_set
        
label ramen_test:

    $ mc.stat['vital']=0
    $ hud_set =  mc.pref['set']
    
    show screen hud_init

    "we"
    "text"
    "test"
    "our"
    
