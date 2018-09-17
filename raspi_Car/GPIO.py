# -*- coding: utf-8 -*-
import cv2
import RPi.GPIO as GPIO    
import time
  
GPIO.setmode(GPIO.BOARD)     
GPIO.setup(37, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)    
GPIO.setup(29, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
global p
global i
i=0

Img = cv2.imread('WASD.jpg')

def go_stright():
    GPIO.setmode(GPIO.BOARD)     
    GPIO.setup(37, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)    
    GPIO.setup(29, GPIO.OUT)
    GPIO.setup(31, GPIO.OUT)
    GPIO.setup(33, GPIO.OUT)
    GPIO.output(23, 1)
    GPIO.output(29, 0)
    GPIO.output(31, 1)
    GPIO.output(33, 0)
    
     
def stop_():
    GPIO.setmode(GPIO.BOARD)     
    GPIO.setup(37, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)    
    GPIO.setup(29, GPIO.OUT)
    GPIO.setup(31, GPIO.OUT)
    GPIO.setup(33, GPIO.OUT)
    GPIO.output(23, 0)
    GPIO.output(29, 0)
    GPIO.output(31, 0)
    GPIO.output(33, 0)

    
def turn_right():
    GPIO.setmode(GPIO.BOARD)     
    GPIO.setup(37, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)    
    GPIO.setup(29, GPIO.OUT)
    GPIO.setup(31, GPIO.OUT)
    GPIO.setup(33, GPIO.OUT)
    GPIO.output(23, 0)
    GPIO.output(29, 1)
    GPIO.output(31, 1)
    GPIO.output(33, 0)
    
    
def turn_left():
    GPIO.setmode(GPIO.BOARD)     
    GPIO.setup(37, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)    
    GPIO.setup(29, GPIO.OUT)
    GPIO.setup(31, GPIO.OUT)
    GPIO.setup(33, GPIO.OUT)
    GPIO.output(23, 1)
    GPIO.output(29, 0)
    GPIO.output(31, 0)
    GPIO.output(33, 1)
    
    
def go_down():
    GPIO.setmode(GPIO.BOARD)     
    GPIO.setup(37, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)    
    GPIO.setup(29, GPIO.OUT)
    GPIO.setup(31, GPIO.OUT)
    GPIO.setup(33, GPIO.OUT)
    GPIO.output(23, 0)
    GPIO.output(29, 1)
    GPIO.output(31, 0)
    GPIO.output(33, 1)
    

while True:
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(37, GPIO.OUT)
    cv2.imshow('Img', Img)
    
    Key = chr(cv2.waitKey(10) & 255)  
    if Key == 'w':
        Img = cv2.imread('W.jpg')
        go_stright()
    elif Key == 'R':
        Img = cv2.imread('W.jpg')
        go_stright()   
    elif Key == 'a':
        Img = cv2.imread('A.jpg')
        turn_left()
    elif Key == 'Q':
        Img = cv2.imread('A.jpg')
        turn_left()
    elif Key == 's':
        Img = cv2.imread('S.jpg')
        go_down()
    elif Key == 'T':
        Img = cv2.imread('S.jpg')
        go_down()
    elif Key == 'd':
        Img = cv2.imread('D.jpg')
        turn_right()
    elif Key == 'S':
        Img = cv2.imread('D.jpg')
        turn_right()
    elif Key == 'q':
        Img = cv2.imread('Q.jpg')
        i=i+1
        if(i==1):
            p= GPIO.PWM(37, 1)
            p.ChangeDutyCycle(50)
            p.start(1)      
    elif Key == 'e':
        Img = cv2.imread('E.jpg')
        p.stop()
    elif Key == '':
        cv2.destroyAllWindows()
        break
    else:
        Img = cv2.imread('WASD.jpg')
        stop_()
        i=0



   
      


