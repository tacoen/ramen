init -201 python:

    class inventory(ramen_object):

        def __init__(self, store, max=24):

            try:
                mc
            except BaseException:
                print "*** Mising mc=player() ***"
                return false

            try:
                mc._inventory[store]
            except BaseException:
                mc._inventory[str(store)] = {}
            self.id = ramu.safe_id(store)
            
            self.sync()
            
            self.max = int(max)
            self.action = object()

        def sync(self):
            self.container = mc._inventory[self.id]
        
        def __repr__(self):
            return self.__class__.__name__

        def __call__(self):
            return self.container

        def transfer(self, item_id, store='stock'):

            try:
                target = globals()[store]
            except BaseException:
                return False

            try:
                item = self.container[item_id]
            except BaseException:
                return False

            if "inventory" in str(type(target)):
                target.add(item)
                self.drop(item_id)
            else:
                self.drop(item_id)

            return True

        def add(self, item):
            i = copy.copy(item)

            self.sync()

            try:
                s = self.container[i.__dict__['id']]
                for k in s.__dict__.keys():
                    if k == 'count':
                        s.__dict__[k] += i.__dict__[k]
                    else:
                        s.__dict__[k] = i.__dict__[k]
            except BaseException:
                self.container[i.__dict__['id']] = i

            mc._inventory[self.id] = self.container
            return True

        def drop(self, item_id):
            del mc._inventory[self.id][item_id]
            self.container = mc._inventory[self.id]

        def use(self, item_id, who=None):

            res = True

            try:
                item = self.container[item_id]
            except BaseException:
                return False

            if item.effect is not None:

                eff = item.effect

                if isinstance(eff, list):
                    if eff[0] == 'stat':

                        ov = mc.stat[eff[1]]
                        mc.stat[eff[1]] += eff[2]

                        if mc.stat[eff[1]] > mc.limits['stat'][1]:
                            mc.stat[eff[1]] = mc.limits['stat'][1]
                        if mc.stat[eff[1]] < mc.limits['stat'][0]:
                            mc.stat[eff[1]] = mc.limits['stat'][0]

                        if ov < mc.stat[eff[1]]:
                            res = False
                        else:
                            res = True

                    if eff[0] == 'rel':
                        res = False
                        if who in mc.rel.keys():
                            if isinstance(eff[1], list):
                                for x in range(0, len(mc.rel[who])):
                                    try:
                                        mc.rel[who][x] += eff[1][x]
                                        res = True
                                    except BaseException:
                                        mc.rel[who][x] += 0
                            else:
                                mc.rel[who][0] += eff[1]
                                res = True
                        else:
                            res = False

            if not item.persist:
                item.count -= 1
                if item.count <= 0:
                    self.drop(item_id)

            return res

    ## shop
    
    class shop(ramen_object):

        def load(self, default=False, **kwargs):
            self.__dict__['container'] = {}

            try:
                rbc.__dict__[self.id + "_cart"]
            except BaseException:
                rbc.__dict__[self.id + "_cart"] = []

        def rbc_clear(self):
            rbc.__dict__[self.id + "_cart"] = []

        def rbc(self, what, add=True):
            if add:
                rbc.__dict__[self.id + "_cart"].append(what)
            else:
                n = rbc.__dict__[self.id + "_cart"].index(what)
                rbc.__dict__[self.id + "_cart"].pop(n)

        def in_rbc(self, what):
            if what in rbc.__dict__[self.id + "_cart"]:
                return True
            else:
                return False

        def cart(self, item_id, check=False):
            if check:
                if self.in_rbc(item_id):
                    self.rbc(item_id, False)
                else:
                    self.rbc(item_id)
            else:
                self.rbc(item_id)

        def add(self, item):
            i = copy.copy(item)
            try:
                s = self.container[i.__dict__['id']]
                for k in s.__dict__.keys():
                    if k == 'count':
                        s.__dict__[k] += i.__dict__[k]
                    else:
                        s.__dict__[k] = i.__dict__[k]
            except BaseException:
                self.container[i.__dict__['id']] = i

            return True

        def checkout(self):
            #print 'checkout'
            for i in rbc.__dict__[self.id + "_cart"]:
                res = self.buy(self.container[i])

            self.rbc_clear()

            return res

        def buy(self, item):
            i = copy.copy(item)
            
            # print i.__dict__

            if mc.cash >= i.cost:
                mc.cash -= i.cost
                pocket.add(i)
                return True
            else:
                return False

        def sell(self, item, price, cash=True):
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

### Inventory ############################################################

python:

    def item_view(item):
        renpy.use_screen('hc_item',item=item)

