import time
import ubinascii
from simple import MQTTClient
from machine import Pin, unique_id, UART
import network
import config
SERVER = "188.166.233.211"
CLIENT_ID = ubinascii.hexlify(unique_id())
TOPIC = config.value[1]
TOPICCMD = config.value[2]
uart = UART(0)

def main(server=SERVER):
    print(config.value)
    wlan = network.WLAN(network.STA_IF) 
    if not wlan.isconnected():
        wlan.active(True)
        wlan.connect(config.value[0][1], config.value[0][2])
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig()) 
    c = MQTTClient(CLIENT_ID, server)
    c.connect()
    print("Connected to %s, waiting for timer" % server)
    value = '0'
    data = uart.read(100)
    while wlan.isconnected():
        data = uart.read(100)
        if data != None:
            a = str(data[2:])
            b = a.split('\'')
            e = b[1].split('\\')
            d = e[0].split(',')
            if d[0]=='IR':
                print(d[0])
                print(d[1])
                if d[1] == '128':
                    c.publish(config.value[2][1],"ON",retain=True)
                    c.publish(config.value[1][1],"Remote",retain=True)
                    print(d[1])
                if d[1] == '129':
                    c.publish(config.value[2][1],"OFF",retain=True)
                    c.publish(config.value[1][1],"Remote",retain=True)
                    print(d[1])
                if d[1] == '130':
                    c.publish(config.value[2][2],"ON",retain=True)
                    c.publish(config.value[1][2],"Remote",retain=True)
                    print(d[1])
                if d[1] == '131':
                    c.publish(config.value[2][2],"OFF",retain=True)
                    c.publish(config.value[1][2],"Remote",retain=True)
                    print(d[1])
                print("Time to publish")      
    c.disconnect()
