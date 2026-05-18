import pygame
from enemy import Enemy
from random import randint
from sound import boom,bite_rocket,heal_hero
from pearl import Pearl
from save import save_score


def event(enemies,scores,group_pearls,window):
    for event in pygame.event.get():
       if event.type == pygame.USEREVENT:
           pearl = Pearl()
           make_pearl(group_pearls,pearl)
       if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_ESCAPE:
               do_pause(window)
       if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
           x,y = event.pos
           for rocket in enemies:
               if rocket.rect.collidepoint(x,y):
                   boom()
                   enemies.remove(rocket)

                   rocket.image = pygame.transform.scale(pygame.image.load('enemy/break_rocket.png').convert_alpha(),(100,100))

                   scores.amount_photo += 1
                   save_score(scores.amount_photo)

       if event.type == pygame.QUIT:
           exit()

def make_rocket(enemies,window,friends):
    enemies.update()
    enemies.draw(window)
    if len(enemies) < 5:
        enemy = Enemy(randint(4,6))
        enemies.add(enemy)
        friends.add(enemy)


def make_friend(friend,window):
    friend.update()
    friend.draw(window)
def make_pearl(group_pearls,pearl):
    group_pearls.add(pearl)
def move_pearl(window,group_pearls):
    group_pearls.update()
    group_pearls.draw(window)
def collide(hero,enemies,group_pearls):
    if pygame.sprite.spritecollide(hero,enemies,True):
        bite_rocket()
        hero.health -= 1
    if pygame.sprite.spritecollide(hero,group_pearls,True):
        if hero.health < 3:
            hero.health += 1
            heal_hero()
def do_pause(window):
    pause = True

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause = False

        pause_text = pygame.font.SysFont('comic', 50).render(
            'PAUSE:press ESC to continue', True, (150, 200, 52)
        )

        window.blit(pause_text, (350, 400))
        pygame.display.update()