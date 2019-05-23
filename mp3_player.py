import os
import random
import sys
import pygame
from pygame.locals import *
import pygame.freetype

# initialization
import speech2text
listOfSongs = []

directory = 'C:/Users/Pietro/Desktop/Feel & Drive/music'
os.chdir(directory)
for file in os.listdir(directory):
    listOfSongs.append(file)
index = random.randint(0, len(listOfSongs) - 1)
index = random.randint(0, len(listOfSongs) - 1)
SONG_END = pygame.USEREVENT +1

#pygame
pygame.init()
screen = pygame.display.set_mode((600,600))
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

pygame.font.init()
display_surface = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Feel & Drive: music player')
motto_label = pygame.font.Font('freesansbold.ttf', 25)
motto = motto_label.render( "WELCOME to you Feel & Drive experience", True, GREEN, BLUE)
mottoRect = motto.get_rect()
mottoRect.center = (600 // 2, 600 // 6)

song_label = pygame.font.Font('freesansbold.ttf', 19)
song = song_label.render(listOfSongs[index], True, BLUE, WHITE)
songRect = song.get_rect()
songRect.center = (600 // 2, 600 // 2)


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
    song = song_label.render(listOfSongs[index], True, BLUE, WHITE)
    songRect = song.get_rect()
    songRect.center = (600 // 2, 600 // 2)
    return (display_surface, song)

def nextsong():
    global index
    index = (index +1)%(len(listOfSongs))
    pygame.mixer.music.load(listOfSongs[index])
    pygame.mixer.music.play()



# ciclo principale
pygame.mixer.music.set_endevent(SONG_END)
pygame.mixer.music.load(listOfSongs[index])
pygame.mixer.music.play()
done = False
while not done:
    display_surface.fill(WHITE)
    display_surface.blit(motto, mottoRect)
    display_surface.blit(song, song.get_rect())
    for ev in pygame.event.get():
        if ev.type == QUIT:
            done = True
        elif ev.type == KEYDOWN:
            command = speech2text.recognize()
            if command == "exit":
                done = True
            elif command == "stop":
                stopsong_voice()
            elif command == "change":
                (display_surface,song)=changesong_voice()
            elif command == "play":
                playsong_voice()
            else:
                print("Vocal Command not recognized")
        elif ev.type == SONG_END:
            nextsong()
        pygame.display.flip()

pygame.quit()