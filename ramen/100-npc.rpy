init -99 python:

    class npc(ramen_object):
    
        def load(self,id=None,**kwargs):
            try: self.color 
            except: self.color=ramu.color_random(128,255)
            try: self.wcolor 
            except: self.wcolor= "#ddd"
            try: self.name
            except: self.name = self.id.title()
            try: self.callname
            except: self.callname = self.name
            try: self.lastname
            except: self.lastname = ""
            try: self.gender
            except: self.gender="f"
            try: self.gender
            except: self.gender="f"
            
            setattr(character, self.id.lower(), Character(self.name, who_color=self.color, what_color=self.wcolor, image=self.id) )
            
            self.define_pose()
            
        def set_phonenum(self,fourdig=None):
            if fourdig is None:
                self.phonenum = "555-" + str(ramu.random_int(10,99)) + str(ramu.random_int(10,99))
            else:
                self.phonenum = "555-" + str(fourdig)
                
        def define_pose(self,main=None):

            voids = [ 'profile', 'nsd-call' ]
            
            files = self.files('self.id' + '/pose/') + self.files(self.id+"/") 
            conte = [ 'sprite' ]
            
            self.__dict__[str('pose')] = {}
            
            for f in files:
                p = ramu.fn_info(f)

                if p['path'] in conte:
                    try: 
                        if not p['name'] in voids: self.__dict__[p['path']][str(p['name'])]=str(f)
                    except:
                        self.__dict__[str(p['path'])]={}
                        if not p['name'] in voids: self.__dict__[p['path']][str(p['name'])]=str(f)
                else:
                    if not p['name'] in voids: self.__dict__['pose'][str(p['name'])]=str(f)

            for k in self.pose.keys():
                renpy.image(self.id+ " "+k, self.pose[k])

            if main is None: 
                l = sorted(self.pose.keys())
                renpy.image(self.id, self.pose[l[0]])
            else: 
                renpy.image(self.id, main)
            
            try: self.sprite = sorted(self.sprite)
            except: pass
            
            try: del self._files
            except: pass
                    
        def spriteanim(self, name=None, list=None, tick=(0.25)):
            
            anim = ()
            
            if name is None:
                print self.__class__.__name__+ ": make_sprite  - misssing name"
                return False
                
            if not type(list) == tuple: list = self.sprite.keys()
            
            n = 0
            
            for i in list:
                try: t = tick[n]
                except: t = 0.25
                anim = anim + (self.sprite[i],t)
                n += 1

            renpy.image((self.id, name), Animation( *anim))
            