import utime
from kappa import Kappa
from miscelanea import LedRGB, Boton
# Creado por Daniel Alvarez (danidask@gmail.com) para curso de Python de EOI (eoi.es)


led = LedRGB()
web = Kappa()

def home(x):
    contexto = {
        "tiempo": str(utime.ticks_ms() // 1000),
    }
    return("index.html", contexto)

def led_encender(x):
    led.encender()
    contexto = {}
    return("luz.html", contexto)

def led_apagar(x):
    led.apagar()
    contexto = {}
    return("luz.html", contexto)


web.add_view("/", home)
web.add_view("/encender", led_encender)
web.add_view("/apagar", led_apagar)

web.run_server()
