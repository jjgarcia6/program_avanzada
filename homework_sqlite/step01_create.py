"""Creacion de unas tablas en una base de datos SQLite3 con with"""

# Importar la conexión a la base de datos
from step00_database import conn

# Definir la sentencia SQL para crear la tabla
create_tables_sql = [
    '''
    CREATE TABLE IF NOT EXISTS empleados (
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        apellido TEXT,
        edad INTEGER,
        salario REAL
    )
    '''
]

# Crear una conexión a la base de datos
with conn:
    cursor = conn.cursor()
    for sql in create_tables_sql:
        cursor.execute(sql)
