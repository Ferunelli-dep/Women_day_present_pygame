import pygame
import random


class Flowers(pygame.sprite.Sprite):
    def update(self):
        self.rect.y += self.speed
        self.rect.x += self.speed_x
        self.rotate()
        if self.rect.top > self.height + 10:
            self.rect.x = random.randrange(self.width - self.rect.width)
            self.rect.y = random.randrange(-200 - self.size, -self.size)
            self.speed = random.randrange(1, 4)

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def __init__(self, file, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.dir = file
        self.size = random.randint(200, 300)
        self.width, self.height = width, height
        self.image_orig = pygame.image.load(file).convert_alpha()
        self.image_orig = pygame.transform.scale(self.image_orig, (self.size, self.size))
        self.image = self.image_orig.copy()
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width - self.rect.width)
        self.rect.y = random.randrange(-200 - self.size, -self.size)
        self.speed = random.randrange(1, 10)
        self.speed_x = self.speed * random.uniform(-0.5, 0.5)
        self.rot = 0
        self.rot_speed = random.randrange(-2, 2)
        self.last_update = pygame.time.get_ticks()
