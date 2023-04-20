def on_forever():
    if pins.digital_read_pin(DigitalPin.P1) == 0:
        basic.show_icon(IconNames.YES)
    else:
        basic.show_icon(IconNames.NO)
basic.forever(on_forever)
