init -1 python:

    rast.register('coba',title='therapist')
    rast.register('coba2',title='bring the balance of long title',start='ramen_test')
    

label ramen_test:

    "hold a sec"
    

label story_coba:        

    label .start:
        "i'am module!"

    label .end:
        $ ramenepisode.coba.complete=True
        "end"
        