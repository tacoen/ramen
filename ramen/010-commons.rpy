init -4 python:

    def ramen_ingamenotify(msg='', icoram=None, who=None):
    
        renpy.show_screen('ingame_notify',msg=msg,icoram=icoram,who=who)


        
# Common ATL and Shared Style

transform p647:
    xpos 647

transform p0:
    xpos 0

## woclock ####################################

screen ramen_woclock():
    hbox xalign 0.9 yalign 0.68:
        text str(wo.clock) style "label" size 32 color "#fff":
            outlines [ (2, gui.textbox_background, absolute(0), absolute(0)) ]
            
    timer 3.0 action Function(renpy.restart_interaction)

## zoom ####################################

transform vertscrolling(sec):
    on show:
        yoffset -720
        linear sec yoffset 0
        pause 2
    on hide:
        linear sec yoffset -360
        alpha 1
        linear 0.3 alpha 0

screen ramen_vsdispay(img, sec=1):
    add (img) at vertscrolling(sec)
    

## scene_mapping #########################################################

screen scene_mapping(obj, scene_id, img=None, overlays=None, shortcut_position=None):

    if not img is None:
        if img.lower() == 'auto':
            $ imgmap = obj.imagemaping(scene_id, None)
        else:
            $ imgmap = obj.imagemaping(scene_id, img)

        imagemap xpos 0 ypos 0:
            ground imgmap['ground']
            hover imgmap['hover']
            for h in imgmap['data']:
                hotspot h[0] action h[1]

    # overlays

    if not overlays is None:
        use _iblays(obj.id, overlays, True)

    # shortcut

    python:
        try:
            shortcuts = obj.short
        except BaseException:
            shortcuts = None

    if not shortcuts is None:
        use scene_shortcut(scene_id, shortcuts, shortcut_position)


## scene_shorcut #######################################################

style shortcut_icon is icoram:
    xalign 0.5

style shortcut_icon_text is icoram:
    size 24
    min_width 30
    text_align 0.5
    outlines[(absolute(2), "#0006", absolute(0), absolute(0))]
    color "#fffc"
    hover_color "#fff"

style shortcut is gui_text

style shortcut_text is default:
    outlines[(absolute(2), "#0006", absolute(0), absolute(0))]
    size 22
    line_leading - 2
    color "#fffc"
    hover_color "#fff"

screen scene_shortcut(scene_id, shorts, position=None):

    python:
        y = config.screen_height * 7 / 8
        x = 32
        s = 48
        n = int(round(y / 48))
        spos = []
        spos.append([x, y])
        for i in range(1, n):
            spos.append([x, y - (i * s)])
        pos = -1

    for s in shorts:

        python:
            show = True
            d = shorts[s]

            if position is None:
                position = d['position']

            try:
                d['hide_on']
            except BaseException:
                d['hide_on'] = None

            try:
                d['show_on']
            except BaseException:
                d['show_on'] = None

            if not d['hide_on'] is None:
                if scene_id in d['hide_on']:
                    show = False
                else:
                    show = True

            if not d['show_on'] is None:

                if scene_id in d['show_on']:
                    show = True
                else:
                    show = False

        if show:

            python:
                pos += 1
                d['pos'] = pos
                if renpy.has_label(d['goto']):
                    Action = Jump(d['goto'])
                else:
                    Action = Null

            if not Action == Null:
                if position == 'right':
                    hbox xalign 1.0 xanchor 1.0 ypos spos[d['pos']][1]:
                        textbutton d['text'] style 'shortcut' action Action
                        null width 6
                        textbutton ico(d['icon']) style 'shortcut_icon' action Action
                        null width 32
                else:
                    hbox xalign 0.0 ypos spos[d['pos']][1]:
                        null width 32
                        textbutton ico(d['icon']) style 'shortcut_icon' action Action
                        null width 6
                        textbutton d['text'] style 'shortcut' action Action


## _overlays #######################################################

screen _iblays(obj_id, data, ontop):

    if ontop:
        zorder 99

    for d in data:
        python:
            if not obj_id is None:
                obj = globals()[obj_id]

            img = ramu.fn_ezy(obj.dir + "/overlays/" + d[0])

            try:
                xy = d[1]
            except BaseException:
                xy = (0, 0)

            try:
                act = d[2]
            except BaseException:
                act = Null

        if img:
            hbox pos xy:
                if act is Null:
                    add img
                else:
                    imagebutton action act:
                        idle img
                        hover im.MatrixColor(img, im.matrix.brightness(0.1))

screen _overlays(obj_id, data, ontop=False):

    if ontop:
        zorder 99

    python:
        if not obj_id is None:
            obj = globals()[obj_id]

    for d in data:
        python:
            img = ramu.fn_ezy(obj.dir + "/overlays/" + d[0])
            xy = d[1]
        if img:
            hbox pos xy:
                add img

screen ingame_notify(msg='', icoram=None, who=None):

    python:
        if icoram is None:
            icoram = 'arrow-up'
            
    zorder 102
    style_prefix "ingame_notify"
    hbox xfill True xalign 1.0 ypos 32 at notify_appear:
        null
        hbox xalign 1.0:
            frame xalign 1.0:
                hbox yalign 0.5:
                    if not who is None:
                        add ramu.get_profilepic(who,(32, 32))
                        null width 8
                    text ico(icoram) style "ingame_notify_icon" min_width 24 text_align 0.5
                    null width 8
                    text "[msg]"
                    null width 8
            null width 32

    timer 3.25 action Hide('ingame_notify')


style ingame_notify_frame:
    padding(8, 8)
    background Frame(Composite(
        (200, 80),
        (0, 0), Solid("#f91d"),
        (0, 0), ramu.theme_image(THEME_PATH, "/gui/outline-b")
    ), Borders(1, 1, 1, 1), tile=False, xalign=0.5)

style ingame_notify_text:
    properties gui.text_properties("notify")
    color "#000"

style ingame_notify_icon is ram_ico:
    color "#000"
    size 24

## special labels ##############################

label after_load:
    stop music fadeout 1.0
    stop sound fadeout 1.0
    $ renpy.free_memory
    $ renpy.block_rollback()
    return

label _ramen_start:

    stop music fadeout 1.0
    stop sound fadeout 1.0
    $ renpy.free_memory

    hide screen _overlays

    python:
        if renpy.has_screen('hud_init'):
            renpy.show_screen('hud_init')
        if renpy.has_label('ramen_test'):
            renpy.jump('ramen_test')

    return
