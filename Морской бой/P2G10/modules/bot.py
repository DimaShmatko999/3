import pygame, random
import modules.ship as ship
import modules.data_base as data
pygame.init()
def place_bot_ship():
    # Задаём растановку кораблей бота с большого
    data.unplaced_ship = ship.Ship("large", [0, 0, 0], None, 0, "enemy")
    # Список кораблей бота которые у нас в игре
    ship_list = ["large", "big", "big", "normal", "normal", "normal", "small", "small", "small", "small"]
    # Функция для проверки ячейки
    def check_cells(): 
       #
        if len(data.unplaced_ship.CELL) == 2:
            # Создаём условие если (тип корабля = лардж) то
            if data.unplaced_ship.TYPE == "large":   
                # длина = 4 клетки          
                lenght = 4
            # Создаём условие если (тип корабля = биг) то
            elif data.unplaced_ship.TYPE == "big":   
                # длина = 3 клетки
                lenght = 3
            # Создаём условие если (тип корабля = норм) то
            elif data.unplaced_ship.TYPE == "normal":
                # длина = 2 клетки
                lenght = 2
            # Создаём условие если (тип корабля = смалл) то
            elif data.unplaced_ship.TYPE == "small":  
                # длина = 1 клетка
                lenght = 1
            # Создаём условие если (угол поварота = -180)
            if data.unplaced_ship.ANGLE == -180:   
                # Сторона равна [0, 1]
                side = [0, 1]
            # Создаём условие если (угол поварота = -90)
            elif data.unplaced_ship.ANGLE == -90:  
                # Сторона равна [1, 0]
                side = [1, 0]
            # Создаём условие если (угол поварота = 0)
            elif data.unplaced_ship.ANGLE == 0:   
                # Сторона равна [0, 1]
                side = [0, 1]
            # Создаём условие если (угол поварота = -270)
            elif data.unplaced_ship.ANGLE == -270: 
                # Сторона равна [1, 0]
                side = [1, 0]
            # Проверка списка
            check_list = 0
            # Переменная хранит error
            fc = "ERROR"
            # Создаём цикл фор для стороны
            for cell in range(lenght):
                #
                if (-1 < data.unplaced_ship.CELL[0] + side[0] * cell < 10 and -1 < data.unplaced_ship.CELL[1] + side[1] * cell < 10): 
                        #
                        if data.enemy_map[data.unplaced_ship.CELL[0] + side[0] * cell][data.unplaced_ship.CELL[1] + side[1] * cell] == 0:
                            #
                            check_list += 1
                            #
                            fc = "???"
                        else: print(data.enemy_map[data.unplaced_ship.CELL[0] + side[0] * cell][data.unplaced_ship.CELL[1] + side[1] * cell], [data.unplaced_ship.CELL[0] + side[0] * cell, data.unplaced_ship.CELL[1] + side[1] * cell])
                        #
                        fc = data.unplaced_ship.CELL[0] + side[0] * (lenght - 1), data.unplaced_ship.CELL[1] + side[1] + (lenght - 1)
            #
            # print(f"Check: {check_list}, lenght: {lenght}, cell/final cell: {data.unplaced_ship.CELL}/{fc}, side: {side}, angle: {data.unplaced_ship.ANGLE}, type: {data.unplaced_ship.TYPE}")
            #
            return check_list == lenght
    # Функция которая
    def place_stop_cells():
        if data.unplaced_ship.TYPE == "large":    lenght = 4
        elif data.unplaced_ship.TYPE == "big":    lenght = 3
        elif data.unplaced_ship.TYPE == "normal": lenght = 2               # Влево,Вправо
        elif data.unplaced_ship.TYPE == "small":  lenght = 1               # Вверх, Вниз
        if data.unplaced_ship.ANGLE == 0:      side = [0, 1]; side_cells = [1, 0, 1, 0]
        elif data.unplaced_ship.ANGLE == -90:  side = [1, 0]; side_cells = [0, 1, 0, 1]
        elif data.unplaced_ship.ANGLE == -180: side = [0, 1]; side_cells = [1, 0, 1, 0]
        elif data.unplaced_ship.ANGLE == -270: side = [1, 0]; side_cells = [0, 1, 0, 1]
        for cell in range(lenght + 2):
            cell -= 1
            if (-1 < data.unplaced_ship.CELL[0] + side[0] * cell < 10 and
                -1 < data.unplaced_ship.CELL[1] + side[1] * cell < 10):
                if side_cells[0] and data.unplaced_ship.CELL[0] + 1 < 10:
                    data.enemy_map[data.unplaced_ship.CELL[0] + 1][data.unplaced_ship.CELL[1] + side[1] * cell] = 2
                if side_cells[2] and data.unplaced_ship.CELL[0] - 1 > -1:
                    data.enemy_map[data.unplaced_ship.CELL[0] - 1][data.unplaced_ship.CELL[1] + side[1] * cell] = 2
                if side_cells[1] and data.unplaced_ship.CELL[1] + 1 < 10:
                    data.enemy_map[data.unplaced_ship.CELL[0] + side[0] * cell][data.unplaced_ship.CELL[1] + 1] = 2
                if side_cells[3] and data.unplaced_ship.CELL[1] - 1 > -1:
                    data.enemy_map[data.unplaced_ship.CELL[0] + side[0] * cell][data.unplaced_ship.CELL[1] - 1] = 2
                data.enemy_map[data.unplaced_ship.CELL[0] + side[0] * cell][data.unplaced_ship.CELL[1] + side[1] * cell] = 2

    def finish_ship():
        data.ships.append(data.unplaced_ship)

        data.ships[-1].place_ship()
    for ship_type in ship_list:
        print(f"placing {ship_type} ship")
        data.unplaced_ship = ship.Ship(ship_type, [0, 0, 0], None, 0, "enemy")
        place_end = 0
        while place_end + 1 == True:
            data.unplaced_ship.ANGLE = random.randint(-3, 0) * 90   
            data.unplaced_ship.CELL = [random.randint(0, 9), random.randint(0, 9)]   
            can_place = check_cells()
            print(f"Cell: {data.unplaced_ship.CELL}, Angle: {data.unplaced_ship.ANGLE}, can place: {can_place}")
            if can_place:
                place_stop_cells()
                finish_ship()
                place_end = 1  
