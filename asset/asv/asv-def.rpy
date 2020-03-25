init -10 python:

    RAMEN_DEV = True
    
    if RAMEN_DEV: RD = {}

    ram.component(
        'asv',
        title="Ramen Object Inspector",
        version="1.0",
        author="tacoen",
        author_url='https://github.com/tacoen/ramen',
        desc="Developer only! A debug tools for developer, If you include this in your distributions, this became a cheating tools.",
    )

    ram._component['asv']['dir']

    build.archive("asv", "all")
    build.classify('game/' + ramu.fn_getdir() + '/**', 'asv')

    def ramen_dev(what, item):

        if RAMEN_DEV:
            print '--- RAMEN_DEV: ' + what
            try:
                RD[what].append(item)
            except BaseException:
                RD[what] = []
                RD[what].append(item)

    def ramendev_gui_propCollect(t=None):

        res = {}
        gk = sorted(gui.__dict__.keys())

        if t is None:
            topic = [
                'text',
                'idle',
                'selected',
                'insensitive',
                'muted',
                'accent',
                'hover']
        else:
            if not isinstance(t, list):
                topic = [str(t)]
            else:
                topic = t

        for t in topic:
            try:
                res[t] = gui.__dict__[t + "_properties"]()
            except BaseException:
                for k in gk:
                    if k.startswith(t + "_"):
                        try:
                            res[t]
                        except BaseException:
                            res[t] = {}
                        res[t][k] = gui.__dict__[k]
        return res

    def start_guicollect():
        known_gui = [
            'accent',
            'bar',
            'button',
            'check',
            'choice',
            'confirm',
            'dialogue',
            'file',
            'frame',
            'game',
            'history',
            'hover',
            'hyperlink',
            'idle',
            'insensitive',
            'interface',
            'label',
            'language',
            'main',
            'muted',
            'name',
            'namebox',
            'naration',
            'navigation',
            'notify',
            'nvl',
            'page',
            'pref',
            'quick',
            'radio',
            'scrollbar',
            'selected',
            'skip',
            'slider',
            'slot',
            'text',
            'textbox',
            'title',
            'unscrollable',
            'vbar',
            'vscrollbar',
            'vslider']
        first = [
            'text',
            'idle',
            'selected',
            'insensitive',
            'muted',
            'accent',
            'hover']
        second = []
        for k in known_gui:
            if k not in first:
                second.append(k)

        known_gui = first + second

        return ramendev_gui_propCollect(known_gui)

    gview = 'text'

    def rai_mval(o, v, r=[0, 10]):
#        print o
        o += float(v)
        o = round(o, 2)
        if o <= float(r[0]):
            o = float(r[0])
        if o >= float(r[1]):
            o = float(r[1])

        return o

    def rai_dict_unpack(obj):
        param = obj
        val = ''
        for k in sorted(param.keys()):
            if isinstance(param[k], (int, str, float, unicode)):
                val += k + "=" + str(param[k]) + "\n"
            elif isinstance(param[k], (list)):
                val += k + "=" + repr(param[k]) + "\n"
            else:
                if param[k] is None:
                    val += k + '= None\n'
                else:
                    try:
                        val += k + "=" + rai_dict_unpack(param[k])
                    # except: val += k + "=" +
                    # repr(param[k]).replace('{','<').replace('}','>')
                    except BaseException:
                        val += repr(type(param[k]))
                    #val += repr(param[k]).replace('{','<').replace('}','>')

        return val

screen ramen_ai_menu():

    python:
        try:
            obj_id
        except BaseException:
            obj_id = None

        try:
            tab
        except BaseException:
            tab = None

        try:
            view
        except BaseException:
            view = None

        try:
            var
        except BaseException:
            var = None

    modal True
    style_prefix "rai"
    layer 'interface'
    add Solid('#123')

    key "K_ESCAPE" action Hide('ramen_ai_menu')

    vbox xpos 0 ypos 0:

        use rai_ctlheader(obj_id)

        if tab is not None:
            hbox:
                use rai_menu(tab)
                frame xsize 1 background "#999"

                if obj_id is not None:

                    frame background "#0006":
                        xmaximum config.screen_width - 200
                        xsize config.screen_width - 200
                        ysize config.screen_height - 70
                        padding(8, 8, 8, 8)
                        use rai_routecontent(tab, obj_id, view, var)


screen rai_viewertab(tab):

    hbox:
        for m in tab.keys():
            textbutton m style 'rai_tab' action SetScreenVariable('view', m)
            null width 8

    null height 8

