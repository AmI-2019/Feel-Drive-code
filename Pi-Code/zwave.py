import requests
import time
from config import Z_BASE_URL, Z_USERNAME, Z_PASSWORD, DEVICE_URL, SWITCH_BINARY


def get_all_devices():
    all_devices = requests.get(Z_BASE_URL + '/ZWaveAPI/Data/0', auth=(Z_USERNAME, Z_PASSWORD)).json()
    all_devices = all_devices['devices']
    all_devices.pop('1')

    return all_devices


def set_value(device, instance, value):
    url_to_call = (DEVICE_URL + '.Set(' + str(value) + ')').format(device, instance, SWITCH_BINARY)
    requests.get(url_to_call, auth=(Z_USERNAME, Z_PASSWORD))


def turn_on():
    all_devices = get_all_devices()
    for device_key in all_devices:
        for instance in all_devices[device_key]['instances']:
            if SWITCH_BINARY in all_devices[device_key]['instances'][instance]['commandClasses']:
                print('Turning on device %s...' % device_key)
                set_value(device_key, instance, 255)


def turn_off():
    all_devices = get_all_devices()

    for device_key in all_devices:
        for instance in all_devices[device_key]['instances']:
            if SWITCH_BINARY in all_devices[device_key]['instances'][instance]['commandClasses']:
                print('Turning off device %s...' % device_key)
                set_value(device_key, instance, 0)


def perfume():
    turn_on()
    time.sleep(2)
    turn_off()


if __name__ == '__main__':
    perfume()
