import requests

def authenticate():

    done=False
    while done == False:
        username=input("Insert username\n")
        password=input("Insert password\n")
        response=requests.get('http://192.168.0.6:5000/api/v1/login', json={'username': username, 'password':password})
        r=response.json()
        
        if r == '200':
            done = True
    return username

