import pygame

WIDTH = 1200
HEIGHT = 800

class Background():
    def __init__(self):
        self.images = [pygame.transform.scale(pygame.image.load('background/bg1.png').convert(),(2048,HEIGHT)),
                      pygame.transform.scale(pygame.image.load('background/bg2.png').convert(), (2048, HEIGHT)),
                      pygame.transform.scale(pygame.image.load('background/bg3.png').convert(), (2048, HEIGHT)),
                      pygame.transform.scale(pygame.image.load('background/bg4.png').convert(), (2048, HEIGHT)),
                      pygame.transform.scale(pygame.image.load('background/bg5.png').convert(), (2048, HEIGHT)),
                      pygame.transform.scale(pygame.image.load('background/bg6.png').convert(), (2048, HEIGHT)),
                      pygame.transform.scale(pygame.image.load('background/bg7.png').convert(), (2048, HEIGHT)),
                      pygame.transform.scale(pygame.image.load('background/bg8.png').convert(), (2048, HEIGHT)),
                      pygame.transform.scale(pygame.image.load('background/bg9.png').convert(), (2048, HEIGHT)),
                      pygame.transform.scale(pygame.image.load('background/bg1.png').convert(), (2048, HEIGHT))
                      ]
        self.index = 0
        self.image1 = self.images[self.index]
        self.image2 = self.images[self.index + 1]
        self.rect = self.image1.get_rect()
        self.moving_speed  = 3
        self.bgX1 = 0
        self.bgX2 = self.rect.width

    def change_background(self):
        self.index = (self.index + 1) % len(self.images)
        self.image = self.images[self.index]
    def update(self):
        self.bgX1 -= self.moving_speed
        self.bgX2 -= self.moving_speed

        if self.bgX1 <= - self.rect.width:
            self.bgX1 = self.rect.width
            self.index = ((self.index + 1) % len(self.images))
            self.image1 = self.images[self.index]
            # self.change_background()
            # менять фон
        if self.bgX2 <= - self.rect.width:
            self.bgX2 = self.rect.width
            self.index = ((self.index + 1) % len(self.images))
            self.image2 = self.images[self.index]
    def render(self, window):
        window.blit(self.image1, (self.bgX1, 0))
        window.blit(self.image2, (self.bgX2, 0))
