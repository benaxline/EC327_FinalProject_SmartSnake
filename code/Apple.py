import pygame
from pygame.locals import *
import time
import random
#from pygamepopup.menu_manager import MenuManager

SIZE = 40
BACKGROUND_COLOR = (110, 110, 5)



class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("apple.jpg").convert()
        self.x = 120
        self.y = 120

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1, 24) * SIZE
        self.y = random.randint(1, 19) * SIZE