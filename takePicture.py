import sys
sys.path.append('/usr/lib/python3/dist-packages')
from picamera2 import Picamera2
import time

def take_picture():
    picam2 = Picamera2()
    
    # Configuración para calidad y enfoque
    still_config = picam2.create_still_configuration(
        {"size": (1280, 720)},  # Resolución máxima de la cámara
        raw={"format": "SRGGB10", "size": (2592, 1944)},  # Formato RAW para más calidad
        buffer_count=3
    )
    picam2.configure(still_config)
    
    # Ajustar controles de la cámara
    picam2.set_controls({
        #"AfMode": 2,  # Autofocus continuo
        "AwbEnable": True,  # Balance automático de blancos
        "Sharpness": 1.5,  # Mejora de nitidez
        "Contrast": 1.2,  # Mejora del contraste
        "Saturation": 1.2,  # Mejora de los colores
        "ExposureValue": 0.5,  # Ajuste de exposición (puedes probar valores negativos o positivos)
        "Brightness": 0.5  # Ajuste de brillo
    })

    picam2.start()
    time.sleep(2)  # Esperar para que la cámara se ajuste

    output_file = "foto.jpeg"
    picam2.capture_file(output_file)
    picam2.stop()

    print("Foto capturada y guardada como", output_file)
    return output_file
