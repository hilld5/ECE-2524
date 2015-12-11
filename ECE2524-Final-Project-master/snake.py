# Snake game -- Created By Moneeb Waseem
# To play the snake game, use the arrow keys to move
# If you run into the wall or a part of the snakes 
# body, the game is over

import curses
import random
from curses import KEY_LEFT, KEY_DOWN, KEY_UP, KEY_RIGHT, KEY_ENTER 
from random import randint

curses.initscr()
win = curses.newwin(20, 70, 0, 0)  #creates game window (70x20)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)

#Initialize the snake to move left when the game first starts
key = KEY_RIGHT
score = 0

#Intitial starting position of the snake
snake = [[5,10], [5,9], [5,8]]

#Initial Food Co-Ordiniate position
food = [10,20]

#add food to the screen
win.addch(food[0], food[1], '*')

#while the user has not hit enter
#if the user hits enter, the game is over
while key != 10:
  win.border(0)
  
  #Prints the score while you are playing the game
  win.addstr(0, 31, 'SCORE: ' + str(score) + ' ')
  
  #Prints the snake's head and body while you are playing the game
  win.addstr(19, 30, 'SNAKE GAME')
  
  #Increases the speed of the snake as the length of the snake increaess
  win.timeout(150-(len(snake)/5 + len(snake)/10) % 110)
  
  oldKey = key
  
  #check if space bar is pressed
  case = win.getch()
  key = key if case == -1 else case
  
  if key == ord(' '):
    key = -1
    
    while key != ord(' '):
      key = win.getch()
    key = oldKey
    continue
#check to see if a key other than the arrow keys is pressed
  if key not in [KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT, 10]:
  #if invalid key is pressed, the direction is the same as the previous direction
    key = oldKey

#Calcualte position of snake
  snake.insert(0, [snake[0][0] + (key == KEY_UP and -1) + (key == KEY_DOWN and 1), snake[0][1] + (key == KEY_RIGHT and 1) + (key == KEY_LEFT and -1)])

#checks ot see if the snake runs into the wall. If it does, then the game is over
  if snake[0][1] == 0 or snake[0][1] == 69 or snake[0][0] == 0 or snake[0][0] == 19:
    break
  

#checks to see if the snake runs into itself. if it does then then the game is over
  if snake[0] in snake[1:]:
    break

#checks to see if the snake eats the food and updates the score
  if snake[0] == food:
    food = []
    score += 1 #update score
    while food == []:
      food = [randint(1,18), randint(1, 68)] #calculate random coordintae for food
    
      if food in snake: 
        food = []
    win.addch(food[0], food[1], '*') #add another food
    
  else:
    last = snake.pop()
    win.addch(last[0], last[1], ' ') #get rid of trailing tail
    
  win.addch(snake[0][0], snake[0][1], 'O') #adds segment to the snake

curses.endwin() #close the window and show the game over display
print("GAME OVER")
print("\nSCORE = " + str(score)) #shows score

    
    
    
  




