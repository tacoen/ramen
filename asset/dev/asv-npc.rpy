screen rai_profile(obj_id,var=None):

    if not obj_id is None:

        python:
            collect={}
            collect['bio']={}
            collect['sta']={}
            obj = globals()[obj_id]

            ppic = ramu.get_profilepic(obj_id, size=(96, 96))

            co = [ 'name','lastname','callname','phonenum','gender','color','wcolor','dir' ]

            for c in co:
                try: collect['bio'][c] = obj.param[c]
                except: collect['bio'][c] = None
                
            try:
                for s in mc.rel[obj_id].keys():
                    collect['sta'][s] = mc.rel[obj_id][s]
            except: pass
                
        text 'profile' size 48
        
        hbox yoffset 64:
            add ppic
            null width 24
        
            vbox:
            
                for c in collect['sta'].keys():
                    hbox:
                        text c min_width 200
                        text str(collect['sta'][c])
                    null height 8
    
                null height 8
                frame background "#999" ysize 1
                null height 8
                
                for c in collect['bio'].keys():
                    hbox:
                        text c min_width 200
                        text str(collect['bio'][c])
                    null height 8


screen rai_asset_npc(obj_id,var=None):

    if not obj_id is None:

        python:
            obj = globals()[obj_id]
            collect = {}

            try: var
            except: var = None

            try:
                for s in sorted(obj.pose.keys()):
                    xy = renpy.image_size(obj.pose[s])
                    w = 'w'+str(xy[0])
                    try: collect[w]
                    except: collect[w] = []
                    collect[w].append([s, xy])
            except:
                pass
                
            nc = 5
            mw = math.floor( (config.screen_width-300)/ nc)
            sp = math.ceil( (config.screen_width-300)-(nc*mw) )
            
        hbox:
        
            frame background "#0003" padding(0, 8,8,8):
                viewport xsize 100:
                    draggable True
                    mousewheel True
                    scrollbars "vertical"
                    style_prefix 'rai_nav'
            
                    vbox xsize 84:
                        
                        text "Width" bold True size 12
                        null height 24
                    
                        python:
                            nl = [w.replace('w', '') for w in collect.keys()]
                            nl = list(map(int, nl))
                        
                        for w in sorted(nl):
                            $ ws = "w"+str(w)
                            textbutton str(w) action SetScreenVariable('var',ws) xsize 84
                            null height 8
                    
            python:
                try: collect[var]
                except: var = None
        
            if not var is None:
                    
                vpgrid:
                    cols int(nc)
                    spacing int(sp)
                    draggable True
                    mousewheel True

                    for s in collect[var]:
                        vbox xsize mw ysize 300 yalign 0.0 yfill False:
                            $ ih = math.ceil(mw * s[1][1] / s[1][0])
                            imagebutton action Show('rai_testpose',img=obj.pose[s[0]]):
                                idle (im.Scale(obj.pose[s[0]], mw, ih))
                            vbox:
                                text s[0] size 14 text_align 0.5
                                text repr(s[1]) size 12 text_align 0.5


screen rai_testpose(img):

    zorder 199
    layer 'interface'
    
    python:
        try: xa
        except: xa = 0.5
        try: zo
        except: zo=1.0
        try: dec
        except: dec = 0.1
        try: ghost
        except: ghost = False
        
    $ bgr = ramu.fn_ezy(RD.path+"/testbgr") 
    
    
    frame background bgr xpos 0 ypos 0 xsize config.screen_width ysize config.screen_height:
        padding (0,0)
        
        if locals()['ghost']:
            add (ramu.fn_ezy(RD.path+"/ghost")) 
    
        vbox at npc_align(xa,zo):
            add ( img )
    
        frame background "#0004" xsize 200 xpos config.screen_width-200 ysize config.screen_height:
            
            padding (8,8)
            
            vbox xsize 184:
                
                textbutton "close" action Hide('rai_testpose') xalign 1.0 text_size 16
                
                null height 64
                
                hbox yalign 0.5 xfill True:
                    style_prefix 'rai_opt'
                    textbutton "0.1" action SetLocalVariable('dec',0.1)
                    null width 2
                    textbutton "0.05" action SetLocalVariable('dec',0.05)
                    null width 2
                    textbutton "0.01" action SetLocalVariable('dec',0.01)
                null height 16
                
                hbox yalign 0.5:
                    textbutton "ghost" action SetLocalVariable('ghost',ramu.ltoggle(ghost)) style 'rai_opt_button'
                null height 16
                
                hbox yalign 0.5 xfill True:
                    style_prefix 'rai_ctl'
                    textbutton "-" action SetLocalVariable('xa',mval(xa,-dec,[0.0,1.0]))
                    textbutton str(locals()['xa']) action SetLocalVariable('xa',0.5)
                    textbutton "+" action SetLocalVariable('xa',mval(xa,dec,[0.0,1.0]))
                null height 16

                hbox yalign 0.5 xfill True:
                    style_prefix 'rai_ctl'
                    textbutton "-" action SetLocalVariable('zo',mval(zo,-dec,[0.1,2.0]))
                    textbutton str(locals()['zo']) action SetLocalVariable('zo',1.0)
                    textbutton "+" action SetLocalVariable('zo',mval(zo,dec,[0.1,2.0]))
                null height 16

                text "at npc_align("+str(locals()['xa'])+","+str(locals()['zo'])+")" style 'rai_text' size 16
