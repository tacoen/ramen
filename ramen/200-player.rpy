init -203 python:

    class player(ramen_object):

        def load(self,id=None,**kwargs):
            self.__dict__['id'] = str('player')
            self.__dict__['dir'] = str('')

            try:
                globals()['mc_name'] = self.name.title()
            except:
                globals()['mc_name'] = "You"

            self._inventory = {}

        def newname(self,name,lastname):
            self.name = name.title()
            globals()['mc_name'] = self.name
            self.bio['lastname'] = lastname

        def limit(self, key, value=None):

            try: self._limit
            except: self.__dict__[str('_limit')] = {}

            if not value is None:
                if isinstance(value,list):
                    self.__dict__['_limit'][str(key)] = value
                    return value
                else:
                    self.__dict__['_limit'][str(key)] = [0,value]
                    return [0,value]
            else:
                try: return self.__dict__['_limit'][key]
                except: return [0,10]

        def adv(self,what,**kwargs):

            try: self.__dict__[what]
            except: self.__dict__[str(what)]={}

            def mod_int(what,key,value):
                ov = 0
                bells = 0
                try:
                    ov = self.__dict__[what][str(key)]
                    self.__dict__[what][str(key)] += value
                except:
                    self.__dict__[what][str(key)] = 0

                try:
                    if self.__dict__[what][str(key)] < self._limit[what][0]:
                        self.__dict__[what][str(key)] = self._limit[what][0]

                    if self.__dict__[what][str(key)] > self._limit[what][1]:
                        self.__dict__[what][str(key)] = self._limit[what][1]

                except: pass

                if self.__dict__[what][str(key)] > ov: bells = 1
                if self.__dict__[what][str(key)] < ov: bells = -1

                return bells

            def mod_list(what,key,va):
                n = len(va)
                ov = []
                bells = []
                for x in range(0, n):
                    ov.append(0)
                    bells.append(0)

                for x in range(0, n):
                    try:
                        ov[x] = self.__dict__[what][str(key)][x]
                        self.__dict__[what][str(key)][x] += va[x]
                    except:
                        self.__dict__[what][str(k)][x] = va[x]

                for x in range(0, n):
                    try:
                        if self.__dict__[what][str(key)][x] < self._limit[what][0]:
                            self.__dict__[what][str(key)][x] = self._limit[what][0]
                        if self.__dict__[what][str(key)][x] > self._limit[what][1]:
                            self.__dict__[what][str(key)][x] = self._limit[what][1]

                    except: pass

                    if ov[x] > self.__dict__[what][str(key)][x]: bells[x]= -1
                    if ov[x] < self.__dict__[what][str(key)][x]: bells[x]= 1

                return bells

            for k in kwargs:

                is_list = False
                res = 0

                try:
                    if isinstance(self.__dict__[what][k],list): is_list=True
                except:
                    pass

                if is_list:
                    if isinstance(kwargs[k],list):
                        res = mod_list(what,k,kwargs[k])
                    else:
                        res = mod_list(what,k,[kwargs[k]])
                else:
                    if isinstance(kwargs[k],list):
                        res = mod_int(what,k,kwargs[k][0])
                    else:
                        res = mod_int(what,k,kwargs[k])

            r = 0

            if isinstance(res,list):
                n = len(res)
                r = 0
                for x in range(0,n):
                    r += res[x]
                else:
                    r = res

            if r >= 1: return True
            if r < 0: return False
            if r == 0: return None

