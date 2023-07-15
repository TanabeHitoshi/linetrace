def 左モーター(数値: number):
    if 数値 == 0:
        pins.digital_write_pin(DigitalPin.P15, 0)
    elif 数値 > 0:
        pins.analog_write_pin(AnalogPin.P15, 数値)
        pins.digital_write_pin(DigitalPin.P16, 1)
    else:
        pins.analog_write_pin(AnalogPin.P15, abs(数値))
        pins.digital_write_pin(DigitalPin.P16, 0)
def 右モーター(数値2: number):
    if 数値2 == 0:
        pins.digital_write_pin(DigitalPin.P13, 0)
    elif 数値2 > 0:
        pins.analog_write_pin(AnalogPin.P13, 数値2)
        pins.digital_write_pin(DigitalPin.P14, 0)
    else:
        pins.analog_write_pin(AnalogPin.P13, abs(数値2))
        pins.digital_write_pin(DigitalPin.P14, 1)

def on_forever():
    custom.左モーター(500)
    custom.右モーター(500)
basic.forever(on_forever)
