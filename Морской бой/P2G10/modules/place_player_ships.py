import pygame
import modules.data_base as data
import modules.ship as ship
ship_list = ["large", "big", "big", "normal", "normal", "normal", "small", "small", "small", "small"]
ship_number = 1
rotate_cd = 0
def blit_unplaced_ship_unchoosed(screen):
    if data.unplaced_ship.TYPE == "large":
        lenght = 4
    elif data.unplaced_ship.TYPE == "big":
        lenght = 3
    elif data.unplaced_ship.TYPE == "normal":
        lenght = 2
    elif data.unplaced_ship.TYPE == "small":
        lenght = 1
    if data.unplaced_ship.ANGLE == 0 or -180:
        data.unplaced_ship.X = 600 - lenght * 20
        data.unplaced_ship.Y = 10
    if data.unplaced_ship.ANGLE == -90 or -270:
        data.unplaced_ship.X = 580
        data.unplaced_ship.Y = 10
    
    data.unplaced_ship.blit_ship(screen)
def choose_ship():
    if data.unplaced_ship.TYPE == "large":
        lenght = 4
    elif data.unplaced_ship.TYPE == "big":
        lenght = 3
    elif data.unplaced_ship.TYPE == "normal":
        lenght = 2
    elif data.unplaced_ship.TYPE == "small":
        lenght = 1
    if data.unplaced_ship.ANGLE == 0 or data.unplaced_ship.ANGLE == -180: 
        if 600 - lenght * 20 < pygame.mouse.get_pos()[0] < 600 + lenght * 20:
            if 10 < pygame.mouse.get_pos()[1] < 50:
                data.unplaced_ship.STATE = "choosed" 
                print("choosed (horiz.)")
            else: 
                print(f"Horiz. choose fail at y (10-50)) check")
                print(f"Mouse coordinates: {pygame.mouse.get_pos()}")
        else: 
            print(f"Horiz. choose fail at x ({600 - lenght * 20} - {600 + lenght * 20})")
            print(f"Mouse coordinates: {pygame.mouse.get_pos()}")
    elif data.unplaced_ship.ANGLE == -90 or data.unplaced_ship.ANGLE == -270: 
        if 580 < pygame.mouse.get_pos()[0] < 620:
            if 10 < pygame.mouse.get_pos()[1] < 10 + lenght * 40:
                data.unplaced_ship.STATE = "choosed" 
                print("choosed (vert.)")
            else: 
                print(f"Vert. choose fail at y (10-{10+lenght*40}) check")
                print(f"Mouse coordinates: {pygame.mouse.get_pos()}")
        else: 
            print(f"Vert. choose fail at x (580-620) check")
            print(f"Mouse coordinates: {pygame.mouse.get_pos()}")
    else: 
        print(f"Not choosed, Angle: {data.unplaced_ship.ANGLE}")

