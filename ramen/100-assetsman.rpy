init -105 python:

    class ramen_assets(ramen_object):

        """
        Ramen Assets management, a simple plugins system for ramen renpy.
        Beware as It's could be almost everything?

        ``` python

        init -90 python:

            ram = ramen_assets('ram')

        init -10 python:

            # provide information about cshooter

            ram.component(
                'cshooter',
                title = "Click Shooter - Minigame",
                version = "1.0",
            )

            # create cshooter-minigame.rpa for distributions

            build.archive("cshooter-minigame", "all")
            build.classify('game/'+ramu.fn_getdir()+'/**', 'cshooter-minigame')

        ```
        """

        def load(self, id=None, **kwargs):
            """Get `*-def.rpy` in 'assets' and make them as assets index/list """

            key_suffix = '-def'

            self.__dict__['_component'] = {}

            for f in sorted(self.files('', '', key_suffix + ".rpy")):
                fn = ramu.fn_info(f)
                a = fn['name'].replace(key_suffix, '')
                self._component[str(a)] = {}
                self._component[str(a)]['dir'] = fn['dir']

        def _call(self, func, **kwargs):
            """Call a modular function and pass their keyword argument. Return `False` if fail/errors"""

            try:
                res = globals()[func](**kwargs)
            except BaseException:
                res = False

            return res

        def component(self, what, **kwargs):
            """
            Set the component, and to get the component use `_component`.

            ``` python
            ram.component(
                'phone',
                title="Appcontainer: Smartphone UI",
                version="1.0",
                author="tacoen",
                author_url='https://github.com/tacoen/ramen',
                desc="A nice apps container. A Modular approach to your stats, relations, game stats, etc.",
                active_func='smp_activated'
            )
            ```

            * To maintain its relative path, 'ram.component' shall be called in every asset component.
            * you also can use 'active_func' to bind the component to your scripts.

            """

            will_active = False

            if what in self._component.keys():

                for k in kwargs:
                    self._component[what][str(k)] = kwargs[k]

                    if k.lower() == 'active_func':
                        will_active = True

                if will_active:
                    func = self._component[what]['active_func']

                    import inspect
                    if (func in globals() and inspect.isfunction(
                            globals()[func])):
                        globals()[func]()

            else:

                print what + " was not registered as component. Information will not provided."
