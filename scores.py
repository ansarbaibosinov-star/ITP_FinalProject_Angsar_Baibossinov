import pygame

class Scores():

    def __init__(self, window):



        self.image_hp = pygame.transform.scale(
            pygame.image.load('stats/heart.png').convert_alpha(),
            (50, 50))

        self.image_rocket = pygame.transform.scale(
            pygame.image.load('stats/asset.png').convert_alpha(),
            (100, 100)
        )

        self.window = window
        self.amount_photo = 0
        self.game = True
        self.game_over = False

    def show_health(self, hero):

        x = 10
        for hp in range(hero.health):
            self.window.blit(self.image_hp, (x, 20))
            x += 50


    def draw_rocket(self):
        print_score = pygame.font.SysFont('comic', 50).render(str(self.amount_photo), True, (209, 52, 52))
        self.window.blit(self.image_rocket, (1050, 20))
        self.window.blit(print_score, (1110, 10))

    def finish(self,hero):
        if hero.health < 1:
            finish_text = pygame.font.SysFont('comic', 50 ).render('Ty vzorvalsya', True, (209, 52, 52))
            self.window.blit(finish_text, (500, 350))
            self.game = False
        elif self.amount_photo > 9:
            finish_text = pygame.font.SysFont('comic', 50 ).render(f'You are winner!!! {self.amount_photo}', True, (209, 52, 52))
            self.window.blit(finish_text, (500, 350))
            self.game = False