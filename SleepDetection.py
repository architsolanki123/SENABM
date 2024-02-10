import cv2
import time
import os
import pygame

pygame.init()

alarm = pygame.mixer.Sound('alarm.wav')

script_dir = os.path.dirname(os.path.abspath(__file__))

face_cascade_path = os.path.join(script_dir, 'haarcascade_frontalface_default.xml')
eye_cascade_path = os.path.join(script_dir, 'haarcascade_eye_tree_eyeglasses.xml')

face_cascade = cv2.CascadeClassifier(face_cascade_path)
eye_cascade = cv2.CascadeClassifier(eye_cascade_path)

cap = cv2.VideoCapture(0)
a=0
b=0
c=time.time()
while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    if len(faces) == 0:
        print("No face detected")

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
        eyes = eye_cascade.detectMultiScale(roi_gray)
        
        if (time.time()-c) >= 15:
            if a/(a+b)>=0.2:
                alarm.play()
                print("****ALERT*****",a,b,a/(a+b))
                
            else:
                print("safe",a/(a+b))
            c=time.time()
            a=0
            b=0
        
        if len(eyes) == 0:
            a=a+1
            print('no eyes!!!')
        else:
            b=b+1
            print('eyes!!!')
            
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    cv2.imshow('SleepAware',img)

    k = cv2.waitKey(1) & 0xff
    if k == 27:
        print("noeyes: ",a)
        print("total: ",(a+b))
        break

cap.release()
cv2.destroyAllWindows()