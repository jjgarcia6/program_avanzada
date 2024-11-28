"""Insertar múltiples registros en una tabla de SQLite con Python."""

from step00_database import conn

# Datos a insertar
empleados = [
    ('Juan', 'Pérez', 30, 500.0),
    ('Ana', 'García', 25, 600.0),
    ('Luis', 'Martínez', 40, 700.0),
    ('María', 'Rodríguez', 35, 550.0)
]

# Definir la sentencia SQL para insertar registros
INSERT_SQL = '''
    INSERT INTO empleados (nombre, apellido, edad, salario)
    VALUES (?, ?, ?, ?)
'''

# Conectar a la base de datos
with conn:
    cursor = conn.cursor()
    # Usar executemany para insertar múltiples registros
    cursor.executemany(INSERT_SQL, empleados)
