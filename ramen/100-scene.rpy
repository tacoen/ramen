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
            
                print fn

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
            
            try: ways = self.maze['way'][floor]
            except: print "object maze-way not here!"

            def makeaction(w):
                
                c = ''
                w1=None
                w2=None
                
                if isinstance(w,list):
                    c = w[0]
                    try: 
                        c += '_'+w[1]
                        w1=w[1]
                    except: pass
                    try:
                        c += '_'+w[2]
                        w2 = w[2]
                    except: pass
                else:
                    c = w
                    
                if renpy.has_label(c):
                    return c
                else:
                    return Call("mapfunc_"+w[0],obj=self.id,f=w1,d=w2)

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

                if hover: himg = himg + ( xy, hover )
                if ground: gimg = gimg + ( xy,ground )

                imgdata.append( [ area, action ] )

            img['ground'] = LiveComposite( (1280,720), *gimg )
            img['hover'] = LiveComposite( (1280,720), *himg )
            img['data'] = imgdata

            return img
            