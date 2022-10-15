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
GPIO.setmode(GPIO.BOARD)
# Setup the servo pin
GPIO.setup(steering_pin,GPIO.OUT) # This sets up the pin for the Steering servo.

# Sets up the PWM for the steering and ESC motor.
pwm_steering = GPIO.PWM(steering_pin,steer_freq)
full_left = 10
full_right = 5
middle = 7.5
# This set steering in the middle
pwm_steering.start(middle)

# Motor max, min, and break constants
ESC_Max = 1000 #Max forward
ESC_Min = 2000 #Max reverse
ESC_break = 1500 #Breaking

# Set up motor
pi = pigpio.pi();
pi.set_servo_pulsewidth(ESC, 0) #Starts motor at break
time.sleep(1)
pi.set_servo_pulsewidth(ESC, ESC_break)

# Function for if a key is pressed
def key_press(key):

    # Checks for 'w' or forward input
    if key.char == 'w':
       
        # Checks if the car is coasting at 0 pulse
        # Starts the motor at one step forwards
        if pi.get_servo_pulsewidth(ESC) == 0:
            pi.set_servo_pulsewidth(ESC, ESC_break - 50)
       
        # Checks if the car is below the max
        # Increments the motor
        elif pi.get_servo_pulsewidth(ESC) < ESC_Max:
=            pi.set_servo_pulsewidth(ESC, pi.get_servo_pulsewidth(ESC) - 100)
        
        # If greater than max
        # Sets motor to max
        else:
            pi.set_servo_pulsewidth(ESC_Max)
       
        print("Current Speed: ", pi.get_servo_pulsewidth(ESC))
   
    # Checks for 's' or backwards input
    if key.char == 's':

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
            pi.set_servo_pulsewidth(ESC_Min)

    # Checks for left input
    # Sets servo to left
    if key.char == 'a':
        pwm_steering.ChangeDutyCycle(full_left)
    
    # Checks for right input
    # Sets servo to right
    if key.char == 'd':
        pwm.ChangeDutyCycle(full_right)
   
   # Quit
    if key.char == 'q':
        pi.set_servo_pulsewidth(ESC, 0)
        pi.stop()
        pwm_steering.ChangeDutyCycle(middle)
        pwm_steering.stop()
        exit()

def key_release(key):

    # If 'w' is released
    # Set motor to coasting
    if key.char == 'w':
        pi.set_servo_pulsewidth(ESC, 0)

    # If 's' is released
    # Set motor to coasting
    if key.char == 's':
        pi.set_servo_pulsewidth(ESC, 0)

    # If 'a' is released
    # Set servo to middle position
    if key.char == 'a':
        pwm_steering.ChangeDutyCycle(middle)

    # If 'd' is released
    # Set servo to middle position
    if key.char == 'd':
        pwm_steering.ChangeDutyCycle(middle)

# Set up for keyboard listener
with keyboard.Listener(on_press = key_press, on_release = key_release) as listener:
    listener.join()