import os
import requests

# Lista de URLs de imágenes
img_urls = ["Insertar links"]


# Define la ruta de la carpeta de salida
output_folder = r"Insertar ruta de destino"

# Crear el directorio si no existe
os.makedirs(output_folder, exist_ok=True)

# Descargar y guardar cada imagen
for i, url in enumerate(img_urls):
    try:
        # Obtener el contenido de la imagen
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción para códigos de estado HTTP de error

        # Definir el nombre del archivo
        file_name = os.path.join(output_folder, f"imagen_{i+1}.jpg")

        # Guardar el contenido de la imagen en un archivo
        with open(file_name, 'wb') as img_file:
            img_file.write(response.content)

        print(f"Imagen guardada en: {file_name}")

    except requests.RequestException as e:
        print(f"No se pudo descargar la imagen {url}: {e}")

#Chat gpt Genereted, todos los derechos a gpt xd xd :V