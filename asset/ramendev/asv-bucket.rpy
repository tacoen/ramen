screen rai_bucket_param():

    python:
        #param = rbc()
        param = {}

    viewport:
        draggable True
        mousewheel True
        scrollbars "vertical"

        vbox:

            for k in param.keys():
                python:
                    if isinstance(param[k], (int, str, float)):
                        val = str(param[k])
                    elif isinstance(param[k], (list)):
                        val = ", ".join(param[k])
                    else:
                        try:
                            val = rai_dict_unpack(param[k])
                        except BaseException:
                            val = repr(type(param[k]))

                hbox:
                    text k min_width 200
                    text val style 'ramen_gui'

screen rai_bucket_worldtime():

#            'python_weekday',
#            'python_month',
#           'daypart',
            # 'diff',
            # 'date',
            # 'clock',
            # 'hour',
            # 'diff',

    python:
        i = [
            'weekday',
            'daytime',
            'sun',
            'suntime',
            'dayplay'
            ]
        w = ramen.__dict__

    viewport:
        draggable True
        mousewheel True
        scrollbars "vertical"

        vbox:
            spacing 8

            for i in sorted(w.keys()):
                hbox:
                    text i min_width 200
                    text repr(w[i]) style 'ramen_gui'

            text "Simulation" bold True

            hbox:
                text '@ sun' min_width 200
                text str(24 / len(ramen.suntime_word)) style 'ramen_gui'

            hbox:
                text '@ time' min_width 200
                text str(24 / len(ramen.timeword)) style 'ramen_gui'


screen rai_event_param(obj_id, var=None):

    python:
        event = rbc.event.__dict__[obj_id]

        try:
            passed = event['pass']
        except BaseException:
            passed = False

        req = ['day', 'sun', 'hour', 'require']
        jum = ['call', 'jump']

        for r in req + jum:
            try:
                event[r]
            except BaseException:
                event[r] = None

        try:
            event['label']
            ok = True
        except BaseException:
            ok = False

    if ok:

        vbox yoffset 20:
            spacing 8

            hbox xfill True:
                vbox:
                    spacing 4
                    text "on label" bold True
                    text event['label'] style 'ramen_gui'

                vbox:
                    spacing 4
                    text 'at/after' bold True

                    for r in req:
                        if event[r] is not None:
                            hbox:
                                text r min_width 100
                                text repr(event[r]) style 'ramen_gui'
                    hbox:
                        text 'Pass' min_width 100
                        text repr(passed)

                vbox:
                    spacing 4
                    text 'goto' bold True

                    for r in jum:
                        if event[r] is not None:
                            hbox:
                                text r  min_width 100
                                text str(event[r]) style 'ramen_gui'
