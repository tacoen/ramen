init -80 python:

    ram.component(
        'ambient',
        title="Ramen Ambient Screens",
        version="1.0",
        author="tacoen",
        author_url='https://github.com/tacoen/ramen',
        desc="Add ambient as screen. you need to add layer 'ambient'.",
    )

    def ramen_ambient(what=None):
        """
        It's a shortcut to
        ``` python
        $ renpy.show_screen('ramen_ambient',what=what)
        ```
        """

        renpy.show_screen('ramen_ambient', what=what)

init -81:

    screen ramen_ambient(what=None):

        layer 'ambient'

        python:
            if what is None:
                what = 'indoor'
            img = (ramu.fn_ezy(ram._component['ambient']['dir'] + "/" + what))

        if img:
            hbox xpos 0 ypos 0:
                add(img)
