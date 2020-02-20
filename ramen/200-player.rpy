init -203 python:

    class player(ramen_object):

        def load(self,id=None,**kwargs):
            self.__dict__['id']=str('player')
            self.__dict__['dir']=str('')

            try:
                globals()['mc_name']=self.name.title()
            except:
                globals()['mc_name']="You"

            self._inventory={}
            self.__dict__['rel']={}

        def newname(self,name,lastname):
            self.name=name.title()
            globals()['mc_name']=self.name
            self.bio['lastname']=lastname

        def set_limit(self, key, value=None):
            """ see: ramu.limit() """
            
            try: self.__dict__[str('limit')]
            except: self.__dict__[str('limit')]={}

            if not value is None:
                if isinstance(value,list):
                    self.__dict__['limit'][str(key)]=value
                    return value
                else:
                    self.__dict__['limit'][str(key)]=[0,value]
                    return [0,value]
            else:
                try: return self.__dict__['limit'][key]
                except: return [0,10]

        def gain(self,what,value=1):

            try: self.__dict__['stat']
            except: self.__dict__[str('stat')]={}
            stat=self.__dict__['stat']
            
            print what
            print type(value)
            
            ov=stat[what]
            nv=ramu.limit(what, ov, value)

            self.__dict__['stat'][what]=nv

            if ov > nv:
                return False
            elif ov < nv:
                return True
            else:
                return None
                
        def pay(self,where,ammount):
            if mc.param[where] > ammount:
                mc.param[where] -= ammount
                return True
            else:
                return False

        def banking(self,ammount=0,where='bank',to='cash'):
            if mc.param[where] > ammount:
                mc.param[where] -= ammount
                mc.param[to] += ammount
                return True
            else:
                return False
                
