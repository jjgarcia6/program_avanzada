# Función simple sin parámetros
def saludar():
    print("Hola mundo")


saludar()  # Llama a la función saludar y muestra "Hola mundo"

# Función con parámetros obligatorios


def saludarConNombre(name, lastname):
    print(f"Hola {name} {lastname}")


saludarConNombre("Jorge", "Hurtado")

# Función con parámetros opcionales (valor por defecto para 'lastname')
# 'lastname' tiene un valor por defecto


def saludarSoloNombre(name, lastname="Anonimo"):
    print(f"Hola {name} {lastname}")


# Parámetros pasados explícitamente
saludarConNombre(lastname="Hurtado", name="Jorge")
# 'lastname' toma el valor por defecto "Anonimo"
saludarSoloNombre(name="Jorge")

# Función que acepta un número variable de argumentos (*args)


def sum(*numbers):  # 'numbers' es una tupla que contiene todos los argumentos
    result = 0
    for number in numbers:  # Recorre todos los números y los suma
        result += number
    print(result)


sum(1, 2, 3)  # Llama a la función pasando tres números como argumentos

# Función que acepta un número variable de argumentos con nombre (**kwargs)


def get_product(**datos):  # 'datos' es un diccionario que contiene todos los argumentos con nombre
    # Accede a los valores usando las claves
    print(datos["name"], "$", datos["cost"])


# Llama a la función pasando argumentos con nombre
get_product(id="id", name="llave", cost=45)
