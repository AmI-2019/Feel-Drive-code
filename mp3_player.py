import os
import random
import sys
import pygame
from pygame.locals import *

# inizializzazione
import speech2text

pygame.init()
screen = pygame.display.set_mode((800, 600))
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
listofsongs=[]
directory = 'C:/Users/Pietro/Desktop/Feel & Drive/music'
os.chdir(directory)
for file in os.listdir(directory):
    listofsongs.append(file)
index = random.randint(0,len(listofsongs)-1)

SONG_END=pygame.USEREVENT +1

def playsong_voice():
    pygame.mixer.music.unpause()

def stopsong_voice():
    pygame.mixer.music.pause()

def changesong_voice():
    global index
    index = random.randint(0, len(listofsongs) - 1)
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()

def nextsong():
    global index
    index = (index +1)%(len(listofsongs))
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()



# ciclo principale
pygame.mixer.music.set_endevent(SONG_END)
pygame.mixer.music.load(listofsongs[index])
pygame.mixer.music.play()
done = False
while not done:
    for ev in pygame.event.get():
        if ev.type == QUIT:
            done = True
        elif ev.type == KEYDOWN:             # e' stato premuto un tasto
            command = speech2text.recognize()
            if command == "exit":
                done = True
            elif command == "stop":
                stopsong_voice()
            elif command == "change":
                changesong_voice()
            elif command == "play":
                playsong_voice()
            else:
                print("Vocal Command not recognized")
        elif ev.type == SONG_END:
            nextsong()
# fine del ciclo e termine del programma
pygame.quit()