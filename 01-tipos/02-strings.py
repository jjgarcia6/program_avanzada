nombre_docente = "Jorge Hurtado"
descripcion = """
Aqui podemos escribir
varias linea de codigo.
"""

print(len(descripcion))
print(len(nombre_docente))

print(nombre_docente[0])   # Primer carácter
print(nombre_docente[0:3])  # Subcadena desde el índice 0 hasta el 2
print(nombre_docente[6:])  # Subcadena desde el índice 6 hasta el final
print(nombre_docente[:5])  # Subcadena desde el inicio hasta el índice 4
print(nombre_docente[:])   # Copia completa de la cadena

nombre = "Jorge"
apellido = "Hurtado"

nombre_completo = nombre + " " + apellido   # Concatenación de cadenas
# Uso de f-strings para interpolación de variables
nombre_completo_2 = f"{nombre} {apellido}"
# También puedes incluir expresiones
nombre_completo_3 = f"{nombre[0]} {2 + 6}"

print(nombre_completo)
print(nombre_completo_2)
print(nombre_completo_3)

animal = "dragon azUL"
print(animal.upper())   # Convierte toda la cadena a mayúsculas
print(animal.lower())   # Convierte toda la cadena a minúsculas
print(animal.capitalize())  # Capitaliza solo la primera letra de la cadena
print(animal.title())   # Capitaliza la primera letra de cada palabra

print(animal.strip())   # Elimina los espacios al inicio y al final de la cadena
print(animal.lstrip())  # Elimina los espacios solo al inicio
print(animal.rstrip())  # Elimina los espacios solo al final


print(animal.strip().capitalize())  # Se puede encadenar funciones

print(animal.find("azUL"))  # Busca la posición de la subcadena "azUL"
print("azUL" in animal)     # Verifica si "azUL" está en la cadena
print("azUL" not in animal)  # Verifica si "azUL" no está en la cadena

print(animal[7:])  # Muestra la subcadena desde el índice 7 hasta el final

print(animal.replace("azUL", "red"))  # Reemplaza "azUL" por "red"
