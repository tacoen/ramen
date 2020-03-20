init -80 python:

    ram.component(
        'tv',
        title = "tv",
        version = "1.0",
        author = "tacoen",
        author_url = 'https://github.com/tacoen/ramen',
        desc = "Ramen Object Gallery Slideshow screen interface",
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
        except:
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
    
    if renpy.loadable(obj.dir + '/body.png'):
        add(obj.dir + '/body.png')
    else:
        add Solid('#000000')

    $ gal = obj.gallery[what]

    python:
        try:
            chan
        except BaseException:
            chan = channel
        try:
            random
        except BaseException:
            random = False

        if renpy.loadable(obj.dir + '/btn.png'): exitbtn = obj.dir + '/btn.png'
        else: exitbtn = Text('ON')

        if renpy.loadable(obj.dir + '/btn-hover.png'): exitbtn_hover = obj.dir + '/btn-hover.png'
        else: exitbtn_hover = Text('OFF')

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
                    ld = sorted(gal[chan][wo.daytime.lower()].values())
                except BaseException:
                    ld = sorted(gal[chan].values())

                if chan.endswith('-show') or length is None:
                    length = len(ld)

                if 'random' in chan:
                    renpy.random.shuffle(playlist)

        use tvshow(playlist, second, loop)
