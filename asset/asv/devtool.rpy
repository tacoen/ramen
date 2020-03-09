init -10 python:

    wdir = "E:/pp-renpy/ramen/wiki/"
    mdfooter = "\n\n[[Home]] | [[Syntax Index|index]] | [[Function|func]]\n"

    def ramendoc_mdwrite(mdfile, strs):
        file = open( wdir+mdfile+".md", "w") 
        file.writelines(strs)
        file.close()
        print wdir+mdfile+".md -- created"

    def ramendoc_screen():
        F = renpy.list_files(False)
        files = filter(lambda w: w.endswith(".rpy"), sorted(F))
        
        ndx_str = ''
        
        for f in files:
            fn = ramu.fn_info(f)
            fr = open("E:/pp-renpy/ramen/game/"+f,"r")
            header = "\n\n### "+fn['name']+"\n\n"+"File: "+ fn['path'] +"/"+ fn['file'] + "\n\n"
            c = ''
            for r in fr:
                r = r.strip()
                if 'screen' in r:
                    if r.startswith('screen'):
                        rn = r.split('screen ')
                        rn[1]=rn[1].replace(":",'')
                        c += " * "+ rn[1] +"\n"
            
            if not c=='':
                ndx_str += header+c
        
        ramendoc_mdwrite('screen', ndx_str + mdfooter)
        
    def ramendoc_flist():
        """bikin ini"""
    
        import sys, inspect
        
        collect = []
        ndx_str = '# Function\n\n'

        for i in sorted(globals().keys()):
            
            o = globals()[i]
            
            try:
                if "game/" in repr(o.func_code):
                    print i + '=' + repr( o )

                    ndx_str += "\n#### "+ i + "\n"
                    try: ndx_str += "\n   " + inspect.getdoc(o) + "\n"
                    except: pass
                    
            except:
                pass

        ramendoc_mdwrite('func', ndx_str + mdfooter)
            
    def ramendoc_class():
   
        import sys, inspect
   
        tag = ['container','WorldTime','event','rn_obj']
        cm = inspect.getmembers(sys.modules[__name__], inspect.isclass)
        ndx= []
        file = open( wdir+"test.md", "w") 
        
        for c in cm:

            t1 = repr(c[1]) + repr(c[1].__bases__)
            
            if 'ramen' in t1 or c[0] in tag:
            
                mdfile = str(c[0]).lower()
            
                strs = "# "+str(c[0])+"\n"
                strs += "\n" + mdfooter
                
                ndx.append('[['+mdfile+']]')

                doc = inspect.getdoc(c[1])
                
                try:
                    if 'ramen_object' in str(c[1].__bases__):
                        strs +="Base: [[ramen_object]]\n"
                except:
                    pass

                if doc is not None:
                    strs += "\n"+ str(doc).strip()+"\n\n"
            
                for m in inspect.getmembers(c[1]):
                    
                    if not m[0].startswith('_') or m[0]=="__init__":
                    
                        try:
                            pr = inspect.getargspec(c[1].__dict__[m[0]])

                            if not m[0]=='__init__':
                                #anchor = "(#"+c[0].lower()+"-"+ m[0].lower()+")"
                                strs +="\n\n### "+m[0]+"\n"
                            else:
                                strs +="### init\n"

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

                            if m[0]=='__init__':
                                sp = "obj = "+str(c[0])+"("
                            else:
                                sp = "obj." + str(m[0]) + "("
                            
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
                            
                            strs += "\n\n*Syntax and default parameters:*\n"+spa

                            try:
                                doc = inspect.getdoc(c[1].__dict__[m[0]])
                                if doc is not None: strs +=str(doc).strip()+"\n"
                            except:
                                pass
                            
                        except:
                            pass
        
                strs += mdfooter
                
                ramendoc_mdwrite(mdfile, strs)
                
        return ndx
        
    def ramendoc_ndx(filename,ndx,ndx_str='',footer=''):
        for n in sorted(ndx): ndx_str += " * "+ n+"\n"
        ramendoc_mdwrite(filename, ndx_str + footer)

    def ramendoc(mdfile=None):
    
        # class

        ndx = ramendoc_class()
        ramendoc_ndx('index', ndx, "# Syntax Index\n\n", mdfooter )
        
        ramendoc_flist()
        
        ramendoc_screen()
        