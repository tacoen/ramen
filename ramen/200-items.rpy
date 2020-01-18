init -202 python:

    class item(object):
    
        def __init__(self,id=None,**kwargs):
        
            self.dir = str('items')
            self.value=5
            self.count=1
            self.persist=False
            self.cost=None
            self.effect=None
            self.desc='Items'
            if id is None:
                self.id = self.__class__.__name__
            else:
                self.id = str(id)
        
        def __call__(self):
            return self.__dict__

        def __repr__(self):
            return self.id


    class inventory(object):
    
        def __init__(self,store):
            try: mc._inventory[store]
            except: mc._inventory[str(store)] = []
            
            self.container = mc._inventory[str(store)]

        def add(self,item):
        
            self.container.append(item)
            
            
            
            