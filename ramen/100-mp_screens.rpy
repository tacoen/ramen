screen _overlays(obj_id, data):

    python:
        if not obj_id is None: obj = globals()[obj_id]

    for d in data:
        python:
            img = ramu.fn_ezy(obj.dir +"/overlays/"+d[0])
            xy = d[1]
            

        if img:
            hbox pos xy:
                add img
