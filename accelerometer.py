import time
import board
import digitalio
import busio
import adafruit_lis3dh

i2c = busio.I2C(board.SCL, board.SDA)                # Remove this line if using SPI
int1 = digitalio.DigitalInOut(board.D24)             # Remove this line if using SPI
lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, int1=int1)  # Remove this line if using SPI

x, y, z = lis3dh.acceleration

while True:
  print("%0.3f %0.3f %0.3f" % (x, y, z))
  time.sleep(2)
