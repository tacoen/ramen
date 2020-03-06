init python:

    sdemo = scenery(id='sdemo',main='f0')

    sdemo.mazing(
            floor=['f0','f1' ],
            hs = {
                'r1':[(63,228),'goto'],
                'r2':[(655,228),'red_room'],
                'r3':[(909,228),'goto'],
            },
            add = {
                'f0': {
                    'down':[None],
                    'up':[(289,154),'map']
                },
                'f1': {
                    'up':[None],
                    'down':[(462,154),'map'],
                    'r2':[(655,228),'goto'],
                    'r3':[(909,228),'white_room'],
                }
            }
        )


label ramen_test:


label scenery_demo:

    $ rbc.data('scene_map',id='sdemo',f='f0',d='f0')
    scene sdemo f0
    "Welcome to scenery demo"
    jump ramen_scene_map

label sdemo_red_room:
    scene sdemo r2
    "you came here because it's labeled 'sdemo_red_room'"
    jump ramen_scene_map

label white_room:
    scene sdemo r2
    "you came here because it's labeled 'white_room'"    
    "and the door was green"
    jump ramen_scene_map

label sdemo_f0_r1:
    scene sdemo r1
    "You came here because it's labeled 'sdemo_f0_r1'. room r1 on floor f0."
    "after this text, you will go to the first floor."
    jump ramen_scene_map
    
label sdemo_f1_r1:
    
    scene sdemo r3
    "conditional scene"

    label .scs:
        scene sdemo r3
        show screen ramen_woclock
        menu:
            "add 5 hours":
                $ wo.adv(5)
            "add 24 hours":
                $ wo.adv(24)
            "exit":
                hide screen ramen_woclock
                jump ramen_scene_map
        jump .scs
            

label sdemo_f1_r2:
    scene demo r4
    jump ramen_scene_map

    
    