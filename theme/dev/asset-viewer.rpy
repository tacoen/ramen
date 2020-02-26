init -197 python:

    RAMEN_DEV = True
    RD = {}
    
    RD.path = ramu.fn_getdir()

    def rai_dict_unpack(obj):
        param = obj
        val = ''
        for k in param.keys():
            if isinstance(param[k], (int, str, float, unicode)): val += k + "=" + str(param[k]) + "\n"
            elif isinstance(param[k], (list)): val += k + "=" +repr(param[k])+ "\n"
            else:
                if param[k] is None: val += k +'= None\n'
                else:
                    try: val += k + "=" + rai_dict_unpack(param[k])
                    # except: val += k + "=" + repr(param[k]).replace('{','<').replace('}','>')
                    except: val += repr(type(param[k]))
                    #val += repr(param[k]).replace('{','<').replace('}','>')

        return val

    def rai_dict_unpack__s(obj):
        param = obj.__dict__
        for k in param.keys():
            if isinstance(param[k], (int, str, float)): val = str(param[k])
            elif isinstance(param[k], (list)): val = ", ".join(param[k])
            else:
                val = ''
                for v in param[k].keys():
                    if isinstance(param[k][v], (int, str, float)): val += v +"=" + str(param[k][v])
                    elif isinstance(param[k][v], (list)): val += v +"="+ ", ".join(param[k])
                    else: val += rai_dict_unpack(param[k])
        return val


style rai is default

style rai_nav is button:
    background "#666"
    hover_background "#999"
    selected_background "#ccc"
    xalign 1.0
    xsize 168
    size 16

style rai_nav_text is abel_font:
    color "#aaa"
    hover_color "#fff"
    selected_color "#333"
    text_align 1.0
    size 16

style rai_tab is button:
    background "#666"
    hover_background "#999"
    selected_background "#ccc"
    size 16

style rai_tab_text is rai_nav_text


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

        try: view
        except: view = None

        try: width
        except: width = None

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

                    frame background "#0003" padding(8, 8):
                        use rai_routecontent(tab, obj_id, view, width)


screen rai_viewertab(tab):

    hbox:
        for m in tab.keys():
            textbutton m style 'rai_tab' action SetScreenVariable('view',m)
            null width 8


    null height 8

screen rai_routecontent(tab, obj_id, view, width):

    python:
        try: route
        except: route = {}

        try: route[tab]
        except: route[tab] = {}

        route['scenery']={}
        route['scenery']['asset'] = 'rai_asset_scene'
        route['scenery']['param'] = 'rai_param'

        route['npc']={}
        route['npc']['asset'] = 'rai_asset_npc'
        route['npc']['param'] = 'rai_param'

        err = False

    if isinstance(route[tab],str):
        if renpy.has_screen(route[tab]):
            viewport:
                draggable True
                mousewheel True
                scrollbars "vertical"

                $ renpy.use_screen(route[tab],obj_id=obj_id)
        else:
            $ err = route[tab][m] + "Not here!"

    else:

        vbox:
            use rai_viewertab(route[tab])
            frame ysize 1 background "#ccc"

            if not view is None:
                viewport:
                    draggable True
                    mousewheel True
                    scrollbars "vertical"

                    if renpy.has_screen(route[tab][view]):
                        $ renpy.use_screen(route[tab][view],obj_id=obj_id,width=width)
                    else:
                        $ err = route[tab][view] + "Not here!"

    if err:
        text err


screen rai_param(obj_id):

    if not obj_id is None:

        python:
            obj = globals()[obj_id]
            param = obj.__dict__

        vbox:

            for k in param.keys():
                python:
                    if isinstance(param[k], (int, str, float)): val = str(param[k])
                    elif isinstance(param[k], (list)): val = ", ".join(param[k])
                    else:
                        try : val = rai_dict_unpack(param[k])
                        except:  val = repr(type(param[k]))

                hbox:
                    vbox xsize 200:
                        text k
                    vbox:
                        text val style 'abel_font'


screen rai_menu(tab):

    python:
        if tab in RD.keys():
            menus = RD[tab]
        if tab == 'ramen':
            menus = ['ico', 'gui', 'vars']

    frame background "#0003" padding(8, 8):

        viewport xsize 184:
            draggable True
            mousewheel True
            scrollbars "vertical"
            
            vbox xsize 168:
                
                for m in menus:
                    textbutton m style 'rai_nav' xsize 168 action SetScreenVariable('obj_id', m)
                    null height 4

screen rai_testpose(img):

    zorder 199
    
    $ bgr = ramu.fn_ezy(RD.path+"/testbgr") 
    frame background bgr xpos 0 ypos 0 xsize config.screen_width ysize config.screen_height:
    
        textbutton "close" action Hide('rai_testpose') xalign 0.9 yalign 0.1
        
        vbox at npc_align(0.5,1):
            add ( img )


screen rai_asset_npc(obj_id,width=None):

    if obj_id is not None:

        python:
            obj = globals()[obj_id]
            colect = {}

            try: width
            except: width = None

            for s in sorted(obj.pose.keys()):
                xy = renpy.image_size(obj.pose[s])
                w = 'w'+str(xy[0])
                try: colect[w]
                except: colect[w] = []
                colect[w].append([s, xy])
            
            nc = 5
            mw = math.floor( (config.screen_width-300)/ nc)
            sp = math.ceil( (config.screen_width-300)-(nc*mw) )
            
        hbox:
        
            frame background "#0003" padding(0, 8,8,8):
                viewport xsize 100:
                    draggable True
                    mousewheel True
                    scrollbars "vertical"
            
                    vbox xsize 84:
                        
                        text "Width" bold True size 12
                        null height 24
                    
                        for w in colect.keys():
                            $ ws = w.replace('w','')
                            textbutton ws action SetScreenVariable('width',w) style 'rai_nav' xsize 84
                            null height 8
                    
        
            if not width is None:
                    
                vpgrid:
                    cols int(nc)
                    spacing int(sp)
                    draggable True
                    mousewheel True

                    for s in colect[width]:
                        vbox xsize mw ysize 300 yalign 0.0 yfill False:
                            $ ih = math.ceil(mw * s[1][1] / s[1][0])
                            imagebutton action Show('rai_testpose',img=obj.pose[s[0]]):
                                idle (im.Scale(obj.pose[s[0]], mw, ih))
                            vbox:
                                text s[0] size 14 text_align 0.5
                                text repr(s[1]) size 12 text_align 0.5


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
