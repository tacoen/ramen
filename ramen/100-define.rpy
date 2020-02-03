init -200 python:

    ramu = ramen_util()

    RAMEN_PATH = ramu.fn_getdir()

    wo = WorldTime(
        [2019,1,18,8],
        ['Midnight','Dusk','Morning','Noon','Evening','Night'],
        ['dark','sun1','sun2','sun3','dark']
    )

    bucket = object()

    mc = player(id='mc',
        score=0,
        level=0,
        cash=100+ramu.random_int(10,50),
        pref=0,
        bank=9000+ramu.random_int(100,200)
    )

    mc.limit('relation',[0,10])
    mc.limit('stat',[0,20])

    mc.data('rel',
        joana={'relation':8,'like':5}
    )
    mc.data('bio',
        lastname = ramu.random_of(['Small','North','Strong','Smith']),
        job = 'it'
    )

    mc.data('stat',
        hygiene = 5,
        energy = 5,
        vital = 5,
        luck = ramu.random_int(0,7),
        intelec = ramu.random_int(4,7),
    )

    mc.pref= {}
    mc.flags = []
    mc.ability = []

    quick_menu = False
    doom = False

init:

    define config.layers = [ 'master', 'transient', 'screens', 'above-screens', 'overlay', 'interface' ]

    define character.mc = Character("mc_name", dynamic=True, who_color="#fe3", what_color="#ddd")
    define character.thou = Character("mc_name", dynamic=True, who_suffix=" ~", who_color="#fe3",
        what_color="#000",
        what_prefix="{i}", what_suffix="{/i}", what_xpos=100, what_xalign=0.0, what_yalign=0.5,
        window_background=Solid("#fff"),
        window_xsize = gui.dialogue_width+40,
        window_xfill = False,
        window_yalign = 0.9,
        window_ysize = 128,
        )
    define character.anon = Character("anon_name",dynamic=True, who_color=ramu.random_color(128,220), what_color="#ccc")

    image ctcon = Text(' ...')

    define character.caption = Character(None, who_color="#ccc", what_color="#fff",
        what_prefix="{size=-3}{cps=80}", what_suffix="{/cps}{/size}")

    define character.tips = Character(None, who_color="#ccc", what_color="#ff0",
        what_prefix="{size=-3}{cps=80}", what_suffix="{/cps}{/size}",  ctc='ctcon')

    define character.narator = Character(None, who_color="#ccc", what_color="#eee",
        what_prefix="{cps=80}", what_suffix="{/cps}")


    # game progress

    default diff = diff
    default mc = mc
    default doom = doom

### ------------------------------

label _ramen_start:

    stop music fadeout 1.0

    $  renpy.free_memory

    show screen hud_init

    $ if renpy.has_label('ramen_test'): renpy.jump('ramen_test')

    return
