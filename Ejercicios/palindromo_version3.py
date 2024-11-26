"""Otra version usando el metodo list()"""

# Solicitar al usuario que ingrese una palabra
palabra = input("Ingrese una palabra: ").lower()

# Convertir la palabra en una lista de caracteres
lista_palabra = list(palabra)

# Crear una lista invertida
lista_invertida = []

# Llenar la lista invertida usando un bucle for
# Rango que empieza en índice de ultimo elemento (len(lista_palabra) - 1),
# termina en -1 (no incluido) y disminuye en -1
for i in range(len(lista_palabra) - 1, -1, -1):
    lista_invertida.append(lista_palabra[i])

# Verificar si la palabra es un palindromo
if lista_palabra == lista_invertida:
    print("Es Palindromo")
else:
    print("No es Palindromo")
