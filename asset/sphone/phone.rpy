init -99 python:

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

    PHONE_SFXPATH = smp.dir + "/audio"

    rbc.smp_apps = None
    rbc.smp_disable = False
