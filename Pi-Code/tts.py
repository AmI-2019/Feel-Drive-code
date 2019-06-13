from gtts import gTTS
import os


# custom functions
def exception_audio():
    os.system("mpg321 /home/pi/tts/exception.mp3")


def start_speak():
    os.system("mpg321 /home/pi/tts/start_speak.mp3")


def initalization():
    os.system('mpg321 /home/pi/tts/init.mp3')


def demo():
    exception_audio()
    start_speak()
    initalization()


# initialization
if __name__ == '__main__':
    tts = gTTS(text="I don't understand!", lang='en' )
    tts.save("/home/pi/tts/exception.mp3")
    tts = gTTS(text="listening", lang='en' )
    tts.save("/home/pi/tts/start_speak.mp3")
    tts = gTTS(text="Wait for initialization", lang='en')
    tts.save("/home/pi/tts/init.mp3")
    demo()
