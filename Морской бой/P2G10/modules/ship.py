import pygame
import modules.data_base as data
import modules.path as path

class Ship():
    def __init__(self, type_, cell, state, angle, side):
        self.TYPE = type_
        self.CELL = cell
        self.STATE = state
        self.ANGLE = angle
        self.SIDE = side
        self.X = 0
        self.Y = 0

    def place_ship(self):
        if self.TYPE == "large":
            lenght = 4
        elif self.TYPE == "big":
            lenght = 3
        elif self.TYPE == "normal":
            lenght = 2
        elif self.TYPE == "small":
            lenght = 1  
        if self.ANGLE == -90:
            side = [1, 0]
        elif self.ANGLE == 0:
            side = [0, 1]
        elif self.ANGLE == -270:
            side = [1, 0]
        elif self.ANGLE == -180:
            side = [0, 1]
        for cell in range(lenght):
            if self.SIDE == "player":
                data.player_map[self.CELL[0] + side[0] * cell][self.CELL[1] + side[1] * cell] = 1
                self.X = 80
            if self.SIDE == "enemy":
                data.enemy_map[self.CELL[0] + side[0] * cell][self.CELL[1] + side[1] * cell] = 1   
                self.X = 720
        self.Y = 260
        for row in range(self.CELL[0]):
            self.Y += 40
        for cell in range(self.CELL[1]):
            self.X += 40

    def blit_ship(self, screen):
        if self.TYPE == "large":
            lenght = 4
        elif self.TYPE == "big":
            lenght = 3
        elif self.TYPE == "normal":
            lenght = 2
        elif self.TYPE == "small":
            lenght = 1
        image = pygame.image.load(path.path_to_file(f"images\\ships\\ship_{self.TYPE}.png"))
        image = pygame.transform.scale(image,(lenght * 40, 40))
        image = pygame.transform.rotate(image, self.ANGLE)
        screen.blit(image, (self.X, self.Y))