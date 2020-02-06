init -99 python:

    pocket = inventory('pocket')
    kondom = item(id='kondom',cost=20,count=3)

    def create_items(inventory, where, prefix, **kwargs ):
        files = ramu.fn_files(where,prefix)
        for f in files:
            fn = ramu.fn_info(f)
            i = item( id= fn['name'], desc=ramu.nicenaming(prefix,fn['name']))
        
            for k in kwargs.keys():
                i.__dict__[k] = kwargs[k]
                if k == 'cost':
                
                    try: kwargs[k][0]
                    except: kwargs[k][0]=10
                    try: kwargs[k][1]
                    except: kwargs[k][1]=20
                    
                    i.__dict__['cost'] = ramu.random_int(kwargs[k][0],kwargs[k][1])

            print i.__dict__
            
            inventory.add(i)
            
    create_items(pocket,'items','z-d_',
        cost=(20,39),
        eatable=True, 
        effect=['stat','energy',2] 
    )
    
    create_items(pocket,'items','v-d_',
        cost=(10,11), 
        eatable=True,
        name='Soft Drinks',
        effect=['stat','energy',1] 
    )

    create_items(pocket,'items','sh-m_',
        cost=(30,50), 
        depend='microwave', 
        effect=['stat','energy',3] 
    )

    pocket.add(kondom)

