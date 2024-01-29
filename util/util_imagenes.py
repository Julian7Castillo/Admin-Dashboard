#Importamos de la libreriaa pil o pillow lo necesario para escalar las imagenes
from PIL import ImageTk, Image

#funcion para escalar imagenes
def leer_imagen(path, size):
    """funcion para escalar imagenes"""
    return ImageTk.PhotoImage(Image.open(path).resize(size, Image.ADAPTIVE))
