init -1 python:
    
    # object must in the object roots
    tv = ramen_object('tv')
    
    tv.ui_set(
        x=193,
        y=80,
        w=909,
        h=502,
    )

    tv.exitarea=(909, 612)

    tv.makegallery('demo','test')

label ramen_test:
    
label demo_tv:

    show screen tv(tv, 'demo', 'test-random', 5, 5)
    window auto

    return 