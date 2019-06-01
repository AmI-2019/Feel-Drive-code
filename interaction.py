import requests

global username
api_uri='http://192.168.1.195:5000/api/v1'

def authenticate():
    global username
    global api_uri
    done=False
    while done == False:
        username=input("Insert username\n")
        password=input("Insert password\n")
        response=requests.get(api_uri+'/login', json={'username': username, 'password':password})
        r=response.json()
        if r == '200':
            done = True
    return username


def add_relation(song, comment, feeling):
        global api_uri
        global username
        if comment == "yes":
            requests.post(api_uri+'/relate',
                          json={'song' : song, 'username': username, 'liked' : 'True','feeling' :feeling})
        else:
            requests.post('http://192.168.0.6:5000/api/v1/relate',
                          json={'song': song, 'username': username, 'liked': 'True'})


def get_songs(feeling):
    global api_uri
    response=requests.get(api_uri+'/songs', json={'feeling':feeling})
    r=response.json()
    return r


if __name__ == '__main__':
    print(get_songs('Happiness'))