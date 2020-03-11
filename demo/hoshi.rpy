init -1 python:
    hoshi = npc(
        id='hoshi',
        name='Hoshiko',
        callname='Hoshi',
        lastname='Liah'
    )
    
    hoshi.by_expression('hs',(70,125))

    renpy.image('hoshi coba', hoshi.expression['upset'] )
    
label ramen_test:

    "pppp"

label demo_npc:

    show hoshi hs at npc_align(0.8,1)
    $ hoshi.express((70,125),ramu.random_of(hoshi.expression.keys()))

    hoshi "My name is [hoshi.fullname]. You can call me [hoshi.callname].{w}\nI am Visual Novel Free Sprite Asset by Liah."
    hoshi "{a=https://liah0227.itch.io/hoshiko}https://liah0227.itch.io/hoshiko{/a}"
    hoshi "You can find my sister and other Liah creations at\n{a=https://itch.io/profile/liah0227}https://itch.io/profile/liah0227{/a}"

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
    
