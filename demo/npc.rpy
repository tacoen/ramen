init -1 python:
    hoshi = npc(
        id='hoshi',
        name='Hoshiko',
        callname='Hoshi',
        lastname='Liah'
    )
    
    hoshi.by_expression('hs',(70,125))

    mc_name = 'Lucas'


label demo_npc:

    show demo red

    show hoshi hs_smile at npc_align(0.8,1)

    hoshi "My name is [hoshi.name]. You can call me [hoshi.callname].{w}"

    label .start:
        menu:
            'intro':
                hoshi "I am Visual Novel Sprite Asset by Liah."
                hoshi "{a=https://liah0227.itch.io/hoshiko}https://liah0227.itch.io/hoshiko{/a}"
                hoshi "You can find other Liah creations at\n{a=https://itch.io/profile/liah0227}https://itch.io/profile/liah0227{/a}"
            
            'non-story dialog':
                'Non-story dialog, is a dialog defined by .json file'
                show hoshi hs_shy
                $ hoshi.chat_usingjson()
            'npc expression':
                jump demo_npc_expression
            'exit':
                jump demo_floor1
    jump .start
    

label demo_npc_expression:

    show hoshi hs at npc_align(0.8,1)
    $ c = 'hs'
    $ hoshi.express(None)
    
    hoshi "Now, I'am faceless, because I want to show you my 'npc expression'"
    hoshi "So, please select:"

    jump .express_choice

    label .back:
        hoshi "See?"
        $ hoshi.express(None)
        jump demo_npc
        
    label .express_choice:
        
        python:
            face =[]

            face.append(('Change Clothes', 'clothes'))

            for e in hoshi.expression.keys():
                face.append((e.title(),e))
            
            face.append(('Exit', 'Return'))
            choice = menu(face)
        
            if choice == 'Return':
                renpy.jump('demo_npc_expression.back')
            elif choice == 'clothes':
                cl = ['hs', 'hw', 'sw']
                
                n = cl.index(c)
                n += 1
                
                if n==len(cl): n=0
                
                c = cl[n]
                
                atl = renpy.get_at_list('hoshi')
                
                hoshi.express(None)
                
                renpy.show('hoshi '+c,at_list=atl)
                renpy.say(character.hoshi,ramu.random_of(["How about this?","this?","You like this?","This one?"]))
            
            else:
                hoshi.express((70,125),choice)
                renpy.say(character.hoshi,"You select: "+ str(choice))
            
        jump .express_choice
    
