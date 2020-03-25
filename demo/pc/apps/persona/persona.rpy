init -1 python:

    pc.index_update(
        title='Persona',
        hcolor='#993',
        order=2,
    )


screen pc_app_persona():

    vbox:
        style_prefix "phonescreen"
        spacing 10

    hbox:
        vbox:
            text mc.name + " "+ mc.bio['lastname']
            text mc.bio['job']
        vbox:
            text 'ability'
            for a in mc.ability:
                text a.title()
        vbox:
            text 'stats'
            for t in mc.stat.keys():
                python:
                    val = mc.stat[t]
                    try: max=mc.limit[t][1]
                    except: max=mc.limit['stat'][1]                
            
                vbox:
                    hbox xminimum 220:
                        xfill True
                        text t.title() size 12 xalign 0
                        text str(val)+"/"+str(max)  size 12 xalign 1.0 text_align 1.0
                    null height 3
                    bar range max value val style barsty xmaximum xmax                    
