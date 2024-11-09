x = input("")

# Convertimos a diferentes tipos de datos
numero_entero = int(x)  # Convierte el string a un número entero
numero_flotante = float(x)  # Convierte el string a un número flotante
texto = str(x)  # Convierte el string a texto (aunque ya es texto)
valor_booleano = bool(x)  # Convierte el string a un valor booleano

print(f"Entrada original: {x}")
print(f"Como entero: {numero_entero}")
print(f"Como flotante: {numero_flotante}")
print(f"Como string: {texto}")
print(f"Como booleano: {valor_booleano}")

# Datos en Falsy -> "" 0 None

print(bool(""))  # Cadena vacía -> False
print(bool("0"))  # Cadena con un '0' -> True (no es vacío, es un string no vacío)
print(bool(None))  # None -> False (ningún valor asignado)
print(bool(" "))  # Espacio vacío -> True (es un string no vacío)
print(bool(0))  # Cero -> False (es el valor falso en números)
