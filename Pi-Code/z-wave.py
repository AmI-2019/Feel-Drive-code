import requests
import time


base_url = 'http://192.168.0.36:8083'


username = 'admin'
password = 'AmI2019'

device_url = base_url + '/ZWaveAPI/Run/devices[{}].instances[{}].commandClasses[{}]'

switch_binary = '37'


def get_all_devices():
    all_devices = requests.get(base_url + '/ZWaveAPI/Data/0', auth=(username, password)).json()
    all_devices = all_devices['devices']
    all_devices.pop('1')

    return all_devices


def set_value(device, instance, value):
    url_to_call = (device_url + '.Set(' + str(value) + ')').format(device, instance, switch_binary)
    requests.get(url_to_call, auth=(username, password))


def turn_on():
    all_devices = get_all_devices()
    for device_key in all_devices:
        for instance in all_devices[device_key]['instances']:
            if switch_binary in all_devices[device_key]['instances'][instance]['commandClasses']:
                print('Turning on device %s...' % device_key)
                set_value(device_key, instance, 255)


def turn_off():
    all_devices = get_all_devices()

    for device_key in all_devices:
        for instance in all_devices[device_key]['instances']:
            if switch_binary in all_devices[device_key]['instances'][instance]['commandClasses']:
                print('Turning off device %s...' % device_key)
                set_value(device_key, instance, 0)


def perfume():
    turn_on()
    time.sleep(2)
    turn_off()


if __name__ == '__main__':
    perfume()
