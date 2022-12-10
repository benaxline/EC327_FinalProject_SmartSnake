import pygame
from pygame.locals import *
import time
import random
#from pygamepopup.menu_manager import MenuManager

SIZE = 40
BACKGROUND_COLOR = (110, 110, 5)

class Math:
    def __init__(self):
        self.first_num = 0
        self.second_num = 0
        self.operator = ''
        self.answer = 0

    def generate_operator(self):
        #determine which operator to use
        num = random.rand(1,4)
        if num == 1:
            self.operator = '+'
        elif num == 2:
            self.operator = '-'
        elif num == 3:
            self.operator = '*'
        elif num == 4:
            self.operator = '/'

    def generate_num(self):
        #generate numbers
        self.first_num = random.randint(1,100)
        self.second_num = random.randint(1,100)

    def solve(self):
        first = self.first_num
        second = self.second_num
        if self.operator == '+':
            self.answer = first + second
        elif self.operator == '-':
            self.answer = first - second
        elif self.operator == '*':
            self.answer = first * second
        elif self.operator == '/':
            self.answer = first / second

    def display_math_problem(self):
        pass

    



