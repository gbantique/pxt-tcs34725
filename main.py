def on_button_pressed_a():
    global POLL2, Red2, Green2, Blue2
    POLL2 = False
    basic.show_icon(IconNames.NO)
    Red2 = -1
    Green2 = -1
    Blue2 = -1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global POLL2
    POLL2 = True
    basic.show_icon(IconNames.YES)
input.on_button_pressed(Button.B, on_button_pressed_b)

Blue2 = 0
Green2 = 0
Red2 = 0
POLL2 = False
# let Blue = 0
# let Green = 0
# let Red = 0
# let POLL = false
POLL2 = False
Red2 = -1
Green2 = -1
Blue2 = -1

def on_forever():
    global Red2, Green2, Blue2
    while POLL2:
        #basic.show_icon(IconNames.HEART)
        Red2 = envirobit.get_red()
        Green2 = envirobit.get_green()
        Blue2 = envirobit.get_blue()
        serial.write_line("Red: " + str(Red2))
        serial.write_line("Blue: " + str(Blue2))
        serial.write_line("Green: " + str(Green2))
        Red2 = 0
        Green2 = 0
        Blue2 = 0
        basic.pause(1000)
basic.forever(on_forever)
