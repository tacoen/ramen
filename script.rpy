# The game starts here.

init python:

    import sys, inspect

    tag = ['container','WorldTime','event']
    cm = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    file = open("E:/pp-renpy/ramen/game/syntax-index.md","w") 
    for c in cm:
    
        t1 = repr(c[1]) + repr(c[1].__bases__)
        
        if 'ramen' in t1 or c[0] in tag:
            file.writelines("## "+str(c[0])+"\n")
            file.writelines("   "+ str(eval(c[0]).__doc__)+"\n")
            #file.writelines( repr(c[1])+"\n")
        
        #mc = eval(c[0])
        
            for m in dir(c[1]):
                if not m.startswith('_'):
                    file.writelines("### "+ m+"\n")
        
            file.writelines("\n")
        
    file.close()

    print dir(uiobj)
    print type(uiobj)

    event_test = event(
        'test',
        label='white_room',
        day=2,
        require={
            'hygiene': 2},
        call='eventest')

image testbgr = Solid('#234')

label start:

    call _ramen_start()

    scene testbgr
    
    "This is a development version of Ramen, and not intent to be a release.{w} When you see this in your working project, you will know that is not ready yet."

    narator "I am a narator just like the line before me.{w}\nBut, I'm best when you want a multiline."

    narator """
    Now we are using three quotes for narations.
    This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as  published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.
    """

    show screen bar_example()
    
    mc "I am your main character."
    anon "a placeholder from annonymous, which can be named with 'rbc.anon_name'"
    mc "We talk, I speak."
    thou "In your mind."
    anon "And, You listened."
    emoti "smile"
    caption "Once upon a time in testing land,{w=1}\nThere was a demo."
    tips "When you see me, you saw a tips!"
    
    

    "This line above to end the game within 3."

    "2"

    "1"

    "After this the game will end."

    # This ends the game.

    return


label eventest:
    "You see a event occur here."
    "nice?"

    # infinite loop aware
    $ event_test.set_pass()

    "Now back to last label"

    return

