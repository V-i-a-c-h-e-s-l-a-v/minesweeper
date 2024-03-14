import pygame
import config

pygame.init()
pygame.mixer.music.load(config.MUSIC_FILE)


def music_play():
    pygame.mixer.music.play(-1)
