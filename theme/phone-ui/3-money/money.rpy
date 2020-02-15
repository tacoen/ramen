init -1 python:

    smp.index_update(
        title='My Money',
        hcolor='#2A2',
        order=3,
    )
screen phone_app_money(data=False):

    vbox:
        text "Pocket:" style "phone_label"
        text str(mc.money['cash']) style "phone_light" size 38
        text "Bank:" style "phone_label"
        text str(mc.money['bank']) style "phone_light" size 38
