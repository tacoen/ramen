screen rai_asset_scene(obj_id, var=None):

    if obj_id is not None:
        python:
            obj = globals()[obj_id]
            sw = config.screen_width - 200 - 32
            sh = config.screen_height
            iw = math.floor(sw / 4)
            ih = math.ceil(iw * 9 / 16)
            cu = False

        null height 8

        vpgrid xminimum sw yminimum sh yoffset 8:
            draggable True
            cols 4
            spacing 16

            for s in sorted(obj.scene.keys()):
                vbox xsize iw yalign 0.0:
                    spacing 8
                    python:
                        ct = ''
                        wot = wo.cond
                        for c in wot:
                            if s.endswith(c.lower()):
                                ct = ' (cs)'

                    imagebutton action Show('rai_scenetest', obj_id=obj_id, tag=s):
                        idle(im.Scale(obj.scene[s], iw, ih))

                    text s + ct size 14

screen rai_scenetest(obj_id, tag):

    layer 'interface'
    zorder 198

    python:

        cond = None
        itag = tag

        try:
            t = tag.split(' ')
            if t[1] in (wo.cond):
                cond = t[1]
                itag = t[0]

        except BaseException:
            pass

        img = ramu.get_sceneimg(cond, obj_id + " " + itag)

        al = []

        try:
            for f in ramu.fn_files(ram._component['ambient']['dir'], "png"):
                fn = ramu.fn_info(f)
                al.append(fn['name'])
        except BaseException:
            ambient = None

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
                textbutton ico('x-square') style 'rai_uico' action Hide('rai_scenetest')
                null height 64
                text repr(img) size 12
                null height 32

                vbox:
                    textbutton 'None' action SetScreenVariable('ambient', None) style 'rai_opt_button'

                    for a in al:
                        textbutton a action SetScreenVariable('ambient', a) style 'rai_opt_button'
                null height 16
