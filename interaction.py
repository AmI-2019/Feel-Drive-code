from time import sleep

import requests

global username
central_api='http://192.168.1.195:5000/api/v1'
emotion_api = 'http://192.168.0.34:5000/fer-server'

def authenticate():
    global username
    global central_api
    done=False
    while done == False:
        username=input("Insert username\n")
        password=input("Insert password\n")
        response=requests.get(central_api+'/login', json={'username': username, 'password':password})
        r=response.json()
        if r == '200':
            done = True
    return username


def add_relation(song, comment, feeling):
        global api_uri
        global username
        if comment == "yes":
            requests.post(central_api+'/relate',
                          json={'song' : song, 'username': username, 'liked' : 'True','feeling' :feeling})
        else:
            requests.post('http://192.168.0.6:5000/api/v1/relate',
                          json={'song': song, 'username': username, 'liked': 'True'})


def get_songs(feeling):
    global api_uri
    songs = []
    response=requests.get(central_api+'/songs', json={'feeling':feeling}).json()
    for r in response:
        song=r[2:len(r)-2]
        songs.append(song)
    return songs


def init_emotion_server():
    global emotion_api
    requests.post(emotion_api+'/start', json={'address' : 'insert_here_your_camera_address'})


def get_emotion():
    global emotion_api
    response=requests.get(emotion_api+'/predictions').json()
    return response


if __name__ == '__main__':
    print(get_songs('Happiness'))
