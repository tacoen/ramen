init -90 python:

    def pc_activated():
        rbc.pc_apps = None
        rbc.pc_who = None
        rbc.pc_disable = False

    ram.component(
        'pc',
        title="Appcontainer: PC UI",
        version="1.0",
        author="tacoen",
        author_url='https://github.com/tacoen/ramen',
        desc="A nice apps container. A Modular approach to your stats, relations, game stats, etc.",
        active_func='pc_activated'
    )

    def pc_comboclose():
        """Hide every pc screens ('pc_'), and clear its `rbc`."""
        rbc.pc_apps = None
        rbc.pc_who = None
        rbc.pc_val = False
        ramu.screen_hideby(prefix='pc_')


screen pc_backbutton(bucket, title=''):
    hbox yalign 0.5 xfill True:
        textbutton ico('arrow-left') style 'ramen_icon':
            text_color "#0009"
            text_hover_color  "#000"
            action SetVariable(bucket, None)
        text title color "#000" size 24 xalign 1.0 line_leading 4
    null height 8

screen pc_ui(apps=None):

    zorder 198

    python:

        if rbc.pc_disable:
            ramu.screen_hideby('pc_')
        else:
            renpy.use_screen('pc_main', apps=apps)

screen pc_main(apps=None):

    python:
        try:
            pc_apps
        except BaseException:
            pc_apps = apps

        iw = pc.ui.icon_size[0]
        ih = pc.ui.icon_size[1]
        cs = 16

    frame background pc.ui.bgr xpos pc.ui.x ypos pc.ui.y xsize pc.ui.w ysize pc.ui.h:

        add(pc.wallpaper) xpos style['pc']['area']['display'].xpos ypos style['pc']['area']['display'].ypos

        imagebutton xpos pc.ui.bx ypos pc.ui.by action Function(pc_comboclose):
            idle(pc.dir + "/images/btn.png")
            hover(pc.dir + "/images/btn-hover.png")

        if rbc.pc_apps is None:

            vpgrid style style['pc']['area']['display'] yoffset 16:
                rows pc.ui.rows
                spacing cs

                for a in sorted(pc.apps.keys()):
                    use pc_item(a)

        else:
            $ a = rbc.pc_apps

            frame style style['pc']['area']['display']:
                ysize 32
                background pc.apps[a]['hcolor']
                hbox yalign 0.5 xfill True xoffset 4:
                    text pc.apps[a]['title'] color "#fff6" size 20 bold True
                    textbutton ico('close') action SetVariable('rbc.pc_apps', None):
                        style "ramen_icon" xsize 32 xalign 1.0
                        text_size 20 text_hover_color "#fff" text_line_leading 4 text_xalign 0.5

            frame yoffset 32:
                background pc.apps[a]['bgr']
                style style['pc']['area']['display']
                ysize style['pc']['area']['display'].yminimum - 32
                padding(0, 0)
                if renpy.has_screen("pc_app_" + a):

                    side "c r":
                        area(
                            8,
                            0,
                            style['pc']['area']['display'].xminimum -
                            8,
                            style['pc']['area']['display'].yminimum)

                        viewport xoffset 8 xsize style['pc']['area']['display'].xminimum - 32 id "pcapp_vp":
                            mousewheel True
                            $ renpy.use_screen("pc_app_" + a)

                        vbar value YScrollValue("pcapp_vp") xsize 8

                else:
                    text "N/A" color "#000" yalign 0.5 xalign 0.5 size 32

screen pc_item(a):

    $ icon = im.Scale(pc.apps[a]['icon'], pc.ui.icon_size[0], pc.ui.icon_size[1])
    vbox:
        imagebutton action SetVariable('rbc.pc_apps', a):
            idle icon
            hover im.MatrixColor(icon, im.matrix.brightness(0.3))
        textbutton pc.apps[a]['title'] action SetVariable('rbc.pc_apps', a):
            style "pc_desktop" text_xalign 0.5 xsize pc.ui.icon_size[0]


style pc_ui is default

style pc_ui_text is ramen_gui:
    size 20
    color "#000"

style pc_ui_button is button

style pc_ui_button_text is ramen_gui:
    size 20
    color "#000"

style pc_desktop is default

style pc_desktop_text is ramen_gui:
    size 14
    color "#fff"
