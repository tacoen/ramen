init python:

    event_test = event(
        'test',
        label='white_room',
        day=2,
        require={
            'hygiene': 2},
        call='eventest')



label eventest:
    "You see a event occur here."
    "nice?"

    # infinite loop aware
    $ event_test.set_pass()

    "Now back to last label"

    return

