init -99 python:

    class scenery(ramen_object):

        def load(self,id=None,**kwargs):

            scenes=self.files('scene')
            cond={}
            condition=list(dict.fromkeys(wo.sunword))
            condition2= list(dict.fromkeys(wo.timeword))

            for file in sorted(scenes):
                fn=ramu.fn_info(file)

                if " " in fn['name']:
                    fc=fn['name'].split(' ')
                    fn['name']=fc[0]
                    fn[str('cond')]=fc[1]

                try: self.main
                except:
                    fn=ramu.fn_info(scenes[0])
                    self.main=fn['name']

                try: cond[fn['name']]
                except KeyError: cond[fn['name']]=()

                f=file

                for s in condition:
                    if fn['name'] +" "+s in fn['file']:
                        cond[fn['name']] += ("wo.suntime=='"+s+"'",f)
                        scenes.remove(f)

                for s in condition2:
                    if fn['name'] +" "+s in fn['file']:
                        cond[fn['name']] += ("wo.daytime=='"+s+"'",f)
                        scenes.remove(f)

                # the default condition

                m1=fn['name']+"."+fn['ext']

                if (m1==fn['file']) and (len(cond[fn['name']])>1):
                   cond[fn['name']] += (True,f)
                   scenes.remove(f)

                # create base on condition

                for cs in cond.keys():
                    renpy.image(self.id+" "+cs,ConditionSwitch(*cond[cs]))

                    if self.main and self.main == cs:
                        renpy.image(self.id, ConditionSwitch(*cond[cs]))

            # create leftover

            for f in scenes:
                fn=ramu.fn_info(f)
                renpy.image(self.id+" "+fn['name'],f)

                if self.main and self.main == fn['name']:
                    renpy.image(self.id,f)

            return

        def shortcut(self,id=None,**kwargs):

            try: self.short
            except: self.short={}

            if not id is None:

                try: self.short[id]
                except: self.short[str(id)]={}

                for k in kwargs:
                    self.short[id][k]=kwargs[k]

                try: self.short[id]['icon']
                except: self.short[id][str('icon')]= 'arrow-left'

                try: self.short[id]['goto']
                except: self.short[id][str('goto')]= str(id).lower()

                try: self.short[id]['text']
                except: self.short[id][str('text')]= str(id).title()

                try: self.short[id]['hide_on']
                except: self.short[id][str('hide_on')]= None

                try: self.short[id]['position']
                except: self.short[id][str('position')]= 'right'

        def mazing(self,**kwargs):

            maze={}
            ahs={}
            
            try: self.map
            except: self.map={}

            for k in kwargs:
                maze[k]=kwargs[k]

            try: maze['floor']
            except: maze['floor'] = []

            try:
                for f in maze['add'].keys():
                    if not f in maze['floor']:
                        maze['floor'].append(f)
            except: 
                pass
            
            for f in sorted(maze['floor']):

                try: ahs[f]=maze['hs'].copy()
                except: ahs[f] = {}

                try: ahs[f].update(maze['add'][f])
                except: pass

                self.map[str(f)]={}

                up=maze['floor'].index(f)+1
                down=maze['floor'].index(f)-1

                if up > len(maze['floor'])-1: up=None
                if down < 0: down=None

                for i in sorted(ahs[f].keys()):

                    hs=ahs[f]

                    try:
                        xy=(hs[i][0][0],hs[i][0][1])
                    except:
                        xy=False

                    try:
                        func=str(hs[i][1])
                    except:
                        func='goto'

                    dest=i

                    if func == 'map':
                        dest=None
                        if "up" in i:
                            if not up is None : dest=maze['floor'][up]
                        if "down" in i:
                            if not down is None: dest=maze['floor'][down]
                    else:
                        dest=i

                    try:
                        img=hs[i][2]
                    except:
                        img=i

                    if not dest is None and xy:
                        self.map[f][str(i)]=[ xy, str(func), str(dest), str(img) ]

            return self.map

        def scene_call(self,what,id,f,d):
            rbc.data('scene_map',id=id, f=f, d=d)
            renpy.jump(what)
            #renpy.call_in_new_context(what,obj_id=obj_id)

        def imagemaping(self, floor, bgr=None):

            if not bgr or bgr is None: 
                bgr=self.get_sceneimg()

            img={}
            img['ground']=bgr
            gimg=tuple()
            himg=tuple()
            imgdata=[]
            shortcuts=[]
            gimg=( (0,0), bgr )
            himg=( (0,0), Solid('#fff0'))

            ways=self.map[floor]

            for k in sorted(ways.keys()):

                w=ways[k]

                action=False
                hover=False
                xy=w[0]

                if not xy is None:

                    #print w
                    # w
                    # 0 xy
                    # 1 key/func
                    # 2 hs code
                    # 3 img

                    if renpy.has_label(w[2]):
                        action=Jump(w[2])
                    elif renpy.has_label(self.id+'_'+w[2]):
                        action=Function(self.scene_call, what=self.id+'_'+w[2], id=self.id, f=floor, d=w[2])

                    elif renpy.has_label(w[1]):
                        action=Jump(w[1])
                    elif renpy.has_label(self.id+'_'+floor+"_"+w[1]):
                        action=Jump(self.id+'_'+floor+"_"+w[1])
                    elif renpy.has_label(self.id+'_'+w[1]):
                        action=Function(self.scene_call, what=self.id+'_'+w[1], id=self.id, f=floor, d=w[2])
                    elif renpy.has_label('_scene_'+w[1]):
                        action=Function(self.scene_call, what='_scene_'+w[1], id=self.id, f=floor, d=w[2])

                    else:
                        action=False

                    file=ramu.fn_ezy(self.dir +"/hs/"+w[3])

                    if file:
                        ground=file
                        area=xy + renpy.image_size(ground)
                        hover=im.MatrixColor(ground,im.matrix.brightness(0.1))
                    else:
                        ground=False
                        area=False

                    file=ramu.fn_ezy(self.dir +"/hs/"+w[3]+"-hover")
                    if file:
                        hover=file
                        if not area:
                            area=xy + renpy.image_size(hover)
                        if not ground:
                            #ground=RAMEN_PATH + "/img/blank.png"
                            ground=Solid('#0000')

                    if hover:
                        himg=himg + ( xy, hover )
                    if ground:
                        gimg=gimg + ( xy,ground )
                    if area:
                        imgdata.append( [ area, action ] )

                    img['ground']=LiveComposite( (1280,720), *gimg )
                    img['hover']=LiveComposite( (1280,720), *himg )
                    img['data']=imgdata

            try:  img['shortcut']=self.short
            except: pass

            return img

        def random_image(self,prefix,scope=None):
            if scope is None:
                scope=''
            imgs=self.files('overlays/'+scope)
            res=[]
            for file in imgs:
                fn=ramu.fn_info(file)
                if fn['file'].startswith(str(prefix)):
                    res.append(fn['path']+"/"+fn['name'])

            return  ramu.random_of(res)


