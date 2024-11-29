"""Actualiza datos de la coleccion empleados"""

# Importar el cliente de pymongo
from step01_conexion import client

# Seleccionar la base de datos y colección
db = client.rrhh
coleccion = db.empleados

# Actualizar un solo documento
resultado = coleccion.update_one(
    {'nombre': 'Juan'},  # Filtro para seleccionar el documento
    {'$set': {'salario': 550.0}}  # Actualización a realizar
)
print("1) Actualizar un solo documento")
print(f"Documentos coincidentes: {resultado.matched_count}")
print(f"Documentos modificados: {resultado.modified_count}")

# Actualizar múltiples documentos
resultado = coleccion.update_many(
    {'edad': {'$gt': 30}},  # Filtro para seleccionar los documentos
    {'$set': {'salario': 750.0}}  # Actualización a realizar
)

print("2) Actualizar múltiples documentos")
print(f"Documentos coincidentes: {resultado.matched_count}")
print(f"Documentos modificados: {resultado.modified_count}")
