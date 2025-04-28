## Ejercicios Prácticos de Python 4

# 4.1
# Pide dos números e indica cuál es mayor o si son iguales.
num1 = int(input("ingresa un numero: "))
num2 = int(input("ingresa un numero: "))
if num1 == num2 :
    print("Los numeros son iguales")
else:
    if num1>num2 :
        print(f"El numero {num1} es mayor")
    else:
        print(f"El numero {num2} es mayor")

# 4.2
# Solicita una edad y determina si la persona es menor de edad (menor a 18).
age = int(input(f"Ingresa tu edad: "))
if age >= 18 :
    print(f"Eres mayor de edad")
else:
    print("eres menor de edad")

# 4.3
# Escribe un programa que compare dos cadenas de texto e indique si son iguales o distintas.
tex1 = str(input("ingresa texto 1: "))
tex2 = str(input("ingresa texto 2: "))
if tex1 == tex2 :
    print("las dos cadenas de texto son iguales")
else:
    print("La dos cadenas de texto son diferentes")
