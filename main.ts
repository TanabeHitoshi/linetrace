function 右手 () {
    if (pins.analogReadPin(AnalogPin.P2) < 100) {
        basic.pause(10)
        if (pins.analogReadPin(AnalogPin.P2) < 100) {
            state = "on"
        }
    }
    if (pins.analogReadPin(AnalogPin.P2) > 300 && state == "on") {
        右手回数 += 1
        state = "off"
        custom.走る(0, 0)
    }
    return 右手回数
}
let 右手回数 = 0
let state = ""
let スピード = 300
basic.forever(function () {
    custom.走る(スピード, custom.ライン位置() * 0.15)
    右手()
    while (右手回数 >= 5) {
        custom.走る(スピード, 0)
        basic.pause(1000)
        while (true) {
            custom.走る(0, 0)
        }
    }
})
