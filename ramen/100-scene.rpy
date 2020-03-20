init -99 python:

    class scenery(ramen_object):
        """
        **From wikipedia:** Scenery is that which is used as a setting for a theatrical production. Scenery may be just about anything, from a single chair to an elaborately re-created street, no matter how large or how small, whether the item was custom-made or is the genuine item, appropriated for theatrical use.

        See: [[scene example|game-scene]]

        """

        def load(self, id=None, **kwargs):

            scenes = self.files('scene')
            cond = {}
            condition = list(dict.fromkeys(wo.sunword))
            condition2 = list(dict.fromkeys(wo.timeword))

            try:
                self.__dict__['scene']
            except BaseException:
                self.__dict__['scene'] = {}

            try:
                ramen_dev('scenery', self.id)
            except BaseException:
                pass

            for file in sorted(scenes):
                fn = ramu.fn_info(file)

                if " " in fn['name']:
                    fc = fn['name'].split(' ')
                    fn['name'] = fc[0]
                    fn[str('cond')] = fc[1]

                try:
                    self.main
                except BaseException:
                    fn = ramu.fn_info(scenes[0])
                    self.main = fn['name']

                try:
                    cond[fn['name']]
                except KeyError:
                    cond[fn['name']] = ()

                f = file

                for s in condition:
                    if fn['name'] + " " + s in fn['file']:
                        cond[fn['name']] += ("wo.suntime=='" + s + "'", f)
                        scenes.remove(f)
                        self.__dict__['scene'][fn['name'] + " " + s] = f

                for s in condition2:
                    if fn['name'] + " " + s in fn['file']:
                        cond[fn['name']] += ("wo.daytime=='" + s + "'", f)
                        scenes.remove(f)
                        self.__dict__['scene'][fn['name'] + " " + s] = f

                # the default condition

                m1 = fn['name'] + "." + fn['ext']

                if (m1 == fn['file']) and (len(cond[fn['name']]) > 1):
                    cond[fn['name']] += (True, f)
                    scenes.remove(f)
                    self.__dict__['scene'][fn['name']] = f

                # create base on condition

                for cs in cond.keys():
                    renpy.image(self.id + " " + cs, ConditionSwitch(*cond[cs]))

                    if self.main and self.main == cs:
                        renpy.image(self.id, ConditionSwitch(*cond[cs]))

            # create leftover

            for f in scenes:
                fn = ramu.fn_info(f)
                renpy.image(self.id + " " + fn['name'], f)

                self.__dict__['scene'][fn['name']] = f

                if self.main and self.main == fn['name']:
                    renpy.image(self.id, f)

                    self.__dict__['scene']['main'] = f

            return

        def shortcut(self, id=None, **kwargs):

            try:
                self.__dict__['short']
            except BaseException:
                self.__dict__['short'] = {}

            if id is not None:

                try:
                    self.short[id]
                except BaseException:
                    self.short[str(id)] = {}

                for k in kwargs:
                    self.short[id][k] = kwargs[k]

                try:
                    self.short[id]['icon']
                except BaseException:
                    self.short[id][str('icon')] = 'arrow-left'

                try:
                    self.short[id]['goto']
                except BaseException:
                    self.short[id][str('goto')] = str(id).lower()

                try:
                    self.short[id]['text']
                except BaseException:
                    self.short[id][str('text')] = str(id).title()

                try:
                    self.short[id]['hide_on']
                except BaseException:
                    self.short[id][str('hide_on')] = None

                try:
                    self.short[id]['position']
                except BaseException:
                    self.short[id][str('position')] = 'right'

        def mazing(self, **kwargs):
            """
            Maze setup for scenery imagemap

            | Keyword | Mark |
            | ---- | ---- |
            | floor | list of imgname for floor scene |
            | hs | `ways`: [ (x,y) , keyfunc, hscode, img ] |
            | add | `ways`: [ (x,y) , keyfunc, hscode, img ] |

            ``` python:

            mansion = scenery(id='mansion',main='f0')

            mansion.mazing(
                floor=['f0','f1' ],
                hs = {
                    'r1':[(63,228),'goto'],
                    'r2':[(655,228),'red_room'],
                    'r3':[(909,228),'goto'],
                },

            ```

            | Keyword | Mark |
            | ---- | ---- |
            | (x,y) | top,left pixel position for the hotspot image |
            | key/func | map, goto or yours own custom functions |
            | hscode | imgname for hotspot |
            | img | if imgname is not hscode |

            `mazing` will create `obj.map`

            """

            maze = {}
            ahs = {}

            try:
                self.__dict__['map']
            except BaseException:
                self.__dict__['map'] = {}

            for k in kwargs:
                maze[k] = kwargs[k]

            try:
                maze['floor']
            except BaseException:
                maze['floor'] = []

            try:
                for f in maze['add'].keys():
                    if f not in maze['floor']:
                        maze['floor'].append(f)
            except BaseException:
                pass

            for f in sorted(maze['floor']):

                try:
                    ahs[f] = maze['hs'].copy()
                except BaseException:
                    ahs[f] = {}

                try:
                    ahs[f].update(maze['add'][f])
                except BaseException:
                    pass

                self.map[str(f)] = {}

                up = maze['floor'].index(f) + 1
                down = maze['floor'].index(f) - 1

                if up > len(maze['floor']) - 1:
                    up = None
                if down < 0:
                    down = None

                for i in sorted(ahs[f].keys()):

                    hs = ahs[f]

                    try:
                        xy = (hs[i][0][0], hs[i][0][1])
                    except BaseException:
                        xy = False

                    try:
                        func = str(hs[i][1])
                    except BaseException:
                        func = 'goto'

                    dest = i

                    if func == 'map':
                        dest = None
                        if "up" in i:
                            if up is not None:
                                dest = maze['floor'][up]
                        if "down" in i:
                            if down is not None:
                                dest = maze['floor'][down]
                    else:
                        dest = i

                    try:
                        img = hs[i][2]
                    except BaseException:
                        img = i

                    if not renpy.has_label(self.id + "_" + f + "_" + dest):

                        try:
                            if self.doors[f][dest] is not None:
                                func = 'meet'
                                dest = self.doors[f][dest].lower()

                        except BaseException:
                            pass

                    if dest is not None and xy:
                        self.map[f][str(i)] = [xy, str(
                            func), str(dest), str(img)]

            return self.map

        def scene_call(self, what, id, f, d):
            """ See: [imagemaping](#imagemaping) """

            rbc.setdata('scene_map', id=str(id), f=str(f), d=str(d))
            renpy.jump(what)
            # renpy.call_in_new_context(what,obj_id=obj_id)

        def imagemaping(self, floor, bgr=None):
            """
            Create and return imagemap for `scene_mapping` (screen) from `obj.map`

            Ref: https://www.renpy.org/doc/html/screens.html#imagemap-statements

            The action will be called in using this order

              - True if label `obj_floor_hscode` exist
              - True if label `obj_hscode` exist
              - True if label `hscode` exist
              - True if label `obj_floor_keyfunc` exist
              - True if label `obj_keyfunc` exist
              - True if label `keyfunc` exist
              - True if label `ramen_scene_keyfunc` exist
              - False

            """

            if not bgr or bgr is None:
                bgr = ramu.get_sceneimg()

            img = {}
            img['ground'] = bgr
            gimg = tuple()
            himg = tuple()
            imgdata = []
            shortcuts = []
            gimg = ((0, 0), bgr)
            himg = ((0, 0), Solid('#fff0'))

            ways = self.map[floor]

            for k in sorted(ways.keys()):

                w = ways[k]

                action = False
                hover = False
                xy = w[0]

                if xy is not None:

                    # w
                    # 0 xy
                    # 1 key/func
                    # 2 hs code
                    # 3 img

                    if renpy.has_label(self.id + '_' + floor + "_" + w[2]):
                        action = Function(
                            self.scene_call,
                            what=self.id + '_' + floor + "_" + w[2],
                            id=self.id,
                            f=floor,
                            d=w[2])
                    elif renpy.has_label(self.id + '_' + w[2]):
                        action = Function(
                            self.scene_call,
                            what=self.id + '_' + w[2],
                            id=self.id,
                            f=floor,
                            d=floor)
                    elif renpy.has_label(w[2]):
                        action = Function(
                            self.scene_call,
                            what=w[2],
                            id=self.id,
                            f=floor,
                            d=w[2])
                    elif renpy.has_label(self.id + '_' + floor + "_" + w[1]):
                        action = Function(
                            self.scene_call,
                            what=self.id + '_' + floor + "_" + w[1],
                            id=self.id,
                            f=floor,
                            d=w[2])
                    elif renpy.has_label(self.id + '_' + w[1]):
                        action = Function(
                            self.scene_call,
                            what=self.id + '_' + w[1],
                            id=self.id,
                            f=floor,
                            d=w[2])
                    elif renpy.has_label(w[1]):
                        action = Function(
                            self.scene_call,
                            what=w[1],
                            id=self.id,
                            f=floor,
                            d=w[2])
                    elif renpy.has_label('ramen_scene_' + w[1]):
                        action = Function(
                            self.scene_call,
                            what='ramen_scene_' +
                            w[1],
                            id=self.id,
                            f=floor,
                            d=w[2])

                    else:
                        action = False

                    file = ramu.fn_ezy(self.dir + "/hs/" + w[3])

                    if file:
                        ground = file
                        area = xy + renpy.image_size(ground)
                        hover = im.MatrixColor(
                            ground, im.matrix.brightness(0.1))
                    else:
                        ground = False
                        area = False

                    file = ramu.fn_ezy(self.dir + "/hs/" + w[3] + "-hover")
                    if file:
                        hover = file
                        if not area:
                            area = xy + renpy.image_size(hover)
                        if not ground:
                            #ground=RAMEN_PATH + "/img/blank.png"
                            ground = Solid('#0000')

                    if hover:
                        himg = himg + (xy, hover)
                    if ground:
                        gimg = gimg + (xy, ground)
                    if area:
                        imgdata.append([area, action])

                    img['ground'] = LiveComposite((1280, 720), *gimg)
                    img['hover'] = LiveComposite((1280, 720), *himg)
                    img['data'] = imgdata

            return img

        def random_image(self, prefix, scope=None):
            if scope is None:
                scope = ''
            imgs = self.files('overlays/' + scope)
            res = []
            for file in imgs:
                fn = ramu.fn_info(file)
                if fn['file'].startswith(str(prefix)):
                    res.append(fn['path'] + "/" + fn['name'])

            return ramu.random_of(res)

