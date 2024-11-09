edad = 22

# Ejemplo 'if' y 'else'
if edad > 17:
    print("Puede ver la película")
else:
    print("No puedes entrar")

# Segundo ejemplo con 'if', 'elif' y 'else'
if edad > 54:
    print("Puede ver la película con descuento")
elif edad > 17:
    print("Puede ver la película")
else:
    print("No puedes entrar")

# Tercer ejemplo con el operador ternario
# Asignamos "Mayor" si la edad es mayor que 17, si no, "Menor"
mensaje = "Mayor" if edad > 17 else "Menor"

# Alternativa sin usar el operador ternario
if edad > 17:
    mensaje = "Mayor"
else:
    mensaje = "Menor"

print(mensaje)  # Imprime el resultado de la condición
