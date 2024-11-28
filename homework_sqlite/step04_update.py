"""Actualizar datos en la tabla empleados."""

# Importar la conexión a la base de datos
from step00_database import conn

# Definir las sentencias SQL para actualizar los datos
update_statements = [
    '''
    UPDATE empleados
    SET salario = 600.0
    WHERE nombre = 'Juan' AND apellido = 'Pérez'
    ''',
    '''
    UPDATE empleados
    SET salario = 750.0
    WHERE nombre = 'Ana' AND apellido = 'García'
    '''
]

# Conectar a la base de datos y ejecutar las actualizaciones
with conn:
    cursor = conn.cursor()
    for sql in update_statements:
        cursor.execute(sql)
