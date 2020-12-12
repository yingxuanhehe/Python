from sense_hat import SenseHat
import time
import random
sense = SenseHat()

R = (255, 0, 0)
G = (0, 255, 0)
B = (0, 0, 255)
Y = (255, 255, 0)
O = (0, 0, 0,)
W = (255, 255, 255)

colours = [R, G, B, W, Y]
rotation = [0, 90, 180, 270]

while True:
    sense.clear()
    X = colours[random.randint(0, 4)]

    image_pixels = [
    O, O, O, O, O, O, O, O,
    O, O, O, X, O, O, O, O,
    O, O, X, X, X, O, O, O,
    O, X, O, X, O, X, O, O,
    O, O, O, X, O, O, O, O,
    O, O, O, X, O, O, O, O,
    O, O, O, X, O, O, O, O,
    O, O, O, X, O, O, O, O]

    sense.set_pixels(image_pixels)
    sense.set_rotation(rotation[random.randint(0, 3)])
    time.sleep(1)
