import time
import ubinascii
from simple import MQTTClient
from machine import Pin, unique_id, ADC
SERVER = "broker.mqttdashboard.com"
CLIENT_ID = ubinascii.hexlify(unique_id())
TOPIC = b"huzzah"
adc = ADC(0)

def main(server=SERVER):
    c = MQTTClient(CLIENT_ID, server)
    c.connect()
    print("Connected to %s, waiting for timer" % server)
    fail = False
    count = 0
    while True:
        count += 1
        time.sleep_ms(5000)
        value = str(adc.read())
        print("Time to publish")
        try:
            if fail:
                print('Attempt to reconnect')
                c.connect()
                print('Reconnected to Huzzah')
        except OSError:
            print('Reconnect fail')
        try:
            c.publish(TOPIC, (value +' count '+str(count)).encode('UTF8'))
            print('Publish ' + value)
            fail = False
        except OSError:
            fail = True

    c.disconnect()