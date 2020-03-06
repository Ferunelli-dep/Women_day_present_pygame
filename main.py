import pygame
from pygame.locals import *

# Initalizing fonts and pygame
pygame.init()
pygame.font.init()

# Just constant vars
colors = {'White': [255, 255, 255],
          'Black': [34, 34, 34],
          'CWhite': [255, 235, 255]}
FPS = 60
rotation = 0
rotation_speed = 2

# Font Settings
MYFONT = pygame.font.SysFont('Comic Sans MS', 450)
# Importing images
icon = pygame.image.load('icon.ico')
eight = pygame.image.load('eight.png')
# Making RECT to place image by it's center
rect = eight.get_rect()
# Screen
screen = pygame.display.set_mode((0, 0), flags=pygame.FULLSCREEN)
# Size of screen. It's fullscreen, so size of monitor
SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()
# Where to place image EIGHT
rect.center = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
# Just windows settings
pygame.display.set_caption('Happy Women\'s day')
pygame.display.set_icon(icon)
# clock to make FPS
clock = pygame.time.Clock()

# Mb it'll be useless but these are boxes of coordinate. Center of each box
COORDINATE_BOXES_X = [x for x in range(0, SCREEN_WIDTH, SCREEN_WIDTH // 12)]
COORDINATE_BOXES_Y = [y for y in range(0, SCREEN_HEIGHT, SCREEN_HEIGHT // 12)]
# Just loop to run programm
state = True
while state:
    # Program quit on escape or exit
    for event in pygame.event.get():
        if (event.type == pygame.locals.KEYDOWN) and (event.key == K_ESCAPE) or (event.type == pygame.QUIT):
            state = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if button.collidepoint(pos):
                rect.center = rect.center[0] + 10, rect.center[1]
                pygame.draw.rect(screen, colors['Black'], rect, 1)

    # Filling screen with color
    screen.fill(colors['CWhite'])
    # Drawing eight pic
    button = screen.blit(eight, rect)
    pygame.draw.rect(screen, colors['Black'], rect, 1)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
