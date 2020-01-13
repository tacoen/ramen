init -208 python:

    import ntpath
    import re
    import datetime
    import hashlib
    import sys

    from colour import pColor

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
            r['path'], r['file'] = ntpath.split(f)
            a = r['file'].split('.')
            r['name'] = a[0]
            r['ext'] = a[1]
            r['dir'] = r['path']
            r['path'] = r['path'].replace(ntpath.dirname(r['path'])+"/",'')
            return r

        def fn_ezy(self, file, ext=['.jpg', '.png', '.webp' ]):
            rfile = False
            n=0
            for e in ext.reverse():
                if renpy.loadable(file+e): 
                    rfile = file+e
                    n = 1
                if n==1: break
            return rfile

        # json
            
        def json_file(self,file):

            with open(renpy.loader.transfn(file),'r') as json_file:
                return json.load(json_file)

        def json_write(self,file,data):
            with open(renpy.loader.transfn(file),'w') as outfile:
                json.dump(data, outfile)                 

        def color_variant(hex_color, brightness_offset=1):
            """ takes a color like #87c95f and produces a lighter or darker variant """
            if len(hex_color) != 7:
                raise Exception("Passed %s into color_variant(), needs to be in #87c95f format." % hex_color)
            rgb_hex = [hex_color[x:x+2] for x in [1, 3, 5]]
            new_rgb_int = [int(hex_value, 16) + brightness_offset for hex_value in rgb_hex]
            new_rgb_int = [min([255, max([0, i])]) for i in new_rgb_int] # make sure new values are between 0 and 255
            # hex() produces "0x88", we want just "88"
            return "#" + "".join([hex(i)[2:] for i in new_rgb_int])
            