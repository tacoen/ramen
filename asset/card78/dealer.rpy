define c78_dealer_name = "Oren"

label ramen_test:

label c78_play:

    show c78_dealer idle
    menu:
        "Bet 5":
            $ bet = 5
        "Bet 10":
            $ bet = 10
        "Bet 25":
            $ bet = 25
        "Next time":
            c78_dealer "No Worry..."
            jump tankitchen

    python:
        if mc.cash > bet:
            can_play = True
            mc.cash -= bet
            renpy.call_in_new_context("card78",bet=bet)
        else:
            can_play = False

    if not can_play:
        c78_dealer "Not so fast buddy! You has no $ [bet]"
        jump c78_talk

    jump c78_play

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
    c78_dealer @win "[text]\nYou Lost $ [bet]"
    return

label c78_lost(bet):
    $ text =  ramu.random_of(c78_dealer.word['lost'])
    $ react =  ramu.random_of(c78_dealer.word['mc_win'] )
    $ mc.cash += (bet*2)
    pause 1
    mc '[react]'
    c78_dealer @lost "[text] You Win $ [bet]"
    return

label c78_talk:
    c78_dealer "Next time maybe."
    jump c78_play
    