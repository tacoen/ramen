init python:

    def rt():
        return [
            ramu.random_int(-3,3),
            ramu.random_int(-4,4),
            ramu.random_int(-2,2),
            ramu.random_int(-5,5),
            ramu.random_int(-3,3),
        ]

    rpo = rt()
    rpa = rt()

    c78_cardpath = ramu.fn_getdir()+"/card/"
    renpy.image('c78_table', ramu.fn_getdir()+"/table.webp")

    c78_dealer = npc(
        id='c78_dealer',
        name='[c78_dealer_name]',
        color='#c8ffc8'
    )

    c78_dealer.word={}

    c78_dealer.word['greets'] = [
        'Ready for some action?',
        '[c78_dealer] is in da house!',
        "Hello [mc_name] the gambler.",
        'I smell money...',
        "Nice "+ wo.daytime+" huh...",
        "What a pleasant surprise....",
        'I see poor people, they bet for their lifes',
        "Happy "+wo.weekday+"."
    ]

    c78_dealer.word['win'] = [
        "Like always it should be done.",
        "Ace for me!",
        "I love the smell of money.",
        "Not so easy huh?",
        "Ouh... you look so sad.",
        "Ain't your good "+wo.weekday+". Huh?",
        "So, you pray doesn't count nah?",
        "its my lucky "+ wo.daytime+". ",
    ]

    c78_dealer.word['lost'] = [
        "Sometime you win, anytime you loose.",
        "Sometime you lost, something you win.",
        "Winner doesn't take all.",
        wo.daytime+" glory for you.",
        "Just your lucky "+wo.weekday+".",
        "Praise your lord!"
    ]

    c78_dealer.word['draw'] = [
        "The world was balance, as we draw.",
        "Sometime you lost, something you win. But this time we draw.",
        "Draw!"
    ]

    c78_dealer.word['mc_win'] = [
        "Holly!",
        "Phew!!",
        "Thank you lord..."
    ]

    c78_dealer.word['mc_lost'] = [
        "Damn!",
        "Fuck!!",
        "Ass hole!"
    ]



screen c78_score():
    zorder 78
    vbox xalign .05 yalign .05:
        $ cash = mc.cash
        text "[cash] $" style 'title' size 40
        null height 20
        hbox:
            text "Bet" min_width 100
            text "[bet]"
        null height 20
        hbox:
            text "House" min_width 100
            text "[cpupoint]"
        null height 10
        hbox:
            text "You" min_width 100
            text "[ipoint]"

screen c78a():
    $ sty = 'choice_vbox'
    vbox style sty:

        if btnn<5:
            textbutton "Bet" xalign .5 yalign .5 style 'button' action [
                SetVariable("karta"+str(btnn),
                ramu.random_int(2,11)),
                SetVariable("kartam"+str(btnn),
                renpy.random.choice([100,200,300,400])),
                SetVariable("kart"+str(btnn),
                ramu.random_int(2,11)),
                SetVariable("kartm"+str(btnn),
                renpy.random.choice([100,200,300,400])),
                SetVariable("btnn",btnn+1),
                Jump("cpui")
                ]
        textbutton "Stand" xalign .5 yalign .54 style 'button' action Jump("cstand")

screen c78():

    zorder 50

    vbox xalign .5 yalign .2 xoffset 0:
        add c78_cardpath+str(kart1+kartm1)+".png"
        at transform:
            rotate rpo[0]
    vbox xalign .5 yalign .2 xoffset 60:
        add c78_cardpath+str(kart2+kartm2)+".png"
        at transform:
            rotate rpo[1]
    vbox xalign .5 yalign .2 xoffset 120:
        add c78_cardpath+str(kart3+kartm3)+".png"
        at transform:
            rotate rpo[2]
    vbox xalign .5 yalign .2 xoffset 180:
        add c78_cardpath+str(kart4+kartm4)+".png"
        at transform:
            rotate rpo[3]

    vbox xalign .5 yalign .6 xoffset 0:
        add c78_cardpath+str(karta1+kartam1)+".png"
        at transform:
            rotate rpa[1]
    vbox xalign .5 yalign .6 xoffset 60:
        add c78_cardpath+str(karta2+kartam2)+".png"
        at transform:
            rotate rpa[2]
    vbox xalign .5 yalign .6 xoffset 120:
        add c78_cardpath+str(karta3+kartam3)+".png"
        at transform:
            rotate rpa[3]
    vbox xalign .5 yalign .6 xoffset 180:
        add c78_cardpath+str(karta4+kartam4)+".png"
        at transform:
            rotate rpa[0]

label card78(bet):
    scene c78_table
    $ btnn=2
    $ kart1=ramu.random_int(2,11)
    $ kartm1=renpy.random.choice([100,200,300,400])
    $ karta1=ramu.random_int(2,11)
    $ kartam1=renpy.random.choice([100,200,300,400])
    $ kart2=0
    $ kart3=0
    $ kart4=0
    $ kartm2=0
    $ kartm3=0
    $ kartm4=0
    $ karta2=0
    $ karta3=0
    $ karta4=0
    $ kartam2=0
    $ kartam3=0
    $ kartam4=0
    $ cpupoint=kart1
    $ ipoint=karta1

label bgme:
    show screen c78
    show screen c78a
    call screen c78_score
    jump bgme

label cpui:
    if cpupoint>16:
        if btnn==4:
            $ kart3=0
            $ kartm3=0
        if btnn==5:
            $ kart4=0
            $ kartm4=0
    $ cpupoint=kart1+kart2+kart3+kart4
    $ ipoint=karta1+karta2+karta3+karta4
    if cpupoint>21:
        if kart1==11:
            $ kart1=1
        elif kart2==11:
            $ kart2=1
        elif kart3==11:
            $ kart3=1
        elif kart4==11:
            $ kart4=1
        $ cpupoint=kart1+kart2+kart3+kart4
    if ipoint>21:
        if karta1==11:
            $ karta1=1
        elif karta2==11:
            $ karta2=1
        elif karta3==11:
            $ karta3=1
        elif karta4==11:
            $ karta4=1
        $ ipoint=karta1+karta2+karta3+karta4
    jump bgme

label cstand:
    hide screen c78a
    $ cpupoint=kart1+kart2+kart3+kart4
    $ ipoint=karta1+karta2+karta3+karta4
    if ipoint>21:
        if cpupoint>21:
            call c78_draw pass (bet) from _call_c78_draw
        else:
            call c78_win pass (bet) from _call_c78_win
    elif cpupoint>21:
            call c78_lost pass (bet) from _call_c78_lost
    elif ipoint==cpupoint:
         call c78_draw pass (bet) from _call_c78_draw_1
    elif ipoint>cpupoint:
        if cpupoint<17:
            if kart2==0:
                $ kart2=ramu.random_int(2,11)
                $ kartm2=renpy.random.choice([100,200,300,400])
                jump cstand
            elif kart3==0:
                $ kart3=ramu.random_int(2,11)
                $ kartm3=renpy.random.choice([100,200,300,400])
                jump cstand
            elif kart4==0:
                $ kart4=ramu.random_int(2,11)
                $ kartm4=renpy.random.choice([100,200,300,400])
                jump cstand
        call c78_lost pass (bet) from _call_c78_lost_1
    else:
        call c78_win pass (bet) from _call_c78_win_1
    return
