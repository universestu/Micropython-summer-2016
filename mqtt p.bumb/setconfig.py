import time
import ubinascii
from simple import MQTTClient
from machine import Pin, unique_id, UART
import network
SERVER = "188.166.233.211"
TOPIC = b"WRAT/simpleDemo1/floor1/room101/power/ORIGIN"
SSID = ""
PASS = ""
uart = UART(0)
config = [[],[],[]]
    

def main():
    while True:
        data = uart.read(1000)
        if data != None:
            a = str(data[2:])
            b = a.split('\'')
            e = b[1].split('\\')
            d = e[0].split(',')
            if d[0]=='IR':
                print(d[0])
                print(d[1])
            if d[0]=='SERVER':
                config[0].append(d[0])
                config[0].append(d[1])
                print(config)
            if d[0]=='TOPIC':
                config[1].append(d[0])
                config[1].append(d[1])
                print(config)
            if d[0]=='SSID':
                config[2].append("WIFI")
                config[2].append(d[1])
                print(config)
            if d[0]=='PASS':
                config[2].append(d[1])
                print(config)
                break
            
        