label ramen_scene_map:

    window hide
    hide screen scene_mapping

    python:
        obj_id = rbc.scene_map['id']
        f = rbc.scene_map['f']
        d = rbc.scene_map['d']
        obj = globals()[obj_id]

        # sometimes stupidos does it better:

        try:
            obj.map[d]
            w = d
        except BaseException:
            w = f

        renpy.scene()
        renpy.show(obj_id + " " + w)
        renpy.with_statement(dissolve)

    call screen scene_mapping(obj, w, ramu.get_sceneimg())

    return

label ramen_scene_goto:

    hide screen scene_mapping

    python:
        obj_id = rbc.scene_map['id']
        f = rbc.scene_map['f']
        d = rbc.scene_map['d']
        obj = globals()[obj_id]
        doors = []
        target = ['knock', 'peek', 'key']

        for t in target:
            if renpy.has_label(obj_id + "_" + f + "_" + d + "_" + t):
                if t == "key":
                    tn = "Open (key)"
                else:
                    tn = t
                doors.append((tn, obj_id + "_" + f + "_" + d + "_" + t))

        if not doors == []:
            doors.append(('Exit', 'Return'))

            renpy.scene()
            renpy.show(obj_id + " door")
            renpy.with_statement(dissolve)

            choice = menu(doors)

            if choice == 'Return':
                renpy.jump('ramen_scene_goto.back')
            else:
                renpy.jump(choice)

    "Nothing responding..."

    label .back:
        python:
            rbc.setdata('scene_map', f=d, d=f, id=obj_id)
            renpy.jump('ramen_scene_map')

    return
