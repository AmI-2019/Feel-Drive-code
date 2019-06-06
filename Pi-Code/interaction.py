from time import sleep

import requests
from config import FER_SERVER, CENTRAL_API


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
            requests.post(CENTRAL_API + '/relate',
                          json={'song': song, 'username': username, 'liked': 'True', 'feeling': feeling})
        else:
            requests.post('http://192.168.0.6:5000/api/v1/relate',
                          json={'song': song, 'username': username, 'liked': 'True'})


def get_songs(feeling):
    songs = []
    response = requests.get(CENTRAL_API + '/songs', json={'feeling': feeling}).json()
    for r in response:
        r1 = str(r)
        song = r1[2:len(r)-3]
        songs.append(song)
    return songs


def init_emotion_server():
    requests.post(FER_SERVER + '/start', json={'address': 'insert_here_your_camera_address'})


def get_emotion():
    response = requests.get(FER_SERVER + '/predictions').json()
    return response


if __name__ == '__main__':
    print(get_songs('Happiness'))
