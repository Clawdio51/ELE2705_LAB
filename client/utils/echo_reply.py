import Adafruit_BBIO.GPIO as GPIO
import time

def echo_reply(response, config):
    
    print(response.decode())

    echo_reply_led = config["echo_reply_led"]
    GPIO.output(echo_reply_led, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(echo_reply_led, GPIO.LOW)
