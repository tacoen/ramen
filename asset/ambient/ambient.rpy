init -103 python:

    AMBIENT_PATH=ramu.fn_getdir()
    
    def ramen_ambient(what=None):
        renpy.show_screen('ramen_ambient',what=what)
    
init -103:

    screen ramen_ambient(what=None):
    
        layer 'ambient'
        
        python:
            if what is None: what = 'indoor'
            img = (ramu.fn_ezy(AMBIENT_PATH+"/"+what))

        if img:
            hbox xpos 0 ypos 0:
                add (img)

            