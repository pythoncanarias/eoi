# This file is executed on every boot (including wake-boot from deepsleep)
import esp
esp.osdebug(None)
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
#import webrepl
#webrepl.start()
gc.collect()
print()
