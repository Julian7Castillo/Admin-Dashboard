import tkinter as tk
import util.util_ventana as utl_ven

class FormularioInfoDesign(tk.Toplevel):

    #Constructor
    def __init__(self) -> None:
        super().__init__()
        self.configuracion_window()
        self.construirWidget()
        
    def configuracion_window(self):
        """Configuracion inicial de la ventana """
        self.title("Pythopn GUI")
        self.iconbitmap("./img/logo.ico")
        w, h = 400, 150
        utl_ven.centrar_ventana(self, w, h)
        
    def construirWidget(self):
        """Creacion y ubicacion de objetos en la ventana"""
        self.labelVersion = tk.Label(self, text = "Versión : 1.0")
        self.labelVersion.config(fg="#000000", font=("Roboto", 15), pady=10, width = 20)
        self.labelVersion.pack()
        
        self.labelVersion = tk.Label(self, text = "Fecha de versión : 1 de Febrero del 2024")
        self.labelVersion.config(fg="#000000", font=("Roboto", 15), pady=10, width = 40)
        self.labelVersion.pack()
        
        self.labelVersion = tk.Label(self, text = "Author : Oscar Julián Castillo")
        self.labelVersion.config(fg="#000000", font=("Roboto", 15), pady=10, width = 30)
        self.labelVersion.pack()
