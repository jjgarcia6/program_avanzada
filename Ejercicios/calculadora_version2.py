"""Ejercicio de Aprendizaje"""

numero1 = int(input("Ingrese 1er numero: "))
numero2 = int(input("Ingrese 2do numero: "))

print("Seleccione la operacion + , - , * , /")
operacion = input()


def respuesta(op, num1, num2):
    """calculo de operaciones matematicas"""
    match op:
        case '+':
            resultado = num1 + num2
        case '-':
            resultado = num1 - num2
        case '*':
            resultado = num1 * num2
        case '/':
            if num2 != 0:
                resultado = num1 / num2
            else:
                resultado = "Error: División por cero"
        case _:
            resultado = "Operación no válida"
    return resultado


valor = respuesta(operacion, numero1, numero2)
print("El resultado es:", valor)
