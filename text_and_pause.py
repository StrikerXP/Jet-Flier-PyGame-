import pygame
from setting import WIN_HEIGHT, WIN_WIDTH
from debug import debug
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN
)

pygame.init()

# Rise text rectangular
def text_objects(text, font, color):
    text_surf = font.render(text, True, color)
    return text_surf, text_surf.get_rect()


# Make button
def button(screen, color, x, y):
    pygame.draw.rect(screen, color, (x, y, WIN_WIDTH/11, WIN_HEIGHT/11), 0, 15)

# Pause menu
def paused(main_txt):
    screen = pygame.display.get_surface()
    text = pygame.font.SysFont("comicsansms",115)
    text_surf, text_rect = text_objects(main_txt, text, 'black')
    text_rect.center = ((WIN_WIDTH/2), (WIN_HEIGHT/3))
    resume_green = button(screen, 'green', WIN_WIDTH / 3, WIN_HEIGHT / 1.95)
    resume_black = button(screen, 'black', WIN_WIDTH / 3, WIN_HEIGHT / 1.95)
    exit_game = button(screen, (200, 0, 0), WIN_WIDTH / 1.77, WIN_HEIGHT / 1.95)

    while paused:
        music = pygame.mixer.music
        music.pause()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                pygame.quit()

            elif (event.type == KEYDOWN and event.key == K_ESCAPE):
                music.unpause()
                return

        # screen.fill((1, 1, 1))
        screen.blit(text_surf, text_rect)

        mouse = pygame.mouse.get_pos()
        debug(mouse)

        if WIN_WIDTH/3 + WIN_WIDTH/11 > mouse[0] > WIN_WIDTH/3 and WIN_HEIGHT/1.95 + WIN_HEIGHT/11 > mouse[1] > WIN_HEIGHT/1.95:
            resume_green
        else:
            resume_black

        pygame.display.update()
        pygame.time.Clock().tick(60)
