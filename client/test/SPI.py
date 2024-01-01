import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.SPI as SPI
import time


if False:
    SPI_BUS = 0
    SPI_DEVICE = 0
    CS_PIN = "P9_15"

    # Set up SPI communication
    spi = SPI.SPI(SPI_BUS, SPI_DEVICE)
    spi.mode = 3
    spi.msh = 500000
    # spi.setBitOrder(SPI.MSBFIRST)

    # Set up chip select pin
    GPIO.setup(CS_PIN, GPIO.OUT)
    GPIO.output(CS_PIN, GPIO.LOW)

    # Function to read data from the ADXL343
    def read_spi_data(register):
        spi.xfer2([register | 0x80, 0])
        value = spi.xfer2([0, 0])
        return value[0]

    # Function to read 16-bit data from two registers
    def read_spi_data_16bit(register):
        high_byte = read_spi_data(register)
        low_byte = read_spi_data(register + 1)
        return (high_byte << 8) | low_byte

    try:
        while True:
            # Read accelerometer data
            x_data = read_spi_data_16bit(0x32)
            y_data = read_spi_data_16bit(0x34)
            z_data = read_spi_data_16bit(0x36)

            # Determine orientation
            if x_data > 1:
                orientation = "Right"
            elif x_data < -1:
                orientation = "Left"
            elif y_data > 1:
                orientation = "Down"
            elif y_data < -1:
                orientation = "Up"
            else:
                orientation = "Flat"

            # Print orientation
            print(f"Orientation: {orientation}")
            
            # Optional: Print raw acceleration values
            print(f"Acceleration (X, Y, Z): {x_data}, {y_data}, {z_data}")

            time.sleep(1)

    except KeyboardInterrupt:
        GPIO.cleanup()
        print("Accelerometer orientation detection stopped.")

else:
    import busio
    import adafruit_adxl34x
    
    i2c = busio.I2C("I2C2_SCL", "I2C2_SDA")
    accelerometer = adafruit_adxl34x.ADXL343(i2c)
    while True:
        acceleration = accelerometer.acceleration
        print(acceleration)
        time.sleep(1)