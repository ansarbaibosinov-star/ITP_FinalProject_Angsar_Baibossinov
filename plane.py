import pygame

class   Hero(pygame.sprite.Sprite):
    def __init__(self,window):
        super().__init__()
        self.index = 0
        self.move_right = [pygame.transform.scale(pygame.image.load('plane/planeYellow.png').convert_alpha(),(120,80)),
                           pygame.transform.scale(pygame.image.load('plane/planeYellow.png').convert_alpha(), (120, 80)),
                           pygame.transform.scale(pygame.image.load('plane/planeYellow.png').convert_alpha(), (120, 80)),
                           pygame.transform.scale(pygame.image.load('plane/planeYellow.png').convert_alpha(), (120, 80)),
                           pygame.transform.scale(pygame.image.load('plane/planeYellow.png').convert_alpha(), (120, 80)),
                           pygame.transform.scale(pygame.image.load('plane/planeYellow.png').convert_alpha(),(120, 80)),
                           pygame.transform.scale(pygame.image.load('plane/planeYellow.png').convert_alpha(),(120, 80)),
                           pygame.transform.scale(pygame.image.load('plane/planeYellow.png').convert_alpha(),(120, 80)),
                           pygame.transform.scale(pygame.image.load('plane/planeYellow.png').convert_alpha(),(120, 80)),
                           pygame.transform.scale(pygame.image.load('plane/planeYellow.png').convert_alpha(),(120, 80))]
        self.move_left =  [pygame.transform.scale(pygame.image.load('plane/leftaplaneYellow.png').convert_alpha(), (120, 80)),
                           pygame.transform.scale(pygame.image.load('plane/leftaplaneYellow.png').convert_alpha(), (120, 80)),
                           pygame.transform.scale(pygame.image.load('plane/leftaplaneYellow.png').convert_alpha(), (120, 80)),
                           pygame.transform.scale(pygame.image.load('plane/leftaplaneYellow.png').convert_alpha(), (120, 80)),
                           pygame.transform.scale(pygame.image.load('plane/leftaplaneYellow.png').convert_alpha(), (120, 80)),
                           pygame.transform.scale(pygame.image.load('plane/leftaplaneYellow.png').convert_alpha(), (120, 80)),
                           pygame.transform.scale(pygame.image.load('plane/leftaplaneYellow.png').convert_alpha(),(120, 80)),
                           pygame.transform.scale(pygame.image.load('plane/leftaplaneYellow.png').convert_alpha(),(120, 80)),
                           pygame.transform.scale(pygame.image.load('plane/leftaplaneYellow.png').convert_alpha(),(120, 80)),
                           pygame.transform.scale(pygame.image.load('plane/leftaplaneYellow.png').convert_alpha(),(120, 80))]
        self.window = window
        self.image = self.move_right[self.index]

        self.rect = self.image.get_rect(center=(600,400))
        self.speed = 4



        self.health = 3

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.image = self.move_right[self.index ]
            self.rect.x += self.speed
        if keys[pygame.K_LEFT] and self.rect.x > 0: #ограничения
            self.image = self.move_left[self.index ]
            self.rect.x -= self.speed
        if keys[pygame.K_UP] and self.rect.y > 18:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < 720:
            self.rect.y += self.speed
        if self.index < 9:
            self.index += 1
        else:
            self.index = 0


        self.window.blit(self.image, self.rect)
