init -204 python:

    class ramen_object:
    
        def __init__(self, id=None, **param):
            
            try: self.param
            except: self.__dict__['param'] = {}
            
            inf = renpy.get_filename_line()
            dir, fn = ntpath.split(inf[0])
            f,e = fn.split('.')
            
            if id is None:
                self.__dict__['id'] = str(f.replace(" ","").lower())
            else:
                self.__dict__['id'] = str(id.replace(" ","").replace("-","").lower())
            
            self.__dict__['dir'] = str(dir.replace('game/',""))
            
            for key in param:
                if key.startswith("_"):
                    self.__dict__[key]= param[key]
                else:
                    self.__dict__['param'][key] = param[key]

            self.load()

        def load(self,id=None,**kwargs):
            pass
            
        def ui(self,**kwargs):
            try: self.ui
            except: self.__dict__['ui'] = {}
            for k in kwargs:
                self.__dict__['ui'][k] = kwargs[k]
            
        def __setattr__(self, key, value):
            if key.startswith("_"):
                self.__dict__[key]=value
            else:
                try: self.__dict__['param']
                except: self.__dict__['param'] = {}
                self.__dict__['param'][key] = value

        def __repr__(self):
            return "It's ramen object"
            
        def __call__(self):
            return self.__dict__

        def __getattr__(self, key):

            try: 
                return self.__dict__['param'][key]
            except:
                if key in self.__dict__:
                    return self.__dict__[key]
                else:
                    try:
                        # try the character object
                        value = getattr( getattr( character, self._id ), key )
                        if key != 'name': return value
                        # substitute the name (for interpolation/translations)
                        return renpy.substitutions.substitute(value)[0]
                    except:
                        pass
            try:
                return super(object, self).__getattr__(key)
            except:
                return super(object, self).__getattribute__(key)

