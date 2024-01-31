import sqlalchemy as db
from persistence.models import Auth_User
from sqlalchemy.orm import Session

class AuthUserRepository():
    
    def __init__(self):
        """inicializar la clase , constructore para conectarse al motor de la base de datos, usamos engine para el uso de ciertas funciones como getUserByUserName"""
        self.engine = db.create_engine('sqlite:///db/login.sqlite', echo=False, future=True)
        
    def getUserByUserName(self, user_name: str):
        """Obtener los usarios atraves el nombre de usuario para validar los datos del usuario"""
        user: Auth_User = None 
        with Session(self.engine) as session:
            #consulta al objeto Auth_User y lo filta por el nombre del usuario y se traera el primero 
            user = session.query(Auth_User).filter_by(username=user_name).first()
        #retornas los valores del usaurio si no se logra coenctar sera none o null 
        return user
    
    def insertUser(self, user: Auth_User):
        """insertar al usuario creando una sesion en el motor de base de datos abriendo la conexion para usar los objetos de la tabla en la base de datos por los objetos Auth_user """
        #agrergamos una session y agrega el objeto user y crea un commit para la autorizacion
        with Session(self.engine) as session:
            session.add(user)
            session.commit()