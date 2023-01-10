import pygame
from setting import WIN_HEIGHT, WIN_WIDTH
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN
)

#Main code
def text_objects(text, font, color):
    text_surf = font.render(text, True, color)
    return text_surf, text_surf.get_rect()

def paused(main_txt, color, screen):
    text = pygame.font.SysFont("comicsansms",115)
    text_surf, text_rect = text_objects(main_txt, text, color)
    text_rect.center = ((WIN_WIDTH/2), (WIN_HEIGHT/2))
    screen.blit(text_surf, text_rect)

    while paused:
        music = pygame.mixer.music
        music.pause()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif (event.type == KEYDOWN and event.key == K_ESCAPE):
                music.unpause()
                return

        pygame.display.update()
        pygame.time.Clock().tick(15)

