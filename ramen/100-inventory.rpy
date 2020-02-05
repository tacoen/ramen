init -99 python:

    pocket = inventory('pocket')
    kondom = item(id='kondom',cost=20,count=3)

    shrte01 = item(id='sh-rte-1',cost=25,count=1,effect=['stat','energy',3],desc='Honey Pork Noddle')
    shrte02 = item(id='sh-rte-2',cost=26,count=1,effect=['stat','energy',3],desc='Spaghetti Carbonarra')
    shrte03 = item(id='sh-rte-3',cost=27,count=1,effect=['stat','energy',3],desc='Spicy Beef Rendang')

    pocket.add(kondom)
    pocket.add(shrte01)
    pocket.add(shrte02)
    pocket.add(shrte03)