init -9 python:

    cboxpuzzle_path = ramu.fn_getdir()

    def rp_vars():
        return {
            'd_var': ramu.random_int(0,5),
            'a_var': ramu.random_int(0,5),
            'b':str(ramu.random_int(5,9)),
            'c':str(ramu.random_int(1,5)),
            'res':False
        }

label cboxgame:

    python:
    
        rp={
            'r1': rp_vars(),
            'r2': rp_vars(),
            'r3': rp_vars(),
            'r4': rp_vars()
        }
        
    show screen cboxgame
    
    return

screen cboxgame():
    
    $ x = config.screen_width/2 - (600/2)
    
    hbox xpos x ypos 125:
        use rowpuzzle('r1')
    hbox xpos x ypos 225:
        use rowpuzzle('r2')
    hbox xpos x ypos 325:
        use rowpuzzle('r3')
    hbox xpos x ypos 425:
        use rowpuzzle('r4')
    
    python:
        if rp['r1']['res']==True and rp['r2']['res']==True and rp['r3']['res']==True and rp['r4']['res']==True:
            fine = True
        else:
            fine = False
        
    if fine == True:
        timer 2.0 action Hide('cboxgame') 
    
screen rowpuzzle(vars='r1'):

    frame xsize 600 ysize 100:
        background Frame(cboxpuzzle_path+"/img/base.png",Borders(0,0,0,0),tile=True)
        padding (0,0,0,0)
        
        python:
            try: a_var
            except: a_var = rp[vars]['a_var']
            try: d_var
            except: d_var = rp[vars]['d_var']
            try: b
            except: b = rp[vars]['b']
            try: c
            except: c = rp[vars]['c']
            
            va = ['base','a1','a2','a3','a4','a5']
            vd = ['base','d0','d1','d2','d3','d4']

            res = "off"
            
            if a_var > len(va)-1: a_var = 0
            if d_var > len(vd)-1: d_var = 0
            
            a_ev = 10-int(b)
            d_ev = 5-int(c)+1
            
            if a_var == a_ev and d_ev == d_var:
                res = "on"

        #vbox xpos 700 ypos 100:
        #    text str(a_var)  + " - e:" + str(a_ev) + " - img:" + va[a_var] color "#000"
        #    text str(d_var)  + " - e:" + str(d_ev) + " - img:" + vd[d_var] color "#000"
            
        vpgrid cols 6 rows 1:
            spacing 0
            draggable True
            mousewheel True
            add (cboxpuzzle_path+"/img/start.png")
            imagebutton: 
                idle cboxpuzzle_path+"/img/"+va[a_var]+".png"
                action SetLocalVariable('a_var',a_var+1)
            add (cboxpuzzle_path+"/img/b"+b+".png")
            add (cboxpuzzle_path+"/img/c"+c+".png")
            imagebutton: 
                idle cboxpuzzle_path+"/img/"+vd[d_var]+".png"
                action SetLocalVariable('d_var',d_var+1)
            add (cboxpuzzle_path+"/img/"+res+".png") xalign 1.0
            
        python:
            if res == "on": rp[vars]['res']=True
            else: rp[vars]['res']=False
