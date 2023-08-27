import pygame
import os
import modules.data_base as data

pygame.init()

def path_to_file(name_file):
    path_to_file = __file__
    path_to_file = path_to_file.split('\\')
    del path_to_file[-1]
    del path_to_file[-1]
    path_to_file = "\\".join(path_to_file)
    path_to_file = os.path.join(path_to_file, name_file)
    return path_to_file
# 1200, 700

def create_field(screen, x, map):
    y = 260
    for row in map:
        for cell in row:
            cell_main = "frame"
            if cell == 5 or cell == 6 or cell == 7 or cell == 8:
                cell_main = "hover"
            cell_frame = pygame.transform.scale(pygame.image.load(path_to_file(f"images\\cells\\cell_{cell_main}.png")), (40,40)); screen.blit(cell_frame, (x, y))
            x += 40
        y += 40
        x -= 400
font = pygame.font.SysFont("notosans", 40)

def numbers_on_field(screen, x = 90, y = 235):
    global font
    for number in range(10):
        text = font.render(str(number+1), True, (0,0,0))
        screen.blit(text, (x, y))
        x += 40

def letters_on_field(screen, x = 60, y = 260):
    letter_list = ["a","b","c","d","e","f","g","h","i","j"]
    global font
    for number in range(10):
        text = font.render(letter_list[number], True, (0,0,0))
        screen.blit(text, (x, y))
        y += 40

def blit_effects(screen, map, x):
    y = 260
    effect_list = [0, 1, 2, "miss", "explosion"]
    for row in map:
        for cell in row:
            if cell == 3 or cell == 4: 
                cell_effect = pygame.transform.scale(pygame.image.load(path_to_file(f"images\\cells\\{effect_list[cell]}.png")), (40,40))
                screen.blit(cell_effect, (x, y))
            x += 40
        x -= 400
        y += 40

def draw_all(screen, back_file):
    screen.blit(pygame.transform.scale(pygame.image.load(path_to_file(f"images\\{back_file}.png")), (1200, 700)), (0, 0))
    create_field(screen, 80,  data.player_map)
    create_field(screen, 720, data.enemy_map)
    numbers_on_field(screen)
    numbers_on_field(screen, 730)
    letters_on_field(screen)
    letters_on_field(screen, 700)
    for ship in data.ships:
        if ship.SIDE == "player":
            ship.blit_ship(screen)
    blit_effects(screen, data.player_map, 80)
    blit_effects(screen, data.enemy_map, 720)