"""Elimina datos de la coleccion empleados"""

# Importar el cliente de pymongo
from step01_conexion import client

# Seleccionar la base de datos y colección
db = client.rrhh
coleccion = db.empleados

# Eliminar un solo documento
resultado = coleccion.delete_one(
    {'nombre': 'Juan'}  # Filtro para seleccionar el documento a eliminar
)

print("1) Eliminar un solo documento")
print(f"Documentos eliminados: {resultado.deleted_count}")

# Eliminar múltiples documentos
resultado = coleccion.delete_many(
    {'edad': {'$gt': 30}}  # Filtro para seleccionar los documentos a eliminar
)

print("2) Eliminar múltiples documentos")
print(f"Documentos eliminados: {resultado.deleted_count}")
