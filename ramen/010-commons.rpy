
# Common ATL and Shared Style

transform p647:
    xpos 647

transform p0:
    xpos 0


screen _iblays(obj_id, data, ontop):

    if ontop:
        zorder 99

    for d in data:
        python:
            if not obj_id is None: obj=globals()[obj_id]
            
            img=ramu.fn_ezy(obj.dir +"/overlays/"+d[0])
            
            try: xy=d[1]
            except: xy=(0,0)
            
            try: act=d[2]
            except: act=Null
            
        if img:
            hbox pos xy:
                if act is Null:
                    add img
                else:
                    imagebutton action act:
                        idle img
                        hover im.MatrixColor(img,im.matrix.brightness(0.1))

screen _overlays(obj_id, data, ontop=False):

    if ontop:
        zorder 99

    python:
        if not obj_id is None: obj=globals()[obj_id]

    for d in data:
        python:
            img=ramu.fn_ezy(obj.dir +"/overlays/"+d[0])
            xy=d[1]
        if img:
            hbox pos xy:
                add img

screen ingame_notify(msg='', icoram=None):

    python:
        if icoram is None:
            icoram='arrow-up'
            
    zorder 102
    style_prefix "ingame_notify"
    hbox xfill True xalign 1.0 ypos 32 at notify_appear:
        null
        hbox xalign 1.0:
            frame xalign 1.0:
                hbox yalign 0.5:
                    text ico(icoram) style "ingame_notify_icon" min_width 24 text_align 0.5
                    null width 8
                    text "[msg]"
                    null width 8
            null width 32

    timer 3.25 action Hide('ingame_notify')        
    

style ingame_notify_frame:
    padding (8,8)
    background Frame(Composite(
          (200,80),
           (0,0), Solid("#f91d"),
           (0,0), ramu.theme_image(THEME_PATH,"/gui/outline-b")
        ), Borders(1,1,1,1), tile=False, xalign=0.5)

style ingame_notify_text:
    properties gui.text_properties("notify")
    color "#000"
    
style ingame_notify_icon is ram_ico:
    color "#000"
    size 24



##########

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
        if renpy.has_screen('hud_init'): renpy.show_screen('hud_init')
        if renpy.has_label('ramen_test'): renpy.jump('ramen_test')

    return
    