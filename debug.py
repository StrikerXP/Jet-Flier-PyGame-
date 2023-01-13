import pygame

pygame.init()
font = pygame.font.Font(None, 30)

def debug(info, y = 10, x = 10):
    disp_surf = pygame.display.get_surface()
    debug_surf = font.render(str(info), True, 'Red')
    debug_rect = debug_surf.get_rect(topleft = (x,y))
    disp_surf.blit(debug_surf, debug_rect)
