#import cv2
from PIL import Image, ImageEnhance


def mejorar_contraste_bn(ruta_imagen, output_dir="processed_images"):
    # Crear el directorio de salida si no existe

    # Lee la imagen
    imagen = Image.open(ruta_imagen)

    # Convertir a escala de grises
    imagen = imagen.convert("L")

    # Mejorar el contraste
    enhancer = ImageEnhance.Contrast(imagen)
    image_contrast = enhancer.enhance(2)  # Ajusta el nivel de contraste (2 es un ejemplo)

    # Guardar o mostrar la imagen mejorada
    image_contrast.save(f"imagen/imagen_mejorada.jpg")

    processed_filename = "imagen/imagen_mejorada.jpg"

    
    # Cargar la imagen en escala de grises
    #gray_image = cv2.imread(ruta_imagen, cv2.IMREAD_GRAYSCALE)
    
    # Aplicar CLAHE para mejorar el contraste
    #clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    #contrast_image = clahe.apply(gray_image)
    
    # Convertir a blanco y negro usando un umbral adaptativo
    #_, bw_image = cv2.threshold(contrast_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Guardar la imagen procesada
    #cv2.imwrite(processed_filename, bw_image)
    
    # Retornar la ruta de la imagen procesada
    return processed_filename