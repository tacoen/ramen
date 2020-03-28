# game definition, please copy this to your working directory

init -99 python:

    RAMEN_COSTOFTIME = False

    wo = WorldTime(
        [2019, 1, 18, 8],
        ['Midnight', 'Dusk', 'Morning', 'Noon', 'Evening', 'Night'],
        ['dark', 'sun1', 'sun2', 'sun3', 'dark']
    )

    mc = player(
        score=0,
        level=0,
        cash=200 + ramu.random_int(50, 99),
        pref=0,
        bank=19000 + ramu.random_int(500, 999)
    )

    mc.set_limit('relation', [0, 20])
    mc.set_limit('stat', [0, 20])

    mc.name = mc_name
    
    mc.setdata('bio',
            lastname=ramu.random_of(['South', 'North', 'East', 'West']),
            job='it'
            )

    mc.setdata('stat',
            hygiene=5,
            energy=5,
            vital=5,
            luck=ramu.random_int(0, 7),
            intelect=ramu.random_int(4, 7),
            )

    mc.pref = {}
    mc.task = {}
    mc.flags = []
    mc.ability = []

    mc.pref['icons'] = ['pocket', 'smp_ui']
    mc.limit['pocket'] = [0, 12]

    pocket = inventory('pocket')

