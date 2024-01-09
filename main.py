def on_received_number(receivedNumber):
    global potato
    potato = receivedNumber
radio.on_received_number(on_received_number)

def on_gesture_shake():
    global potato
    if potato > 0:
        potato = -1
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_ab():
    global potato
    potato = randint(10, 20)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

potato = 0
potato = -1
radio.set_group(1)
potato = 0

def on_forever():
    global potato
    if potato == 0:
        basic.show_icon(IconNames.SKULL)
    if potato < 0:
        basic.clear_screen()
    if potato > 0:
        basic.show_icon(IconNames.CHESSBOARD)
        potato += -1
basic.forever(on_forever)
