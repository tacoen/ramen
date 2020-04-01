init -208 python:

    try:
        RAMEN_DEV
    except BaseException:
        RAMEN_DEV = False

    class ramen_util:

        def __repr__(self):

            return "https://https://github.com/tacoen/ramen"

        # fn -- files functions

        def fn_getdir(self):
            """Get the directory of the scripts from renpy.get_filename_line"""

            inf = renpy.get_filename_line()
            return str(re.sub(r'^game/', '', os.path.dirname(inf[0])))

        def fn_info(self, f):
            """
            Get and extract the file information of the [file] as dict

            f = "e:/yourproject/game/npc/girls_of_90/alpha/lucy smile.png"

            | key | mark | example |
            | ---- | ---- | ---- |
            | file | filename | lucy smile.png |
            | name | name | lucy smile |
            | ext | extension | png |
            | dir  | where the file was | npc/girl_of_90 | "
            | path | path | alpha |

            """

            r = {}
            r[str('path')] = os.path.dirname(f)
            r[str('file')] = os.path.basename(f)
            a = r['file'].split('.')
            r[str('name')] = str(a[0])
            r[str('ext')] = str(a[1])
            r[str('dir')] = str(r['path'])
            r[str('path')] = r['path'].replace(
                os.path.dirname(r['path']) + "/", '')
            return r

        def fn_ezy(self, file, ext=['.jpg', '.png', '.webp']):
            """Get renpy.loadable [file] base on last-seen [ext] extension-list"""
            rfile = False
            n = 0
            for e in ext:
                if renpy.loadable(file + e):
                    return file + e

            return False

        def fn_files(self, where, key=False):
            """ Collect files from [where], and [keyword]."""

            F = renpy.list_files(False)
            files = filter(lambda w: where + "/" in w, sorted(F))
            if key:
                files = filter(lambda w: key in w, files)
            return files

        # str

        def nicenaming(self, str_strip, name):
            """
            Strip 'str_strip' from 'name', and replace '_' as whitespace as title

            ``` python
                a = ramu.nicenaming('prefix_','prefix_keyword_some')

                >a
                Keyword Some
            ```
            """
            return str(name.replace(str_strip, '').replace('_', ' ').title())

        def safe_id(self, id):
            """Strip non-safecharacter for [id]."""
            id = id.replace('-', '').replace(' ', '_').strip()
            id = re.sub('[^0-9a-zA-Z_]+', '', id)
            return id.lower()

        def unique_id(self, prefix='obj'):
            """
            Random generic id base on classname

            ``` python:
                testobj = ramen_object(keyword='value')

                > testobj.id
                ramen_object_VH98
            ```

            Beware of this kind of object, it's not be in your `renpy store` because it's randomize.
            It's there for counter-measuring.

            """
            return prefix + "_" +\
                "".join(random.choice(string.ascii_lowercase) for x in range(2)) + \
                "".join(random.choice(string.digits) for x in range(2))

        # json

        def json_file(self, file):

            with open(renpy.loader.transfn(file), 'r') as json_file:
                return json.load(json_file)

        def json_write(self, file, data):
            with open(renpy.loader.transfn(file), 'w') as outfile:
                json.dump(data, outfile)

        # Color

        def safecolor_for_bgr(self, hex_color, bgr_hc='#000'):
            if Color(hex_color) == Color(bgr_hc):
                return self.Color_invert(hex_color)
            else:
                return Color(hex_color)

        def color_Darken(self, hex_color, ammount=0.2):
            """Utilize renpy color.py."""
            return Color(hex_color).shade(ammount)

        def color_Brighten(self, hex_color, amount=0.2):
            """Utilize renpy color.py."""
            return Color(hex_color).tint(1 - float(ammount))

        def color_Invert(self, hex_color):
            """Invert color, #fff -> #000 vice-versa"""
            a = Color(hex_color).alpha
            (r, g, b) = Color(hex_color).rgb
            r = 1.0 - float(r)
            g = 1.0 - float(g)
            b = 1.0 - float(b)
            return Color(rgb=(r, g, b)).opacity(a)

        # Love the random (renpy.random.randint)

        def color_random(self, lo=0, hi=255):
            """Color be random. """
            if lo < 96:
                lo = 96
            if hi > 255:
                hi = 255

            def r(): return renpy.random.randint(lo, hi)
            return ('#%02X%02X%02X' % (r(), r(), r()))

        random_color = color_random

        def random_shuffle(self, array):
            random.shuffle(array)
            return array

        def random_series(self, many=5, min=-5, max=5):
            """Return random series of number from min to max for many."""
            r = []
            for n in range(0, many - 1):
                r.append(self.random_int(min, max))
            return r

        def random_int(self, min=0, max=1, array=False):
            """renpy.random.randint made easy."""
            if array:
                return array[int(renpy.random.randint(min, max) - 1)]
            else:
                return int(renpy.random.randint(min, max))

        def random_of(self, array):
            """renpy.random.randint of array/list."""
            return array[int(renpy.random.randint(0, len(array) - 1))]

        # mc interaction

        def mc_pay(self, price):
            """Pay `price` from mc.cash"""
            if mc.cash >= price:
                mc.cash -= price
                return True
            else:
                return False

        def mc_limit(self, what, ov, value=1):
            """Set value base on mc.limit values of it"""
            ov += value

            if what not in mc.limit.keys():
                what = 'stat'
            if ov > mc.limit[what][1]:
                ov = mc.limit[what][1]
            elif ov < mc.limit[what][0]:
                ov = mc.limit[what][0]
            return ov

        # toggles

        def ltoggle(self, what):
            if what:
                return False
            else:
                return True

        def toggle(self, what, sfx=True):

            if not self.sfx("tone1", False, False):
                sfx = False

            if globals()[what]:
                globals()[what] = False
                if sfx:
                    self.sfx("tone0", True, False)
            else:
                globals()[what] = True
                if sfx:
                    self.sfx("tone1", True, False)

        def cycle(self, current, list):
            current += 1
            if current >= len(list):
                current = 0
            return current

        # Screen/ UI Utils

        def screen_hideby(self, prefix):
            scrs = filter(
                lambda fw: prefix in fw,
                renpy.get_showing_tags('screens'))
            for scr in scrs:
                renpy.hide_screen(scr)

        def screen_check(self, name):
            if name in renpy.get_showing_tags('screens'):
                return True
            else:
                return False

        def notify(self, msg, ramen_icon=None):
            """
            Show 'ingame_notify' with 'msg' and 'ramen_icon'
            """

            renpy.show_screen('ingame_notify', msg=msg, ramen_icon=ramen_icon)

        def create_items(self, inventory, where, prefix, **kwargs):
            """
            Mass Create items

            ``` python
                ramu.create_items(marto,'items','zd_',
                    cost=(20,29),
                    eatable=True,
                    name='Soft Drinks',
                    effect=['stat','energy',2]
                )
            ```

            Scan image file from 'items', which has 'zd_' prefix and add the rest item attributes, and put them into `marto` inventory.
            """

            files = ramu.fn_files(where, prefix)

            for f in files:
                fn = ramu.fn_info(f)
                i = item(fn['name'])

                for k in kwargs.keys():
                    i.__dict__[k] = kwargs[k]

                    if k == 'cost':
                        try:
                            kwargs[k][0]
                        except BaseException:
                            kwargs[k][0] = 10
                        try:
                            kwargs[k][1]
                        except BaseException:
                            kwargs[k][1] = 20

                        i.__dict__['cost'] = ramu.random_int(
                            kwargs[k][0], kwargs[k][1])

                i.__dict__['dir'] = str(where)
                i.__dict__['desc'] = ramu.nicenaming(prefix, fn['name'])

                inventory.add(i)

        # Image util

        def get_profilepic(self, whoid, size=(48, 48)):
            """Get profile pic of whoid(npc)"""
            try:
                ppic = globals()[whoid].profile_pic
            except BaseException:
                ppic = ramu.fn_search('profile')
            return im.Scale(ppic, size[0], size[1])

        def get_sceneimg(self, condition=None, bgr=None):
            """Get currently showing scene"""
            t = tuple(renpy.get_showing_tags('master', True))
            a = renpy.get_attributes(t[0])

            if bgr is None:
                try:
                    bgr = t[0] + " " + a[0]
                except BaseException:
                    bgr = t[0]

            res = None

            try:
                res = renpy.get_registered_image(bgr).filename

            except BaseException:

                if condition is None:
                    condition = wo.suntime

                rl = renpy.get_registered_image(bgr).child.args[0]

                for r in rl:
                    if r[0] is True:
                        res_default = r[1].filename
                    try:
                        if r[0].endswith(condition + "'"):
                            res = r[1].filename
                    except BaseException:
                        pass

                if res is None:
                    res = res_default

            return res

        # Sound util

        def sfx(self, file, where=None, play=True, loop=False):
            """Play audio file if play is True, return if play is False."""

            file = self.fn_search(
                file, where, [
                    '.ogg', '.mp3', '.wav'], RAMEN_SFX_PATHS)

            if file and play:
                renpy.music.play(file, loop=loop)
            return file

        def fn_search(self, what, where=None, ext=[
                      '.jpg', '.png', '.webp'], wheres=RAMEN_GUI_PATHS):
            """
            Search file[.ext] from where_list. Ramen use RAMEN_GUI_PATHS and RAMEN_SFX_PATHS. Both are defined in theme_define.rpy

            ``` python
                ppic = ramu.fn_search('profile')
                file = self.fn_search(file, where, ['.ogg', '.mp3', '.wav'], RAMEN_SFX_PATHS)
            ```

            """
            if where is not None:
                wheres.append(where)

            wheres.sort()
            wheres.reverse()

            for where in wheres:
                if "." in what:
                    file = where + "/" + what
                    if renpy.loadable(file):
                        return file
                else:
                    file = self.fn_ezy(where + "/" + what, ext)
                    if file:
                        return file

            return False

        def safe(self, what, type='image'):
            """
            Safe value, default of type

            ``` python:
            image side thou = ramu.safe( ramu.fn_search('side-thou'), 'image')
            ```

            """
            if what:
                return what
            else:
                if type == 'sound':
                    return RAMEN_THEME_PATH + "/audio/beep.mp3"
                return RAMEN_THEME_PATH + "/gui/noimage.png"
