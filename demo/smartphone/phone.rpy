init -89 python:

    smp = ramen_object(id='smp')

    smp.ui_set(
        bgr=smp.dir + "/images/body.png",
        x=0,
        y=0,
        w=480,
        h=720,
        bx=202,
        by=639,
        icon_size=(70, 70),
        cols=4,
        area={
            'display': [64, 88, 327, 551, (8, 8, 8, 8)],
            'pbars': [0, 0, 327 - 96 - 16, 48, (8, 8, 8, 8)],
            'minibars': [0, 0, 120, 32, (4, 4, 4, 4)],
        },
        hbar={
            'like': ['#f91', 12],
            'relation': ['#2B2', 12],
            'libido': ['#959', 12],
        },
    )

    smp.index('apps', 'apps', 'rpy')

    smp.wallpaper = im.Scale(ramu.random_of(smp.files('images/wp')), style['smp']['area']['display'].xminimum, style['smp']['area']['display'].yminimum)
    
    PHONE_SFXPATH = smp.dir + "/audio"
