#import the pygame library 
import pygame

import os
#VP.100 - Space Shooter Game

#start the pygame module
pygame.init()

#variables for screen size: 
screen_width=690 
screen_height=290

#other variable initializers (fonts, text, images, etc)
font = pygame.font.SysFont("comicsansms", 72)
text = font.render("Space Shooter Game", True, (0, 128, 0))

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
print("Uhhhhh..?..!??", name, "......")
print("Creator: oh btw the credit of this game goes to Caleb A!!")
print("Ahhh man I should stop glazing myself, and let the user play the game already.")
print("Alright then enjoy my game I made then!!!")

#controls for the game
pressed = pygame.key.get_pressed()
if pressed[pygame.K_LEFT]:
  x1 =3
if pressed[pygame.K_RIGHT]:
  x1 =x1+ 3

#the clock will be used to regulate the frame rate
clock = pygame.time.Clock()

#set the screen caption 
pygame.display.set_caption("Space Shooter Game!")

# Background Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# What will make you get points (Enemy variables, survive)

#variable controls the game loop
keep_playing=True

#tests if keep_playing variable is true and if it is the loop keeps repeating
while keep_playing==True:

   #sets the frame rate
   clock.tick(60)

#quits the pygame module 
pygame.quit() 
quit()           