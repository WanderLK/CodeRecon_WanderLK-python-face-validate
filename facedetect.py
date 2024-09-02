import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def identify_faces(image_path):
    
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

    if len(faces) > 0 and len(faces) < 2:
        return 'Face detected'

    else:
        return 'No face detected'
