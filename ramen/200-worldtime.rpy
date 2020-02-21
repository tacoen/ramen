init - 205 python:

    class WorldTime:
        """
        ref: https://docs.python.org/2/library/datetime.html
        """

        def __init__(self,
                     gamedate=[2016, 1, 18, 9],
                     tword=[
                         'Midnight',
                         'Dusk',
                         'Morning',
                         'Morning',
                         'Noon',
                         'Evening',
                         'Evening',
                         'Night'],
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
                         'Monday',
                         'Tuesday',
                         'Wednesday',
                         'Thrusday',
                         'Friday',
                         'Saturday',
                         'Sunday']
                     ):

            self.timeword = tword
            self.sunword = sword
            self.wdayword = wword
            self.diff = 0

            self.starttime(gamedate)

        def starttime(self, gamedate):
            self.time = datetime.datetime(
                gamedate[0], gamedate[1], gamedate[2], gamedate[3])
            self.start = self.time
            self.time_populate()

        def time_populate(self):
            self.python_weekday = self.time.strftime("%A")
            self.python_month = self.time.strftime("%B")
            self.weekday = self.wdayword[self.time.weekday()]
            # hh=self.time.hour+1
            self.daypart = int(round(len(self.timeword) * self.time.hour / 24))
            self.daytime = self.timeword[self.daypart]
            self.sun = int(round(len(self.sunword) * self.time.hour / 24))
            self.suntime = str(self.sunword[self.sun])
            self.diff = self.time - self.start
            self.date = self.time.strftime("%d %B %Y")
            self.clock = self.time.strftime("%H:%M")
            self.hour = self.time.strftime("%I")

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
            self.time = self.start + diff
            self.time_populate()

        def adv(self, a=1, block=False):
            self.time = self.time + datetime.timedelta(hours=a)
            self.time_populate()
            if block:
                renpy.block_rollback()

        def adv_day(self, a=1, block=True):
            a = a * 24
            self.time = self.time + datetime.timedelta(hours=a)
            self.time_populate()
            if block:
                renpy.block_rollback()

        def next_day(self, hour=6, block=True):
            a = 24 - self.time.hour + hour
            self.time = self.time + datetime.timedelta(hours=a)
            self.time_populate()
            if block:
                renpy.block_rollback()
