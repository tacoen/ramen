init -200 python:

    ramu = ramen_util()
    RAMEN_PATH = ramu.fn_getdir()

    renpy.music.register_channel('music', 'sfx', 'movie')

    # Ramen bucket container, a proxydict for renpy storable

    _ramen_container = object()

    rbc = container()
    rbc.diff = 0
    rbc.doom = None
    rbc.cycle = True

    # Default fallback:

    style['hbar'] = Style(style.default)
    style['hbar'].thumb = "#9AB"
    style['hbar'].right_bar = Color("#9AB").opacity(.5)
    style['hbar'].left_bar = Color("#9AB").opacity(.75)
    style['hbar'].ysize = 16

init -100 python:

    quick_menu = False

    rbc.anon_name = "She"

    def ramen_nosideimage(tag, argument):
        return ""

    config.self_closing_custom_text_tags["noside"] = ramen_nosideimage

init -2:

    # layers
    define config.layers = ['master', 'transient', 'ambient', 'screens', 'above-screens', 'console', 'overlay', 'interface']

    # A list of layers that are cleared when entering a new context.
    define config.context_clear_layers = ['ambient','console']

    # proxydict
    default _ramen_container = _ramen_container
    default mc = mc

    # mc from third party views:

    define character.thou = Character(
        "mc_name",
        image='thou',
        dynamic=True,
        who_suffix="~",
        who_color="#fe3",
        what_color="#000",
        what_prefix="{i}",
        what_suffix="{/i}",
        what_xpos=100,
        what_xalign=0.0,
        what_yalign=0.5,
        window_background=Solid("#ffffffcc"),
        window_xsize=gui.dialogue_width + 40,
        window_xfill=False,
        window_xalign=0.85,
        window_yalign=0.9,
        window_ysize=150,
    )


    image side thou = Fixed(Image(ramu.safe( ramu.fn_search('side-thou'), 'image'), xalign=1.0, yalign=1.0))


    define character.anon = Character(
        "rbc.anon_name",
        dynamic=True,
        who_color=ramu.random_color(128, 220),
        what_color="#ccc"
    )

    image arrow = Text("  " + ico('arrow-right'), line_leading=8, font=font.ui_ico, color="#fc3", size=16)
    image mouse_l = Text("  " + ico('mouse-l'), line_leading=6, font=font.ui_ico, color="#fffc", size=18)

    define character.caption = Character(
        None,
        window_xalign=0.1,
        window_yalign=0.15,
        window_xsize=config.screen_width / 2,
        window_ysize=None,
        window_padding=(0, 0, 0, 0),
        window_background="#FFCC33DD",
        what_xalign=0.0,
        what_xpos=24,
        what_yalign=0.5,
        what_xsize=(config.screen_width / 2) - 48,
        who_color="#ccc",
        what_color="#000",
        what_prefix="{vspace=24}{size=-1}{cps=80}",
        what_suffix="{/cps}{/size}{vspace=0}",
    )

    define character.tips = Character(
        None,
        window_background="#00000000",
        who_color="#ccc",
        what_color="#ace",
        what_prefix="{size=-3}{cps=80}",
        what_suffix="{/cps}{/size}",
        what_xalign=0.9,
        what_yalign=0.5,
        what_outlines=[(absolute(2), "#0006", absolute(0), absolute(0))],
        ctc='arrow'
    )

    define character.narator = Character(
        None,
        who_color="#ccc",
        what_color="#dd0",
        what_prefix="{cps=80}",
        what_suffix="{/cps}",
        what_xalign=0.0,
        what_xpos=gui.dialogue_xpos,
        what_xsize=gui.dialogue_width,
        ctc='mouse_l'
    )

    define character.emoti = Character(
        None,
        who_color="#ccc",
        what_color="#fff",
        window_background=Solid("#0000"),
        what_bold=True,
        what_prefix="(",
        what_suffix=")",
        what_outlines=[(absolute(2), "#0006", absolute(0), absolute(0))]
    )
