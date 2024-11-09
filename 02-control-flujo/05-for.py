# Bucle 'for' con 'range()' para imprimir números del 0 al 4
for numero in range(5):
    print(numero)

# Buscar un número específico en un rango y usar 'break' para salir del bucle
buscar = 3
for numero in range(5):
    print(numero)
    if numero == buscar:
        # Se imprime si el número buscado se encuentra
        print("Encontrado", numero)
        break  # Sale del bucle cuando encuentra el número
else:
    print("No encontrado")  # Si no se encontró el número, se ejecuta esta parte

# Bucle 'for' para iterar sobre los caracteres de una cadena
for chart in "JEANNE":
    print(chart)

# Bucle 'for' anidados
for j in range(3):
    for k in range(2):
        print(f"{j}, {k}")

print("Bienvenido a la calculadora")
