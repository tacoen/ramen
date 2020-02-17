init -208 python:

    import ntpath
    import re
    import datetime
    import copy
    import sys
    import json
    import uuid

    class ramen_util:

        def __repr__(self): 
        
            return "https://https://github.com/tacoen/ramen"

        # fn -- files functions

        def fn_getdir(self):
            inf=renpy.get_filename_line()
            dir, fn=ntpath.split(inf[0])
            return re.sub(r'^game/','',dir)

        def fn_info(self,f):
            r={}

            r[str('path')], r[str('file')]=ntpath.split(f)
            a=r['file'].split('.')
            r[str('name')]=str(a[0])
            r[str('ext')]=str(a[1])
            r[str('dir')]=str(r['path'])
            r[str('path')]=r['path'].replace(ntpath.dirname(r['path'])+"/",'')
            return r

        def fn_ezy(self, file, ext=['.jpg', '.png', '.webp' ]):
            rfile=False
            n=0
            for e in ext:
                if renpy.loadable(file+e):
                    rfile=file+e
                    n=1
                if n==1: break
            return rfile

        def fn_files(self,where,key=False):
            F=renpy.list_files(False)
            files=filter(lambda w:where+"/" in w, sorted(F))
            if key:  files=filter(lambda w:key in w, files)
            return files

        # str

        def nicenaming(self,str_strip,name):
            nn=name.replace(str_strip,'').replace('_',' ')
            return nn.title()

        def safeid(self,id):
            id=id.replace('-','')
            return id

        def safestr(self,string1,string2=None):
            s=str(string1)
            if not string2 is None:
                s +=  "_" + str(string2)
            else:
                s=s.replace(' ','_')
            regex=re.compile('[^a-zA-Z_0-9]')
            va=[ 'for','of','by']
            for v in va: s=s.replace(v,'')
            s=regex.sub('',s)
            s=s.replace('__','_')
            return s

        # json

        def json_file(self,file):

            with open(renpy.loader.transfn(file),'r') as json_file:
                return json.load(json_file)

        def json_write(self,file,data):
            with open(renpy.loader.transfn(file),'w') as outfile:
                json.dump(data, outfile)

        # Color

        def safecolor_for_bgr(self,hex_color,bgr_hc):
            nno=Color(hex_color).hexcode[:7]
            if nno == bgr_hc:
                return Color(nno).replace_lightness(.1).hexcode
            else:
                return hex_color

        def color_Darken(self,hex_color,ammount=0.2):
            return Color(hex_color).shade(ammount)

        def color_Brighten(self,hex_color,amount=0.2):
            return Color(hex_color).tint(1-float(ammount))

        # Love the random (renpy.random.randint)

        def color_random(self,lo=0,hi=255):
            r=lambda: renpy.random.randint(lo,hi)
            return ('#%02X%02X%02X' % (r(),r(),r()))

        random_color=color_random

        def random_int(self,min=0,max=1,array=False):
            if array:
                return array [ int(renpy.random.randint(min,max)-1)]
            else:
                return int(renpy.random.randint(min,max))

        def random_of(self,array):
            return array [ int(renpy.random.randint(0,len(array)-1))]

        # mc interaction
        
        def buy(self,price):
            if mc.cash >= price:
                mc.cash -= price
                return True
            else:
                return False

        def limit(self, what, ov, value=1):
            ov += int(value)
            if not what in mc.limit.keys(): what='stat'
            if ov > mc.limit[what][1]:
                ov=mc.limit[what][1]
            elif ov < mc.limit[what][0]:
                ov=mc.limit[what][0]
            return ov
                
        # toggles

        def ltoggle(self,what):
            if what:
                return False
            else:
                return True

        def toggle(self,what,sfx=True):
            
            if not ramu.sfx( THEME_PATH, "tone1", False, False):
                sfx=False

            if globals()[what] == True:
                globals()[what]=False
                if sfx: ramu.sfx( THEME_PATH, "tone0", True, False)
            else:
                globals()[what]=True
                if sfx: ramu.sfx( THEME_PATH, "tone1", True, False)

        def cycle(self,current,list):
            current += 1
            if current >= len(list): current=0
            return current

        # Screen/ UI Utils
        
        def screen_hideby(self,prefix):
            scrs=filter(lambda fw:prefix in fw, renpy.get_showing_tags('screens'))
            for scr in scrs:
                renpy.hide_screen(scr)
        
        def screen_check(self,name):
            if name in renpy.get_showing_tags('screens'):
                return True
            else:
                return False
                
        def notify(self,msg,icoram=None):
            renpy.show_screen('ingame_notify',msg=msg,icoram=icoram)                
        
        # Mass function : Items
        
        def create_items(self, inventory, where, prefix, **kwargs ):
        
            files=ramu.fn_files(where,prefix)

            for f in files:
                fn=ramu.fn_info(f)
                i=item(fn['name'])

                for k in kwargs.keys():
                    i.__dict__[k]=kwargs[k]

                    if k == 'cost':
                        try: kwargs[k][0]
                        except: kwargs[k][0]=10
                        try: kwargs[k][1]
                        except: kwargs[k][1]=20

                        i.__dict__['cost']=ramu.random_int(kwargs[k][0],kwargs[k][1])

                i.__dict__['dir']=str(where)
                i.__dict__['desc']=ramu.nicenaming(prefix,fn['name'])
                
                inventory.add(i)
            
            
        # Image util

        def get_profilepic(self,whoid,size=(48,48)):
            try: ppic = globals()[whoid].profile_pic
            except: ppic = ramu.theme_image(THEME_PATH, "/gui/profile")
            return im.Scale(ppic,size[0],size[1])

        def get_sceneimg(self):
            t=tuple(renpy.get_showing_tags('master',True))
            a=renpy.get_attributes(t[0])
            try: bgr=t[0] +" "+ a[0]
            except: bgr=t[0]
            try: res=renpy.get_registered_image(bgr).filename
            except:
                try:
                    res=renpy.get_registered_image(bgr).child.args[0][0][1].filename
                except:
                    res="blank"
            return res
            
        def theme_image(self,where,what):
            file= self.fn_ezy(where+"/"+what)
            if file: 
                return file
            else:
                file=self.fn_ezy(RAMEN_THEME_PATH+"/"+what)
                if file: return file
            
            return RAMEN_PATH + "/img/noimage.png"
            

        # Sound util
        
        def sfx(self,where,what,play=True,loop=False):
            file= self.fn_ezy(where+"/"+what , ['.ogg', '.mp3', '.wav' ])
            if not file: file=self.fn_ezy(RAMEN_THEME_PATH+"/audio/"+what , ['.ogg', '.mp3', '.wav' ])
            if not file: file=self.fn_ezy(DEFAULT_SFXPATH+"/"+what , ['.ogg', '.mp3', '.wav' ])
            if file and play: renpy.music.play(file,loop=loop)
            return file
                
            

    # renpy behave

    def label_callback(name, abnormal):
        store.last_label=name

    config.label_callback=label_callback
   
init -102 python:

    def rbcing(what,value=None,**kwargs):
        # rbc.data
        try: _ramen_container.__dict__[what]
        except:  _ramen_container.__dict__[str(what)]={}

        if not value is None:
             _ramen_container.__dict__[what]=value
        for k in kwargs:
             _ramen_container.__dict__[what][k]=kwargs[k]

    def get_rbc(which,what=None):
        if what is None:
            try: return  _ramen_container.__dict__[which]
            except: return False
        else:
            try: return  _ramen_container.__dict__[which][what]
            except: return False
            
            