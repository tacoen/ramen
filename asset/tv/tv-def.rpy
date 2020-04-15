init -80 python:

    ram.component(
        'tv',
        title="tv",
        version="1.0",
        author="tacoen",
        author_url='https://github.com/tacoen/ramen',
        desc="Ramen Object Gallery Slideshow screen interface",
    )

transform slide_pause(s):

    alpha 0.1
    easein 1 alpha 1
    pause float(s) - 2
    easeout 1 alpha 0.1
    repeat

screen tvshow(list, s=3, loop=True):

    $ if s < 3: s = 3

    python:

        try:
            locals()['n']
        except BaseException:
            locals()['n'] = 0

        n = locals()['n']

        if s < 3:
            s = 3

        if n == len(list) - 1:
            if not loop:
                renpy.hide_screen('tvshow')
            else:
                n = 0

        img = list[n]

    hbox xpos tv.ui.x ypos tv.ui.y:

        add(im.Scale(list[n], tv.ui.w, tv.ui.h)) at slide_pause(s)

    timer s action[SetLocalVariable('n', n + 1)] repeat True

screen tv(obj, what, channel=None, length=None, second=3, loop=True):

    key "K_ESCAPE" action Hide('tv')

    layer 'above-screens'

    python:
        tvbgr = ramu.fn_search('tv-body', obj.dir)
        gal = obj.gallery[what]

        try:
            chan
        except BaseException:
            chan = channel
        try:
            random
        except BaseException:
            random = False

        exitbtn = ramu.fn_search('tv-btn', obj.dir)
        if not exitbtn:
            exitbtn = Text('ON')

        exitbtn_hover = ramu.fn_search('tv-btn-hover', obj.dir)
        if not exitbtn_hover:
            exitbtn_hover = Text('OFF')

    if tvbgr:
        add(tvbgr)
    else:
        add Solid('#000000')

    imagebutton pos tv.exitarea action Hide('tv'):
        idle exitbtn
        hover exitbtn_hover

    if chan is None:

        vbox xpos tv.ui.x ypos tv.ui.y:
            spacing 24
            for c in gal.keys():
                $ cz = c.replace('-random', '')
                $ cz = cz.replace('-show', '')
                textbutton cz action[SetLocalVariable('chan', c)] text_size 24 xoffset 24
    else:

        python:

            try:
                playlist

            except BaseException:

                try:
                    playlist = sorted(gal[chan][ramen.daytime.lower()].values())
                except BaseException:
                    playlist = sorted(gal[chan].values())

                if chan.endswith('-show') or length is None:
                    length = len(playlist)

                if 'random' in chan:
                    random.shuffle(playlist)

        use tvshow(playlist, second, loop)
