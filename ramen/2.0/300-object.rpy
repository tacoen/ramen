init -300 python:
    
    class ramen_native(object):
        """
        ramen_native is base class set for ramen ReverTableDict({}) Store.
        
        ``` python
            a = ramen_native('absurd')
        ```
        
        * `a.id` will return `a.__dict__['id']` which are `absurd` 
        * `a.x` is equivalent `a.__dict__['___']['x']`
        * `a.get('x')` will do the same
        * `a('x')` also will do the same
        * `a()` is equivalent `a.__dict__['___']`
        * `a.y=2` will set `a.__dict__['___']['y']` to 2
        
        """
        
        def __init__(self, id=None, obj_type=None):
        
            if id is None:
                id = self.__class__.__name__ + "_" + str(ramen.uid())

            id = raut.safestr(id)
            self.__dict__[str('id')]= str(id)

            if obj_type is None:
                self.__dict__[str('___')]= {}
            else:
                self.__dict__[str('___')]= obj_type

        def set(self, key, value):
            if isinstance(value,(str,unicode)):
                self.__dict__['___'][str(key)] = str(value)
            else:
                self.__dict__['___'][str(key)] = value    
        
        def __setattr__(self,key,value):
            self.set(key, value)
            
        def dict(self,where=None,**kwargs):
            """
            Put keyword arguments into dict
            
            * `player.dict('stat',x=1,y=2)` put the x=1, y=2 into player.stat, so player.stat['x'] = 1 and player.stat['y'] = 2
            * `player.dict(x=3,y=4)` put the x=3, y=4 into player.stat, so player.x = 3 and player.y = 4
            * `player.x` is equivalent to `player.___['x']`
            """
            
            if where is None:
                for k in kwargs:
                    self.set(k,kwargs[k])
            else:
            
                try: 
                        holder = self.__dict__['___'][where]
                except:
                        holder = self.__dict__['___'][str(where)]={}
               
               
                for k in kwargs:
                    value = kwargs[k]
                    if isinstance(value,(str,unicode)):
                        holder[str(k)] = str(value)
                    else:
                        holder[str(k)] = value    
                
        def __call__(self,key=None):
            if key is None:
                return self.__dict__['___']
            else:
                return self.__dict__['___'][key]

        def get(self,key):
            try:
                return self.__dict__[key]
            except BaseException:
                try:
                    return self.__dict__['___'][key]
                except:
                    return None
        
        def __getattr__(self, key):
            return self.get(key)
            
        def __delattr__(self,key):
            try:
                del self.__dict__[key]
            except:
                del self.__dict__['___'][key]    
    
    class ramen2_object(ramen_native):
        
        def __init__(self,id=None, *agrs,**kwargs):
            super(ramen2_object,self).__init__(id,None)
            self.__dict__[str('dir')]= raut.getdir()
            self.load(*agrs,**kwargs)
        
        def load(self,*agrs,**kwargs):
            pass
            
        def setdir(self,dir):
            """Automaticly when ramen_object being init, it will get the 'dir' with `raut.getdir()`, `setdir` allow you to manualy set `dir` it to something else."""
            
            self.__dict__[str('dir')]=str(dir)
            
        def ctype(self,what,type=None):
            """
            Return or set the type of container. if None then its on the object Revetabledict.
            
            ``` python:
                obj.ctype('var','persistent')
            ```
            
            >obj.ctype('var)
            'persistent'
            
            """
            if type is not None:
                
                try: self.__dict__['ct']
                except: self.__dict__['ct'] = {}
                
                self.__dict__['ct'][what]=str(type)
            else:
            
                try: return self.__dict__['ct'][what]
                except: return None
        
        def native(self,what,**kwargs):
            try: self.__dict__[what]
            except: self.__dict__[what]=ramen_native(what)
            self.__dict__[what].dict(**kwargs)
            
        def persistent(self,what,**kwargs):
            try: ramen_pe[self.id]
            except: ramen_pe[str(self.id)]={}
            try: ramen_pe[self.id][what]
            except: ramen_pe[str(self.id)][str(what)]={}
            self.ctype(what,'persistent')
            self.__dict__[what] = ramen_native(what,ramen_pe[self.id][what])
            self.__dict__[what].dict(**kwargs)
            
        def multipersistent(self,what,**kwargs):
            try: ramen_mp.__dict__[self.id]
            except: ramen_mp.__dict__[str(self.id)]={}
            try: ramen_mp.__dict__[self.id][what]
            except: ramen_mp.__dict__[str(self.id)][str(what)]={}
            self.ctype(what,'multipersistent')
            self.__dict__[str(what)] = ramen_native(what,ramen_mp.__dict__[self.id][what])
            self.__dict__[what].dict(**kwargs)


init -200 python:
            
    class player2(ramen2_object):

        def load(self,*args,**kwargs):
            self.dict(**kwargs)
            if RAMEN_DEV: rd.asset.append(self.id)


