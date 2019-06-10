from gtts import gTTS
import os


# custom functions
def exception_audio():
    os.system("mpg321 exception.mp3")


def song_added():
    os.system("mpg321 add.mp3")


def song_removed():
    os.system("mpg321 remove.mp3")


def start_speak():
    os.system("mpg321 start_speak.mp3")


def demo():
    exception_audio()
    song_added()
    song_removed()
    start_speak()


# initialization
if __name__ == '__main__':
    tts = gTTS(text="I don't understand!", lang='en', )
    tts.save("exception.mp3")
    tts = gTTS(text="song added from favourites", lang='en', )
    tts.save("add.mp3")
    tts = gTTS(text="song removed from favourites", lang='en', )
    tts.save("remove.mp3")
    tts = gTTS(text="Feel & Drive, listening", lang='en', )
    tts.save("start_speak.mp3")
    demo()
