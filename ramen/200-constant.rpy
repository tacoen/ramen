init -200 python:

    ramu = ramen_util()
    
    wo = WorldTime(
        [2020,1,18,9],
        ['Midnight','Dusk','Morning','Noon','Evening','Night'],
        ['dark','dim','sun','dim','dark']
    )
    

    mc = player()
    mc._id = "You"
    
init -100:

    define config.layers = [ 'master', 'transient', 'screens', 'overlay', 'interface' ]
    
    default diff = diff                     # worldtime save game progress
    default mc = mc                         # maincharacter as container

    define character.mc = Character("mc_name", dynamic=True, who_color="#fe3", what_color="#ddd")    
    define character.thou = Character("mc_name", dynamic=True, who_suffix=" ~", who_color="#fe3", what_color="#ddd")    
    
    image ctcon = Text(' ...')
    
    define character.narator = Character(None, who_color="#ccc", what_color="#ccc", 
        what_prefix="{size=-3}{cps=80}", what_suffix="{/cps}{/size}", ctc='ctcon')