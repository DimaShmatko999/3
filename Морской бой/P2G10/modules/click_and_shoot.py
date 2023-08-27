import pygame
import modules.data_base as data

prev_cell = [0,0,0]

def check_click(mouse_state):
    global prev_cell
    cell = [0,0,0]
    if (0 < pygame.mouse.get_pos()[0] - 720 < 400 and 0 < pygame.mouse.get_pos()[1] - 260 < 400):
        cell = [(pygame.mouse.get_pos()[1] - 260) // 40, (pygame.mouse.get_pos()[0] - 720) // 40]
        if cell != prev_cell:
            if   data.enemy_map[prev_cell[0]][prev_cell[1]] == 5 or data.enemy_map[prev_cell[0]][prev_cell[1]] == 7:
                data.enemy_map[prev_cell[0]][prev_cell[1]] = 0
            elif   data.enemy_map[prev_cell[0]][prev_cell[1]] == 6 or data.enemy_map[prev_cell[0]][prev_cell[1]] == 8:
                data.enemy_map[prev_cell[0]][prev_cell[1]] = 1 
            else:
                print(cell, prev_cell)
        prev_cell = cell
        print(f"State = {mouse_state}, Cell = {cell}")
        if mouse_state == "hover":
            if data.enemy_map[cell[0]][cell[1]] == 0 or data.enemy_map[cell[0]][cell[1]] == 2:
                data.enemy_map[cell[0]][cell[1]] = 5; 
            elif data.enemy_map[cell[0]][cell[1]] == 1:
                data.enemy_map[cell[0]][cell[1]] = 6; 
            else: print("error1")
        elif mouse_state == "click":
            if data.enemy_map[cell[0]][cell[1]] == 5:
                data.enemy_map[cell[0]][cell[1]] = 7; 
            elif data.enemy_map[cell[0]][cell[1]] == 6:
                data.enemy_map[cell[0]][cell[1]] = 8; 
        elif mouse_state == "up":
            if data.enemy_map[cell[0]][cell[1]] == 7:
                data.enemy_map[cell[0]][cell[1]] = 3
                print(f"miss at {cell}")
                return True
            elif data.enemy_map[cell[0]][cell[1]] == 8:
                data.enemy_map[cell[0]][cell[1]] = 4
                print(f"attacked at {cell}")
                return False
    else: 
        return False
        