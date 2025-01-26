import cv2
import numpy as np
from PIL import Image
import pytesseract
import os

def detectar_angulo_rotacion(image_path):
    # Cargar la imagen en escala de grises
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detectar bordes en la imagen
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

    # Detectar líneas usando la transformada de Hough
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)

    # Si encontramos líneas, calcular el ángulo promedio de rotación
    angles = []
    if lines is not None:
        for rho, theta in lines[:, 0]:
            angle = np.degrees(theta) - 90  # Convertir de radianes a grados
            angles.append(angle)
    
    # Si encontramos ángulos, calcular el ángulo promedio
    if angles:
        return np.mean(angles)
    else:
        return 0  # Si no se detectan líneas, supondremos que no hay rotación

def corregir_rotacion(image_path, angulo, output_dir="rotated_images"):
    # Cargar la imagen original
    image = Image.open(image_path)
    
    # Convertir a formato OpenCV para realizar la rotación
    cv_image = cv2.imread(image_path)
    
    # Obtener las dimensiones de la imagen
    (h, w) = cv_image.shape[:2]
    center = (w // 2, h // 2)
    
    # Crear la matriz de rotación
    M = cv2.getRotationMatrix2D(center, angulo, 1.0)
    
    # Rotar la imagen
    rotated = cv2.warpAffine(cv_image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    
    # Crear el nombre del archivo para la imagen rotada
    rotated_filename = f"imagen/imagen_mejorada_rotada.jpg"
    
    # Guardar la imagen rotada
    cv2.imwrite(rotated_filename, rotated)
    
    # Retornar la ruta de la imagen rotada
    return rotated_filename