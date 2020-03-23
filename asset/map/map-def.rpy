init -90 python:

    ram.component(
        'map',
        title="Interactive Map",
        version="1.0",
        author="tacoen",
        author_url='https://github.com/tacoen/ramen',
        desc="Put Interative maps screens into yourgames.",
    )
    
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

        cont={}
        
        for k in kwargs:
            cont[k]=str(kwargs[k])
            
        try: cont['ico']
        except: cont['ico']='pin'

        try: cont['color']
        except: cont['color']='#119'
        
        if int(cont['x']) < int(obj.prop['xmin']): cont['x'] = obj.prop['xmin'] 
        if int(cont['y']) < int(obj.prop['ymin']): cont['y'] = obj.prop['ymin'] 
        if int(cont['x']) > int(obj.prop['xmax']): cont['x'] = obj.prop['xmax'] 
        if int(cont['y']) > int(obj.prop['ymax']): cont['y'] = obj.prop['ymax'] 
        
        obj.__dict__['item'][str(id).strip().lower()] = cont
        
    def map_goto(label,dist=0):
    
        time_cost = dist * (1/60)
        wo.adv(time_cost)
        renpy.jump(label)

style map is default

style map_button_text is gui_text:
    size 18
    color "#fff"
    outlines[(absolute(2), "#000", absolute(0), absolute(0))]

style map_ico is ramen_icon
style map_ico_text is ramen_icon_text:
    size 20
    outlines[(absolute(6), "#fffc", absolute(0), absolute(0))]
    hover_outlines[(absolute(6), "#fff", absolute(0), absolute(0))]

style map_hbox:
    spacing 0

screen map_screen(obj,current_pos=(210,250)):
    
    layer "above-screens"
    
    style_prefix "map"
    add (shmap.dir+'/map.png') xpos 0 ypos 0
    
    hbox xpos config.screen_width-40 ypos 8:
        textbutton ico('close') style 'map_ico' text_size 32:
            text_color "#ccc"
            text_outlines[(absolute(0), "#0000", absolute(0), absolute(0))]
            text_hover_color "#fff"
            action Hide('map_screen')
        
    for o in obj.item.keys():
        
        $ m = obj.item[o]
        $ td = absolute(int(m['x'])-current_pos[0]) + absolute(int(m['y'])-current_pos[1]) 
        
        hbox xpos int(m['x']) ypos int(m['y']):
            yoffset -20
            textbutton ico(m['ico']) style 'map_ico':
                text_color Color(m['color']) 
                text_hover_color Color("#000")
                tooltip (o,m['title'])
                action [ Hide('map_screen'), Function(map_goto,label=m['goto'],dist=td) ]
    
            $ tooltip = GetTooltip()
            
            if tooltip:
                
                python:
                    if tooltip[0] == o: tt = tooltip[1]
                    else: tt = ''
                
                if int(m['x']) > 1000:
                    vbox xanchor 130:
                        text "[tt]" style 'map_button_text' xalign 1.0 min_width 130
                else:
                    vbox:
                        text "[tt]" style 'map_button_text' 

