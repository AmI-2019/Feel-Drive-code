import os
import sys
import random
import interaction
import pygame
from pygame.locals import *
import pygame.freetype

username = interaction.authenticate()


# initialization
import speech2text
listOfSongs = []

directory = 'C:/Users/Pietro/Desktop/Feel & Drive/music/Anger'
os.chdir(directory)
for file in os.listdir(directory):
    if file.endswith('.mp3'):
        listOfSongs.append(file)
index = random.randint(0, len(listOfSongs) - 1)
SONG_END = pygame.USEREVENT +1

#pygame
pygame.init()
screen = pygame.display.set_mode((600,600))
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
RED= (255,0,0)
BLACK=(0,0,0)

pygame.font.init()
display_surface = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Feel & Drive: music player')
motto_label = pygame.font.Font('freesansbold.ttf', 25)
motto = motto_label.render( "WELCOME to you Feel & Drive experience", True, BLUE, RED)
mottoRect = motto.get_rect()
mottoRect.center = (600 // 2, 600 // 6)

song_label=pygame.font.Font('freesansbold.ttf', 19)
song=song_label.render(listOfSongs[index][:-4],True, BLACK,WHITE)
songRect = song.get_rect()
songRect.center = (600 // 2, 600 // 2)

command_label=pygame.font.Font('freesansbold.ttf', 19)
command=command_label.render('Press a key to enable your assistant!', True, RED)
commandRect=command.get_rect()
commandRect.center = (600 // 2, 400)



#_________________________________________________________



def playsong_voice():
    pygame.mixer.music.unpause()

def stopsong_voice():
    pygame.mixer.music.pause()

def changesong_voice():
    global index
    index = random.randint(0, len(listOfSongs) - 1)
    pygame.mixer.music.load(listOfSongs[index])
    pygame.mixer.music.play()


    display_surface = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Feel & Drive: music player')



    song_label = pygame.font.Font('freesansbold.ttf', 19)
    song = song_label.render(listOfSongs[index][:-4], True, BLACK, WHITE)
    songRect=song.get_rect()
    songRect.center = (display_surface.get_width() // 2, display_surface.get_height() // 2)

    command_label = pygame.font.Font('freesansbold.ttf', 19)
    command = command_label.render('Press a key to enable your assistant!', True, RED)
    commandRect = command.get_rect()
    commandRect.center = (600 // 2, 400)

    return (display_surface, song, command)


def nextsong():
    global index
    index = (index +1)%(len(listOfSongs))
    pygame.mixer.music.load(listOfSongs[index])
    pygame.mixer.music.play()



# ciclo principale
pygame.mixer.music.set_endevent(SONG_END)
pygame.mixer.music.load(listOfSongs[index])
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play()
done = False
while not done:

    display_surface.fill(WHITE)
    display_surface.blit(motto, mottoRect)

    songRect = song.get_rect()
    songRect.center = (600 // 2, 600 // 2)
    display_surface.blit(song, songRect)

    commandRect = command.get_rect()
    commandRect.center =(600 // 2, 400)
    display_surface.blit(command,commandRect)

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
                (display_surface,song, command)=changesong_voice()
            elif vocal_command == "play":
                playsong_voice()
            else:
                print("Vocal Command not recognized")
        elif ev.type == SONG_END:
            nextsong()
        pygame.mixer.music.set_volume(1.0)
        pygame.display.flip()

pygame.quit()