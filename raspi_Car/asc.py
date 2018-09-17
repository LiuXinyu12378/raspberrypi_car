import cv2
Img = cv2.imread('WASD.jpg')
cv2.imshow('Img', Img) 
while True:
    Key = chr(cv2.waitKey(100) & 255)
    print(Key)