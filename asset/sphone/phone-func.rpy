init -102 python:

    class phone(ramen_object):

        def load(self, id=None, **kwargs):
            self.index('apps', 'apps', 'rpy')

        # TODO: apps indirect

        def pickup(self, appname=False):
            scrs = filter(
                lambda fw: 'smp_ui' in fw,
                renpy.get_showing_tags('screens'))
            if 'phone_ui' not in scrs:
                renpy.show_screen('smp_ui', app=appname)

        def hide(self,):
            scrs = filter(
                lambda fw: 'smp_' in fw,
                renpy.get_showing_tags('screens'))
            for scr in scrs:
                renpy.hide_screen(scr)
