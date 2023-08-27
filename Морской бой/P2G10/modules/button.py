import pygame
import modules.data_base as data
import modules.path as path
class Button():
    def __init__(self, x = 0, y = 0, width = 100, height = 30):
        self.WIDTH = width
        self.HEIGHT = height
        self.X = x
        self.Y = y
        self.STATE = "hover"
    def blit_button(self, screen):
        if self.STATE != None:
            if self.STATE == "hover" or self.STATE == "up":
                image = pygame.transform.scale(pygame.image.load(path.path_to_file("images\\other\\button_unpressed.png")), (self.WIDTH, self.HEIGHT))
            elif self.STATE == "click":
                image = pygame.transform.scale(pygame.image.load(path.path_to_file("images\\other\\button_pressed.png")), (self.WIDTH, self.HEIGHT))
            screen.blit(image,(self.X, self.Y))