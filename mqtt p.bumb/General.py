import os
passwd1 = "1234"
with open("port_config.py", "w") as f:
        f.write("WEBREPL_PASS = %r\n" % passwd1)
        
wifiValue = "Micropython"
with open("config.py", 'w') as f:
        f.write("WIFI = %r\n" % wifiValue)
topicValue = "WRAT/simpleDemo1/floor1/room101/power/ORIGIN"
with open("config.py", 'a') as f:
        f.write("TOPIC = %r\n" % topicValue)
server = "188.166.233.211"
with open("config.py", 'a') as f:
        f.write("SERVER = %r\n" % server)

        
f = open("port_config.py")
f.read()

port_config.WEBREPL_PASS

import network
sta_if = network.WLAN(network.STA_IF)
sta_if.active(1)
sta_if.connect('gogo','ilovecpe')


import os
value = [["WIFI","gogo_mt","ilovecpe"],
          ["TOPIC","WRAT/simpleDemo1/floor1/room101/power/ORIGIN","WRAT/simpleDemo1/floor1/room102/power/ORIGIN"],
            ["TOPICCMD","WRAT/simpleDemo1/floor1/room101/power/CMD","WRAT/simpleDemo1/floor1/room102/power/CMD"],
          ["server","188.166.233.211"]]
with open("config.py", 'w') as f:
        f.write("value = %r" % value)

        
for i in range(0,2):
    for j in range(0,2): 
        config[i].append("Micropython")

if config[0]:
    print("havedata")
