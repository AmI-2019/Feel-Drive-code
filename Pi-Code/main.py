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

PARTY_MODE = False

SPRAY_WINDOW = 60*9
PERFUME = True


if __name__ == '__main__':
    username = interaction.authenticate()
    feeling = ""

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
            if not player.party_on:
                feeling = interaction.get_dominant_emotion(feeling_prediction)
                hue, bri, sat = hue_controller.compute_hue(feeling_prediction, bright_sensor.get_brightness_smooth())
                hue = interaction.emotion_to_hue(feeling)
                lights.set(int(round(hue)), int(round(bri)), int(round(sat)))


                player.set_feeling(feeling)

                if PERFUME and (feeling == SADNESS or feeling == ANGER):
                    if time.time() - last_spray > SPRAY_WINDOW:
                        last_spray = time.time()
                        zwave.perfume()
            else:
                lights.set_party()

    del player
    interaction.close_emotion_server()
    lights.off()

