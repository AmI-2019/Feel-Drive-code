import zwave
import config
import music_player
import speech2text
import interaction
from gpio import Button
import huecontroller
import lights
import time

global username

if __name__ == '__main__':

    username = interaction.authenticate()
    player = music_player.MusicPlayer()

    #interaction.init_emotion_server()  #remember to set camera's IP address
    #time.sleep(8)
    #feeling = interaction.get_emotion()

    button = Button()
    button.set_callback_function(player.vocal_command)

    quit_player = False
    while not quit_player:
        quit_player = player.handle_event()
    del player

