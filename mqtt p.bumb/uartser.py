from machine import UART
import socket
import network
import time

uart = UART(0)
    
def main():
    wlan = network.WLAN(network.STA_IF) 
    if not wlan.isconnected():
        wlan.active(True)
        wlan.connect('gogo_mt', 'ilovecpeilovecpe')  
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig()) 
    while wlan.isconnected():
        data = uart.read(100)
        if data != None:
            a = str(data[2:])
            b = a.split('\'')
            c = b[1].split('\\')
            d = c[0].split(',')
            if d[0]=='field1':
                f1 = d[0]
                v1 = d[1]
                i = 1
            else:
                f2 = d[0]
                v2 = d[1]
                i = 2
                GET = 'update?key=E5JNXV8S63PYUUCW'
                host = 'data.learninginventions.org'
                addr = socket.getaddrinfo(host, 80)[0][-1]
                s = socket.socket()
                s.connect(addr)
                s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (GET+'&'+f1+'='+v1+'&'+f2+'='+v2, host), 'utf8'))
                print(GET+'&'+f1+'='+v1+'&'+f2+'='+v2)
                time.sleep(1)
                s.close()
                i=0
    
    
