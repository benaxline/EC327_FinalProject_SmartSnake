
EC327 - Introduction to Software Engineering 

Final Project - Snake Game with different modes

Initial Snake Game - sourced from CodeBasics

Team Name: Smart Snake

Team Members:   
Albert Zhao: albertz@bu.edu   
Eric Davis: edavis19@bu.edu   
Benjamin Axline: baxline@bu.edu


Overview:   

This "Smart Snake" Game is derived from the traditional style snake game. In the original, each time the snake eats an apple, the length of the snake grows. Our game consists of three different modes: Math mode, Trivia mode, and normal mode. In the math and trivia mode, each time the snake eats an apple, the user is prompted with a question related to their selected mode. If the user gets the question incorrect, the snake gets longer, and if the user gets the question correct, the snake gets shorter. In these modes, the goal is to decrease the snake length until it is zero. If the snake hits itself before getting to zero or if they hit a wall, they lose. If they reach zero length, they win! In our normal mode, the game works like the original. When the snake eats an apple, they grow longer. The goal is to create the longest snake.


This project is utilizes Python's object-oriented programming. It also uses Pygame as the user interface. The program consists of five python classes: Apple, Game, Trivia, Math, and Snake. Each class handles their respective objects. The Apple class handles the creation of the apple the snake eats, the Game class handles the innerworkings of the game, the Snake class handles the attributes of the snake, the math and trivia classes handle the math and trivia modes, respectfully. 


How to Play:
To play our game, it is very simple. Download all of the files from the Github repository, and ensure that pygame is also downloaded on your device. Once the repository is cloned and pygame is installed, our game can be ran by typing in the command line: "python main.py". This command will create a new pygame window, and the game can then be played!

Link to Video:
