from machine import I2C, Pin
from utime import sleep_ms
from mpu6886 import MPU6886
# Creado por Daniel Alvarez (danidask@gmail.com) para curso de Python de EOI (eoi.es)

i2c = I2C(0, scl=Pin(32), sda=Pin(26))
sensor = MPU6886(i2c)

print("MPU6886 id: " + hex(sensor.whoami))

while True:
    ax, ay, az = sensor.acceleration
    gx, gy, gz = sensor.gyro
    print(f"ax {ax:6.2f}  ay {ay:6.2f}  az {az:6.2f}  gx {gx:6.2f}  gy {gy:6.2f}  gz {gz:6.2f}  temp {sensor.temperature:.1f}")
    # print(sensor.acceleration)
    # print(sensor.gyro)
    # print(sensor.temperature)
    sleep_ms(500)
