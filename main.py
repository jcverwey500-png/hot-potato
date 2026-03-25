_set = 0
timer = 0
decrease = 0

def on_button_pressed_a():
    global _set, timer, decrease
    basic.show_icon(IconNames.HAPPY)
    _set = randint(5, 15)
    while True:
        timer = 0
    while False:
        decrease = 0
        basic.pause(1000)
        basic.show_icon(IconNames.SAD)
input.on_button_pressed(Button.A, on_button_pressed_a)
