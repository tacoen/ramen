screen rai_bucket_param():

    python:
        param = rbc()

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

    python:
        i = [
            'python_weekday',
            'python_month',
            'weekday',
            'daypart',
            'daytime',
            'sun',
            'suntime',
            'diff',
            'date',
            'clock',
            'hour',
            'diff',
            'dayplay',
            'cycle']
        w = wo.__dict__

    viewport:
        draggable True
        mousewheel True
        scrollbars "vertical"

        vbox:
            spacing 8

            for i in sorted(w.keys()):
                hbox:
                    text i min_width 200
                    text repr(w[i])

            text "Simulation" bold True

            hbox:
                text '@ sun' min_width 200
                text str(24 / len(wo.sunword))

            hbox:
                text '@ time' min_width 200
                text str(24 / len(wo.timeword))


screen rai_event_param(obj_id, var=None):

    python:
        event = rbc.event.__dict__[obj_id]

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
                    text event['label']

                vbox:
                    spacing 4
                    text 'at/after' bold True

                    for r in req:
                        if event[r] is not None:
                            hbox:
                                text r min_width 100
                                text repr(event[r])

                vbox:
                    spacing 4
                    text 'goto' bold True

                    for r in jum:
                        if event[r] is not None:
                            hbox:
                                text r  min_width 100
                                text repr(event[r])
