import cv2

def identify_faces(image_path):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
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
        face_to_image_ratio = total_face_area / image_area if image_area > 0 else 0
        return True 
    elif len(faces) > 1:
        return 'Multiple faces detected'
    else :
        return 'No face detected'