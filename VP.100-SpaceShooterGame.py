#import the pygame library 
import pygame

#VP.100 - Space Shooter Game

#other variable initializers (fonts, text, images, etc)

print("Hi I am a space ship!!!")

#name for the space ship
name=input("Please enter your name: ")
print("Hello", name)
print("Wow you are", name, "nice!")

print("Are you ready to play my game?!?!?!?! Yes/No")

def Yes():
    print("Ok, lets do this!")

Yes()

def No():
    print("Oh... well then whatever..")

No()

#the clock will be used to regulate the frame rate
clock = pygame.time.Clock(60)

#set the screen caption 
pygame.display.set_caption("Space Shooter Game!")

#fills the screen initially with white
screen.fill((255, 255, 255))

# What will make you get points (Enemy variables, )

#variable controls the game loop
keep_playing=True

#tests if keep_playing variable is true and if it is the loop keeps repeating
while keep_playing==True:

   #This code updates the screen
   pygame.display.update() 
   #sets the frame rate
   clock.tick(60)

#quits the pygame module 
pygame.quit() 
quit()           