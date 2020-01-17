init -200 python:

    ramu = ramen_util()
    
    wo = WorldTime(
        [2020,1,18,9],
        ['Midnight','Dusk','Morning','Noon','Evening','Night'],
        ['dark','dim','sun','dim','dark']
    )
    
    mc = player(id='mc',
        score=0,
        level=0,
        cash=100,
        bank=ramu.random_int(9000,9999)
    )

    mc.limit('rel',[0,10])
    mc.limit('stat',[0,10])
    
    mc.data('stat',
        hygiene = 5,
        vital = 5,
        luck = 4
    )
    
    
    quick_menu = False
    
init -100:

    define config.layers = [ 'master', 'transient', 'screens', 'overlay', 'interface' ]

    define character.mc = Character("mc_name", dynamic=True, who_color="#fe3", what_color="#ddd")    
    define character.thou = Character("mc_name", dynamic=True, who_suffix=" ~", who_color="#fe3", what_color="#ddd")    
    
    image ctcon = Text(' ...')
    
    define character.narator = Character(None, who_color="#ccc", what_color="#ccc", 
        what_prefix="{size=-3}{cps=80}", what_suffix="{/cps}{/size}", ctc='ctcon')
        
    # game progress
    
    default diff = diff
    default mc = mc
