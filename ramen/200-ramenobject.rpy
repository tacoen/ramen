init -204 python:

    class container():

        def __setattr__(self, key,value):
            _ramen_container.__dict__[key]=value

        def __getattr__(self, key):
            try : return _ramen_container.__dict__[key]
            except: return None
        
        def __call__(self):
            return _ramen_container.__dict__            

        def __repr__(self):
            return repr(type(_ramen_container))
            
        def data(self, what, **kwargs):
            try: _ramen_container.__dict__[what]
            except: _ramen_container.__dict__[str(what)]={}
            for k in kwargs:
                _ramen_container.__dict__[what][k]=kwargs[k]
            
            

    class rn_obj(object):
        """rn_obj=ramen native object"""

        def __init__(self,default=False,**kwargs):
            self._=default
            self.set(**kwargs)
            self.load(default,**kwargs)

        def set(self,**kwargs):
            for k in kwargs:
                self.__dict__[k]=kwargs[k]

        def __repr__(self):
            str= "<" + self.__class__.__name__ +">"
            return str

        def __call__(self):
            return self.__dict__

        def load(self,id=None,**kwargs):
            """chain for child-class"""
            pass

        def __setattr__(self, key,value):
            self.__dict__[str(key).lower()]=value

        def __getattr__(self, key):
            try: return self.__dict__[key]
            except: return self._

    class ramen_object:

        def __init__(self, id=None, **param):

            try: self.param
            except: self.__dict__[str('param')]={}

            inf=renpy.get_filename_line()
            dir, fn=ntpath.split(inf[0])
            f,e=fn.split('.')

            if dir == 'renpy/common': dir='';
            self.__dict__[str('dir')]=str(dir.replace('game/',""))

            if id is None:
                self.__dict__[str('id')]=str(f.replace(" ","").replace("-","").lower())
                self.__dict__[str('id')]=str(uuid.uuid4())[:8].lower()
            else:
                self.__dict__[str('id')]=str(id.replace(" ","").replace("-","").lower())

            for key in param:
                if key.startswith("_"):
                    self.__dict__[key]= param[key]
                else:
                    self.__dict__[str('param')][str(key)]=param[key]

            self.load(id, **param)

        def load(self,id=None,**kwargs):
            """chain for child-class"""
            pass

        def __setattr__(self, key, value):
            if key.startswith("_"):
                self.__dict__[str(key)]=value
            else:
                try: self.__dict__['param']
                except: self.__dict__[str('param')]={}
                self.__dict__['param'][str(key)]=value

        def __repr__(self):
            return str(self.id)

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
                        value=getattr( getattr( character, self.id ), key )
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

            self.__dict__['ui']=rn_obj(0)
            
            for k in kwargs:
                instyle=self.makestyle(k,kwargs[k])
                setattr(self.__dict__['ui'],k,kwargs[k])
                
            if noparam: self.__dict__['param']={}

        def makestyle_hbar(self, key, val):

                for t in val.keys():
                
                    try: bcolor = val[t]
                    except: bcolor = [ ramu.random_colour(128,255), 16 ]
                    
                    if not isinstance(val[t],list): bcolor = [ val[t], 16 ]
                    
                    try: bcolor[1]
                    except: bcolor[1]=16

                    style[self.id][key][t].thumb=bcolor[0]
                    style[self.id][key][t].right_bar=Color(bcolor[0]).opacity(.5)
                    style[self.id][key][t].left_bar=Color(bcolor[0]).opacity(.8)
                    style[self.id][key][t].ysize=bcolor[1]

                return True
                
        def makestyle_area(self, key,val):
                for t in val.keys():

                    try: style[self.id][key][t].xpos=val[t][0]
                    except: style[self.id][key][t].xpos=0
                    try: style[self.id][key][t].ypos=val[t][1]
                    except: style[self.id][key][t].ypos=0
                    try: style[self.id][key][t].xsize=val[t][2]
                    except: style[self.id][key][t].xsize=config.screen_width
                    try: style[self.id][key][t].ysize=val[t][3]
                    except: style[self.id][key][t].ysize=config.screen_height
                    try: style[self.id][key][t].padding=val[t][4]
                    except: style[self.id][key][t].padding=(0,0,0,0)
                    
                return True

        def makestyle(self, key, val):

            try: style[self.id]
            except: style[self.id]=Style(style.default)

            ins=False

            if key=='hbar':
                ins=self.makestyle_hbar(key,val)
            if key=='area': 
                ins=self.makestyle_area(key,val)

        def data(self,key,**kwargs):
            """set object as data container"""

            try: self.__dict__[str(key.lower())]
            except: self.__dict__[str(key.lower())]={}

            for k in kwargs:
                self.__dict__[str(key.lower())][str(k)]=kwargs[k]

        def default(self,key,default,param=True):
            if param:
                self.__dict__['param'][str(key)]=default
            else:
                self.__dict__[str(key)]=default

        def files(self,key=None,scope=None):
            """set object as files container"""

            try: self._files
            except: self.__dict__['_files']=[]
            F=renpy.list_files(False)
            res=[]

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
                
        def index(self,what,ext):
            
            try: self.__dict__[what]
            except: self.__dict__[str(what)]={}
            
            res = {}
            inf=renpy.get_filename_line()
            cf =inf[0].replace('game/','')
            
            for f in sorted(self.files()):
                if not f==cf and f.endswith(ext):
                    fn = ramu.fn_info(f)
                    res[fn['name']] = {}
            
            self.__dict__[str(what)] = res
            
        def index_update(self,what='apps',**kwargs):

            inf=renpy.get_filename_line()
            i = ramu.fn_info(inf[0])
            apps = i['name']
            i['dir']=i['dir'].replace('game/','')

            try: self.__dict__[what]
            except: self.__dict__[str(what)]={}

            try: self.__dict__[what][apps]
            except: self.__dict__[str(what)][apps]={}

            self.__dict__[str(what)][apps]['dir'] = i['dir']
            
            if ramu.fn_ezy(i['dir']+"/icon"):
                self.__dict__[str(what)][apps]['icon'] = ramu.fn_ezy(i['dir']+"/icon")

            for k in kwargs:
                self.__dict__[str(what)][apps][k] = kwargs[k]

            try: self.__dict__[str(what)][apps]['bgr']
            except: self.__dict__[str(what)][apps]['bgr'] = "#ffffff"
                
                
