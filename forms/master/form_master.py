#importacion de librerias tkiinter y util 
import tkinter as tk
from tkinter import font
from config import COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA
import util.util_imagenes as utl_img
import util.util_ventana as utl_ven
from forms.master.form_info_design import FormularioInfoDesign
from forms.master.form_sitio_construccion import FormularioSitioConstruccionDesign

class MasterPanel(tk.Tk):
    
    #constructor
    def __init__(self):
        """Creacion de la ventana general del sistema y con sus caracteristicas """
        super().__init__()
        
        #invocando las imagenes
        self.logo = utl_img.leer_imagen("./img/logo (1).png", (560, 136))
        self.perfil = utl_img.leer_imagen("./img/Perfil.png", (100, 100))
        self.img_sitio_construccion = utl_img.leer_imagen("./img/sitio_construccion.png", (400, 400))
        self.config_window()
        self.paneles()
        self.controles_barra_superior()
        self.controles_menu_lateral()
        self.control_cuerpo()
    
    def config_window(self):
        #self.ventana = tk.Tk() no es necesaria esta linea por que la clase ya ereda TK 
        self.title("Python GUI")
        self.iconbitmap("./img/logo.ico")
        w, h = 1024, 600 #self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()
        utl_ven.centrar_ventana(self, w, h)
        #self.ventana.geometry("%dx%d+0+0" % (w, h))
        #self.ventana.config(bg="#fcfcfc")
        #self.ventana.resizable(width=0, height=0) 
        
    def paneles(self):
        #crear paneles: barra superior, menu lateral y cuerpo principal
        self.barra_superior = tk.Frame(self, bg=COLOR_BARRA_SUPERIOR, height=50)
        self.barra_superior.pack(side=tk.TOP, fill="both")
        
        self.menu_lateral = tk.Frame(self, bg=COLOR_MENU_LATERAL, width=150)
        self.menu_lateral.pack(side=tk.LEFT, fill="both", expand=False)
        
        self.Cuerpo_Principal = tk.Frame(self, bg=COLOR_CUERPO_PRINCIPAL)
        self.Cuerpo_Principal.pack(side=tk.RIGHT, fill="both", expand=True)
        
    def controles_barra_superior(self):
        #Configuracion de la barra superior
        font_awesome = font.Font(family='FontAwesome', size=12)
        
        #Etiqueta de titulo 
        self.labelTitulo = tk.Label(self.barra_superior, text="Autodidacta")
        self.labelTitulo.config(fg="#fff", font=("Roboto", 15), bg = COLOR_BARRA_SUPERIOR, pady=10, width=15)
        self.labelTitulo.pack(side=tk.LEFT)
        
        #boton de menu lateral
        self.buttonMenuLateral = tk.Button(self.barra_superior, text="\uf0c9", font=font_awesome, command=self.toggle_panel, bd=0, bg=COLOR_BARRA_SUPERIOR, fg="white")
        
        self.buttonMenuLateral.pack(side=tk.LEFT)
        
        #etiqueta de informacion
        self.labelTitulo = tk.Label(self.barra_superior, text="servicio@autodidacta.mx")
        self.labelTitulo.config(fg="#fff", font=("Roboto", 10), bg = COLOR_BARRA_SUPERIOR, padx=10, width=20)
        self.labelTitulo.pack(side=tk.RIGHT)
        
    def controles_menu_lateral(self):
        """configuracion del menú lateral"""
        ancho_menu = 20
        alto_menu = 2
        font_awesome = font.Font(family='FontAwesome', size=15)
        
        #etiqueta de perfil
        self.labelPerfil = tk.Label(self.menu_lateral, image=self.perfil, bg=COLOR_MENU_LATERAL)
        self.labelPerfil.pack(side=tk.TOP, pady = 10)
        
        #boton del menu lateral
        self.buttonDashBoard = tk.Button(self.menu_lateral)
        self.buttonProfile = tk.Button(self.menu_lateral)
        self.buttonPicture = tk.Button(self.menu_lateral)
        self.buttonInfo = tk.Button(self.menu_lateral)
        self.buttonSettings = tk.Button(self.menu_lateral)
        
        button_info =[
            ("Dashboard","\uf109",self.buttonDashBoard, self.abrir_panel_en_construccion),
            ("Profile","\uf007",self.buttonProfile, self.abrir_panel_en_construccion),
            ("Picture","\uf03e",self.buttonPicture, self.abrir_panel_en_construccion),
            ("Info","\uf129",self.buttonInfo, self.abrir_panel_info),
            ("Serttings","\uf013",self.buttonSettings, self.abrir_panel_en_construccion)
        ]
        
        #ciclo para llenar las configuraciones de los diferentes botonews atravews de la tupla o diccionario
        for text, icon, button, comando in button_info:
            self.configurar_boton_menu(button, text, icon, font_awesome, ancho_menu, alto_menu, comando)
    
    def control_cuerpo(self):
        """Imagen en el cuerpo principal o area de trabajo"""
        label = tk.Label(self.Cuerpo_Principal, image=self.logo, bg = COLOR_CUERPO_PRINCIPAL)
        label.place(x=0, y=0, relwidth=1, relheight=1)
    
    def configurar_boton_menu(self, button, text, icon, font_awesome, ancho_menu, alto_menu, comando ):
        """Funcion para establecer los valores de los botones medui¿iantre a las variables de parametros que van ingresando en el for anterior que cicla la tupla o diccionario"""
        button.config(text=f" +{icon} {text}", anchor="w", font=font_awesome, bd=0, bg=COLOR_MENU_LATERAL, fg="white", width=ancho_menu, height=alto_menu, command = comando)
        button.pack(side=tk.TOP)
        #evento para detectar el maus en los botones 
        self.bind_hover_events(button)    
        
    def bind_hover_events(self, button):
        """Asociar eventos enter y leave con lña funcion dinamica"""
        button.bind("<Enter>", lambda event: self.on_enter(event, button))
        button.bind("<Leave>", lambda event: self.on_leave(event, button))
    
    def on_enter(self, event, button):
        """cambiar estilo al pasar el raton por encima"""
        button.config(bg=COLOR_MENU_CURSOR_ENCIMA, fg="white")
        
    def on_leave(self, event, button):
        """Restaurar el estilo al salir el raton del boton """
        button.config(bg=COLOR_MENU_LATERAL, fg="white")
        
    def toggle_panel(self):
        """Alterar la visiblidad del menu lateral si esta visible lo retira en la visibilidad y si no se encuentra visible, lo ajusta al lado derecho en el eje y para pocisionarlo """
        if self.menu_lateral.winfo_ismapped():
            self.menu_lateral.pack_forget()
        else:
            self.menu_lateral.pack(side=tk.LEFT, fill="y")
        
    def abrir_panel_info(seld):
        FormularioInfoDesign()
        
    def abrir_panel_en_construccion(self):
        self.limpiarPanel(self.Cuerpo_Principal)
        FormularioSitioConstruccionDesign(self.Cuerpo_Principal, self.img_sitio_construccion)
        
    def limpiarPanel(self, panel):
        """Funcion para Destrio todos los hijos de panel gracias al winfo _children que se le indique limpiando el panel que baya encontrando por eso se encientra en un bucle parea que se pueda hubicar otro panel diferente """
        for widget in panel.winfo_children():
            widget.destroy()