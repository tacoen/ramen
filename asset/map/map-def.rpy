init -90 python:

    def map_item(obj,id,**kwargs):
        """
        Put map_item into map.
        
        ``` python
        
        init -2 python:
            map_item(world_map,'home',
                title = 'Home',
                ico = 'home',
                x = 210,
                y = 252,
                goto='plex_side'
            )        
        
        label start:
            show screen map_screen(obj)
        
        ```
        
        """
        try: obj.__dict__['item']
        except: obj.__dict__[str('item')]={}

        try: obj.__dict__['item'][str(id).strip().lower()]
        except: obj.__dict__['item'][str(id).strip().lower()]={}
        
        for k in kwargs:
            obj.__dict__['item'][str(id).strip().lower()][k]=str(kwargs[k])
            

style map is default

style map_button_text is gui_text:
    size 18
    color "#fff"
    outlines[(absolute(2), "#000", absolute(0), absolute(0))]

style map_ico is ram_ico
style map_ico_text is ram_ico_text:
    size 20
    outlines[(absolute(6), "#0008", absolute(0), absolute(0))]
    hover_outlines[(absolute(6), "#000C", absolute(0), absolute(0))]

style map_hbox:
    spacing 0

screen map_screen(obj):

    default tt = Tooltip("")
    
    python:
    
        def Mouse():
            import pygame
            return pygame.mouse.get_pos()
    
    layer "above-screens"
    
    style_prefix "map"
    add (shmap.dir+'/map.png') xpos 0 ypos 0
    
    hbox xpos config.screen_width-40 ypos 8:
        textbutton ico('close') style 'map_ico' text_size 32:
            text_color "#f00"
            text_outlines[(absolute(1), "#fff", absolute(0), absolute(0))]        
            action Hide('map_screen')
        
    for o in obj.item.keys():
        $ m = obj.item[o]
        hbox xpos int(m['x']) ypos int(m['y']):
            yoffset -20
            textbutton ico(m['ico']) style 'map_ico':
                text_color Color("#f00") 
                text_hover_color Color("#fff")
                hovered tt.Action(m['title'])
                action [ Hide('map_screen'), Jump(m['goto']) ]
    
            text tt.value style 'map_button_text' 

