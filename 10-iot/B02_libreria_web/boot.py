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
    utime.sleep_ms(100)

print(red.ifconfig())