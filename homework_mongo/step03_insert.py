"""Insertar varios documentos en la colección empleados de la base de datos rrhh."""

# Importar el cliente de pymongo
from step01_conexion import client

# Seleccionar la base de datos y colección
db = client.rrhh
coleccion = db.empleados

# Lista de documentos a insertar
lista = [
    {"nombre": "Juan", "apellido": "Perez", "edad": 30, "salario": 1000},
    {"nombre": "Ana", "apellido": "Gomez", "edad": 25, "salario": 1200},
    {"nombre": "Pedro", "apellido": "Garcia", "edad": 35, "salario": 1100},
    {"nombre": "Maria", "apellido": "Rodriguez", "edad": 40, "salario": 1500}
]

# Insertar los documentos en la colección
coleccion.insert_many(lista)
