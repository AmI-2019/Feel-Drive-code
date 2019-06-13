import snowboydecoder
import sys
import signal

PATH = '/home/pi/'
NEXT = PATH + 'Feel-Drive-code/Pi-Code/vocal_command/Next.pmdl'
PLAY = PATH + 'Feel-Drive-code/Pi-Code/vocal_command/Play.pmdl'
STOP = PATH + 'Feel-Drive-code/Pi-Code/vocal_command/Stop.pmdl'



class VocalCommand:
    def __init__(self):
        self.interrupted = False
        self.detected = False
        self.command = ''
        self.models = [STOP, PLAY, NEXT]

        signal.signal(signal.SIGINT, self.signal_handler)
        self.sensitivity = [0.5] * len(self.models)

    def signal_handler(self, signal, frame):
        global interrupted
        self.interrupted = True

    def interrupt_callback(self):
        if self.interrupted:
                print("interrupted")
        return self.detected or self.interrupted

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

    def recognize(self):
        self.command = ''
        self.detected = False
        detector = snowboydecoder.HotwordDetector(self.models, sensitivity=self.sensitivity)
        print('Listening... Press Ctrl+C to exit')

        detector.start(detected_callback=[self.on_stop, self.on_play, self.on_next],
               interrupt_check=self.interrupt_callback,
               sleep_time=0.03)
        detector.terminate()
        
        
        return self.command

