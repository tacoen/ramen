# The game starts here.
init python:
    event_test = event('test',label='start',day=1,call='eventest',jump='eventest_jump')

label start:

    call _ramen_start()
    
    "This is a development version of Ramen, and not intent to be a release."
    
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
    
label eventest_jump:

    "but hey, you got here from a jump!"
    "So, you can use rbc.event_lastlabel to return"
    "which are \"[rbc.event_lastlabel]\""
    
    # infinite loop aware
    $ event_test.set_pass()
    $ renpy.jump(rbc.event_lastlabel)
    