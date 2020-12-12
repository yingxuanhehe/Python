from sense_hat import SenseHat
import time
import random
sense = SenseHat()

R = (255, 0, 0)
G = (0, 255, 0)
O = (0, 0, 0)
W = (255, 255, 255)
checkRotation = 0
colors = [R, G, W]
orientation = [0, 90, 180, 270]

def image():
    image_pixels = [
    O, O, O, O, O, O, O, O,
    O, O, O, X, O, O, O, O,
    O, O, X, X, X, O, O, O,
    O, X, O, X, O, X, O, O,
    O, O, O, X, O, O, O, O,
    O, O, O, X, O, O, O, O,
    O, O, O, X, O, O, O, O,
    O, O, O, X, O, O, O, O]
    return image_pixels

while True:
    arrowRotation = orientation[random.randint(0, 3)]
    sense.clear()
    X = G
    sense.set_pixels(image())

    if arrowRotation == checkRotation:          #to prevent same orientation for two continuous times
        continue
    else:
        sense.set_rotation(arrowRotation)

    time.sleep(10)
    checkRotation = arrowRotation               #to prevent same orientation for two continuous times
    acceleration = sense.get_accelerometer_raw()
    x = round(acceleration['x'])
    y = round(acceleration['y'])

    if arrowRotation == 0 and x == 0 and y == 1:
        continue
    elif arrowRotation == 90 and x == -1 and y == 0:
        continue
    elif arrowRotation == 180 and x == 0 and y == -1:
        continue
    elif arrowRotation == 270 and x == 1 and y == 0:
        continue

    else:
        X = R
        sense.set_pixels(image())
        break