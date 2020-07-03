## DESARROLLO DE VIDEOJUEGOS CON PYGAME

Desarrollo de pequeños videojuegos con PyGame https://www.pygame.org/

Pygame es un conjunto de módulos para desarrollo de videojuegos y aplicaciones multimedia que añade funcionalidad sobre libSDL (https://www.libsdl.org/). 

Instalación:

python3 -m pip install -U pygame --user

python3 -m pygame.examples.aliens

## TEMARIO

1. Instalación de pygame
2. Hello World! Dibujar una cara con primitivas
3. Juego: Snake
	- Movimiento en rejilla
	- Comer y crecer
	- Puntos y fin de partida
	- Pantalla de inicio, final y UI
4. Juego: Arkanoid
	- Pala del jugador: movimiento continuo con velocidad y aceleración
	- Bola: aritmética de vectores para velocidad
	- Colisiones sprite-grupo
	- Ladrillos: colisiones grupo-grupo
	- Resolución de colisión bola-ladrillos
	- Gráficos, FX, música
5. Prototipo: Plataformas básico
	- Carga de mapas desde fichero
	- Movimiento del jugador en 2D
	- Resolución de colisiones
	- Gravedad
	- Salto proporcional al tiempo de pulsación
6. Juego: PEWPEWPEW!
	- Criaturas perseguidoras
	- Nidos generadores de criaturas
	- Más aritmética de vectores: criaturas que esquivan criaturas
	- Balas, disparos y destrucción
	- Generación procedural de cuevas
	- Items: inmediatos (salud) y temporales (velocidad)
	- Armas
	- Criaturas que disparan