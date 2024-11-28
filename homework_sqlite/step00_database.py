"""Crear la base de datos de Python con SQLite."""

import sqlite3

# Ruta de la base de datos
DB_PATH = 'homework_sqlite/rrhh.db'

# Crear una nueva conexión a la base de datos
conn = sqlite3.connect(DB_PATH)
