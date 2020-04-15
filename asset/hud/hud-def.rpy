init -95 python:

    ram.component(
        'hud',
        title="Game HUD",
        version="1.0",
        author="tacoen",
        author_url='https://github.com/tacoen/ramen',
        desc="Life Simulation Game HUD",
    )

    # hub object

    hud = ramen_object(id='hud')
    hud.ui_set(
        x=0,
        y=0,
        w=config.screen_width,
        h=config.screen_height / 10,

        sun=['g', 'g', 'a', 'c', 'c', 'd', 'e', 'e', 'e'],
        bgcolor=["#0000", "#fff", "#000c", "#fffc", "#123", "#123c"],
        fgcolor=["#eee", "#111", "#fff", "#000", "#eee", "#fff"],
        winbgcolor=['#333', '#ddd', '#333', '#ddd', '#333', '#333'],
        element={
            'hud': rbc.hud_show,
            'pocket': False,
            'stats': False,
            'legend': False,
            'map': False,
        },
        icons={
            'pocket': ['2', 'wallet', "Pocket", Function(ramen_hud_toggle, what='pocket')],
            'map': ['3', 'map', "Map", 'map', Function(ramen_hud_toggle, what='map')],
        },

        keyb={
            'f6': ["K_F6", Function(ramen_hud_toggle, what='stats')],
            'f8': ["K_F8", Function(ramen_hud_toggle, what='hud')],
            'shift_f8': ["shift_K_F8", Function(ramu.toggle, what='quick_menu')],
            'ctrl_f1': ["ctrl_K_F1", Function(ramen_hud_toggle, what='legend')],
            'f9': ["K_F9", Function(ramen_hud_toggle, what='pocket')],
        },

        hbar={
            'energy': ['#f91', 12],
            'hygiene': ['#2B2', 12],
            'vital': ['#959', 12],
        },

        area={
            'toolbar': [0, 0, config.screen_width, config.screen_height / 10],
            'stats': [16, config.screen_height / 10 + 4, 224, None, (8, 8, 8, 20)],
            'pocket': [
                config.screen_width / 2,
                config.screen_height / 10 + 4,
                config.screen_width / 2 - 16,
                config.screen_height - (config.screen_height / 10 + 4) - 48,
                (8, 8, 8, 8)
            ]
        }
    )

    # why?

    for e in hud.ui.element.keys():
        rbc.hud_element[e] = hud.ui.element[e]
        hud.ui.element[e] = rbc.hud_element[e]

screen hud_toolbar():

    frame background hud.ui.bgcolor[rbc.hud_set] style style['hud']['area']['toolbar']:
        hbox:
            xfill True
            yalign 0.5
            hbox xoffset 48:
                yalign 0.5
                textbutton("{:03d}".format(mc.score)) style "hud_score":
                    action Function(ramen_hud_toggle, what='stats')
                    text_color Color(hud.ui.fgcolor[rbc.hud_set]).opacity(.8)
                    text_hover_color hud.ui.fgcolor[rbc.hud_set]
                hbox xoffset 8 yoffset 8:
                    textbutton hud.ui.sun[ramen.sun] style 'hud_sunico' text_color hud.ui.fgcolor[rbc.hud_set] action Null
                    vbox xoffset 6:
                        text "Day " + str(ramen.dayplay) color Color(hud.ui.fgcolor[rbc.hud_set]).opacity(.8)
                        text("{:03d}".format(mc.cash)) + " $" color hud.ui.fgcolor[rbc.hud_set] size 18
            hbox xalign 1.0 yalign 0.5:
                for m in hud.ui.icons.keys():
                    $ i = hud.ui.icons[m]
                    if m in mc.pref['icons']:
                        textbutton ico(i[1]) action i[3] style 'hud_icon':
                            text_color Color(hud.ui.fgcolor[rbc.hud_set]).opacity(.8)
                            text_hover_color hud.ui.fgcolor[rbc.hud_set]
                    else:
                        textbutton ico(i[1]) action Null style 'hud_icon' text_color "#fff3"
                null width 32

screen hud_status():

    zorder 102

    python:
        ct = {}
        ct['energy'] = ['You are very hungry.', 'Eat something.', 2]
        ct['vital'] = ['You tired.', 'Rest a while.', 4]
        ct['hygiene'] = ['You need a bath.', 'Keep Clean.', 24]

        pp = False
        ctext = ''

        w = False

        for s in hud.ui.hbar.keys():

            if not w:

                if mc.stat[s] > 2 and mc.stat[s] < 5:
                    ctext = ct[s][1]
                    pp = pulse
                    w = s
                    rbc.doom = None
                elif mc.stat[s] <= 2:
                    ctext = ct[s][0]
                    pp = pulse_dying
                    w = s
                    try:
                        if rbc.doom is None:
                            rbc.doom = ramen.time + \
                                datetime.timedelta(hours=ct[s][2])
                    except BaseException:
                        rbc.doom = ramen.time + datetime.timedelta(hours=ct[s][2])

        try:
            tcolor = Color(hud.ui.hbar[w][0]).opacity(.9)
        except BaseException:
            tcolor = Color(hud.ui.fgcolor[w]).opacity(.9)

    if pp:
        hbox xalign 1.0 ypos 80:
            text ico('user') style "hud_sunico" size 24 color tcolor at pp:
                outlines[(2, gui.textbox_background, absolute(0), absolute(0))]
            null width 8
            text ctext color tcolor at pp:
                outlines[(2, gui.textbox_background, absolute(0), absolute(0))]

            null width 32

screen hud_init():

    zorder 190
    tag hud

    if not rbc.hud_disable:

        # add ramu.fn_search('hud-shade')

        key "K_F5" action SetVariable('rbc.hud_set', ramu.cycle(rbc.hud_set, hud.ui.bgcolor))

        if RAMEN_DEV and renpy.has_screen('ramen_ai_menu'):
            key "shift_K_F5"  action  Show('ramen_ai_menu')

        for a in hud.ui.keyb.keys():
            $ k = hud.ui.keyb[a]
            key k[0] action k[1]

        if hud.ui.element['hud']:
            $ hud_tic = ico('chevrons-up')
            if hud.ui.element['legend']:
                use hud_legend
            if hud.ui.element['stats']:
                use hud_stats
            if hud.ui.element['pocket']:
                use inventory_ui('pocket')

            use hud_toolbar
        else:
            python:
                hud_tic = ico('chevrons-down')

        textbutton hud_tic xpos 16 ypos 18 action Function(ramen_hud_toggle, what='hud') style "hud_sunico":
            if hud.ui.element['hud']:
                text_color Color(hud.ui.fgcolor[rbc.hud_set]).opacity(.6)
                text_hover_color hud.ui.fgcolor[rbc.hud_set]
            else:
                text_color "#fff9"
                text_hover_color "#fff"

        use hud_status()

screen hud_stats():

    frame background hud.ui.bgcolor[rbc.hud_set] style style['hud']['area']['stats']:
        vbox:
            use hc_tbar('stats', 'Stats',False)
            vbox:
                box_wrap_spacing 8
                spacing 12
                for topic in sorted(hud.ui.hbar.keys()):
                    use hc_hbar(hud, topic, mc.stat[topic], style['hud']['area']['stats'], hud.ui.fgcolor[rbc.hud_set])

screen hud_legend():
    modal True
    add(Solid("#000d"))
    add(ramu.fn_search('hud-legend'))

init python:
    config.overlay_screens.append("hud_init")
