init -89 python:

    pc = ramen_object(id='pc')

    pc.ui_set(
        bgr=pc.dir + "/images/body.png",
        x=0,
        y=0,
        w=480,
        h=720,
        bx=1062,
        by=682,
        icon_size=(70, 70),
        cols=4,
        rows=12,
        area={
            'display': [175, 53, 958, 605, (8, 8, 8, 8)],
            'pbars': [0, 0, 327 - 96 - 16, 48, (8, 8, 8, 8)],
            'minibars': [0, 0, 120, 32, (4, 4, 4, 4)],
        },
        hbar={
            'like': ['#f91', 12],
            'relation': ['#2B2', 12],
            'libido': ['#959', 12],
        },
    )

    pc.index('apps', 'apps', 'rpy')
    
    pc.wallpaper = im.MatrixColor( im.Scale(ramu.random_of(pc.files('images/wp')), style['pc']['area']['display'].xminimum, style['pc']['area']['display'].yminimum), im.matrix.brightness(-.3))

    PC_SFXPATH = pc.dir + "/audio"

