init -1 python:

    demo = scenery('demo',main='floor1')

    demo.mazing(
            floor=['floor1', 'floor2', 'floor3', 'floor4' ],
            hs = {
                'up':[(713,197),'map'],
                'down':[(557,181),'map'],               
                'd1':[(223,234),'goto'],
                'd2':[(929,265),'goto'],
            },
            add = {
                'floor1': {
                    'down':[None],
                    'd1':[(223,234),'demo_npc'],
                },
                'floor3': {
                    'd2':[(929,265),'blue_room'],
                },
                'floor4': {
                    'up':[None],
                }
            }
        )
    
    demo.shortcut(id='goback',icon='log-out',goto='demo',position='left',text="Exit",show_on=['floor0'])        
        
        
label demo:

    tips "See the source, young padawan. See the Source you must."
   
label demo_scenery:

    scene demo floor1
    
label demo_floor1:    

    $ rbc.setdata('scene_map',id='demo',f='floor1',d='floor1')
    jump ramen_scene_map
    
label demo_floor2:

    scene demo floor2

    "Inside this demo, only this floor has a conditionswitch"
    
    $ rbc.setdata('scene_map',id='demo',f='floor2',d='floor2')
    
    label .scs:
        scene demo floor2
        show screen ramen_woclock
        menu:
            "+1 hours":
                $ wo.adv(1)
            "+6 hours":
                $ wo.adv(+6)
            "continue":
                hide screen ramen_woclock
                jump ramen_scene_map
        jump .scs

label demo_floor4_d2:
    "We gonna jump to blue_room"
    "When you exit from blue_room', You gonna be in floor 3."
    jump blue_room
        
label blue_room:

    scene demo blue
    $ rbc.setdata('scene_map',id='demo',f='floor3',d='floor3')
    "Blue room, this room is on floor 3."
    "but also on floor 4"
    jump ramen_scene_map
    
    
