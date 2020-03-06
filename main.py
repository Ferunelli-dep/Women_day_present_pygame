import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((0, 0), flags=pygame.FULLSCREEN)
pygame.display.set_caption('Happy Women\'s day')
icon = pygame.image.load('icon.ico')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()
colors = {'White': [255, 255, 255],
          'Black': [34, 34, 34],
          'CWhite': [255, 235, 255]}
FPS = 60
rotation = 0
rotation_speed = 2

eight_orig = pygame.image.load('eight.png')
eight_orig.set_colorkey(colors['CWhite'])
eight = eight_orig.copy()
eight.set_colorkey(colors['CWhite'])
rect = eight.get_rect()
rect.center = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2

state = True
while state:
    clock.tick(FPS)
    screen.fill(colors['CWhite'])
    for event in pygame.event.get():
        if (event.type == pygame.locals.KEYDOWN) and (event.key == K_ESCAPE) or (event.type == pygame.QUIT):
            state = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if rect.collidepoint(pos):
                rect.center = rect.center[0] + 50, rect.center[1]
                pygame.draw.rect(screen, colors['CWhite'], rect, 1)

    old_center = rect.center
    rotation = (rotation - rotation_speed) % 360
    new_eight = pygame.transform.rotate(eight_orig, rotation)
    rect = new_eight.get_rect()
    rect.center = old_center
    screen.blit(new_eight, rect)
    pygame.display.flip()

pygame.quit()
