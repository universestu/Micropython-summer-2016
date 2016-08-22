from machine import UART
import socket
import network
import time

uart = UART(0)
    
def uarttest():
    while True:
        data = uart.read(1000)
        if data != None:
            a = str(data[2:])
            b = a.split('\'')
            c = b[1].split('\\')
            d = c[0].split(',')
            print(data)
            print(str(data[0:2]))
            print(d[0])
            print(d[1])
    
    
