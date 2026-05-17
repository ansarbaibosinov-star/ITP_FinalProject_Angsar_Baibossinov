import background
import pygame
import events
import sound
from save import save_score, load_score
from plane import Hero
from enemy import Enemy
from scores import Scores

pygame.init()
sound.bg_music()
pygame.display.set_caption("SKY ADVENTURE")
window = pygame.display.set_mode((1200, 800))
clock = pygame.time.Clock()


menu_bg = pygame.image.load('background/menu.png').convert()
menu_bg = pygame.transform.scale(menu_bg, (1200, 800))
game_over_bg = pygame.image.load('background/game_over.png').convert()
game_over_bg = pygame.transform.scale(game_over_bg, (1200, 800))
you_win_bg = pygame.image.load('background/you_win.png').convert()
you_win_bg = pygame.transform.scale(you_win_bg, (1200, 800))
start_button_rect = pygame.Rect(400, 420, 400, 150)
restart_button_rect = pygame.Rect(430, 580, 340, 120)

#You Win
next_level_rect = pygame.Rect(370, 650, 460, 120)

game_state = "menu"

window.fill((10, 68, 210))
background = background.Background()
ro = Hero(window)
enemies = pygame.sprite.Group()
scores = Scores(window)
scores.amount_photo = load_score()
friends = pygame.sprite.Group()
group_pearls = pygame.sprite.Group()
pygame.time.set_timer(pygame.USEREVENT, 1800)



def reset_game():
    global hero, enemies, friends, group_pearls, scores
    hero = Hero(window)
    enemies.empty()
    friends.empty()
    group_pearls.empty()
    scores.amount_photo = 0


while True:
    if game_state == "menu":
        window.blit(menu_bg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if start_button_rect.collidepoint(event.pos):
                    reset_game()
                    game_state = "game"
    elif game_state == "game":
        events.event(enemies, scores, group_pearls, window)
        background.update()
        background.render(window)
        hero.update()
        events.make_rocket(enemies, window, friends)
        events.collide(hero, enemies, group_pearls)
        scores.show_health(hero)
        scores.draw_rocket()
        events.make_friend(friends, window)
        events.move_pearl(window, group_pearls)

        if hero.health < 1:
            game_state = "game_over"
        elif scores.amount_photo > 9:  # Если сбили больше 9 ракет
            game_state = "you_win"

    elif game_state == "game_over":
        window.blit(game_over_bg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Выход в меню по ESC
                    game_state = "menu"
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if restart_button_rect.collidepoint(event.pos):  # Клик по RESTART
                    reset_game()
                    game_state = "game"

    elif game_state == "you_win":
        window.blit(you_win_bg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Выход в меню по ESC
                    game_state = "menu"
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if next_level_rect.collidepoint(event.pos):  # Клик по NEXT LEVEL
                    reset_game()
                    game_state = "game"  # Начинаем заново (или следующий уровень)
    pygame.display.update()
    clock.tick(60)











# import background
# import pygame
# import events
# import sound
#
# from plane import Hero
# from enemy import Enemy
# from scores import Scores
#
#
# pygame.init()
# sound.bg_music()
# pygame.display.set_caption("SKY ADVENTURE")
# window = pygame.display.set_mode((1200, 800))
# clock = pygame.time.Clock()
#
# menu_bg = pygame.image.load('background/menu.png').convert()
# menu_bg = pygame.transform.scale(menu_bg, (1200, 800))
#
# start_button_rect = pygame.Rect(400, 400, 400, 150)
#
# game_state = "menu"
#
#
# window.fill((10,68,210))
# background = background.Background()
# hero = Hero(window)
# enemies = pygame.sprite.Group()
# scores = Scores(window)
# friends = pygame.sprite.Group()
# group_pearls = pygame.sprite.Group()
#
# pygame.time.set_timer(pygame.USEREVENT,1800)
# # while True:
# #     events.event(enemies,scores,group_pearls,window)
# #
# #     # for event in pygame.event.get(): #чтобы закрылся
# #     #     if event.type == pygame.QUIT:
# #     #         exit() #было до этого чтобы закрывать но теперь в енеми будет закрывать
# #     background.update()
# #     background.render(window)
# #                                #что бы фон подключить
# #     hero.update()
# #     events.make_rocket(enemies,window,friends)
# #     events.collide(hero,enemies,group_pearls)
# #     scores.show_health(hero)
# #     scores.draw_rocket()
# #     events.make_friend(friends,window)
# #
# #     events.move_pearl(window, group_pearls)
# #     scores.finish(hero)
# #
# #     pygame.display.update() #для экрана
# #     clock.tick(60)
# #
# #
