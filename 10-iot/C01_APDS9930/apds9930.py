import utime
from micropython import const


# NOTA esto no es una libreria completa, es un ejemplo parcial para ilustrar lo que es el protocolo I2C
# se puede encontrar una libreria mas completa y funcional aqui:
# https://github.com/micropython-Chinese-Community/mpy-lib/tree/master/sensor/APDS9930


class APDS9930:
    I2C_ADDRESS = const(0x39)  # (57 en decimal) es la direccion de este sensor que es fija y no se puede cambiar
    # utilizamos const para indicar que es un valor fijo que no va a cambiar nunca. Es mas eficiente en memoria
    def __init__(self, i2c):
        self.i2c = i2c
        # Todo esto es la inicializacion del sensor segun viene descrita en el datasheet pagina 15
        ATIME = 0xFF # 2.7 ms – minimum ALS integration time
        WTIME = 0xFF # 2.7 ms – minimum Wait time
        PTIME = 0xFF # 2.7 ms – minimum Prox integration time
        PPULSE = 1 # Minimum prox pulse count
        self._write_reg_data(0, 0)  # Disable and Powerdown
        self._write_reg_data (0x01, ATIME)
        self._write_reg_data (0x02, PTIME)
        self._write_reg_data (0x03, WTIME)
        self._write_reg_data (0x0E, PPULSE)
        PDRIVE = 0  # 100mA of LED Power
        PDIODE = 0x20  # CH1 Diode
        PGAIN = 0  # 1x Prox gain
        AGAIN = 0  # 1x ALS gain
        self._write_reg_data (0x0F, PDRIVE | PDIODE | PGAIN | AGAIN)
        WEN = 8  # Enable Wait
        PEN = 4  # Enable Prox
        AEN = 2  # Enable ALS
        PON = 1  # Enable Power On
        self._write_reg_data(0, WEN | PEN | AEN | PON)  # self._write_reg_data(0, 0x0F)
        utime.sleep_ms(12)  # Wait for 12 ms
        CH0_data = self._read_word(0x14)
        CH1_data = self._read_word(0x16)
        Prox_data = self._read_word(0x18)
        # print(CH0_data)
        # print(CH1_data)
        # print(Prox_data)
    

    def _read_word(self, reg):
        """ Lee un word (2 bytes, 16 bits) de un registro del sensor """
        # es una implementacion del codigo de ejemplo que aparece en el datasheet pag 15
        registro_enmascarado = reg|0xA0  # para enteder esta mascara mirar Command Register pag 19 datasheet
        # al wirteto le pasamos la direccion y los bytes que queremos escribir
        # puede ser en formato b'\x11\x43\xa8' o con bytearray donde le pasamos una lista o tupla con los bytes
        # aunque sea un solo byte se lo tenemos que pasar asi, como lista o tupla (tupla mas eficiente)
        self.i2c.writeto(APDS9930.I2C_ADDRESS, bytearray((registro_enmascarado, )))
        # despues de decirle que registro queremos leer, lo leemos. En este caso como son dos bytes le pasamos
        # un 2 y nos devolvera un bytearray de 2 elementos con la lectura de ese registro y el siguiente
        r = self.i2c.readfrom(APDS9930.I2C_ADDRESS, 2)
        return r[0] + r[1]*256  # convertimos esos dos bytes en un entero (el primero el menos signigicativo)


    def _read_byte(self, reg):
        """ Lee un byte de un registro del sensor """
        # mirar comentarios de _read_word
        self.i2c.writeto(APDS9930.I2C_ADDRESS, bytearray([reg|0xA0]))
        t = self.i2c.readfrom(APDS9930.I2C_ADDRESS, 1)
        return t[0]


    def _write_reg_data(self, reg, data):
        """ Escribe el byte 'data' en un registro del sensor """
        # mirar comentarios de _read_word
        self.i2c.writeto(APDS9930.I2C_ADDRESS, bytearray((reg|0x80, data)))


    def activar_proximidad(self):
        """ Activa el sensor de proximidad """
        # Modificamos los bits necesarios del Enable Register segun indica el datasheet
        Enable_Register = 0x00
        en_reg_data = self._read_byte(Enable_Register)
        # print("antes {0:08b}".format(en_reg_data))  # podemos mostrar como estaba el registro antes de modificarlo
        en_reg_data_enmascarado = en_reg_data | 0b00000100  # con esta mascara (0x04), ponemos el bit Proximity Enable a 1 sin modificar los demas
        # si quisiesemos poner ese bit a 0 sin modificar los demas, utilizariamos esta mascara:
        # en_reg_data = en_reg_data & 0b11111011
        self._write_reg_data(Enable_Register, en_reg_data_enmascarado)
        # print("despues {0:08b}".format(en_reg_data))  # podemos mostrar como estaba el registro despues de modificarlo


    def get_proximidad(self):
        """ Devuelve lectura del sensor de proximidad """
        # lee el dato de 16 bits del registro PDATA
        # NOTA este valor habria que dividirlo por la ganancia, no lo vamos a hacer por simplicidad
        return self._read_word(0x18)  # 0x18 PDATAL, 0x19 PDATAH
