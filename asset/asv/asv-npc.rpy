screen rai_profile(obj_id, var=None):

    if obj_id is not None:

        python:
            collect = {}
            collect['bio'] = {}
            collect['sta'] = {}
            obj = globals()[obj_id]

            ppic = ramu.get_profilepic(obj_id, size=(96, 96))

            co = [
                'name',
                'lastname',
                'callname',
                'phonenum',
                'gender',
                'color',
                'wcolor',
                'dir']

            for c in co:
                try:
                    collect['bio'][c] = obj.param[c]
                except BaseException:
                    collect['bio'][c] = None

            try:
                for s in mc.rel[obj_id].keys():
                    collect['sta'][s] = mc.rel[obj_id][s]
            except BaseException:
                pass

        text 'profile' size 48

        hbox yoffset 64:
            add ppic
            null width 24

            vbox:

                for c in collect['sta'].keys():
                    hbox:
                        text c min_width 200
                        text str(collect['sta'][c])
                    null height 8

                null height 8
                frame background "#999" ysize 1
                null height 8

                for c in collect['bio'].keys():
                    hbox:
                        text c min_width 200
                        text str(collect['bio'][c])
                    null height 8


screen rai_asset_npc(obj_id, var=None):

    if obj_id is not None:

        python:
            obj = globals()[obj_id]
            collect = {}

            try:
                var
            except BaseException:
                var = None

            try:
                for s in sorted(obj.pose.keys()):
                    xy = renpy.image_size(obj.pose[s])
                    w = 'w' + str(xy[0])
                    try:
                        collect[w]
                    except BaseException:
                        collect[w] = []
                    collect[w].append([s, xy])
            except BaseException:
                pass

            nc = 4
            mw = math.floor((config.screen_width - 302) / nc)
            sp = math.ceil((config.screen_width - 302) - (nc * mw))

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

                        python:
                            nl = [w.replace('w', '') for w in collect.keys()]
                            nl = list(map(int, nl))

                        for w in sorted(nl):
                            $ ws = "w" + str(w)
                            textbutton str(w) action SetScreenVariable('var', ws) xsize 84
                            null height 8

            python:
                try:
                    collect[var]
                except BaseException:
                    var = None

            if var is not None:

                vpgrid yminimum config.screen_height yoffset 8:
                    cols int(nc)
                    spacing int(sp)
                    draggable True

                    for s in collect[var]:
                        vbox xsize mw ysize 300 yalign 0.0:
                            $ ih = math.ceil(mw * s[1][1] / s[1][0])

                            frame background Frame(ramu.fn_search('outline-w'), Borders(1, 1, 1, 1)):
                                imagebutton action Show('rai_testpose', img=obj.pose[s[0]]):
                                    idle(im.Scale(obj.pose[s[0]], mw, ih))
                            vbox:
                                spacing 4
                                text s[0] size 14 text_align 0.5
                                text repr(s[1]) size 12 text_align 0.5


screen rai_testpose(img):

    zorder 199
    layer 'interface'

    python:
        try:
            xa
        except BaseException:
            xa = 0.5
        try:
            zo
        except BaseException:
            zo = 1.0
        try:
            dec
        except BaseException:
            dec = 0.1
        try:
            ghost
        except BaseException:
            ghost = False

    $ bgr = ramu.fn_ezy(ram._component['asv']['dir'] + "/asvbgr")

    frame background bgr xpos 0 ypos 0 xsize config.screen_width ysize config.screen_height:
        padding(0, 0)

        if locals()['ghost']:
            add(ramu.fn_ezy(ram._component['asv']['dir'] + "/ghost"))

        vbox at npc_align(xa, zo):
            add(img)

        frame background "#0004" xsize 200 xpos config.screen_width - 200 ysize config.screen_height:

            padding(8, 8)

            vbox xsize 184:

                textbutton ico('x-square') style 'rai_uico' action Hide('rai_testpose')

                null height 64

                hbox yalign 0.5 xfill True:
                    style_prefix 'rai_opt'
                    textbutton "0.1" action SetLocalVariable('dec', 0.1)
                    null width 2
                    textbutton "0.05" action SetLocalVariable('dec', 0.05)
                    null width 2
                    textbutton "0.01" action SetLocalVariable('dec', 0.01)
                null height 16

                hbox yalign 0.5:
                    textbutton "ghost" action SetLocalVariable('ghost', ramu.ltoggle(ghost)) style 'rai_opt_button'
                null height 16

                hbox yalign 0.5 xfill True:
                    style_prefix 'rai_ctl'
                    textbutton "-" action SetLocalVariable('xa', rai_mval(xa, -dec, [0.0, 1.0]))
                    textbutton str(locals()['xa']) action SetLocalVariable('xa', 0.5)
                    textbutton "+" action SetLocalVariable('xa', rai_mval(xa, dec, [0.0, 1.0]))
                null height 16

                hbox yalign 0.5 xfill True:
                    style_prefix 'rai_ctl'
                    textbutton "-" action SetLocalVariable('zo', rai_mval(zo, -dec, [0.1, 2.0]))
                    textbutton str(locals()['zo']) action SetLocalVariable('zo', 1.0)
                    textbutton "+" action SetLocalVariable('zo', rai_mval(zo, dec, [0.1, 2.0]))
                null height 16

                text "at npc_align(" + str(locals()['xa']) + "," + str(locals()['zo']) + ")" style 'rai_text' size 16
