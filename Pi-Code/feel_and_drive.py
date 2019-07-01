import config
import music_player
import interaction
from gpio import Button, BrightnessSensor
from huecontroller import HueController
from lights import HueLights
from perfume import Perfume
from vocal_command.vocal_command import VocalCommand
import time
import tts


ANGER = 'angry'
HAPPINESS = 'happy'
SADNESS = 'sad'
EMOTION_LABELS = (ANGER, HAPPINESS, SADNESS)


class FeelAndDrive:
    def __init__(self):
        self.username = interaction.authenticate()
        self.feeling = ""

        tts.initalization()
        interaction.init_emotion_server()  # remember to set camera's IP address
        time.sleep(10)

        self.player = music_player.MusicPlayer()
        self.party_mode = False
        self.favourites_mode = False
        self.voice_recognizer = VocalCommand()

        self.button = Button()
        self.button.set_callback_function(self.get_vocal_command)

        self.bright_sensor = BrightnessSensor()
        self.lights = HueLights(config.HUE_BASE_URL, config.HUE_USERNAME)
        self.lights_on = True
        self.hue_controller = HueController()
        self.perfume = Perfume()

        self.quit_player = False

    def get_vocal_command(self, channel=None):
        self.player.set_volume(vol=0.1)
        tts.start_speak()
        vocal_command = self.voice_recognizer.recognize()
        if vocal_command == "exit":
            done = True
            return done
        elif vocal_command == "stop":
            self.player.pause()
        elif vocal_command == "next":
            self.player.next()
        elif vocal_command == "play":
            self.player.resume()
        elif vocal_command == "add":
            self.player.add_song_to_favourites()
        elif vocal_command == 'remove':
            self.player.remove_song_from_favourites()
            # To prevent discrepancy between local and player flag
            self.favourites_mode = self.player.favourites
        elif vocal_command == 'party':
            self.party_mode = not self.party_mode
            self.player.set_party_mode(party=self.party_mode)
            if self.party_mode:
                self.player.set_feeling(music_player.PARTY)
        elif vocal_command == 'my songs':
            self.favourites_mode = not self.favourites_mode
            self.player.set_favourites_mode(self.favourites_mode)
            # switching to favourites mode when no liked song are available
            # requires to reset the favourites_mode flag
            self.favourites_mode = self.player.favourites
        elif vocal_command == 'lights':
            self.lights_on = not self.lights_on
            if not self.lights_on:
                self.lights.off()
        elif vocal_command == 'perfume':
            self.perfume.spray(force=True)
        else:
            tts.exception_audio()
        self.player.set_volume(1)
        done = False
        return done

    def run(self):
        quit_player, voice = self.player.handle_event()
        if quit_player:
            return quit_player
        if voice:
            if self.get_vocal_command():
                return True

        feeling_prediction = interaction.get_emotion_prediction()
        if type(feeling_prediction) is dict:
            if not self.player.party_on:
                feeling = interaction.get_dominant_emotion(feeling_prediction)
                if self.lights_on:
                    hue, bri, sat = self.hue_controller.compute_hue(feeling_prediction,
                                                                    self.bright_sensor.get_brightness_smooth())
                    hue = interaction.emotion_to_hue(feeling)
                    self.lights.set(int(round(hue)), int(round(bri)), int(round(sat)))
                self.player.set_feeling(feeling)

                self.perfume.spray(feeling)
            else:
                self.lights.set_party()
        self.player.refresh()
        return quit_player

    def close(self):
        del self.player
        interaction.close_emotion_server()
        self.lights.off()


if __name__ == '__main__':
    fd = FeelAndDrive()
    terminate = fd.run()
    while not terminate:
        terminate = fd.run()
    fd.close()
