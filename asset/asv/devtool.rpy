init -10 python:

    def ramendoc(mdfile=None):
    
        import sys, inspect
        if mdfile is None: mdfile = "E:/pp-renpy/ramen/game/syntax-index.txt"
    
        tag = ['container','WorldTime','event']
        cm = inspect.getmembers(sys.modules[__name__], inspect.isclass)
        
        file = open(mdfile,"w") 
        
        for c in cm:
        
            t1 = repr(c[1]) + repr(c[1].__bases__)
        
            if 'ramen' in t1 or c[0] in tag:
                file.writelines("## "+str(c[0])+"\n")
                
                if eval(c[0]).__doc__ is not None:
                    file.writelines(""+ str(eval(c[0]).__doc__)+"\n")
        
        
                try:
                    if 'ramen_object' in str(c[1].__bases__):
                        file.writelines("Base: [[ramen_object]]\n")
                except:
                    pass
                    
                for m in inspect.getmembers(c[1]):
                    
                    if not m[0].startswith('_'):
                    
                        try:
                            pr = inspect.getargspec(c[1].__dict__[m[0]])

                            file.writelines("### "+ m[0]+"\n")
                        
                            try:
                                doc = inspect.getdoc(c[1].__dict__[m[0]])
                                if doc is not None: file.writelines(str(doc).strip()+"\n")
                            except:
                                pass
                        
                            if pr.defaults is not None:
                                at = len(pr.args[1:]) - len(pr.defaults)
                            else:
                                at = 0

                            if pr.keywords is not None:
                                keywr=repr(pr.keywords).replace("'","")
                            else:
                                keywr= ""
                        
                            ags = []
                            n = 0
                            cn = 0
                            d = ''
                            sp = ''
                            spa = '\n``` python\n'
                            
                            sp = str(c[0]) + "." + str(m[0]) + "("
                            
                            for ag in pr.args[1:]:
                                
                                if n >= at:
                                    try: d = str(pr.defaults[cn])
                                    except: d  =""
                                    cn += 1
                                    
                                if not d == "":
                                    sp += ag + "="+ d  +","
                                else:
                                    sp += ag +","
                                
                                n+=1
                                
                            
                            if not keywr =="":
                                sp = sp + "**"+keywr

                            if sp.endswith(','): sp=sp[:-1]
                            
                            sp = sp + ")"
                            spa += sp + "\n```\n\n"
                            
                            file.writelines(spa)

                            print sp
                            
                        except:
                            pass
        
                file.writelines("\n")
        
        file.close()

        print "See: "+mdfile