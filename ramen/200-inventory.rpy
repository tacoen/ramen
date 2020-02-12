init -201 python:

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

                        if mc.stat[eff[1]] > mc.limits['stat'][1]: mc.stat[eff[1]] = mc.limits['stat'][1]
                        if mc.stat[eff[1]] < mc.limits['stat'][0]: mc.stat[eff[1]] = mc.limits['stat'][0]

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


    class shop(rn_obj):

        def load(self,default=False,**kwargs):
            self.__dict__['container']={}

            try: bucket.__dict__[self.id]
            except: bucket.__dict__[self.id]= []

        def bucket_clear(self):
            bucket.__dict__[self.id]=[]

        def bucket(self,what,add=True):
            if add:
                bucket.__dict__[self.id].append(what)
            else:
                n = bucket.__dict__[self.id].index(what)
                bucket.__dict__[self.id].pop(n)

        def in_bucket(self,what):
            if what in bucket.__dict__[self.id]:
                return True
            else:
                return False

        def cart(self,item_id,check=False):
            if check:
                if self.in_bucket(item_id):
                    self.bucket(item_id,False)
                else:
                    self.bucket(item_id)
            else:
                self.bucket(item_id)


        def add(self,item):
            i = copy.copy(item)
            try:
                s = self.container[i.__dict__['id']]
                for k in s.__dict__.keys():
                    if k == 'count': s.__dict__[k] += i.__dict__[k]
                    else: s.__dict__[k] = i.__dict__[k]
            except:
                self.container[i.__dict__['id']] = i

            return True

        def checkout(self):
            print 'checkout'
            for i in bucket.__dict__[self.id]:
                res = self.buy( self.container[i] )

            self.bucket_clear()

            return res

        def buy(self,item):
            i = copy.copy(item)

            if mc.cash >= i.cost:
                mc.cash -= i.cost
                pocket.add(i)
                return True
            else:
                return False

        def sell(self,item,price,cash=True):
            i = copy.copy(item)
            i.cost = price
            pocket.drop(i.id)
            if cash:
                mc.cash += i.cost
            else:
                mc.bank += i.cost

            i.cost = i.cost * float(1.3)
            self.add(i)
            return True




### Shop #####################################################################################

style vui_button:
    padding (5,5,15,5)

screen shop_ui(obj):
    python:
        prod = obj.container
        c = 2
        cs = 10
        cw = (vui.ui.area['catalog'][2] / c )-cs
        total = 0
        stt = str(len(bucket.__dict__[obj.id]))
        for i in bucket.__dict__[obj.id]:
            total += prod[i].cost

    hbox:
        python:
            try:
                if renpy.loadable(vui.ui.bg_img):
                    thebgr = vui.ui.bg_img
                else:
                    thebgr = Color(vui.ui.bg).shade(.8)
            except:
                thebgr = Color(vui.ui.bg).shade(.8)

        frame style style['vui']['area']['tag']:
            background thebgr

            vbox yalign 0.5 xoffset 40-4 spacing 16:
                textbutton "Selection" action SetVariable('bucket.vui','catalog'):
                    text_color vui.ui.fg style 'vui_button'
                    xsize vui.ui.area['tag'][2]-40 text_xalign 1.0 selected_background Color(vui.ui.bg)
                textbutton "Cart ("+stt+")" action SetVariable('bucket.vui','cart'):
                    text_color vui.ui.fg style 'vui_button'
                    xsize vui.ui.area['tag'][2]-40 text_xalign 1.0 selected_background Color(vui.ui.bg)
                if mc.cash >= total:
                    if total > 0:
                        $ maction = Function(obj.checkout)
                    else:
                        $ maction = Null
                    textbutton "Pay ("+str(total)+" $)" action maction :
                        xsize vui.ui.area['tag'][2]-40 text_xalign 1.0 selected_background Color(vui.ui.bg)
                else:
                    textbutton "Not Enough" action Null :
                        text_color Color(vui.ui.fg).shade(.5)
                        xsize vui.ui.area['tag'][2]-40 text_xalign 1.0 selected_background Color(vui.ui.bg)

                textbutton "Reset" action Function(obj.bucket_clear):
                    text_color vui.ui.fg style 'vui_button'
                    xsize vui.ui.area['tag'][2]-40 text_xalign 1.0 selected_background Color(vui.ui.bg)

                textbutton "Exit" action Return(False):
                    text_color vui.ui.fg style 'vui_button'
                    xsize vui.ui.area['tag'][2]-40 text_xalign 1.0 selected_background Color(vui.ui.bg)

        if bucket.vui == 'catalog':
            frame style style['vui']['area']['catalog']:
                background vui.ui.bg
                vpgrid:
                    scrollbars "vertical"
                    cols c
                    spacing cs
                    draggable True
                    mousewheel True
                    for i in sorted(prod.keys()):
                        use shop_item(obj, prod[i], cw)

        else:
            frame style style['vui']['area']['cart']:
                background vui.ui.bg
                vbox:
                    viewport ysize vui.ui.area['cart'][3]:
                        scrollbars "vertical"
                        vbox:
                            spacing 8
                            python:
                                c = {}
                                for i in bucket.__dict__[obj.id]:
                                    if not i in c:
                                        c[i] = 1
                                    else:
                                        c[i] += 1

                            for i in c.keys():
                                hbox xfit True:
                                    vbox xsize 20:
                                        textbutton ico("minus-square") action Function(obj.cart,item_id=prod[i].id,check=True):
                                            style "ram_ico" text_size 18 text_line_leading 2 text_color vui.ui.fg
                                    vbox xsize 60:
                                        text str(c[i]) xalign 1.0 color vui.ui.fg
                                    vbox xsize 80:
                                        text str(prod[i].cost) xalign 1.0 color vui.ui.fg
                                    text prod[i].desc xoffset 20 color vui.ui.fg

                                frame ysize 1 background Color(vui.ui.bg).replace_lightness(.5)

                            hbox yoffset 24:
                                vbox xsize 80:
                                    text "Total" color vui.ui.fg
                                vbox xsize 80:
                                    text str(total) xalign 1.0  color vui.ui.fg bold True

screen shop_item(obj,item,width=180):
        python:
            iconsize=(100,100)
            icon = im.Scale(item.icon(),iconsize[0],iconsize[1])
        window xsize width ysize 100:
            hbox:
                vbox xsize 100 yalign 0.0 xalign 0.5:
                    imagebutton action Function(obj.cart,item_id=item.id):
                        idle icon
                        hover im.MatrixColor(icon,im.matrix.brightness(0.3))

                vbox xsize width-100 yalign 0.5:
                    python:
                        try: name = item.name
                        except: name = None
                    if not name is None:
                        text item.name bold True size 14 color vui.ui.fg
                    text item.desc color vui.ui.fg
                    if not item.effect is None:
                        text item.effect[1].title() + " (" + str(item.effect[2]) + ")" size 18 color Color(vui.ui.fg).shade(.7)
                    text str(item.cost)+" $" color vui.ui.fg

