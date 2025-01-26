import RPi.GPIO as GPIO
from time import sleep
from procesarImagen import procesarImagen

# Configuración GPIO
INPUT_PIN = 17  # Cambia al pin GPIO que estás usando
GPIO.setmode(GPIO.BCM)
GPIO.setup(INPUT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

import csv

def comparar_direccion(csv_file, direccion_a_comparar):
    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)  # Leer el archivo como un diccionario
        for row in reader:
            direccion_csv = row.get('direccion')  # Cambia 'direccion' por el nombre de la columna correspondiente
            zona_csv = row.get('zona')  # Obtén la columna 'zona' (ajusta el nombre según tu CSV)

            # Verifica si la dirección del CSV está contenida en la dirección que estás pasando
            if direccion_csv and direccion_a_comparar and direccion_csv.strip() in direccion_a_comparar.strip():
                print(f"Dirección encontrada: {direccion_csv}")
                print(f"Zona: {zona_csv}")  # Devuelve la zona que corresponde
                return {"is_found": True, "zona": zona_csv}
    
    print("Dirección no encontrada.")
    return {"is_found": False, "zona": ""}





def main():
    print("Iniciando monitoreo del pin GPIO...")
    x = 0
    while True:
        # Detectar nivel lógico alto
        if GPIO.input(INPUT_PIN) == GPIO.HIGH:
            x += 1
            print("Nivel lógico alto detectado...> ", x)
            texto = procesarImagen()
            sleep(1)
            print("texto direccion>> ", texto)

            csv_file = 'direcciones.csv'
            if (len(texto)) > 0:
                direccion_a_comparar = texto[0]
                find_zona = comparar_direccion(csv_file, direccion_a_comparar)

                if (find_zona.is_found == True):
                    # enviar informacion por serial
                    print("encontro zona")
            

                

if __name__ == "__main__":
    main()

