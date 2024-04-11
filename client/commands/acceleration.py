import busio
import adafruit_adxl34x

from utils.status_codes import STATUS_CODE

def acceleration(config):

    scl = config["acceleration"]["SCL"]
    sda = config["acceleration"]["SDA"]

    i2c = busio.I2C(scl, sda)
    accelerometer = adafruit_adxl34x.ADXL343(i2c)
    acceleration = accelerometer.acceleration

    data = "acceleration=" + str(acceleration)
    print(data)

    return {"status": STATUS_CODE.OK, "data": data}