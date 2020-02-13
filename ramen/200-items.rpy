init -202 python:

    class item(ramen_object):

        def load (self,id=None,**kwargs):

            for k in kwargs:
                print k
                self.__dict__[k]=kwargs[k]

            if id is None:
                self.__dict__['id'] = self.__class__.__name__ +"_"+str(uuid.uuid4())[:8].lower()
            else:
                self.__dict__['id'] = str(id)

            try: self.dir
            except: self.__dict__['dir'] = str('items')

            try: self.persist
            except: self.__dict__['persist'] = False
            
            try: self.cost
            except: self.__dict__['cost'] = 0

            try: self.count
            except: self.__dict__['count'] = 1
            
            try: self.name
            except: self.__dict__['name'] = self.id.title()

            try: self.desc
            except: self.__dict__['desc'] = self.name

            try: self.effect
            except: self.__dict__['effect'] = None

            if self.persist==True:
                self.count = 1

        def __call__(self):
            return self.__dict__

        def __repr__(self):
            return "item("+self.id+")"

        def icon(self):
            f = ramu.fn_ezy(self.dir +"/"+self.id);
            if f == False:
                return self.dir +"/noicon.png"
            else:
                return f

