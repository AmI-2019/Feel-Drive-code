import os
import random
import pygame
import interaction
from pygame.locals import *
import pygame.freetype
import speech2text
import config
from config import SONG_DIRECTORY

SONG_END = pygame.USEREVENT + 1
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
RED = (255, 0, 0)
BLACK = (0, 0, 0)


class MusicPlayer:
    # class shared variables
    __instance = None
    song_played = None

    def __init__(self):
        # Singleton pattern: only one Music Player should be created
        if MusicPlayer.__instance is not None:
            raise Exception("The Music player has already been created!")
        else:
            self.__instance = self

        pygame.init()
        pygame.font.init()
        self.song_list = interaction.get_songs('Happiness')
        os.chdir(SONG_DIRECTORY)
        pygame.mixer.music.set_endevent(SONG_END)
        pygame.mixer.music.set_volume(1.0)
        self.next()

    def __del__(self):
        pygame.quit()

    def resume(self):
        pygame.mixer.music.unpause()

    def pause(self):
        pygame.mixer.music.pause()

    def next(self):
        index = random.randint(0, len(self.song_list) - 1)
        self.song_played=self.song_list[index]
        pygame.mixer.music.load(self.song_list[index])
        pygame.mixer.music.play()
        self.get_gui(self.song_list[index])

    def get_gui(self, song):
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
        command = command_label.render('Press a key to enable your assistant!', True, BLACK)
        commandRect = command.get_rect()
        commandRect.center = (600 // 2, 400)

        liked_label = pygame.font.Font('freesansbold.ttf', 50)
        if interaction.is_song_liked(self.song_played) == False:
            liked=liked_label.render('+', True, RED)
        else:
            liked = liked_label.render('_/', True, GREEN)
        likedRect = liked.get_rect()
        likedRect.center=(600 // 2, 500)

        display_surface.fill(WHITE)
        display_surface.blit(motto, mottoRect)

        display_surface.blit(liked, likedRect)

        songRect = song.get_rect()
        songRect.center = (600 // 2, 600 // 2)
        display_surface.blit(song, songRect)

        commandRect = command.get_rect()
        commandRect.center = (600 // 2, 400)
        display_surface.blit(command, commandRect)

        return display_surface

    def handle_event(self):
        done = False
        for ev in pygame.event.get():
            if ev.type == QUIT:
                done = True
            elif ev.type == KEYDOWN:
                pygame.mixer.music.set_volume(0.1)
                vocal_command = speech2text.recognize()
                if vocal_command == "exit":
                    done = True
                elif vocal_command == "stop":
                    self.pause()
                elif vocal_command == "change":
                    self.next()
                elif vocal_command == "play":
                    self.resume()
                elif vocal_command == "add":
                    interaction.add_relation()
                else:
                    print("Vocal Command not recognized")
            elif ev.type == SONG_END:
                self.next()

            pygame.mixer.music.set_volume(1.0)
            pygame.display.flip()
        return done


# usage example
if __name__ == '__main__':
    player = MusicPlayer()
    quit_player = False
    while not quit_player:
        quit_player = player.handle_event()
    del player
