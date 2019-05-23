import speech_recognition as sr
#import keyboard
import pyttsx3
import tkinter
engine = pyttsx3.init()
r = sr.Recognizer()
mic = sr.Microphone()


def recognize():
    with mic as source:
        #tkinter.Tk.bell()
        r.adjust_for_ambient_noise(source, 0.5)
        audio = r.listen(source, phrase_time_limit=1)
        # print(r.recognize_houndify(audio, "4ld9WM_kTXLshYS-GOKr7g==", "5b55t3QsJeptvgRe6f2U3mhjx9DGMkliWpaG24QVlbEziEAKDKdBlfPcuz037fk9e2UmaDK3-NaNKm7c3ZA6pw=="))
        try:
            response = r.recognize_google(audio)
        except sr.UnknownValueError:
            response = "exception"
            engine.say("NO CABIDO CABO")
            engine.runAndWait()
        return response


def stopSong():
    print("stop")


def changeSong():
    print("change")


def askSong():
    engine.say("Do you like this song?")
    engine.runAndWait()
    print("done")
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