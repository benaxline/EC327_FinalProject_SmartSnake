import pygame
from pygame.locals import *
import time
import random
import sys
#from pygamepopup.menu_manager import MenuManager

from Apple import *
from Game import *
from Snake import *
from Math import *
from Trivia import *

SIZE = 40
BACKGROUND_COLOR = (110, 110, 5)

white = 255,255,255
cyan = 0,255,255
yellow = 255,255,0
purple = 255,0,255
green = 0,255,0
red = 255,0,0

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
        self.math = Math()
        self.pause = False
        self.running = False
        self.mode = ''
        self.expression = ""
        self.math_answer = 0
        self.num1 = 0
        self.num2 = 0
        self.op = ''
        self.current = 0
        self.scored = False
        self.failed = False
        self.trivia = Trivia("trivia_data.txt")
        self.result = 0
        self.count = 0


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


    def displayMathProblem(self):
        # num1 = self.math.generate_num1()
        # num2 = self.math.generate_num2
        # op = self.math.generate_operator()
        self.surface.fill(BACKGROUND_COLOR)  # setting background color of the main window
        font = pygame.font.SysFont('arial', 30)

        line1 = font.render("Your question...", True, (255, 255, 255))
        self.surface.blit(line1, (200, 300))
        line2 = font.render(f"{self.math_exp()} = " , True, (255, 255, 255))
        self.surface.blit(line2, (200, 350))
        # line3 = font.render(f"1.) {random.randrange(1,100)}     2.) {random.randrange(1,100)}", True, (255, 255, 255))
        # self.surface.blit(line3, (200, 400))
        # line4 = font.render(f"3.) {self.math_answer}     4.) {random.randrange(1,100)}", True, (255, 255, 255))
        # self.surface.blit(line4, (200, 450))
        pygame.display.flip()

        #pygame.draw.rect(200, 400, 50, 100)
        character = ""
        esc = True
        while esc:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_0:
                        character += "0"
                    elif event.key == K_1:
                        character += "1"
                    elif event.key == K_2:
                        character += "2"
                    elif event.key == K_3:
                        character += "3"
                    elif event.key == K_4:
                        character += "4"
                    elif event.key == K_5:
                        character += "5"
                    elif event.key == K_6:
                        character += "6"
                    elif event.key == K_7:
                        character += "7"
                    elif event.key == K_8:
                        character += "8"
                    elif event.key == K_9:
                        character += "9"
                    elif event.key == K_DELETE:
                        character = character[:-1]
                    elif event.key == K_PERIOD:
                        character += "."
                    elif event.key == K_MINUS:
                        character += "-"
                    if event.key == K_RETURN:
                        esc = False
                        

                line = font.render(f"{character}" , True, (255, 255, 255))
                self.surface.blit(line, (300, 450))
                pygame.display.flip()

                ans = str(self.math_answer)
                print(ans)
                print(character)

            self.pause = False

        if character == ans:
            #output result
            self.surface.fill(BACKGROUND_COLOR)  # setting background color of the main window
            font = pygame.font.SysFont('arial', 30)

            line1 = font.render("CORRECT", True, (255, 255, 255))
            self.surface.blit(line1, (300, 300))
            line2 = font.render("Press Enter to move on.", True, (255, 255, 255))
            self.surface.blit(line2, (200, 350))
            pygame.display.flip()

            #press button
            esc = True
            while esc:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == K_RETURN:
                            
                            esc = False
                            break

            #decrease length of snake
            self.snake.decrease_length()
        else:
            #output result
            self.surface.fill(BACKGROUND_COLOR)  # setting background color of the main window
            font = pygame.font.SysFont('arial', 30)

            line1 = font.render("INCORRECT", True, (255, 255, 255))
            self.surface.blit(line1, (300, 300))
            line2 = font.render("Press Enter to move on.", True, (255, 255, 255))
            self.surface.blit(line2, (200, 350))
            pygame.display.flip()

            #press button
            esc = True
            while esc:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == K_RETURN:
                            
                            esc = False
                            break

            #increase length of snake
            self.snake.increase_length()

        pygame.display.flip()


    def displayTriviaProblem(self):
        
        self.surface.fill(BACKGROUND_COLOR)  # setting background color of the main window
        font = pygame.font.SysFont('arial', 30)

        line1 = font.render("TRIVIA GAME", True, (255, 255, 255))
        self.surface.blit(line1, (200, 300))
        line2 = font.render("Press Keys (1-4) To Answer", True, (255, 255, 255))
        self.surface.blit(line2, (200, 350))

        # #get correct answer out of data (first)
        self.correct = int(self.trivia.data[self.current+5])

        #display question
        question = self.current // 6 + 1
        line3 = font.render(f"QUESTION: {question}", True, (255, 255, 255))
        self.surface.blit(line3, (200, 400))
        line4 = font.render(f"{self.trivia.data[self.current]}", True, (255, 255, 255))
        self.surface.blit(line4, (200,450))

        #respond to correct answer
        # if self.scored:
        #    self.colors = [white,white,white,white]
        #    self.colors[self.correct-1] = green
        #    print_text(font1, 230, 380, "CORRECT!", green)
        #    print_text(font2, 170, 420, "Press Enter For Next Question", green)
        #    sys.exit()
        
        # elif self.failed:
        #     self.colors = [white,white,white,white]
        #     self.colors[self.wronganswer-1] = red
        #     self.colors[self.correct-1] = green
        #     print_text(font1, 220, 380, "INCORRECT!", red)
        #     print_text(font2, 170, 420, "Press Enter For Next Question", red)

        #display answers
        line5 = font.render("ANSWERS:", True, (255, 255, 255))
        self.surface.blit(line5, (200,500))
        self.current += 1
        line6 = font.render(f"1 - {str(self.trivia.data[self.current])}", True, (255, 255, 255))
        self.surface.blit(line6, (200,550))
        self.current += 1
        line7 = font.render(f"2 - {str(self.trivia.data[self.current])}", True, (255, 255, 255))
        self.surface.blit(line7, (200,600))
        self.current += 1
        line8 = font.render(f"3 - {str(self.trivia.data[self.current])}", True, (255, 255, 255))
        self.surface.blit(line8, (200,650))
        self.current += 1
        line9 = font.render(f"4 - {str(self.trivia.data[self.current])}", True, (255, 255, 255))
        self.surface.blit(line9, (200,700))
        self.current += 1
        pygame.display.flip()
        # print_text(font1, 5, 170, "ANSWERS")
        # print_text(font2, 20, 210, "1 - " + self.trivia.data[self.current+1], self.colors[0])
        # print_text(font2, 20, 240, "2 - " + self.trivia.data[self.current+2], self.colors[1])
        # print_text(font2, 20, 270, "3 - " + self.trivia.data[self.current+3], self.colors[2])
        # print_text(font2, 20, 300, "4 - " + self.trivia.data[self.current+4], self.colors[3])
        
        
        # self.surface.fill(BACKGROUND_COLOR)  # setting background color of the main window
        # font = pygame.font.SysFont('arial', 30)
        # line1 = font.render("Trivia Game", True, (255, 255, 255))
        # self.surface.blit(line1, (200, 300))
        # line2 = font.render("Press Keys (1-4) To Answer" , True, (255, 255, 255))
        # self.surface.blit(line2, (200, 350))
        #line3 = font.render()

        
        esc = True
        while esc:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_1:
                        self.result = 1
                        esc = False
                        break
                    elif event.key == K_2:
                        self.result = 2
                        esc = False
                        break
                    elif event.key == K_3:
                        self.result = 3
                        esc = False
                        break
                    elif event.key == K_4:
                        self.result = 4
                        esc = False
                        break
                    if event.key == K_RETURN:
                        break

               


                # self.handle_input(self.result)
                # print(self.result)

                  

            # self.pause = False

        if self.result == self.correct:
            #output result
            self.surface.fill(BACKGROUND_COLOR)  # setting background color of the main window
            font = pygame.font.SysFont('arial', 30)

            line1 = font.render("CORRECT", True, (255, 255, 255))
            self.surface.blit(line1, (300, 300))
            line2 = font.render("Press Enter to move on.", True, (255, 255, 255))
            self.surface.blit(line2, (200, 350))
            pygame.display.flip()

            #press button
            esc = True
            while esc:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == K_RETURN:
                            
                            esc = False
                            break

            #change length
            self.snake.decrease_length()
        else:
            #output result
            self.surface.fill(BACKGROUND_COLOR)  # setting background color of the main window
            font = pygame.font.SysFont('arial', 30)

            line1 = font.render("INCORRECT", True, (255, 255, 255))
            self.surface.blit(line1, (300, 300))
            line2 = font.render("Press Enter to move on.", True, (255, 255, 255))
            self.surface.blit(line2, (200, 350))
            pygame.display.flip()

            #press button
            esc = True
            while esc:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == K_RETURN:
                            
                            esc = False
                            break
            #change length
            self.snake.increase_length()
        


        self.pause = False
        self.current += 1 

        pygame.display.flip()



  
    def handle_input(self,number):
        if not self.scored and not self.failed:
            if number == self.correct:
                self.scored = True
                #self.snake.length += 1
                self.snake.decrease_length()
                
            else:
                self.failed = True
                self.wronganswer = number
                self.snake.increase_length()
    
    def question(self):
        if self.mode == 'm':
            self.displayMathProblem()
        elif self.mode == 't':
            self.displayTriviaProblem()
        elif self.mode == 'n':
            self.snake.increase_length()
            self.pause = False


    def play(self):
        
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        # snake eating apple scenario 
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.pause = True
            self.question()
            #self.snake.decrease_length() #decreases length
            self.apple.move() #apple moves

        # snake colliding with itself (LOSE)
        for i in range(2, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise "Collision Occured"
        
        # snake with zero length (WIN)
        if self.snake.length == 0:
            raise "Zero Length"

        # snake off grid (LOSE)
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

    def menu(self):
        #menu display
        self.surface.fill(BACKGROUND_COLOR)  # setting background color of the main window
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"Choose mode: ", True, (255, 255, 255))
        self.surface.blit(line1, (200, 300))
        line2 = font.render("Press M key for math mode", True, (255, 255, 255))
        self.surface.blit(line2, (200, 350))
        line3 = font.render("Press T key for trivia mode", True, (255, 255, 255))
        self.surface.blit(line3, (200, 400))
        line4 = font.render("Press N key for normal mode", True, (255, 255, 255))
        self.surface.blit(line4, (200, 450))
        line4 = font.render("Press Escape to quit.", True, (255, 255, 255))
        self.surface.blit(line4, (200, 500))
        pygame.display.flip()


        self.pause = False

    def math_exp(self):
        num1 = random.randint(1,100)
        num2 = random.randint(1,100)
        num = random.randint(1,4)
        if num == 1:
            operator = '+'
            self.math_answer = num1 + num2
        elif num == 2:
            operator = '-'
            self.math_answer = num1 - num2
        elif num == 3:
            operator = '*'
            self.math_answer = num1 * num2
        elif num == 4:
            operator = '/'
            self.math_answer = num1/num2
        expression = str(num1) + " " + operator + " " + str(num2)
        return expression

    def answer_choice(self):
        return random.randrange(1,100)

    def run(self):
        
        self.menu()
        self.running = True
        self.pause = True
        while self.running:
            for event in pygame.event.get():
                
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.running = False

                    if event.key == K_RETURN:
                        self.pause = False

                    if event.key == K_m:
                        self.mode = 'm'
                        self.pause = False

                    if event.key == K_t:
                        self.mode = 't'
                        self.pause = False

                    if event.key == K_n:
                        self.mode = 'n'
                        self.pause = False

                    if not self.pause:
                        if event.key == K_LEFT:
                            self.snake.move_left()

                        if event.key == K_RIGHT:
                            self.snake.move_right()

                        if event.key == K_UP:
                            self.snake.move_up()

                        if event.key == K_DOWN:
                            self.snake.move_down()

                    if self.mode == 'm':
                        num1 = self.math.generate_num1
                        num2 = self.math.generate_num2
                        op = self.math.generate_operator
                        self.expression = str(num1) + " " + str(op) + " " + str(num2)
                    if self.mode == 't':
                        #print("hello")
                        pass
                    if self.mode == 'n' and self.count == 0:
                        self.snake.length = 1
                        self.count += 1
                        #pass

                elif event.type == QUIT:
                    self.running = False
            try:
                if not self.pause:
                    self.play()

            except Exception as e:
                #keep in this order - else it won't show the right end score!!!!
                if self.snake.length == 0:
                    self.snake_zero = True
                
                self.end_of_game()
                self.pause = True
                self.reset()
                

            time.sleep(0.15)

    def print_text(font, x, y, text, color=(255,255,255), shadow=True):
        if shadow:
            imgText = font.render(text, True, (0,0,0))
            screen.blit(imgText, (x-2,y-2))
        imgText = font.render(text, True, color)
        screen.blit(imgText, (x,y))
    