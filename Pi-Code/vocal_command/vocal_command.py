import vocal_command.snowboydecoder
import sys
import signal
import time

PATH = '/home/pi/Feel-Drive-code/'
NEXT = PATH + 'Pi-Code/vocal_command/Next.pmdl'
PLAY = PATH + 'Pi-Code/vocal_command/Play.pmdl'
STOP = PATH + 'Pi-Code/vocal_command/Stop.pmdl'
ADD = PATH + 'Pi-Code/vocal_command/Add.pmdl'
REMOVE = PATH + 'Pi-Code/vocal_command/Remove.pmdl'
CLOSE = PATH + 'Pi-Code/vocal_command/Close.pmdl'
PARTY = PATH + 'Pi-Code/vocal_command/Party.pmdl'
SHUFFLE = PATH + 'Pi-Code/vocal_command/shuffle.pmdl'
MY_SONGS = PATH + 'Pi-Code/vocal_command/My_songs.pmdl'
LIGHTS = PATH + 'Pi-Code/vocal_command/Lights.pmdl'
PERFUME = PATH + 'Pi-Code/vocal_command/Perfume.pmdl'
TIMEOUT = 4
SENSITIVITY = 0.44


class VocalCommand:
    def __init__(self):
        self.detected = False
        self.command = ''
        self.models = [STOP, PLAY, NEXT, ADD, REMOVE, CLOSE, PARTY, MY_SONGS, LIGHTS, PERFUME]
        self.sensitivity = [SENSITIVITY] * len(self.models)

    def interrupt_callback(self):
        if time.time() - self.start > TIMEOUT:
            print("Timeout")
            return True
        return self.detected

    def on_stop(self):
        self.detected = True
        print("stop")
        self.command = 'stop'

    def on_play(self):
        self.detected = True
        print("play")
        self.command = 'play'

    def on_next(self):
        self.detected = True
        print("next")
        self.command = 'next'

    def on_add(self):
        self.detected = True
        print("add")
        self.command = 'add'

    def on_remove(self):
        self.detected = True
        print("remove")
        self.command = 'remove'

    def on_close(self):
        self.detected = True
        print("close")
        self.command = 'exit'

    def on_party(self):
        self.detected = True
        print("party")
        self.command = 'party'

    def on_shuffle(self):
        self.detected = True
        print("shuffle")
        self.command = 'shuffle'

    def on_my_songs(self):
        self.detected = True
        print("my songs")
        self.command = 'my songs'

    def on_lights(self):
        self.detected = True
        print("lights")
        self.command = 'lights'

    def on_perfume(self):
        self.detected = True
        print("perfume")
        self.command = 'perfume'

    def recognize(self):
        self.command = ''
        self.detected = False
        detector = vocal_command.snowboydecoder.HotwordDetector(self.models, sensitivity=self.sensitivity)
        print('Listening... ')
        self.start = time.time()
        detector.start(detected_callback=[self.on_stop, self.on_play, self.on_next,
                                          self.on_add, self.on_remove, self.on_close,
                                          self.on_party, self.on_my_songs, self.on_lights,
                                          self.on_perfume
                                          ],
               interrupt_check=self.interrupt_callback,
               sleep_time=0.03)
        detector.terminate()
        
        return self.command

