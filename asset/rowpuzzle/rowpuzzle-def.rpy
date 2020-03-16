init -9 python:

    ram.component(
        'rowpuzzle',
        title = "Row Puzzle",
        version = "1.0",
        author = "tacoen",
        author_url = 'https://github.com/tacoen/ramen',
        desc = "Minigame: Row Puzzle",
    )

    build.archive("mg_rowpuzzle", "all")
    build.classify('game/' + ramu.fn_getdir() + '/**', 'mg_rowpuzzle')
    
    cpuzzle_path=ramu.fn_getdir()

    def cpuzzle_vars():
        return {
            'a': ramu.random_int(1,9),
            'b': ramu.random_int(1,9),
            'c': ramu.random_int(1,9),
            'd': ramu.random_int(1,9),
            'e': ramu.random_int(1,9),
            'f': ramu.random_int(1,9),
            'res':True
        }

label cable_puzzle(broke=[]):

    # need to reset vars

    python:

        renpy.hide_screen('cable_puzzle')

        rp={
            'r1': cpuzzle_vars(),
            'r2': cpuzzle_vars(),
            'r3': cpuzzle_vars(),
            'r4': cpuzzle_vars(),
            'co': cpuzzle_vars()
        }

        if not broke == []:
            for b in broke:
                rp[b]['res']=False

        renpy.show_screen('cable_puzzle',rp=rp)

    return

screen cable_puzzle(rp):

    python:
        x=config.screen_width/2 - (400/2)
        ys=40
        fine=True

    for r in sorted(rp.keys()):
        $ ys += 80
        hbox xpos x ypos ys:
            use rowpuzzle( r )

    python:
        for r in rp.keys():
            if rp[r]['res']==False: fine=False

    if fine == True:
        timer 2.0 action Hide('cable_puzzle')

screen rowpuzzle(vars='co'):

    frame xsize 400 ysize 80:
        background Frame(cpuzzle_path+"/img/base.png",Borders(0,0,0,0),tile=True)
        padding (0,0,0,0)

        python:

            try: a
            except: a=rp[vars]['a']
            try: b
            except: b=rp[vars]['b']
            try: c
            except: c=rp[vars]['c']
            try: d
            except: d=rp[vars]['d']
            try: e
            except: d=rp[vars]['e']
            try: f
            except: f=rp[vars]['f']
            try: res
            except: res=rp[vars]['res']

            pz={}

            if a > 9: a=1
            if b > 9: b=1
            if c > 9: c=1
            if d > 9: d=1
            if e > 9: e=1
            if f > 9: f=1

            b_ev=10-int(a)
            c_ev=10-int(d)
            e_ev=10-int(f)

            if res==True:
                c=c_ev
                b=b_ev
                e=e_ev

            if res==False:
                res="off"


            pz['a']=cpuzzle_path+"/img/a"+str(a)+".png"
            pz['b']=cpuzzle_path+"/img/b"+str(b)+".png"
            pz['c']=cpuzzle_path+"/img/c"+str(c)+".png"
            pz['e']=cpuzzle_path+"/img/a"+str(e)+".png"

            if b == b_ev and c== c_ev:
                res="on"
                if e==e_ev: res="ok"
            else:
                res="off"

        vpgrid cols 6 rows 1:
            spacing 0
            draggable True
            mousewheel True
            imagebutton idle pz['a'] action SetLocalVariable('a',b+1)
            imagebutton idle pz['b'] action SetLocalVariable('b',b+1)
            imagebutton idle pz['c'] action SetLocalVariable('c',c+1)
            add (cpuzzle_path+"/img/"+res+".png")
            imagebutton idle pz['e'] action SetLocalVariable('e',e+1)

        python:
            if res == "ok": rp[vars]['res']=True
            else: rp[vars]['res']=False
