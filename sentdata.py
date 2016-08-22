import machine
import time
import socket
import esp
import network
def senddata(v):
    value = str(v)
    GET = 'update?key=E5JNXV8S63PYUUCW&field1='
    host = 'data.learninginventions.org'
    addr = socket.getaddrinfo(host, 80)[0][-1]
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


#uart.write('import sentdata')
#uart.write('sentdata.senddata('+'230'+')\r\n')
