init -300 python in character:
    """character is container of renpy."""
    test = False

init -300 python in ramen:

    """
    Ramen is StoreModule for ramen frameworks enviroment/controls.
    All Storemodule changes will store in Game savedata.
    
    In previous version this 'ramen' was rbc() functions.
    
    #### ramen.uid()
    
    Return Next Unique id for object creations. for current unique id use 'ramen.uid_number'.
    replacing the needed 'uuid' for ramen object creations.

    #### ramen.time

    | func | return |
    | ---- | ---- |
    | _suntime() | True: return name, False: Return Interger (Default=True) |
    | _daytime() | True: return name, False: Return Interger (Default=True) |
    | ... | All function from datetime. See: https://docs.python.org/2/library/datetime.html |
    
    * ramen.time.hour return 8
    * ramen.time.strftime('%X') return '08:00:00'
    
    ### ramen.mouse
    Return mouse position (x,y)
    
    ### ramen.var
    
    Return Dict item in ramen._container. If not exist, return False
    
    ``` python
        > ramen.var.a=1
        > ramen.var.a
        1
        > ramen.var.b
        False
    ```
    Short for ramen._container.__dict__ using container() class to interact.
    
    * ramen.var.x is ramen._container.__dict__['x']
    * ramen.var.x=object() set ramen._container.__dict__['x']=object()
    
    """

    import datetime
    import re
    import pygame

    toggle = {}

    def Mouse():
        """Get Mouse pos, return (x,y)"""
        return pygame.mouse.get_pos()
        
    uid_number = 0

    def uid():
        """Return Next Unique id for object creations."""
        global uid_number
        uid_number += 1
        return "{:03d}".format(uid_number)

    _var = object()
    
    class var_container(object):
    
        def __call__(self):
            return _var.__dict__
            
        def __setattr__(self, key, value):
            _var.__dict__[key] = value

        def __getattr__(self, key):
            try:
                return _var.__dict__[key]
            except BaseException:
                return False
                
        def setdata(self, what, **kwargs):
            try:
                _var.__dict__[what]
            except BaseException:
                _var.__dict__[str(what)] = {}

            for k in kwargs:
                _var.__dict__[what][k] = kwargs[k]                

    var = var_container()

    time_seed = datetime.timedelta(0, 0)
    time_doom = None
    
    suntime = ''
    daytime = ''
    sun = ''
    weekday = ''
    dayplay = 0
    timecond = []
    
    class time():
        """
        Python datetime for game's time
        
        See: https://docs.python.org/2/library/datetime.html
        
        """

        def __init__(self, y=2020, m=1, d=18, h=13, min=0, **kwargs):
            self.time = datetime.datetime(y, m, d, h, min)

            try:
                self.daytime_word = kwargs['daytime']
            except BaseException:
                self.daytime_word = ['midnight', 'dusk',
                                     'morning', 'noon', 'evening', 'night']

            try:
                self.suntime_word = kwargs['suntime']
            except BaseException:
                self.suntime_word = [
                    'dark',
                    'dark',
                    'sun1',
                    'sun1',
                    'sun',
                    'sun',
                    'sun2',
                    'dark',
                    'dark']

            global timecond
            
            timecond = list(set( self.suntime_word + self.suntime_word))
            
            self.start = self.time
            self.populate()            
            
        def __getattr__(self,key):
            try: 
                return self.__dict__[key] 
            except:
                return getattr(self.time,key)
            
        def clock(self):
            return self.time.strftime('%H:%M')

        def daytime(self, name=True):
            """If True, return in word. If False, return int"""

            p = int(round(len(self.daytime_word) * self.time.hour / 24))
            if name:
                return str(self.daytime_word[p]).title()
            else:
                return p

        def suntime(self, name=True):
            """If True, return in word. If False, return int"""

            p = int(round(len(self.suntime_word) * self.time.hour / 24))
            if name:
                return str(self.suntime_word[p]).title()
            else:
                return p

        def __call__(self):
            return self.time

        def dayplay(self):
            global time_seed
            return time_seed.days+1
            
        def doom(self, **kwargs):
            """
            Set Doomed time, if used when you need to set a doom time.
            
            ``` python
                ramen.time.doom(day=1,hour=2)
            ```
            
            * Set ramen.time_doom to next 1 day and 2 hour
            * Doom time is checked by last_label callback.
            * All you had to do is advance the time and set the doom label in last_label callback.
            """

            global time_doom

            try:
                kwags['day']
            except BaseException:
                kwags['day'] = 0
            try:
                kwags['hour']
            except BaseException:
                kwags['hour'] = 6

            time_doom = self.time + \
                datetime.timedelta(hours=kwags['hour'], days=kwags['day'])

        def populate(self):

            global time_seed
            global sun
            global suntime
            global daytime
            global weekday
            global dayplay
            
            time_seed = self.time - self.start
            suntime = self.suntime(True)
            daytime = self.daytime(True)
            sun = self.suntime(False)
            weekday = self.strftime('%A')
            dayplay = self.dayplay()
            
        def adv(self, a, block=True):
            """Advance `a` hours from time. Update `ramen.time_seed` (store). If `block` is True, rollback will be block."""

            self.time = self.time + datetime.timedelta(hours=a)

            self.populate()

            if block:
                renpy.block_rollback()

            return self.time

    time = time()