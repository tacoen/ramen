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
            
            try: self.stat
            except: self.data('stat',like=3,corrupt=0,desire=0)

            setattr(character, self.id.lower(), Character(self.name, who_color=self.color, what_color=self.wcolor, image=self.id) )

            self.define_byfile()

        def gain(self,what=None,value=1):
        
            def limit(what, ov, value=1):
                
                ov += int(value)
                
                if not what == 'rel': what = 'stat'

                if ov > mc._limit[what][1]:
                    ov = mc._limit[what][1]
                elif ov < mc._limit[what][0]:
                    ov = mc._limit[what][0]

                return ov
            
            if what == 'relation' or what== 'rel':
                what = 'rel'
            
                try: mc.rel[self.id]
                except: mc.rel[self.id]=[0,self.stat]
                
                ov = mc.rel[self.id][0]
                nv = limit(what, ov, value)
                mc.rel[self.id][0] = nv                
                
            else:
            
                if what in self.stat.keys():
                
                    try: self.stat[what]
                    except: self.stat[what]= 0                
                    
                    ov = self.stat[what]
                    nv = limit(what, ov, value)
                    self.stat[what] = nv
                    
                mc.rel[self.id][1] = self.stat        

            if ov > nv:
                return False
            elif ov < nv:
                return True
            else:
                return None
                
        
        def set_phonenum(self,fourdig=None):
            if fourdig is None:
                self.phonenum = "555-" + str(ramu.random_int(10,99)) + str(ramu.random_int(10,99))
            else:
                self.phonenum = "555-" + str(fourdig)

        def define_byfile(self,main=None):

            voids = [ 'profile', 'nsd-chat' ]

            files = self.files('self.id' + '/pose/') + self.files(self.id+"/")
            conte = [ 'sprite' ]

            self.__dict__[str('pose')] = {}

            for f in files:
                p = ramu.fn_info(f)
                
                if p['ext'] == 'json': 
                    try: self.__dict__['json']
                    except: self.__dict__['json'] = {}
                    self.__dict__['json'][str(p['name'])]=f
                
                if p['name'] == 'profile': self.profile_pic = f
                
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
            
        def chat_usingjson(self,key=None,use_pose=True,file=None,pose=None):

            if file is None:
                try:
                    l = sorted(self.json.keys())
                    jfile = self.json[l[0]]            
                except: jfile = False
            else:
                try:
                    jfile = self.json[file]            
                except: jfile = False
            
            if jfile:

                dialogue = ramu.json_file(jfile)

                if key is None:
                    d = ramu.random_of(dialogue.keys())
                else:
                    d = key

                if use_pose:
                    if pose is None:
                        renpy.show(self.id+' '+d)
                    else:
                        renpy.show(self.id+' '+pose)

                npc = True
                who = character.__dict__[self.id]
                
                for line in dialogue[d]:
                    if not npc:
                        if not line == "": character.mc(line)
                        npc = True
                    else:
                        if not line == "": who(line)
                        npc = False

                if use_pose:
                    renpy.hide(self.id)

            else:
            
                if use_pose:
                    character.narator(self.name + " wasn't interested talking with you.")
                else:
                    character.narator(self.name + " not answering your call.")            