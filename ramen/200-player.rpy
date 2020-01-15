init -203 python:

    class player(ramen_object):

        def load(self,id=None,**kwargs):
            self.__dict__['id'] = str('player')
            self.__dict__['dir'] = str('')
            try: globals()['mc_name'] = self.name.title()
            except: globals()['mc_name'] = "You"

        def newname(self,name):
            self.name = name.title()
            globals()['mc_name'] = self.name 
            
        def limit(self, key, value=None):
            
            try: self._limit
            except: self.__dict__['_limit'] = {}
            
            if not value is None:
                if isinstance(value,list):
                    self.__dict__['_limit'][key] = value
                    return value
                else:
                    self.__dict__['_limit'][key] = [0,value]
                    return [0,value]
            else:
                try: return self.__dict__['_limit'][key]
                except: return [0,10]



    