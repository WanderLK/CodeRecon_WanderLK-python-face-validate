import cv2
import numpy as np

def check_aspect_ratio(image_path):
    image = cv2.imread(image_path)
    h, w = image.shape[:2]
    if h / w == 1 / 1:
        return True
    return False

def check_resolution(image_path, min_resolution=600, max_resolution=1200):
    image = cv2.imread(image_path)
    h, w = image.shape[:2]
    if h >= min_resolution and w >= min_resolution and h <= max_resolution and w <= max_resolution:
        return True
    return False

def check_background(image_path, edge_threshold=2.1, border_ratio=0.2):  
    image = cv2.imread(image_path)
    resized_image = cv2.resize(image, (300, 400))
    
    blurred_image = cv2.GaussianBlur(resized_image, (5, 5), 0)
    
   
    edges = cv2.Canny(blurred_image, 100, 200)
    
    height, width = edges.shape
    border_width = int(width * border_ratio)
    border_height = int(height * border_ratio)
    
    top_edges = edges[:border_height, :]
    bottom_edges = edges[-border_height:, :]
    left_edges = edges[:, :border_width]
    right_edges = edges[:, -border_width:]
    
    total_border_edges = (
        np.sum(top_edges) +
        np.sum(bottom_edges) +
        np.sum(left_edges) +
        np.sum(right_edges)
    )
    total_border_area = (
        top_edges.size +
        bottom_edges.size +
        left_edges.size +
        right_edges.size
    )
    edge_density = total_border_edges / total_border_area
    
    if edge_density > edge_threshold:
        return False  
    else:
        return True