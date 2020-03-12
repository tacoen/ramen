init -203 python:

    class uiobj(ramen_object):

        def load(self, id=None, **kwargs):
            self.ui_set(True, **kwargs)

init -96 python:

    class npcrowd(ramen_object):

        def load(self, id=None, **kwargs):

            files = self.files()
            self.crowd = []

            for f in files:
                fn = ramu.fn_info(f)
                if fn['path'] not in self.crowd:
                    self.crowd.append(fn['path'])
                    self.makenpc_image(fn['path'])

        def makenpc_image(self, who):
            for d in [0, 1, 2]:
                st = self.id + " " + who + " " + str(d)
                stt = ramu.fn_ezy(self.dir + "/" + who + "/" + str(d))
                if stt:
                    renpy.image(st, stt)

        def meet(self, who, label=None, d=None):

            npc = True

            if who in self.crowd:
                if label is not None and renpy.has_label(label):
                    renpy.call_in_new_context(label)
                else:
                    if renpy.has_label(who + "_meet"):
                        renpy.call_in_new_context(who + "_meet")
                    else:

                        if renpy.loadable(self.dir + "/" + who + "/chat.json"):
                            dialogue = ramu.json_file(
                                self.dir + "/" + who + "/chat.json")
                        else:
                            dialogue = ramu.json_file(self.dir + "/chat.json")

                        if d is None:
                            d = ramu.random_of(dialogue.keys())

                        renpy.show(self.id + ' ' + who + ' ' +
                                   str(ramu.random_int(0, 2)))

                        rbc.anon_name = who.title()

                        for line in dialogue[d]:
                            if not npc:
                                if not line == "":
                                    character.mc(line)
                                npc = True
                            else:
                                renpy.show(self.id + ' ' + who +
                                           ' ' + str(ramu.random_int(0, 2)))
                                if not line == "":
                                    character.anon(line)
                                npc = False

                        renpy.hide(self.id)
