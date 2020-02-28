init -80 python:

    def smp_comboclose():
        rbc.smp_apps = None
        rbc.smp_who = None
        ramu.screen_hideby(prefix='smp_')    

    smp=ramen_object(id='smp')
    smp.ui_set(
        bgr = smp.dir + "/body.png",
        x=0,
        y=0,
        w=480,
        h=720,
        bx = 202,
        by = 639,
        icon_size=(70,70),
        cols=4,
        area={
            'display': [64,88,327,551,(8,8,8,8)],
            'pbars': [0,0,327-96-16,48,(8,8,8,8)],
            'minibars': [0,0,120,32,(4,4,4,4)],
        },
        hbar={
            'like':['#f91',12],
            'relation':['#2B2',12],
            'libido':['#959',12],
        },        
    )

    smp.index('apps','rpy')
    
    rbc.smp_apps = None
    rbc.smp_disable = False

style phone_ui is default

style phone_ui_text is abel_font:
    size 14
    color "#eee" 

screen smp_backbutton(bucket,title=''):
    hbox yalign 0.5 xfill True:
        textbutton ico('arrow-left') style 'ram_ico':
            text_color "#0009"
            text_hover_color  "#000"
            action SetVariable(bucket,None)
        text title color "#000" size 24 xalign 1.0 line_leading 4
    null height 8

transform pullup:

    on show:
        ypos config.screen_height
        easein 0.6 ypos 0
    on hide:
        ypos 0 
        alpha 1
        easeout 0.5 ypos config.screen_height, alpha 0

screen smp_ui(apps=None):

    zorder 198
    
    python:
        
        if rbc.smp_disable:
            ramu.screen_hideby('smp_')
        else:
            renpy.use_screen('smp_main',apps=apps)
    
screen smp_main(apps=None):

    python:
        try: smp_apps
        except: smp_apps = apps
        
        iw = smp.ui.icon_size[0]
        ih = smp.ui.icon_size[1]
        cs = round((style['smp']['area']['display'].xminimum/4)-iw)

    frame background smp.ui.bgr xpos smp.ui.x ypos smp.ui.y xsize smp.ui.w ysize smp.ui.h at pullup:
        
        add (ramu.fn_ezy(smp.dir+"/wp/1")) xpos style['smp']['area']['display'].xpos ypos style['smp']['area']['display'].ypos
        
        imagebutton xpos smp.ui.bx ypos smp.ui.by action Function(smp_comboclose):
            idle (smp.dir + "/btn.png")
            hover (smp.dir + "/btn-hover.png")

        text wo.clock color "#fff" style 'abel_font' xpos style['smp']['area']['display'].xpos+8 ypos style['smp']['area']['display'].ypos+8 size 48
        
        if rbc.smp_apps is None:
        
            vpgrid style style['smp']['area']['display'] yoffset style['smp']['area']['display'].yminimum/2:
                cols smp.ui.cols
                spacing cs
        
                for a in sorted(smp.apps.keys()):
                    use smp_item(a)
                
        else:
            $ a = rbc.smp_apps
            
            frame style style['smp']['area']['display']:
                ysize 32 
                background smp.apps[a]['hcolor']
                hbox yalign 0.5 xfill True xoffset 4:
                    text smp.apps[a]['title'] color "#fff6" size 20 bold True
                    textbutton ico('close') action SetVariable('rbc.smp_apps',None):
                        style "ram_ico" xsize 32 xalign 1.0
                        text_size 16 text_hover_color "#fff" text_line_leading 4 text_xalign 0.5
                        
            frame yoffset 32:
                background smp.apps[a]['bgr'] 
                style style['smp']['area']['display'] 
                ysize style['smp']['area']['display'].yminimum-32

                if renpy.has_screen("smp_app_"+a):
                    $ renpy.use_screen("smp_app_"+a)
                else:
                    text "N/A" color "#000" yalign 0.5 xalign 0.5 size 32


screen smp_item(a):

    $ icon = im.Scale(smp.apps[a]['icon'],smp.ui.icon_size[0],smp.ui.icon_size[1])
    vbox:
        imagebutton action SetVariable('rbc.smp_apps',a):
            idle icon
            hover im.MatrixColor(icon,im.matrix.brightness(0.3))
        textbutton smp.apps[a]['title'] action SetVariable('rbc.smp_apps',a):
            style "phone_ui" text_xalign 0.5 xsize smp.ui.icon_size[0]
