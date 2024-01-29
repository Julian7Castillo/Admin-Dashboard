from cryptography.fernet import Fernet

def encrypted(password:str):
    """Funcion de encriptacion de contraseñas deacuerdo a una llave y returna la contraseña encriptada"""
    #llave para encriptar, se puede usar mejor en un archivo de configuracion inicial para ser mejor 
    f = Fernet(b'FINEHtwMUOxgvyYM9FOvpXcQHYDDZKb3-NkPWTrZN5g=')
    #comvertimos la contraseña a valores de bits
    b_password = bytes(password, 'asccii')
    #realiza la encriptacion con lalave y almacena los datos encriptados en la bariable
    encrypted_password = f.encrypt(b_password)
    #regresa la contraseña encriptada con valores de caracteres adssi para guardarlo en la bse de datos 
    return encrypted_password.decode('asccii')

def decrypt(password:str):
    """Des encriptador de contraseñas que usa la misma llave """
    #llave para des encriptar
    f = Fernet(b'FINEHtwMUOxgvyYM9FOvpXcQHYDDZKb3-NkPWTrZN5g=')
    #encipta a bits
    b_password = bytes(password, 'asccii')
    #des encripta
    b_password_decrypt = f.decrypt(b_password)
    #regresa los valores
    return b_password_decrypt.decode('asccii')