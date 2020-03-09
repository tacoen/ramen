init -199 python:

    import math

    # renpy behave

    def ramen_labelcallback(name, abnormal):

        store.last_label = name

        # event
        ramen_event_occuring()
        ramen_cot(2, hygiene=0.5, vital=0.25)

    config.label_callback = ramen_labelcallback

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

    def ramen_cot(hour, **kwargs):
        """
        Cost of time. Make game harder using `rbc.tick`

        #### Example:

        ``` python
            ramen_cot(2,hygiene=0.5,vital=0.25)
        ```

        Every 2 hours, reduce `hygiene` and `vital` from `mc.stat`

        """

        if rbc.tick is None:
            rbc.tick = rbc.diff.total_seconds()

        hh = float(rbc.diff.total_seconds()) - float(rbc.tick)

        if hh == float(hour * 3600):
            for k in kwargs:
                mc.gain(k, -1 * kwargs[k])
            rbc.tick = rbc.diff.total_seconds()

    class event():

        def __init__(self, id, label, **kwargs):
            """
            Create and set an event

            ``` python
            event_test = event( 'test', 'white_room',
                day=2,
                hour=9,
                sun=1,
                require={
                    'hygiene': 2
                    },
                call='eventest'
                )
            ```

            """

            try:
                rbc.events
            except BaseException:
                rbc.event = object()

            self.id = str(id)

            rbc.event.__dict__[str(id)] = {}
            rbc.event.__dict__[str(id)][str('label')] = str(label)

            self.set_occur(**kwargs)

            try:
                ramen_dev('events', self.id)
            except BaseException:
                pass

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
                rbc.event.__dict__[str(self.id)][str(k)] = kwargs[k]

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

        if res:

            try:

                for r in rbc.event.__dict__[id]['require'].keys():

                    if int(mc.stat[r]) >= int(
                            rbc.event.__dict__[id]['require'][r]):
                        res = True
                    else:
                        res = False

            except BaseException:
                pass

        return res
