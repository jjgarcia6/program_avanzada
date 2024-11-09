# Solicitamos los números al usuario
n1 = input("Ingresa el primer número: ")
n2 = input("Ingresa el segundo número: ")

# Convertimos las entradas de texto a enteros
n1 = int(n1)
n2 = int(n2)

# Realizamos las operaciones matemáticas
suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2

# Creamos un mensaje formateado con los resultados
message = f"""
Resultados:
La suma es {suma}
La resta es {resta}
La multiplicación es {multi}
La división es {div}
"""

print(message)
