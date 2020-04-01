init -200 python:

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
            # print 'checkout'
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
