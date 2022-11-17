# BLUE IS STEERING
# Libraries or packages used.

import RPi.GPIO as GPIO
import curses, time, os, sys
import pigpio

# pins used
steering_pin = 12 # Pin used for the steering.
ESC = 13 # pin used for motor
# Frequency used for the steering, which is 50Hz.
steer_freq = 50

# Setup the GPIO board.
GPIO.setmode(GPIO.BCM)
# Setup the servo pin
GPIO.setup(steering_pin,GPIO.OUT) # This sets up the pin for the Steering servo.

# Sets up the PWM for the steering and ESC motor.
pwm_steering = GPIO.PWM(steering_pin,steer_freq)
full_left = 10
full_right = 5
middle = 7.5
# This set steering in the middle
pwm_steering.start(middle) # pwm_steering.start(0); start the signal at 0 ? 

# Motor max, min, and break constants
ESC_Max = 1300 #Max forward
ESC_Min = 1700 #Max reverse
ESC_break = 1500 #Breaking

# Set up motor
pi = pigpio.pi();
pi.set_servo_pulsewidth(ESC, 0) #Starts motor at break
time.sleep(1)
pi.set_servo_pulsewidth(ESC, ESC_break)

#Initialize curses to detect keyboard inputs
stdCurses = curses.initscr()
stdCurses.keypad(True)
curses.cbreak()
curses.echo(False)


while True:
    c = stdCurses.getch() #Retrieve the input

    if c == ord('w'):
        print("pressed w");
       
        # Checks if the car is coasting at 0 pulse
        # Starts the motor at one step forwards
        if pi.get_servo_pulsewidth(ESC) == 0:
            pi.set_servo_pulsewidth(ESC, ESC_break - 50)
       
        # Checks if the car is below the max
        # Increments the motor
        elif pi.get_servo_pulsewidth(ESC) < ESC_Max:
            pi.set_servo_pulsewidth(ESC, pi.get_servo_pulsewidth(ESC) - 100)
        
        # If greater than max
        # Sets motor to max
        else:
            pi.set_servo_pulsewidth(ESC, ESC_Max)
       
        print("Current Speed: ", pi.get_servo_pulsewidth(ESC))

    elif c == ord('s'):
        # Checks if the car is coasting at 0 pulse
        # Starts the motor at one step backwards
        if pi.get_servo_pulsewidth(ESC) == 0:
            pi.set_servo_pulsewidth(ESC, ESC_break + 50)
        
        # Checks if the car is above the min
        # Decrements the motor
        elif pi.get_servo_pulsewidth(ESC) > ESC_Min:
            pi.set_servo_pulsewidth(ESC, pi.get_servo_pulsewidth(ESC) + 100)
        
        # If less than min
        # Sets motor to min
        else:
            pi.set_servo_pulsewidth(ESC, ESC_Min)

    elif c == ord('q'):
        pwm_steering.ChangeDutyCycle(middle)
        pwm_steering.stop()
        GPIO.cleanup()
        break
    elif c == ord('a'):
        pwm_steering.ChangeDutyCycle(full_left) #sets servo to left position
    elif c == ord('d'):
        pwm_steering.ChangeDutyCycle(full_right) #sets servo to right position
    elif c == ord('c'):
        pwm_steering.ChangeDutyCycle(middle)


curses.nocbreak()
curses.echo()
curses.endwin()