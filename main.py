import os
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pathlib import Path
import RPi.GPIO as GPIO
from time import sleep
import subprocess
from procesarImagen import procesarImagen

app = FastAPI()

# Configuración GPIO
INPUT_PIN = 17  # Cambia al pin GPIO que estás usando
GPIO.setmode(GPIO.BCM)
GPIO.setup(INPUT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Directorio donde guardar imágenes
# IMAGE_DIRECTORY = Path("/home/pi/images")
# MAGE_DIRECTORY.mkdir(exist_ok=True)

@app.get("/")
def read_root():
    return {"message": "Servidor FastAPI funcionando correctamente"}

@app.get("/images/{image_name}")
def serve_image(image_name: str):
    file_path = IMAGE_DIRECTORY / image_name
    if not file_path.exists():
        return {"error": "La imagen no existe"}
    return FileResponse(file_path)


@app.get("/procesar-imagen")
def procesar_imagen():
    procesarImagen()
    return {"message": "Servidor FastAPI funcionando correctamente"}