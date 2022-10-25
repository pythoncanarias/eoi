# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
import network
import utime
from credenciales import ssid, password

red = network.WLAN(network.STA_IF)
red.active(True)
red.connect(ssid, password)

while not red.isconnected():
    utime.sleep_ms(50)
    if utime.ticks_ms() > 10000:  # timeout de 10 segundos
        print("ERROR no se ha podido conectar a la wifi {}".format(ssid))
        break
else:
    print(red.ifconfig())
