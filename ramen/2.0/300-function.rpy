init -301 python:
    
    class ramen2_util():

        def kwdict(self,**kwargs):
            d ={}
            for k in kwargs:
                d[str(k)] = kwargs[k]
            return d
            
        def styleref(self,what=None):
            styleprop = []
            for s in dir(style.default):
                if not s.startswith('_'):
                    if what is not None:
                        if what in s:
                            styleprop.append(s)
                    else:
                        styleprop.append(s)
            return sorted(styleprop)
            
        def style(self, id, key=None, val=None, **kwargs):
        
            if val is None:
                val = self.kwdict(**kwargs)

            try:
                style[id]
            except BaseException:
                style[id] = Style(style.default)
            
            if key is not None:
                holder = style[id][key]
            else:
                holder = style[id]

            try: 
                holder.xpos = val['x']
                del val['x']
            except: pass
            try: 
                holder.ypos = val['y']
                del val['y']
            except: pass

            try: 
                holder.xsize = val['w']
                del val['w']
            except: pass

            try: 
                holder.ysize = val['h']
                del val['h']
            except: pass

            try: 
                holder.padding = val['p']
                del val['p']
            except: pass

            for s in self.styleref():
                try: 
                    setattr(holder,s,val[s])
                    del val[s]
                except: pass
                
            for v in val:
            
                if not isinstance(val[v],(str,int,unicode,tuple)):
                    self.style(id, v, val[v])
                

        def getdir(self):
            return re.sub(r'^game/','',os.path.dirname(renpy.get_filename_line()[0])) + "/"
            
        def files(self, where=False, key=False, ext=False):
            """ 
            Return file list from `persisten.files`
            
            ``` python
                file = raut.files('gui','bar','png')
            ```
            
            * return files inside 'gui/' which has 'bar' in filename(including his path), and end with 'png'
            * ramen's framework work best with namespaces in mind.
            
            """
            
            F = persistent.files
            if where: F = filter(lambda w: where+"/" in w, sorted(F))
            if key: F = filter(lambda w: key in w, F)
            if ext: F = filter(lambda w: w.endswith(ext), F)
            
            return F        
            
        def file_info(self,file):
            """
            Get and extract the file information of the file as dict.
            
            ``` python:
                info = raut.file_info("e:/yourproject/game/npc/girls_of_90/alpha/lucy smile.png")
            ```
            
            * info['file'] = lucy smile.png
            * info['name'] = lucy smile
            * info['ext'] = png
            * info['dir'] = npc/girl_of_90
            * info['path'] = alpha
            
            Note: `dir` and `path` doesn't had trailing slash.

            """

            r = {}
            r[str('path')] = os.path.dirname(file)
            r[str('file')] = os.path.basename(file)
            a = r['file'].split('.')
            r[str('name')] = str(a[0])
            r[str('ext')] = str(a[1])
            r[str('dir')] = str(r['path'])
            r[str('path')] = r['path'].replace(
                os.path.dirname(r['path']) + "/", '')
            return r

        def limits(self, value, min=RAMEN_INTMIN, max=RAMEN_INTMAX):
            if int(value) < min:
                return min
            elif int(value) > max:
                return max
            else:
                return int(value)

        def toggle(self,what,key):
            
            try: 
                try: 
                    what[key]
                except:
                    what[key] = True
            
                if what[key]: what[key] = False
                else: what[key] = True
                
                return what[key]
            except:
                return False
            
        def pref_toggle(self,what):
            
            try: 
                persistent.pref[what]
            except:
                persistent.pref[what] = True
            
            if persistent.pref[what]:
                persistent.pref[what] = False
            else:
                persistent.pref[what] = True
                
            return persistent.pref[what]

        def cycle(self,current,array):
            current = int(current) + 1
            if current >= len(array) or current < 0: 
                current = 0
            return int(current)
        
        def random_int(self, min=0, max=100):
            return int(renpy.random.randint(min, max))

        def random_of(self, array):
            return array[int(renpy.random.randint(0, len(array)-1))]

        def safestr(self, str=''):
            return re.sub(r'\W+', '',str.lower())

        def character(self, id, name, **kwargs):
            """Define character"""
            chaattr = {}
            for k in kwargs:
                for c in ['dynamic', 'window_', 'who_',
                          'what_', 'show_', 'cb_', 'ctc_']:
                    if k.startswith(c):
                        chaattr[k] = kwargs[k]

            setattr(
                character,
                id,
                Character(
                    name.lower().strip(),
                    image=id,
                    **chaattr
                )
            )

    raut = ramen2_util()
    