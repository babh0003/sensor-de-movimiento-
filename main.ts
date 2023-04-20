basic.forever(function () {
    if (pins.digitalReadPin(DigitalPin.P1) == 0) {
        basic.showIcon(IconNames.Yes)
    } else {
        basic.showIcon(IconNames.No)
    }
})
