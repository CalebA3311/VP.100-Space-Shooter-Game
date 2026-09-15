#import the pygame library 
import pygame

#VP.100 - Space Shooter Game

#variables for screen size: 
screen_width=690 
screen_height=290

#other variable initializers (fonts, text, images, etc)

print("Hi I am a space ship!!!")

#name for the space ship
name=input("Please enter your name: ")
print("Hello", name)
print("Wow you are", name, "nice!")

user=input("Are you ready to play my game?!?!?!?! Yes/No")

def Yes():
    print("Ok, lets do this!")

Yes()

def No():
    print("Oh... well then whatever..")

No()

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

# What will make you get points (Enemy variables, )

#variable controls the game loop
keep_playing=True

#tests if keep_playing variable is true and if it is the loop keeps repeating
while keep_playing==True:

   #sets the frame rate
   clock.tick(60)

#quits the pygame module 
pygame.quit() 
quit()           