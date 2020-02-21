init - 199 python:

    import math

    # renpy behave

    def label_callback(name, abnormal):

        store.last_label = name

        # event
        ramen_event_occuring()

        # make game harder
        cost_of_time()

    config.label_callback = label_callback

    rbc.event = object()

    def ramen_event_occuring():
        h = rbc.event.__dict__
        for e in h.keys():
            if ramen_event_isoccur(e):
                rbc.event_lastlabel = last_label
                try:
                    goto = h[e]['call']
                except BaseException:
                    goto = False
                if goto:
                    if renpy.has_label(goto):
                        renpy.call(goto)

                try:
                    goto = h[e]['jump']
                except BaseException:
                    goto = False
                if goto:
                    if renpy.has_label(goto):
                        renpy.jump(goto)

    def cost_of_time():

        if rbc.tick is None:
            print '>>'
            rbc.tick = rbc.diff.total_seconds()

        hh = float(rbc.diff.total_seconds()) - float(rbc.tick)
        if hh == float(2 * 3600):
            mc.gain('energy', -0.5)
            mc.gain('hygiene', -1)
            rbc.tick = rbc.diff.total_seconds()
            print "---"

        print rbc.tick

    class event():

        def __init__(self, id, label, **kwargs):
            try:
                rbc.events
            except BaseException:
                rbc.event = object()

            self.id = str(id)

            rbc.event.__dict__[str(id)] = {}
            rbc.event.__dict__[str(id)][str('label')] = str(label)

            self.set_occur(**kwargs)

        def __call__(self, what=None):
            if what is None:
                return rbc.event.__dict__[str(self.id)]
            else:
                try:
                    return rbc.event.__dict__[str(self.id)][what]
                except BaseException:
                    return None

        def set_occur(self, **kwargs):
            for k in kwargs:
                rbc.event.__dict__[str(self.id)][str(k)] = str(kwargs[k])

        def set_pass(self):
            rbc.event.__dict__[str(self.id)][str('pass')] = True

        def is_pass(self):
            try:
                return rbc.event.__dict__[str(self.id)][str('pass')]
            except BaseException:
                return False

        def occur(self):
            return ramen_event_isoccur(self.id)

    def ramen_event_isoccur(id=None):

        if id is None:
            return False

        res = False

        try:
            if rbc.event.__dict__[id]['pass']:
                return False
            else:
                return True
        except BaseException:
            pass

        try:
            if rbc.event.__dict__[id]['label'] == last_label:
                res = True
            else:
                return False
        except BaseException:
            pass

        if res:
            try:
                if rbc.event.__dict__[id]['day'] > wo.dayplay:
                    res = True
            except BaseException:
                pass

        if res:

            try:
                if int(rbc.event.__dict__[id]['sun']) == int(wo.sun):
                    res = True
                else:
                    res = False
            except BaseException:
                pass

        if res:

            try:
                if int(rbc.event.__dict__[id]['hour']) > int(wo.time.hour):
                    res = True
                else:
                    res = False
            except BaseException:
                pass

        return res
