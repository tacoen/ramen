init -200 python:

    ramu = ramen_util()
    
    RAMEN_PATH = ramu.fn_getdir()
    
    wo = WorldTime(
        [2019,1,18,8],
        ['Midnight','Dusk','Morning','Noon','Evening','Night'],
        ['dark','sun1','sun2','sun3','dark']
    )
    
    mc = player(id='mc',
        score=0,
        level=0,
        cash=100,
        pref=0,
        bank=ramu.random_int(9000,9999)
    )

    mc.limit('rel',[0,10])
    mc.limit('stat',[0,10])
    
    mc.data('bio',
        lastname = ramu.random_of(['Small','North','Strong','Smith']),
        job = 'it'
    )
    
    mc.data('stat',
        hygiene = 5,
        energy = 5,
        vital = 5,
        luck = 4
    )
    
    mc.pref= {}
    mc.pref['set']=0
    mc.flags = []
    mc.ability = []
    
    quick_menu = False
    doom = False

    hud_show = False
    hud_disable = False
    hud_set = mc.pref['set']
    
init -100:

    define config.layers = [ 'master', 'transient', 'screens', 'overlay', 'interface' ]

    define character.mc = Character("mc_name", dynamic=True, who_color="#fe3", what_color="#ddd")    
    define character.thou = Character("mc_name", dynamic=True, who_suffix=" ~", who_color="#fe3", what_color="#ddd")    
    define character.anon = Character("anon_name",dynamic=True,who_color="#9cf",what_color="#ccc")   
    
    image ctcon = Text(' ...')

    define character.caption = Character(None, who_color="#ccc", what_color="#fff", 
        what_prefix="{cps=80}", what_suffix="{/cps}")
    
    define character.narator = Character(None, who_color="#ccc", what_color="#eee", 
        what_prefix="{size=-3}{cps=80}", what_suffix="{/cps}{/size}", ctc='ctcon')
        
        
    # game progress
    
    default diff = diff
    default mc = mc
    default doom = doom
    
    default hud_show = hud_show
    default hud_disable = hud_disable

init python:

    # We check here
    
    renpy.free_memory
