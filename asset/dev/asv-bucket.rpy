screen rai_bucket_param():

    python:
        param = rbc()

    viewport:
        draggable True
        mousewheel True
        scrollbars "vertical"

        vbox:
    
            for k in param.keys():
                python:
                    if isinstance(param[k], (int, str, float)): val = str(param[k])
                    elif isinstance(param[k], (list)): val = ", ".join(param[k])
                    else:
                        try : val = rai_dict_unpack(param[k])
                        except:  val = repr(type(param[k]))

                hbox:
                    text k min_width 200
                    text val style 'abel_font'

screen rai_bucket_worldtime(): 

    python:
        i = [ 'python_weekday',' python_month',' weekday',' daypart',' daytime',' sun',' suntime',' diff',' date',' clock',' hour',' diff',' dayplay',' cycle']
        w = wo.__dict__
        
    viewport:
        draggable True
        mousewheel True
        scrollbars "vertical"
    
        vbox:
            spacing 8
    
            for i in sorted(w.keys()):
                hbox:
                    text i min_width 200
                    text repr(w[i])

            text "Simulation" bold True
        
            hbox:
                text '@ sun' min_width 200
                text str(24/len(wo.sunword))

            hbox:
                text '@ time' min_width 200
                text str(24/len(wo.timeword))
            