# scene map ###################################################################

screen scene_mapping(obj, scene_id, img=None, overlays=None, shortcut_position=None ):

    if not img is None:

        $ img = obj.imagemaping(scene_id, img)
    
        imagemap xpos 0 ypos 0:
            ground img['ground']
            hover img['hover']
            for h in img['data']:
                hotspot h[0] action h[1]

    # overlays
    
    if not overlays is None:
        use _iblays(obj.id, overlays, True)

    # shortcut

    python:
        try: shortcuts=img['shortcut']
        except: shortcuts=None

    if not shortcuts is None:
        use scene_shortcut( scene_id, shortcuts, shortcut_position)

label _scene_map:

    hide screen scene_mapping

    python:
        obj_id=rbc.scene_map['id']
        f=rbc.scene_map['f']
        d=rbc.scene_map['d']
        obj=globals()[obj_id]

        renpy.scene()
        renpy.show(obj_id + " "+d)
        renpy.with_statement(dissolve)

        # rbc
        #map=obj.imagemaping(d, ramu.get_sceneimg())

    call screen scene_mapping(obj, d, ramu.get_sceneimg())

    return

label _scene_goto:

    hide screen scene_mapping

    python:
        obj_id=rbc.scene_map['id']
        f=rbc.scene_map['f']
        d=rbc.scene_map['d']
        obj=globals()[obj_id]
        doors=[]
        target=['knock', 'peek', 'key' ]

        for t in target:
            if renpy.has_label(obj_id+"_"+f+"_"+d+"_"+ t):
                if t == "key":
                    tn="Open (key)"
                else:
                    tn=t
                doors.append(( tn, obj_id+"_"+f+"_"+d+"_"+ t ))

        if not doors == []:
            doors.append(('Exit','Return'))

            renpy.scene()
            renpy.show(obj_id + " door")
            renpy.with_statement(dissolve)

            choice=menu(doors)

            if choice=='Return':
                renpy.jump('_back')
            else:
                renpy.jump(choice)

    "Nothing responding..."

    label _back:
        python:
            rbc.data('scene_map',f=d,d=f,id=obj_id)
            renpy.jump('_scene_map')

    return



## scene_shorcut #######################################################

style shortcut_icon is icoram:
    xalign 0.5

style shortcut_icon_text is icoram:
    size 24
    min_width 30
    text_align 0.5
    outlines [ (absolute(2), "#0006", absolute(0), absolute(0)) ]
    color "#fffc"
    hover_color "#fff"

style shortcut is gui_text

style shortcut_text is default:
    outlines [ (absolute(2), "#0006", absolute(0), absolute(0)) ]
    size 22
    line_leading -2
    color "#fffc"
    hover_color "#fff"

screen scene_shortcut(scene_id, shorts, position=None):

    python:
        y=config.screen_height * 7/8
        x=32
        s=48
        n=int(round(y / 48))
        spos=[]
        spos.append([ x,y ])
        for i in range(1,n):
            spos.append([ x,y-(i*s) ])
        pos=-1

    for s in shorts:

        python:
            show=True
            d=shorts[s]

            if position is None:
                position=d['position']

            try: d['hide_on']
            except: d['hide_on']=None

            try: d['show_on']
            except: d['show_on']=None

            if not d['hide_on'] is None:
                if scene_id in d['hide_on']:
                    show=False
                else:
                    show=True

            if not d['show_on'] is None:

                if scene_id in d['show_on']:
                    show=True
                else:
                    show=False

        if show:

            python:
                pos +=1
                d['pos']=pos
                if renpy.has_label(d['goto']):
                    Action=Jump (d['goto'])
                else:
                    Action=Null

            if not Action == Null:
                if position == 'right':
                    hbox xalign 1.0 xanchor 1.0 ypos spos[d['pos']][1]:
                        textbutton d['text'] style 'shortcut' action Action
                        null width 6
                        textbutton ico(d['icon']) style 'shortcut_icon' action Action
                        null width 32
                else:
                    hbox xalign 0.0 ypos spos[d['pos']][1]:
                        null width 32
                        textbutton ico(d['icon']) style 'shortcut_icon' action Action
                        null width 6
                        textbutton d['text'] style 'shortcut' action Action
