init -204 python:

    class rn_obj(object):
        """rn_obj = ramen native object"""

        def __init__(self,default=False,**kwargs):
            self._ = default
            self.set(**kwargs)
            self.load(default,**kwargs)

        def set(self,**kwargs):
            for k in kwargs:
                self.__dict__[k]=kwargs[k]

        def __repr__(self):
            str =  "<" + self.__class__.__name__ +">"
            return str

        def __call__(self):
            return self.__dict__

        def load(self,id=None,**kwargs):
            """chain for child-class"""
            pass

        def __setattr__(self, key,value):
            self.__dict__[str(key).lower()] = value

        def __getattr__(self, key):
            try: return self.__dict__[key]
            except: return self._

    class ramen_object:

        def __init__(self, id=None, **param):

            try: self.param
            except: self.__dict__[str('param')] = {}

            inf = renpy.get_filename_line()
            dir, fn = ntpath.split(inf[0])
            f,e = fn.split('.')

            if dir == 'renpy/common': dir = '';
            self.__dict__[str('dir')] = str(dir.replace('game/',""))

            if id is None:
                self.__dict__[str('id')] = str(f.replace(" ","").replace("-","").lower())
                self.__dict__[str('id')] = str(uuid.uuid4())[:8].lower()
            else:
                self.__dict__[str('id')] = str(id.replace(" ","").replace("-","").lower())

            for key in param:
                if key.startswith("_"):
                    self.__dict__[key]= param[key]
                else:
                    self.__dict__[str('param')][str(key)] = param[key]

            self.load(id, **param)

        def load(self,id=None,**kwargs):
            """chain for child-class"""
            pass

        def __setattr__(self, key, value):
            if key.startswith("_"):
                self.__dict__[str(key)]=value
            else:
                try: self.__dict__['param']
                except: self.__dict__[str('param')] = {}
                self.__dict__['param'][str(key)] = value

        def __repr__(self):
            str =  self.__class__.__name__ + " is ramen_object"
            return str

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
                        value = getattr( getattr( character, self.id ), key )
                        if key != 'name': return value
                        # substitute the name (for interpolation/translations)
                        return renpy.substitutions.substitute(value)[0]
                    except:
                        pass
            try:
                return super(object, self).__getattr__(key)
            except:
                return super(object, self).__getattribute__(key)

        def ui_set(self, noparam=False, **kwargs):

            self.__dict__['ui'] = rn_obj(0)
            
            try: bucket.__dict__[self.id]
            except: bucket.__dict__[self.id] = {}
            
            for k in kwargs:
                instyle = self.makestyle(k,kwargs[k])
                setattr(self.__dict__['ui'],k,kwargs[k])
                
            if noparam: self.__dict__['param'] = {}

        def makestyle(self, key, val):

            try: style[self.id]
            except: style[self.id] = Style(style.default)

            ins = False

            def makestyle_hbar(key,val):

                for t in val.keys():
                    try: bcolor = val[t]
                    except: bcolor = ramen.random_colour(128,255)

                    style[self.id][key][t].thumb = bcolor
                    style[self.id][key][t].right_bar=bcolor+"5"
                    style[self.id][key][t].left_bar=bcolor+"D"
                    style[self.id][key][t].ysize = 16

                return True
                
            def makestyle_area(key,val):
                for t in val.keys():

                    try: style[self.id][key][t].xpos = val[t][0]
                    except: style[self.id][key][t].xpos = 0
                    try: style[self.id][key][t].ypos = val[t][1]
                    except: style[self.id][key][t].ypos = 0
                    try: style[self.id][key][t].xsize = val[t][2]
                    except: style[self.id][key][t].xsize = config.screen_width
                    try: style[self.id][key][t].ysize = val[t][3]
                    except: style[self.id][key][t].ysize = config.screen_height
                    try: style[self.id][key][t].padding = val[t][4]
                    except: style[self.id][key][t].padding = (0,0,0,0)
                    
                return True

            if key=='hbar':
                ins = makestyle_hbar(key,val)
            if key=='area': 
                ins = makestyle_area(key,val)

            
        def set_ui_old(self,**kwargs):
            """set object as ui object"""

            try: self.__dict__['ui']
            except: self.__dict__[str('ui')] = object()
            ui = self.__dict__['ui']
            for k in kwargs:
                setattr(ui,k,kwargs[k])

                if k == 'bars':
                    try: style.hbar
                    except: style.hbar = Style(style.default)

                    for t in kwargs['bars'].keys():
                        try: bcolor = kwargs['bars'][t]
                        except: bcolor = ramen.random_colour(128,255)
                        style.hbar[t].thumb = bcolor
                        style.hbar[t].right_bar= Color(bcolor).shade(.9)
                        style.hbar[t].left_bar= Color(bcolor).opacity(.5)

        def data(self,key,**kwargs):
            """set object as data container"""

            try: self.__dict__[str(key.lower())]
            except: self.__dict__[str(key.lower())] = {}

            for k in kwargs:
                self.__dict__[str(key.lower())][str(k)] = kwargs[k]

        def default(self,key,default,param=True):
            if param:
                self.__dict__['param'][str(key)] = default
            else:
                self.__dict__[str(key)] = default

        def files(self,key=None,scope=None):
            """set object as files container"""

            try: self._files
            except: self.__dict__['_files'] = []
            F = renpy.list_files(False)
            res = []

            def collect():
                for f in F:
                    if self.dir+"/" in f: self.__dict__['_files'].append(f)

            if key is None:

                collect()

                return self._files

            else:
                if self._files ==[]: collect()

                for f in self._files:
                    if key in f:
                        if not scope is None:
                            if scope in f: res.append(f)
                        else:
                            res.append(f)
                return res
