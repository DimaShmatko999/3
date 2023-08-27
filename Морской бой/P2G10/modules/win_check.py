import pygame
import modules.data_base as data

scan_finished = 0

def win(frame):
    if frame % 60 == 0:
        player_ship_cells = 0
        enemy_ship_cells = 0
        for row in data.player_map: 
            for cell in row: 
                if cell == 1:
                    player_ship_cells += 1  
        for row in data.enemy_map:
            for cell in row:
                if cell == 1:
                    enemy_ship_cells += 1
        if enemy_ship_cells == 0:
            return "player"
        elif player_ship_cells == 0:
            return "bot"
    