init -99 python:

    class scenery(ramen_object):

        def load(self,id=None,**kwargs):

            scenes = self.files('scene')
            cond = {}
            condition = list(dict.fromkeys(wo.sunword))
            condition2 =  list(dict.fromkeys(wo.timeword))

            for file in sorted(scenes):
                fn = ramu.fn_info(file)

                if " " in fn['name']:
                    fc = fn['name'].split(' ')
                    fn['name'] = fc[0]
                    fn[str('cond')] = fc[1]

                try: self.main
                except:
                    fn = ramu.fn_info(scenes[0])
                    self.main = fn['name']

                try: cond[fn['name']]
                except KeyError: cond[fn['name']] = ()

                f = file

                for s in condition:
                    if fn['name'] +" "+s in fn['file']:
                        cond[fn['name']] += ("wo.suntime=='"+s+"'",f)
                        scenes.remove(f)

                for s in condition2:
                    if fn['name'] +" "+s in fn['file']:
                        cond[fn['name']] += ("wo.daytime=='"+s+"'",f)
                        scenes.remove(f)

                # the default condition

                m1 = fn['name']+"."+fn['ext']

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
                fn = ramu.fn_info(f)
                renpy.image(self.id+" "+fn['name'],f)

                if self.main and self.main == fn['name']:
                    renpy.image(self.id,f)

            return

        def shortcut(self,id=None,**kwargs):

            try: self.short
            except: self.short = {}

            if not id is None:

                try: self.short[id]
                except: self.short[str(id)] = {}

                for k in kwargs:
                    self.short[id][k] = kwargs[k]

                try: self.short[id]['icon']
                except: self.short[id][str('icon')] =  'arrow-left'

                try: self.short[id]['goto']
                except: self.short[id][str('goto')] =  str(id)

                try: self.short[id]['text']
                except: self.short[id][str('text')] =  str(id).title()

        def mazing(self,**kwargs):

            maze = {}
            self.map = {}
            ahs = {}

            for k in kwargs:
                maze[k] = kwargs[k]

            for f in sorted(maze['floor']):

                ahs[f] = maze['hs'].copy()

                try: ahs[f].update(maze['add'][f])
                except: pass

                #print hs[f].keys()

                self.map[f] = {}

                up = maze['floor'].index(f)+1
                down = maze['floor'].index(f)-1

                if up > len(maze['floor'])-1: up = None
                if down < 0: down = None

                for i in sorted(ahs[f].keys()):

                    hs = ahs[f]

                    try:
                        xy = (hs[i][0][0],hs[i][0][1])
                    except:
                        xy = False

                    try:
                        func = hs[i][1]
                    except:
                        func = 'goto'

                    dest = i

                    if func == 'map':
                        dest = None
                        if "up" in i:
                            if not up is None : dest = maze['floor'][up]
                        if "down" in i:
                            if not down is None: dest = maze['floor'][down]
                    else:
                        dest = i

                    try:
                        img = hs[i][2]
                    except:
                        img = i

                    if not dest is None and xy:
                        self.map[f][i] = [ xy, func, dest, img ]

            return self.map

        def scene_call(self,what,obj_id,f,r):
            renpy.call_in_new_context(what,obj_id=obj_id, f=f, r=r)

        def imagemaping(self,floor,bgr=None):

            if bgr is None: bgr = self.get_sceneimg()

            img = {}
            img['ground'] = bgr
            gimg = tuple()
            himg = tuple()
            imgdata=[]
            shortcuts=[]
            gimg = ( (0,0), bgr )
            himg = ( (0,0), Solid('#fff0'))

            ways = self.map[floor]

            for k in sorted(ways.keys()):

                w = ways[k]

                action = False
                hover = False
                xy = w[0]

                if not xy is None:

                    if renpy.has_label(w[1]):
                        action = Jump(w[1])
                    if renpy.has_label(self.id+"_"+w[1]):
                        action = Jump(self.id+"_"+w[1])
                    if renpy.has_label('_'+self.id+'_'+w[1]):
                        action = Function(self.scene_call, obj_id=self.id, what='_'+self.id+'_'+w[1], r=w[2], f=floor)
                    if renpy.has_label('_scene_'+w[1]):
                        action = Function(self.scene_call, obj_id=self.id, what='_scene_'+w[1], r=w[2], f=floor)

                    file = ramu.fn_ezy(self.dir +"/hs/"+w[3])

                    if file:
                        ground = file
                        area = xy + renpy.image_size(ground)
                        hover = im.MatrixColor(ground,im.matrix.brightness(0.1))
                    else:
                        ground = False
                        area = False

                    file = ramu.fn_ezy(self.dir +"/hs/"+w[3]+"-hover")
                    if file:
                        hover = file
                        if not area:
                            area = xy + renpy.image_size(hover)
                        if not ground:
                            #ground = RAMEN_PATH + "/img/blank.png"
                            ground = Solid('#0000')

                    if hover: himg = himg + ( xy, hover )
                    if ground: gimg = gimg + ( xy,ground )
                    if area: imgdata.append( [ area, action ] )

                    img['ground'] = LiveComposite( (1280,720), *gimg )
                    img['hover'] = LiveComposite( (1280,720), *himg )
                    img['data'] = imgdata

            try:  img['shortcut'] = self.short
            except: pass

            return img


