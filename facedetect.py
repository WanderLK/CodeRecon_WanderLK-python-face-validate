import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def identify_faces(image_path):
    
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    image_center_x = image.shape[1] // 2
    image_center_y = image.shape[0] // 2

    max_height_ratio = 30//45
    min_height_ratio = 26//45

    if len(faces) == 1:

        x, y, w, h = faces[0]

        # get face center coordinates
        face_left = x
        face_top = y
        face_right = x + w
        face_bottom = y + h

        x_threshold = 0.1 * image.shape[1]
        y_threshold = 0.1 * image.shape[0]

        if face_left < image_center_x - x_threshold  and face_right > image_center_x + x_threshold :
            if face_top < image_center_y - y_threshold and face_bottom > image_center_y + y_threshold:

                if (w // image.shape[0]) <= max_height_ratio and  (w // image.shape[0]) >= min_height_ratio:
                    return True ,'Face detected'
                else:
                    return False, "Not valid Ratios" 
            else:
                return False, 'Face is not centered vertically'
        else:
            return False, 'Face is not centered horizontally'
    elif len(faces) > 1:
        return False,'Multiple faces detected'
    else :
        return False,'No face detected'