"""Select data from the table empleados."""
from step00_database import conn

SELECT_SQL = ''' SELECT * FROM empleados '''

# Consultar datos de la tabla
with conn:
    cursor = conn.cursor()
    cursor.execute(SELECT_SQL)
    empleados = cursor.fetchall()
    for empleado in empleados:
        print(empleado)