screen inventory_ui(obj='pocket',max=None,returnvalue=False):

    $ globals()[obj].sync()
    
    modal True

    python:
        try: rbc.hud_selected_item
        except: rbc.hud_selected_item = None

        inv=mc._inventory[obj]
        iconsize=(100,100)
        w=style['hud']['area'][obj].xminimum
        h=style['hud']['area'][obj].yminimum
        tc=int(round(w/(iconsize[0])))
        tr=int(round(h/(iconsize[1])))
        cmax=tc * tr

        if max > cmax: 
            cmax = max
            tr=None
        
        cs=((w-(tc * iconsize[0]+2)) / tc)/2
        safebgr=ramu.safecolor_for_bgr(hud.ui.bgcolor[rbc.hud_set], hud.ui.fgcolor[rbc.hud_set])
        
        mc.limit[obj]=[0, cmax]

    frame background safebgr style style['hud']['area'][obj]:

        style_prefix "inventory_ui"

        vbox:
            use hc_tbar(obj,obj.title(),returnvalue)

            hbox ysize 32 yalign 0.5 xfill True:
                text "Maximum: " + ("{:02d}".format(mc.limit[obj][1])) color hud.ui.fgcolor[rbc.hud_set]
                text ("{:03d}".format(mc.cash)) +" $" yalign 0.5 line_leading 2 color hud.ui.fgcolor[rbc.hud_set] size 24 xalign 1.0

            null height 16

            if rbc.hud_selected_item is None:

                vpgrid cols tc spacing cs ysize h/2:
                    draggable True
                    mousewheel True
                    scrollbars "vertical"

                    for i in sorted(inv.keys()):
                        python:
                            item=inv[i]
                            icon=im.Scale(item.icon(),iconsize[0],iconsize[1])

                        imagebutton:
                            idle icon
                            hover im.MatrixColor(icon,im.matrix.brightness(0.3))
                            action SetVariable('rbc.hud_selected_item',item)

                null height 16

            else:
                frame background Color(safebgr).replace_lightness(0.3) padding (8,8,8,8):
                    textbutton "x" action SetVariable('rbc.hud_selected_item',None) xpos 1.0 ypos -8 xanchor 0.9
                    viewport:
                        use hc_item(obj,rbc.hud_selected_item)

screen hbox_item(what,value):
    hbox xfill True yalign 0.5:
        text str(what) size 20 color hud.ui.fgcolor[rbc.hud_set]
        text str(value) size 20 xalign 1.0 color hud.ui.fgcolor[rbc.hud_set]

screen hc_item(obj,item):

    python:
        try: eatable=item.eatable
        except: eatable=False
        try: depend=item.depend
        except: depend=False
        w=style['hud']['area'][obj].xminimum - 120

    hbox:
        add item.icon()
        null width 12
        vbox spacing 6 yfit True:
            if not item.name is None:
                text "{b}"+item.name +"{/b}\n{size=-2}"+item.desc+"{/size}" color hud.ui.fgcolor[rbc.hud_set]
            else:
                text item.desc color hud.ui.fgcolor[rbc.hud_set]

            null height 8
            frame background hud.ui.fgcolor[rbc.hud_set] ysize 1
            null height 8

            use hbox_item('Price', item.cost)

            if depend:
                use hbox_item('Require',depend)

            if not item.effect is None:
                use hbox_item(item.effect[1].title()+"("+item.effect[0].title()+")", item.effect[2] )

            null height 8
            frame background hud.ui.fgcolor[rbc.hud_set] ysize 1
            null height 8

            # item action
            
            python:
                act = globals()[obj].action.__dict__
                
            hbox xfill True:
            
                if obj.lower() != 'pocket':
                    textbutton "-> Pocket" action [
                    Function( globals()[obj].transfer,item_id=item.id, store='pocket'),
                    SetVariable('rbc.hud_selected_item',None)
                    ]
                else:
                    if last_label == 'mch_kitchen':
                        textbutton "<- Stock" action [
                        Function( globals()[obj].transfer,item_id=item.id, store='stock'),
                        SetVariable('rbc.hud_selected_item',None)
                        ]
                
                if eatable:
                    textbutton "Eat/Drink" action [
                    Function( globals()[obj].use,item_id=item.id),
                    SetVariable('rbc.hud_selected_item',None)
                    ]

                textbutton "Drop" action [ 
                    Function( globals()[obj].drop,item_id=item.id),
                    SetVariable('rbc.hud_selected_item',None)
                    ]

                for a in act:
                    
                    if depend and a == depend.lower():
                    
                        textbutton a.title() action [
                            Function(act[a],item_id=item.id),
                            SetVariable('rbc.hud_selected_item',None)
                        ]
                        

                #textbutton "Give" action Null



### Shop #################################################################

style shopui_button:
    padding(5, 5, 15, 5)

