# 0 - Пустота
# 1 - Корабль
# 2 - Занято
# 3 - Промах
# 4 - Взрыв
# 5 - Наведение
# 6 - Наведение, корабль
# 7 - Нажатие 
# 8 - Нажатие, корабль
 
def map():
    map1 = []
    for row in range(10):
        map1.append([])
        for cell in range(10):
            map1[row].append(0)
    return map1
player_map = map()
enemy_map = map()
unplaced_ship = 0 
ships = []