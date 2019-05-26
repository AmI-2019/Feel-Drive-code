import requests

def authenticate():

    done=False
    while done is False:
        username=input("Insert username\n")
        password=input("Insert password\n")
        payload=username+'/'+password
        response=requests.get('http://0.0.0.0', params=payload)
        print(response)


if __name__ == '__main__':
    authenticate()