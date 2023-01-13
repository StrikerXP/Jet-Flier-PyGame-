# Import the pygame module
import pygame, sys
from text_and_pause import paused
from debug import debug
from entities import Player, Enemy, Cloud
from setting import WIN_HEIGHT, WIN_WIDTH

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_ESCAPE,
    K_SPACE,
    KEYDOWN,
    QUIT,
)

# Setup for sounds
pygame.mixer.init()

# Initialize pygame
pygame.init()

time = pygame.time

# Load and play background music
# Sound source: http://ccmixter.org/files/Apoxode/59262
# License: https://creativecommons.org/licenses/by/3.0/
pygame.mixer.music.load("sound/Apoxode_-_Electric_1.mp3")
pygame.mixer.music.play(loops = -1)

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
# pygame.FULLSCREEN
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

#Custom event number itterator
event_counter = int(0)

def event_counter_iterator():
    global event_counter
    event_counter += 1
    return event_counter

# Create a custom event for adding a new enemy and a cloud
ADDENEMY = pygame.USEREVENT + (event_counter_iterator())
pygame.time.set_timer(ADDENEMY, 250)
ADDCLOUD = pygame.USEREVENT + (event_counter_iterator())
pygame.time.set_timer(ADDCLOUD, 1000)

# Instantiate player. Right now, this is just a rectangle.
player = Player(2)

# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_layers = pygame.sprite.LayeredUpdates()
all_layers.add(player)

# Variable to keep the main loop running
running = True

# Main loop
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == QUIT:
            running = False
            pygame.quit()
            sys.exit()

        elif (event.type == KEYDOWN and event.key == K_ESCAPE):
            paused('Pause')

        # Add a new enemy?
        elif event.type == ADDENEMY:
            # Create the new enemy and add it to sprite groups
            new_enemy = Enemy(1)
            enemies.add(new_enemy)
            all_layers.add(new_enemy)

        # Add clouds
        elif event.type == ADDCLOUD:
            new_cloud = Cloud(0)
            clouds.add(new_cloud)
            all_layers.add(new_cloud)

        # Attack
        elif (event.type == KEYDOWN and event.key == K_SPACE):
            player.attack()

    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()
    player.move(pressed_keys)

    # Update player, enemy position and clouds
    all_layers.update()

    # Fill the screen with white
    screen.fill((135, 206, 250))

    # Draw all sprites
    for entity in all_layers:
        screen.blit(entity.surf, entity.rect)

    # Check if any enemies have collided with the player
    if pygame.sprite.spritecollideany(player, enemies):
        # If so, then remove the player and stop the loop
        screen.fill((135, 206, 250))
        player.dead()
        # debug(player.surf, 50)
        pygame.display.update(player)
        pygame.time.wait(3000)
        paused('Game Over')
        running = False

    # This line says "Draw surf onto the screen at the center"
    pygame.display.update()
    time.Clock().tick(60)
