import machine
import time
import socket
import esp
import network
pin = machine.Pin(5, machine.Pin.OUT)
def toggle(p):
    p.value(not p.value())
    time.sleep_ms(500)
    p.value(not p.value())
    time.sleep_ms(500)
    
def connect():
    wlan = network.WLAN(network.STA_IF) 
    wlan.active(True)       
    wlan.scan()            
    wlan.isconnected()      
    wlan.connect('gogo_mt', 'ilovecpeilovecpe')    
    wlan.ifconfig()

def main():
    connect()
    adc = machine.ADC(0)
    GET = 'update?key=SPOA89HOE84P6NXJ&field1='
    host = 'data.learninginventions.org'
    addr = socket.getaddrinfo(host, 80)[0][-1]
    value = '0'
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)  
    while True:
        if sta_if.isconnected():
            value = str(adc.read())
            print(value)
            print('-gogo-')
            s = socket.socket()
            s.connect(addr)
            s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (GET+value, host), 'utf8'))
            while True:
                data = s.recv(100)
                if data:
                    print(str(data, 'utf8'), end='')
                else:
                    break
            s.close()
            time.sleep(1)
            toggle(pin)
            time.sleep(13)

        else:
            print('connecting to network...')      
            sta_if.connect('gogo_mt', 'ilovecpeilovecpe')
            while not sta_if.isconnected():
                value = str(adc.read())
                print(value)
                print('---')
                s = socket.socket()
                s.connect(addr)
                s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (GET+value, host), 'utf8'))
                while True:
                    data = s.recv(100)
                    if data:
                        print(str(data, 'utf8'), end='')
                    else:
                        break
                s.close()
                toggle(pin)
                toggle(pin)
                pass
        


    
