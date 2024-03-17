import pygame
import config

pygame.init()
pygame.mixer.music.load(config.MUSIC_FILE)
pygame.mixer.music.set_volume(config.MUSIC_VALUE)


def music_value(val: float):
    pygame.mixer.music.set_volume(val)


def music_play():
    pygame.mixer.music.play(-1)


def music_stop():
    pygame.mixer.music.stop()
