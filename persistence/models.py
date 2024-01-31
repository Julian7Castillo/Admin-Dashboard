from sqlalchemy import Column
from sqlalchemy import String, Integer
from sqlalchemy.orm import declarative_base

#inicializar la variable base
Base = declarative_base()

#mapeo de objetos relacionados
class Auth_User(Base):
    #nombre de la tabla
    __tablename__ ="auth_user"
    
    #campos de la tabla
    id = Column(Integer, primary_key = True, autoincrement=True)
    username = Column(String(150))
    password = Column(String(128))
    
    def __repr__(self):
        """solicitud de con el resultado"""
        return f'auth_user({self.username}, {self.password})'
    
    def __str__(self):
        """solicitud de con el resultado"""
        return self.username
    
    
