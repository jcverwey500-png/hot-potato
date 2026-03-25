let _set = 0
let timer = 0
let decrease = 0
input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.Happy)
    _set = randint(5, 15)
    while (true) {
        timer = 0
    }
    while (false) {
        decrease = 0
        basic.pause(1000)
        basic.showIcon(IconNames.Sad)
    }
})
