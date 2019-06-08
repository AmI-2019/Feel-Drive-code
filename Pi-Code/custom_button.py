import RPi.GPIO as GPIO  # Import Raspberry Pi GPIO library
BUTTON_PIN = 18
BOUNCETIME = 750

# PULL_DOWN = 10000
# PULL_UP = 220
# V = 3.3
# Iin = 0.3  # mV
# Vh = 3.23


def button_callback(channel):
    print("button pressed!")


GPIO.setwarnings(False)  # Ignore warning
GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
GPIO.setup(BUTTON_PIN, GPIO.IN)
# Physical pull-down resistor is used otherwise use
# GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(BUTTON_PIN, GPIO.RISING, callback=button_callback, bouncetime=BOUNCETIME)

# demo
if __name__ == '__main__':
    while True:
        pass
    GPIO.cleanup()