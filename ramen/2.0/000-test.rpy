init python:

    print "*** New Testramen ***"

    print 'ramen_object'
    
    a = ramen2_object('apa')
    a.x=1
    a.persistent('prop')
    a.prop.x=2
    a.multipersistent('var')
    a.var.x=3

    b = ramen2_object('beh')
    b.x=4
    b.persistent('prop')
    b.prop.x=5
    b.multipersistent('var')
    b.var.x=6
    
    res = "a="
    res += repr( a())
    res += repr( a.prop())
    res += repr( a.var())
    
    print res
    
    res = "b="
    res += repr( b())
    res += repr( b.prop())
    res += repr( b.var())
    
    print res



    