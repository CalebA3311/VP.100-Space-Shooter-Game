#import the pygame library 
import pygame
from pygame.locals import *

#anchor the pygame screen.
#Click on the arrow in the upper left corner to display in a new browser tab.
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (25, 25)

#VP.100 - Space Shooter Game

#start the pygame module
pygame.init()

#variables for screen size: 
screen_width=1124
screen_height=834

#create a screen with dimensions 
screen = pygame.display.set_mode((screen_width, screen_height))
game_title = pygame.display.set_caption("Space Shooter Game!")
clock = pygame.time.Clock()

#other variable initializers (fonts, text, images, etc)
font = pygame.font.SysFont("comicsansms", 40)
text = font.render("Space Shooter Game", True, (0, 128, 0))

#the clock will be used to regulate the frame rate
clock = pygame.time.Clock()

#set the screen caption 
pygame.display.set_caption("Space Shooter Game!")

# Background Colors or Code Color Constants
RED = (255, 0, 0)
WHITE = (255, 255, 255)
LIGHT = (170, 170, 170)
DARK = (100, 100, 100)
BG = (0, 0, 0)

#fills the screen initially with white
screen.fill(BG) 

#position of the player on start
player_image = pygame.image.load("SpaceShooter.png")
player_image_surface = player_image.convert()
player = pygame.transform.scale(player_image_surface, (50, 40))
player_rect = player.get_rect(center=(screen_width // 2, screen_height - 50))
player_speed = 10

#position of the enemy 1 on start
enemy_image = pygame.image.load("TrollfaceEnemy.png")
enemy_image_surface = enemy_image.convert()
enemy = pygame.transform.scale(enemy_image_surface, (60, 10))
enemy_rect = player.get_rect(center=(screen_width // 2, screen_height - 50))
enemy_speed = 8

#position of the enemy 2 on start
enemy_image = pygame.image.load("EvilFaceEmoji.jpeg")
enemy_image_surface = enemy_image.convert()
enemy = pygame.transform.scale(enemy_image_surface, (60, 20))
enemy_rect = player.get_rect(center=(screen_width // 2, screen_height - 50))
enemy_speed = 5

#position of the enemy 3 on start
enemy_image = pygame.image.load("EnemySmile.jpg")
enemy_image_surface = enemy_image.convert()
enemy = pygame.transform.scale(enemy_image_surface, (60, 80))
enemy_rect = player.get_rect(center=(screen_width // 2, screen_height - 50))
enemy_speed = 7

#position of the enemy 4 on start
enemy_image = pygame.image.load("MadEmojiEnemy.png")
enemy_image_surface = enemy_image.convert()
enemy = pygame.transform.scale(enemy_image_surface, (60, 45))
enemy_rect = player.get_rect(center=(screen_width // 2, screen_height - 50))
enemy_speed = 11

#position of the enemy 5 on start
enemy_image = pygame.image.load("EvilCandyLarry.jpeg")
enemy_image_surface = enemy_image.convert()
enemy = pygame.transform.scale(enemy_image_surface, (60, 50))
enemy_rect = player.get_rect(center=(screen_width // 2, screen_height - 50))
enemy_speed = 8

#And Lastly, position of the enemy 6 on start
enemy_image = pygame.image.load("SadEmojiEnemy.jpeg")
enemy_image_surface = enemy_image.convert()
enemy = pygame.transform.scale(enemy_image_surface, (60, 90))
enemy_rect = player.get_rect(center=(screen_width // 2, screen_height - 50))
enemy_speed = 9

#setup bullets
bullets = []
bullet_speed = -4

#setup enemies
enemies = []
enemy_down_speed = -2

#Enemies showing up on screen
#1. Creating the first enemy.
enemy_image = pygame.image.load("TrollfaceEnemy.png")
x1=60
y1=10
#2. Creating the second enemy.
enemy_image = pygame.image.load("EvilFaceEmoji.jpeg")
x1=60
y1=20
#3. Creating the thrid enemy.
enemy_image = pygame.image.load("EnemySmile.jpg")
x1=60
y1=80
#4 Creating the fourth enemy.
enemy_image = pygame.image.load("MadEmojiEnemy.png")
x1=60
y1=45
#5 Creating the fifth enemy.
enemy_image = pygame.image.load("EvilCandyLarry.jpeg")
x1=60
y1=50
#6 Creating the sixth enemy.
enemy_image = pygame.image.load("SadEmojiEnemy.jpeg")
x1=60
y1=90

#What will make you get points (Enemy variables, survive)

#tests if running variable is true and if it is the loop keeps repeating
def play_game():
    running = True
    space_pressed = False
    dt = 0
    while running:
        clock.tick(60)
        screen.fill((0, 0, 0))
        #iterates over the current list of events(checks for events)  
        for event in pygame.event.get(): 
            #will stop the game loop if escape is pressed (doesn't work in Codio)
            if event.type == pygame.QUIT: 
                running = False
            #This code below is showing how the game is kicking you out and that above it and below is responing with the running = True.
            elif event.type == pygame.KEYDOWN and event.key in (pygame.K_ESCAPE, pygame.K_q):
                running = False

        #Also I want to just say a quick thing about the -= and the += mean, first off the -= is always used for the left side which is the left arrow movement for the game.
        #And for the += it means it is for the right side which is used for the right arrow only instead of the left arrow, and if we were to switch them over we could get an error,
        #Or if we switched them together we could get an error, but it would likely go the opposite which is going left will only go to the right, and the same thing as the right side, using right arrow will only make it go left instead of it going it's apporirate way.
        
        #controls for the game
        keys = pygame.key.get_pressed()
        #move player left
        if keys[pygame.K_LEFT] and player_rect.left > 0:
            player_rect.x -= player_speed
        #move player right
        if keys[pygame.K_RIGHT] and player_rect.right < screen_width:
            player_rect.x += player_speed
        
        #shoot bullet and lock space bar
        if keys[pygame.K_SPACE] and not space_pressed:
            space_pressed = Truescreen = pygame.display.set_mode((screen_width, screen_height))
            if len(bullets) < 8:
                #This gets the player, sets the width of the bullet
                #And centers the bullet to the player
                rect = player.get_rect(center=player_rect.center)
                #The code is just the width of how long the bullets are, and how long they are when being shot with space.
                rect.width = 10
                #This code below is making it the bullets in the center of the character as of the player as well.
                rect.center = player_rect.center
                #It is making it so it is adding the bullet to the list which is the bullets list I have.
                bullets.append(rect)

        #unlock space                
        if not keys[pygame.K_SPACE] and space_pressed:
            space_pressed = False

        for bullet in bullets:
            bullet.y += bullet_speed
            if bullet.bottom < 0:
                bullets.remove(bullet)

        #This statement below me is that the bullets will be drawn out is when you are shooting which is using the space bar and when you shoot, it make a small rectangle when shoot out becuase I made them in the sizes on lines 108 - 114.
        
        #Drawing the game out
        for bullet in bullets:
            pygame.draw.rect(screen, WHITE, bullet)
        screen.blit(player, player_rect)

        #This function call updates the screen
        pygame.display.flip()

def start_menu():

    while True:

        #I got these lines of code from geeksforgeeks.com and to my understanding it is used for to start the game up when it is running, and the quit_text is to be pressed with the mouse when you are playing the game.
        #The other one's is for the boxes that say play, and quit which if you were to click "play" it would bring you to the real game, and if you clicked "quit" it would exit out of the game like most games are if not all of them.
        #And lastly, the screen.blit I'm using is for to show up the game_title which is the "Space Shooter Game", also the "Play" button so people understand if they think it would be the quit button or an other button setting,
        #Also the quit_text so people can click "quit" at anytime if they don't want to play anymore.

        screen.fill(BG)
        #set the screen caption
        game_title_font = pygame.font.SysFont("comicsansms", 72) 
        game_title = game_title_font.render("Space Shooter Game!", True, WHITE)
        mouse = pygame.mouse.get_pos()
        play_button = pygame.Rect(300, 300, 170, 75)
        quit_button = pygame.Rect(300, 380, 170, 75) 

        pygame.draw.rect(screen, LIGHT if play_button.collidepoint(mouse) else DARK, play_button)
        pygame.draw.rect(screen, LIGHT if quit_button.collidepoint(mouse) else DARK, quit_button)

        play_text = font.render("Play", True, WHITE)
        quit_text = font.render("Quit", True, WHITE)

        screen.blit(game_title, (250, 150))
        screen.blit(play_text, (335, 305))
        screen.blit(quit_text, (335, 385))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(mouse):
                    play_game()

                if quit_button.collidepoint(mouse):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

# to start the game out
start_menu()