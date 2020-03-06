import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((0, 0), flags=pygame.FULLSCREEN)
pygame.display.set_caption('Happy Women\'s day')
icon = pygame.image.load('pics/icon.ico')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
background = pygame.image.load('pics/background.png').convert_alpha()
rect_bg = background.get_rect()
rect_bg.left, rect_bg.top = [0, 0]

SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()
colors = {'White': [255, 255, 255],
          'Black': [34, 34, 34],
          'CWhite': [255, 235, 255]}
FPS = 60
rotation = 0
rotation_speed = 2
WIDTH_CENTER = SCREEN_WIDTH // 2
HEIGHT_CENTER = SCREEN_HEIGHT // 2
eight_orig = pygame.image.load('pics/eight.png').convert_alpha()
eight = eight_orig.copy()
rect = eight.get_rect()
rect.center = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2


state = True
eight_pressed = False
rotation_flag = True
eight_visibility = True
screen.fill(colors['White'])

while state:
    clock.tick(FPS)
    screen.blit(background, rect_bg)
    for event in pygame.event.get():
        if (event.type == pygame.locals.KEYDOWN) and (event.key == K_ESCAPE) or (event.type == pygame.QUIT):
            state = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if rect.collidepoint(pos):
                eight_pressed = True
    if eight_pressed:
        if rotation_speed <= 60 and rotation_flag:
            rotation_speed += 0.3
        else:
            rotation_flag = False

        old_center = rect.center
        rotation = (rotation - rotation_speed) % 360
        new_eight = pygame.transform.rotate(eight_orig, rotation)
        rect = new_eight.get_rect()
        rect.center = old_center
        screen.blit(new_eight, rect)
        if not rotation_flag:
            if rect.bottom > 0:
                HEIGHT_CENTER -= 5
                rect.center = WIDTH_CENTER, HEIGHT_CENTER
            else:
                eight_pressed = False
                eight_visibility = False
    elif eight_visibility:
        rect = eight_orig.get_rect()
        rect.center = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
        screen.blit(eight_orig, rect)
    pygame.display.flip()

pygame.quit()
