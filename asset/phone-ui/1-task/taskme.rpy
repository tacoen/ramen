#init -1 python:

#    mcph.update_app({
 #       'title': 'My Task',
  #      'hcolor': '#c11',
   # })

init -1 python:

    smp.index_update(
        title='My Task',
        hcolor='#c11',
        order=1,
    )

screen phone_app_task(data=False):
    $ task = mc.store['task']
    vbox:
        style_prefix "phonescreen"
        spacing 10
        
        for t in task.keys():
            hbox:
                if task[t][1]:
                    text "v" style 'icoram' size 18 color "#393" yoffset 2
                    $ tcolor = "#999"
                else:
                    text "q" style 'icoram' size 18 color "#333" yoffset 2
                    $ tcolor = "#000"
                null width 8
                text task[t][0] color tcolor


init offset = 0

