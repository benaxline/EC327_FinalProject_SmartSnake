# EC327 - Introduction to Software Engineering 

## Project Information

Team Name: Smart Snake

Team Members:   
Albert Zhao(U68071332): albertz@bu.edu   
Eric Davis(U28393843): edavis19@bu.edu   
Benjamin Axline(U19649803): baxline@bu.edu

Project Start Date: Dec 3rd, 2022
Project End Date: Dec 12th, 2022

*See detailed project timeline, go to documents folder and see "EC327 Smark Snake Project Timeline"*


## Project Overview:   

This "Smart Snake" Game is derived from the traditional style snake game. In the original, each time the snake eats an apple, the length of the snake grows. Our game consists of three different modes: Math mode, Trivia mode, and normal mode. In the math and trivia mode, each time the snake eats an apple, the user is prompted with a question related to their selected mode. If the user gets the question incorrect, the snake gets longer, and if the user gets the question correct, the snake gets shorter. In these modes, the goal is to decrease the snake length until it is zero. If the snake hits itself before getting to zero or if they hit a wall, they lose. If they reach zero length, they win! In our normal mode, the game works like the original. When the snake eats an apple, they grow longer. The goal is to create the longest snake.

This project is utilizes Python's object-oriented programming. It also uses Pygame as the user interface. The program consists of five python classes: Apple, Game, Trivia, Math, and Snake. Each class handles their respective objects. The Apple class handles the creation of the apple the snake eats, the Game class handles the innerworkings of the game, the Snake class handles the attributes of the snake, the math and trivia classes handle the math and trivia modes, respectfully. 

For more information on the project, please go to the documentation folder

## How to Play:

To play our game, it is very simple. Download all of the files from the Github repository, and ensure that pygame is also downloaded on your device. Once the repository is cloned and pygame is installed, our game can be ran by typing in the command line: "python main.py". This command will create a new pygame window, and the game can then be played!

Link to Video:
https://youtu.be/b1D-0l0GVpE


## Setting up Project Environment:

In order to run the program, you need to make sure that your computer has the Python Programming Language installed. 
Usually, python comes pre-installed on your machine if you have a mac. However, if not, you can click on the following link to install python.

For Windows, follow: https://www.python.org/downloads/windows/ 

For Mac, follow: https://www.python.org/downloads/macos/

For Other Environment, check Python.org for more download information 


After you have the python installed on your machine, you then need to install pygame. 
Pygame is a python module: 

Follow https://www.pygame.org/wiki/GettingStarted to install pygame on your machine.

Once everything is installed. You should now be able to run our program the Smart Snake!!!


## How to Start the Game:
To start the game/program, open the terminal on your machine.
Make sure that your current directory is in *code*
Once you are in the code folder, or the code directory, type: 
```
python3 -m main
```
or
```
python main.py
```
in your terminal

This should launch the game, and you should be able to play the game from there. 

## Other Information:
In the documentation folder, you can find a lot of detailed information regarding our project:
- EC327_Smart_Snake_ProjectTimeline.pdf: contains our project timeline 
- EC327_Smart_Snake_ProjectDocumentation.pdf: contains our project overview and technical documentation
- EC327 _Smart_Snake_StatementofWork.pdf: contains what each person worked on 
- SmartSnake_ProjectArchitecture.pptx: contains our project architecture presentation

Folders:
- Code: Contains all the necessary code to run the game
- Documentation: Contains all the project documentation
- Mics: Miscellaneous files, not important
