import pygame
from pygame.locals import *
import set_classes as set
pygame.init()
screen = pygame.display.set_mode((0, 0), flags=pygame.FULLSCREEN)
pygame.display.set_caption('Happy Women\'s day')
clock = pygame.time.Clock()

SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()

icon = pygame.image.load('pics/icon.ico')
background = pygame.image.load('pics/background.png').convert_alpha()
eight_orig = pygame.image.load('pics/eight.png').convert_alpha()
text_1 = pygame.image.load("pics/text_1.png").convert_alpha()
text_2 = pygame.image.load("pics/text_2.png").convert_alpha()
text_3 = pygame.image.load("pics/text_3.png").convert_alpha()

flower_1 = set.Flowers('pics/flws/yellow.png', SCREEN_WIDTH, SCREEN_HEIGHT)
flower_2 = set.Flowers('pics/flws/camomile.png', SCREEN_WIDTH, SCREEN_HEIGHT)
flower_3 = set.Flowers('pics/flws/orange.png', SCREEN_WIDTH, SCREEN_HEIGHT)
flower_4 = set.Flowers('pics/flws/crocus.png', SCREEN_WIDTH, SCREEN_HEIGHT)
flower_5 = set.Flowers('pics/flws/pink.png', SCREEN_WIDTH, SCREEN_HEIGHT)
flower_6 = set.Flowers('pics/flws/purple.png', SCREEN_WIDTH, SCREEN_HEIGHT)
flower_7 = set.Flowers('pics/flws/white.png', SCREEN_WIDTH, SCREEN_HEIGHT)
flower_8 = set.Flowers('pics/flws/yellow-orange.png', SCREEN_WIDTH, SCREEN_HEIGHT)
flower_9 = set.Flowers('pics/flws/red.png', SCREEN_WIDTH, SCREEN_HEIGHT)
flower_10 = set.Flowers('pics/flws/rose.png', SCREEN_WIDTH, SCREEN_HEIGHT)
flower_11 = set.Flowers('pics/flws/violete.png', SCREEN_WIDTH, SCREEN_HEIGHT)
flower_12 = set.Flowers('pics/flws/yellow.png', SCREEN_WIDTH, SCREEN_HEIGHT)
flower_13 = set.Flowers('pics/flws/camomile.png', SCREEN_WIDTH, SCREEN_HEIGHT)
flower_14 = set.Flowers('pics/flws/orange.png', SCREEN_WIDTH, SCREEN_HEIGHT)
flower_15 = set.Flowers('pics/flws/crocus.png', SCREEN_WIDTH, SCREEN_HEIGHT)
flower_16 = set.Flowers('pics/flws/pink.png', SCREEN_WIDTH, SCREEN_HEIGHT)
flower_17 = set.Flowers('pics/flws/purple.png', SCREEN_WIDTH, SCREEN_HEIGHT)
flower_18 = set.Flowers('pics/flws/white.png', SCREEN_WIDTH, SCREEN_HEIGHT)
flower_19 = set.Flowers('pics/flws/yellow-orange.png', SCREEN_WIDTH, SCREEN_HEIGHT)
flower_20 = set.Flowers('pics/flws/red.png', SCREEN_WIDTH, SCREEN_HEIGHT)
flower_21 = set.Flowers('pics/flws/rose.png', SCREEN_WIDTH, SCREEN_HEIGHT)
flower_22 = set.Flowers('pics/flws/violete.png', SCREEN_WIDTH, SCREEN_HEIGHT)

flowers = pygame.sprite.Group()
flowers.add(flower_1, flower_2, flower_3, flower_4, flower_5, flower_6,
            flower_7, flower_8, flower_9, flower_10, flower_11,
            flower_12, flower_13, flower_14, flower_15, flower_16, flower_17,
            flower_18, flower_19, flower_20, flower_21, flower_22
            )

pygame.display.set_icon(icon)
rect_bg = background.get_rect()
rect_bg.left, rect_bg.top = [0, 0]
rect_T0 = text_1.get_rect()
rect_T1 = text_2.get_rect()
rect_T2 = text_3.get_rect()

colors = {'White': [255, 255, 255],
          'Black': [34, 34, 34],
          'CWhite': [255, 235, 255]}
FPS = 80
rotation = 0
rotation_speed = 2
WIDTH_CENTER = SCREEN_WIDTH // 2
HEIGHT_CENTER = SCREEN_HEIGHT // 2
eight = eight_orig.copy()
rect = eight.get_rect()
rect.center = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2

rect_T0.center = SCREEN_WIDTH // 2, SCREEN_HEIGHT + 250
rect_T1.center = SCREEN_WIDTH // 2, SCREEN_HEIGHT + 1000
rect_T2.center = SCREEN_WIDTH // 2, SCREEN_HEIGHT + 1250
T_Y_finish = [250, 600, 850]

pos_state_0 = False
pos_state_1 = False
state = True
eight_pressed = False
rotation_flag = True
eight_visibility = True
screen.fill(colors['White'])
y_0 = SCREEN_HEIGHT + 250
y_1 = SCREEN_HEIGHT + 600
y_2 = SCREEN_HEIGHT + 850
visibility_1 = True
visibility_2 = True
visibility_3 = True
while state:
    clock.tick(FPS)
    flower_1.update()
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
            if rect.bottom > -0:
                HEIGHT_CENTER -= 5
                rect.center = WIDTH_CENTER, HEIGHT_CENTER
            else:
                eight_pressed = False
                eight_visibility = False
    elif eight_visibility:
        rect = eight_orig.get_rect()
        rect.center = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
        screen.blit(eight_orig, rect)
    elif visibility_1 or visibility_2 or visibility_3:
        if y_0 > T_Y_finish[0]:
            y_0 -= 10
            rect_T0.center = (SCREEN_WIDTH // 2, y_0)
        else:
            pos_state_0 = True
        if pos_state_0:
            if rect_T1.top > SCREEN_HEIGHT:
                y_1 -= 3
                rect_T1.center = (SCREEN_WIDTH // 2, y_1)
            elif y_1 > T_Y_finish[1]:
                y_1 -= 12
                rect_T1.center = (SCREEN_WIDTH // 2, y_1)
            else:
                pos_state_1 = True
        if pos_state_1:
            visibility_1 = False
            if rect_T2.top > SCREEN_HEIGHT:
                y_2 -= 7
                rect_T2.center = (SCREEN_WIDTH // 2, y_2)
            elif y_2 > -100:
                y_2 -= 12
                rect_T2.center = (SCREEN_WIDTH // 2, y_2)
                if y_2 > T_Y_finish[2] - 200:
                    visibility_2 = False
            else: visibility_3 = False
        if visibility_1:
            screen.blit(text_1, rect_T0)
        if visibility_2:
            screen.blit(text_2, rect_T1)
        if visibility_3:
            screen.blit(text_3, rect_T2)
    else:
        flowers.update()
        flowers.draw(screen)
        flowers.update()
        flowers.draw(screen)
    pygame.display.flip()

pygame.quit()
