radio.onReceivedNumber(function (receivedNumber) {
    potato = receivedNumber
})
input.onButtonPressed(Button.A, function () {
	
})
input.onGesture(Gesture.Shake, function () {
    if (potato > 0) {
        radio.sendNumber(potato)
        potato = -1
    } else {
        potato = 0
    }
})
input.onButtonPressed(Button.AB, function () {
    potato = randint(10, 20)
})
let potato = 0
potato = -1
radio.setGroup(1)
basic.forever(function () {
    if (potato == 0) {
        basic.showIcon(IconNames.No)
    }
    if (potato < 0) {
        basic.clearScreen()
    }
    if (potato > 0) {
        basic.showIcon(IconNames.Chessboard)
        potato += -1
    }
})
