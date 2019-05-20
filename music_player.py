import os
import random
import sys
import pygame
from tkinter import *

SONG_END=pygame.USEREVENT +1

root = Tk()
root.wm_title('FEEL & DRIVE: Music player')
root.geometry('500x500')

listofsongs = []
v = StringVar()
songlabel = Label(root,textvariable=v,width=1000)
mottolabel=Label(root, text="Follow your heart-beat", fg="green", width=1000)


def changesong(event):
    global index
    index = random.randint(0,len(listofsongs)-1)
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()


def stopsong(event):
    pygame.mixer.music.pause()


def playsong(event):
    pygame.mixer.music.unpause()


def updatelabel():
    v.set(listofsongs[index])

def nextsong():
    global index
    index = (index +1)%(len(listofsongs))
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()


label = Label(root, text='FEEL & DRIVE: Music Player')
label.pack()


changebutton = Button(root, text='CHANGE')
changebutton.pack()

stopbutton = Button(root, text='STOP')
stopbutton.pack()

playbutton = Button(root, text='PLAY')
playbutton.pack()

quitbutton = Button(root, )

changebutton.bind("<Button-1>", changesong)
stopbutton.bind("<Button-1>", stopsong)
playbutton.bind("<Button-1>", playsong)


songlabel.pack()

mottolabel.pack()


directory = 'C:/Users/Pietro/Desktop/Feel & Drive/music'
os.chdir(directory)
for file in os.listdir(directory):
    listofsongs.append(file)
index = random.randint(0,len(listofsongs)-1)
pygame.init()
pygame.mixer.music.set_endevent(SONG_END)
pygame.mixer.music.load(listofsongs[index])
pygame.mixer.music.play()
updatelabel()


LOOP_ACTIVE = True
while LOOP_ACTIVE:
    root.update()
    for event in pygame.event.get():
        if event.type == SONG_END:
            nextsong()
        if event.type == pygame.QUIT:
            sys.exit(0)
            root.quit()
            LOOP_ACTIVE=False