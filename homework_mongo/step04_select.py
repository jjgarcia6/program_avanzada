"""Muestra los documentos de la colección empleados"""

# Importar el cliente de pymongo
from step01_conexion import client

# Seleccionar la base de datos y colección
db = client.rrhh
coleccion = db.empleados

# Uso del método find_one
print("1) Muestra un solo documento de colección empleados")
data_01 = coleccion.find_one({}, {'_id': 0})
print(data_01)

# Uso del método find
print("2) Muestra todos los documentos de la colección empleados")
data_02 = coleccion.find({}, {'_id': 0})
for registro in data_02:
    print(registro)

# Uso del método find_one con parámetros
print("3) Muestra un solo documento de la colección empleados cuando nombre = Pedro")
data_03 = coleccion.find_one({'nombre': 'Pedro'}, {'_id': 0})
print(data_03)

# Uso del método find con parámetros
print("4) Muestra todos los documentos de la colección empleados que cumplan con la \
condición, salario > 1200")
data_04 = coleccion.find({'salario': {"$gt": 1200}}, {'_id': 0})
for registro in data_04:
    print(registro)
