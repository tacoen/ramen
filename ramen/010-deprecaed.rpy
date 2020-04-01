# disposal in doubt.

init -1 python:

    def item_view(item):
        renpy.use_screen('hc_item', item=item)
        
    def coba():
        
        import inspect
        
        for func in sorted(globals()):
    
            if inspect.isfunction(globals()[func]):
                file = inspect.getfile(globals()[func])
                if 'game/' in file:
                    print func+" = " + file
    