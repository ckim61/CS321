# BLUE IS STEERING
# Libraries or packages used.
import RPi.GPIO as GPIO
import curses, time, os, sys
# pins used
steering_pin = 12 # Pin used for the steering.
# Frequency used for the steering, which is 50Hz.
steer_freq = 50
# Setup the GPIO board.
GPIO.setmode(GPIO.BOARD)
# Setup the pins.
GPIO.setup(steering_pin,GPIO.OUT) # This sets up the pin for the Steering servo.
# Sets up the PWM for the steering and ESC motor.
pwm_steering = GPIO.PWM(steering_pin,steer_freq)
full_left = 10
full_right = 5
middle = 7.5
# This set steering in the middle
pwm_steering.start(middle)


#Initializes curses to detect keyboard inputs
stdCurses = curses.initscr()
stdCurses.keypad(True)
curses.cbreak()
curses.echo(False)

# Continuously checks the input
while True:
    c = stdCurses.getch() #retrieves input
    if c == ord('a'):
        pwm_steering.ChangeDutyCycle(full_left) #sets servo to left position
    elif c == ord('d'):
        pwm_steering.ChangeDutyCycle(full_right) #sets servo to right position
    elif c == ord('q'):
        pwm_steering.ChangeDutyCycle(middle)
        pwm_steering.stop()
        GPIO.cleanup()
        break
    else:
        pwm_steering.ChangeDutyCycle(middle) #resets servo to straight


curses.nocbreak()
curses.echo()
curses.endwin()

