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

        def __init__(self,store,max=24):
        
            try: mc
            except:
                print "*** Mising mc=player() ***"
                return false
                
            try: mc._inventory[store]
            except: mc._inventory[str(store)] = {}
            self.container = mc._inventory[str(store)]
            self.max = int(max)

        def __call__(self):
            return self.container

        def add(self,item):
            i = item.__dict__.copy()
            try: 
                s = self.container[i['id']]
                for k in s.keys(): 
                    if k == 'count': s[k] += i[k]
                    else: s[k] = i[k]
            except:    
                self.container[i['id']] = copy.copy(item)

        def drop(self,item,id=True):
            if id==False: item = globals()[item].id
            self.container.pop(item)
            
        def use(self, item, who=None, id=True):
        
            try: self.container[item]
            except: return False

            if not self.container[item]['effect'] is None:
            
                eff = self.container[item]['effect']
            
                if isinstance(eff,list):
                    if eff[0] == 'stat':
                        mc.stat[eff[0]][eff[1]] = eff[2]
                    if eff[0] == 'rel':
                        if isinstance(eff[1],list):
                            mc.stat[eff[0]][who] = eff[1]
                        else:
                            mc.stat[eff[0]][who] = [eff[1],0,0]

            if self.container[item]['persist'] == False:
            
                if id==False: item = globals()[item].id

                self.container[item]['count'] -= 1
                
                if self.container[item]['count'] <= 0:
                    self.drop(item,id)
                
            
