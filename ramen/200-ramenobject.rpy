init -204 python:

    class container():

        def __setattr__(self, key, value):
            _ramen_container.__dict__[key] = value

        def __getattr__(self, key):
            try:
                return _ramen_container.__dict__[key]
            except BaseException:
                return None

        def __call__(self):
            return _ramen_container.__dict__

        def __repr__(self):
            return repr(type(_ramen_container))

        def data(self, what, **kwargs):
            try:
                _ramen_container.__dict__[what]
            except BaseException:
                _ramen_container.__dict__[str(what)] = {}
            for k in kwargs:
                _ramen_container.__dict__[what][k] = kwargs[k]

    class rn_obj(object):
        """rn_obj=ramen native object"""

        def __init__(self, default=False, **kwargs):
            self._ = default
            self.set(**kwargs)
            self.load(default, **kwargs)

        def set(self, **kwargs):
            for k in kwargs:
                self.__dict__[k] = kwargs[k]

        def __repr__(self):
            str = "<" + self.__class__.__name__ + ">"
            return str

        def __call__(self):
            return self.__dict__

        def load(self, id=None, **kwargs):
            """chain for child-class"""
            pass

        def __setattr__(self, key, value):
            self.__dict__[str(key).lower()] = value

        def __getattr__(self, key):
            try:
                return self.__dict__[key]
            except BaseException:
                return self._

    class ramen_object:

        def __init__(self, id=None, **param):

            try:
                self.param
            except BaseException:
                self.__dict__[str('param')] = {}

            inf = renpy.get_filename_line()
            dir, fn = ntpath.split(inf[0])
            f, e = fn.split('.')

            if dir == 'renpy/common':
                dir = ''

            #self.__dict__[str('dirs')]= [ str(dir.replace('game/',"")) ]

            self.dir = str(dir.replace('game/', ""))

            if id is None:
                self.__dict__[
                    str('id')] = str(
                    f.replace(
                        " ",
                        "").replace(
                        "-",
                        "").lower())
                self.__dict__[str('id')] = str(uuid.uuid4())[:8].lower()
            else:
                self.__dict__[
                    str('id')] = str(
                    id.replace(
                        " ",
                        "").replace(
                        "-",
                        "").lower())

            for key in param:
                if key.startswith("_"):
                    self.__dict__[key] = param[key]
                else:
                    self.__dict__[str('param')][str(key)] = param[key]

            self.load(id, **param)

        def load(self, id=None, **kwargs):
            """chain for child-class"""
            pass

        def __setattr__(self, key, value):
            if key.startswith("_"):
                self.__dict__[str(key)] = value
            else:
                try:
                    self.__dict__['param']
                except BaseException:
                    self.__dict__[str('param')] = {}
                self.__dict__['param'][str(key)] = value

        def __repr__(self):
            return str('id=' + self.id)

        def __call__(self):
            return self.__dict__

        def __getattr__(self, key):

            try:
                return self.__dict__['param'][key]
            except BaseException:
                if key in self.__dict__:
                    return self.__dict__[key]
                else:
                    try:
                        # try the character object
                        value = getattr(getattr(character, self.id), key)
                        if key != 'name':
                            return value
                        # substitute the name (for interpolation/translations)
                        return renpy.substitutions.substitute(value)[0]
                    except BaseException:
                        pass
            try:
                return super(object, self).__getattr__(key)
            except BaseException:
                return super(object, self).__getattribute__(key)

        def ui_set(self, noparam=False, **kwargs):

            self.__dict__['ui'] = rn_obj(0)

            for k in kwargs:
                instyle = self.makestyle(k, kwargs[k])
                setattr(self.__dict__['ui'], k, kwargs[k])

            if noparam:
                self.__dict__['param'] = {}

        def makestyle_hbar(self, key, val):

            for t in val.keys():

                try:
                    bcolor = val[t]
                except BaseException:
                    bcolor = [ramu.random_colour(128, 255), 16]

                if not isinstance(val[t], list):
                    bcolor = [val[t], 16]

                try:
                    bcolor[1]
                except BaseException:
                    bcolor[1] = 16

                style[self.id][key][t].thumb = bcolor[0]
                style[self.id][key][t].right_bar = Color(bcolor[0]).opacity(.5)
                style[self.id][key][t].left_bar = Color(bcolor[0]).opacity(.8)
                style[self.id][key][t].ysize = bcolor[1]

            return True

        def makestyle_area(self, key, val):
            for t in val.keys():

                try:
                    style[self.id][key][t].xpos = val[t][0]
                except BaseException:
                    style[self.id][key][t].xpos = 0
                try:
                    style[self.id][key][t].ypos = val[t][1]
                except BaseException:
                    style[self.id][key][t].ypos = 0
                try:
                    style[self.id][key][t].xsize = val[t][2]
                except BaseException:
                    style[self.id][key][t].xsize = config.screen_width
                try:
                    style[self.id][key][t].ysize = val[t][3]
                except BaseException:
                    style[self.id][key][t].ysize = config.screen_height
                try:
                    style[self.id][key][t].padding = val[t][4]
                except BaseException:
                    style[self.id][key][t].padding = (0, 0, 0, 0)

            return True

        def makestyle(self, key, val):

            try:
                style[self.id]
            except BaseException:
                style[self.id] = Style(style.default)

            ins = False

            if key == 'hbar':
                ins = self.makestyle_hbar(key, val)
            if key == 'area':
                ins = self.makestyle_area(key, val)

        def data(self, key, **kwargs):
            """set object as data container"""

            try:
                self.__dict__[str(key.lower())]
            except BaseException:
                self.__dict__[str(key.lower())] = {}

            for k in kwargs:
                self.__dict__[str(key.lower())][str(k)] = kwargs[k]

        def default(self, key, default, param=True):
            if param:
                self.__dict__['param'][str(key)] = default
            else:
                self.__dict__[str(key)] = default

        def files(self, key=None, scope=None):
            """set object as files container"""

            files = []
            res = []

            if isinstance(self.dir, list):
                dirs = self.dir
            else:
                dirs = [self.dir]

            F = sorted(renpy.list_files(False))

            if key is None:
                key = ''

            for d in dirs:
                files += filter(lambda w: d + "/" + key in w, F)

            if scope is not None:
                res = filter(lambda w: scope in w, files)
                return res
            else:
                return files

        def gallery(self,what,where=''):
            try:
                self.__dict__[what]
            except BaseException:
                self.__dict__[str(what)] = {}

            res = {}
            inf = renpy.get_filename_line()
            cf = inf[0].replace('game/', '')
            d=[]
            
            for f in sorted(self.files(where)):
                fn = ramu.fn_info(f)
                dirs = fn['dir'].replace(self.dir+'/','')
                
                if dirs == self.dir:
                    dirs = None
                
                if dirs is not None: d.append(dirs)
            
            for dirs in list(d):
                dc = self.__dict__[str(what)]
                for x in dirs.split('/'):
                    dc = dc.setdefault(x, {})

            n=0

            for f in sorted(self.files(where)):
                fn = ramu.fn_info(f)
                dirs = f.replace(self.dir+"/",'')

                d = dirs.split('/')
                
                s = str(n)
                
                if len(d)==2:
                    self.__dict__[str(what)][d[0]][s]=f
                elif len(d)==3:
                    self.__dict__[str(what)][d[0]][d[1]][s]=f
                
                n += 1
                
                
        
        def index(self, what, where=None, ext='rpy'):

            try:
                self.__dict__[what]
            except BaseException:
                self.__dict__[str(what)] = {}

            res = {}
            inf = renpy.get_filename_line()
            cf = inf[0].replace('game/', '')

            for f in sorted(self.files(where)):
                if not f == cf and f.endswith(ext):
                    fn = ramu.fn_info(f)
                    res[fn['name']] = {}

            self.__dict__[str(what)] = res

        def index_update(self, what='apps', **kwargs):

            inf = renpy.get_filename_line()
            i = ramu.fn_info(inf[0])
            apps = i['name']
            i['dir'] = i['dir'].replace('game/', '')

            try:
                self.__dict__[what]
            except BaseException:
                self.__dict__[str(what)] = {}

            try:
                self.__dict__[what][apps]
            except BaseException:
                self.__dict__[str(what)][apps] = {}

            self.__dict__[str(what)][apps]['dir'] = i['dir']

            if ramu.fn_ezy(i['dir'] + "/icon"):
                self.__dict__[
                    str(what)][apps]['icon'] = ramu.fn_ezy(
                    i['dir'] + "/icon")

            for k in kwargs:
                self.__dict__[str(what)][apps][k] = kwargs[k]

            try:
                self.__dict__[str(what)][apps]['bgr']
            except BaseException:
                self.__dict__[str(what)][apps]['bgr'] = "#ffffff"

        def get_dir(self, p=0):

            if isinstance(self.dir, (unicode, str)):
                return self.dir
            else:
                return self.dir[p]
