# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    mc "My name is [mc_name]"
    
    narator "This is a narration"
    narator "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut mattis posuere tortor, blandit tristique risus ornare sit amet. Donec finibus magna in placerat imperdiet. Maecenas pretium imperdiet augue. Proin nisl sem, vulputate vitae malesuada in, laoreet id mi. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Sed vel maximus magna, vel mollis nibh. Morbi commodo hendrerit facilisis. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Cras eget vehicula risus. Fusce sit amet tellus eu orci pharetra convallis. Praesent rutrum suscipit tortor sed placerat. Morbi cursus ultricies ex et laoreet. Aenean cursus dolor et interdum aliquam. Fusce lobortis dui vitae ex tristique, eget pretium sem pretium. Aenean facilisis leo non nulla tincidunt, eget interdum ex auctor. Sed fermentum facilisis elementum. Nunc gravida quis justo lacinia egestas. Sed bibendum, tellus feugiat blandit eleifend, nunc ex tristique orci, vitae porta justo nulla mattis leo. Cras ac erat diam. Ut sit amet lectus in neque accumsan venenatis. Aenean eleifend in erat eget suscipit. Integer in congue libero, pulvinar vehicula diam. Sed ac hendrerit arcu."
    
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    narator """
    This is the first line of dialogue. It's longer than the other two
    lines, so it has to wrap.

    This is the second line of dialogue.

    This is the third line of dialogue.
    """
    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"
    
    e "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut mattis posuere tortor, blandit tristique risus ornare sit amet. Donec finibus magna in placerat imperdiet. Maecenas pretium imperdiet augue. Proin nisl sem, vulputate vitae malesuada in, laoreet id mi. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Sed vel maximus magna, vel mollis nibh. Morbi commodo hendrerit facilisis. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Cras eget vehicula risus. Fusce sit amet tellus eu orci pharetra convallis. Praesent rutrum suscipit tortor sed placerat. Morbi cursus ultricies ex et laoreet. Aenean cursus dolor et interdum aliquam. Fusce lobortis dui vitae ex tristique, eget pretium sem pretium. Aenean facilisis leo non nulla tincidunt, eget interdum ex auctor. Sed fermentum facilisis elementum. Nunc gravida quis justo lacinia egestas. Sed bibendum, tellus feugiat blandit eleifend, nunc ex tristique orci, vitae porta justo nulla mattis leo. Cras ac erat diam. Ut sit amet lectus in neque accumsan venenatis. Aenean eleifend in erat eget suscipit. Integer in congue libero, pulvinar vehicula diam. Sed ac hendrerit arcu."

    # This ends the game.

    return
