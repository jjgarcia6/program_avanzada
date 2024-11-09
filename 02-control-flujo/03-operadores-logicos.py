# Operadores lógicos: and, or, not

gas = False      # Variable que indica si hay gasolina
encendido = True  # Variable que indica si el motor está encendido
edad = 17        # Edad del usuario

# Ejemplo con el operador 'and' (Y)
if gas and encendido and edad > 17:
    print("Seguro")  # Se ejecuta solo si todas las condiciones son verdaderas

# Ejemplo con el operador 'not' (NO) y 'or' (O)
if not gas and (encendido or edad > 17):
    # Se ejecuta si 'gas' es False y cualquiera de las otras condiciones es verdadera
    print("Seguro")

# Ejemplo con el operador 'or' (O)
if gas or encendido:  # Si cualquiera de las dos condiciones es verdadera
    print("Puede funcionar")

# Operaciones de corto-circuito
# 'and' y 'or' en Python tienen corto-circuito:
# Si la primera condición ya es suficiente para determinar el resultado, las siguientes no se evalúan.

if gas and encendido:  # Si 'gas' es False, no se evalúa 'encendido', porque el resultado ya es falso
    print("Esto no se ejecutará.")

if encendido or edad > 18:  # Si 'encendido' es True, no se evalúa 'edad > 18', porque el resultado ya es verdadero
    print("Esto siempre se ejecutará.")
