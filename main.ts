input.onButtonPressed(Button.A, function () {
    POLL2 = false
    basic.showIcon(IconNames.No)
    Red2 = -1
    Green2 = -1
    Blue2 = -1
})

input.onButtonPressed(Button.B, function () {
    POLL2 = true
    basic.showIcon(IconNames.Yes)
})

let Blue2 = -1
let Green2 = -1
let Red2 = -1
let POLL2 = false

basic.forever(function () {
    while (POLL2) {
        basic.showIcon(IconNames.Heart)
        Red2 = envirobit.getRed()
        Green2 = envirobit.getGreen()
        Blue2 = envirobit.getBlue()
        serial.writeLine("Red: " + Red2)
        serial.writeLine("Blue: " + Blue2)
        serial.writeLine("Green: " + Green2)
        Red2 = 0
        Green2 = 0
        Blue2 = 0
        basic.pause(1000)
    }
})
