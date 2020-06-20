from machine import RTC
from utime import sleep


# la conexion a wifi la hace en boot.py

rtc = RTC()  # instanciamos el Real Time Clock
rtc.datetime((2020,6,15,19,1,0,0,0))  # podemos configurar la hora manualmente
print(rtc.datetime())

import ntptime
ntptime.host  # muestra el servidor ntp que vamos a usar
ntptime.settime() # actualizamos la fecha/hora desde el servidor ntp (necesitamos conexion a internet)
print(rtc.datetime())
print(ntptime.time())  # tiempo unix (segundos desde 1/1/1970 0:00:00 UTC+0)


# while True:
#     sleep(0.1)

