# -*- coding: utf-8 -*-
import cv2
import RPi.GPIO as GPIO    
import time

cap = cv2.VideoCapture(0)  
GPIO.setmode(GPIO.BOARD)     
GPIO.setup(37, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)    
GPIO.setup(29, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)

Img = cv2.imread('WASD.jpg')
cv2.namedWindow('Img', flags=cv2.WINDOW_NORMAL | cv2.WINDOW_FREERATIO)

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
    GPIO.output(37, 1) 
     
def stop_():
    GPIO.setmode(GPIO.BOARD)     
    GPIO.setup(37, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)    
    GPIO.setup(29, GPIO.OUT)
    GPIO.setup(31, GPIO.OUT)
    GPIO.setup(33, GPIO.OUT)
    GPIO.cleanup()

    
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
    GPIO.output(37, 1) 
    
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
    GPIO.output(37, 1)
    
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
    GPIO.output(37, 1)

img_count = 1
while True:
    ret, frame = cap.read()
    cv2.imshow('Capture', frame)
    cv2.imshow('Img', Img)    
    Key = chr(cv2.waitKey(30) & 255)  
    if Key == 'w':
        Img = cv2.imread('W.jpg')
        go_stright()    
    elif Key == 'a':
        Img = cv2.imread('A.jpg')
        turn_left()
    elif Key == 's':
        Img = cv2.imread('S.jpg')
        go_down()
    elif Key == 'd':
        Img = cv2.imread('D.jpg')
        turn_right()
    else:
        Img = cv2.imread('WASD.jpg')
        stop_()
        



   
      

