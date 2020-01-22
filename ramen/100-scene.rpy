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
                   Files.remove(f)

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
                        func = 'door'

                    dest = i
                    
                    if func == 'lead':
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
            gimg = ( (0,0), bgr )
            himg = ( (0,0), Solid('#fff0'))

            ways = self.map[floor]

            for k in sorted(ways.keys()):
                
                w = ways[k]

                action = False
                
                if renpy.has_label(w[1]):
                    action = Jump(w[1])
                if renpy.has_label(self.id+"_"+w[1]):
                    action = Jump(self.id+"_"+w[1])
                if renpy.has_label('_scene_'+w[1]):
                    action = Function(self.scene_call, obj_id=self.id, what='_scene_'+w[1], r=w[2], f=floor)
                
                file = ramu.fn_ezy(self.dir +"/hotspot/"+w[3])
                if file:
                    ground = file
                    xy = w[0]
                    area = xy + renpy.image_size(ground)
                    hover = im.MatrixColor(ground,im.matrix.brightness(0.1))
                else:
                    ground = False
                    area = False

                file = ramu.fn_ezy(self.dir +"/hotspot/"+w[3]+"-hover")
                if file:
                    hover = file
                    xy = w[0]
                    if not area: 
                        area = xy + renpy.image_size(hover)
                    if not ground: 
                        ground = im.MatrixColor(hover,im.matrix.brightness(-0.2))

                if hover: himg = himg + ( xy, hover )
                if ground: gimg = gimg + ( xy,ground )
                if area: imgdata.append( [ area, action ] )

            img['ground'] = LiveComposite( (1280,720), *gimg )
            img['hover'] = LiveComposite( (1280,720), *himg )
            img['data'] = imgdata

            return img

label _scene_goto(obj_id=None,d=None,f=None,r=None):
        
    python:
        if r is None: r = ''
        if not obj_id is None: obj = globals()[obj_id]
        
    "is [d] [f] [r]"

label _scene_door(obj_id=None, f=None,r=None):
        
    python:
        if not obj_id is None: obj = globals()[obj_id]
        
    "door [f] [r]"
    return

label _scene_elevator(obj_id=None,f=None,r=None):
    hide screen scene_imagemap
    "elevator"
    return
    
label _scene_lead(obj_id=None,f=None,r=None):

    hide screen scene_imagemap
    
    python:
        if not obj_id is None: obj = globals()[obj_id]
        renpy.scene()
        renpy.show(obj_id + " "+r)        
        map = obj.imagemaping(r, ramu.get_sceneimg())
   
    call screen scene_imagemap(map)

    return
    
    return