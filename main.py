import lightsensor
import machine
import webrepl
pin = machine.Pin(4, machine.Pin.IN)
if pin.value():
    print('start....')
    webrepl.start()
else:
    lightsensor.connectsend()

    

