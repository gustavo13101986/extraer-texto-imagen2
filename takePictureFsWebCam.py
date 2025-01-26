

import subprocess

def take_photo(output_file="photo.jpg", resolution="1920x1080"):
    try:
        # Construir el comando de fswebcam
        command = [
            "fswebcam",
            "-r", resolution,  # Configurar resolución
            "--no-banner",     # Desactivar la marca de agua de fswebcam
            output_file        # Nombre del archivo de salida
        ]
        # Ejecutar el comando
        subprocess.run(command, check=True)
        print(f"Foto guardada como {output_file} con resolución {resolution}.")
        return output_file
    except FileNotFoundError:
        print("Error: fswebcam no está instalado. Instálalo con 'sudo apt install fswebcam'.")
    except subprocess.CalledProcessError as e:
        print(f"Error al tomar la foto: {e}")