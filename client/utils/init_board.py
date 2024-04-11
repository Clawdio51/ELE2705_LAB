import Adafruit_BBIO.GPIO as GPIO

def initialize_board(config):
    """
    Initialize input and output pins on the microcontroller.
    """

    # Acceleration
    activate = config["acceleration"]["activate"]
    GPIO.setup(activate, GPIO.IN, GPIO.PUD_DOWN)

    # Distance
    activate = config["distance"]["activate"]
    echo = config["distance"]["echo"]
    trigger = config["distance"]["trigger"]
    GPIO.setup(activate, GPIO.IN, GPIO.PUD_DOWN)
    GPIO.setup(echo, GPIO.IN, GPIO.PUD_DOWN)
    GPIO.setup(trigger, GPIO.OUT)
    GPIO.output(trigger, GPIO.LOW)

    # Echo reply LED
    echo_reply_led = config["echo_reply_led"]
    GPIO.setup(echo_reply_led, GPIO.OUT)
    GPIO.output(echo_reply_led, GPIO.LOW)