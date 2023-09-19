from pico2d import *
import math


open_canvas()

grass = load_image("grass.png")
character = load_image("character.png")

X_PADDING = 20
Y_PADDING = 40
RIGHT_LIMIT = 800
LEFT_LIMIT = 0
BOTTOM_LIMIT = 50
UP_LIMIT = 600

position = [400, 90]
move = [(2, 0), (0, 2), (-2, 0), (0, -2), (2, 0)]   # 우 상 좌 하 우
move_cycle = 5
rad = 0

while True:
    clear_canvas_now()

    grass.draw_now(400, 30)
    print(move_cycle)
    character.draw_now(position[0], position[1])

    if move_cycle == 5:
        if rad < math.pi * 2:
            rad += 0.01
            position[0] = 400 + 200*math.sin(rad)
            position[1] = 200 + 90 - 200*math.cos(rad)
        else:
            move_cycle = 0
            rad = 0
            position[0] = 400
            position[1] = 90
    else:
        position[0] += move[move_cycle][0]
        position[1] += move[move_cycle][1]
        if move_cycle == 0:
            if position[0] >= RIGHT_LIMIT - X_PADDING:
                position[0] = RIGHT_LIMIT - X_PADDING
                move_cycle = 1
        elif move_cycle == 1:
            if position[1] >= UP_LIMIT - Y_PADDING:
                position[1] = UP_LIMIT - Y_PADDING
                move_cycle = 2
        elif move_cycle == 2:
            if position[0] <= LEFT_LIMIT + X_PADDING:
                position[0] = LEFT_LIMIT + X_PADDING
                move_cycle = 3
        elif move_cycle == 3:
            if position[1] <= BOTTOM_LIMIT + Y_PADDING:
                position[1] = BOTTOM_LIMIT + Y_PADDING
                move_cycle = 4
        elif move_cycle == 4:
            if position[0] >= 400:
                position[0] = 400
                move_cycle = 5
    
    delay(0.01)

close_canvas()
