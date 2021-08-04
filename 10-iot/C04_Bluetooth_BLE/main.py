# Este ejemplo muestra como crear un dispositivo BLE que emule un sensor de temperatura.
# El valor local del sensor se actualiza cada segundo, y notifica cada 10 segundos
# Codigo original https://github.com/lemariva/uPyM5BLE
# Modificaciones y comentarios por Daniel Alvarez (danidask@gmail.com) para curso de Python de EOI (eoi.es)

import bluetooth
import random
import struct
import binascii
import utime
from ble_advertising import advertising_payload
from micropython import const

_IRQ_CENTRAL_CONNECT = const(1 << 0)
_IRQ_CENTRAL_DISCONNECT = const(1 << 1)

# org.bluetooth.service.environmental_sensing
_ENV_SENSE_UUID = bluetooth.UUID(0x181A)
# org.bluetooth.characteristic.temperature
_TEMP_CHAR = (bluetooth.UUID(0x2A6E), bluetooth.FLAG_READ | bluetooth.FLAG_NOTIFY,)
_ENV_SENSE_SERVICE = (_ENV_SENSE_UUID, (_TEMP_CHAR,),)

# org.bluetooth.characteristic.gap.appearance.xml
_ADV_APPEARANCE_GENERIC_THERMOMETER = const(768)


class BLETemperature:
    """ Notifica temperatura por BLE """

    def __init__(self, ble, name):
        """
        object constructor
        :param ble: instancia de BLE
        :param name: (string) nombre con el que se va a publicitar
        """
        self._ble = ble
        self._ble.active(True)
        self._connections = set()
        self._ble.irq(self._irq)
        ((self._handle,),) = self._ble.gatts_register_services((_ENV_SENSE_SERVICE,))
        self._connections = set()
        self._payload = advertising_payload(name=name, services=[_ENV_SENSE_UUID], appearance=_ADV_APPEARANCE_GENERIC_THERMOMETER)
        self._advertise()

    def _irq(self, event, data):
        # Track connections so we can send notifications.
        if event == _IRQ_CENTRAL_CONNECT:
            conn_handle, _, _, = data
            self._connections.add(conn_handle)
        elif event == _IRQ_CENTRAL_DISCONNECT:
            conn_handle, _, _, = data
            self._connections.remove(conn_handle)
            # Start advertising again to allow a new connection.
            self._advertise()

    def set_temperature(self, temp_deg_c, notify=False):
        # Data is sint16 in degrees Celsius with a resolution of 0.01 degrees Celsius.
        # Write the local value, ready for a central to read.
        temp_sint16 = struct.pack('<h', int(temp_deg_c * 100))
        self._ble.gatts_write(self._handle, temp_sint16)
        # representacion hexadecimal del valor que enviamos con el mismo formato que veremos en BLE Scanner
        print("DEBUG sent 0x{}".format(binascii.hexlify(temp_sint16).decode().upper()))
        if notify:
            for conn_handle in self._connections:
                # Notify connected centrals to issue a read.
                self._ble.gatts_notify(conn_handle, self._handle)

    def _advertise(self, interval_us=500000):
        self._ble.gap_advertise(interval_us, adv_data=self._payload)


if __name__ == "__main__":
    ble = bluetooth.BLE()
    termometro = BLETemperature(ble, 'curso-eoi')

    temperatura = 25  # temepratura inicial
    i = 0

    while True:
        # Escribe cada segundo, notifica cada 10 segundos.
        utime.sleep_ms(1000)
        i += 1
        # Alteramos ligeramente la temperatura ficticia (Random walk)
        temperatura += random.uniform(-0.5, 0.5)
        notificar = i % 10 == 0  # Usamos el operador modulo que resultara en 0 cada 10 veces
        print("Enviado temperatura {:.2f} notificar {}".format(temperatura, notificar))
        termometro.set_temperature(temperatura, notify=notificar)