screen scene_imagemap(img):

    # map

    imagemap xpos 0 ypos 0:
        ground img['ground']
        hover img['hover']
        for h in img['data']:
           hotspot h[0] action h[1]

    # shortcut

    python:
        try: shortcuts = img['shortcut']
        except: shortcuts = None

    if not shortcuts is None:
        use scene_shortcut(shortcuts)


style shortcut_icon is icoram:
    xalign 0.5

style shortcut_icon_text is icoram:
    size 24
    min_width 30
    text_align 0.5
    outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]
    color "#fffc"
    hover_color "#fff"

style shortcut is gui_text

style shortcut_text is default:
    outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]
    size 22
    line_leading -2
    color "#fffc"
    hover_color "#fff"

screen scene_shortcut(shorts):

    python:
        y = config.screen_height * 7/8
        x = 32
        s = 48
        spos = [
            [ x, y ],
            [ x, y - s ],
            [ x, y - (2*s) ],
        ]

    for s in shorts:
        python:
            si = shorts.keys()
            d = shorts[s]
            try: d['pos']
            except: d['pos'] = si.index(s)

            try:
                if renpy.has_label(d['goto']):
                    Action = Jump(d['goto'])
                else:
                    Action = Null

            except: Action = Null

        hbox xalign 1.0 xanchor 1.0 ypos spos[d['pos']][1]:
            textbutton d['text'] style 'shortcut' action Action
            null width 6
            textbutton ico(d['icon']) style 'shortcut_icon' action Action
            null width 32


screen _overlays(obj_id, data):

    python:
        if not obj_id is None: obj = globals()[obj_id]

    for d in data:
        python:
            img = ramu.fn_ezy(obj.dir +"/overlays/"+d[0])
            xy = d[1]

        if img:
            hbox pos xy:
                add img

label _scene_goto(obj_id=None,d=None,f=None,r=None):

    python:
        if r is None: r = ''
        if not obj_id is None: obj = globals()[obj_id]

    "is [d] [f] [r]"

label _scene_elevator(obj_id=None,f=None,r=None):
    hide screen scene_imagemap
    "elevator"
    return

label _scene_map(obj_id=None,f=None,r=None):

    hide screen scene_imagemap

    python:
        if not obj_id is None: obj = globals()[obj_id]
        renpy.scene()
        renpy.show(obj_id + " "+r)
        map = obj.imagemaping(r, ramu.get_sceneimg())

    call screen scene_imagemap(map)


    return