screen shop_ui(obj):
    python:
        prod = obj.container
        c = 2
        cs = 10
        cw = (obj.ui.area['catalog'][2] / c) - cs
        total = 0

        stt = str(len(rbc.__dict__[obj.id + "_cart"]))

        for i in rbc.__dict__[obj.id + "_cart"]:
            total += prod[i].cost

        try:
            shop_tab
        except BaseException:
            shop_tab = 'catalog'

    hbox:
        python:
            try:
                if renpy.loadable(obj.ui.bg_img):
                    thebgr = obj.ui.bg_img
                else:
                    thebgr = Color(obj.ui.bg).shade(.8)
            except BaseException:
                thebgr = Color(obj.ui.bg).shade(.8)

        frame style style[obj.id]['area']['tag']:
            background thebgr

            vbox yalign 0.5 xoffset 40 - 4 spacing 16:
                textbutton "Selection" action SetScreenVariable('shop_tab', 'catalog'):
                    text_color obj.ui.fg style 'obj.ui_button'
                    xsize obj.ui.area['tag'][2] - 40 text_xalign 1.0 selected_background Color(obj.ui.bg)
                textbutton "Cart (" + stt + ")" action SetScreenVariable('shop_tab', 'cart'):
                    text_color obj.ui.fg style 'obj.ui_button'
                    xsize obj.ui.area['tag'][2] - 40 text_xalign 1.0 selected_background Color(obj.ui.bg)
                if mc.cash >= total:
                    if total > 0:
                        $ maction = Function(obj.checkout)
                    else:
                        $ maction = Null
                    textbutton "Pay (" + str(total) + " $)" action maction:
                        xsize obj.ui.area['tag'][2] - 40 text_xalign 1.0 selected_background Color(obj.ui.bg)
                else:
                    textbutton "Not Enough" action Null:
                        text_color Color(obj.ui.fg).shade(.5)
                        xsize obj.ui.area['tag'][2] - 40 text_xalign 1.0 selected_background Color(obj.ui.bg)

                textbutton "Reset" action Function(obj.rbc_clear):
                    text_color obj.ui.fg style 'obj.ui_button'
                    xsize obj.ui.area['tag'][2] - 40 text_xalign 1.0 selected_background Color(obj.ui.bg)

                textbutton "Exit" action Return(False):
                    text_color obj.ui.fg style 'obj.ui_button'
                    xsize obj.ui.area['tag'][2] - 40 text_xalign 1.0 selected_background Color(obj.ui.bg)

        if shop_tab == 'catalog':
            frame style style[obj.id]['area']['catalog']:
                background obj.ui.bg
                vpgrid:
                    scrollbars "vertical"
                    cols c
                    spacing cs
                    draggable True
                    mousewheel True
                    for i in sorted(prod.keys()):
                        use shop_item(obj, prod[i], cw)

        else:
            frame style style[obj.id]['area']['cart']:
                background obj.ui.bg
                vbox:
                    viewport ysize obj.ui.area['cart'][3]:
                        scrollbars "vertical"
                        vbox:
                            spacing 8
                            python:
                                c = {}
                                for i in rbc.__dict__[obj.id + "_cart"]:
                                    if i not in c:
                                        c[i] = 1
                                    else:
                                        c[i] += 1

                            for i in c.keys():
                                hbox xfit True:
                                    vbox xsize 20:
                                        textbutton ico("minus-square") action Function(obj.cart, item_id=prod[i].id, check=True):
                                            style "ramen_icon" text_size 18 text_line_leading 2 text_color obj.ui.fg
                                    vbox xsize 60:
                                        text str(c[i]) xalign 1.0 color obj.ui.fg
                                    vbox xsize 80:
                                        text str(prod[i].cost) xalign 1.0 color obj.ui.fg
                                    text prod[i].desc xoffset 20 color obj.ui.fg

                                frame ysize 1 background Color(obj.ui.bg).replace_lightness(.5)

                            hbox yoffset 24:
                                vbox xsize 80:
                                    text "Total" color obj.ui.fg
                                vbox xsize 80:
                                    text str(total) xalign 1.0  color obj.ui.fg bold True

screen shop_item(obj, item, width=180):
    python:
        iconsize = (100, 100)
        icon = im.Scale(item.icon(), iconsize[0], iconsize[1])
    window xsize width ysize 100:
        hbox:
            vbox xsize 100 yalign 0.0 xalign 0.5:
                imagebutton action Function(obj.cart, item_id=item.id):
                    idle icon
                    hover im.MatrixColor(icon, im.matrix.brightness(0.3))

            vbox xsize width - 100 yalign 0.5:
                python:
                    try:
                        name = item.name
                    except BaseException:
                        name = None
                if name is not None:
                    text item.name bold True size 14 color obj.ui.fg
                text item.desc color obj.ui.fg
                if item.effect is not None:
                    text item.effect[1].title() + " (" + str(item.effect[2]) + ")" size 18 color Color(obj.ui.fg).shade(.7)
                text str(item.cost) + " $" color obj.ui.fg
