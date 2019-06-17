import requests
import time
from config import HUE_USERNAME, HUE_BASE_URL
HUE_ID = '6'
HUE_EMULATOR_ID = '1'
HUE_EMULATOR = False


class HueLights:
    def __init__(self, base_url, username):
        if HUE_EMULATOR:
            self.light = HUE_EMULATOR_ID
        else:
            self.light = '6'
        self.base_url = base_url
        self.username = username
        self.lights_url = self.base_url + '/api/' + self.username + '/lights/'
        self.all_the_lights = requests.get(self.lights_url).json()

    def set(self, hue, bri):
        if type(self.all_the_lights) is dict:
            url_to_call = self.lights_url + self.light + '/state'
            body = {'on': True, "hue": hue, 'bri': bri, 'sat':254, 'effect': 'none'}
            requests.put(url_to_call, json=body)

    # azzurro
    def set_sad(self):
        if type(self.all_the_lights) is dict:
            # iterate over the Hue lights, turn them on with the color loop effect
            #for light in self.all_the_lights:
                url_to_call = self.lights_url + self.light + '/state'
                body = {'on': True, "hue": 46920, "bri": 65, 'sat': 254, 'effect':'none'}
                requests.put(url_to_call, json=body)

    # arancione
    def set_happy(self):
        if type(self.all_the_lights) is dict:
            #for light in self.all_the_lights:
                url_to_call = self.lights_url + self.light + '/state'
                body = {'on': True, "hue": 8000, "bri": 70, 'sat':254, 'effect':'none'}
                requests.put(url_to_call, json=body)

    # rosso
    def set_angry(self):
        if type(self.all_the_lights) is dict:
            #for light in self.all_the_lights:
                url_to_call = self.lights_url + self.light + '/state'
                body = {'on': True, "hue": 0, "bri": 75, 'sat':254, 'effect':'none'}
                requests.put(url_to_call, json=body)

    # viola
    def set_purple(self):
        if type(self.all_the_lights) is dict:
            #for light in self.all_the_lights:
                url_to_call = self.lights_url + self.light + '/state'
                body = {'on': True, "hue": 56000, "bri": 95, 'sat':254, 'effect':'none'}
                requests.put(url_to_call, json=body)

    # verde
    def set_green(self):
        if type(self.all_the_lights) is dict:
            #for light in self.all_the_lights:
                url_to_call = self.lights_url + self.light + '/state'
                body = {'on': True, "hue": 22000, "bri": 50, 'sat':254, 'effect':'none'}
                requests.put(url_to_call, json=body)

    def set_party(self):
        if type(self.all_the_lights) is dict:
            #for light in self.all_the_lights:
                url_to_call = self.lights_url + self.light + '/state'
                body = {'on': True, 'effect': 'colorloop', 'sat':254}
                requests.put(url_to_call, json=body)



    def off(self):
        if type(self.all_the_lights) is dict:
            url_to_call = self.lights_url + self.light + '/state'
            body = {'on': False}
            requests.put(url_to_call, json=body)


#demo
if __name__ == '__main__':
    lights = HueLights(HUE_BASE_URL, HUE_USERNAME)

    lights.set_party()
    time.sleep(5)
    lights.set_sad()
    time.sleep(10)
    lights.set_happy()
    time.sleep(2)
    lights.set_green()
    time.sleep(2)
    lights.set_angry()
    time.sleep(2)
    lights.set_purple()
    time.sleep(2)
    lights.off()



