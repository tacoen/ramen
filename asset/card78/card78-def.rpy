init -78 python:

    ram.component(
        'card78',
        title = "Black Jack",
        version = "1.0",
        author = "tacoen",
        author_url = 'https://github.com/tacoen/ramen',
        desc = "Blackjack minigame",
    )

    build.archive("card78", "all")
    build.classify('game/'+ramu.fn_getdir()+'/**', 'card78')

    c78_cardpath = ramu.fn_getdir()+"/card/"
    renpy.image('c78_table', ramu.fn_getdir()+"/table.webp")


screen c78_score():
    zorder 78
    vbox xalign .05 yalign .05:
        spacing 20
        $ cash = mc.cash
        text "[cash] $" style 'title' size 40
        hbox:
            text "Bet" min_width 100
            text "[bet]"
        hbox:
            text "House" min_width 100
            text "[cpupoint]"
        hbox:
            text "You" min_width 100
            text "[ipoint]"

screen c78_bet():

    style_prefix 'choice'

    vbox:


        if btnn<5:
            textbutton "Bet" xalign .5 yalign .8  action [
                SetVariable("karta"+str(btnn),
                ramu.random_int(2,11)),
                SetVariable("kartam"+str(btnn),
                renpy.random.choice([100,200,300,400])),
                SetVariable("kart"+str(btnn),
                ramu.random_int(2,11)),
                SetVariable("kartm"+str(btnn),
                renpy.random.choice([100,200,300,400])),
                SetVariable("btnn",btnn+1),
                Jump("card78.cpui")
                ]

            $ sword = 'Hold'
        else:
            $ sword = 'Stand'

        textbutton sword xalign .5 yalign .84 action Jump("card78.cstand")

screen c78(rpa,rpo):

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

    python:
        rpo = ramu.random_series(5,-5,5)
        rpa = ramu.random_series(5,-4,4)

    scene c78_table

    python:
        btnn=2
        kart1=ramu.random_int(2,11)
        kartm1=renpy.random.choice([100,200,300,400])
        karta1=ramu.random_int(2,11)
        kartam1=renpy.random.choice([100,200,300,400])
        kart2=0
        kart3=0
        kart4=0
        kartm2=0
        kartm3=0
        kartm4=0
        karta2=0
        karta3=0
        karta4=0
        kartam2=0
        kartam3=0
        kartam4=0
        cpupoint=kart1
        ipoint=karta1

    label .bgme:
        show screen c78(rpo,rpa)
        show screen c78_bet
        call screen c78_score
        jump .bgme

    label .cpui:

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

        jump .bgme

    label .cstand:

        hide screen c78_bet

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
                    jump .cstand
                elif kart3==0:
                    $ kart3=ramu.random_int(2,11)
                    $ kartm3=renpy.random.choice([100,200,300,400])
                    jump .cstand
                elif kart4==0:
                    $ kart4=ramu.random_int(2,11)
                    $ kartm4=renpy.random.choice([100,200,300,400])
                    jump .cstand
            call c78_lost pass (bet) from _call_c78_lost_1
        else:
            call c78_win pass (bet) from _call_c78_win_1
        return

label c78_draw(bet):
    $ text =  ramu.random_of(c78_dealer.word['draw'])
    $ react =  ramu.random_of(c78_dealer.word['mc_win'] )
    $ mc.cash += bet
    pause 1
    mc '[react]'
    c78_dealer @draw "[text]"
    return

label c78_win(bet):
    $ text =  ramu.random_of(c78_dealer.word['win'])
    $ react =  ramu.random_of(c78_dealer.word['mc_lost'] )
    pause 1
    mc '[react]'
    c78_dealer @win "[text]\n{w}You Lost $ [bet]."
    return

label c78_lost(bet):
    $ text =  ramu.random_of(c78_dealer.word['lost'])
    $ react =  ramu.random_of(c78_dealer.word['mc_win'] )
    $ mc.cash += (bet*2)
    pause 1
    mc '[react]'
    c78_dealer @lost "[text]\n{w}You Win $ [bet]."
    return

