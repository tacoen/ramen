init -208 python:

    import ntpath
    import re
    import datetime
    import copy
    import sys

    class ramen_util:

        def __repr__(self): return """

        ramen_util syntax:
        ------------------
        fn_getdir()
        fn_info(fullfilepath)
        fn_ezy(filepath,extension_list)

        """

        # fn -- files functions

        def fn_getdir(self):
            inf = renpy.get_filename_line()
            dir, fn = ntpath.split(inf[0])
            return re.sub(r'^game/','',dir)

        def fn_info(self,f):
            r = {}

            r[str('path')], r[str('file')] = ntpath.split(f)
            a = r['file'].split('.')
            r[str('name')] = str(a[0])
            r[str('ext')] = str(a[1])
            r[str('dir')] = str(r['path'])
            r[str('path')] = r['path'].replace(ntpath.dirname(r['path'])+"/",'')
            return r

        def fn_ezy(self, file, ext=['.jpg', '.png', '.webp' ]):
            rfile = False
            n=0
            for e in ext:
                if renpy.loadable(file+e):
                    rfile = file+e
                    n = 1
                if n==1: break
            return rfile

        def safestr(self,string1,string2=None):
            s = str(string1)
            if not string2 is None:
                s +=  "_" + str(string2)
            else:
                s = s.replace(' ','_')
            regex = re.compile('[^a-zA-Z_0-9]')
            va = [ 'for','of','by']
            for v in va: s = s.replace(v,'')
            s = regex.sub('',s)
            s = s.replace('__','_')
            return s

        # json

        def json_file(self,file):

            with open(renpy.loader.transfn(file),'r') as json_file:
                return json.load(json_file)

        def json_write(self,file,data):
            with open(renpy.loader.transfn(file),'w') as outfile:
                json.dump(data, outfile)

        # Color

        def color_variant(self, hex_color, percent=25,invert=False):
            brightness_offset = int(float(256) * percent/100)
            if len(hex_color) == 4:
                R = str(hex_color[1])+str(hex_color[1]) + str(hex_color[2])+str(hex_color[2]) + str(hex_color[3])+str(hex_color[3])
                s = '#'
                hex_color = "#"+ R
            if len(hex_color) != 7:
                raise Exception("Passed %s into color_variant(), needs to be in #ffcc33 or #fc3 format." % hex_color)
            rgb_hex = [hex_color[x:x+2] for x in [1, 3, 5]]

            if invert:
                new_rgb_int = [255-int(hex_value, 16) for hex_value in rgb_hex]
            else:
                new_rgb_int = [int(hex_value, 16) + brightness_offset for hex_value in rgb_hex]

            new_rgb_int = [min([255, max([0, i])]) for i in new_rgb_int] # make sure new values are between 0 and 255
            fin_rgb_int=[]
            for i in new_rgb_int:
                # hex() produces "0x88", we want just "88"
                a = hex(i)[2:]
                if len(a)==1: a = str(a) +"0"
                fin_rgb_int.append(a)
            return "#" + "".join([str(i) for i in fin_rgb_int])

        def color_Darken(self,hex_color,percent=15):
            return self.color_variant(hex_color,percent*-1)

        def color_Brighten(self,hex_color,percent=15):
            return self.color_variant(hex_color,percent)

        def color_Invert(self,hex_color):
            return self.color_variant(hex_color,0,True)

        # Love the random (renpy.random.randint)

        def color_random(self,lo=0,hi=255):
            r = lambda: renpy.random.randint(lo,hi)
            return ('#%02X%02X%02X' % (r(),r(),r()))

        random_color = color_random

        def random_int(self,min=0,max=1,array=False):
            if array:
                return array [ int(renpy.random.randint(min,max)-1)]
            else:
                return int(renpy.random.randint(min,max))

        def random_of(self,array):
            return array [ int(renpy.random.randint(0,len(array)-1))]

        # toggles

        def toggle(self,what,sfx=True):

            if not renpy.loadable(DEFAULT_SFXPATH+"/tone1.mp3"):
                sfx = False

            if globals()[what] == True:
                globals()[what] = False
                if sfx: renpy.play(DEFAULT_SFXPATH+"/tone0.mp3")
            else:
                globals()[what] = True
                if sfx: renpy.play(DEFAULT_SFXPATH+"/tone1.mp3")

        def cycle(self,current,list):
            current += 1
            if current >= len(list): current = 0
            return current

        # Image util

        def get_sceneimg(self):
            t = tuple(renpy.get_showing_tags('master',True))
            a = renpy.get_attributes(t[0])
            try: bgr = t[0] +" "+ a[0]
            except: bgr = t[0]
            try: res = renpy.get_registered_image(bgr).filename
            except:
                try:
                    res = renpy.get_registered_image(bgr).child.args[0][0][1].filename
                except:
                    res = "blank"
            return res
