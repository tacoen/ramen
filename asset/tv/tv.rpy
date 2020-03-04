init -1 python:


    
    # object must in the object roots
    tv = ramen_object('tv')
    tv.ui_set(
        x=193,
        y=80,
        w=909,
        h=502,
    )

    tv.exitarea=(905, 610)

    tv.gallery('mc','atv')
    tv.gallery('mc','intro')

   
transform slide_pause(s):
    alpha 0.2
    easein 0.25 alpha 1
    pause float(s)-0.5
    easeout 0.25 alpha 0.3
    repeat
    
screen tvshow(list,s=3,loop=True):

    python:

        if s < 3: s = 3
        
        try: n
        except: n = 0

        if n == len(list)-1:
            if not loop: renpy.hide_screen('tvshow')
            
        try: 
            img = list[n]
            
        except:
            n=0
            img = list[n]

    hbox xpos tv.ui.x ypos tv.ui.y:
    
        add (im.Scale(list[n],tv.ui.w,tv.ui.h)) at slide_pause(s)
    
    #text str(locals()['n'])+ repr(len(list))
   
    timer s action [ SetLocalVariable('n',n+1) ] repeat True

screen tv(obj,channel=None,length=None,second=3,loop=True):

    layer 'above-screens'
    add ('asset/tv/tv.png')

    python:
        try: chan
        except: chan=channel
        try: random
        except: random = False
        
    hbox pos tv.exitarea:
        textbutton 'stop' action Hide('tv')

    #text repr(locals()['chan'])

    if chan is None:

        vbox xpos tv.ui.x ypos tv.ui.y:
        
            for c in obj.keys():
                python:
                    if 'random' in c: random = True

                textbutton c action [ SetLocalVariable('chan',c), SetLocalVariable('random',random) ]
                
    else:

        python:
            try: 
                ld = obj[chan][wo.daytime.lower()].values()
            except: 
                ld = sorted(obj[chan].values())

#            if random: renpy.random.shuffle(ld)
            if length is None: length = len(ld)
            
            list = ld            
            
        use tvshow(list,second,loop) 

    
    
label ramen_watch_tv(channel,n=None,s=None,loop=True,Random=True):
    python:
        if s is None: s = 5
        if n is None: n = len(channel)
        if Random: 
            renpy.random.shuffle(channel)
        renpy.show_screen('tvshow',list=channel[0:n],s=s,loop=loop)
        wo.adv(n*0.1)
    
    return

    
label ramen_test:
    #call ramen_watch_tv(tv.mc['atv'][wo.daytime.lower()].values(), None, 3, False)
#    call ramen_watch_tv(sorted(tv.mc['intro'].values()), None, 3, False, False)

    show screen tv(tv.mc)
    window auto

label ne:    
    '1'
    '2'
    '3'
    return
    
