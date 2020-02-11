init -202 python:

    class item(object):

        def __init__(self,id=None,**kwargs):

            self.dir = str('items')
            self.count=1
            self.persist=False
            self.cost=None
            self.effect=None
            self.desc='No Descriptions'
            self.name= None
            
            for k in kwargs:
                self.__dict__[k]=kwargs[k]

            if self.persist==True:
                self.count = 1

            if id is None:
                self.id = self.__class__.__name__
            else:
                self.id = str(id)

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

    def create_items(inventory, where, prefix, **kwargs ):
        # Great for shops items
        files = ramu.fn_files(where,prefix)
        for f in files:
            fn = ramu.fn_info(f)
            i = item( id= fn['name'], desc=ramu.nicenaming(prefix,fn['name']))
        
            for k in kwargs.keys():
                i.__dict__[k] = kwargs[k]
                if k == 'cost':
                
                    try: kwargs[k][0]
                    except: kwargs[k][0]=10
                    try: kwargs[k][1]
                    except: kwargs[k][1]=20
                    
                    i.__dict__['cost'] = ramu.random_int(kwargs[k][0],kwargs[k][1])
                    i.__dict__['dir'] = str(where)

            inventory.add(i)
