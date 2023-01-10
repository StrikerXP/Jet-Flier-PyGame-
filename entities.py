import pygame
import random
from setting import WIN_HEIGHT, WIN_WIDTH, enemy_speed_min, enemy_speed_max
from pygame.locals import (
    RLEACCEL,
    K_w,
    K_s,
    K_a,
    K_d,
)

# Define a Player object by extending pygame.sprite.Sprites
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self, layer):
        super(Player, self).__init__()
        self.surf = pygame.image.load('img/jet.png').convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()
        self._layer = layer

    # Move the sprite based on user keypresses
    def move(self, key):
        if key[K_w]:
            self.rect.move_ip(0, -3)
        if key[K_s]:
            self.rect.move_ip(0, 3)
        if key[K_a]:
            self.rect.move_ip(-3, 0)
        if key[K_d]:
            self.rect.move_ip(3, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIN_WIDTH:
            self.rect.right = WIN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= WIN_HEIGHT:
            self.rect.bottom = WIN_HEIGHT

    def dead(self):
        self.surf = pygame.image.load('img/boom.png').convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)

#Creating enemy class by extending pygame.sprite.Sprite
class Enemy(pygame.sprite.Sprite):
    def __init__(self, layer):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load('img/missile.png').convert()
        self.surf.set_colorkey(('white'))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(WIN_WIDTH, WIN_WIDTH + 20),
                random.randint(0, WIN_HEIGHT)
            )
        )
        self.speed = random.randint(enemy_speed_min, enemy_speed_max)
        self._layer = layer

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


# Define the cloud object by extending pygame.sprite.Sprite
# Use an image for a better-looking sprite
class Cloud(pygame.sprite.Sprite):
    def __init__(self, layer):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load('img/cloud.png').convert()
        self.surf.set_colorkey('black', RLEACCEL)
        self.rect = self.surf.get_rect(
            # The starting position is randomly generated
            center=(
                random.randint(WIN_WIDTH + 30, WIN_WIDTH + 100),
                random.randint(0, WIN_HEIGHT)
            )
        )
        self._layer = layer

    # Move the cloud based on a constant speed
    # Remove the cloud when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-3, 0)
        if self.rect.right < 0:
            self.kill()
