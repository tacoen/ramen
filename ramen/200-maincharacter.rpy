init -203 python:

    class player:
    
        def __getattr__(self, key):

            try:
                return self.__dict__['_param'][key]
            except:
                if key in self.__dict__:
                    return self.__dict__[key]
                else:
                    try:
                        # try the character object
                        value = getattr( getattr( character, self._id ), key )
                        if key != 'name':
                            return value
                        # substitute the name (for interpolation/translations)
                        return renpy.substitutions.substitute(value)[0]
                    except:
                        pass
            try:
                return super(object, self).__getattr__(key)
            except:
                return super(object, self).__getattribute__(key)

        def __setattr__(self, key, value):

            if "_" in key:
                self.__dict__[key]=value
            else:
                try:
                    self.__dict__['_param']
                except:
                    self.__dict__['_param'] = {}

                self.__dict__['_param'][key] = value

            if key == "_id":
                globals()['mc_name'] = value


    