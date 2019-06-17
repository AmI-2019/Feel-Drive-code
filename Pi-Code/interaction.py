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


def add_relation(song, feeling):
        global username
        response=requests.post(CENTRAL_API + '/add_relation',
                      json={'song': song, 'username': username, 'liked': 'True', 'feeling': feeling})

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
    if type(response) is dict:
        del response['surprise']
        del response['disgust']
        del response['fear']
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
    response=requests.post(CENTRAL_API+'/delete', json={"song":song, "username":username})
    print(response)


def get_dominant_emotion(predictions):
    return map_emotion_label(max(predictions, key=predictions.get))


def map_emotion_label(label):
    if label == 'angry':
        return 'Relax'
    elif label == 'sad':
        return 'Motivational'
    elif label == 'happy':
        return 'Happiness'
    else:
        return label


def get_color():
    global username
    response=requests.get(CENTRAL_API+'/color', json = {'username':username}).json()
    return response

if __name__ == '__main__':
    authenticate()
    print(get_color())