def place_ship():
    if data.unplaced_ship.STATE == "choosed":
        x = 80
        y = 260
        cell = [0, 0, 0]
        if (0 < pygame.mouse.get_pos()[0] - 80 < 400 and 0 < pygame.mouse.get_pos()[1] - 260 < 400):
            cell = [(pygame.mouse.get_pos()[1] - 260) // 40, (pygame.mouse.get_pos()[0] - 80) // 40]
        print(f"x/y = {x}/{y}; cell = {cell}")
        if len(cell) != 3:
            data.unplaced_ship.CELL = cell
            data.unplaced_ship.X, data.unplaced_ship.Y = x, y

def rotate_ship(repeat):
    global rotate_cd
    if pygame.key.get_pressed()[pygame.K_SPACE] and repeat >= rotate_cd:
        data.unplaced_ship.ANGLE -= 90
        rotate_cd = repeat + 8
        if data.unplaced_ship.ANGLE < -270:
            data.unplaced_ship.ANGLE = 0      

def check_cells(): 
    if len(data.unplaced_ship.CELL) == 2:
        if data.unplaced_ship.TYPE == "large":
            lenght = 4
        elif data.unplaced_ship.TYPE == "big":
            lenght = 3
        elif data.unplaced_ship.TYPE == "normal":
            lenght = 2
        elif data.unplaced_ship.TYPE == "small":
            lenght = 1
        if data.unplaced_ship.ANGLE == -180:
            side = [0, 1]
        elif data.unplaced_ship.ANGLE == -90:
            side = [1, 0]
        elif data.unplaced_ship.ANGLE == 0:
            side = [0, 1]
        elif data.unplaced_ship.ANGLE == -270:
            side = [1, 0]
        check_list = 0
        for cell in range(lenght):
            if (-1 < data.unplaced_ship.CELL[0] + side[0] * cell < 10 and -1 < data.unplaced_ship.CELL[1] + side[1] * cell < 10): 
                    if data.player_map[data.unplaced_ship.CELL[0] + side[0] * cell][data.unplaced_ship.CELL[1] + side[1] * cell] == 0:
                        check_list += 1
        return check_list == lenght


def place_stop_cells():
    if data.unplaced_ship.TYPE == "large":
        lenght = 4
    elif data.unplaced_ship.TYPE == "big":
        lenght = 3
    elif data.unplaced_ship.TYPE == "normal":
        lenght = 2                                                
    elif data.unplaced_ship.TYPE == "small":
        lenght = 1                                                  
    if data.unplaced_ship.ANGLE == 0:
        side = [0, 1]
        side_cells = [1, 0, 1, 0]
    elif data.unplaced_ship.ANGLE == -90:
        side = [1, 0]
        side_cells = [0, 1, 0, 1]
    elif data.unplaced_ship.ANGLE == -180:
        side = [0, 1]
        side_cells = [1, 0, 1, 0]
    elif data.unplaced_ship.ANGLE == -270:
        side = [1, 0]
        side_cells = [0, 1, 0, 1]
    for cell in range(lenght + 2):
        cell -= 1
        if (-1 < data.unplaced_ship.CELL[0] + side[0] * cell < 10 and -1 < data.unplaced_ship.CELL[1] + side[1] * cell < 10):
            if side_cells[0] and data.unplaced_ship.CELL[0] + 1 < 10:
                data.player_map[data.unplaced_ship.CELL[0] + 1][data.unplaced_ship.CELL[1] + side[1] * cell] = 2
            if side_cells[2] and data.unplaced_ship.CELL[0] - 1 > -1:
                data.player_map[data.unplaced_ship.CELL[0] - 1][data.unplaced_ship.CELL[1] + side[1] * cell] = 2
            if side_cells[1] and data.unplaced_ship.CELL[1] + 1 < 10:
                data.player_map[data.unplaced_ship.CELL[0] + side[0] * cell][data.unplaced_ship.CELL[1] + 1] = 2
            if side_cells[3] and data.unplaced_ship.CELL[1] - 1 > -1:
                data.player_map[data.unplaced_ship.CELL[0] + side[0] * cell][data.unplaced_ship.CELL[1] - 1] = 2
            data.player_map[data.unplaced_ship.CELL[0] + side[0] * cell][data.unplaced_ship.CELL[1] + side[1] * cell] = 2

def finish_ship():
    global ship_number
    if data.unplaced_ship.TYPE == "large":
        lenght = 4
    elif data.unplaced_ship.TYPE == "big":
        lenght = 3
    elif data.unplaced_ship.TYPE == "normal":
        lenght = 2
    elif data.unplaced_ship.TYPE == "small":
        lenght = 1
    data.ships.append(data.unplaced_ship)
    data.ships[-1].place_ship()
    if ship_number < 10:
        data.unplaced_ship = ship.Ship(ship_list[ship_number],[0, 0, 0], None, 0, "player")
        data.unplaced_ship.X = 600 - lenght * 20
        data.unplaced_ship.Y = 590 
    ship_number += 1
def place_finish():
    can_place = check_cells()
    if can_place:
        place_stop_cells()
        finish_ship()
    else:
        data.unplaced_ship.CELL = [0,0,0]