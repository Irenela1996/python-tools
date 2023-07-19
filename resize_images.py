import os
from PIL import Image

RUTA_BASE = "home/usuario/imagenes"


def comprobaciones(ruta):
    # Comprobamos si la ruta existe
    if not os.path.exists(ruta):
        print("La ruta introducida no existe")
        exit()
    # Comprobamos si la ruta es una carpeta
    if not os.path.isdir(ruta):
        print("La ruta introducida no es una carpeta")
        exit()
    # Comprobamos si la carpeta está vacía
    if not os.listdir(ruta):
        print("La carpeta está vacía")
        exit()


def size(ancho, alto):
    ancho = int(ancho)
    alto = int(alto)
    # Comprobamos si el tamaño es válido
    if ancho <= 0 or alto <= 0:
        print("El tamaño introducido no es válido")
        exit()


def redimensionado(ruta, archivo):
    # Comprobamos si es una imagen
    if (
        archivo.endswith(".jpg")
        or archivo.endswith(".png")
        or archivo.endswith(".jpeg")
        or archivo.endswith(".webp")
    ):
        # Abrimos la imagen
        imagen = Image.open(os.path.join(ruta, archivo))
        # Redimensionamos
        imagen.thumbnail((ancho, alto))
        # Guardamos la imagen en una carpeta llamada redimensionadas, si no existe la crea
        if not os.path.exists(os.path.join(ruta, "redimensionadas")):
            os.mkdir(os.path.join(ruta, "redimensionadas"))
        imagen.save(os.path.join(ruta, "redimensionadas", archivo))
        print("Imagen redimensionada: " + archivo)


if __name__ == "__main__":
    # Preguntamos la ruta de las carpetas a procesar. Esta ruta debe ser absoluta
    ruta = input("Introduce la ruta de la carpeta a procesar: ")
    # si no nos introduce una ruta, por defecto será la carpeta RUTA_BASE
    if ruta == "":
        ruta = RUTA_BASE
    # Comprobamos la ruta
    comprobaciones(ruta)

    # Preguntamos el tamaño de las imágenes
    ancho = str(input("Introduce el ancho de las imágenes: "))
    alto = str(input("Introduce el alto de las imágenes: "))
    # si no nos introduce un tamaño, por defecto será 320x320
    if ancho == "":
        ancho = 320
    if alto == "":
        alto = 320
    # Comprobamos el tamaño
    size(int(ancho), int(alto))

    # Recorremos la carpeta
    for archivo in os.listdir(ruta):
        redimensionado(ruta, archivo)
