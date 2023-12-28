from utils.status_codes import STATUS_CODE
import Adafruit_BBIO.GPIO as GPIO
import time

def distance(config):

    echo = config["distance"]["echo"]
    trigger = config["distance"]["trigger"]

    
    GPIO.output(trigger, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trigger, GPIO.LOW)

    while GPIO.input(echo) == 0:
        start = time.time()
    while GPIO.input(echo) == 1:
        end = time.time()

    duration = end - start
    distance = round(duration * 17150, 2)

    data = "distance=" + str(distance) + "cm"
    
    return {"status": STATUS_CODE.OK, "data": data}