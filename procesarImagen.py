import pytesseract
from PIL import Image
import re
from takePictureFsWebCam import take_photo
from datetime import datetime
from rotar_imagen import detectar_angulo_rotacion, corregir_rotacion
from mejorar_contraste import mejorar_contraste_bn

def procesarImagen():
    # Especifica la ruta de la imagen que quieres leer
    #ruta_imagen = 'imagen/imagen2.jpeg'  # Reemplaza 'tu_imagen.jpg' con la ruta de tu imagen

    # Obtener la fecha y hora actual
    fecha_actual = datetime.now()

    fecha_formateada = fecha_actual.strftime("%Y-%m-%d_%H-%M-%S")

    #ruta_imagen = take_picture()
    #ruta_imagen = take_photo(f"imagen/{fecha_formateada}.jpg", "1920x1080")
    ruta_imagen = take_photo(f"imagen/foto.jpg", "1920x1080")

    

    mejorar_contraste_bn(ruta_imagen)

    
    angulo = detectar_angulo_rotacion(f"imagen/imagen_mejorada.jpg")

    print(f"Ángulo detectado: {angulo} grados")
    
    # Corregir la rotación de la imagen
    image = corregir_rotacion(f"imagen/imagen_mejorada.jpg", angulo)


    image_to_process = Image.open(image)

    # Extrae el texto de la imagen
    texto = pytesseract.image_to_string(image_to_process, lang='eng')  # 'spa' indica que el texto está en español



    def extraer_linea_Destino(texto):
        """
        Busca la palabra 'destino' en un texto y devuelve el fragmento desde donde 
        aparece hasta el siguiente salto de línea.

        Args:
            texto (str): El texto donde se buscará.

        Returns:
            list: Lista de fragmentos que contienen 'destino' hasta el próximo salto de línea.
        """
        if not isinstance(texto, str):
            raise ValueError("La entrada debe ser un string.")

        # Expresión regular para encontrar "destino" y el texto hasta el próximo salto de línea
        patrones = re.finditer(r"Destino.*?(?=\n|$)", texto, re.IGNORECASE)

        # Extraer los fragmentos que coinciden
        fragmentos = [match.group() for match in patrones]

        return fragmentos

    texto_original = extraer_linea_Destino(texto)

    if len(texto_original) > 0:
        print(texto)
        return texto_original
    else:
        # Si el texto no tiene sentido, probar con rotación de 180 grados
        print("Texto no legible, intentando con rotación de 180 grados...")
        image_180 = corregir_rotacion("imagen/imagen_mejorada_rotada.jpg", 180)
        image_to_process = Image.open("imagen/imagen_mejorada_rotada.jpg")
        texto_180 = pytesseract.image_to_string(image_to_process, lang='eng') 
        
        texto_original = extraer_linea_Destino(texto_180)

        # Verificar si el texto ahora tiene sentido
        if len(texto_original) > 0:
            return texto_original
        else:
            return ""
            print("No se pudo leer el texto")
        return texto_180