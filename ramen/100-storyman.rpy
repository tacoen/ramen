init -105 python:

    # Disable if your game is a linear plot
    RAMEN_EPISODES_MENU = True

    class ramen_episodes():
        """Ramen Episodes Module - Function Set"""
        
        def __init__(self):
            """Create and init 'ramenepisode', and set `rast` as the caller object."""
            
            try: ramenepisode
            except: globals()['ramenepisode'] = rn_obj()
            
            ramenepisode._prop = {}
            ramenepisode._prop['thumb'] = ramu.theme_image(THEME_PATH,'story_thumb.png')
            ramenepisode._prop['cover'] = ramu.theme_image(THEME_PATH,'story_cover.png')
    
        def __call__(self,pack=None):
            
            if pack is not None:
            
                try:
                    return ramenepisode.__dict__[pack].__dict__
                except:
                    return None
                    
            else:
                res = []
                for p in ramenepisode.__dict__:
                    if not p.startswith('_'):
                        res.append(p)
                return res
        
        def register(self, id=None, **kwargs):
            """
            Register a story as a module
            
            ``` python
                rast.register('juliet', 
                    title='Romeo and Juliet', 
                    author='Shakespare', 
                    start='juliet_room', 
                    tags='rommance,mf')
            ```
            
            * Will search 'cover.png' and 'thumb.jpg' (webp too) for ramen story screens
            * register will successed if 'juliet_room' (starting label) found, if not then register will be ignored.
            
            """
        
            id = id.strip().lower()
            dir = ramu.fn_getdir()
        
            ramenepisode.__dict__[id] = object()
            obj = ramenepisode.__dict__[id]
            
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
                obj.__dict__['thumb'] = ramenepisode._prop['thumb']

            if renpy.loadable(dir+"/cover.png"):
                obj.__dict__['cover'] = dir+"/cover.png"
            else:
                obj.__dict__['cover'] = ramenepisode._prop['cover']
                
            try: 
                obj.__dict__['hint']
                if obj.__dict__['hint'] > 0:
                    obj.__dict__['score'] = 0
                    obj.__dict__['complete']=False

            except: pass

            try: obj.__dict__['title']
            except: obj.__dict__['title'] =  str(id.title()+" Story")

            try: obj.__dict__['start']
            except: obj.__dict__['start'] =  str('story_'+id)
        
            try: obj.__dict__['end']
            except: obj.__dict__['end'] =  str('story_'+id+"_end")

            if not renpy.has_label(obj.__dict__['end']):
                obj.__dict__['end'] = str('start')

            if not renpy.has_label(obj.__dict__['start']):
                del ramenepisode.__dict__[id]

            rbc.__dict__[id] = {}
            
        def hint(self, id):
            """ For story progression: Return [hint,score] """
            obj = ramenepisode.__dict__[id]

            try: 
                res = []
                res[0] = obj.__dict__['score']
                res[1] = obj.__dict__['hint']
                return res
            except:
                return False
                
        def init(seld,id):
            obj = ramenepisode.__dict__[id]
            globals()['save_name'] = obj.__dict__['title'].strip().replace(" ","_")
        
        def score(self, id,value=1):
            """For story progression: add score until its equal hint value."""

            obj = ramenepisode.__dict__[id]

            try: 
                obj.__dict__['score'] += value
                if obj.__dict__['score'] == obj.__dict__['hint']: obj.__dict__['complete']=True
                if obj.__dict__['score'] < 0:  obj.__dict__['score'] = 0
            except:
                pass

    rast = ramen_episodes()

###################################

style story_vbox:
    xsize (config.screen_width-340) / 3 - 10
    xfill False
    yfill False
    spacing 5

style story_text is gui_text

screen ramen_episode_menu():

    tag menu

    use game_menu(_("Episodes"), scroll="viewport"):

        vpgrid:
            cols 3
            spacing 10
            style_prefix "story"
        
            for s in rast():
                use rast_menuitem(s)
        
screen rast_menuitem(story):
    
    python:
        inf = rast(story)
        thumb = im.Scale(inf['thumb'], style['story_vbox'].xminimum, style['story_vbox'].xminimum * 9/16 )
        
        # Composite(
            # (, style['story_vbox'].yminimum),
            # (0, 0), Solid(gui.choice_background),
        # (0, 0), ramu.theme_image(THEME_PATH, "gui/outline-embose")
    # ), Borders(3, 1, 1, 1), tile=False, xalign=0.5)

    
    vbox:
        spacing 4
        yfill False
        imagebutton:
            action [ Function(rast.init,id=story), Start(inf['start'])]
            idle (thumb)
        
        python:
            try: synopsis = inf['synopsis']
            except: synopsis = 'No synopsis avaliable'

        text inf['title'].title() bold True size 24
        text synopsis size 18
        
        null height 24
        
