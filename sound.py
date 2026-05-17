import pygame

def bg_music():
    pygame.mixer.music.load('sound/musicbg.mp3')
    pygame.mixer.music.play(-1)

def boom():
    boom = pygame.mixer.Sound('sound/boom.mp3')
    boom.play()

def bite_rocket():
    bite = pygame.mixer.Sound('sound/bite.mp3')
    bite.play()

def heal_hero():
    heal = pygame.mixer.Sound('sound/heal.mp3')
    heal.play()