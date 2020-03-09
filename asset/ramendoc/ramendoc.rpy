init -10 python:

    build.archive("ramendoc", "all")
    build.classify('game/'+ramu.fn_getdir()+'/**', 'ramendoc')

    class ramen_documentation():
        """ Create a md documentations from __doc__. base on pydoc but customized for renpy/ramen """
    
        def __init__(self,**kwagrs):

            self.dir = "E:/pp-renpy/ramen/wiki/"
            self.files = filter(lambda w: w.endswith(".rpy"), sorted(renpy.list_files(False)))
        
        def setting(self, **kwagrs):
            
            self.footer = "\n\n[[Home]] | [[Class Index|index]] | [[Function|function]]\n"
            self.title = 'Ramen'
            self.home_info = "Renpy according me, a modular approach. It is renpy framework to help you creating of visual novell game."
            
            try:
                for k in kwagrs(k): self.__dict__[k] = kwagrs[k]
            except: pass
                
        def write(self, mdfile, sts):
            file = open( self.dir+mdfile+".md", "w") 
            file.writelines(self.wrapper(sts))
            file.close()
            print self.dir+mdfile+".md -- created"

        def wrapper(self,sts):
            return sts + "\n\n---\n\n"+self.footer
            
        def collect(self,what,st=''):
            
            for f in self.files:
                fn = ramu.fn_info(f)
                line_fileinfo = "\n### "+fn['name']+"\n\n\nFile: "+ fn['dir']+"/"+ fn['path'] +"/"+ fn['file'] + "\n"
                c = ''
                for line in open("E:/pp-renpy/ramen/game/"+f,"r"):
                    line = line.strip()
                    if line.startswith(what):
                        rn = line.split(what +' ')
                        rn[1]=rn[1].replace(":",'')
                        c += "\n * "+ rn[1]
                if not c =='':
                    st += line_fileinfo + c + "\n"
                    
            self.write(what.lower(), st)
            
        def getfunc(self):

            import sys, inspect

            collect = []
            ndx_st = '# Function\n\n'

            for i in sorted(globals().keys()):
                o = globals()[i]
                try:
                    if "game/" in repr(o.func_code):
                        #print i + '=' + repr( o )
                        ndx_st += "\n#### "+ i + "\n"
                        try: ndx_st += "\n   " + inspect.getdoc(o) + "\n"
                        except: pass
                    
                except:
                    pass

            self.write('function', ndx_st)
            
        def getclass(self):

            import sys, inspect
   
            tag = ['container','WorldTime','event','rn_obj']
            cm = inspect.getmembers(sys.modules[__name__], inspect.isclass)
            ndx= []
        
            for c in cm:
                t1 = repr(c[1]) + repr(c[1].__bases__)
            
                if 'ramen' in t1 or c[0] in tag:
            
                    mdfile = str(c[0]).lower()
                    sts = "# "+str(c[0])+"\n"
                
                    ndx.append('[['+mdfile+']]')

                    doc = inspect.getdoc(c[1])
                
                    try:
                        if 'ramen_object' in str(c[1].__bases__):
                            sts +="Base: [[ramen_object]]\n"
                    except:
                        pass

                    if doc is not None:
                        sts += "\n"+ str(doc).strip()+"\n\n"
            
                    for m in inspect.getmembers(c[1]):
                    
                        if not m[0].startswith('_') or m[0]=="__init__":
                    
                            try:
                                pr = inspect.getargspec(c[1].__dict__[m[0]])

                                if not m[0]=='__init__':
                                    #anchor = "(#"+c[0].lower()+"-"+ m[0].lower()+")"
                                    sts +="\n\n### "+m[0]+"\n"
                                else:
                                    sts +="### init\n"

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
                            
                                sts += "\n\n*Syntax and default parameters:*\n"+spa

                                try:
                                    doc = inspect.getdoc(c[1].__dict__[m[0]])
                                    if doc is not None: sts +=str(doc).strip()+"\n"
                                except:
                                    pass
                            
                            except:
                                pass
        
                    self.write(mdfile, sts)
                
            return ndx
        
        def geth1(self,mdfile):
            title = []
            for line in open(mdfile,"r"):
                line.strip()
                if line.startswith('# '):
                    line = line.replace('# ','')
                    line = line.rstrip() 
                    if line.endswith(':'): line = line.replace(':','')
                    title.append(line)
            
            return title
             
        def mdindex(self,what,st=''):
            import glob
            
            files = glob.glob(self.dir+what+"*.txt")
            
            for f in files:
                fn = ramu.fn_info(f)
                fn['md'] = fn['file'].replace('.txt','.md')
                #mdfile = fn['name']+ suffix
                title = self.geth1(f)
                st += " * [["+ str(title[0]) + "|"+ fn['name'] + "]]\n"
                    
                with open(f, 'r') as file:
                    sts = file.read()
                self.write(fn['name'], sts)

            return st
        
        def class_index(self, filename, ndx, ndx_st='', footer=''):
            for n in sorted(ndx): ndx_st += " * "+ n+"\n"
            self.write(filename, ndx_st + footer)

        
        def build(self):
    
            self.setting()
            
        # class
            ndx = self.getclass()
            self.class_index('index', ndx, "# Class Index\n\n" )
        
            self.getfunc()
            self.collect('screen')
            
        # home
        
            home = "#" + self.title
            home += "\n" + self.home_info + "\n\n"

            home += "## Reference:\n\n"
            home += " * [[Class Index|index]]\n"
            home += " * [[Function List|function]]\n"
            home += " * [[Screens List|screen]]\n"
            
            for t in [ 'tips','howto','game']:
            
                stp = t.title()
                if t == 'game': stp= 'Example'
                
                home += "\n## "+stp+"\n\n"
                home += self.mdindex(t)
                home += "\n"

            self.write('Home', home )
        
    ramendoc = ramen_documentation()