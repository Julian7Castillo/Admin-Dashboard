from tkinter import messagebox
from forms.master.form_master import MasterPanel
from forms.login.form_login_designer import FormLoginDesigner
from persistence.repository.auth_user_repository import AuthUserRepository
from persistence.models import Auth_User
import util.encoding_decoding as end_dec
from forms.register.form_Register import FormRegister

class FormLogin(FormLoginDesigner):
    
    def __init__(self):
        """Creacion de la ventana Login del sistema y con sus widgets e inicializacion de la sesion"""
        self.auth_repository = AuthUserRepository()
        super().__init__()

    def verificar(self):
        """verificacion de datos ern el formulario del login, consultando la informacion con la base de datos si el usuaio existe """
        #trae el usuario de la base de datos
        user_db: Auth_User = self.auth_repository.getUserByUserName(self.usuario.get())
        if(self.isUser(user_db)):
            self.isPassword(self.password.get(), user_db)
            
    def userRegister(self):
        FormRegister()
            
    def isUser(self, user: Auth_User):
        """Verificacion de que el usuario exista para ser registrado """
        status : bool = True
        if(user == None):
            status = False
            messagebox.showerror(message="El usuario no existe por favor registrese", title="Mensaje")
        return status
    
    def isPassword(self, password: str, user:Auth_User):
        """Valida la contraseña escrita en el formulario con la contraseña encriptada en la base de datos"""
        #la variable la contraseña des encriptadad del usaurio en la base de dato s
        b_password = end_dec.decrypt(user.password)
        #se compara la contraseña de la base de datos desencriptada y la contraseña que se uso en el login 
        if(password == b_password):
            # si son iguales destruye la ventana anterior y crrea la nueva iniciando sesion 
            self.destroy()
            MasterPanel()
        else:
            #En el caso de ser incortectas muestra uyn mensaje por pantalla 
            messagebox.showerror(message="La contraseña no es correcta ", title="Mensaje")
        