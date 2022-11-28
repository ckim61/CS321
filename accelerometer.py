#update the pi first 
#in terminal do [sudo apt-get update] then [sudo apt-get upgrade]
# this code gives the accelerometer data (x,y,z) every 2 seconds.
import time
import board
import digitalio
import busio
import adafruit_lis3dh #if not install do [sudo pip3 install adafruit-circuitpython-lis3dh] to install library

i2c = busio.I2C(board.SCL, board.SDA)                
int1 = digitalio.DigitalInOut(board.D6)             # interrupt connected to GPIO6
lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, int1=int1) 

x, y, z = lis3dh.acceleration

while True:
  print("%0.3f %0.3f %0.3f" % (x, y, z))
  time.sleep(2)
