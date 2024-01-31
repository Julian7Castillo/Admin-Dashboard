import tkinter as tk
from tkinter import ttk
import util.util_ventana as utl_ven
import util.util_imagenes as utl_img

class FormRegisterDesigner():
    
    def __init__(self):
        """Creacion de la ventana Login del sistema y con sus widgets """
        #super().__init__()
        
        #configuracion de la ventana 
        self.ventana = tk.Toplevel()
        self.ventana.title("Registro de usuarios")
        self.ventana.iconbitmap("./img/logo.ico")
        self.ventana.config(bg="#fcfcfc")
        self.ventana.resizable(width=0, height=0)        
        utl_ven.centrar_ventana(self.ventana, 600, 480)
         
        #llamado de url de imagen para precargarla y evitar errores
        logo = utl_img.leer_imagen("./img/logo.png", (200, 200)) 
        
        #cre3acion de fram para el label de la imagen
        frame_logo = tk.Frame(self.ventana, bd=0, width=250, relief=tk.SOLID, padx=10, pady=10, bg="#F87474")       
        frame_logo.pack(side="left", expand=tk.NO, fill=tk.BOTH)
        
        #insertar imagen en un label 
        label = tk.Label(frame_logo, image = logo, bg="#F87474")
        label.place(x=0, y=0, relwidth=1, relheight=1)
        
        #frame para el formulario de inicio de sesion 
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg="#fcfcfc")       
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)
        
        #frame y titulo para el titulo de inicio de sesion
        frame_form_top = tk.Frame(frame_form, height=30, bd=0, relief=tk.SOLID, bg="black")       
        frame_form_top.pack(side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text="Registro de usuarios", font=("Times", 30), fg="#666a88", bg="#fcfcfc", pady=30)
        title.pack(expand=tk.YES, fill=tk.BOTH)
        
        #frame para relleno
        frame_form_fil = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        frame_form_fil.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)
        
        #Label y campo de entrada para el usuario
        etiqueta_usuario = tk.Label(frame_form_fil, text="Usuario: ", font=("Times", 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_usuario.pack(fill=tk.X, padx=20, pady=5)
        self.usuario = ttk.Entry(frame_form_fil, font=("Times", 14))
        self.usuario.pack(fill=tk.X, padx=20, pady=10)
        
        #Label y campo de entrada para la contraseña
        etiqueta_contraseña = tk.Label(frame_form_fil, text="Contraseña: ", font=("Times", 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_contraseña.pack(fill=tk.X, padx=20, pady=5)
        self.password = ttk.Entry(frame_form_fil, font=("Times", 14))
        self.password.pack(fill=tk.X, padx=20, pady=10)
        self.password.config(show="*")
        
        #Label y campo de entrada para la conformacion de la contraseña
        etiqueta_confirmacion = tk.Label(frame_form_fil, text="Confirmación: ", font=("Times", 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_confirmacion.pack(fill=tk.X, padx=20, pady=5)
        self.confirmation = ttk.Entry(frame_form_fil, font=("Times", 14))
        self.confirmation.pack(fill=tk.X, padx=20, pady=10)
        self.confirmation.config(show="*")

        #Boton para Registrar usuarios
        register = tk.Button(frame_form_fil, text="Registrar", font=("times", 15), bg="#F87474", bd=0, fg="#fcfcfc", command=self.register)
        register.pack(fill=tk.X, padx=20, pady=10)
        register.bind("<Return>", (lambda event: self.register(self)))
        
        self.ventana.mainloop()
    
    def register():
        pass
    
