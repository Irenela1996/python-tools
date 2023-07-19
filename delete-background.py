import os
from rembg import remove
from PIL import Image


def remove_backgrounds(folder_path):
    # Crear una subcarpeta dentro de la carpeta inicial para guardar las imágenes sin fondo
    output_folder = os.path.join(folder_path, "sin_fondo")
    os.makedirs(output_folder, exist_ok=True)

    # Obtener la lista de archivos en la carpeta
    file_list = os.listdir(folder_path)

    # Filtrar solo los archivos con extensiones de imágenes compatibles (puedes agregar más extensiones si es necesario)
    image_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".webp")
    image_files = [
        file for file in file_list if file.lower().endswith(image_extensions)
    ]

    # Procesar cada imagen para eliminar el fondo y guardarla en la subcarpeta
    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        with open(image_path, "rb") as image_stream:
            # Utilizar rembg para eliminar el fondo de la imagen
            output = remove(image_stream.read())

        # le quitamos la extensión al archivo original
        image_file_name = os.path.splitext(image_file)[0]
        # le ponemos la extensión .png
        image_file_name = image_file_name + ".png"

        # Guardar la imagen resultante en la subcarpeta "sin_fondo" con el mismo nombre que el archivo original, pero con extensión .png
        output_file = os.path.join(
            output_folder, image_file_name.replace(".", "_sin_fondo.")
        )
        with open(output_file, "wb") as new_image_stream:
            new_image_stream.write(output)


if __name__ == "__main__":
    # Le pasamos la ruta absoluta de la carpeta con las imágenes
    folder_path = input("Ingrese la carpeta con la que desea trabajar: ")
    remove_backgrounds(folder_path)
