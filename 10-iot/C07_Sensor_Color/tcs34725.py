import utime
import ustruct


"""
    Creado por Daniel Alvarez (danidask@gmail.com) para curso de Python de EOI (eoi.es)
    Basado en la libreria de adafruit
    https://github.com/adafruit/micropython-adafruit-tcs34725
"""


# Registros (datasheet Table 3. Register Address)
_COMMAND_BIT = const(0x80)
_REGISTER_ENABLE = const(0x00)
_REGISTER_ATIME = const(0x01)
_REGISTER_AILT = const(0x04)
_REGISTER_AIHT = const(0x06)
_REGISTER_ID = const(0x12)
_REGISTER_APERS = const(0x0c)
_REGISTER_CONTROL = const(0x0f)
_REGISTER_SENSORID = const(0x12)
_REGISTER_STATUS = const(0x13)
_REGISTER_CDATA = const(0x14)
_REGISTER_RDATA = const(0x16)
_REGISTER_GDATA = const(0x18)
_REGISTER_BDATA = const(0x1a)
_ENABLE_AIEN = const(0x10)
_ENABLE_WEN = const(0x08)
_ENABLE_AEN = const(0x02)
_ENABLE_PON = const(0x01)

INTEG_CYCLES_1 = const(0xFF)
INTEG_CYCLES_10 = const(0xF6)
INTEG_CYCLES_42 = const(0xD5)
INTEG_CYCLES_64 = const(0xC0)
INTEG_CYCLES_256 = const(0x00)

_GAINS = (1, 4, 16, 60)
_CYCLES = (0, 1, 2, 3, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60)


class TCS34725:
    def __init__(self, i2c, address=0x29):
        self.i2c = i2c
        self.address = address
        self._active = False
        self.integration_cycles(INTEG_CYCLES_1)
        sensor_id = self.sensor_id()
        if sensor_id not in (0x44, 0x10):
            raise RuntimeError("wrong sensor id 0x{:x}".format(sensor_id))

    def _register8(self, register, value=None):
        register |= _COMMAND_BIT
        if value is None:
            return self.i2c.readfrom_mem(self.address, register, 1)[0]
        data = ustruct.pack('<B', value)
        self.i2c.writeto_mem(self.address, register, data)

    def _register16(self, register, value=None):
        register |= _COMMAND_BIT
        if value is None:
            data = self.i2c.readfrom_mem(self.address, register, 2)
            return ustruct.unpack('<H', data)[0]
        data = ustruct.pack('<H', value)
        self.i2c.writeto_mem(self.address, register, data)

    def active(self, value=None):
        """ Activa o desactiva el sensor """
        if value is None:  # si no se le pasan argumentos, devuelve el estado actual
            return self._active
        value = bool(value)
        if self._active == value:  # si ya estaba en ese estado, no hace nada
            return
        self._active = value
        enable = self._register8(_REGISTER_ENABLE)
        if value:
            self._register8(_REGISTER_ENABLE, enable | _ENABLE_PON)
            utime.sleep_ms(3)
            self._register8(_REGISTER_ENABLE, enable | _ENABLE_PON | _ENABLE_AEN)
        else:
            self._register8(_REGISTER_ENABLE, enable & ~(_ENABLE_PON | _ENABLE_AEN))

    def sensor_id(self):
        return self._register8(_REGISTER_SENSORID)

    def integration_cycles(self, integ_cycles):
        """ Cambiar tiempo de integracion
        pasar constante del tipo tcs34725.INTEG_CYCLES_1
        ver datasheet Table 6. RGBC Timing Register """
        self._register8(_REGISTER_ATIME, integ_cycles)


    def gain(self, value):
        """ Selecciona ganancia entre 1, 4, 16 o 60 
        ver datasheet Table 11. Control Register """
        if value is None:
            return _GAINS[self._register8(_REGISTER_CONTROL)]
        if value not in _GAINS:
            raise ValueError("gain must be 1, 4, 16 or 60")
        return self._register8(_REGISTER_CONTROL, _GAINS.index(value))

    def _valid(self):
        return bool(self._register8(_REGISTER_STATUS) & 0x01)

    def read_rgbc(self):
        was_active = self.active()
        self.active(True)
        while not self._valid():
            utime.sleep_ms(int(self._integration_time + 0.9))
        data = tuple(self._register16(register) for register in (
            _REGISTER_RDATA,
            _REGISTER_GDATA,
            _REGISTER_BDATA,
            _REGISTER_CDATA,
        ))
        self.active(was_active)
        return data

    def read_rgb(self):
        """ Extrae los valores RGB a partir de RGBC"""
        red, green, blue, clear = self.read_rgbc()
        r = pow((int((red/clear) * 256) / 255), 2.5) * 255
        g = pow((int((green/clear) * 256) / 255), 2.5) * 255
        b = pow((int((blue/clear) * 256) / 255), 2.5) * 255
        return int(r), int(g), int(b)

    def read_rgb_alt(self):
        """ Calculo altenativo basado en una libreria de arduino"""
        red, green, blue, clear = self.read_rgbc()
        if (clear == 0):  # si clear es 0 devuelve negro (evita division entre 0)
            return 0, 0, 0
        r = red / clear * 255.0
        g = green / clear * 255.0
        b = blue / clear * 255.0
        return int(r), int(g), int(b)

    def read_temperature_and_lux(self):
        """ Extrae temperaura de color y lumenes a partir de RGBC"""
        r, g, b, c = self.read_rgbc()
        x = -0.14282 * r + 1.54924 * g + -0.95641 * b
        y = -0.32466 * r + 1.57837 * g + -0.73191 * b
        z = -0.68202 * r + 0.77073 * g +  0.56332 * b
        d = x + y + z
        n = (x / d - 0.3320) / (0.1858 - y / d)
        cct = 449.0 * n**3 + 3525.0 * n**2 + 6823.3 * n + 5520.33
        return cct, y
