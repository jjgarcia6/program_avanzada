"""Otra version de palindromo usando tecnica slicing"""

# Solicitar al usuario que ingrese una palabra
palabra = input("Ingrese una palabra: ").lower()

# Verificar si la palabra es un palindromo
if palabra == palabra[::-1]:  # Aqui se invierte la palabra(inicio:fin:paso)
    print("Es Palindromo")
else:
    print("No es Palindromo")
