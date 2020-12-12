from sense_hat import SenseHat
sense = SenseHat()

def get_color(color):
    no_of_try = 0

    while True:
        color_str = int(input("Enter the value of the " + color + " color for message (0 to 255):"))

        if (color_str > 0 and color_str < 256):
            return color_str
        else:
            while (no_of_try < 3):
                color_str = int(input("Please enter the int number between 0 to 255 for " + color + ":"))
                no_of_try += 1

                if (color_str > 0 and color_str < 256):
                    return color_str

                else:
                    continue

            if (no_of_try == 3):
                return 0


r_int = get_color("red")
g_int = get_color("green")
b_int = get_color("blue")

msg_color = (r_int, g_int, b_int)

print(msg_color)

sense.show_message("I got it!", text_colour=msg_color)