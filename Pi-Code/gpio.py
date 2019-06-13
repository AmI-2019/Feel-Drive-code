import RPi.GPIO as GPIO  # Import Raspberry Pi GPIO library
from gpiozero import LightSensor
import queue
import statistics
BUTTON_PIN = 18
BOUNCETIME = 750
LDR_PIN = 10

MEAN_SAMPLES = 10
DEBUG = False


# PULL_DOWN = 10000
# PULL_UP = 220
# V = 3.3
# Iin = 0.3  # mV
# Vh = 3.23


def debug_button_callback(channel):
    print("button pressed!")


class Button:
    def __init__(self, pin=BUTTON_PIN):
        self.pin = pin
        GPIO.setwarnings(False)  # Ignore warning
        GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
        GPIO.setup(self.pin, GPIO.IN)
        # Physical pull-down resistor is used otherwise use
        # GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def set_callback_function(self, callback_action=debug_button_callback):
        GPIO.add_event_detect(self.pin, GPIO.RISING, callback=callback_action, bouncetime=BOUNCETIME)

    def __del__(self):
        GPIO.cleanup()


class BrightnessSensor:
    def __init__(self, pin=LDR_PIN):
        self.light = LightSensor(pin, charge_time_limit=0.03)
        self.values = queue.Queue(maxsize=MEAN_SAMPLES)

    def get_brightness(self):
        if DEBUG:
            print(self.light.value)
        return self.light.value

    def get_brightness_smooth(self):
        val = self.get_brightness()
        if self.values.full():
            self.values.get()
            self.values.put(val)
            avg = statistics.mean(list(self.values.queue))
            print("mean: ")
            print(avg)
            return avg
        else:
            self.values.put(val)
            return val


# demo
if __name__ == '__main__':
    button = Button()
    ls = BrightnessSensor()
    button.set_callback_function()
    while True:
        print(ls.get_brightness())
