from forms.register.form_register_desingner import FormRegisterDesigner
from persistence.repository.auth_user_repository import AuthUserRepository
from persistence.models import Auth_User
from tkinter import messagebox
import util.encoding_decoding as end_dec
import tkinter as tk
#from forms.login.form_login import FormLogin

class FormRegister(FormRegisterDesigner):
    def __init__(self):
        self.auth_repository = AuthUserRepository()
        super().__init__()
        
    def register(self):
        """Registro de usuario pasando por las validadciones de la contraseñas sean iguales y que el usuario no exusta en la baser de datos """
        if(self.isConfirmationPassword()):
            user = Auth_User()
            user.username = self.usuario.get()
            user_db: Auth_User = self.auth_repository.getUserByUserName(self.usuario.get())
            
            if not (self.isUserRegister(user_db)):
                user.password = end_dec.encrypted(self.password.get())
                self.auth_repository.insertUser(user)
                messagebox.showinfo(message="Se Registro el usuario con exito", title="Mensaje")
                self.ventana.destroy()

    def isConfirmationPassword(self):
        """Funcion para validar que las contraseñas sean iguales y en el caso de que no se asi limpia los campos """
        status: bool = True
        if(self.password.get() != self.confirmation.get()):
            status = False
            messagebox.showerror( message = "Las contraseñas no coinciden Por favor verificar el registro", title="Mensaje")
            self.password.delete(0, tk.END)
            self.confirmation.delete(0, tk.END)
        return status
    
    def isUserRegister(self, user: Auth_User):
        """Funcion para validar si el usuario ya existe en la base de datos """
        status: bool = False
        if(user != None):
            status = True
            messagebox.showerror(message = "El usuario ya existe", title="Mensaje")
        return status