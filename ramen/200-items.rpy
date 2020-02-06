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

    class inventory(object):

        def __init__(self,store,max=24):

            try: mc
            except:
                print "*** Mising mc=player() ***"
                return false

            try: mc._inventory[store]
            except: mc._inventory[str(store)] = {}
            self.id = str(store)
            self.container = mc._inventory[self.id]
            self.max = int(max)

        def __repr__(self):
            return self.__class__.__name__

        def __call__(self):
            return self.container

        def transfer(self,item_id,store='storage'):

            try: target = globals()[store]
            except: return False

            try: item = self.container[item_id]
            except: return False

            if "inventory" in str(type(target)):
                target.add(item)
                self.drop(item_id)
            else:
                self.drop(item_id)

            return True

        def add(self,item):
            i = copy.copy(item)
            try:
                s = self.container[i.__dict__['id']]
                for k in s.__dict__.keys():
                    if k == 'count': s.__dict__[k] += i.__dict__[k]
                    else: s.__dict__[k] = i.__dict__[k]
            except:
                self.container[i.__dict__['id']] = i

            mc._inventory[self.id] = self.container
            return True

        def drop(self,item_id):
            self.container.pop(item_id)

        def use(self, item_id, who=None):

            res = True

            try: item = self.container[item_id]
            except: return False

            if not item.effect is None:

                eff = item.effect

                if isinstance(eff,list):
                    if eff[0] == 'stat':

                        ov = mc.stat[eff[1]]
                        mc.stat[eff[1]] += eff[2]

                        if mc.stat[eff[1]] > mc._limits['stat'][1]: mc.stat[eff[1]] = mc._limits['stat'][1]
                        if mc.stat[eff[1]] < mc._limits['stat'][0]: mc.stat[eff[1]] = mc._limits['stat'][0]

                        if ov < mc.stat[eff[1]]: res = False
                        else: res = True

                    if eff[0] == 'rel':
                        res = False
                        if who in mc.rel.keys():
                            if isinstance(eff[1],list):
                                for x in range(0,len(mc.rel[who])):
                                    try:
                                        mc.rel[who][x] += eff[1][x]
                                        res = True
                                    except: mc.rel[who][x] += 0
                            else:
                                mc.rel[who][0] += eff[1]
                                res = True
                        else:
                            res = False

            if item.persist == False:
                item.count -= 1
                if item.count <= 0:
                    self.drop(item_id)

            return res
