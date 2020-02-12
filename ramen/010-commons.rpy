# Common ATL and Shared Style

transform p647:
    xpos 647

transform p0:
    xpos 0

screen _overlays(obj_id, data, ontop=False):

    zorder 99

    python:
        if not obj_id is None: obj = globals()[obj_id]

    for d in data:
        python:
            img = ramu.fn_ezy(obj.dir +"/overlays/"+d[0])
            xy = d[1]
        if img:
            hbox pos xy:
                add img

screen ingame_notify(msg='',icoram=None):

    zorder 102
    style_prefix "ingame_notify"
    hbox xfill True xalign 1.0 ypos gui.notify_ypos at notify_appear:
        null
        hbox xalign 1.0:
            frame xalign 1.0:
                hbox yalign 0.5:
                    text ico(icoram) style "ingame_notify_icon"
                    text "[msg]"
            null width 16

    timer 3.25 action Hide('ingame_notify')        
    

style ingame_notify_frame:
    padding (8,8)
    background Frame(Composite(
          (200,80),
           (0,0), Solid("#fffd"),
           (0,0), THEME_PATH + "/gui/outline-w.png"
        ), Borders(1,1,1,1), tile=False, xalign=0.5)

style ingame_notify_text:
    properties gui.text_properties("notify")
    color "#000"
    
style ingame_notify_icon is ram_ico:
    color "#000"
    size 24
    