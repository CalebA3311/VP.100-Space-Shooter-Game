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

#setup bullets
bullets = []
bullet_speed = -4

# What will make you get points (Enemy variables, survive)

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
            elif event.type == pygame.KEYDOWN and event.key in (pygame.K_ESCAPE, pygame.K_q):
                running = False

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
            space_pressed = True
            if len(bullets) < 8:
                #This gets the player, sets the width of the bullet
                #And centers the bullet to the player
                rect = player.get_rect(center=player_rect.center)
                rect.width = 10
                rect.center = player_rect.center
                bullets.append(rect)

        #unlock space                
        if not keys[pygame.K_SPACE] and space_pressed:
            space_pressed = False

        for bullet in bullets:
            bullet.y += bullet_speed
            if bullet.bottom < 0:
                bullets.remove(bullet)
        
        # Drawing the game out
        for bullet in bullets:
            pygame.draw.rect(screen, WHITE, bullet)
        screen.blit(player, player_rect)

        #This function call updates the screen
        pygame.display.flip()

def start_menu():
    while True:
        screen.fill(BG)
        #set the screen caption
        game_title_font = pygame.font.SysFont("comicsansms", 72) 
        game_title = game_title_font.render("Space Shooter Game!", True, WHITE)
        mouse = pygame.mouse.get_pos()
        play_button = pygame.Rect(300, 300, 140, 75)
        quit_button = pygame.Rect(300, 380, 140, 75)

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