import time
import ubinascii
from simple import MQTTClient
from machine import Pin, unique_id, UART
import network
SERVER = "188.166.233.211"
CLIENT_ID = ubinascii.hexlify(unique_id())
TOPIC = b"WRAT/simpleDemo1/floor1/room101/power/ORIGIN"

uart = UART(0)

def main(server=SERVER):
    wlan = network.WLAN(network.STA_IF) 
    if not wlan.isconnected():
        wlan.active(True)
        wlan.connect('Micropython-wifi', '12345678')  
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig()) 
    c = MQTTClient(CLIENT_ID, server)
    c.connect()
    print("Connected to %s, waiting for timer" % server)
    fail = False
    count = 0
    value = '0'
    data = uart.read(100)
    c.publish(TOPIC,value,retain=True);
    time.sleep(1);
    c.disconnect()
