import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD
import util.util_ventana as utl_ven
import util.util_imagenes as utl_img

class FormLoginDesigner(tk.Tk):

    def verificar(self):
        pass
    
    def userRegister(self):
        pass
        
    def __init__(self):
        """Creacion de la ventana Login del sistema y con sus widgets """
        super().__init__()
        
        #llamado de url de imagen para precargarla y evitar errores
        self.logo = utl_img.leer_imagen("./img/logo.png", (200, 200)) 
        
        #configuracion de la ventana 
        #self.ventana = tk.Tk() esta parte no es necesaria al ser una clase que hereda TK
        self.title("Inicio de sesión ")
        self.iconbitmap("./img/logo.ico")
        self.geometry("800x500")
        self.config(bg="#fcfcfc")
        self.resizable(width=0, height=0)        
        utl_ven.centrar_ventana(self, 800,500)
         
        #cre3acion de fram para el label de la imagen
        frame_logo = tk.Frame(self, bd=0, width=400, relief=tk.SOLID, padx=10, pady=10, bg="#3a7ff6")       
        frame_logo.pack(side="left", expand=tk.NO, fill=tk.BOTH)
        
        #insertar imagen en un label 
        label = tk.Label(frame_logo, image = self.logo, bg="#3a7ff6")
        label.place(x=0, y=0, relwidth=1, relheight=1)
        
        #frame para el formulario de inicio de sesion 
        frame_form = tk.Frame(self, bd=0, relief=tk.SOLID, bg="#fcfcfc")       
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)
        
        #frame y titulo para el titulo de inicio de sesion
        frame_form_top = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg="black")       
        frame_form_top.pack(side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text="Inicio de sesión", font=("Times", 30), fg="#666a88", bg="#fcfcfc", pady=50)
        title.pack(expand=tk.YES, fill=tk.BOTH)
        
        #frame para relleno
        frame_form_fil = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        frame_form_fil.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)
        
        #Label y campo de entrada para el usuario
        etiqueta_usuario = tk.Label(frame_form_fil, text="Usuario", font=("times", 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_usuario.pack(fill=tk.X, padx=20, pady=5)
        self.usuario = ttk.Entry(frame_form_fil, font=("times", 14))
        self.usuario.pack(fill=tk.X, padx=20, pady=10)
        
        #Label y campo de entrada para la contraseña
        etiqueta_usuario = tk.Label(frame_form_fil, text="Contraseña", font=("times", 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_usuario.pack(fill=tk.X, padx=20, pady=5)
        self.password = ttk.Entry(frame_form_fil, font=("times", 14))
        self.password.pack(fill=tk.X, padx=20, pady=10)
        self.password.config(show="*")
        
        #Boton para inicio sesión 
        inicio = tk.Button(frame_form_fil, text="Inciar sesión", font=("times", 14), bg="#3a7ff6", bd=0, fg="#fff", command=self.verificar)
        inicio.pack(fill=tk.X, padx=20, pady=20)
        inicio.bind("<Return>", (lambda event: self.verificar()))
        
        #Boton para Registrar usuarios
        registro = tk.Button(frame_form_fil, text="Registrar Usuario", font=("times", 15), bg="#fcfcfc", bd=0, fg="#3a7ff6", command=self.userRegister)
        registro.pack(fill=tk.X, padx=20, pady=20)
        registro.bind("<Return>", (lambda event: self.userRegister()))
        