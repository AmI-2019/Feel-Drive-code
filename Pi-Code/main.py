import zwave
import config
import music_player
import speech2text
import interaction
from gpio import Button, BrightnessSensor
from huecontroller import HueController
from lights import HueLights
import time
import tts


ANGER = 'angry'
HAPPINESS = 'happy'
SADNESS = 'sad'
EMOTION_LABELS = (ANGER, HAPPINESS, SADNESS)

SPRAY_WINDOW = 60*9
PERFUME = True


if __name__ == '__main__':
    username = interaction.authenticate()

    tts.initalization()
    interaction.init_emotion_server()  #remember to set camera's IP address
    time.sleep(10)

    player = music_player.MusicPlayer()

    button = Button()
    button.set_callback_function(player.vocal_command)

    bright_sensor = BrightnessSensor()
    lights = HueLights(config.HUE_BASE_URL, config.HUE_USERNAME)
    hue_controller = HueController()

    last_spray = time.time()- SPRAY_WINDOW
    quit_player = False
    while not quit_player:
        quit_player = player.handle_event()

        feeling_prediction = interaction.get_emotion_prediction()
        if type(feeling_prediction) is dict:
            hue, bri = hue_controller.compute_hue(feeling_prediction, bright_sensor.get_brightness_smooth())

            #brightness = bright_sensor.get_brightness()*100
            lights.set(int(round(hue)), bri)

            feeling = interaction.get_dominant_emotion(feeling_prediction)

            player.set_feeling(feeling)

            if PERFUME and (feeling is SADNESS or feeling is ANGER):
                if time.time()- last_spray > SPRAY_WINDOW:
                    last_spray = time.time()
                    zwave.perfume()

    del player

