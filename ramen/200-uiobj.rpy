init -203 python:

    class uiobj(ramen_object):

        def load(self,id=None,**kwargs):
            self.__dict__['param'] = {}
            
            self.__dict__['ui'] = rn_obj(0)
            
            self.set(**kwargs)

            try: bucket.__dict__[self.id]
            except: bucket.__dict__[self.id] = {}

        def set(self,**kwargs):

            for k in kwargs:
                instyle = self.makestyle(k,kwargs[k])
            
                setattr(self.__dict__['ui'],k,kwargs[k])

        def makestyle(self, key, val):

            try: style[self.id]
            except: style[self.id] = Style(style.default)

            ins = False

            def makestyle_hbar(key,val):

                for t in val.keys():
                    try: bcolor = val[t]
                    except: bcolor = ramen.random_colour(128,255)

                    style[self.id][key][t].thumb = bcolor
                    style[self.id][key][t].right_bar=bcolor+"5"
                    style[self.id][key][t].left_bar=bcolor+"D"
                    style[self.id][key][t].ysize = 16

            def makestyle_area(key,val):
                for t in val.keys():

                    try: style[self.id][key][t].xpos = val[t][0]
                    except: style[self.id][key][t].xpos = 0
                    try: style[self.id][key][t].ypos = val[t][1]
                    except: style[self.id][key][t].ypos = 0
                    try: style[self.id][key][t].xsize = val[t][2]
                    except: style[self.id][key][t].xsize = config.screen_width
                    try: style[self.id][key][t].ysize = val[t][3]
                    except: style[self.id][key][t].ysize = config.screen_height
                    try: style[self.id][key][t].padding = val[t][4]
                    except: style[self.id][key][t].padding = (0,0,0,0)

            if key=='hbar': ins = makestyle_hbar(key,val)
            if key=='area': ins = makestyle_area(key,val)

