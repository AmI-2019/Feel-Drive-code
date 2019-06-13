import snowboydecoder
import sys
import signal
import time

PATH = '/home/pi/repo/'
NEXT = PATH + 'Pi-Code/vocal_command/Next.pmdl'
PLAY = PATH + 'Pi-Code/vocal_command/Play.pmdl'
STOP = PATH + 'Pi-Code/vocal_command/Stop.pmdl'
ADD = PATH + 'Pi-Code/vocal_command/Add.pmdl'
REMOVE = PATH + 'Pi-Code/vocal_command/Remove.pmdl'
QUIT = PATH + 'Pi-Code/vocal_command/quit.pmdl'
TIMEOUT = 7


class VocalCommand:
    def __init__(self):
        self.detected = False
        self.command = ''
        self.models = [STOP, PLAY, NEXT, ADD, REMOVE, QUIT]
        self.sensitivity = [0.5] * len(self.models)

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

    def on_quit(self):
        self.detected = True
        print("quit")
        self.command = 'exit'

    def recognize(self):
        self.command = ''
        self.detected = False
        detector = snowboydecoder.HotwordDetector(self.models, sensitivity=self.sensitivity)
        print('Listening... ')
        self.start = time.time()
        detector.start(detected_callback=[self.on_stop, self.on_play, self.on_next,
                                          self.on_add, self.on_remove, self.on_quit],
               interrupt_check=self.interrupt_callback,
               sleep_time=0.03)
        detector.terminate()
        
        return self.command

