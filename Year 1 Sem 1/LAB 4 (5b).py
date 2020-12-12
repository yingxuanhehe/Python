from sense_hat import SenseHat
sense = SenseHat()

y = (255, 255, 0)
b = (0, 0, 0)
image_pixels = [
b, b, b, b, b, b, b, b,
b, b, b, y, b, b, b, b,
b, b, y, y, y, b, b, b,
b, y, b, y, b, y, b, b,
b, b, b, y, b, b, b, b,
b, b, b, b, y, b, b, b,
b, b, b, y, b, b, b, b,
b, b, b, b, b, b, b, b]

sense.set_pixels(image_pixels)