from time import sleep
import requests
from config import FER_SERVER, CENTRAL_API, PI_BASE_URL


def authenticate():
    global username
    done = False
    while not done:
        username = input("Insert username\n")
        password = input("Insert password\n")
        response = requests.get(CENTRAL_API + '/login', json={'username': username, 'password':password})
        r = response.json()
        if r == '200':
            done = True
    return username


def add_relation(song, comment, feeling):
        global username
        if comment == "yes":
            response=requests.post(CENTRAL_API + '/add_relation',
                          json={'song': song, 'username': username, 'liked': 'True', 'feeling': feeling})
        else:
            requests.post(CENTRAL_API+'/add_relation',
                          json={'song': song, 'username': username, 'liked': 'False', 'feeling' : feeling})

        print(response)


def get_songs(feeling):
    songs = []
    response = requests.get(CENTRAL_API + '/songs', json={'feeling': feeling}).json()
    for r in response:
        r1 = str(r)
        song = r1[2:len(r)-3]
        songs.append(song)
    return songs


def get_liked_songs(feeling):
    global username
    songs = []
    response = requests.get(CENTRAL_API + '/liked_songs', json={'feeling': feeling, "username" : username}).json()
    for r in response:
        r1 = str(r)
        song = r1[2:len(r)-3]
        songs.append(song)
    return songs


def init_emotion_server(camera_address=PI_BASE_URL):
    requests.post(FER_SERVER + '/start', json={'address': camera_address+':8080/stream/video.mjpeg'})

def close_emotion_server():
    requests.get(FER_SERVER+'/stop')

def get_emotion_prediction():
    response = requests.get(FER_SERVER + '/predictions').json()
    return response


def is_song_liked(song):
    global username
    response = requests.get(CENTRAL_API + '/is_song_liked', json={"song":song, "username": username}).json()
    if response is not None:
        return True
    else:
        return False


def delete_relation(song):
    global username
    requests.post(CENTRAL_API+'/delete', json={"song":song, "username":username})


def get_dominant_emotion(predictions):
    return ''


if __name__ == '__main__':
    add_relation('Dancing Queen - Abba.mp3','yes','Happiness')
