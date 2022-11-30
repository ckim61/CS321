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
alignment = middle

speed = 0

# This set steering in the middle
pwm_steering.start(middle) # pwm_steering.start(0); start the signal at 0 ? 

# Motor break constant
ESC_break = 1500 #Breaking

def quit():
    pi.set_servo_pulsewidth(ESC, 0)
    pi.stop()
    pwm_steering.ChangeDutyCycle(middle)
    pwm_steering.stop()
    curses.nocbreak()
    curses.echo()
    curses.endwin()
    exit()

def control():
    #Initialize curses to detect keyboard inputs
    stdCurses = curses.initscr()
    stdCurses.keypad(True)
    curses.echo(False)
    curses.cbreak()
    ESC_Max = 1000 #Max forward
    ESC_Min = 2000 #Max reverse
    speed = 0
    alignment = middle
    while True:
        c = stdCurses.getch() #Retrieve the input

        if c == ord('w'):
            print("pressed w");
           
            # Checks if the car is coasting at 0 pulse
            # Starts the motor at one step forwards
            if speed == 0:
                speed = ESC_break - 50
           
            # Checks if the car is below the max
            # Increments the motor
            elif speed > ESC_Max:
                speed = speed - 50
                if speed < ESC_Max:
                    speed = ESC_Max
            
            # If greater than max
            # Sets motor to max
            else:
                speed = ESC_Max
            pi.set_servo_pulsewidth(ESC, speed)           
            print("Current Speed: ", pi.get_servo_pulsewidth(ESC))

        elif c == ord('s'):
            print("pressed s");

            # Checks if the car is coasting at 0 pulse
            # Starts the motor at one step backwards
            if speed == 0:
                speed = ESC_break + 50
            
            # Checks if the car is above the min
            # Decrements the motor
            elif speed < ESC_Min:
                speed = speed + 50
                if speed > ESC_Min:
                    speed = ESC_Min
            
            # If less than min
            # Sets motor to min
            else:
                speed = ESC_Min
            pi.set_servo_pulsewidth(ESC, speed)
            print("Current Speed: ", speed)

        elif c == ord('q'):
            pwm_steering.ChangeDutyCycle(middle)
            pwm_steering.stop()
            GPIO.cleanup()
            quit()
        elif c == ord('a'):
            if alignment >= full_left:
                alignment = full_left
            else:
                alignment = alignment + 1.25
            pwm_steering.ChangeDutyCycle(alignment) #sets servo to left position
        elif c == ord('d'):
            if alignment <= full_right:
                alignment = full_right
            else:
                alignment = alignment - 1.25
            pwm_steering.ChangeDutyCycle(alignment) #sets servo to left position
        elif c == ord('c'):
            pwm_steering.ChangeDutyCycle(middle)
        elif c == ord('v'):
            pi.set_servo_pulsewidth(ESC, 0)

def arm():
    sleep = 0
    pi.set_servo_pulsewidth(ESC, 0)
    print("Make sure battery is connected but switch is OFF.  Press ENTER to continue")
    inp = input()
    if inp == '':
        pi.set_servo_pulsewidth(ESC, ESC_break - 50)
        print("Turn the switch ON now. You will hear two beeps then press Enter")
        inp = input()
        if inp == '':            
            pi.set_servo_pulsewidth(ESC, ESC_break + 50)
            print ("Working...")
            time.sleep(2)
            print ("Wait for it ....")
            time.sleep (1)
            print ("Almost there.....")
            pi.set_servo_pulsewidth(ESC, 0)
            time.sleep(1)
            print ("Arming ESC now...")
            pi.set_servo_pulsewidth(ESC, ESC_break + 50)
            time.sleep(1)
            print ("ESC is armed.  Entering control function")
            pi.set_servo_pulsewidth(ESC, 0)
            control()

# Set up motor
pi = pigpio.pi()
arm()