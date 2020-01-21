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
            
            try: self.maze
            except: self.maze = {}
            
            for k in kwargs:
                self.maze[k] = kwargs[k]
                
            def next_floor(f,w='up'):
                if w == 'up':
                    u = self.maze['floor'].index(f)+1
                else:
                    u = self.maze['floor'].index(f)-1
                
                
                if u >= len(self.maze['floor']) or u < 0:
                    res = None
                else:
                    res = self.maze['floor'][u]

                return res
                    
            self.map = {}
    
            for f in sorted(self.maze['floor']):

                up = next_floor(f,'up')
                down = next_floor(f,'down')
                
                self.map[f] = {}

                for i in sorted(self.maze['hs'].keys()):
                    self.map[f][i]=[]

                    try:
                        func = self.maze['hs'][i][2]
                        if "up" in i: self.map[f][i]=[func, up]
                        elif "down" in i: self.map[f][i]=[func, down]
                        else: self.map[f][i]=[func, f]
                    except:
                        self.map[f][i] = ['door',f,i]
                
        def scene_call(self,what,obj_id,var):
            try: d = var[0]
            except: d = None
            try: r = var[2]
            except: r = None
            try: f = var[1]
            except: f = None
            
            renpy.call_in_new_context(what,obj_id=obj_id, d=d, f=f, r=r)
            
        def imagemaping(self,floor,bgr=None):

            if bgr is None:
                bgr = self.get_sceneimg()
                
            img = {}
            img['ground'] = bgr
            gimg = tuple()
            himg = tuple()
            imgdata=[]
            gimg = ( (0,0), bgr )
            himg = ( (0,0), Solid('#fff0'))
            
            ways = self.map[floor]

            def makeaction(w):
            
                try: 
                    if w[1] == None or w[2] == None:
                        return Null
                except: pass
                
                if renpy.has_label(w[0]):
                   return Function(self.scene_call, what =w[0], obj_id=self.id, var=w )
                if renpy.has_label("_scene_"+w[0]):
                   return Function(self.scene_call, what ="_scene_"+w[0], obj_id=self.id, var=w )

                #return Call("_scenemap",obj_id=self.id,d=w0,f=w1,r=w2)
                return Function(self.scene_call,what='_scene_goto', obj_id=self.id, var=w)

            for w in sorted(ways.keys()):
            
                action = makeaction(ways[w])
                
                file = ramu.fn_ezy(self.dir +"/hotspot/"+w)
                if file and renpy.loadable(file):
                    ground = file
                    xy = (self.maze['hs'][w][0],self.maze['hs'][w][1]) 
                    area = xy + renpy.image_size(ground)
                else:
                    ground = False

                hover = (Solid('#fff9'))

                file = ramu.fn_ezy(self.dir +"/hotspot/"+w+"-hover")
                
                if file and renpy.loadable(file):
                    hover = file
                    xy = (self.maze['hs'][w][0],self.maze['hs'][w][1]) 
                    area = xy + renpy.image_size(hover)
                else:
                    if ground:
                        hover = im.MatrixColor(ground,im.matrix.brightness(0.1))
                    else:
                        hover = (Solid('#fff9'))

                if not action is "Null":
                    if hover: himg = himg + ( xy, hover )
                    if ground: gimg = gimg + ( xy,ground )
                    imgdata.append( [ area, action ] )

            img['ground'] = LiveComposite( (1280,720), *gimg )
            img['hover'] = LiveComposite( (1280,720), *himg )
            img['data'] = imgdata

            return img

label _scene_goto(obj_id=None,d=None,f=None,r=None):
        
        
    python:
        if r is None: r = ''
        if not obj_id is None: obj = globals()[obj_id]
        
    "is [d] [f] [r]"

label door(obj_id=None,d=None,f=None,r=None):
        
    python:
        if not obj_id is None: obj = globals()[obj_id]
        
    "door [f] [r] [d]"


label _scene_lead(obj_id=None,d=None,f=None,r=None):

    hide screen scene_imagemap
    
    python:
        if not obj_id is None: obj = globals()[obj_id]
        map = obj.imagemaping(f, ramu.get_sceneimg())
        renpy.scene()
        renpy.show(obj_id + " "+f)        
   
    call screen scene_imagemap(map)

    "lead f"
    
    return