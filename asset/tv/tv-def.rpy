transform slide_pause(s):

    alpha 0.1
    easein 1 alpha 1
    pause float(s) - 2
    easeout 1 alpha 0.1
    repeat

screen tvshow(list, s=3, loop=True):

    $ if s < 3: s = 3
    
    python:

        if s < 3:
            s = 3

        try:
            n
        except BaseException:
            n = 0

        if n == len(list) - 1:
            if not loop:
                renpy.hide_screen('tvshow')

        try:
            img = list[n]

        except BaseException:
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

    imagebutton pos tv.exitarea action Hide('tv'):
        idle(obj.dir+'/btn.png')
        hover(obj.dir+'/btn-hover.png') 
            

    # text repr(locals()['chan'])

    if chan is None:

        vbox xpos tv.ui.x ypos tv.ui.y:

            for c in gal.keys():
                $ cz = c.replace('-random', '')
                $ cz = cz.replace('-show', '')
                textbutton cz action[SetLocalVariable('chan', c)]
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

                playlist = ld[0:length]

                if 'random' in chan:
                    renpy.random.shuffle(playlist)

        use tvshow(playlist, second, loop)
