import pygame
import background as bg

from random import randint

class Pearl(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.pearls = ['stats/heal1.png','stats/heal2.png','stats/heal3.png']
        self.image = pygame.transform.scale(pygame.image.load('stats/heart.png').convert(),(50,50))

        self.rect = self.image.get_rect(center=(bg.WIDTH,randint(118,620)))


    def update(self):
        self.rect.x -= 3
        if self.rect.x < 0:
            self.kill()




    def draw(self,window):
        window.blit(self.image,self.rect)
