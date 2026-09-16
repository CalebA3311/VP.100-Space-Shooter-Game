#import the pygame library 
import pygame

import os
#VP.100 - Space Shooter Game

#using turtle for drawing things
import turtle

#start the pygame module
pygame.init()

#variables for screen size: 
screen_width=690 
screen_height=290

#create a screen with dimensions 
screen = pygame.display.set_mode((screen_width, screen_height))

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
print("Uhhhhh..?..!??", name, "......")
print("Creator: oh btw the credit of this game goes to Caleb A!!")
print("Ahhh man I should stop glazing myself, and let the user play the game already.")
print("Alright then enjoy my game I made then!!!")

#player position



#the clock will be used to regulate the frame rate
clock = pygame.time.Clock()

#set the screen caption 
pygame.display.set_caption("Space Shooter Game!")

# Background Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# What will make you get points (Enemy variables, survive)



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
    if pressed[pygame.K_LEFT]:
     x1 =x1- 3
    if pressed[pygame.K_RIGHT]:
     x1 =x1+ 3
    if pressed[pygame.K_a]:
     x1 =x1- 3
    if pressed[pygame.K_d]:
     x1 =x1+ 3

    #all items drawn to the screen

    screen.blit((x1,y1))

    #all items drawn to the screen go here
    pygame.draw.line(screen, WHITE, [0, 0], [100,100], 5)

    #This function call updates the screen
    pygame.display.update()

    #sets the frame rate
    clock.tick(60)

#quits the pygame module 
pygame.quit() 
quit()           