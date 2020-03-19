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

    tv.makegallery('mc','atv')
    tv.makegallery('mc','intro')    

label demo_asset:

    menu:
        "atm":
            call atm
        "tv":
            call demo_tv
        "back":
            jump demo
    jump demo_asset
    
    
label demo_tv:

    show screen tv(tv, 'demo', None,5,5)
    window auto

    return 