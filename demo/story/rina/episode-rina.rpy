init -1 python:

    rast.register('rina_qna',
        title='Rina qna',
        start='rina_qna', 
        synopsis='Question and answer with Rina',
        tags='demo,npc'
    )

    rina = npc(
        id='rina',
        name='Rina',
        callname='Rin',
        lastname='Liah'
    )
    
    rina.by_expression('0',(223,181))    
   
label rina_qna:

    show demo red
    show rina at npc_align(0.8,1)
    with dissolve
    mc 'Uh, Hi!'
    rina @0_happy "I'm happy to meet you..."
    rina "You came by selecting episode?"
    mc "Yes. I was."
    rina @0_blush "Great!"
    rina "It's a first step to understand what is Episodes in Ramen"
    mc "I think i can create a side-story in renpy."
    rina "Yes, every story can have it's own start and ending."
    label .end:

        rina "Bye!"
        return


label rina_phonedemo:

    rina "[mc_name]?! Hello?"
    mc "Yeah?"
    rina "I'm calling your from demo_floor4_d1"
    mc "What do you meant?"
    rina "Take your time, and see the source code."
    mc "ok, I will do that."
    rina "See you."

    return

label demo_floor4_d1:
    
    show demo red
    $ rina.phonein('label','phonedemo')
    "Well?"
    jump ramen_scene_map
            
