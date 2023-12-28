import Adafruit_BBIO.GPIO as GPIO


def _choose_command_from_button(config):
    
    print("Push a button to indicate command.")
    while True:
            if GPIO.input(config["distance"]["activate"]) == GPIO.HIGH:
                return "distance"
                


def choose_command(config):

    if config["use_button"] == True:
        return _choose_command_from_button(config)
    else:
        return input("Command: ").strip().lower()