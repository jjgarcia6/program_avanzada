"""Eliminar datos de la tabla empleados"""

# Importar la conexión a la base de datos
from step00_database import conn

# Definir la sentencia SQL para eliminar registros
DELETE_SQL = '''
    DELETE FROM empleados
    WHERE nombre = 'Ana' AND apellido = 'García'
'''

# Eliminar datos de la tabla
with conn:
    cursor = conn.cursor()
    cursor.execute(DELETE_SQL)
