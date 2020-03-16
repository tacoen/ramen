init -77 python:

    c78_dealer = npc(
        id='c78_dealer',
        name='[c78_dealer_name]',
        color='#c8ffc8',
        window_left_padding=100,
    )

    c78_dealer_name = "Oren"

    c78_dealer.word={}

    c78_dealer.word['greets'] = [
        'Well...',
        'Sure.',
        'Ready?',
        'Dealer in the house!',
        "Fine! "+mc_name+" the gambler!",
        'I smell money...',
        'I smell my winning aroma...',
        "Nice "+ wo.daytime+" huh...",
        "What a pleasant surprise....",
        'I see poor people, they bet for their lifes',
        "Look like a happy "+wo.weekday+" for me."
    ]

    c78_dealer.word['bye'] = [
        'See you next time, buddy.',
        "Thanks for playing, [mc_name].",
        "Have a nice "+ wo.daytime+", buddy."
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


label c78_play:

    scene c78_table
    
    $ text = ramu.random_of(c78_dealer.word['greets'])

    menu:

        "Bet 5":
            c78_dealer @idle "[text]"
            $ bet = 5
        "Bet 10":
            c78_dealer @idle "[text]"
            $ bet = 10
        "Bet 25":
            c78_dealer @idle "[text]"
            $ bet = 25
        "Next time":
            c78_dealer @idle "No Worry..."
            jump .end

    python:
        if mc.cash > bet:
            can_play = True
            mc.cash -= bet
            renpy.call_in_new_context("card78",bet=bet)
        else:
            can_play = False

    if not can_play:
        c78_dealer @idle "Not so fast buddy! You has no $ [bet]"
        jump .end

    jump c78_play

    label .end:
        c78_dealer @idle "Next time maybe."
