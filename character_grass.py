from pico2d import *
import math


open_canvas()

grass = load_image("grass.png")
character = load_image("character.png")


position = [400, 90]
move = [(2, 0), (0, 2), (-2, 0), (0, -2), (2, 0)]   # 우 상 좌 하 우
move_cycle = 0
rad = 0
while True:
    clear_canvas_now()

    grass.draw_now(400, 30)

    if move_cycle > 4:
        if rad < math.pi * 2:
            rad += 0.01
            character.draw_now(position[0]+200*math.sin(rad), position[1] + 200 - 200*math.cos(rad))
        else:
            move_cycle = 0
            rad = 0
    else:
        position[0] += move[move_cycle-1][0]
        position[1] += move[move_cycle-1][1]
        print(move_cycle)
        character.draw_now(position[0], position[1])
        if position[0] >= 780:
            position[0] -= 2
            move_cycle += 1
        elif position[1] >= 560:
            position[1] -= 2
            move_cycle += 1
        elif position[0] <= 20:
            position[0] += 2
            move_cycle += 1
        elif position[1] <= 89:
            position[1] += 2
            move_cycle += 1
        if move_cycle == 4:
            if position[0] >= 400:
                move_cycle += 1
                position = [400, 90]
    
    delay(0.01)


delay(5)

close_canvas()
