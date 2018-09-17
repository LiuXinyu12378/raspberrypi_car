import RPi.GPIO as GPIO  
import time
GPIO.setmode(GPIO.BOARD)  
GPIO.setup(23, GPIO.OUT)    
GPIO.setup(29, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)

GPIO.output(23, 0)
GPIO.output(29, 0)
GPIO.output(31, 0)
GPIO.output(33, 1)
time.sleep(1)    
GPIO.cleanup()    

GPIO.cleanup()

    