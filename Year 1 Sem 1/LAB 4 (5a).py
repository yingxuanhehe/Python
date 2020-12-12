#5a-1
from sense_hat import SenseHat
sense = SenseHat()

red = (255, 0, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

sense.set_pixel(0, 0, red)
sense.set_pixel(7, 0, yellow)
sense.set_pixel(0, 7, blue)
sense.set_pixel(7, 7, green)

#5a-2
from sense_hat import SenseHat
from time import sleep
from random import randint
sense = SenseHat()

red = (255, 0, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

x1 = randint(0, 7)
y1 = randint(0, 7)
x2 = randint(0, 7)
y2 = randint(0, 7)
x3 = randint(0, 7)
y3 = randint(0, 7)
x4 = randint(0, 7)
y4 = randint(0, 7)

sense.set_pixel(x1, y1, red)
sense.set_pixel(x2, y2, yellow)
sense.set_pixel(x3, y3, blue)
sense.set_pixel(x4, y4, green)

sleep(1)
sense.clear()