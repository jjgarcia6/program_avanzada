# Importamos el módulo math, que contiene funciones matemáticas avanzadas.
import math

# Definimos diferentes tipos de números
numero = 2  # Un número entero
decimal = 1.2  # Un número flotante
imaginario = 2 + 2j  # Un número complejo

# Operaciones aritméticas básicas con el número
numero += 2  # Incrementamos 'numero' en 2 (equivalente a numero = numero + 2)

# Ejemplo de operaciones matemáticas simples
print(1 + 3)  # Suma
print(1 - 3)  # Resta
print(1 * 3)  # Multiplicación
print(1 / 3)  # División normal (float)
print(1 // 3)  # División entera (retorna solo la parte entera)
print(1 % 3)  # Módulo (resto de la división)
print(1 ** 3)  # Potencia

# Redondeo de un número decimal
print(round(1.7))  # Imprime 2 (redondeo al entero más cercano)
print(round(1.1))  # Imprime 1 (redondeo al entero más cercano)

# Valor absoluto de un número
print(abs(1.1))

# Redondeo hacia arriba (ceil)
print(math.ceil(1.1))  # Imprime 2 (redondeo hacia arriba)

# Redondeo hacia abajo (floor)
print(math.floor(1.9999999))  # Imprime 1 (redondeo hacia abajo)

# Verifica si un número es 'NaN' (Not a Number)
print(math.isnan(23))  # Imprime False (23 no es NaN)

# Potencia: Calcula 10 elevado a la potencia de 3
print(math.pow(10, 3))  # Imprime 1000.0 (10^3)

# Raíz cuadrada de un número
print(math.sqrt(9))  # Imprime 3.0
