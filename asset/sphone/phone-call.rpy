init -102 python:

    def ramen_phone_dering(nr=False):
        if nr:
            return nr
        else:
            nr = ''
            num = ramu.random_int(2, 4)
            for z in range(num):
                nr += "Ring... {w=3.0}"
            nr += "Ring!"
            return nr

    def phone_is_dialing(event, interact=False, **kwargs):

        if event == "show_done":
            renpy.sound.play(PHONE_SFXPATH + "/phone-dial.mp3")
        elif event == "end":
            renpy.sound.stop()

    def phone_is_hangup(event, interact=False, **kwargs):

        if event == "show_done":
            renpy.sound.play(PHONE_SFXPATH + "/phone-close.mp3")
        elif event == "end":
            renpy.sound.stop()

define phone_status = Character("Phone",
                                who_suffix="~",
                                what_xpos=300,
                                what_ypos=-40,
                                what_color="#9CF",
                                what_size=24,
                                what_xsize=400,
                                what_outlines=[(absolute(2), gui.textbox_background, absolute(0), absolute(0))]
                                )

define phone_dialing = Character("Phone",
                                 callback=phone_is_dialing,
                                 who_suffix="~",
                                 what_xpos=300,
                                 what_ypos=-40,
                                 what_color="#9CF",
                                 what_size=24,
                                 what_xsize=400,
                                 what_outlines=[(absolute(2), gui.textbox_background, absolute(0), absolute(0))]
                                 )

define phone_hangup = Character("Phone",
                                callback=phone_is_hangup,
                                who_suffix="~",
                                what_xpos=300,
                                what_ypos=-40,
                                what_color="#9CF",
                                what_size=24,
                                what_xsize=400,
                                what_outlines=[(absolute(2), gui.textbox_background, absolute(0), absolute(0))]
                                )

transform ringging:
    rotate 0
    block:
        linear 0.5 rotate 10
        linear 0.5 rotate - 10
        linear 0.5 rotate 0
        repeat

style phone_notif is default

style phone_notif_text is abel_font:
    color "#333"

style phone_notif_frame:
    background "#fff"
    padding(16, 16)
    yalign 0.8
    xalign 0.0
    xsize config.screen_width * 3 / 4

style phone_notif_name is phone_notif_text:
    size 32
    xoffset 58
    yoffset - 12

style phone_btn:
    padding(8, 8)

style phone_btn_text is abel_font
style phone_btn_green_text is abel_font
style phone_btn_red_text is abel_font

style phone_btn_green is phone_btn:
    background Solid('#090')
    hover_background Solid('#060')

style phone_btn_red is phone_btn:
    background Solid('#900')
    hover_background Solid('#600')

screen phone_incoming_notice(who):
    style_prefix "phone_notif"
    frame:
        hbox xfill True xoffset 320 xsize style['phone_notif_frame'].xminimum - 320:
            vbox xalign 0 yalign 0.5:
                hbox:
                    text "V" style 'icoram' at ringging color style['phone_notif_text'].color
                    text 'Incoming call'  xoffset 8
                $ whoname = globals()[who].name
                text whoname.title() style 'phone_notif_name'
            hbox xalign 1.0 yalign 0.5:
                textbutton "Answer" action[Return(True)] style 'phone_btn_green'
                null width 8
                textbutton "Reject" action[Return(False)] style 'phone_btn_red'
                null width 32
    # the length of sound file
    timer 25 action[Hide('phone_incoming_notice'), Return(False)]
