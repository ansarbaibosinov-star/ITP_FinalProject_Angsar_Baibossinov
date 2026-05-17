import pygame
from background import WIDTH
from random import randint
class Enemy(pygame.sprite.Sprite):
    def __init__(self,speed):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('enemy/rocket.png'),(75,75))
        self.rect = self.image.get_rect()
        self.speed = randint(2, 4)
        self.rect.x = WIDTH
        self.rect.y = randint(118,620)

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()

    def draw(self, window):
        window.blit(self.image, self.rect)

