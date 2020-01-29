# The game starts here.

label start:

    stop music fadeout 1.0
    $ if renpy.has_label('ramen_test'): renpy.jump('ramen_test')

    "This is a development version of Ramen, and not intent to be a release."

    # This ends the game.

    return
