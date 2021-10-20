#!/usr/bin/env python2.7  
# demo of "BOTH" bi-directional edge detection  
# script by Alex Eames https://raspi.tv  
# https://raspi.tv/?p=6791  
  
import RPi.GPIO as GPIO  
from time import sleep     # this lets us have a time delay (see line 12)  
  
GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering  
GPIO.setup(17, GPIO.IN)    # set GPIO25 as input (button)  
  
# Define a threaded callback function to run in another thread when events are detected  
def my_callback(channel):  
    if GPIO.input(17):     # if port 25 == 1  
        print ("Yes")  
    else:                  # if port 25 != 1  
        print ("No")  
  
# when a changing edge is detected on port 25, regardless of whatever   
# else is happening in the program, the function my_callback will be run  
GPIO.add_event_detect(17, GPIO.BOTH, callback=my_callback)  
    
input("Press Enter when ready\n>")  
  
try:  
    print ("When pressed, you'll see: Rising Edge detected on 25")  
    print ("When released, you'll see: Falling Edge detected on 25" ) 
    sleep(30)         # wait 30 seconds  
    print ("Time's up. Finished!" ) 
  
finally:                   # this block will run no matter how the try block exits  
    GPIO.cleanup()  