init -105 python:

    ramenstory = rn_obj()
    ramenstory._prop = {}
    ramenstory._prop.thumb = ramu.theme_image(THEME_PATH,'story_thumb.png')
    ramenstory._prop.cover = ramu.theme_image(THEME_PATH,'story_cover.png')
    
    def ramen_story(id=None, **kwargs):
        
        id = id.strip().lower()
        dir = ramu.fn_getdir()
        
        ramenstory.__dict__[id] = object()
        obj = ramenstory.__dict__[id]
            
        for p in kwargs:
        
            if p == 'tags':
                print 'tag!'
                print kwargs[p]
                if isinstance(kwargs[p],(int,str,unicode)): 
                    tags = kwargs[p].split(",")
                    print tags
                obj.__dict__['tags'] = tags
            
            else:
                
                obj.__dict__[p] = kwargs[p]
                
        if renpy.loadable(dir+"/thumb.png"):
           obj.__dict__['thumb'] = dir+"/thumb.png"
        else:
           obj.__dict__['thumb'] = ramenstory._prop.thumb

        if renpy.loadable(dir+"/cover.png"):
            obj.__dict__['cover'] = dir+"/cover.png"
        else:
            obj.__dict__['cover'] = ramenstory._prop.cover
                
        try: obj.__dict__['hint']
        except: obj.__dict__['hint'] = 10

        rbc.__dict__[id] = {}

        try: obj.__dict__['start']
        except: obj.__dict__['start'] = 'story_'+id
        
        try: obj.__dict__['end']
        except: obj.__dict__['end'] = 'story_'+id+"_end"

        if not renpy.has_label(obj.__dict__['end']):
            obj.__dict__['end'] = 'start'

        print obj.__dict__['start']
        
        if not renpy.has_label(obj.__dict__['start']):
            del ramenstory.__dict__[id]
            
        obj.__dict__['complete']=False
        
    ramen_story('gadis',title='Meeting coba',start='kamar_gadis',tags='keras,sadis')
    ramen_story('coba',title='tidak bisa Meeting coba')
    

label ramen_test:

label kamar_gadis:
    "ini kamar gadis"

label story_coba:        

    label .start:
        "i'am module!"

    label .end:
        $ ramenstory.coba.complete=True
        "end"
        