import speech_recognition as sr
import tts
import time
r = sr.Recognizer()
mic = sr.Microphone()


def recognize():
    with mic as source:
        r.adjust_for_ambient_noise(source, 1)
        #time.sleep(1)
        # tkinter.Tk.bell()
        #tts.start_speak()
        audio = r.listen(source, phrase_time_limit=1)
        # print(r.recognize_houndify(audio, "4ld9WM_kTXLshYS-GOKr7g==", "5b55t3QsJeptvgRe6f2U3mhjx9DGMkliWpaG24QVlbEziEAKDKdBlfPcuz037fk9e2UmaDK3-NaNKm7c3ZA6pw=="))
        try:
            response = r.recognize_google(audio)
        except sr.UnknownValueError:
            response = "exception"
            tts.exception_audio()
        return response


def stopSong():
    print("stop")


def changeSong():
    print("change")


def askSong():
    response = recognize()
    print(response)


def playSong(string):
    print(string[5:])

'''
if __name__ == '__main__':
    askSong()
    command = recognize()
    if command == "exit":
        exit()
    elif command == "stop":
        stopSong()
    elif command == "change song":
        changeSong()
    elif command.startswith("play"):
        playSong(command)
'''