screen rai_routecontent(tab, obj_id, view, var):

    python:
        try:
            route
        except BaseException:
            route = {}

        try:
            route[tab]
        except BaseException:
            route[tab] = {}

        route['scenery'] = {}
        route['scenery']['asset'] = 'rai_asset_scene'
        route['scenery']['param'] = 'rai_param'

        route['npc'] = {}
        route['npc']['asset'] = 'rai_asset_npc'
        route['npc']['param'] = 'rai_param'
        route['npc']['profile'] = 'rai_profile'

        route['events'] = 'rai_event_param'
        #route['events']['param'] = 'rai_event_param'

        err = False

    if isinstance(route[tab], (str, unicode)):
        if renpy.has_screen(route[tab]):
            viewport xsize config.screen_height - 500:
                draggable True
                mousewheel True
                scrollbars "vertical"
                $ renpy.use_screen(route[tab], obj_id=obj_id)
        else:
            $ err = route[tab] + " not here!"

    else:

        if not route[tab] == {}:

            vbox:
                use rai_viewertab(route[tab])

                frame ysize 1 background "#ccc"

                if view is not None:
                    viewport:
                        draggable True
                        mousewheel True
                        scrollbars "vertical"

                        if renpy.has_screen(route[tab][view]):
                            $ renpy.use_screen(route[tab][view], obj_id=obj_id, var=var)
                        else:
                            $ err = route[tab][view] + " not here!"
        else:

            python:
                ps = "rai_" + str(tab) + "_" + str(obj_id)

            if renpy.has_screen(ps):
                $ renpy.use_screen(ps)
            else:
                $ err = ps + " not here!"

    if err:
        hbox yalign 0.5 xalign 0.5:
            text err size 32


screen rai_param(obj_id, var=None):

    if obj_id is not None:

        python:
            obj = globals()[obj_id]
            param = obj.__dict__

        vbox:

            for k in param.keys():
                python:
                    if isinstance(param[k], (int, str, float)):
                        val = str(param[k])
                    elif isinstance(param[k], (list)):
                        val = ", ".join(param[k])
                    else:
                        try:
                            val = rai_dict_unpack(param[k])
                        except BaseException:
                            val = repr(type(param[k]))

                hbox:
                    vbox xsize 200:
                        text k
                    vbox:
                        text val style 'ramen_gui'


screen rai_menu(tab):

    python:
        if tab in RD.keys():
            menus = RD[tab]
        if tab == 'ramen':
            menus = ['ico', 'gui', 'vars','component']
            if 'ramen_documentation' in globals():
                menus.append('compile_md')
        if tab == 'bucket':
            menus = ['param', 'worldtime']

    frame background "#0003" padding(8, 8):

        viewport xsize 184:
            draggable True
            mousewheel True
            scrollbars "vertical"
            style_prefix 'rai_nav'
            vbox xsize 168:

                for m in menus:
                    textbutton m xsize 168 action[SetScreenVariable('obj_id', m), SetLocalVariable('obj_id', m)]
                    null height 4

screen rai_asset_npc(obj_id, var=None):

    if obj_id is not None:

        python:
            obj = globals()[obj_id]
            colect = {}

            try:
                var
            except BaseException:
                var = None

            for s in sorted(obj.pose.keys()):
                xy = renpy.image_size(obj.pose[s])
                w = 'w' + str(xy[0])
                try:
                    colect[w]
                except BaseException:
                    colect[w] = []
                colect[w].append([s, xy])

            nc = 5
            mw = math.floor((config.screen_width - 300) / nc)
            sp = math.ceil((config.screen_width - 300) - (nc * mw))

        hbox:

            frame background "#0003" padding(0, 8, 8, 8):
                viewport xsize 100:
                    draggable True
                    mousewheel True
                    scrollbars "vertical"
                    style_prefix 'rai_nav'

                    vbox xsize 84:

                        text "Width" bold True size 12
                        null height 24

                        for w in sorted(colect.keys()):
                            $ ws = w.replace('w', '')
                            textbutton ws action SetScreenVariable('var', w) xsize 84
                            null height 8

            python:
                try:
                    colect[var]
                except BaseException:
                    var = None

            if var is not None:

                vpgrid:
                    cols int(nc)
                    spacing int(sp)
                    draggable True
                    mousewheel True

                    for s in colect[var]:
                        vbox xsize mw ysize 300 yalign 0.0 yfill False:
                            $ ih = math.ceil(mw * s[1][1] / s[1][0])
                            imagebutton action Show('rai_testpose', img=obj.pose[s[0]]):
                                idle(im.Scale(obj.pose[s[0]], mw, ih))
                            vbox:
                                text s[0] size 14 text_align 0.5
                                text repr(s[1]) size 12 text_align 0.5


screen rai_ctlheader(title=None):

    python:
        if title is None:
            title = "Ramen Object Inspector"
        else:
            title = "Ramen Object Inspector: " + title

        rdtabs = RD.keys()

        rdtabs.append('ramen')
        rdtabs.append('bucket')

    frame xpos 0 ypos 0 background "#0001" xsize config.screen_width:
        style_prefix "rai"
        padding(8, 8, 8, 0)

        vbox:
            hbox xfill True:
                text title bold True color "#fff"
                hbox xalign 1.0:
                    textbutton ico('x-square') style 'rai_uico' action Hide('ramen_ai_menu') 

            hbox:
                null width 200
                for t in rdtabs:
                    textbutton t style 'rai_tab' action[SetScreenVariable('tab', t), SetScreenVariable('view', None), SetScreenVariable('obj_id', None)]
                    null width 8

            frame ysize 1 background "#999"
