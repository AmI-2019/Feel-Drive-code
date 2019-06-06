import os
import random
import pygame
import interaction
from pygame.locals import *
import pygame.freetype
import speech2text
from config import SONG_DIRECTORY


SONG_END = pygame.USEREVENT + 1
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
RED = (255, 0, 0)
BLACK = (0, 0, 0)


def playsong_voice():
    pygame.mixer.music.unpause()


def stopsong_voice():
    pygame.mixer.music.pause()


def nextsong(listOfSongs):
    index=random.randint(0, len(listOfSongs) - 1)
    pygame.mixer.music.load(listOfSongs[index])
    pygame.mixer.music.play()
    get_GUI(listOfSongs[index])


def init_player(listOfSongs):
    index = random.randint(0, len(listOfSongs) - 1)
    song = listOfSongs[index]
    pygame.mixer.music.set_endevent(SONG_END)
    pygame.mixer.music.load(song)
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play()
    get_GUI(song)


def changesong_voice(listOfSongs):
    index=random.randint(0, len(listOfSongs) - 1)
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

    display_surface.fill(WHITE)
    display_surface.blit(motto, mottoRect)

    songRect = song.get_rect()
    songRect.center = (600 // 2, 600 // 2)
    display_surface.blit(song, songRect)

    commandRect = command.get_rect()
    commandRect.center = (600 // 2, 400)
    display_surface.blit(command, commandRect)

    return display_surface


if __name__ == '__main__':
    pygame.init()
    pygame.font.init()
    songs = interaction.get_songs('Happiness')
    os.chdir(SONG_DIRECTORY)
    init_player(songs)

    done = False
    while not done:
        for ev in pygame.event.get():
            if ev.type == QUIT:
                done = True
            elif ev.type == KEYDOWN:
                pygame.mixer.music.set_volume(0.1)
                vocal_command = speech2text.recognize()
                if vocal_command == "exit":
                    done = True
                elif vocal_command == "stop":
                    stopsong_voice()
                elif vocal_command == "change":
                    changesong_voice(songs)
                elif vocal_command == "play":
                    playsong_voice()
                else:
                    print("Vocal Command not recognized")
            elif ev.type == SONG_END:
                nextsong()
            pygame.mixer.music.set_volume(1.0)
            pygame.display.flip()

    pygame.quit()