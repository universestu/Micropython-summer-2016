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

def connectsend(): 
    GET = 'update?key=SPOA89HOE84P6NXJ&field1='
    host = 'data.learninginventions.org'
    addr = socket.getaddrinfo(host, 80)[0][-1]
    adc = machine.ADC(0)
    value = '0'
    i=0
    wlan = network.WLAN(network.STA_IF) 
    if not wlan.isconnected():
        wlan.active(True)
        wlan.connect('gogo_mt', 'ilovecpeilovecpe')  
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig()) 
    while wlan.isconnected():
        value = str(adc.read())
        s = socket.socket()
        s.connect(addr)
        s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (GET+value, host), 'utf8'))
        toggle(pin)
        time.sleep(5)
        s.close()
        time.sleep(10)
    machine.reset()

def main():
    try:
        connectsend()
    except:
        import machine
        machine.reset()

        



    
