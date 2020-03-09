# The game starts here.

image testbgr = Solid('#234')

label start:

    # init your game at start
    
    call _ramen_start()
    
    scene testbgr
    
    "This is a development version of Ramen, and not intent to be a release.{w} When you see this in your working project, you will know that is not ready yet."

    narator "I am a narator just like the line before me.{w}\nBut, I'm best when you want a multiline."

    narator """
    Now we are using three quotes for narations.
    This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as  published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.
    """
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

    jump start

    # This ends the game.

    return

