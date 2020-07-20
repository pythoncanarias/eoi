import uasyncio
from machine import Pin
# Creado por Daniel Alvarez (danidask@gmail.com) para curso de Python de EOI (eoi.es)


async def blink(pin):
    led = Pin(pin, Pin.OUT)
    
    while True:
        led.on()
        await uasyncio.sleep_ms(500)
        led.off()
        await uasyncio.sleep_ms(100)


async def texto():
    for i in range(5):
        print("linea: {}".format(i+1))
        await uasyncio.sleep_ms(1000)


async def main():
    tarea1 = uasyncio.create_task(blink(2))
    tarea2 = uasyncio.create_task(texto())
    # await uasyncio.sleep_ms(10_000)
    await tarea2
    tarea1.cancel()
    
uasyncio.run(main())
