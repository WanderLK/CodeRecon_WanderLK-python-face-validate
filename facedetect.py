import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def identify_faces(image_path):
    
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    height, width = image.shape[:2]
    image_area = height * width
    
    total_face_area = 0

    for (x, y, w, h) in faces:
        face_area = w * h
        total_face_area += face_area
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

    if len(faces) == 1:
        return True,"image is valid"

    elif len(faces) > 1:
        return False,'Multiple faces detected'
    else :
        return False,'No face detected'