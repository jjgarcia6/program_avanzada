"""Programa que verifica si una palabra es palíndromo."""

# Variables
palabra_invertida = ""

# Entrada de datos
palabra = input("Ingrese una palabra:").lower()

# Proceso
for letra in palabra:
    palabra_invertida = letra + palabra_invertida

# Salida
if palabra == palabra_invertida:
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")
