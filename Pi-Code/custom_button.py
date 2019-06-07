import RPi.GPIO as GPIO  # Import Raspberry Pi GPIO library


# TODO: Simo check your circuit and modify effective pin of the demo!
# demo to check effective working of the button
def button_callback():
    print("button pressed!")


# change number of pin with the one effectively used; in this way the logic should not be inverted
# Vhigh = button pressed

GPIO.setwarnings(False)  # Ignore warning for now
GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Set pin 10 to be an input pin and set initial value to be pulled low (off)

GPIO.add_event_detect(10, GPIO.RISING, callback=button_callback)