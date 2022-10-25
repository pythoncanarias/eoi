from machine import RTC
from utime import sleep
# Creado por Daniel Alvarez (danidask@gmail.com) para curso de Python de EOI (eoi.es)
# https://docs.micropython.org/en/latest/library/pyb.RTC.html

# la conexion a wifi la hace en boot.py

rtc = RTC()  # instanciamos el Real Time Clock
rtc.datetime((2020,6,15,19,1,0,0,0))  # podemos configurar la hora manualmente
print(rtc.datetime())

import ntptime
print(ntptime.host)  # muestra el servidor ntp que vamos a usar
ntptime.settime() # actualizamos la fecha/hora desde el servidor ntp (necesitamos conexion a internet)
# (year, month, day, weekday*, hours, minutes, seconds, subseconds*)
print(rtc.datetime())
print(ntptime.time())  # tiempo unix (segundos desde 1/1/1970 0:00:00 UTC+0)
