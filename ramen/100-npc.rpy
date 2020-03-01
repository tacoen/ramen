init -99 python:

    class npc(ramen_object):

        def load(self, id=None, **kwargs):

            try:
                self.__dict__['pose']
            except BaseException:
                self.__dict__['pose'] = {}
            try:
                self.color
            except BaseException:
                self.color = ramu.color_random(128, 255)
            try:
                self.wcolor
            except BaseException:
                self.wcolor = "#d0d0d0"
            try:
                self.name
            except BaseException:
                self.name = self.id.title()
            try:
                self.callname
            except BaseException:
                self.callname = self.name
            try:
                self.lastname
            except BaseException:
                self.lastname = ""
            try:
                self.gender
            except BaseException:
                self.gender = "f"
            try:
                self.gender
            except BaseException:
                self.gender = "f"

            setattr(
                character,
                self.id.lower(),
                Character(
                    self.name,
                    who_color=self.color,
                    what_color=self.wcolor,
                    image=self.id))

            self.define_byfile()

            try:
                ramen_dev('npc', self.id)
            except BaseException:
                pass

        def extend(self):

            if isinstance(self.dir, list):
                new_dir = self.dir
            else:
                new_dir = [self.dir]

            new_dir.append(str(ramu.fn_getdir()))

            self.dir = new_dir

            self.define_byfile()

        def get_stat(self):

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

            try:
                mc.rel[self.id]
            except BaseException:
                mc.rel[self.id] = {}

            for k in kwargs:
                mc.rel[self.id][k] = kwargs[k]

        def gain(self, what=None, value=1):

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

            voids = ['profile', 'nsd-chat', 'side']

            files = self.files(self.id + '/pose/') + self.files(self.id + "/")

            if files == []:
                return False

            conte = ['sprite', 'video', 'audio']

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
                    renpy.image((self.id, v), Movie(play=alina.video[v]))
            except BaseException:
                pass

            try:
                del self._files
            except BaseException:
                pass

            pi = ['phone-incall', 'phone-outcall', 'phone-oncall']

            for i in pi:
                temp_img = ramu.theme_image(THEME_PATH, i)
                print i
                print THEME_PATH
                print temp_img

                try:
                    self.create_sideimage(self.profile_pic, temp_img, i)
                except BaseException:
                    pass

        def create_sideimage(self, img, temp_img, tag):
            if temp_img:
                compo = Composite(
                    (340, 340),
                    (0, 0), temp_img,
                    (105, 112), At(im.Scale(img, 96, 96, bilinear=True))
                )

                what = tag.replace('phone-', '')
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
                use_pose=True,
                file=None,
                pose=None):

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

                renpy.sound.play(
                    PHONE_SFXPATH +
                    "/phone-ring.mp3",
                    channel='sound',
                    loop=3,
                    fadeout=1,
                    fadein=0)
                renpy.show(
                    self.id + " incall",
                    [phone_speak],
                    zorder=99,
                    layer='above-screens')
                res = renpy.call_screen('phone_incoming_notice', who=self.id)
                renpy.sound.stop()

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
