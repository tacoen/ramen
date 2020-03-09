init -205 python:

    class WorldTime:
        """
        Ramen use python datetime for it's game. It also support strftime(format) method, to create a string representing the time under the control of an explicit format string. 
        
        ``` python
        wo = WorldTime(
            [2050, 1, 1, 8],
            ['midnight', 'dusk', 'morning', 'noon', 'evening', 'night'],
            ['dark', 'east', 'mid', 'west', 'dark']
        )        
        ```
        
        * Create a WorldTime object `wo`, Set the time to 8:00 at 1 January 2050.
        * Set 'midnight', 'dusk', 'morning', 'noon', 'evening', 'night' as daytime
        * Set 'dark', 'east', 'mid', 'west', 'dark' as sun time

        See: [[scenery]] 

        Ref: https://docs.python.org/2/library/datetime.html
        
        """

        def __init__(self,
                     gamedate=[2016, 1, 18, 9],
                     tword=[
                         'midnight',
                         'dusk',
                         'morning',
                         'morning',
                         'noon',
                         'evening',
                         'evening',
                         'night'],
                     sword=[
                         'dark',
                         'dark',
                         'sun1',
                         'sun2',
                         'sun2',
                         'sun3',
                         'dark',
                         'dark'],
                     wword=[
                         'monday',
                         'tuesday',
                         'wednesday',
                         'thrusday',
                         'friday',
                         'saturday',
                         'sunday']
                     ):

            self.timeword = tword
            self.sunword = sword
            self.wdayword = wword
            self.greets = [
                         'Night',
                         'Morning',
                         'Morning',
                         'Afternoon',
                         'Afternoon',
                         'Evening',
                         'Night',
                         'Night']
            self.diff = 0

            self.starttime(gamedate)

        def starttime(self, gamedate):
            self.time = datetime.datetime(
                gamedate[0], gamedate[1], gamedate[2], gamedate[3])
            self.start = self.time
            self.time_populate()

        def time_populate(self):
            """ 
            It's called everytime, when `adv`, `adv_day`, or `next_day` called.
            
            populate the attribute, so we can use it in game.
            
            
            | object attr | desc |
            | --- | --- |
            | python_weekday | strftime("%A") =  Friday | 
            | python_month | strftime("%B") = March | 
            | weekday | just like python_weekday, but lowercase | 
            | daypart | int() of day part, base on  the length of `tword` list | 
            | daytime | str() name of day part = Morning | 
            | sun | int() of sun time, base on  the length of `sword` list | 
            | suntime | str() name of sun time = sun1 | 
            | greet | current greets of time, using the length of `greets` list | 
            | diff | the diferents of current time and game-start time, for game progress | 
            | diff_sec | diff in seconds | 
            | date | strftime("%d %B %Y"), current date of game time | 
            | clock | strftime("%H:%M"), current clock of game time | 
            | hour | current hour of game time | 
            | cond | 'sword' + 'tword' list used mostly in renpy's conditionswitch | 
            | dayplay | the day of your game time | 
            | cycle | day of dayplay in 25 days, 2 cycle is 50 | 
            
            """

            self.python_weekday = self.time.strftime("%A")
            self.python_month = self.time.strftime("%B")
            self.weekday = str(self.wdayword[self.time.weekday()])
            self.daypart = int(round(len(self.timeword) * self.time.hour / 24))
            self.daytime = str(self.timeword[self.daypart])
            self.sun = int(round(len(self.sunword) * self.time.hour / 24))
            self.suntime = str(self.sunword[self.sun])
            self.greet = str(self.greets[self.sun])
            self.diff = self.time - self.start
            self.diff_sec = self.diff.total_seconds()
            self.date = self.time.strftime("%d %B %Y")
            self.clock = self.time.strftime("%H:%M")
            self.hour = str(int(self.time.strftime("%I")))
            self.cond = list(set(self.sunword + self.timeword))

            # globals()['diff']=self.diff

            rbc.diff = self.diff
            self.dayplay = self.diff.days + 1

            try:
                self.cycle
            except BaseException:
                self.cycle = self.dayplay

            if self.dayplay - self.cycle == 25:
                rbc.cycle = True
                self.cycle = self.dayplay

        def seed(self, diff):
            """get time seed, aka. time sync. mostly when restore/load saved game"""
            self.time = self.start + diff
            self.time_populate()

        def adv(self, a=1, block=False):
            """advance `a` hour(s), for half hours: `obj.adv(0.5)`. For 15 minuets: `obj.adv(0.25)`. To reverse the time, `obj.adv(-1)` also can be used, but beware.""" 
            self.time = self.time + datetime.timedelta(hours=a)
            self.time_populate()
            if block:
                renpy.block_rollback()

        def adv_day(self, a=1, block=True):
            """advance `a` day(s), equal `obj.adv(a x 24)`""" 
            a = a * 24
            self.time = self.time + datetime.timedelta(hours=a)
            self.time_populate()
            if block:
                renpy.block_rollback()

        def next_day(self, hour=6, block=True):
            """advance to `hour` at next day. let python do the math.""" 
            a = 24 - self.time.hour + hour
            self.time = self.time + datetime.timedelta(hours=a)
            self.time_populate()
            if block:
                renpy.block_rollback()
