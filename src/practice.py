# The Trivia Game
# Chapter 3

import sys, pygame
from pygame.locals import *
from Trivia import *

#main program begins
pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("The Trivia Game")
font1 = pygame.font.Font(None, 40)
font2 = pygame.font.Font(None, 24)
black = 0,0,0
white = 255,255,255
cyan = 0,255,255
yellow = 255,255,0
purple = 255,0,255
green = 0,255,0
red = 255,0,0
gameOver = False

#load the trivia data file
trivia = Trivia("trivia_data.txt")

#repeating loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYUP:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.key == pygame.K_1:
                trivia.handle_input(1)
            elif event.key == pygame.K_2:
                trivia.handle_input(2)
            elif event.key == pygame.K_3:
                trivia.handle_input(3)
            elif event.key == pygame.K_4:
                trivia.handle_input(4)
            elif event.key == pygame.K_RETURN:
                gameOver = trivia.next_question()
            if gameOver:
                trivia.game_over()
                trivia.current = 0
                if event.key == pygame.K_y:
                    gameOver = False
                elif event.key == pygame.K_n:
                    sys.exit()

            
    if not gameOver:
        screen.fill((0,0,200))
        trivia.show_question()
    
    #update the display
    pygame.display.update()