shoot = [0,0]
target = 0
sides = [[-1, 0],[0, -1],  [0, 1], [1, 0]]
line = 0
line_lenght = 0
end_of_line = False
side = 0
repeat = 0
line_ready = 0
def bot_shoot(repeater):
    global shoot
    global target
    global sides
    global line

    global line_lenght 
    global end_of_line
    global side
    global repeat
    global line_ready
    shoot_place = True
    busy=0
    if repeater % 15 == 0:
        if target == "Ship":
            print(line)
            if line == 0:
                print(f"passed line check, {repeat}")
                if len(sides)== 0:
                    sides = [[-1, 0],[0, -1],  [0, 1], [1, 0]]
                if repeat == 0:
                    repeat = len(sides)
                for r in range(repeat):
                    repeat -= 1
                    side = sides[random.randint(0, 3 - abs(len(sides)-4))]
                    sides.remove(side)
                    if shoot_place:
                        if 0 <= shoot[0] + side[0] <= 9 and 0 <= shoot[1] + side[1] <= 9:
                            if data.player_map[shoot[0] + side[0]][shoot[1] + side[1]] == 0 or data.player_map[shoot[0] + side[0]][shoot[1] + side[1]] == 2:
                                data.player_map[shoot[0] + side[0]][shoot[1] + side[1]] = 3
                                shoot_place = False
                                repeat = len(sides)
                                return True
                            elif data.player_map[shoot[0] + side[0]][shoot[1] + side[1]] == 1:
                                data.player_map[shoot[0] + side[0]][shoot[1] + side[1]] = 4
                                shoot = [shoot[0] + side[0],shoot[1] + side[1]]
                                shoot = [shoot[0] + side[0],shoot[1] + side[1]]
                                sides = [[-1, 0],[0, -1],  [0, 1], [1, 0]]
                                if line_ready == True:
                                    line = side
                                line_lenght = 3
                                repeat = len(sides)
                                return False
                            else:
                                busy += 1     
                        else: 
                            busy += 1
                if busy == 4:
                    repeat = 4
                    target = 0
                    shoot = [0, 0]
                    line_ready = 0
                    shoot_place = False
            else: 
                if -1 < shoot[0] < 10 and -1 < shoot[1] < 10:
                    if end_of_line==0 and  data.player_map[shoot[0]][shoot[1]] == 0:
                        if data.player_map[shoot[0]][shoot[1]] == 0 or data.player_map[shoot[0]][shoot[1]] == 2:
                            prev_shoot = shoot
                            if side == [1, 0]:    
                                shoot = [shoot[0]-line_lenght, shoot[1]]
                                end_of_line=2
                            elif side == [-1, 0]:
                                shoot = [shoot[0]+line_lenght, shoot[1]]
                                end_of_line=2
                            elif side == [0, 1]:    
                                shoot = [shoot[0], shoot[1]-line_lenght]
                                end_of_line = 2
                            elif side == [0, -1]: 
                                shoot = [shoot[0] ,shoot[1]+line_lenght]
                                end_of_line=2
                            shoot_place = True
                            data.player_map[prev_shoot[0]][prev_shoot[1]] = 3
                            return True
                    if end_of_line == 1 and  data.player_map[shoot[0]][shoot[1]] == 0 or  data.player_map[shoot[0]][shoot[1]] == 2:
                        if  data.player_map[shoot[0]][shoot[1]] == 0 or data.player_map[shoot[0]][shoot[1]]:
                            data.player_map[shoot[0]][shoot[1]] = 3
                        target = 0
                        side = 0
                        end_of_line = 0
                        shoot = 0
                        line_ready = 0
                        end_of_line = 0
                        shoot_place = 1
                        line = 0
                        return True
                    if data.player_map[shoot[0]][shoot[1]] == 1 and end_of_line==1:
                        shoot_place = 1
                        data.player_map[shoot[0]][shoot[1]]
                        shoot = [shoot[0] - side[0],shoot[1] - side[1]]
                        return False
                    elif data.player_map[shoot[0]][shoot[1]] == 1 and end_of_line==0:
                        shoot_place = 1
                        data.player_map[shoot[0]][shoot[1]] = 4
                        shoot = [shoot[0] + side[0],shoot[1] + side[1]]
                        line_lenght += 1
                        return False
                    elif data.player_map[shoot[0]][shoot[1]] == 1 and end_of_line==2:
                        shoot_place = 1
                        data.player_map[shoot[0]][shoot[1]] = 4
                        shoot = [shoot[0] - side[0],shoot[1] - side[1]]
                        end_of_line = 1
                        return False 
                    elif end_of_line == 2:
                        if data.player_map[shoot[0]][shoot[1]] == 0 or data.player_map[shoot[0]][shoot[1]] == 2 and end_of_line == 2:
                            data.player_map[shoot[0]][shoot[1]] = 3
                        target = 0
                        side = 0
                        line = 0
                        line_ready = 0
                        end_of_line = 0
                        shoot = 0
                        end_of_line = 0
                        shoot_place = 0
                        return True
                    else:
                        if end_of_line == 0:
                            print(side, f"({shoot[0]}, {shoot[1]})")
                            prev_shoot = shoot
                            if side == [1, 0]:   
                                shoot = [shoot[0]-line_lenght,shoot[1]]
                                end_of_line=2
                            elif side == [-1, 0]:   
                                shoot = [shoot[0]+line_lenght,shoot[1]]
                                end_of_line=2
                            elif side == [0, 1]:    
                                shoot = [shoot[0],shoot[1]-line_lenght]
                                end_of_line=2
                            elif side == [0, -1]:   
                                shoot = [shoot[0],shoot[1]+line_lenght]
                                end_of_line=2
                            if data.player_map[prev_shoot[0]][prev_shoot[1]] == 0 or data.player_map[prev_shoot[0]][prev_shoot[1]] == 2:
                                data.player_map[prev_shoot[0]][prev_shoot[1]] = 3
                                return True
                            else:
                                return False
                        else:
                            prev_shoot = shoot
                            target = 0
                            side = 0
                            line = 0
                            line_ready = 0
                            end_of_line = 0
                            shoot = 0
                            end_of_line = 0
                            shoot_place = 0
                            if data.player_map[prev_shoot[0]][prev_shoot[1]] == 0 or data.player_map[prev_shoot[0]][prev_shoot[1]] == 2:
                                data.player_map[prev_shoot[0]][prev_shoot[1]] = 3
                                return True
                            else: 
                                return False
                else:
                    if end_of_line == 0:
                        prev_shoot = shoot
                        if   side == [1, 0]:    shoot = [shoot[0]-line_lenght,shoot[1]];   end_of_line=2
                        elif side == [-1, 0]:   shoot = [shoot[0]+line_lenght,shoot[1]];   end_of_line=2
                        elif side == [0, 1]:    shoot = [shoot[0],shoot[1]-line_lenght];   end_of_line=2
                        elif side == [0, -1]:   shoot = [shoot[0],shoot[1]+line_lenght];   end_of_line=2
                        if -1 < prev_shoot[0] < 10 and -1 < prev_shoot[1] < 10:
                            if data.player_map[prev_shoot[0]][prev_shoot[1]] == 0 or data.player_map[prev_shoot[0]][prev_shoot[1]] == 2:
                                data.player_map[prev_shoot[0]][prev_shoot[1]] = 3
                                return True
                            else:
                                return False
                        else:
                            return False
                    elif end_of_line == 1 or end_of_line == 2:
                        prev_shoot = shoot
                        target = 0
                        side = 0
                        line = 0
                        end_of_line = 0
                        shoot = 0
                        line_ready = 0
                        end_of_line = 0
                        shoot_place = 0
                        if -1 < prev_shoot[0] < 10 and -1 < prev_shoot[1] < 10:
                            if data.player_map[prev_shoot[0]][prev_shoot[1]] == 0 or data.player_map[prev_shoot[0]][prev_shoot[1]] == 2:
                                data.player_map[prev_shoot[0]][prev_shoot[1]] = 3
                                return True
                            else:
                                return False
                        else:
                            return False
    elif target == 0: 
        cell = [random.randint(0, 9), random.randint(0, 9)]
        if data.player_map[cell[0]][cell[1]] == 0 or data.player_map[cell[0]][cell[1]] == 2:
            data.player_map[cell[0]][cell[1]] = 3
            return True
        elif data.player_map[cell[0]][cell[1]] == 1: 
            data.player_map[cell[0]][cell[1]] = 4
            target = "Ship"
            shoot = [cell[0],cell[1]]
            line_ready = True
            return False                                                                                                                       