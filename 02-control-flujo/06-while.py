# Bucle 'while' que duplica el número hasta que sea mayor o igual a 100
numero = 1
while numero < 100:
    print(numero)
    numero *= 2

# Bucle 'while' que sigue pidiendo comandos hasta que el usuario ingrese "salir"
comando = ""
while comando.lower() != "salir":
    comando = input('$ ')
    print(comando)

# Bucle 'while' que solicita comandos infinitamente (hasta que el programa se cierre)
# comando = ""
# while True:
#     comando = input('$ ')
#     print(comando)

# Bucle 'while' con 'break' para salir cuando el usuario ingresa "salir"
comando = ""
while True:
    comando = input('$ ')  # Solicita un comando al usuario
    print(comando)
    if comando.lower() == "salir":
        break
