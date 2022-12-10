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
        num = random.randint(1,4)
        if num == 1:
            operator = '+'
        elif num == 2:
            operator = '-'
        elif num == 3:
            operator = '*'
        elif num == 4:
            operator = '/'
        return operator

    def generate_num1(self):
        #generate numbers
        num = random.randint(1,100)
        return num

    def generate_num2(self):
        #generate numbers
        num = random.randint(1,100)
        return num
    

    def solve(self):
        first = self.first_num
        second = self.second_num
        if self.operator == '+':
            answer = first + second
        elif self.operator == '-':
            answer = first - second
        elif self.operator == '*':
            answer = first * second
        elif self.operator == '/':
            answer = first / second
        return answer

    def math_expression(self):
        f = str(self.first_num)
        s = str(self.second_num)
        expression = f + " " + self.operator + " " + s
        return expression

    

    



