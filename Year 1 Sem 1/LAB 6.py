from sense_hat import SenseHat

from time import sleep

import random


def move_marble(pitch, roll, x, y):
    new_x = x

    new_y = y

    if 1 < pitch < 179 and x != 0:

        new_x -= 1

    elif 359 > pitch > 179 and x != 7:

        new_x += 1

    if 1 < roll < 179 and y != 7:

        new_y += 1

    elif 359 > roll > 179 and y != 0:

        new_y -= 1

    new_x, new_y = check_wall(x, y, new_x, new_y)

    return new_x, new_y


def check_wall(x, y, new_x, new_y):
    if board[new_y][new_x] != r:

        return new_x, new_y

    elif board[new_y][x] != r:

        return x, new_y

    elif board[y][new_x] != r:

        return new_x, y

    return x, y


def random_target():
    while True:

        target_x = random.randint(0, 7)

        target_y = random.randint(0, 7)

        if board[target_y][target_x] != r and board[target_y][target_x] != g:
            break

    return target_x, target_y


def random_board():
    board = [[b, b, b, b, b, b, b, b],

             [b, b, b, b, b, b, b, b],

             [b, b, b, b, b, b, b, b],

             [b, b, b, b, b, b, b, b],

             [b, b, b, b, b, b, b, b],

             [b, b, b, b, b, b, b, b],

             [b, b, b, b, b, b, b, b],

             [b, b, b, b, b, b, b, b]]

    for x in range(0, 8):

        for y in range(0, 8):
            board[y][x] = random.choice([r, b, b, b])

    return board


sense = SenseHat()

sense.clear()

b = (0, 0, 0)

w = (255, 255, 255)

r = (255, 0, 0)

g = (0, 255, 0)

board = random_board()

x, y = 2, 2

seconds = 0

target_x, target_y = random_target()

board[target_y][target_x] = g

while True:

    g = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    pitch = sense.get_orientation()['pitch']

    roll = sense.get_orientation()['roll']

    board[y][x] = b

    x, y = move_marble(pitch, roll, x, y)

    # moving target :P

    # board[target_y][target_x] = b

    # target_x,target_y = move_marble((pitch+180)%360,(roll+180)%360,target_x,target_y)

    # board[target_y][target_x] = g

    # moving target :P

    if x == target_x and y == target_y:
        break

    board[y][x] = w

    sense.set_pixels(sum(board, []))

    sleep(0.05)

    seconds += 0.05

    if seconds >= 10:
        board[target_y][target_x] = b

        target_x, target_y = random_target()

        seconds = 0

    board[target_y][target_x] = g

sense.show_message("yay!!")