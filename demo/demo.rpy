
label demo:

    label .tips:
        tips "See the source, young padawan. See the Source you must."

    label .demomenu:
    
        $ rbc.setdata('scene_map',id='demo',f='floor1',d='floor1')
        
        menu:
            "Phone":
                "Phone demo is inside 'episode-rina'"
                menu:
                    "Incoming Call":
                        jump demo_floor4_d1
                    "Outgoing Call":
                        jump demo_floor3_d2
            "Assets":
                jump demo_asset
            "NPC":
                jump demo_npc
            
            "Scenery":
                jump demo_scenery
                
            "End":
                jump .end
                
        jump .demomenu

    label .end:
        return
                
        