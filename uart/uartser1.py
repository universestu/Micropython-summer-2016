from machine import UART
uart = UART(0)
def main():
    print('start...')
    while True:
        data = uart.read(100)
        if data != None:
            print(data)
            print(data[0])
            print(data[1])
            d = data[0]==5
            f = data[1]==223
            if d and f:
                print(data[2:])
            
        
    

