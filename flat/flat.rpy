init python:

    def lead(f,d=None):
        print f
        print d
        
    flat = scenery(id='flat',main='f0')

    flat.maze = {
        'floor':['f0','f1','f2','f3','f4','f5','f6' ],
        'hs': {
            'stair-down':[318,167,'lead'],
            'stair-up':[369,159,'lead'],
            'elevator':[457,264,'elevator'],
            'terrace':[493,292],
            'r1':[547,313],
            'r2':[690,313],
            'r3':[709,292],
            'r4':[785,184],
            'cbox':[962,239,'cbox'],
        }
    }
    
    flat.maze['way'] = {}
    
    for f in sorted(flat.maze['floor']):
    
        up =  flat.maze['floor'].index(f)+1
        down = flat.maze['floor'].index(f)-1

        try: flat.maze['way'][f]
        except: flat.maze['way'][f]={}

        for i in sorted(flat.maze['hs'].keys()):
            try: flat.maze['way'][f][i]
            except: flat.maze['way'][f][i]=[]

            try:
                func = flat.maze['hs'][i][2]
                if "up" in i:
                    if up == len(flat.maze['floor']): up = None
                    flat.maze['way'][f][i]=[func, up]
                if 'down' in i:
                    if down < 0: down = None
                    flat.maze['way'][f][i]=[func, down]
                else:
                    flat.maze['way'][f][i]=[func, f]
                
            except:
                flat.maze['way'][f][i] = ['door',f,i]

screen scene_imagemap(img):

    imagemap xpos 0 ypos 0:
        ground img['ground']
        hover img['hover']
        for h in img['data']:
           $ print h
           hotspot h[0] action h[1]    

label ramen_test:
    scene flat f2
    python:
        flat_map = flat.imagemaping('f2',ramu.get_sceneimg())
        
    show screen scene_imagemap(flat_map)

    "work?"
