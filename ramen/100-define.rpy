init -200 python:

    ramu=ramen_util()
    RAMEN_PATH=ramu.fn_getdir()

    # Ramen bucket container, a proxydict for renpy storable
    
    _ramen_container= object()
    
    rbc=container()
    rbc.diff=0
    rbc.doom=0
    rbc.cycle=True

    # Default fallback:

    style['hbar']=Style(style.default)
    bcolor="#9AB"
    style['hbar'].thumb=bcolor
    style['hbar'].right_bar=Color(bcolor).opacity(.5)
    style['hbar'].left_bar=Color(bcolor).opacity(.75)
    style['hbar'].ysize=16

init -100 python:

    quick_menu=False

init -2:

    #layers
    
    define config.layers=[ 'master', 'transient', 'screens', 'above-screens', 'overlay', 'interface' ]

    # proxydict

    default _ramen_container= _ramen_container
    default mc=mc

    define character.mc=Character("mc_name", dynamic=True, who_color="#fe3", what_color="#ddd")
    
    # mc from third party views:
    
    $ mc3rd = npc('mc',name='[mc_name]',lastname='[mc.lastname]')
    

    define character.thou=Character("mc_name", dynamic=True, who_suffix=" ~", who_color="#fe3",
        what_color="#000",
        what_prefix="{i}", what_suffix="{/i}", what_xpos=100, what_xalign=0.0, what_yalign=0.5,
        window_background=Solid("#fff"),
        window_xsize=gui.dialogue_width+40,
        window_xfill=False,
        window_yalign=0.9,
        window_ysize=128,
        )

    define character.anon=Character("anon_name",dynamic=True, who_color=ramu.random_color(128,220), what_color="#ccc")

    image ctcon=Text(' ...')

    define character.caption=Character(None, who_color="#ccc", what_color="#fff",
        what_prefix="{size=-3}{cps=80}", what_suffix="{/cps}{/size}")

    define character.tips=Character(None, who_color="#ccc", what_color="#ff0",
        what_prefix="{size=-3}{cps=80}", what_suffix="{/cps}{/size}",  ctc='ctcon')

    define character.narator=Character(None, who_color="#ccc", what_color="#eee",
        what_prefix="{cps=80}", what_suffix="{/cps}")
