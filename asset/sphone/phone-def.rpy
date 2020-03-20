init -100 python:

    def smp_comboclose():
        """Hide every phone screens ('smp_'), and clear its `rbc`."""
        rbc.smp_apps = None
        rbc.smp_who = None
        ramu.screen_hideby(prefix='smp_')

    def ramen_phone_dering(nr=False):
        """Make phone ringging in stories. """
        if nr:
            return nr
        else:
            nr = ''
            num = ramu.random_int(2, 4)
            for z in range(num):
                nr += "Ring... {w=2.0}"
            nr += "Ring!"
            return nr

    def ramen_phone_cb_dialing(event, interact=False, **kwargs):
        """Provide callback function for `phone_dialing`."""
        if event == "show_done":
            ramu.sfx("phone-dial", PHONE_SFXPATH, True)
#            renpy.sound.play(PHONE_SFXPATH + "/phone-dial.mp3")
        elif event == "end":
            renpy.sound.stop()

    def ramen_phone_cb_hangup(event, interact=False, **kwargs):
        """Provide callback function for `phone_hangup`."""
        if event == "show_done":
            ramu.sfx("phone-close", PHONE_SFXPATH, True)
#            renpy.sound.play(PHONE_SFXPATH + "/phone-close.mp3")
        elif event == "end":
            renpy.sound.stop()

init offset = -1

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
                                 callback=ramen_phone_cb_dialing,
                                 who_suffix="~",
                                 what_xpos=300,
                                 what_ypos=-40,
                                 what_color="#9CF",
                                 what_size=24,
                                 what_xsize=400,
                                 what_outlines=[(absolute(2), gui.textbox_background, absolute(0), absolute(0))]
                                 )

define phone_hangup = Character("Phone",
                                callback=ramen_phone_cb_hangup,
                                who_suffix="~",
                                what_xpos=300,
                                what_ypos=-40,
                                what_color="#9CF",
                                what_size=24,
                                what_xsize=400,
                                what_outlines=[(absolute(2), gui.textbox_background, absolute(0), absolute(0))]
                                )


style smp_ui is default

style smp_ui_text is ramen_gui:
    size 14
    color "#eee"

transform smp_pullup:
    on show:
        ypos config.screen_height
        easein 0.6 ypos 0
    on hide:
        ypos 0
        alpha 1
        easeout 0.5 ypos config.screen_height, alpha 0

screen smp_backbutton(bucket, title=''):
    hbox yalign 0.5 xfill True:
        textbutton ico('arrow-left') style 'ram_ico':
            text_color "#0009"
            text_hover_color  "#000"
            action SetVariable(bucket, None)
        text title color "#000" size 24 xalign 1.0 line_leading 4
    null height 8

screen smp_ui(apps=None):

    zorder 198

    python:

        if rbc.smp_disable:
            ramu.screen_hideby('smp_')
        else:
            if not rbc.onphone:
                renpy.use_screen('smp_main', apps=apps)

screen smp_main(apps=None):

    python:
        try:
            smp_apps
        except BaseException:
            smp_apps = apps

        iw = smp.ui.icon_size[0]
        ih = smp.ui.icon_size[1]
        cs = round((style['smp']['area']['display'].xminimum / 4) - iw)

    frame background smp.ui.bgr xpos smp.ui.x ypos smp.ui.y xsize smp.ui.w ysize smp.ui.h at smp_pullup:

        add(ramu.fn_ezy(smp.dir + "/images/wp/1")) xpos style['smp']['area']['display'].xpos ypos style['smp']['area']['display'].ypos

        imagebutton xpos smp.ui.bx ypos smp.ui.by action Function(smp_comboclose):
            idle(smp.dir + "/images/btn.png")
            hover(smp.dir + "/images/btn-hover.png")

        text wo.clock color "#fff" style 'ramen_gui' xpos style['smp']['area']['display'].xpos + 8 ypos style['smp']['area']['display'].ypos + 8 size 48

        if rbc.smp_apps is None:

            vpgrid style style['smp']['area']['display'] yoffset style['smp']['area']['display'].yminimum / 2:
                cols smp.ui.cols
                spacing cs

                for a in sorted(smp.apps.keys()):
                    use smp_item(a)

        else:
            $ a = rbc.smp_apps

            frame style style['smp']['area']['display']:
                ysize 32
                background smp.apps[a]['hcolor']
                hbox yalign 0.5 xfill True xoffset 4:
                    text smp.apps[a]['title'] color "#fff6" size 20 bold True
                    textbutton ico('close') action SetVariable('rbc.smp_apps', None):
                        style "ram_ico" xsize 32 xalign 1.0
                        text_size 16 text_hover_color "#fff" text_line_leading 4 text_xalign 0.5

            frame yoffset 32:
                background smp.apps[a]['bgr']
                style style['smp']['area']['display']
                ysize style['smp']['area']['display'].yminimum - 32

                if renpy.has_screen("smp_app_" + a):
                    $ renpy.use_screen("smp_app_" + a)
                else:
                    text "N/A" color "#000" yalign 0.5 xalign 0.5 size 32


screen smp_item(a):

    $ icon = im.Scale(smp.apps[a]['icon'], smp.ui.icon_size[0], smp.ui.icon_size[1])
    vbox:
        imagebutton action SetVariable('rbc.smp_apps', a):
            idle icon
            hover im.MatrixColor(icon, im.matrix.brightness(0.3))
        textbutton smp.apps[a]['title'] action SetVariable('rbc.smp_apps', a):
            style "smp_ui" text_xalign 0.5 xsize smp.ui.icon_size[0]


# For phone calls:


transform phone_ringging:
    rotate 0
    block:
        linear 0.5 rotate 10
        linear 0.5 rotate - 10
        linear 0.5 rotate 0
        repeat

style phone_notif is default

style phone_notif_text is ramen_gui:
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

style phone_btn_text is ramen_gui
style phone_btn_green_text is ramen_gui
style phone_btn_red_text is ramen_gui

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
                    text "V" style 'icoram' at phone_ringging color style['phone_notif_text'].color
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
