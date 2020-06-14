from machine import Timer
import utime


tim1 = Timer(-1)  # -1 para timer virtual (basado en RTOS)
tim1.init(period=2500, mode=Timer.ONE_SHOT, callback=lambda x:print("#### esto solo se ejecuta una vez"))
tim2 = Timer(-1)
tim2.init(period=1000, mode=Timer.PERIODIC, callback=lambda x:print("esto se ejecutara periodicamente"))

print("inicio")
utime.sleep(10)  # podemos hacer otras cosas
tim2.deinit()  # desactivamos el timer periodico
print("fin")
