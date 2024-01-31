#motor para cpnectarnos con la base de datos 
#importamos la libreria sqlalchemy como el diminutico bd
import sqlalchemy as db
#importamos el script de los modelos como mod
import persistence.models as mod

#cree el motor engine con la estructura para conectarnos con la base de dato ds
engine = db.create_engine('sqlite:///db/login.sqlite', echo=True, future=True)

#levante los modelos que tenemos configurados 
mod.Base.metadata.create_all(engine)

#Necesita ejecutarse antes o no funcionanra las validaciones