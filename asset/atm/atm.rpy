init -2 python:

    ATMPATH = ramu.fn_getdir() 

    def atm_drawn(ammount):
        mc.banking(ammount)
        ramu.sfx(ATMPATH,"atm-over",True)
        return True

style atm is default

style atm_frame:
    background "#0000"
    xpos 272
    ypos 138
    xsize 740
    ysize 430

style atm_text is abel_font:
    color "#ff0"
    size 32

style atm_button is gui_button:
    hover_background "#cdf"
    
style atm_button_text is atm_text:
    hover_color "#000"

screen atm(dscr=None):
    
    
    python:
        try: scr
        except: scr=dscr
        
    style_prefix "atm"

    add (ATMPATH+"/atm-face.png")

    frame:
        vbox yfill True:
            vbox:
                null height 32
                hbox xfill True:
                    text "SHBANK ATM" xalign 0.5
                null height 32
            
            if scr is None:
                use atm_mainmenu
            elif scr == 'balance':
                use atm_balance
            elif scr == 'withdrawn':
                use atm_withdrawn
            elif scr == 'payment':
                use atm_payment    
            else:
                vbox yfill True xsize 740:
                    text "Thank you for banking with us." xalign 0.5

screen atm_pin(text):
    style_prefix "atm"
    frame:
        vbox xalign 0.5 yalign 0.5:
            text "[text]"

screen atm_balance():
        vbox yfill True xsize 740:
            text str(mc.bank)+" $" size 48 xalign 0.5
            textbutton "< Back" action SetScreenVariable('scr',None)

screen atm_payment():
    python:
        if rbc.cycle:
            homebill = 350
        else:
            homebill = 0
            
    hbox xfill True:
        vbox yalign 1.0:
            textbutton "< Back" action SetScreenVariable('scr',None)
        vbox xalign 1.0:
            spacing 24
            textbutton "("+str(homebill)+") Home Bill >" action [ 
                SetVariable('rbc.cycle',False),
                Function(mc.pay,where='bank',ammount=homebill),
                Return('balance')
            ]

screen atm_withdrawn():
    hbox xfill True:
        vbox:
            spacing 24
            textbutton "< 1000" action [ Function(atm_drawn,ammount=1000), Return('balance') ]
            textbutton "< 700" action [ Function(atm_drawn,ammount=700), Return('balance') ]
            textbutton "< 500" action [ Function(atm_drawn,ammount=500), Return('balance') ]
            null height 32
            textbutton "< Back" action SetScreenVariable('scr',None)
        vbox xalign 1.0:
            spacing 24
            textbutton "300 >" action [ Function(atm_drawn,ammount=300), Return('balance') ]
            textbutton "100 >" action [ Function(atm_drawn,ammount=100), Return('balance') ]
            textbutton "50 >" action [ Function(atm_drawn,ammount=50), Return('balance') ]

screen atm_mainmenu():

    hbox xfill True:
        vbox:
            spacing 24
            textbutton "< Payment" action SetScreenVariable('scr','payment')
            textbutton "< Balance" action SetScreenVariable('scr','balance')
            textbutton "< Exit" action Return(False)
        vbox yalign 1.0 xalign 1.0:
            spacing 24
            textbutton "Withdrawn >" action SetScreenVariable('scr','withdrawn')
            

label atm:
    show screen atm_pin('pin:')
    $ ramu.sfx(ATMPATH,'atm-start',True)
    pause 1
    hide screen atm_pin
    show screen atm_pin('pin: ******')
    pause 3
    hide screen atm_pin
    call screen atm()
    if _return == 'balance':
        call screen atm('balance')
    else:
        show screen atm('thanks')
        pause 1
        hide screen atm
    return
    