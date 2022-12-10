import pygame
from pygame.locals import *
import time
import random
#from pygamepopup.menu_manager import MenuManager

from Apple import *
from Game import *
from Snake import *

SIZE = 40
BACKGROUND_COLOR = (110, 110, 5)



class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("EC327 Snake Game")
        self.surface = pygame.display.set_mode((1000, 800))  # set mode: setting the window size of the game
        self.snake = Snake(self.surface)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()
        self.snake_zero = False
        self.off_grid = False

    def reset(self):
        self.snake = Snake(self.surface)
        self.apple = Apple(self.surface)

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False

    def is_off_grid(grid, x, y):
        if x > 1000 or x < 0:
            return True
        elif y > 800 or y < 0:
            return True
        else:
            return False

    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        # snake eating apple scenario
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):

            self.snake.decrease_length() #decreases length
            self.apple.move() #apple moves

        # snake colliding with itself
        for i in range(2, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise "Collision Occured"
        if self.snake.length == 0:
            raise "Zero Length"
        for i in range(2, self.snake.length):
            if self.is_off_grid(self.snake.x[0], self.snake.y[0]):
                self.off_grid = True
                raise "Off Grid"

    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score: {self.snake.length}", True, (200, 200, 200))
        self.surface.blit(score, (850, 10))

    def show_game_over(self):
        self.surface.fill(BACKGROUND_COLOR)  # setting background color of the main window
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"Game is over! Your score is {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(line1, (200, 300))
        line2 = font.render("To play again press Enter. To exit press Escape!", True, (255, 255, 255))
        self.surface.blit(line2, (200, 350))

        pygame.display.flip()

    def show_game_won(self):
        self.surface.fill(BACKGROUND_COLOR)  # setting background color of the main window
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"You Won! Your score is {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(line1, (200, 300))
        line2 = font.render("To play again press Enter. To exit press Escape!", True, (255, 255, 255))
        self.surface.blit(line2, (200, 350))

        pygame.display.flip()

    def show_off_grid(self):
        self.surface.fill(BACKGROUND_COLOR)  # setting background color of the main window
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"You Lose! You went off the grid! Your score is {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(line1, (200, 300))
        line2 = font.render("To play again press Enter. To exit press Escape!", True, (255, 255, 255))
        self.surface.blit(line2, (200, 350))

        pygame.display.flip()

    def end_of_game(self):
        if self.snake.length == 0:
            self.show_game_won()
            #self.show_game_over()
        elif self.off_grid == True:
            self.show_off_grid()
            
        else:
            self.show_game_over()
            #self.show_game_won()
        # self.pause = True
        # self.reset()

    


    def is_snakelength_zero(self):
        if self.snake.length == 0:
            self.snake_zero = True
        else:
            self.snake_zero = False


        # if self.snake.length != 0:
        #     return False
        # else:
        #     return True

    def run(self):
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        pause = False

                    if not pause:
                        if event.key == K_LEFT:
                            self.snake.move_left()

                        if event.key == K_RIGHT:
                            self.snake.move_right()

                        if event.key == K_UP:
                            self.snake.move_up()

                        if event.key == K_DOWN:
                            self.snake.move_down()

                elif event.type == QUIT:
                    running = False
            try:
                
               

                if not pause:
                    self.play()

            except Exception as e:
                #keep in this order - else it won't show the right end score!!!!
                if self.snake.length == 0:
                    self.snake_zero = True
                self.end_of_game()
                pause = True
                self.reset()
                

            time.sleep(0.15)