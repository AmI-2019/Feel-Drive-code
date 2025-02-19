import os
import random
import pygame
import interaction
from pygame.locals import *
import pygame.freetype
from config import SONG_DIRECTORY


SONG_END = pygame.USEREVENT + 1
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

ANGER = 'Relax'
HAPPINESS = 'Happiness'
SADNESS = 'Motivational'
PARTY = 'Party'
EMOTION_LABELS = (ANGER, HAPPINESS, SADNESS, PARTY)


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

        self.feeling = HAPPINESS
        self.party_on = False
        pygame.init()
        pygame.font.init()
        self.song_list = {}
        self.favourites = False
        self.load_song_list()
        print(self.song_list)
        os.chdir(SONG_DIRECTORY)
        pygame.mixer.music.set_endevent(SONG_END)
        pygame.mixer.music.set_volume(1.0)
        self.next()

    def load_song_list(self, favourites=False):
        for emotion in EMOTION_LABELS:
            if favourites:
                self.song_list[emotion] = interaction.get_liked_songs(emotion)
            else:
                self.song_list[emotion] = interaction.get_songs(emotion)

    def __del__(self):
        pygame.quit()

    def close(self):
        pygame.quit()

    def resume(self):
        pygame.mixer.music.unpause()

    def pause(self):
        pygame.mixer.music.pause()

    def next(self):
        # if there are no liked songs, then switch back to play all songs!
        if len(self.song_list[self.feeling]) == 0:
            print("Yuo do not have any liked song associated with the current emotion!")
            print("Switching back to play our songs")
            self.favourites = False
            self.load_song_list(favourites=False)
        index = random.randint(0, len(self.song_list[self.feeling]) - 1)
        self.song_played = self.song_list[self.feeling][index]
        pygame.mixer.music.load(self.feeling+'/'+self.song_list[self.feeling][index])
        pygame.mixer.music.play()
        self.get_gui(self.song_list[self.feeling][index])

    def set_feeling(self, feeling):
        if feeling not in EMOTION_LABELS:
            print("Error: emotion not supported")
            return ''
        old_feeling = self.feeling
        self.feeling = feeling
        if self.feeling is not old_feeling:
            self.next()
        return old_feeling

    def set_party_mode(self, party=True):
        self.party_on = party

    def add_song_to_favourites(self):
        interaction.add_relation(self.song_played, self.feeling)
        # if playing in favourite mode, the song must be added to the playlist
        if self.favourites:
            self.song_list[self.feeling] = interaction.get_liked_songs(self.feeling)
        self.get_gui(self.song_played)

    def remove_song_from_favourites(self):
        interaction.delete_relation(self.song_played)
        # if playing in favourite mode, the song must be removed from the playlist
        # and another song must be played
        if self.favourites:
            self.song_list[self.feeling] = interaction.get_liked_songs(self.feeling)
            self.next()
        self.get_gui(self.song_played)

    def set_favourites_mode(self, favourites_only=False):
        if favourites_only:
            self.load_song_list(favourites=True)
            self.favourites = True
            self.next()
        else:
            self.load_song_list()
            self.favourites = False
            self.next()

    def set_volume(self, vol):
        pygame.mixer.music.set_volume(vol)

    def refresh(self):
        pygame.display.flip()

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
        if not interaction.is_song_liked(self.song_played):
            liked = liked_label.render('+', True, RED)
        else:
            liked = liked_label.render('_/', True, GREEN)
        likedRect = liked.get_rect()
        likedRect.center = (600 // 2, 500)

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
        get_vocal_command = False
        for ev in pygame.event.get():
            if ev.type == QUIT:
                done = True
            elif ev.type == KEYDOWN:
                get_vocal_command = True
            elif ev.type == SONG_END:
                self.next()
            pygame.mixer.music.set_volume(1.0)
        return done, get_vocal_command


# usage example
if __name__ == '__main__':
    username = interaction.authenticate()
    player = MusicPlayer()
    quit_player = False
    while not quit_player:
        quit_player = player.handle_event()
    del player
