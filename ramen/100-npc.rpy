init -100 python:

    class npc(ramen_object):
        """
        Create a npc object. NPC, Non Player Character. a character of your renpy's visual novel.

        ## How to Create a NPC

        ### Namespace

        ``` bash
        . mia.rpy
        + -- /sprite/
             +-- s0.png
             +-- s1.png
             +-- s2.png
             +-- s3.png
             +-- s4.png
        +-- /pose/
             +-- smile.jpg
             +-- sad.jpg
             +-- bored.jpg
        +-- audio/
        +-- video/
        +-- expression/
        ```

        ### python code

        ``` python
        mia = npc('mia',name='Mia',lastname='Oranama')
        mia.spriteanim('dance',('s0','s1','s3','s4','s3'),(0.25,1,1,1,1))
        mia.set_phonenum()
        mia.gain('love',10)
        ```

        ### renpy

        ``` python
        show mia smile
        mia 'Shall we dance?'
        show mia dance
        ```


        """

        def load(self, id=None, **kwargs):
            """
            `load` is chained to __init__ at parent class

            Define Character() and its images.

            ``` python
            joan = npc('joan', name='Joana', lastname='Hurry', callname='An')
            ```

            kwargs:

            | keyword | argument/value |
            | ---- | ---- |
            | color | Color for character name in dialog. hexcolor or will be randomize |
            | wcolor | Color for character text in dialog, hexcolor or will be `#d0d0d0` |
            | name | Character name of will retrieve from id, textag: [joan.name] |
            | callname | Character call name of will retrieve from name, textag: [joan.callname] |
            | lastname | Character last name or will be empty string, textag: [joan.lastname]. `fullname` will be name + lastname |
            | gender | just a value, realy! |

            in label:

            ``` python
            show joan hi
            joan "Hi, everyone! My name is [joan.name]."
            ```

            """

            try:
                self.__dict__['pose']
            except BaseException:
                self.__dict__['pose'] = {}

            try:
                self.__dict__['chaattr']
            except BaseException:
                self.__dict__['chaattr'] = {}

            try:
                self.chaattr['who_color'] = str(self.color)
                del self.color
            except BaseException:
                self.chaattr['who_color'] = str(ramu.color_random(128, 255))

            try:
                self.chaattr['what_color'] = str(self.wcolor)
                del self.wcolor
            except BaseException:
                self.chaattr['what_color'] = str("#d9d9d9")

            try:
                self.name
                self.name = self.name.title()
            except BaseException:
                self.name = self.id.title()
            try:
                self.callname
                self.callname = self.callname.title()
            except BaseException:
                self.callname = self.name
            try:
                self.lastname
                self.lastname = self.lastname.title()
            except BaseException:
                self.lastname = ""
            try:
                self.gender
            except BaseException:
                self.gender = "f"

            self.fullname = str(self.name + " " + self.lastname).strip()

            if "[" in self.name:
                safename = self.name.lower()
            else:
                safename = self.name

            delm = []

            for p in self.param:
                for chp in ['window_', 'who_', 'what_']:
                    if p.startswith(chp):
                        self.chaattr[p] = self.param[p]
                        delm.append(p)

            for d in delm:
                del self.param[d]

            setattr(
                character,
                self.id.lower(),
                Character(
                    safename,
                    image=self.id,
                    **self.chaattr
                )
            )

            self.define_byfile()

            try:
                ramen_dev('npc', self.id)
            except BaseException:
                pass

        def extend(self):
            """
            Extend the character object.
            """
            if isinstance(self.dir, list):
                new_dir = self.dir
            else:
                new_dir = [self.dir]

            new_dir.append(str(ramu.fn_getdir()))

            self.dir = new_dir

            self.define_byfile()

        def get_stat(self):
            """All characters store their stat inside `player`(mc). if its not defined, it will be loaded from `defaults`"""

            try:
                mc.rel[self.id]
            except BaseException:
                mc.rel[self.id] = {}

            # defaults

            try:
                mc.rel[self.id]['relation']
            except BaseException:
                mc.rel[self.id]['relation'] = 0
            try:
                mc.rel[self.id]['corrupt']
            except BaseException:
                mc.rel[self.id]['corrupt'] = 0
            try:
                mc.rel[self.id]['love']
            except BaseException:
                mc.rel[self.id]['love'] = 0

            try:
                mc.rel[self.id]['like']
            except BaseException:
                mc.rel[self.id]['like'] = 10

            return mc.rel[self.id]

        def set_stat(self, **kwargs):
            """Set the character stats (dup?)"""

            try:
                mc.rel[self.id]
            except BaseException:
                mc.rel[self.id] = {}

            for k in kwargs:
                mc.rel[self.id][k] = kwargs[k]

        def gain(self, what=None, value=1):
            """Set the character stats within its limits"""

            # function that load from mc.rel
            stat = self.get_stat()

            try:
                stat[what]
            except BaseException:
                stat[what] = 0

            ov = stat[what]
            nv = ramu.limit(what, ov, value)
            stat[what] = nv

            mc.rel[self.id] = stat

            if ov > nv:
                return False
            elif ov < nv:
                return True
            else:
                return None

        def __call__(self):
            return self.__dict__['param']

        def define_byfile(self, main=None):
            """
            Called by init or load. Define everything in `namespaces`
            """

            voids = ['profile', 'chat', 'side']

            files = self.files(self.id + '/pose/') + self.files(self.id + "/")

            if files == []:
                return False

            conte = ['expression', 'sprite', 'video', 'audio', 'side']

            self.__dict__[str('side')] = {}

            self.__dict__[str('pose')] = {}

            for f in sorted(files):

                p = ramu.fn_info(f)

                if p['ext'] == 'json':
                    try:
                        self.__dict__['json']
                    except BaseException:
                        self.__dict__['json'] = {}

                    self.__dict__['json'][str(p['name'])] = f

                # sideimage and profile

                if p['name'] == 'profile':
                    self.profile_pic = f

                if p['name'] == 'side':
                    renpy.image('side ' + self.id, f)
                    self.side[self.id, f]

                if p['path'] in conte:

                    try:
                        if not p['name'] in voids:
                            self.__dict__[p['path']][str(p['name'])] = str(f)
                    except BaseException:
                        self.__dict__[str(p['path'])] = {}
                        if not p['name'] in voids:
                            self.__dict__[p['path']][str(p['name'])] = str(f)
                else:
                    if not p['name'] in voids and p['ext'] in [
                            'webp', 'jpg', 'png']:
                        self.__dict__['pose'][str(p['name'])] = str(f)

            n = 0

            for k in self.pose.keys():
                renpy.image(self.id + " " + k, self.pose[k])
                if n == 0:
                    ff = self.pose[k]
                n += 1

            if main is None:
                l = sorted(self.pose.keys())
                renpy.image(self.id, self.pose[l[0]])
            else:
                renpy.image(self.id, main)

            try:
                for v in self.video.keys():
                    renpy.image((self.id, v), Movie(play=self.video[v]))
            except BaseException:
                pass

            try:
                for v in self.side.keys():
                    renpy.image('side ' + self.id + " " + v, self.side[v])
            except BaseException:
                pass

            try:
                del self._files
            except BaseException:
                pass

            pi = ['phone-incall', 'phone-outcall', 'phone-oncall']

            for i in pi:

                print THEME_PATH

                try:
                    temp_img = ramu.theme_image(THEME_PATH, i)
                    print temp_img
                    print self.profile_pic
                    self.create_sideimage(self.profile_pic, temp_img, i)
                except BaseException:
                    pass

        def by_expression(self, pose, xy=(0, 0)):
            """
            ``` python:
                tina.by_expression('hs',(70,125))
            ```

            * tina.expression.keys() = [ 'happy', 'sad' ]
            * create: `tina hs_happy`, `tina hs_sad`

            See: [[#expressa]], [[#express]]
            """

            for e in self.expression.keys():
                renpy.image(
                    self.id +
                    " " +
                    pose +
                    "_" +
                    e.lower(),
                    self.expressa(
                        pose,
                        xy,
                        e))

        def expressa(self, atag, xy, expimg=None):
            """
            Put Expression to your NPC, inside the game. by compose them.

            Also See: [[#express]]
            """

            res = renpy.get_registered_image(
                self.id + " " + str(atag)).filename
            hw = renpy.image_size(res)
            compo = Composite(hw, (0, 0), res, xy, self.expression[expimg])
            return compo

        def express(self, xy, expimg=None):
            """
            Put Expression to your NPC, inside the game. Using 'screens'.

            ``` python
            init python:
                tina = npc('tina')

            label start:
                show tina standing
                $ tina.express( (70,125), 'smile')
            ```

            * 'tina standing' was the template, a faceless image
            * (70,125) is (x,y) pos relative to the image
            * the size and ATL will be retrieved from 'tina standing'
            * use `None` to remove/hide it: `$ tina.express(None)`
            * the list of expressions in on `tina.expression`

            """

            if xy is None:
                renpy.hide_screen('ramen_npc_expression')
                return False

            t = ''
            s = tuple(renpy.get_showing_tags())
            if self.id in s:
                a = renpy.get_attributes(self.id)
                try:
                    t = " " + str(a[0])
                except BaseException:
                    pass
            else:
                return False

            try:
                res = renpy.get_registered_image(self.id + t).filename
            except BaseException:
                res = False

            if res:
                hw = renpy.image_size(res)

            atl = renpy.get_at_list(self.id + t)

            renpy.show_screen(
                'ramen_npc_expression',
                self.expression[expimg],
                hw,
                xy,
                atl)

            # return res

        def create_sideimage(self, img, temp_img, tag):
            if temp_img:
                compo = Composite(
                    (340, 340),
                    (0, 0), temp_img,
                    (105, 112), At(im.Scale(img, 96, 96, bilinear=True))
                )

                what = tag.replace('phone-', '')
                print self.id + " " + what
                renpy.image(self.id + " " + what, compo)

        def set_phonenum(self, fourdig=None):
            if fourdig is None:
                self.phonenum = "555-" + \
                    str(ramu.random_int(10, 99)) + str(ramu.random_int(10, 99))
            else:
                self.phonenum = "555-" + str(fourdig)

            return self.phonenum

        def play_video(self, name=None, loops=-1):
            if name is not None:
                renpy.movie_cutscene(self.video[name], loops=-1)
                Movie(play=self.video[name], channel='movie')

        def play_audio(self, name=None):
            if name is not None:
                renpy.music.play(self.audio[name])

        def spriteanim(self, name=None, list=None, tick=(0.25)):

            anim = ()
            n = 0

            if name is None:
                print self.__class__.__name__ + ": make_sprite  - misssing name"
                return False

            try:

                if not type(list) == tuple:
                    list = self.sprite.keys()
                for i in list:
                    #                print i
                    try:
                        t = tick[n]
                    except BaseException:
                        t = 0.25
                    anim = anim + (self.sprite[i], t)
                    n += 1

                renpy.image((self.id, name), Animation(*anim))

            except BaseException:
                print 'no sprite'

        def chat_usingjson(
                self,
                key=None,
                use_pose=False,
                file='chat',
                pose=None):
            """
            Start a dialog using JSON file.

            ``` python
            $ monica.chat_usingjson(None,True,'daily','standing')
            ```
            """

            if file is None:
                try:
                    l = sorted(self.json.keys())
                    jfile = self.json[l[0]]
                except BaseException:
                    jfile = False
            else:
                try:
                    jfile = self.json[file]
                except BaseException:
                    jfile = False

            if jfile:

                dialogue = ramu.json_file(jfile)

                if key is None:
                    d = ramu.random_of(dialogue.keys())
                else:
                    d = key

                if use_pose:
                    if pose is None:
                        renpy.show(self.id + ' ' + d)
                    else:
                        renpy.show(self.id + ' ' + pose)

                npc = True
                who = character.__dict__[self.id]

                for line in dialogue[d]:
                    if not npc:
                        if not line == "":
                            character.mc(line)
                        npc = True
                    else:
                        if not line == "":
                            who(line)
                        npc = False

                if use_pose:
                    renpy.hide(self.id)

            else:

                if use_pose:
                    character.narator(
                        self.name + " wasn't interested talking with you.")
                else:
                    character.narator(self.name + " not answering your call.")

        def dialing(self):
            rbc.onphone = True
            renpy.show(
                self.id + " outcall",
                [phone_speak],
                zorder=99,
                layer='above-screens')
            nr = ramen_phone_dering()
            phone_dialing("{size=18}Calling: " + self.name +
                          " (" + self.phonenum + ")...{/size}\n" + nr)

        def onphone(self, state=False):

            # Todo: onphone in state/world

            if state:
                renpy.show(
                    self.id + ' oncall',
                    at_list=[phone_speak],
                    zorder=99,
                    layer='above-screens')
                rbc.onphone = True
            else:
                renpy.hide(self.id + ' oncall', layer='above-screens')
                phone_hangup("(click)")
                rbc.onphone = False

            return rbc.onphone

        def phoneout(self, what=None, jl=None, jsonkey=None):

            self.dialing()

            if jl is not None:

                self.onphone(True)

                if what == 'label' and renpy.has_label(self.id + '_' + jl):
                    renpy.call_in_new_context(self.id + '_' + jl)
                else:
                    if jsonkey is not None:
                        self.chat_usingjson(jsonkey, False, jl)
                    else:
                        self.chat_usingjson(None, False, jl)

                self.onphone(False)

            else:
                phone_status("No answer from " + self.name + ".")

        def phonein(self, what='label', jl=None, jsonkey=None):

            rbc.answered = False

            if jl is not None:

                rbc.onphone = True

                try:
                    renpy.sound.play(
                        PHONE_SFXPATH +
                        "/phone-ring.mp3",
                        channel='sound',
                        loop=3,
                        fadeout=1,
                        fadein=0)
                except BaseException:
                    print "--- The phone_sfxpath/phone-ring can't be found."
                pass

                _window_hide()

                renpy.show(
                    self.id + " incall",
                    [phone_speak],
                    zorder=99,
                    layer='above-screens')
                res = renpy.call_screen('phone_incoming_notice', who=self.id)
                renpy.sound.stop()

                _window_show()

                if res:

                    self.onphone(True)
                    rbc.answered = True

                    if what == 'label' and renpy.has_label(self.id + '_' + jl):
                        renpy.call_in_new_context(self.id + '_' + jl)
                    else:
                        if jsonkey is not None:
                            self.chat_usingjson(jsonkey, False, jl)
                        else:
                            self.chat_usingjson(None, False, jl)

                    self.onphone(False)

                else:
                    phone_status("The call ignored")
                    self.onphone(False)

            else:
                phone_status("You ignoring the call")
                rbc.answered = False

            return rbc.answered
