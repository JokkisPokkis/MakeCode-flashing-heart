def on_forever():
    basic.show_leds("""
        . # . # .
                # . # . #
                # . . . #
                . # . # .
                . . # . .
    """)
    basic.show_leds("""
        . . . . .
                . # . # .
                . . . . .
                . # # # .
                # . . . #
    """)
    basic.show_leds("""
        # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
    """)
    basic.show_string("JOAKIM")
    basic.show_number(6)
basic.forever(on_forever)
