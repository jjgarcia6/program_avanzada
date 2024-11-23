"""Ejercicio Calculadora"""


def suma(a, b):
    """Funcion para sumar"""
    return a + b


def resta(a, b):
    """Funcion para restar"""
    return a - b


def multiplicacion(a, b):
    """Funcion para multiplicar"""
    return a * b


def division(a, b):
    """Funcion para dividir"""
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"


# Diccionario que mapea símbolos a funciones
operaciones = {
    '+': suma,
    '-': resta,
    '*': multiplicacion,
    '/': division
}

# Solicitar al usuario que elija una operación
operacion = input("Elige una operación (+, -, *, /): ")

# Solicitar al usuario que ingrese dos números
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Obtener la función correspondiente y calcular el resultado
resultado = operaciones[operacion](num1, num2)

# Mostrar el resultado
print("El resultado es:", resultado)
