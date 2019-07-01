import requests
import time
from config import Z_BASE_URL, Z_USERNAME, Z_PASSWORD, DEVICE_URL, SWITCH_BINARY


class Perfume:
    def __init__(self):
        self.spray_window = 60
        self.last_spray = time.time() - self.spray_window
        self.all_devices = self.get_all_devices()

    def get_all_devices(self):
        all_devices = requests.get(Z_BASE_URL + '/ZWaveAPI/Data/0', auth=(Z_USERNAME, Z_PASSWORD)).json()
        all_devices = all_devices['devices']
        all_devices.pop('1')

        return all_devices

    def set_value(self, device, instance, value):
        url_to_call = (DEVICE_URL + '.Set(' + str(value) + ')').format(device, instance, SWITCH_BINARY)
        requests.get(url_to_call, auth=(Z_USERNAME, Z_PASSWORD))

    def turn_on(self):
        for device_key in self.all_devices:
            for instance in self.all_devices[device_key]['instances']:
                if SWITCH_BINARY in self.all_devices[device_key]['instances'][instance]['commandClasses']:
                    print('Turning on device %s...' % device_key)
                    self.set_value(device_key, instance, 255)

    def turn_off(self):
        for device_key in self.all_devices:
            for instance in self.all_devices[device_key]['instances']:
                if SWITCH_BINARY in self.all_devices[device_key]['instances'][instance]['commandClasses']:
                    print('Turning off device %s...' % device_key)
                    self.set_value(device_key, instance, 0)

    def spray(self, feeling='', force=False):
        if force or (feeling == 'Motivational' or feeling == 'Realx'):
            if time.time() - self.last_spray > self.spray_window:
                self.last_spray = time.time()
            self.turn_on()
            time.sleep(5)
            self.turn_off()


if __name__ == '__main__':
    perfume = Perfume()
    perfume.spray(force=True)
