
# Transform and (maybe) style needed by ramen at init level

init -199:

    transform rotate4:
        rotate -4
        
    transform phone_speak:
        ypos config.screen_height-320
        on show:
            alpha 0
            easein 0.5 alpha 1
        on hide:
            xoffset 0
            easeout 0.5 xoffset -360