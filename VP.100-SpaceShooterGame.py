#import the pygame library 
import pygame
from pygame.locals import *

#anchor the pygame screen.
#Click on the arrow in the upper left corner to display in a new browser tab.
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,0)

#VP.100 - Space Shooter Game

#start the pygame module
pygame.init()

#variables for screen size: 
screen_width=1124 
screen_height=834

#create a screen with dimensions 
screen = pygame.display.set_mode((1124, 834))
clock = pygame.time.Clock()
running = True
dt = 0

#other variable initializers (fonts, text, images, etc)
font = pygame.font.SysFont("comicsansms", 72)

text = font.render("Space Shooter Game", True, (0, 128, 0))

carImg = pygame.image.load('SpaceShooter.png')
x1=150
y1=30

print("Hi I am a space ship!!!")

#name for the space ship
name=input("Please enter your name: ")
print("Hello", name)
print("Wow you are", name, "nice!")

keep_going = input("Are you ready to play my game?!?!?!?! Yes/No")

if keep_going == "Yes":
   print("Ok, lets do this!")

if keep_going == "No":
   print("Oh... well then whatever..")

print("Creator: This is where the adventure begins?!?!?!?!")
keep_going = input("Uhhhhh..?..!??", name, "...... Mb/Hi")

if keep_going == "Mb":
  print("Oh your fine I was just worried about you.")

if keep_going == "Hi":
  print("Oh hi??, you awake now I see.")

print("Creator: oh btw the credit of this game goes to Caleb A!!")
print("Ahhh man I should stop glazing myself, and let the user play the game already.")
print("Alright then enjoy my game I made then!!!")
keep_going = input("You might like it, I'm fine if you don't. Thanks/Ok/Cool")

if keep_going == "Thanks":
  print("You're welcome as always!!")

if keep_going == "Ok":
  print("Thumbs Up Emoji.")

if keep_going == "Cool":
  print("-o-")

#the clock will be used to regulate the frame rate
clock = pygame.time.Clock()

#set the screen caption 
pygame.display.set_caption("Space Shooter Game!")

# Background Colors or Code Color Constants
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

#fills the screen initially with white
screen.fill((255, 255, 255))

#position of the player on start

player.x = 244
player.y = 444

# What will make you get points (Enemy variables, survive)



x=265
y=112
#this code will still draw the circle in the same place as the code above
pygame.draw.circle(screen, RED, [265, 112], 40)

x=472
y=334
#this code will still draw the circle in the same place as the code above
pygame.draw.circle(screen, RED, [472, 334], 40)

#the clock will be used to regulate the frame rate
clock = pygame.time.Clock()

#variable controls the game loop
keep_playing=True

#tests if keep_playing variable is true and if it is the loop keeps repeating
while keep_playing==True:
    #iterates over the current list of events(checks for events)  
    for event in pygame.event.get(): 
    #will stop the game loop if escape is pressed (doesn't work in Codio)
      if event.type == pygame.QUIT: 
        keep_playing = False

    #controls for the game
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT] and pressed[pygame.K_a]:
     x1 =x1- 3
    if pressed[pygame.K_RIGHT] and pressed[pygame.K_d]:
     x1 =x1+ 3

    #all items drawn to the screen
    pygame.draw.rect(screen, RED, [75, 10, 50, 20], 2)

    screen.blit(text,(50, 100))

    #all items drawn to the screen go here
    pygame.draw.line(screen, WHITE, [0, 0], [100,100], 5)

    #This function call updates the screen
    pygame.display.update()

    #sets the frame rate
    clock.tick(60)

#quits the pygame module 
pygame.quit() 
quit()           