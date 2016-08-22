import machine
import time
import socket
import esp
import network
import dht

pin = machine.Pin(5, machine.Pin.OUT)
def toggle(p):
    p.value(not p.value())
    time.sleep_ms(500)
    p.value(not p.value())
    time.sleep_ms(500)

def connectsend():
    wlan = network.WLAN(network.STA_IF) 
    wlan.active(True)       
    wlan.scan()            
    wlan.isconnected()      
    wlan.connect('gogo_mt', 'ilovecpeilovecpe')    
    wlan.ifconfig() 
    GET = 'update?key=SPOA89HOE84P6NXJ&field1='
    f2 = '&field2='
    f3 = '&field3='
    host = 'data.learninginventions.org'
    addr = socket.getaddrinfo(host, 80)[0][-1]
    adc = machine.ADC(0)
    sensordht = dht.DHT22(machine.Pin(2))
    value = '0'
    i=0
    while wlan.isconnected():
        sensordht.measure()
        value1 = str(adc.read())
        value2 = str(sensordht.temperature())
        value3 = str(sensordht.humidity())
        s = socket.socket()
        s.connect(addr)
        s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (GET+value1+f2+value2+f3+value3, host), 'utf8'))
        toggle(pin)
        s.close()
        print(GET+value1+f2+value2+f3+value3)
        print('ILoveCPE')
        i+=1
        print('---',i)
        time.sleep(15)
    machine.reset()

def main():
    try:
        connectsend()
    except:
        import machine
        machine.reset()

        



    
