import machine, neopixel, time, random
# Creado por Daniel Alvarez (danidask@gmail.com) para curso de Python de EOI (eoi.es)

# Instanciamos el objeto NeoPixel diciendole donde esta el pin de datos de los neopixeles, y cuantos neopixeles hay
np = neopixel.NeoPixel(machine.Pin(27), 1)  # La placa Atom Lite tiene un neopixel en el GPIO 27

while True:  # bucle infinito
    np[0] = (255, 255, 0)  # escojemos el color rgb del primer neopixel (la placa atom lite solo tiene uno)
    np.write()  # despues de elegir los colores de todos los leds, los mandamos con este comando
    print("Neopixel en amarillo (rojo y verde al maximo, y azul apagado)")
    time.sleep_ms(2000)

    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    np[0] = (red, green, blue)
    np.write()
    print("Color aleatorio {}, {}. {}".format(red, green, blue))
    time.sleep_ms(2000)

    np[0] = (0,0,0)
    np.write()
    print("Neopixel apagado")
    time.sleep_ms(2000)
