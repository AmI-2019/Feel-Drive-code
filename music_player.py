import random

import pygame
from pygame.locals import *
import pygame.freetype

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
RED= (255,0,0)
BLACK=(0,0,0)


def playsong_voice():
    pygame.mixer.music.unpause()


def stopsong_voice():
    pygame.mixer.music.pause()



def nextsong(listOfSongs):
    index=random.randint
    pygame.mixer.music.load(listOfSongs[index])
    pygame.mixer.music.play()
    get_GUI(listOfSongs[index])


def get_GUI(song):
    display_surface = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Feel & Drive: music player')
    motto_label = pygame.font.Font('freesansbold.ttf', 25)
    motto = motto_label.render("WELCOME to you Feel & Drive experience", True, BLUE, RED)
    mottoRect = motto.get_rect()
    mottoRect.center = (600 // 2, 600 // 6)

    song_label = pygame.font.Font('freesansbold.ttf', 19)
    song = song_label.render(song[:-4], True, BLACK, WHITE)
    songRect = song.get_rect()
    songRect.center = (600 // 2, 600 // 2)

    command_label = pygame.font.Font('freesansbold.ttf', 19)
    command = command_label.render('Press a key to enable your assistant!', True, RED)
    commandRect = command.get_rect()
    commandRect.center = (600 // 2, 400)

