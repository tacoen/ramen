screen rai_asset_scene(obj_id, var=None):

    if obj_id is not None:
        python:
            obj = globals()[obj_id]
            iw = math.floor((config.screen_width - 200 - 32) / 4)
            ih = math.ceil(iw * 9 / 16)
            cu = False

        null height 8
        vpgrid:

            draggable True
            mousewheel True
            cols 4
            spacing 16
            for s in sorted(obj.scene.keys()):
                vbox xsize iw yalign 0.0 ysize ih + 50:
                    python:
                        ct = ''
                        wot = list(set(wo.sunword + wo.timeword))
                        for c in wot:
                            if s.endswith(c.lower()):
                                ct = ' (cs)'
                                cu = True

                    if cu:
                        imagebutton action Show('rai_scenetest', obj_id=obj_id, tag=s):
                            idle(im.Scale(obj.scene[s], iw, ih))
                    else:
                        add(im.Scale(obj.scene[s], iw, ih))

                    text s + ct size 14

screen rai_scenetest(obj_id, tag):

    layer 'interface'
    zorder 198

    python:
        t = tag.split(' ')

        try:
            t[1]
        except BaseException:
            t[1] = None
            t[0] = tag

        img = ramu.get_sceneimg(t[1], obj_id + " " + t[0])

        al = []

        for f in ramu.fn_files(AMBIENT_PATH, "png"):
            fn = ramu.fn_info(f)
            al.append(fn['name'])

        try:
            ambient
        except BaseException:
            ambient = None

    frame background '#fff' xpos 0 ypos 0 xsize config.screen_width ysize config.screen_height:
        padding(0, 0)

        add(img)
        if ambient is not None:
            use ramen_ambient(ambient)

        frame background "#0004" xsize 200 xpos config.screen_width - 200 ysize config.screen_height:
            padding(8, 8)

            vbox xsize 184:
                textbutton "close" action Hide('rai_scenetest') xalign 1.0 text_size 16
                null height 64
                text repr(img) size 12
                null height 32

                vbox:
                    textbutton 'None' action SetScreenVariable('ambient', None) style 'rai_opt_button'

                    for a in al:
                        textbutton a action SetScreenVariable('ambient', a) style 'rai_opt_button'
                null height 16
